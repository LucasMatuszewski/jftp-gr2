package com.myjavaworld.jftp;

import java.io.*;
import com.myjavaworld.ftp.FTPConstants;

public class ConnectionConfigurationTest extends BehaviorTestCase {
    public void testNewConnectionUsesPlainFtpAndPassiveMode() {
        RemoteHost host = new RemoteHost();
        assertEquals(21, host.getPort());
        assertTrue(host.isPassive());
        assertEquals(FTPConstants.USE_NO_SSL, host.getSSLUsage());
        assertFalse(host.isDataChannelUnencrypted());
        assertEquals(990, host.getImplicitSSLPort());
        assertEquals(0, host.getCommands().length);
    }

    public void testHostWhitespaceAndMissingCredentialsAreNormalized() {
        RemoteHost host = new RemoteHost("  localhost  ", null, null);
        assertEquals("localhost", host.getHostName());
        assertEquals("", host.getUser());
        assertEquals("", host.getPassword());
        host.setHostName(null);
        host.setAccount(null);
        assertEquals("", host.getHostName());
        assertEquals("", host.getAccount());
    }

    public void testInvalidPortsFallBackWhileCustomPortIsKept() {
        RemoteHost host = new RemoteHost();
        host.setPort(0);
        assertEquals(21, host.getPort());
        host.setPort(-1);
        assertEquals(21, host.getPort());
        host.setPort(2121);
        assertEquals(2121, host.getPort());
    }

    public void testLoginCommandsSkipBlankLinesAndPreserveOrderAndSpaces() {
        RemoteHost host = new RemoteHost();
        host.setCommands("TYPE I\r\n\r\n  \n SITE TEST \rNOOP\n");
        assertEquals(3, host.getCommands().length);
        assertEquals("TYPE I", host.getCommands()[0]);
        assertEquals(" SITE TEST ", host.getCommands()[1]);
        assertEquals("NOOP", host.getCommands()[2]);
        assertEquals("TYPE I\n SITE TEST \nNOOP\n", host.getCommandsAsString());
    }

    public void testFtpsConfigurationSurvivesSerialization() throws Exception {
        RemoteHost original = favorite("Synthetic FTPS");
        original.setSSLUsage(FTPConstants.USE_IMPLICIT_SSL);
        original.setImplicitSSLPort(2990);
        original.setDataChannelUnencrypted(true);
        ByteArrayOutputStream bytes = new ByteArrayOutputStream();
        try (ObjectOutputStream out = new ObjectOutputStream(bytes)) { out.writeObject(original); }
        RemoteHost restored;
        try (ObjectInputStream in = new ObjectInputStream(new ByteArrayInputStream(bytes.toByteArray()))) {
            restored = (RemoteHost) in.readObject();
        }
        assertEquals(original.getHostName(), restored.getHostName());
        assertEquals(2121, restored.getPort());
        assertEquals("synthetic", restored.getUser());
        assertEquals("test-only", restored.getPassword());
        assertEquals("account", restored.getAccount());
        assertFalse(restored.isPassive());
        assertEquals(FTPConstants.USE_IMPLICIT_SSL, restored.getSSLUsage());
        assertEquals(2990, restored.getImplicitSSLPort());
        assertTrue(restored.isDataChannelUnencrypted());
        assertEquals(files.toString(), restored.getInitialLocalDirectory());
        assertEquals("/synthetic", restored.getInitialRemoteDirectory());
        assertEquals("TYPE I\nNOOP\n", restored.getCommandsAsString());
    }
}
