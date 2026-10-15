package com.myjavaworld.jftp;

import java.nio.file.Files;

/** Persistence tests require the real Swing filesystem services used by JFTP. */
public abstract class PersistenceTestCase extends BehaviorTestCase {
    protected void setUp() throws Exception {
        super.setUp();
        assertEquals("Refuse to use another profile", PROFILE.resolve(".jftp/data").toFile(), JFTP.DATA_HOME);
        Files.deleteIfExists(dataFile("favorites.ser").toPath());
        Files.deleteIfExists(dataFile("preferences.ser").toPath());
        JFTP.prefs = JFTP.loadPreferences();
        JFTP.prefs.setCheckForUpdates(false);
        JFTP.prefs.setLocalDirectory(files.toString());
        JFTP.savePreferences(JFTP.prefs);
    }
}
