package com.myjavaworld.jftp;

import java.awt.Color;
import java.awt.Component;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.util.Arrays;
import javax.swing.BorderFactory;
import javax.swing.Icon;
import javax.swing.ImageIcon;
import javax.swing.JLabel;
import javax.swing.UIManager;
import javax.swing.border.Border;
import javax.swing.plaf.ColorUIResource;
import javax.swing.plaf.FontUIResource;

/** Small presentation layer over the saved look and feel; no preference writes. */
final class SygnityStyle {
    static final Color CYAN = new ColorUIResource(0x00AEEF);
    static final Color BLUE = new ColorUIResource(0x1E73BE);
    static final Color TEXT = new ColorUIResource(0x3A3A3A);
    static final Color WHITE = new ColorUIResource(Color.WHITE);
    static final Color SURFACE = new ColorUIResource(0xF9F9F9);
    static final Color SECTION = new ColorUIResource(0xF1F1F1);
    static final Color LINE = new ColorUIResource(0xDDE2E5);
    private static final Color SELECTION = new ColorUIResource(0xDDF3FD);

    private SygnityStyle() { }

    static void install() {
        FontUIResource font = new FontUIResource(Font.SANS_SERIF, Font.PLAIN, 13);
        String[] controls = {"Button", "ToggleButton", "CheckBox", "RadioButton", "Label",
                "MenuBar", "Menu", "MenuItem", "CheckBoxMenuItem", "RadioButtonMenuItem",
                "PopupMenu", "TabbedPane", "Table", "TableHeader", "List", "Tree",
                "ComboBox", "TextField", "PasswordField", "FormattedTextField",
                "ToolTip", "ProgressBar", "TitledBorder"};
        for (String control : controls) {
            UIManager.put(control + ".font", font);
            UIManager.put(control + ".foreground", TEXT);
        }
        colors(WHITE, "Table.background", "List.background", "Tree.background",
                "TextField.background", "PasswordField.background", "ComboBox.background",
                "ToolBar.background", "MenuBar.background", "Menu.background",
                "MenuItem.background", "PopupMenu.background", "Viewport.background");
        colors(SURFACE, "Panel.background", "ScrollPane.background", "TabbedPane.background",
                "SplitPane.background", "ToolTip.background");
        colors(SECTION, "Button.background", "ToggleButton.background", "TableHeader.background",
                "ScrollBar.background", "ProgressBar.background", "control");
        colors(TEXT, "textText", "controlText", "Table.selectionForeground",
                "List.selectionForeground", "Tree.selectionForeground", "TextField.selectionForeground",
                "Menu.selectionForeground", "MenuItem.selectionForeground",
                "ProgressBar.selectionForeground", "ProgressBar.selectionBackground");
        colors(SELECTION, "Table.selectionBackground", "List.selectionBackground",
                "Tree.selectionBackground", "TextField.selectionBackground",
                "Menu.selectionBackground", "MenuItem.selectionBackground", "TabbedPane.selected");
        colors(BLUE, "Button.focus", "ToggleButton.focus", "TabbedPane.focus",
                "Tree.selectionBorderColor", "TitledBorder.titleColor");
        colors(CYAN, "ProgressBar.foreground", "TabbedPane.selectHighlight");
        colors(LINE, "Table.gridColor", "Separator.foreground", "SplitPane.shadow",
                "SplitPane.darkShadow", "TabbedPane.shadow", "TabbedPane.darkShadow",
                "ScrollBar.thumb", "ScrollBar.thumbShadow", "ScrollBar.thumbDarkShadow");
        colors(WHITE, "SplitPane.highlight", "ScrollBar.thumbHighlight",
                "TabbedPane.highlight", "TabbedPane.borderHightlightColor");
        UIManager.put("SplitPane.dividerSize", 6);
        UIManager.put("TableHeader.cellBorder", BorderFactory.createCompoundBorder(
                BorderFactory.createMatteBorder(0, 0, 1, 1, LINE),
                BorderFactory.createEmptyBorder(6, 8, 6, 8)));
        // Metal's default gradient otherwise paints over the supplied surface color.
        UIManager.put("Button.gradient", Arrays.asList(0f, 0f, SECTION, SECTION, SECTION));
        UIManager.put("ToggleButton.gradient", Arrays.asList(0f, 0f, SECTION, SECTION, SECTION));
        UIManager.put("MenuBar.gradient", Arrays.asList(0f, 0f, WHITE, WHITE, WHITE));
    }

    private static void colors(Color value, String... keys) {
        for (String key : keys) { UIManager.put(key, value); }
    }

    static Border statusCellBorder() {
        return BorderFactory.createCompoundBorder(
                BorderFactory.createMatteBorder(0, 1, 0, 0, LINE),
                BorderFactory.createEmptyBorder(4, 8, 4, 8));
    }

    static JLabel logo() {
        final ImageIcon image = new ImageIcon(SygnityStyle.class.getResource("/images/sygnity-logo.png"));
        JLabel label = new JLabel(new Icon() {
            public int getIconWidth() { return 120; }
            public int getIconHeight() { return 36; }
            public void paintIcon(Component component, Graphics graphics, int x, int y) {
                Graphics2D g = (Graphics2D) graphics.create();
                try {
                    g.setRenderingHint(RenderingHints.KEY_INTERPOLATION, RenderingHints.VALUE_INTERPOLATION_BICUBIC);
                    g.drawImage(image.getImage(), x, y, getIconWidth(), getIconHeight(), component);
                } finally { g.dispose(); }
            }
        });
        label.getAccessibleContext().setAccessibleName("Sygnity");
        label.setFocusable(false);
        label.setBorder(BorderFactory.createEmptyBorder(0, 16, 0, 4));
        return label;
    }
}
