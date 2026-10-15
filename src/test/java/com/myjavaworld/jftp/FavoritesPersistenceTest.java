package com.myjavaworld.jftp;

import java.io.*;
import java.nio.file.Files;
import java.util.*;

public class FavoritesPersistenceTest extends PersistenceTestCase {
    public void testSavedFavoritesCanBeReadByAnotherJvm() throws Exception {
        FavoritesManager.addFavorite(favorite("Across JVM"));
        readInAnotherJvm("read-favorites");
    }

    public void testFirstUseStartsEmpty() throws Exception {
        assertTrue(FavoritesManager.getFavorites().isEmpty());
    }

    public void testAddingFavoritesPreservesOrderAndConnectionData() throws Exception {
        FavoritesManager.addFavorite(favorite("First"));
        FavoritesManager.addFavorite(favorite("Second"));
        List loaded = FavoritesManager.getFavorites();
        assertEquals(2, loaded.size());
        RemoteHost first = (RemoteHost) loaded.get(0);
        assertEquals("First", first.getName());
        assertEquals("Second", ((RemoteHost) loaded.get(1)).getName());
        assertEquals("127.0.0.1", first.getHostName());
        assertEquals(2121, first.getPort());
        assertEquals("test-only", first.getPassword());
        assertEquals(files.toString(), first.getInitialLocalDirectory());
        assertEquals("/synthetic", first.getInitialRemoteDirectory());
        assertEquals("TYPE I\nNOOP\n", first.getCommandsAsString());
        assertFalse(first.isPassive());
    }

    public void testEditingAndRemovingArePersisted() throws Exception {
        FavoritesManager.saveFavorites(new ArrayList<RemoteHost>(Arrays.asList(favorite("First"), favorite("Second"))));
        List loaded = FavoritesManager.getFavorites();
        RemoteHost changed = (RemoteHost) loaded.get(1);
        changed.setName("Edited"); changed.setPort(2021);
        loaded.remove(0);
        FavoritesManager.saveFavorites(loaded);
        List reopened = FavoritesManager.getFavorites();
        assertEquals(1, reopened.size());
        assertEquals("Edited", ((RemoteHost) reopened.get(0)).getName());
        assertEquals(2021, ((RemoteHost) reopened.get(0)).getPort());
    }

    public void testNullAndEmptySaveClearExistingFavorites() throws Exception {
        FavoritesManager.addFavorite(favorite("First"));
        FavoritesManager.saveFavorites(null);
        assertTrue(FavoritesManager.getFavorites().isEmpty());
        FavoritesManager.addFavorite(favorite("Second"));
        FavoritesManager.saveFavorites(new ArrayList());
        assertTrue(FavoritesManager.getFavorites().isEmpty());
    }

    public void testLegacyUnencryptedListCanBeReadRepeatedly() throws Exception {
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(dataFile("favorites.ser")))) {
            out.writeObject(new ArrayList<RemoteHost>(Arrays.asList(favorite("Legacy"))));
        }
        assertEquals("Legacy", ((RemoteHost) FavoritesManager.getFavorites().get(0)).getName());
        assertEquals("Legacy", ((RemoteHost) FavoritesManager.getFavorites().get(0)).getName());
    }

    public void testDamagedFavoritesReportIoFailureAndKeepOriginalBytes() throws Exception {
        byte[] damaged = new byte[] {1, 2, 3, 4, 5};
        Files.write(dataFile("favorites.ser").toPath(), damaged);
        try { FavoritesManager.getFavorites(); fail("Expected damaged-file error"); }
        catch (IOException expected) { /* Existing public failure contract. */ }
        assertTrue(Arrays.equals(damaged, Files.readAllBytes(dataFile("favorites.ser").toPath())));
    }
}
