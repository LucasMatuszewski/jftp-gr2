package com.myjavaworld.jftp;

import java.awt.Rectangle;
import java.nio.file.Files;
import java.util.*;
import com.myjavaworld.ftp.FTPConstants;

public class PreferencesPersistenceTest extends PersistenceTestCase {
    public void testPreferencesCanBeReadByAnotherJvm() throws Exception {
        JFTPPreferences prefs = JFTP.loadPreferences();
        prefs.setEmail("across-jvm@example.invalid");
        prefs.setTimeout(12345);
        JFTP.savePreferences(prefs);
        readInAnotherJvm("read-preferences");
    }

    public void testFirstUseCreatesUsableDefaults() throws Exception {
        Files.delete(dataFile("preferences.ser").toPath());
        JFTPPreferences prefs = JFTP.loadPreferences();
        assertTrue(dataFile("preferences.ser").isFile());
        assertTrue(prefs.isPassive());
        assertEquals(FTPConstants.TYPE_BINARY, prefs.getDefaultTransferType());
        assertEquals(FTPConstants.USE_NO_SSL, prefs.getSSLUsage());
        assertEquals(Integer.valueOf(FTPConstants.TYPE_ASCII), prefs.getTransferTypes().get("TXT"));
    }

    public void testConnectionAndTransferSettingsSurviveReload() throws Exception {
        JFTPPreferences prefs = JFTP.loadPreferences();
        prefs.setTimeout(12345); prefs.setBufferSize(32768); prefs.setPassive(false);
        prefs.setDefaultTransferType(FTPConstants.TYPE_ASCII);
        Map<String, Integer> types = new TreeMap<String, Integer>();
        types.put("DATA", FTPConstants.TYPE_BINARY);
        prefs.setTransferTypes(types);
        JFTP.savePreferences(prefs);
        JFTPPreferences loaded = JFTP.loadPreferences();
        assertEquals(12345, loaded.getTimeout());
        assertEquals(32768, loaded.getBufferSize());
        assertFalse(loaded.isPassive());
        assertEquals(FTPConstants.TYPE_ASCII, loaded.getDefaultTransferType());
        assertEquals(types, loaded.getTransferTypes());
    }

    public void testUiLocaleDirectoryAndUpdateChoiceSurviveReload() throws Exception {
        JFTPPreferences prefs = JFTP.loadPreferences();
        prefs.setLocale(Locale.GERMANY); prefs.setLocalDirectory(files.toString());
        prefs.setWindowBounds(new Rectangle(30, 40, 900, 600));
        prefs.setCheckForUpdates(false);
        JFTP.savePreferences(prefs);
        JFTPPreferences loaded = JFTP.loadPreferences();
        assertEquals(Locale.GERMANY, loaded.getLocale());
        assertEquals(files.toString(), loaded.getLocalDirectory());
        assertEquals(new Rectangle(30, 40, 900, 600), loaded.getWindowBounds());
        assertFalse(loaded.getCheckForUpdates());
    }

    public void testCertificateAndProxyConfigurationSurvivesWithoutOpeningStores() throws Exception {
        JFTPPreferences prefs = JFTP.loadPreferences();
        String store = files.resolve("synthetic.jks").toString();
        prefs.setServerCertificateStore(store); prefs.setClientCertificateStore(store);
        prefs.setServerCertificateStorePassword("synthetic".toCharArray());
        prefs.setClientCertificateStorePassword("client-only".toCharArray());
        prefs.setSSLUsage(FTPConstants.USE_IMPLICIT_SSL); prefs.setImplicitSSLPort(2990);
        prefs.setUseProxy(true); prefs.setProxyHost("127.0.0.1"); prefs.setProxyPort(1081);
        JFTP.savePreferences(prefs);
        JFTPPreferences loaded = JFTP.loadPreferences();
        assertEquals(store, loaded.getServerCertificateStore());
        assertEquals(store, loaded.getClientCertificateStore());
        assertEquals("synthetic", new String(loaded.getServerCertificateStorePassword()));
        assertEquals("client-only", new String(loaded.getClientCertificateStorePassword()));
        assertEquals(FTPConstants.USE_IMPLICIT_SSL, loaded.getSSLUsage());
        assertEquals(2990, loaded.getImplicitSSLPort());
        assertTrue(loaded.isUseProxy());
        assertEquals("127.0.0.1", loaded.getProxyHost());
        assertEquals(1081, loaded.getProxyPort());
    }

    public void testSecondSaveReplacesPreviousValues() throws Exception {
        JFTPPreferences prefs = JFTP.loadPreferences();
        prefs.setEmail("first@example.invalid"); JFTP.savePreferences(prefs);
        prefs = JFTP.loadPreferences();
        prefs.setEmail("second@example.invalid"); JFTP.savePreferences(prefs);
        assertEquals("second@example.invalid", JFTP.loadPreferences().getEmail());
    }

    public void testDamagedPreferencesCurrentlyFallBackWithoutOverwriting() throws Exception {
        byte[] damaged = new byte[] {1, 2, 3, 4, 5};
        Files.write(dataFile("preferences.ser").toPath(), damaged);
        JFTPPreferences loaded = JFTP.loadPreferences();
        assertNotNull(loaded);
        assertEquals(FTPConstants.TYPE_BINARY, loaded.getDefaultTransferType());
        assertTrue(Arrays.equals(damaged, Files.readAllBytes(dataFile("preferences.ser").toPath())));
    }
}
