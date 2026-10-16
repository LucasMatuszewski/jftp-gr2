package com.myjavaworld.jftp;

import java.awt.Component;
import java.awt.Dimension;
import java.awt.image.BufferedImage;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import javax.imageio.ImageIO;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.SwingUtilities;

/** Presentation contracts: decorative branding must not replace any action. */
public class SygnityAppearanceTest extends BehaviorTestCase {
    public void testOriginalToolbarActionsRemainInOrder() throws Exception {
        onEdt(() -> {
            JFTPToolBar toolbar = new JFTPToolBar(null);
            List<String> actions = new ArrayList<String>();
            for (Component component : toolbar.getComponents()) {
                if (component instanceof JButton) {
                    JButton button = (JButton) component;
                    assertNotNull("Original icon", button.getIcon());
                    assertNotNull("Original tooltip", button.getToolTipText());
                    for (java.awt.event.ActionListener listener : button.getActionListeners()) {
                        actions.add(listener.getClass().getSimpleName());
                    }
                }
            }
            assertEquals(Arrays.asList("NewSessionAction", "ConnectAction", "DisconnectAction",
                    "ReconnectAction", "DownloadAction", "UploadAction", "AbortAction",
                    "NewLocalFileAction", "NewLocalDirectoryAction", "ChangeLocalDirectoryAction",
                    "RenameLocalFileAction", "DeleteLocalFileAction", "NewRemoteFileAction",
                    "NewRemoteDirectoryAction", "ChangeRemoteDirectoryAction", "RenameRemoteFileAction",
                    "DeleteRemoteFileAction", "ManageFavoritesAction", "ManageCertificatesAction",
                    "DisplayHelpFromSource"), actions);
        });
    }

    public void testDecorativeLogoIsVisibleAtRightWithoutReplacingButtons() throws Exception {
        onEdt(() -> {
            JFTPToolBar toolbar = new JFTPToolBar(null);
            JLabel logo = null;
            int buttons = 0;
            for (Component component : toolbar.getComponents()) {
                if (component instanceof JButton) { buttons++; }
                if (component instanceof JLabel
                        && "Sygnity".equals(component.getAccessibleContext().getAccessibleName())) {
                    logo = (JLabel) component;
                }
            }
            assertEquals("All existing toolbar buttons", 20, buttons);
            assertNotNull("Sygnity wordmark in the toolbar", logo);
            assertNotNull("Wordmark loaded from runtime resources", logo.getIcon());
            assertFalse("Decorative logo must not join keyboard navigation", logo.isFocusable());
            assertTrue("Compact wordmark", logo.getIcon().getIconHeight() <= 40);
            toolbar.setSize(new Dimension(1100, toolbar.getPreferredSize().height));
            toolbar.doLayout();
            assertTrue("Logo aligned to right edge", logo.getX() > 900);
            int logoLeft = logo.getX();
            for (Component component : toolbar.getComponents()) {
                if (component instanceof JButton) {
                    assertTrue("No button overlaps logo", component.getX() + component.getWidth() <= logoLeft);
                }
            }
        });
    }

    public void testPackagedWordmarkRetainsOriginalAspectRatioAndTransparency() throws Exception {
        java.net.URL url = getClass().getResource("/images/sygnity-logo.png");
        assertNotNull("Logo must be on the runtime classpath", url);
        BufferedImage image = ImageIO.read(url);
        assertNotNull(image);
        assertEquals("Original 1600:480 aspect ratio", image.getWidth() * 3, image.getHeight() * 10);
        assertTrue("Transparent logo background", image.getColorModel().hasAlpha());
    }

    private static void onEdt(Runnable check) throws Exception {
        try {
            SwingUtilities.invokeAndWait(check);
        } catch (java.lang.reflect.InvocationTargetException failure) {
            if (failure.getCause() instanceof Error) { throw (Error) failure.getCause(); }
            throw failure;
        }
    }
}
