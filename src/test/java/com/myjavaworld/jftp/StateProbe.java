package com.myjavaworld.jftp;

import java.nio.file.*;
import java.util.*;

/** Separate-process persistence checks and an offline synthetic desktop profile. */
public class StateProbe {
    public static void main(String[] args) throws Exception {
        if (args.length != 1) { throw new IllegalArgumentException("Expected probe operation"); }
        if ("prepare-desktop".equals(args[0])) {
            Path profile = Paths.get(System.getProperty("user.home")).toAbsolutePath().normalize();
            String requested = System.getProperty("jftp.qa.home");
            if (requested == null || !profile.equals(Paths.get(requested).toAbsolutePath().normalize())) {
                throw new IllegalArgumentException("Set user.home and jftp.qa.home to the same new synthetic directory");
            }
            if (Files.exists(profile.resolve(".jftp"))) {
                throw new IllegalArgumentException("Refuse to replace an existing profile");
            }
            Path files = Files.createDirectories(profile.resolve("synthetic-files"));
            Files.write(files.resolve("report.txt"), Arrays.asList("synthetic QA data"));
            Files.write(files.resolve("image.csv"), Arrays.asList("id,value", "1,synthetic"));
            Files.createDirectory(files.resolve("folder"));
            JFTPPreferences prefs = JFTP.loadPreferences();
            prefs.setLocale(Locale.ENGLISH);
            prefs.setLocalDirectory(files.toString());
            prefs.setCheckForUpdates(false);
            prefs.setUseProxy(false);
            JFTP.savePreferences(prefs);
            System.out.println("Offline synthetic profile prepared: " + profile);
        } else if ("read-favorites".equals(args[0])) {
            List favorites = FavoritesManager.getFavorites();
            require(favorites.size() == 1, "Favorite count");
            RemoteHost host = (RemoteHost) favorites.get(0);
            require("Across JVM".equals(host.getName()), "Favorite name");
            require(host.getPort() == 2121, "Favorite port");
            require("test-only".equals(host.getPassword()), "Favorite credential");
            require("TYPE I\nNOOP\n".equals(host.getCommandsAsString()), "Favorite commands");
        } else if ("read-preferences".equals(args[0])) {
            JFTPPreferences prefs = JFTP.loadPreferences();
            require("across-jvm@example.invalid".equals(prefs.getEmail()), "Preference email");
            require(prefs.getTimeout() == 12345, "Preference timeout");
        } else { throw new IllegalArgumentException("Unknown operation: " + args[0]); }
    }

    private static void require(boolean condition, String message) {
        if (!condition) { throw new AssertionError(message); }
    }
}
