package com.myjavaworld.jftp;

import java.nio.file.*;
import java.nio.file.attribute.*;
import java.util.*;
import java.util.regex.Pattern;
import com.myjavaworld.util.DateFilter;
import com.myjavaworld.util.RegexFilter;

public class LocalFilteringTest extends BehaviorTestCase {
    private LocalFile file(String name, long modified) throws Exception {
        Path path = Files.write(files.resolve(name), new byte[] {1, 2, 3});
        Files.setLastModifiedTime(path, FileTime.fromMillis(modified));
        return new LocalFile(path.toFile());
    }

    public void testDefaultFilterKeepsFilesAndDirectories() throws Exception {
        assertTrue(new LocalFileFilter().accept(file("report.txt", 100000)));
        assertTrue(new LocalFileFilter().accept(new LocalFile(Files.createDirectory(files.resolve("folder")).toFile())));
    }

    public void testListingIncludesMatchingFilesAndKeepsNavigationDirectories() throws Exception {
        file("report.txt", 100000); file("image.png", 100000);
        Files.createDirectory(files.resolve("folder"));
        LocalFile[] listed = new LocalFile(files.toFile()).list(new LocalFileFilter(new RegexFilter(".*\\.txt", 0), null));
        Set<String> names = new TreeSet<String>();
        for (LocalFile entry : listed) { names.add(entry.getName()); }
        assertEquals(new TreeSet<String>(Arrays.asList("report.txt", "folder")), names);
    }

    public void testRegexCaseSensitivityIsUserSelectable() throws Exception {
        LocalFile upper = file("REPORT.TXT", 100000);
        assertFalse(new LocalFileFilter(new RegexFilter(".*\\.txt", 0), null).accept(upper));
        assertTrue(new LocalFileFilter(new RegexFilter(".*\\.txt", Pattern.CASE_INSENSITIVE), null).accept(upper));
    }

    public void testDateRangeIncludesBothBoundariesAndRejectsOutside() throws Exception {
        LocalFileFilter filter = new LocalFileFilter(null, new DateFilter(new Date(100000), new Date(200000)));
        assertFalse(filter.accept(file("before.txt", 98000)));
        assertTrue(filter.accept(file("start.txt", 100000)));
        assertTrue(filter.accept(file("end.txt", 200000)));
        assertFalse(filter.accept(file("after.txt", 202000)));
    }

    public void testNameAndDateMustBothMatch() throws Exception {
        LocalFileFilter filter = new LocalFileFilter(new RegexFilter(".*\\.txt", 0), new DateFilter(new Date(100000), null));
        assertTrue(filter.accept(file("recent.txt", 200000)));
        assertFalse(filter.accept(file("old.txt", 98000)));
        assertFalse(filter.accept(file("recent.png", 200000)));
    }

    public void testExclusionInvertsFileMatchButKeepsDirectories() throws Exception {
        LocalFileFilter filter = new LocalFileFilter(new RegexFilter(".*\\.txt", 0), null, true, true);
        assertFalse(filter.accept(file("report.txt", 100000)));
        assertTrue(filter.accept(file("image.png", 100000)));
        assertTrue(filter.accept(new LocalFile(Files.createDirectory(files.resolve("folder.txt")).toFile())));
    }

    public void testHiddenAttributeParticipatesInInclusionAndExclusion() throws Exception {
        LocalFile hidden = file(".synthetic-hidden.txt", 100000);
        DosFileAttributeView dos = Files.getFileAttributeView(hidden.getFile().toPath(), DosFileAttributeView.class);
        if (dos != null) { dos.setHidden(true); }
        assertTrue("Fixture must really be hidden", hidden.isHidden());
        assertFalse(new LocalFileFilter(null, null, false, false).accept(hidden));
        assertTrue(new LocalFileFilter(null, null, true, false).accept(hidden));
        assertTrue(new LocalFileFilter(null, null, false, true).accept(hidden));
    }
}
