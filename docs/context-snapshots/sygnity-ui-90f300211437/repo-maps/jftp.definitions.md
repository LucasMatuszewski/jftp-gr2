# Repository map export

- Implementation: rust
- Examined source: "/tmp/jftp-ui-runtime/snapshot/source"
- Examined revision: null; dirty working copy: None
- Candidates seen: 192
- Files selected / parsed: 191 / 191
- Definitions found / selected: 1642 / 1642
- Captured definitions omitted: 0
- Selection mode / rendering: all-definitions / compact
- Requested coverage: none
- Requested maximum definitions: none
- Effective maximum definitions: 1642
- Actual captured-definition coverage: 100%
- Selection limit reached: no
- Declaration snippets clipped: 0
- Map budget: 300000 estimated tokens
- Truncated: no; exclusions, unsupported files and parse failures still limit coverage
- Skipped entries / parse failures: 1 / 0
- Original generation wall time: 0.246 seconds (measured subprocess wall time)
- Raw content: 100542 Unicode characters, 100542 UTF-8 bytes, approximately 25136 tokens
- Whole annotated report: approximately 25511 tokens
- Token estimator: ceil(Unicode characters / 4); a size estimate, not a model tokenizer
- Raw map SHA-256: 11837a9a55912d7173fa4727668ebd5e8f00bdb45a65cc6ac75826b8da6f26bd
- Evidence sidecars: "definitions/jftp.definitions.raw.md", "definitions/jftp.definitions.meta.json", "definitions/jftp.definitions.inventory.json"

Generation status complete means the selected map was published, not that every repository file or relationship was analyzed. Read the sidecars for scope, skips, parser failures and the original working-copy fingerprint.

---

# Repository map

## src/main/java/com/myjavaworld/gui/DateCellRenderer.java

L31: public class DateCellRenderer extends MTableCellRenderer {
L61: @Override
L62: public Component getTableCellRendererComponent(JTable table, Object value,
L63: boolean isSelected, boolean hasFocus, int row, int col) {

## src/main/java/com/myjavaworld/gui/DefaultLargeTheme.java

L29: public class DefaultLargeTheme extends DefaultTheme {
L40: @Override
L41: public String getName() {
L45: @Override
L46: public FontUIResource getControlTextFont() {
L50: @Override
L51: public FontUIResource getSystemTextFont() {
L55: @Override
L56: public FontUIResource getUserTextFont() {
L60: @Override
L61: public FontUIResource getMenuTextFont() {
L65: @Override
L66: public FontUIResource getWindowTitleFont() {
L70: @Override
L71: public FontUIResource getSubTextFont() {

## src/main/java/com/myjavaworld/gui/DefaultTheme.java

L30: public class DefaultTheme extends DefaultMetalTheme {
L41: @Override
L42: public String getName() {
L46: @Override
L47: public FontUIResource getControlTextFont() {
L51: @Override
L52: public FontUIResource getSystemTextFont() {
L56: @Override
L57: public FontUIResource getUserTextFont() {
L61: @Override
L62: public FontUIResource getMenuTextFont() {
L66: @Override
L67: public FontUIResource getWindowTitleFont() {
L71: @Override
L72: public FontUIResource getSubTextFont() {

## src/main/java/com/myjavaworld/gui/EditPopupMenu.java

L32: public class EditPopupMenu extends MPopupMenu implements ActionListener {
L58: public static synchronized EditPopupMenu getInstance() {
L72: public void setTextComponent(MTextComponent textComponent) {
L89: public MTextComponent getTextCompoent() {
L99: @Override
L100: public void show(Component invoker, int x, int y) {
L110: public void actionPerformed(ActionEvent evt) {
L132: private void initComponents() {

## src/main/java/com/myjavaworld/gui/GUIUtil.java

L39: public class GUIUtil {
L53: public static Point getCenterPointRelativeToScreen(Dimension size) {
L59: public static boolean isSystemLookAndFeel() {
L67: public static KeyStroke getHelpKeyStroke() {
L75: public static int getDeleteKey() {
L79: public static void showInformation(Component parent, String info) {
L84: public static void showInformation(Component parent, String info,
L85: boolean format) {
L90: public static void showInformation(Component parent, String title,
L91: String info) {
L95: public static void showInformation(Component parent, String title,
L96: String info, boolean format) {
L104: public static int showConfirmation(Component parent, String message) {
L109: public static int showConfirmation(Component parent, String message,
L110: boolean format) {
L115: public static int showConfirmation(Component parent, String title,
L116: String message) {
L120: public static int showConfirmation(Component parent, String title,
L121: String message, boolean format) {
L129: public static void showError(Component parent, String error) {
L134: public static void showError(Component parent, String title, String error) {
L138: public static void showError(Component parent, String title, String error,
L139: boolean format) {
L147: public static void showError(Component parent, Throwable t) {
L151: public static void showError(Component parent, String title, Throwable t) {
L158: public static String htmlFormat(String input) {

## src/main/java/com/myjavaworld/gui/GreenMetalLargeTheme.java

L29: public class GreenMetalLargeTheme extends GreenMetalTheme {
L40: @Override
L41: public String getName() {
L45: @Override
L46: public FontUIResource getControlTextFont() {
L50: @Override
L51: public FontUIResource getSystemTextFont() {
L55: @Override
L56: public FontUIResource getUserTextFont() {
L60: @Override
L61: public FontUIResource getMenuTextFont() {
L65: @Override
L66: public FontUIResource getWindowTitleFont() {
L70: @Override
L71: public FontUIResource getSubTextFont() {

## src/main/java/com/myjavaworld/gui/GreenMetalTheme.java

L27: public class GreenMetalTheme extends DefaultTheme {
L36: @Override
L37: public String getName() {
L41: @Override
L42: protected ColorUIResource getPrimary1() {
L46: @Override
L47: protected ColorUIResource getPrimary2() {
L51: @Override
L52: protected ColorUIResource getPrimary3() {

## src/main/java/com/myjavaworld/gui/HighContrastLargeTheme.java

L29: public class HighContrastLargeTheme extends HighContrastTheme {
L40: @Override
L41: public String getName() {
L45: @Override
L46: public FontUIResource getControlTextFont() {
L50: @Override
L51: public FontUIResource getSystemTextFont() {
L55: @Override
L56: public FontUIResource getUserTextFont() {
L60: @Override
L61: public FontUIResource getMenuTextFont() {
L65: @Override
L66: public FontUIResource getWindowTitleFont() {
L70: @Override
L71: public FontUIResource getSubTextFont() {

## src/main/java/com/myjavaworld/gui/HighContrastTheme.java

L27: public class HighContrastTheme extends DefaultTheme {
L41: @Override
L42: public String getName() {
L46: @Override
L47: protected ColorUIResource getPrimary1() {
L51: @Override
L52: protected ColorUIResource getPrimary2() {
L56: @Override
L57: protected ColorUIResource getPrimary3() {
L61: @Override
L62: protected ColorUIResource getSecondary1() {
L66: @Override
L67: protected ColorUIResource getSecondary2() {
L71: @Override
L72: protected ColorUIResource getSecondary3() {

## src/main/java/com/myjavaworld/gui/IDTreeNode.java

L26: public class IDTreeNode extends DefaultMutableTreeNode {
L44: public void setID(int id) {
L48: public int getID() {

## src/main/java/com/myjavaworld/gui/ImageCellRenderer.java

L40: public class ImageCellRenderer extends JLabel implements TableCellRenderer,
L41: ListCellRenderer, TreeCellRenderer {
L74: public Component getListCellRendererComponent(JList list, Object value,
L75: int index, boolean isSelected, boolean hasFocus) {
L89: public Component getTableCellRendererComponent(JTable table, Object value,
L90: boolean isSelected, boolean hasFocus, int row, int col) {
L104: public Component getTreeCellRendererComponent(JTree tree, Object value,
L105: boolean isSelected, boolean expanded, boolean leaf, int row,
L106: boolean hasFocus) {

## src/main/java/com/myjavaworld/gui/IndentIcon.java

L28: public class IndentIcon implements Icon {
L38: public void setIcon(Icon icon) {
L42: public Icon getIcon() {
L49: public int getDepth() {
L57: public void setDepth(int depth) {
L61: public void paintIcon(Component c, Graphics g, int x, int y) {
L69: public int getIconWidth() {
L73: public int getIconHeight() {

## src/main/java/com/myjavaworld/gui/IntegerField.java

L32: public class IntegerField extends MTextField {
L79: public void setValue(int value) {
L90: public int getValue() {
L94: @Override
L95: protected Document createDefaultModel() {
L103: static class IntegerDocument extends SingleLineDocument {
L105: @Override
L106: public void insertString(int offset, String str, AttributeSet a)
L107: throws BadLocationException {

## src/main/java/com/myjavaworld/gui/LicenseAgreementDlg.java

L43: public class LicenseAgreementDlg extends MDialog implements ActionListener {
L59: public void setURL(URL url) {
L70: public URL getURL() {
L74: public boolean isLicenseAgreed() {
L78: public void actionPerformed(ActionEvent evt) {
L86: @Override
L87: protected void escape() {
L91: private void initComponents() {
L125: private Component getCommandButtons() {

## src/main/java/com/myjavaworld/gui/MButton.java

L30: public class MButton extends JButton {
L75: public void setMnemonic(String str) {
L81: public void setDisplayedMnemonicIndex(String str) {
L91: public void setMnemonic(String mnemonic, String mnemonicIndex) {

## src/main/java/com/myjavaworld/gui/MCheckBox.java

L24: public class MCheckBox extends JCheckBox {
L58: public void setMnemonic(String mnemonic) {
L64: public void setDisplayedMnemonicIndex(String mnemonicIndex) {
L74: public void setMnemonic(String mnemonic, String mnemonicIndex) {

## src/main/java/com/myjavaworld/gui/MComboBox.java

L30: public class MComboBox extends JComboBox {
L79: public void setData(Object[] data) {
L93: public void setData(Vector data) {

## src/main/java/com/myjavaworld/gui/MDefaultRenderer.java

L35: public class MDefaultRenderer extends JLabel implements TableCellRenderer,
L36: ListCellRenderer {
L62: public Component getListCellRendererComponent(JList list, Object value,
L63: int index, boolean isSelected, boolean hasFocus) {
L77: public Component getTableCellRendererComponent(JTable table, Object value,
L78: boolean isSelected, boolean hasFocus, int row, int col) {

## src/main/java/com/myjavaworld/gui/MDesktopPane.java

L34: public class MDesktopPane extends JDesktopPane {
L51: public void cascade() {
L97: public void tileHorizontally() {
L107: public void tileVertically() {
L111: private void tile(boolean horizontal) {

## src/main/java/com/myjavaworld/gui/MDialog.java

L38: public class MDialog extends JDialog implements WindowListener {
L142: protected void escape() {
L151: private void configure() {
L164: private class EscapeAction extends AbstractAction {
L166: public void actionPerformed(ActionEvent evt) {
L171: public void windowOpened(WindowEvent evt) {
L174: public void windowActivated(WindowEvent evt) {
L177: public void windowDeactivated(WindowEvent evt) {
L180: public void windowIconified(WindowEvent evt) {
L183: public void windowDeiconified(WindowEvent evt) {
L186: public void windowClosing(WindowEvent evt) {
L192: public void windowClosed(WindowEvent evt) {

## src/main/java/com/myjavaworld/gui/MFrame.java

L31: public class MFrame extends JFrame {
L59: @Override
L60: public Insets getInsets() {
L79: public void setBusy(boolean busy) {

## src/main/java/com/myjavaworld/gui/MGlassPane.java

L34: public class MGlassPane extends JComponent implements MouseListener,
L35: KeyListener {
L53: public void mouseEntered(MouseEvent evt) {
L57: public void mouseExited(MouseEvent evt) {
L61: public void mousePressed(MouseEvent evt) {
L65: public void mouseReleased(MouseEvent evt) {
L69: public void mouseClicked(MouseEvent evt) {
L73: public void keyPressed(KeyEvent evt) {
L77: public void keyReleased(KeyEvent evt) {
L81: public void keyTyped(KeyEvent evt) {

## src/main/java/com/myjavaworld/gui/MInternalFrame.java

L30: public class MInternalFrame extends JInternalFrame {
L58: public void setBusy(boolean busy) {
L72: public boolean isBusy() {
L76: private class MGlassPane extends com.myjavaworld.gui.MGlassPane {
L78: @Override
L79: public void mousePressed(MouseEvent evt) {

## src/main/java/com/myjavaworld/gui/MLabel.java

L30: public class MLabel extends JLabel {
L72: public void setDisplayedMnemonic(String mnemonic) {
L78: public void setDisplayedMnemonicIndex(String mnemonicIndex) {
L88: public void setMnemonic(String mnemonic, String mnemonicIndex) {

## src/main/java/com/myjavaworld/gui/MLabelTextField.java

L40: public class MLabelTextField extends JTextField implements MTextComponent,
L41: MouseListener {
L67: @Override
L68: public void setText(String text) {
L77: @Override
L78: public void setDocument(Document model) {
L83: public void setMaximumLength(int maxLength) {
L88: public int getMaximumLength() {
L93: public void setCharacterCase(int characterCase) {
L98: public int getCharacterCase() {
L103: public void setUndoLimit(int undoLimit) {
L107: public int getUndoLimit() {
L111: public void delete() {
L125: public void undo() throws CannotUndoException {
L129: public void redo() throws CannotRedoException {
L133: public boolean canCut() {
L140: public boolean canCopy() {
L144: public boolean canPaste() {
L153: public boolean canDelete() {
L160: public boolean canSelectAll() {
L164: public boolean canUndo() {
L171: public boolean canRedo() {
L178: public void mouseEntered(MouseEvent evt) {
L181: public void mouseExited(MouseEvent evt) {
L184: public void mousePressed(MouseEvent evt) {
L191: public void mouseReleased(MouseEvent evt) {
L197: public void mouseClicked(MouseEvent evt) {
L203: @Override
L204: protected Document createDefaultModel() {
L209: private void setup() {
L216: private void setAppearance() {

## src/main/java/com/myjavaworld/gui/MList.java

L28: public class MList extends JList {

## src/main/java/com/myjavaworld/gui/MMenu.java

L30: public class MMenu extends JMenu {
L48: public void setMnemonic(String str) {
L54: public void setDisplayedMnemonicIndex(String str) {
L64: public void setMnemonic(String mnemonic, String mnemonicIndex) {
L71: @Override
L72: public JMenuItem add(Action action) {

## src/main/java/com/myjavaworld/gui/MMenuItem.java

L30: public class MMenuItem extends JMenuItem {
L56: public void setMnemonic(String str) {
L62: public void setDisplayedMnemonicIndex(String str) {
L72: public void setMnemonic(String mnemonic, String mnemonicIndex) {

## src/main/java/com/myjavaworld/gui/MOptionPane.java

L26: public class MOptionPane extends JOptionPane {
L40: @Override
L41: public int getMaxCharactersPerLineCount() {

## src/main/java/com/myjavaworld/gui/MPasswordField.java

L39: public class MPasswordField extends JPasswordField implements MTextComponent,
L40: MouseListener {
L64: public void setMaximumLength(int maximumLength) {
L69: public int getMaximumLength() {
L74: public void setCharacterCase(int characterCase) {
L79: public int getCharacterCase() {
L84: public void setUndoLimit(int undoLimit) {
L88: public int getUndoLimit() {
L93: public void delete() {
L107: public void undo() throws CannotUndoException {
L111: public void redo() throws CannotRedoException {
L115: public boolean canCut() {
L119: public boolean canCopy() {
L123: public boolean canPaste() {
L132: public boolean canDelete() {
L139: public boolean canSelectAll() {
L143: public boolean canUndo() {
L148: public boolean canRedo() {
L153: public void mouseEntered(MouseEvent evt) {
L156: public void mouseExited(MouseEvent evt) {
L159: public void mousePressed(MouseEvent evt) {
L166: public void mouseReleased(MouseEvent evt) {
L172: public void mouseClicked(MouseEvent evt) {
L178: @Override
L179: protected Document createDefaultModel() {
L192: @Override
L193: protected void processFocusEvent(FocusEvent evt) {
L202: private void setup() {

## src/main/java/com/myjavaworld/gui/MPlainDocument.java

L31: public class MPlainDocument extends PlainDocument {
L54: public void setMaximumLength(int maximumLength) {
L64: public int getMaximumLength() {
L75: public void setCharacterCase(int characterCase) {
L85: public int getCharacterCase() {
L89: @Override
L90: public void insertString(int offset, String str, AttributeSet a)
L91: throws BadLocationException {

## src/main/java/com/myjavaworld/gui/MPopupMenu.java

L37: public class MPopupMenu extends JPopupMenu {
L53: @Override
L54: public void show(Component invoker, int x, int y) {
L72: @Override
L73: public JMenuItem add(Action action) {

## src/main/java/com/myjavaworld/gui/MRadioButton.java

L24: public class MRadioButton extends JRadioButton {
L58: public void setMnemonic(String mnemonic) {
L64: public void setDisplayedMnemonicIndex(String mnemonicIndex) {
L74: public void setMnemonic(String mnemonic, String mnemonicIndex) {

## src/main/java/com/myjavaworld/gui/MRadioButtonMenuItem.java

L30: public class MRadioButtonMenuItem extends JRadioButtonMenuItem {
L64: public void setMnemonic(String str) {
L70: public void setDisplayedMnemonicIndex(String str) {
L80: public void setMnemonic(String mnemonic, String mnemonicIndex) {

## src/main/java/com/myjavaworld/gui/MScrollPane.java

L29: public class MScrollPane extends JScrollPane {

## src/main/java/com/myjavaworld/gui/MTable.java

L35: public class MTable extends JTable {
L110: @Override
L111: public int getRowHeight() {
L121: @Override
L122: protected void processMouseEvent(MouseEvent evt) {
L141: private void processPopupTrigger(MouseEvent evt) {

## src/main/java/com/myjavaworld/gui/MTableCellRenderer.java

L32: public class MTableCellRenderer extends JLabel implements TableCellRenderer {
L44: public Component getTableCellRendererComponent(JTable table, Object value,
L45: boolean isSelected, boolean hasFocus, int row, int col) {

## src/main/java/com/myjavaworld/gui/MTableHeaderRenderer.java

L35: public class MTableHeaderRenderer extends JLabel implements TableCellRenderer {
L64: public Component getTableCellRendererComponent(JTable table, Object value,
L65: boolean isSelected, boolean hasFocus, int row, int col) {
L82: @Override
L83: public void setIcon(Icon icon) {
L93: @Override
L94: public Icon getIcon() {

## src/main/java/com/myjavaworld/gui/MTextArea.java

L39: public class MTextArea extends JTextArea implements MTextComponent,
L40: MouseListener {
L67: public void setMaximumLength(int maximumLength) {
L72: public int getMaximumLength() {
L77: public void setCharacterCase(int characterCase) {
L82: public int getCharacterCase() {
L87: public void setUndoLimit(int undoLimit) {
L91: public int getUndoLimit() {
L95: public void delete() {
L109: public void undo() throws CannotUndoException {
L113: public void redo() throws CannotRedoException {
L117: public boolean canCut() {
L124: public boolean canCopy() {
L128: public boolean canPaste() {
L137: public boolean canDelete() {
L144: public boolean canSelectAll() {
L148: public boolean canUndo() {
L152: public boolean canRedo() {
L156: public void mouseEntered(MouseEvent evt) {
L159: public void mouseExited(MouseEvent evt) {
L162: public void mousePressed(MouseEvent evt) {
L169: public void mouseReleased(MouseEvent evt) {
L175: public void mouseClicked(MouseEvent evt) {
L181: @Override
L182: protected Document createDefaultModel() {
L187: private void setup() {

## src/main/java/com/myjavaworld/gui/MTextComponent.java

L26: public interface MTextComponent {
L48: public void setCharacterCase(int characterCase);
L56: public int getCharacterCase();
L66: public void setMaximumLength(int maximumLength);
L74: public int getMaximumLength();
L83: public void setUndoLimit(int limit);
L91: public int getUndoLimit();
L98: public void cut();
L105: public void copy();
L111: public void paste();
L117: public void delete();
L123: public void selectAll();
L129: public void undo();
L135: public void redo();
L144: public boolean canCut();
L153: public boolean canCopy();
L162: public boolean canPaste();
L171: public boolean canDelete();
L180: public boolean canSelectAll();
L189: public boolean canUndo();
L198: public boolean canRedo();

## src/main/java/com/myjavaworld/gui/MTextField.java

L40: public class MTextField extends JTextField implements MTextComponent,
L41: MouseListener {
L67: @Override
L68: public void setText(String text) {
L77: @Override
L78: public void setDocument(Document model) {
L83: public void setMaximumLength(int maxLength) {
L88: public int getMaximumLength() {
L93: public void setCharacterCase(int characterCase) {
L98: public int getCharacterCase() {
L103: public void setUndoLimit(int undoLimit) {
L107: public int getUndoLimit() {
L111: public void delete() {
L125: public void undo() throws CannotUndoException {
L129: public void redo() throws CannotRedoException {
L133: public boolean canCut() {
L140: public boolean canCopy() {
L144: public boolean canPaste() {
L153: public boolean canDelete() {
L160: public boolean canSelectAll() {
L164: public boolean canUndo() {
L171: public boolean canRedo() {
L178: public void mouseEntered(MouseEvent evt) {
L181: public void mouseExited(MouseEvent evt) {
L184: public void mousePressed(MouseEvent evt) {
L191: public void mouseReleased(MouseEvent evt) {
L197: public void mouseClicked(MouseEvent evt) {
L203: @Override
L204: protected Document createDefaultModel() {
L209: @Override
L210: protected void processFocusEvent(FocusEvent evt) {
L219: private void setup() {

## src/main/java/com/myjavaworld/gui/MTree.java

L32: public class MTree extends JTree {

## src/main/java/com/myjavaworld/gui/NumericCellRenderer.java

L31: public class NumericCellRenderer extends MTableCellRenderer {
L45: @Override
L46: public Component getTableCellRendererComponent(JTable table, Object value,
L47: boolean isSelected, boolean hasFocus, int row, int col) {

## src/main/java/com/myjavaworld/gui/ProgressDialog.java

L35: public class ProgressDialog extends MDialog {
L61: public void setText(String text) {
L65: public void setIndeterminate(boolean indterminate) {
L69: public void setMinimum(int minimum) {
L73: public void setMaximum(int maximum) {
L77: public void setProgress(int value) {
L81: public void setCancelButtonEnabled(boolean enable) {
L85: @Override
L86: public void setVisible(boolean visible) {
L93: public void addActionListener(ActionListener al) {
L97: public void removeActionListener(ActionListener al) {
L101: private void initComponents() {

## src/main/java/com/myjavaworld/gui/SandstoneLargeTheme.java

L29: public class SandstoneLargeTheme extends SandstoneTheme {
L40: @Override
L41: public String getName() {
L45: @Override
L46: public FontUIResource getControlTextFont() {
L50: @Override
L51: public FontUIResource getSystemTextFont() {
L55: @Override
L56: public FontUIResource getUserTextFont() {
L60: @Override
L61: public FontUIResource getMenuTextFont() {
L65: @Override
L66: public FontUIResource getWindowTitleFont() {
L70: @Override
L71: public FontUIResource getSubTextFont() {

## src/main/java/com/myjavaworld/gui/SandstoneTheme.java

L27: public class SandstoneTheme extends DefaultTheme {
L29: @Override
L30: public String getName() {
L44: @Override
L45: protected ColorUIResource getPrimary1() {
L49: @Override
L50: protected ColorUIResource getPrimary2() {
L54: @Override
L55: protected ColorUIResource getPrimary3() {
L59: @Override
L60: protected ColorUIResource getSecondary1() {
L64: @Override
L65: protected ColorUIResource getSecondary2() {
L69: @Override
L70: protected ColorUIResource getSecondary3() {

## src/main/java/com/myjavaworld/gui/SingleLineDocument.java

L33: public class SingleLineDocument extends MPlainDocument {
L50: @Override
L51: public void insertString(int offset, String str, AttributeSet a)
L52: throws BadLocationException {

## src/main/java/com/myjavaworld/gui/SplashWindow.java

L32: public class SplashWindow extends JWindow {
L48: private void initComponents(Icon icon) {
L64: @Override
L65: public void setVisible(boolean visible) {

## src/main/java/com/myjavaworld/gui/SwingWorker.java

L30: public abstract class SwingWorker {
L40: private static class ThreadVar {
L48: synchronized Thread get() {
L52: synchronized void clear() {
L63: protected synchronized Object getValue() {
L70: private synchronized void setValue(Object x) {
L77: public abstract Object construct();
L83: public void finished() {
L90: public void interrupt() {
L105: public Object get() {
L127: public void run() {
L134: public void run() {
L152: public void start() {

## src/main/java/com/myjavaworld/jftp/AboutDlg.java

L47: public class AboutDlg extends MDialog implements ActionListener {
L67: public void actionPerformed(ActionEvent evt) {
L79: @Override
L80: protected void escape() {
L84: private void recalculateMemory() {
L94: private void initComponents() {
L332: private Component getCommandButtons() {

## src/main/java/com/myjavaworld/jftp/AdvancedConnectionPrefsPanel.java

L40: public class AdvancedConnectionPrefsPanel extends JPanel {
L56: public boolean validateFields() {
L82: public void populateScreen() {
L86: public void populateScreen(JFTPPreferences prefs) {
L96: public void saveChanges() {
L108: private void initComponents() {

## src/main/java/com/myjavaworld/jftp/AutoUpdater.java

L31: public class AutoUpdater extends Thread {
L48: @Override
L49: public void run() {

## src/main/java/com/myjavaworld/jftp/CertificatePrefsPanel.java

L42: public class CertificatePrefsPanel extends JPanel implements ActionListener {
L57: public void saveChanges() {
L62: public void actionPerformed(ActionEvent evt) {
L70: private void browseServerCertificateStore() {
L95: private void browseClientCertificateStore() {
L120: private void initComponents() {

## src/main/java/com/myjavaworld/jftp/ChangeLocalDirectoryDlg.java

L47: public class ChangeLocalDirectoryDlg extends MDialog implements ActionListener {
L80: public String getDirectory() {
L87: public void actionPerformed(ActionEvent evt) {
L99: @Override
L100: protected void escape() {
L104: private void close() {
L108: private boolean validateInput() {
L125: private void initComponents() {
L175: private Component getCommandButtons() {

## src/main/java/com/myjavaworld/jftp/ChangeRemoteDirectoryDlg.java

L47: public class ChangeRemoteDirectoryDlg extends MDialog implements ActionListener {
L80: public String getDirectory() {
L87: public void actionPerformed(ActionEvent evt) {
L99: @Override
L100: protected void escape() {
L104: private void close() {
L108: private boolean validateInput() {
L125: private void initComponents() {
L175: private Component getCommandButtons() {

## src/main/java/com/myjavaworld/jftp/ConnectionDlg.java

L63: public class ConnectionDlg extends MDialog implements ActionListener,
L64: ComponentListener, ItemListener {
L102: public void setRemoteHost(RemoteHost remoteHost) {
L107: public RemoteHost getRemoteHost() {
L114: public void actionPerformed(ActionEvent evt) {
L130: public void itemStateChanged(ItemEvent evt) {
L144: public void componentHidden(ComponentEvent evt) {
L147: public void componentShown(ComponentEvent evt) {
L152: public void componentMoved(ComponentEvent evt) {
L155: public void componentResized(ComponentEvent evt) {
L158: private void close() {
L162: @Override
L163: protected void escape() {
L167: private void initComponents() {
L200: private Component getGeneralTab() {
L303: private Component getSSLTab() {
L408: private Component getAdvancedTab() {
L515: private Component getCommandsTab() {
L546: private Component getCommandButtons() {
L565: private void populateScreen() {
L607: private void connectButtonPressed() {
L641: private void cancelButtonPressed() {
L645: private void browseButtonPressed() {
L673: private boolean validateInput() {

## src/main/java/com/myjavaworld/jftp/DnDTransferHandler.java

L34: public class DnDTransferHandler extends TransferHandler {
L49: @Override
L50: public int getSourceActions(JComponent c) {
L54: @Override
L55: public boolean canImport(JComponent comp, DataFlavor[] transferFlavors) {
L75: @Override
L76: protected Transferable createTransferable(JComponent c) {
L88: @Override
L89: public boolean importData(JComponent comp, Transferable t) {
L100: @Override
L101: public Icon getVisualRepresentation(Transferable t) {
L117: private class LocalFileTransferable implements Transferable {
L126: public DataFlavor[] getTransferDataFlavors() {
L130: public boolean isDataFlavorSupported(DataFlavor flavor) {
L134: public Object getTransferData(DataFlavor flavor)
L135: throws UnsupportedFlavorException, IOException {
L143: private class RemoteFileTransferable implements Transferable {
L152: public DataFlavor[] getTransferDataFlavors() {
L156: public boolean isDataFlavorSupported(DataFlavor flavor) {
L160: public Object getTransferData(DataFlavor flavor)
L161: throws UnsupportedFlavorException, IOException {

## src/main/java/com/myjavaworld/jftp/DownloadAndUnzipDlg.java

L52: public class DownloadAndUnzipDlg extends MDialog implements ActionListener,
L53: ItemListener {
L85: public boolean isApproved() {
L89: public File getUnzipDirectory() {
L102: public File getDownloadTo() {
L123: public boolean getDeleteOption() {
L127: public void actionPerformed(ActionEvent evt) {
L147: public void itemStateChanged(ItemEvent evt) {
L158: @Override
L159: protected void escape() {
L163: private void browseUnzipDir() {
L170: private void browseDownloadDir() {
L177: private File browse() {
L191: private boolean validateInput() {
L214: private void initComponents() {
L251: private Component getUnzipOptions() {
L318: private Component getDownloadOptions() {
L397: private Component getCommandButtons() {

## src/main/java/com/myjavaworld/jftp/DownloadAsDlg.java

L45: public class DownloadAsDlg extends MDialog implements ActionListener {
L67: public boolean isApproved() {
L71: public String getFileName() {
L78: public void actionPerformed(ActionEvent evt) {
L91: @Override
L92: protected void escape() {
L96: private boolean validateInput() {
L114: private void initComponents() {
L158: private Component getCommandButtons() {

## src/main/java/com/myjavaworld/jftp/DriveCellRenderer.java

L31: public class DriveCellRenderer extends JLabel implements ListCellRenderer {
L42: public Component getListCellRendererComponent(JList list, Object value,
L43: int index, boolean isSelected, boolean hasFocus) {

## src/main/java/com/myjavaworld/jftp/ExecuteCommandDlg.java

L49: public class ExecuteCommandDlg extends MDialog implements ActionListener {
L69: public String[] getCommands() {
L90: public void actionPerformed(ActionEvent evt) {
L104: @Override
L105: protected void escape() {
L109: private void close() {
L113: private boolean validateInput() {
L130: private void initComponents() {
L164: private Component getCommandButtons() {

## src/main/java/com/myjavaworld/jftp/FTPMenu.java

L51: public class FTPMenu extends MMenu implements MenuListener {
L80: private void prepareMenuItems() {
L210: public void menuSelected(MenuEvent e) {
L249: public void menuDeselected(MenuEvent e) {
L263: public void menuCanceled(MenuEvent e) {
L277: private boolean isZipFile(RemoteFile file) {

## src/main/java/com/myjavaworld/jftp/FTPSession.java

L70: public class FTPSession extends SessionPanel implements FTPConnectionListener,
L71: ControlConnectionListener, DataConnectionListener, ActionListener,
L72: FileChangeListener, ProgressListener, ZipListener {
L138: @Override
L139: public void componentShown(ComponentEvent arg0) {
L153: public void fileChanged(FileChangeEvent evt) {
L175: @Override
L176: public Object construct() {
L191: @Override
L192: public void finished() {
L199: public int getId() {
L203: @Override
L204: public void setBusy(boolean busy) {
L208: public void setTransferType(int transferType) {
L212: public int getTransferType() {
L216: public void setAutoDetect(boolean autoDetect) {
L220: public boolean isAutoDetect() {
L224: public int getTransferType(String ext) {
L236: public void actionPerformed(ActionEvent evt) {
L250: @Override
L251: public String toString() {
L258: public void setLocalFileFilter(Filter filter) {
L266: public Filter getLocalFileFilter() {
L273: public void setRemoteFileFilter(Filter filter) {
L281: public Filter getRemoteFileFilter() {
L285: private void updateTitle() {
L289: private Component getCenterPanel() {
L310: private Component getSouthPanel() {
L315: public void closeSession() {
L330: public RemoteHost getRemoteHost() {
L334: public FTPClient getFTPClient() {
L338: public void setLocalWorkingDirectory(String dir) {
L346: public void setLocalWorkingDirectory(final LocalFile dir) {
L357: @Override
L358: public Object construct() {
L364: @Override
L365: public void finished() {
L372: public LocalFile getLocalWorkingDirectory() {
L376: public void upLocalWorkingDirectory() {
L387: public void refreshLocalPane() {
L391: public void setRemoteWorkingDirectory(String name) {
L396: public RemoteFile getRemoteWorkingDirectory() {
L400: public void setRemoteWorkingDirectory(final RemoteFile dir) {
L413: @Override
L414: public Object construct() {
L437: @Override
L438: public void finished() {
L446: public void upRemoteWorkingDirectory() {
L457: @Override
L458: public Object construct() {
L481: @Override
L482: public void finished() {
L490: public void refreshRemotePane() {
L494: public int getLocalFileSelectionCount() {
L498: public LocalFile getSelectedLocalFile() {
L502: public LocalFile[] getSelectedLocalFiles() {
L506: public int getRemoteFileSelectionCount() {
L510: public RemoteFile getSelectedRemoteFile() {
L514: public RemoteFile[] getSelectedRemoteFiles() {
L518: public void connectionOpened(FTPConnectionEvent evt) {
L524: public void connectionClosed(FTPConnectionEvent evt) {
L537: public void commandSent(ControlConnectionEvent evt) {
L541: public void replyReceived(ControlConnectionEvent evt) {
L545: public void connectionDropped(ControlConnectionEvent evt) {
L549: public void dataTransferStarted(DataConnectionEvent evt) {
L552: public void dataTransferFinished(DataConnectionEvent evt) {
L556: public void dataTransferProgress(DataConnectionEvent evt) {
L560: public void dataTransferAborted(DataConnectionEvent evt) {
L568: public void dataTransferError(DataConnectionEvent evt) {
L571: public void ftpException(Exception exp) {
L575: public void exception(Throwable t) {
L580: public void connectionException(Exception exp) {
L593: public void connect(final RemoteHost remoteHost) {
L621: @Override
L622: public Object construct() {
L686: @Override
L687: public void finished() {
L701: public void reconnect() {
L707: public void download() {
L721: @Override
L722: public Object construct() {
L733: @Override
L734: public void finished() {
L741: public void download(RemoteFile sourceDir, File targetDir, RemoteFile source) {
L745: public void download(RemoteFile sourceDir, File targetDir,
L746: RemoteFile source, String targetName) {
L812: public void downloadDataFile(RemoteFile source, File target) {
L835: public void upload() {
L849: @Override
L850: public Object construct() {
L871: @Override
L872: public void finished() {
L879: public void upload(LocalFile sourceDir, RemoteFile targetDir,
L880: LocalFile source) {
L884: public void upload(LocalFile sourceDir, RemoteFile targetDir,
L885: LocalFile source, String targetName) {
L944: public void upload(LocalFile localFile, String remoteFileName) {
L950: public void upload(LocalFile localFile, RemoteFile destination) {
L973: public void createRemoteDirectory(final String directory) {
L979: @Override
L980: public Object construct() {
L997: @Override
L998: public void finished() {
L1007: public void createRemoteFile(final String file) {
L1013: @Override
L1014: public Object construct() {
L1031: @Override
L1032: public void finished() {
L1041: public void renameRemoteFile(final String fromName, final String toName) {
L1047: @Override
L1048: public Object construct() {
L1064: @Override
L1065: public void finished() {
L1074: public void changeRemoteFilePermissions(final RemoteFile oldFile,
L1075: final RemoteFile newFile, final boolean recursive) {
L1081: @Override
L1082: public Object construct() {
L1110: @Override
L1111: public void finished() {
L1120: private void changeRemoteFilePermissions(RemoteFile file, String attributes) {
L1160: public void updateRemoteFile(final RemoteFile oldFile,
L1161: final RemoteFile newFile) {
L1167: @Override
L1168: public Object construct() {
L1196: @Override
L1197: public void finished() {
L1206: public void deleteRemoteFiles() {
L1221: @Override
L1222: public Object construct() {
L1241: @Override
L1242: public void finished() {
L1249: private void delete(RemoteFile file) {
L1280: public void createLocalDirectory(final String dir) {
L1287: @Override
L1288: public Object construct() {
L1300: @Override
L1301: public void finished() {
L1313: public void createLocalFile(final String fileName) {
L1320: @Override
L1321: public Object construct() {
L1337: @Override
L1338: public void finished() {
L1350: public void renameLocalFile(String fromName, String toName) {
L1369: public void deleteLocalFiles() {
L1386: @Override
L1387: public Object construct() {
L1396: @Override
L1397: public void finished() {
L1404: private void delete(LocalFile file) {
L1420: public void executeCommand(final String command) {
L1427: @Override
L1428: public Object construct() {
L1443: @Override
L1444: public void finished() {
L1450: public void executeCommands(final String[] commands) {
L1457: @Override
L1458: public Object construct() {
L1488: @Override
L1489: public void finished() {
L1495: public void disconnect() {
L1502: @Override
L1503: public Object construct() {
L1518: @Override
L1519: public void finished() {
L1533: public boolean isConnected() {
L1540: private void cleanup() {
L1558: public File downloadToTempFile(RemoteFile source, boolean monitor) {
L1604: public void updateToolBar() {
L1608: public void setAbortFlag(boolean abort) {
L1612: public void clearAbortFlag() {
L1616: public JFTP getJFTP() {
L1620: public void setStatus(String status) {
L1624: public void resetStatusBar() {
L1628: public void setProgress(int progress) {
L1632: public void progressChanged(ProgressEvent evt) {
L1636: public void beginFile(ZipEvent evt) {
L1646: public void endFile(ZipEvent evt) {
L1652: public void selectAllLocalFiles() {
L1656: public void invertLocalFileSelection() {
L1660: public void selectAllRemoteFiles() {
L1664: public void invertRemoteFileSelection() {

## src/main/java/com/myjavaworld/jftp/Favorite.java

L25: public class Favorite extends RemoteHost implements java.io.Serializable,
L26: Comparable {
L37: @Override
L38: public boolean equals(Object obj) {
L46: public int hashcode() {
L50: @Override
L51: public int compareTo(Object obj) {

## src/main/java/com/myjavaworld/jftp/FavoritePropertiesDlg.java

L64: public class FavoritePropertiesDlg extends MDialog implements ActionListener,
L65: ComponentListener, ItemListener {
L140: private void initDialog() {
L160: public void setFavorite(Favorite favorite) {
L171: public Favorite getFavorite() {
L178: public void actionPerformed(ActionEvent evt) {
L194: public void itemStateChanged(ItemEvent evt) {
L208: public void componentHidden(ComponentEvent evt) {
L211: public void componentShown(ComponentEvent evt) {
L216: public void componentMoved(ComponentEvent evt) {
L219: public void componentResized(ComponentEvent evt) {
L222: private void close() {
L226: @Override
L227: protected void escape() {
L231: private void initComponents() {
L264: private Component getGeneralTab() {
L383: private Component getSSLTab() {
L487: private Component getAdvancedTab() {
L594: private Component getCommandsTab() {
L625: private Component getCommandButtons() {
L651: private void populateScreen() {
L695: private void okButtonPressed() {
L724: private void cancelButtonPressed() {
L728: private void browseButtonPressed() {
L754: private boolean validateInput() {

## src/main/java/com/myjavaworld/jftp/FavoritesDlg.java

L55: public class FavoritesDlg extends MDialog implements ActionListener,
L56: ListSelectionListener, MouseListener {
L90: public void actionPerformed(ActionEvent evt) {
L105: @Override
L106: public void windowClosing(WindowEvent evt) {
L111: public void valueChanged(ListSelectionEvent listSelectionEvent) {
L131: @Override
L132: public void windowOpened(WindowEvent evt) {
L136: public void mouseClicked(MouseEvent evt) {
L146: public void mouseEntered(MouseEvent evt) {
L149: public void mouseExited(MouseEvent evt) {
L152: public void mousePressed(MouseEvent evt) {
L155: public void mouseReleased(MouseEvent evt) {
L158: @Override
L159: protected void escape() {
L163: private void addButtonPressed() {
L187: private void editButtonPressed() {
L214: private void deleteButtonPressed() {
L232: private void connectButtonPressed() {
L252: private void initComponents() {
L288: private Component getCommandButtons() {
L325: private void loadFavorites() {
L335: private void saveFavorites() {
L349: class FavoritesListModel extends AbstractListModel {
L361: public void setFavorites(java.util.List favorites) {
L370: public java.util.List getFavorites() {
L374: public int getSize() {
L378: public Object getElementAt(int index) {
L382: public void add(Object obj) {
L388: public void set(int index, Object obj) {
L394: public Object get(int index) {
L398: public void delete(Collection objects) {
L403: public boolean contains(Object obj) {

## src/main/java/com/myjavaworld/jftp/FavoritesManager.java

L45: public class FavoritesManager {
L64: public static List getFavorites() throws IOException,
L65: ClassNotFoundException, IllegalBlockSizeException,
L66: BadPaddingException {
L112: public static void saveFavorites(List favorites) throws IOException,
L113: IllegalBlockSizeException {
L149: public static void addFavorite(RemoteHost host) throws IOException,
L150: ClassNotFoundException, IllegalBlockSizeException,
L151: BadPaddingException {
L157: private static void checkDataHome() {
L163: private static void checkFavFile() throws IOException {
L170: private static Cipher getCipher(int mode) {

## src/main/java/com/myjavaworld/jftp/GeneralConnectionPrefsPanel.java

L46: public class GeneralConnectionPrefsPanel extends JPanel implements
L47: ActionListener {
L65: public boolean validateFields() {
L84: public void populateScreen(JFTPPreferences prefs) {
L89: public void populateScreen() {
L93: public void saveChanges() {
L98: public void actionPerformed(ActionEvent evt) {
L104: private void initComponents() {
L168: private void browseButtonPressed() {

## src/main/java/com/myjavaworld/jftp/HelpMenu.java

L35: public class HelpMenu extends MMenu implements ActionListener {
L61: private void prepareMenuItems() {
L108: public void actionPerformed(ActionEvent evt) {

## src/main/java/com/myjavaworld/jftp/JFTP.java

L62: public class JFTP extends MFrame implements WindowListener, ActionListener,
L63: ChangeListener {
L149: public void newSession() {
L156: public void windowOpened(WindowEvent evt) {
L166: public void windowActivated(WindowEvent evt) {
L169: public void windowDeactivated(WindowEvent evt) {
L172: public void windowIconified(WindowEvent evt) {
L175: public void windowDeiconified(WindowEvent evt) {
L178: public void windowClosing(WindowEvent evt) {
L182: public void windowClosed(WindowEvent evt) {
L185: public void stateChanged(ChangeEvent evt) {
L189: public void closeSession() {
L200: public void exit() {
L220: public void actionPerformed(ActionEvent evt) {
L295: private void executeCustomCommand() {
L311: private void executeCommand(String command) {
L319: private void manageCertificates() {
L326: private void showRemoteFileProperties() {
L348: private void showLocalFileProperties() {
L364: private void showLocalFileFilter() {
L380: private void clearLocalFileFilter() {
L388: private void showRemoteFileFilter() {
L404: private void clearRemoteFileFilter() {
L412: private void addToFavorites() {
L452: public void showPreferencesDialog() {
L459: private JMenuBar prepareMenuBar() {
L477: private Rectangle getPreferredBounds() {
L496: public FTPSession getCurrentSession() {
L513: public static synchronized void savePreferences(JFTPPreferences prefs)
L514: throws IOException {
L536: public static synchronized JFTPPreferences loadPreferences()
L537: throws IOException {
L576: public static String[] getInstalledThemes() {
L590: public static String getThemeClassName(String themeName) {
L599: public static String[] getInstalledParsers() {
L612: public static String getParserClassName(String parserName) {
L623: public static String getParserName(String parserClassName) {
L640: public static String[] getInstalledClients() {
L654: public static String getClientClassName(String clientName) {
L665: public static String getClientName(String clientClassName) {
L677: public void updateSessionTitle(FTPSession session) {
L695: public void showAboutDialog() {
L705: public void updateToolBar() {
L709: private void showLicenseAgreement() {
L731: private void selectAllLocalFiles() {
L738: private void invertLocalFileSelection() {
L745: private void selectAllRemoteFiles() {
L752: private void invertRemoteFileSelection() {

## src/main/java/com/myjavaworld/jftp/JFTPApplet.java

L37: public class JFTPApplet extends JApplet implements ActionListener {
L53: @Override
L54: public void init() {
L59: public void actionPerformed(ActionEvent evt) {
L67: private void initComponents() {

## src/main/java/com/myjavaworld/jftp/JFTPApplication.java

L28: public class JFTPApplication {
L65: public static void main(String args[]) {
L69: public void showAboutDialog() {
L75: public void showPreferencesDialog() {
L81: public void quit() {
L87: private void registerForMacOSXEvents() {

## src/main/java/com/myjavaworld/jftp/JFTPConstants.java

L21: public interface JFTPConstants {

## src/main/java/com/myjavaworld/jftp/JFTPHelp2.java

L32: public class JFTPHelp2 {
L53: public HelpBroker getHelpBroker() {
L57: public static synchronized JFTPHelp2 getInstance() {
L64: public void enableHelp(Component comp, String id) {
L68: public void enableHelpKey(Component comp, String id) {

## src/main/java/com/myjavaworld/jftp/JFTPPreferences.java

L38: public class JFTPPreferences implements Serializable {
L153: public void setLocale(Locale locale) {
L157: public Locale getLocale() {
L161: public void setLookAndFeelClassName(String laf) {
L165: public String getLookAndFeelClassName() {
L169: public void setTheme(String theme) {
L173: public String getTheme() {
L177: public void setClient(String client) {
L181: public String getClient() {
L185: public void setListParser(String listParser) {
L189: public String getListParser() {
L193: public void setEmail(String email) {
L197: public String getEmail() {
L201: public void setTimeout(int timeout) {
L205: public int getTimeout() {
L209: public void setBufferSize(int bufferSize) {
L213: public int getBufferSize() {
L217: public void setLocalDirectory(String localDirectory) {
L221: public String getLocalDirectory() {
L225: public void setDateFormat(int dateFormat) {
L229: public int getDateFormat() {
L233: public void setTimeFormat(int timeFormat) {
L237: public int getTimeFormat() {
L241: public void setDefaultTransferType(int defaultTransferType) {
L245: public int getDefaultTransferType() {
L249: public void setTransferTypes(Map transferTypes) {
L253: public Map getTransferTypes() {
L257: public void setPassive(boolean passive) {
L261: public boolean isPassive() {
L265: public void setUseJavaWindows(boolean useJavaWindows) {
L269: public boolean getUseJavaWindows() {
L273: public void setToolBarType(int toolBarType) {
L277: public int getToolBarType() {
L281: public void setServerCertificateStore(String fileName) {
L285: public String getServerCertificateStore() {
L292: public void setClientCertificateStore(String fileName) {
L296: public String getClientCertificateStore() {
L303: public void setServerCertificateStorePassword(char[] password) {
L307: public char[] getServerCertificateStorePassword() {
L314: public void setClientCertificateStorePassword(char[] password) {
L318: public char[] getClientCertificateStorePassword() {
L325: public void setUseProxy(boolean useProxy) {
L329: public boolean isUseProxy() {
L336: public void setProxyHost(String proxyHost) {
L340: public String getProxyHost() {
L347: public void setProxyPort(int proxyPort) {
L351: public int getProxyPort() {
L358: public void setProxyUser(String proxyUser) {
L362: public String getProxyUser() {
L369: public void setProxyPassword(char[] proxyPassword) {
L373: public char[] getProxyPassword() {
L380: public void setSSLUsage(int sslUsage) {
L384: public int getSSLUsage() {
L391: public void setImplicitSSLPort(int implicitSSLPort) {
L395: public int getImplicitSSLPort() {
L402: public void setDataChannelUnencrypted(boolean dataChannelUnencrypted) {
L406: public boolean isDataChannelUnencrypted() {
L413: public void setWindowBounds(Rectangle windowBounds) {
L417: public Rectangle getWindowBounds() {
L421: public void setLicenseAgreed(boolean licenseAgreed) {
L425: public boolean isLicenseAgreed() {
L435: public String getLicenseAgreedForVersion() {
L446: public void setLicenseAgreedForVersion(String licenseAgreedForVersion) {
L450: public boolean getCheckForUpdates() {
L457: public void setCheckForUpdates(boolean checkForUpdates) {

## src/main/java/com/myjavaworld/jftp/JFTPToolBar.java

L57: public class JFTPToolBar extends JToolBar {
L92: @Override
L93: public Insets getInsets() {
L97: private void prepareToolBar() {
L281: @Override
L282: public JButton add(Action action) {
L288: @Override
L289: protected JButton createActionComponent(Action a) {
L294: public void updateButtons() {

## src/main/java/com/myjavaworld/jftp/JFTPUtil.java

L33: public class JFTPUtil {
L35: public static Icon getIcon(String name) {
L39: public static Image getImage(String name) {
L44: public static String getTimeString(int seconds) {
L70: public static void updateProxySettings() {
L83: @Override
L84: protected PasswordAuthentication getPasswordAuthentication() {

## src/main/java/com/myjavaworld/jftp/LocalFile.java

L35: public class LocalFile implements Serializable {
L70: public File getFile() {
L74: public String getAbsolutePath() {
L78: public LocalFile getAbsoluteFile() {
L82: public String getCanonicalPath() throws IOException {
L86: public LocalFile getCanonicalFile() throws IOException {
L90: public String getNameOld() {
L94: public String getName() {
L98: public String getDisplayName() {
L102: public String getExtension() {
L106: public String getTypeOld() {
L116: public String getType() {
L124: public long getSize() {
L128: public long getLastModified() {
L132: public boolean isDirectory() {
L136: public boolean isFile() {
L140: public boolean exists() {
L144: public boolean canRead() {
L148: public boolean canWrite() {
L152: public boolean isHidden() {
L156: public LocalFile getParentOld() {
L164: public LocalFile getParent() {
L172: public LocalFile[] listOld() {
L184: public LocalFile[] list() {
L196: public LocalFile[] listOld(Filter filter) {
L215: public LocalFile[] list(Filter filter) {
L234: public static LocalFile[] listRoots() {
L246: @Override
L247: public boolean equals(Object obj) {
L255: public int compareTo(Object obj) {
L263: @Override
L264: public String toString() {
L268: public Icon getIcon() {
L272: public boolean isTraversable() {
L276: public boolean delete() {
L280: public boolean isDrive() {

## src/main/java/com/myjavaworld/jftp/LocalFileCellRenderer.java

L31: public class LocalFileCellRenderer extends MTableCellRenderer {
L42: @Override
L43: public Component getTableCellRendererComponent(JTable table, Object value,
L44: boolean isSelected, boolean hasFocus, int row, int col) {

## src/main/java/com/myjavaworld/jftp/LocalFileComparator.java

L28: public class LocalFileComparator implements Comparator {
L52: public void setCompareBy(int compareBy) {
L56: public int getCompareBy() {
L60: public void setOrder(int order) {
L64: public int getOrder() {
L68: public int compare(Object o1, Object o2) {
L82: private int compareByName(LocalFile l1, LocalFile l2) {
L102: private int compareBySize(LocalFile l1, LocalFile l2) {
L125: private int compareByDate(LocalFile l1, LocalFile l2) {
L141: private int compareByType(LocalFile l1, LocalFile l2) {

## src/main/java/com/myjavaworld/jftp/LocalFileFilter.java

L26: public class LocalFileFilter implements Filter {
L73: public DateFilter getDateFilter() {
L81: public void setDateFilter(DateFilter dateFilter) {
L88: public RegexFilter getRegexFilter() {
L96: public void setRegexFilter(RegexFilter regexFilter) {
L103: public boolean isShowHiddenFiles() {
L111: public void setShowHiddenFiles(boolean showHiddenFiles) {
L115: public void setExclusionFilter(boolean exclusionFilter) {
L119: public boolean isExclusionFilter() {
L123: public boolean accept(Object value) {

## src/main/java/com/myjavaworld/jftp/LocalFileFilterDlg.java

L58: public class LocalFileFilterDlg extends MDialog implements ActionListener {
L95: public boolean isApproved() {
L102: public void setFilter(Filter filter) {
L132: public Filter getFilter() {
L146: public void actionPerformed(ActionEvent evt) {
L158: @Override
L159: public void windowOpened(WindowEvent evt) {
L163: @Override
L164: protected void escape() {
L168: private boolean validateInput() {
L195: private RegexFilter getRegexFilter() {
L204: private DateFilter getDateFilter() throws ParseException {
L221: private void initComponents() {
L277: private Component getFilterTypePanel() {
L316: private Component getFileNameFilterPanel() {
L363: private Component getDateFilterPanel() {
L434: private Component getAttributesFilterPanel() {
L457: private Component getCommandButtons() {

## src/main/java/com/myjavaworld/jftp/LocalFilePropertiesDlg.java

L58: public class LocalFilePropertiesDlg extends MDialog implements ActionListener {
L99: public void actionPerformed(ActionEvent evt) {
L105: @Override
L106: public void windowClosing(WindowEvent evt) {
L110: @Override
L111: public void windowOpened(WindowEvent evt) {
L117: @Override
L118: protected void escape() {
L122: private void start() {
L129: @Override
L130: public Object construct() {
L135: @Override
L136: public void finished() {
L143: private void updateTitle() {
L151: private void close() {
L156: private void populateScreen() {
L173: private void updateSizeAndContents() {
L183: private void computeSizeAndContents(LocalFile file) {
L204: private void initComponents() {
L387: private Component getAttributesPanel() {
L410: private Component getCommandButtons() {

## src/main/java/com/myjavaworld/jftp/LocalFileTableModel.java

L32: public class LocalFileTableModel extends AbstractTableModel {
L50: public void setData(LocalFile[] data) {
L58: public LocalFile[] getData() {
L62: public LocalFile getFileAt(int row) {
L66: public int getColumnCount() {
L70: @Override
L71: public String getColumnName(int col) {
L75: public int getRowCount() {
L79: public Object getValueAt(int row, int col) {
L92: @Override
L93: public Class getColumnClass(int col) {

## src/main/java/com/myjavaworld/jftp/LocalPane.java

L75: public class LocalPane extends JPanel implements ActionListener, MouseListener,
L76: ListSelectionListener {
L115: public void setData(LocalFile dir, LocalFile[] data) {
L135: public LocalFile[] getData() {
L139: public int getSelectionCount() {
L143: public LocalFile getSelectedFile() {
L151: public LocalFile[] getSelectedFiles() {
L163: public void refresh() {
L168: public void valueChanged(ListSelectionEvent evt) {
L173: public void actionPerformed(ActionEvent evt) {
L191: public void mouseEntered(MouseEvent evt) {
L194: public void mouseExited(MouseEvent evt) {
L197: public void mousePressed(MouseEvent evt) {
L207: public void mouseReleased(MouseEvent evt) {
L232: public void mouseClicked(MouseEvent evt) {
L235: private void tableRightClicked(MouseEvent evt) {
L240: private void scrollerRightClicked(MouseEvent evt) {
L246: private void doubleClicked(MouseEvent evt) {
L256: private LocalFile[] getRoots() {
L264: private void updateComboWorkingDirectory(LocalFile dir) {
L271: private void updateStatus() {
L295: private void sort(int col) {
L313: private void updateTableHeader() {
L330: private void initComponents() {
L379: @Override
L380: public boolean getScrollableTracksViewportWidth() {
L413: private void configureTable() {
L448: class DirectoryComboBoxModel extends AbstractListModel implements
L449: ComboBoxModel {
L460: public Object getSelectedItem() {
L464: public void setSelectedItem(Object selectedDir) {
L469: public int getSize() {
L473: public Object getElementAt(int index) {
L477: private void addItem(LocalFile dir) {
L493: class DirectoryCellRenderer extends MLabel implements ListCellRenderer {
L503: public Component getListCellRendererComponent(JList list, Object value,
L504: int index, boolean isSelected, boolean cellHasFocus) {
L523: public void selectAll() {
L527: public void invertSelection() {

## src/main/java/com/myjavaworld/jftp/LocalSystemMenu.java

L46: public class LocalSystemMenu extends MMenu implements MenuListener {
L88: private void prepareMenuItems() {
L235: public void menuCanceled(MenuEvent menuEvent) {
L251: public void menuDeselected(MenuEvent menuEvent) {
L267: public void menuSelected(MenuEvent menuEvent) {

## src/main/java/com/myjavaworld/jftp/LocalSystemPopupMenu.java

L46: public class LocalSystemPopupMenu extends MPopupMenu implements
L47: PopupMenuListener {
L90: public static LocalSystemPopupMenu getInstance(JFTP jftp) {
L99: private void preparePopupMenu() {
L244: public void popupMenuCanceled(PopupMenuEvent popupMenuEvent) {
L247: public void popupMenuWillBecomeInvisible(PopupMenuEvent popupMenuEvent) {
L250: public void popupMenuWillBecomeVisible(PopupMenuEvent popupMenuEvent) {

## src/main/java/com/myjavaworld/jftp/LocaleCellRenderer.java

L32: public class LocaleCellRenderer extends JLabel implements ListCellRenderer {
L43: public Component getListCellRendererComponent(JList list, Object value,
L44: int index, boolean isSelected, boolean hasFocus) {

## src/main/java/com/myjavaworld/jftp/LocalePrefsPanel.java

L43: public class LocalePrefsPanel extends JPanel implements ActionListener {
L65: public boolean validateFields() {
L69: public void populateScreen() {
L73: public void populateScreen(JFTPPreferences prefs) {
L88: public void saveChanges() {
L103: private void initComponents() {
L237: public void actionPerformed(ActionEvent evt) {
L241: private void updatePreview() {

## src/main/java/com/myjavaworld/jftp/NewLocalDirectoryDlg.java

L47: public class NewLocalDirectoryDlg extends MDialog implements ActionListener {
L79: public String getDirectory() {
L86: public void actionPerformed(ActionEvent evt) {
L98: private void close() {
L102: @Override
L103: protected void escape() {
L107: private boolean validateInput() {
L124: private void initComponents() {
L173: private Component getCommandButtons() {

## src/main/java/com/myjavaworld/jftp/NewLocalFileDlg.java

L47: public class NewLocalFileDlg extends MDialog implements ActionListener {
L79: public String getFile() {
L86: public void actionPerformed(ActionEvent evt) {
L98: private void close() {
L102: @Override
L103: protected void escape() {
L107: private boolean validateInput() {
L124: private void initComponents() {
L154: private Component getCommandButtons() {

## src/main/java/com/myjavaworld/jftp/NewRemoteDirectoryDlg.java

L47: public class NewRemoteDirectoryDlg extends MDialog implements ActionListener {
L66: public String getDirectory() {
L73: public void actionPerformed(ActionEvent evt) {
L85: private void close() {
L89: @Override
L90: protected void escape() {
L94: private boolean validateInput() {
L111: private void initComponents() {
L141: private Component getCommandButtons() {

## src/main/java/com/myjavaworld/jftp/NewRemoteFileDlg.java

L46: public class NewRemoteFileDlg extends MDialog implements ActionListener {
L66: public String getFile() {
L73: public void actionPerformed(ActionEvent evt) {
L85: private void close() {
L89: @Override
L90: protected void escape() {
L94: private boolean validateInput() {
L111: private void initComponents() {
L141: private Component getCommandButtons() {

## src/main/java/com/myjavaworld/jftp/OSXAdapter.java

L18: public class OSXAdapter {
L41: private static class MacOSXEventHandler implements InvocationHandler {
L43: public Object invoke(Object proxy, Method method, Object[] args)
L44: throws Throwable {
L65: public static void init(JFTPApplication jftpApplication) {
L81: private static void registerAboutHandler() {
L88: private static void registerQuitHandler() {
L95: private static void registerPreferencesHandler() {
L111: private static void registerHandler(String handlerClassName,
L112: String registrationMethodName) {
L138: public static void enableFullScreenMode(Window window) {
L156: private static void handleDockIcon() {
L173: private static void createMacOSXApplication() {

## src/main/java/com/myjavaworld/jftp/OSXAdapterOld.java

L61: public class OSXAdapterOld extends ApplicationAdapter {
L77: @Override
L78: public void handleAbout(ApplicationEvent ae) {
L88: @Override
L89: public void handlePreferences(ApplicationEvent ae) {
L99: @Override
L100: public void handleQuit(ApplicationEvent ae) {
L121: public static void registerMacOSXApplication(JFTPApplication inApp) {
L134: public static void enablePrefs(boolean enabled) {

## src/main/java/com/myjavaworld/jftp/PreferencesDlg.java

L55: public class PreferencesDlg extends MDialog implements ActionListener,
L56: TreeSelectionListener {
L95: public void actionPerformed(ActionEvent evt) {
L113: public void valueChanged(TreeSelectionEvent evt) {
L124: @Override
L125: protected void escape() {
L129: private MTree createTree() {
L192: private void initComponents() {
L258: private Component getCommandButtons() {
L288: private void saveButtonPressed() {

## src/main/java/com/myjavaworld/jftp/ProxyPrefsPanel.java

L42: public class ProxyPrefsPanel extends JPanel implements ActionListener {
L58: public void actionPerformed(ActionEvent evt) {
L62: private void setProxySettingsEnabled(boolean enabled) {
L69: private void initComponents() {
L205: public void populateScreen() {
L209: public void populateScreen(JFTPPreferences prefs) {
L218: public boolean validateFields() {
L244: public void saveChanges() {

## src/main/java/com/myjavaworld/jftp/RemoteFileCellRenderer.java

L33: public class RemoteFileCellRenderer extends MTableCellRenderer {
L46: @Override
L47: public Component getTableCellRendererComponent(JTable table, Object value,
L48: boolean isSelected, boolean hasFocus, int row, int col) {

## src/main/java/com/myjavaworld/jftp/RemoteFileComparator.java

L31: public class RemoteFileComparator implements Comparator {
L55: public void setCompareBy(int compareBy) {
L59: public int getCompareBy() {
L63: public void setOrder(int order) {
L67: public int getOrder() {
L71: public int compare(Object o1, Object o2) {
L85: private int compareByName(RemoteFile r1, RemoteFile r2) {
L98: private int compareBySize(RemoteFile r1, RemoteFile r2) {
L118: private int compareByDate(RemoteFile r1, RemoteFile r2) {
L134: private int compareByType(RemoteFile r1, RemoteFile r2) {

## src/main/java/com/myjavaworld/jftp/RemoteFileFilterDlg.java

L59: public class RemoteFileFilterDlg extends MDialog implements ActionListener {
L95: public boolean isApproved() {
L102: public void setFilter(Filter filter) {
L129: public Filter getFilter() {
L142: public void actionPerformed(ActionEvent evt) {
L154: @Override
L155: public void windowOpened(WindowEvent evt) {
L159: @Override
L160: protected void escape() {
L164: private boolean validateInput() {
L191: private RegexFilter getRegexFilter() {
L200: private DateFilter getDateFilter() throws ParseException {
L217: private void initComponents() {
L263: private Component getFilterTypePanel() {
L302: private Component getFileNameFilterPanel() {
L349: private Component getDateFilterPanel() {
L420: private Component getCommandButtons() {

## src/main/java/com/myjavaworld/jftp/RemoteFilePropertiesDlg.java

L56: public class RemoteFilePropertiesDlg extends MDialog implements ActionListener {
L113: public RemoteFile getFile() {
L120: public boolean isRecursive() {
L124: public void actionPerformed(ActionEvent evt) {
L133: @Override
L134: public void windowClosing(WindowEvent evt) {
L138: @Override
L139: public void windowOpened(WindowEvent evt) {
L145: private void start() {
L152: @Override
L153: public Object construct() {
L164: @Override
L165: public void finished() {
L172: private void updateSizeAndContents() {
L182: private void computeSizeAndContents(RemoteFile file) {
L214: private void okButtonPressed() {
L237: private void populateScreen() {
L256: @Override
L257: protected void escape() {
L261: private void updateTitle() {
L268: private void close() {
L273: private void initComponents() {
L519: private Component getAttributesPanel() {
L736: private Component getCommandButtons() {

## src/main/java/com/myjavaworld/jftp/RemoteFileTableModel.java

L33: public class RemoteFileTableModel extends AbstractTableModel {
L52: public void setData(RemoteFile[] data) {
L60: public RemoteFile[] getData() {
L64: public RemoteFile getFileAt(int row) {
L68: public int getRowCount() {
L72: public int getColumnCount() {
L76: @Override
L77: public String getColumnName(int col) {
L81: public Object getValueAt(int row, int col) {
L97: @Override
L98: public Class getColumnClass(int col) {

## src/main/java/com/myjavaworld/jftp/RemoteHost.java

L33: public class RemoteHost implements Serializable, Comparable {
L86: public void setName(String name) {
L90: public String getName() {
L94: public void setHostName(String hostName) {
L98: public String getHostName() {
L102: public void setPort(int port) {
L106: public int getPort() {
L110: public void setPassword(String password) {
L114: public String getPassword() {
L118: public void setUser(String user) {
L122: public String getUser() {
L126: public void setAccount(String account) {
L130: public String getAccount() {
L134: public void setFTPClientClassName(String ftpClientClassName) {
L138: public String getFTPClientClassName() {
L142: public void setListParserClassName(String listParserClassName) {
L146: public String getListParserClassName() {
L150: public void setCommands(String[] commands) {
L154: public void setCommands(String commands) {
L168: public String[] getCommands() {
L172: public String getCommandsAsString() {
L181: public void setPassive(boolean passive) {
L185: public boolean isPassive() {
L189: public void setInitialLocalDirectory(String initialLocalDirectory) {
L193: public String getInitialLocalDirectory() {
L197: public void setInitialRemoteDirectory(String initialRemoteDirectory) {
L201: public String getInitialRemoteDirectory() {
L205: public void setSSLUsage(int sslUsage) {
L209: public int getSSLUsage() {
L213: public void setDataChannelUnencrypted(boolean dataChannelUnencrypted) {
L217: public boolean isDataChannelUnencrypted() {
L221: public void setImplicitSSLPort(int implicitSSLPort) {
L225: public int getImplicitSSLPort() {
L232: @Override
L233: public String toString() {
L240: public int compareTo(Object obj) {
L245: @Override
L246: public boolean equals(Object obj) {

## src/main/java/com/myjavaworld/jftp/RemotePane.java

L69: public class RemotePane extends JPanel implements ActionListener,
L70: MouseListener, ListSelectionListener {
L107: public void setData(RemoteFile dir, RemoteFile[] data) {
L122: public RemoteFile[] getData() {
L126: public int getSelectionCount() {
L130: public RemoteFile getSelectedFile() {
L138: public RemoteFile[] getSelectedFiles() {
L150: public void refresh() {
L154: public void clearAll() {
L159: public void valueChanged(ListSelectionEvent evt) {
L164: public void actionPerformed(ActionEvent evt) {
L176: public void mouseEntered(MouseEvent evt) {
L179: public void mouseExited(MouseEvent evt) {
L182: public void mousePressed(MouseEvent evt) {
L192: public void mouseReleased(MouseEvent evt) {
L219: public void mouseClicked(MouseEvent evt) {
L222: private void tableRightClicked(MouseEvent evt) {
L227: private void scrollerRightClicked(MouseEvent evt) {
L233: private void doubleClicked(MouseEvent evt) {
L247: private void updateComboWorkingDirectory(RemoteFile dir) {
L262: private void updateStatus() {
L284: private void sort(int col) {
L302: private void updateTableHeader() {
L319: private void initComponents() {
L350: @Override
L351: public boolean getScrollableTracksViewportWidth() {
L381: private void configureTable() {
L420: public void selectAll() {
L424: public void invertSelection() {

## src/main/java/com/myjavaworld/jftp/RemoteSystemMenu.java

L44: public class RemoteSystemMenu extends MMenu implements MenuListener {
L83: private void prepareMenuItems() {
L262: public void menuCanceled(javax.swing.event.MenuEvent menuEvent) {
L279: public void menuDeselected(javax.swing.event.MenuEvent menuEvent) {
L296: public void menuSelected(javax.swing.event.MenuEvent menuEvent) {
L327: private boolean isZipFile(RemoteFile file) {

## src/main/java/com/myjavaworld/jftp/RemoteSystemPopupMenu.java

L48: public class RemoteSystemPopupMenu extends MPopupMenu implements
L49: PopupMenuListener {
L89: public static RemoteSystemPopupMenu getInstance(JFTP jftp) {
L98: private void preparePopupMenu() {
L286: public void popupMenuCanceled(PopupMenuEvent popupMenuEvent) {
L289: public void popupMenuWillBecomeInvisible(PopupMenuEvent popupMenuEvent) {
L292: public void popupMenuWillBecomeVisible(PopupMenuEvent popupMenuEvent) {
L327: private boolean isZipFile(RemoteFile file) {

## src/main/java/com/myjavaworld/jftp/RenameLocalFileDlg.java

L47: public class RenameLocalFileDlg extends MDialog implements ActionListener {
L70: @Override
L71: public void windowOpened(WindowEvent evt) {
L77: public void actionPerformed(ActionEvent evt) {
L89: @Override
L90: protected void escape() {
L94: private void close() {
L98: public String getFromFile() {
L105: public String getToFile() {
L112: private boolean validateInput() {
L132: private void initComponents() {
L180: private Component getCommandButtons() {

## src/main/java/com/myjavaworld/jftp/RenameRemoteFileDlg.java

L47: public class RenameRemoteFileDlg extends MDialog implements ActionListener {
L70: public void actionPerformed(ActionEvent evt) {
L82: private void close() {
L86: public String getFromFile() {
L93: public String getToFile() {
L100: @Override
L101: public void windowOpened(WindowEvent evt) {
L107: private boolean validateInput() {
L127: private void initComponents() {
L175: private Component getCommandButtons() {

## src/main/java/com/myjavaworld/jftp/SecurityPrefsPanel.java

L42: public class SecurityPrefsPanel extends JPanel implements ActionListener,
L43: ItemListener {
L60: public void actionPerformed(ActionEvent evt) {
L63: public void itemStateChanged(ItemEvent evt) {
L73: public void populateScreen() {
L77: public void populateScreen(JFTPPreferences prefs) {
L96: private void initComponents() {
L203: public boolean validateFields() {
L207: public void saveChanges() {

## src/main/java/com/myjavaworld/jftp/SessionPanel.java

L28: public class SessionPanel extends JRootPane {
L40: public void setBusy(boolean busy) {
L46: public boolean isBusy() {
L50: public void setTitle(String title) {
L54: public String getTitle() {
L58: public void dispose() {

## src/main/java/com/myjavaworld/jftp/SoftwareUpdatePrefsPanel.java

L35: public class SoftwareUpdatePrefsPanel extends JPanel implements ActionListener {
L48: public void actionPerformed(ActionEvent evt) {
L53: public boolean validateFields() {
L57: public void populateScreen() {
L61: public void populateScreen(JFTPPreferences prefs) {
L65: public void saveChanges() {
L69: private void initComponents() {

## src/main/java/com/myjavaworld/jftp/StatusBar.java

L38: public class StatusBar extends JPanel {
L62: public void setStatus(String status) {
L66: public void setMinimum(int min) {
L70: public void setMaximum(int max) {
L74: public void setProgress(int value) {
L78: public void setSpeed(long speed) {
L83: public void setTimeElapsed(String timeElapsed) {
L88: public void setSecured(boolean secured) {
L93: public void setIndeterminate(boolean indeterminate) {
L98: public void reset() {
L108: private void initComponents() {

## src/main/java/com/myjavaworld/jftp/StatusWindow.java

L39: public class StatusWindow extends JTextPane {
L65: public void addNormal(String str) {
L69: public void addCommand(String str) {
L73: public void addReply(String str) {
L77: public void addError(String str) {
L81: public void addStatus(String str) {
L85: public void addInfo(String str) {
L89: private synchronized void append(String str, Style style) {
L101: private void initStyles() {

## src/main/java/com/myjavaworld/jftp/SygnityStyle.java

L20: final class SygnityStyle {
L32: static void install() {
L76: private static void colors(Color value, String... keys) {
L80: static Border statusCellBorder() {
L86: static JLabel logo() {
L89: public int getIconWidth() {
L90: public int getIconHeight() {
L91: public void paintIcon(Component component, Graphics graphics, int x, int y) {

## src/main/java/com/myjavaworld/jftp/ToolsMenu.java

L36: public class ToolsMenu extends MMenu implements MenuListener {
L56: private void prepareMenuItems() {
L101: public void menuCanceled(javax.swing.event.MenuEvent menuEvent) {
L104: public void menuDeselected(javax.swing.event.MenuEvent menuEvent) {
L107: public void menuSelected(javax.swing.event.MenuEvent menuEvent) {

## src/main/java/com/myjavaworld/jftp/TransferModeMenu.java

L38: public class TransferModeMenu extends MMenu implements MenuListener {
L59: private void prepareMenuItems(ResourceBundle resources) {
L96: public void menuCanceled(javax.swing.event.MenuEvent menuEvent) {
L99: public void menuDeselected(javax.swing.event.MenuEvent menuEvent) {
L102: public void menuSelected(javax.swing.event.MenuEvent menuEvent) {

## src/main/java/com/myjavaworld/jftp/TransferModesPrefsPanel.java

L50: public class TransferModesPrefsPanel extends JPanel {
L69: @Override
L70: public Dimension getPreferredSize() {
L74: public boolean validateFields() {
L78: public void populateScreen() {
L82: public void populateScreen(JFTPPreferences prefs) {
L88: public void saveChanges() {
L102: private void initComponents() {
L147: private void configureTable() {
L158: private class TypesTableModel extends AbstractTableModel {
L171: public void setData(Map map) {
L186: public int getRowCount() {
L190: public int getColumnCount() {
L194: @Override
L195: public String getColumnName(int col) {
L199: public Object getValueAt(int row, int col) {
L207: @Override
L208: public void setValueAt(Object value, int row, int col) {
L223: @Override
L224: public Class getColumnClass(int col) {
L231: @Override
L232: public boolean isCellEditable(int row, int col) {
L236: private void addEmptyRow() {
L242: private static class TransferTypeCellRenderer extends MTableCellRenderer {
L248: @Override
L249: public Component getTableCellRendererComponent(JTable table,
L250: Object value, boolean isSelected, boolean hasFocus, int row,
L251: int col) {

## src/main/java/com/myjavaworld/jftp/TransferObject.java

L23: public class TransferObject {
L38: public int getDirection() {
L42: public LocalFile getLocalFile() {
L46: public RemoteFile getRemoteFile() {
L50: @Override
L51: public String toString() {

## src/main/java/com/myjavaworld/jftp/UIPrefsPanel.java

L38: public class UIPrefsPanel extends JPanel {
L50: private void initComponents() {
L85: public boolean validateFields() {
L89: public void populateScreen() {
L93: public void populateScreen(JFTPPreferences prefs) {
L105: public void saveChanges() {
L115: private String[] getInstalledLookAndFeels() {
L124: private String getLookAndFeelClassName(String lookAndFeelName) {
L134: private String getLookAndFeelName(String lookAndFeelClassName) {

## src/main/java/com/myjavaworld/jftp/UploadAsDlg.java

L44: public class UploadAsDlg extends MDialog implements ActionListener {
L66: public boolean isApproved() {
L70: public String getFileName() {
L77: public void actionPerformed(ActionEvent evt) {
L90: @Override
L91: protected void escape() {
L95: private boolean validateInput() {
L113: private void initComponents() {
L156: private Component getCommandButtons() {

## src/main/java/com/myjavaworld/jftp/ZipAndUploadDlg.java

L51: public class ZipAndUploadDlg extends MDialog implements ActionListener,
L52: ItemListener {
L79: public boolean isApproved() {
L83: public String getFileName() {
L90: public boolean getDeleteOption() {
L94: public File getZipFile() {
L115: public void actionPerformed(ActionEvent evt) {
L134: public void itemStateChanged(ItemEvent evt) {
L140: @Override
L141: protected void escape() {
L145: private boolean validateInput() {
L174: private void browse() {
L189: private void initComponents() {
L239: private Component getOptionsPanel() {
L319: private Component getCommandButtons() {

## src/main/java/com/myjavaworld/jftp/actions/AbortAction.java

L35: public class AbortAction implements ActionListener {
L44: public static synchronized AbortAction getInstance(JFTP jftp) {
L53: public void actionPerformed(ActionEvent evt) {
L62: @Override
L63: public Object construct() {
L76: @Override
L77: public void finished() {

## src/main/java/com/myjavaworld/jftp/actions/ChangeLocalDirectoryAction.java

L32: public class ChangeLocalDirectoryAction implements ActionListener {
L41: public static synchronized ChangeLocalDirectoryAction getInstance(JFTP jftp) {
L50: public void actionPerformed(ActionEvent evt) {

## src/main/java/com/myjavaworld/jftp/actions/ChangeRemoteDirectoryAction.java

L32: public class ChangeRemoteDirectoryAction implements ActionListener {
L41: public static synchronized ChangeRemoteDirectoryAction getInstance(JFTP jftp) {
L50: public void actionPerformed(ActionEvent evt) {

## src/main/java/com/myjavaworld/jftp/actions/ConnectAction.java

L33: public class ConnectAction implements ActionListener {
L42: public static synchronized ConnectAction getInstance(JFTP jftp) {
L51: public void actionPerformed(ActionEvent evt) {

## src/main/java/com/myjavaworld/jftp/actions/DeleteLocalFileAction.java

L31: public class DeleteLocalFileAction implements ActionListener {
L40: public static synchronized DeleteLocalFileAction getInstance(JFTP jftp) {
L49: public void actionPerformed(ActionEvent evt) {

## src/main/java/com/myjavaworld/jftp/actions/DeleteRemoteFileAction.java

L32: public class DeleteRemoteFileAction implements ActionListener {
L41: public static synchronized DeleteRemoteFileAction getInstance(JFTP jftp) {
L50: public void actionPerformed(ActionEvent evt) {

## src/main/java/com/myjavaworld/jftp/actions/DisconnectAction.java

L31: public class DisconnectAction implements ActionListener {
L40: public static synchronized DisconnectAction getInstance(JFTP jftp) {
L49: public void actionPerformed(ActionEvent evt) {

## src/main/java/com/myjavaworld/jftp/actions/DownloadAction.java

L31: public class DownloadAction implements ActionListener {
L40: public static synchronized DownloadAction getInstance(JFTP jftp) {
L49: public void actionPerformed(ActionEvent evt) {

## src/main/java/com/myjavaworld/jftp/actions/DownloadAndUnzipAction.java

L36: public class DownloadAndUnzipAction implements ActionListener {
L45: public static synchronized DownloadAndUnzipAction getInstance(JFTP jftp) {
L54: public void actionPerformed(ActionEvent evt) {
L58: private void downloadAndUnzip() {
L87: @Override
L88: public Object construct() {
L107: @Override
L108: public void finished() {

## src/main/java/com/myjavaworld/jftp/actions/DownloadAsAction.java

L34: public class DownloadAsAction implements ActionListener {
L43: public static synchronized DownloadAsAction getInstance(JFTP jftp) {
L52: public void actionPerformed(ActionEvent evt) {
L74: @Override
L75: public Object construct() {
L82: @Override
L83: public void finished() {

## src/main/java/com/myjavaworld/jftp/actions/EditLocalFileAction.java

L34: public class EditLocalFileAction implements ActionListener {
L43: public static synchronized EditLocalFileAction getInstance(JFTP jftp) {
L52: public void actionPerformed(ActionEvent evt) {

## src/main/java/com/myjavaworld/jftp/actions/EditRemoteFileAction.java

L36: public class EditRemoteFileAction implements ActionListener {
L45: public static synchronized EditRemoteFileAction getInstance(JFTP jftp) {
L54: public void actionPerformed(ActionEvent evt) {
L70: @Override
L71: public Object construct() {
L76: @Override
L77: public void finished() {

## src/main/java/com/myjavaworld/jftp/actions/EmailLocalFileAction.java

L30: public class EmailLocalFileAction implements ActionListener {
L39: public static synchronized EmailLocalFileAction getInstance(JFTP jftp) {
L48: public void actionPerformed(ActionEvent evt) {

## src/main/java/com/myjavaworld/jftp/actions/EmailRemoteFileAction.java

L30: public class EmailRemoteFileAction implements ActionListener {
L39: public static synchronized EmailRemoteFileAction getInstance(JFTP jftp) {
L48: public void actionPerformed(ActionEvent evt) {

## src/main/java/com/myjavaworld/jftp/actions/ManageCertificatesAction.java

L32: public class ManageCertificatesAction extends AbstractAction {
L41: public static synchronized ManageCertificatesAction getInstance(JFTP jftp) {
L50: public void actionPerformed(ActionEvent evt) {

## src/main/java/com/myjavaworld/jftp/actions/ManageFavoritesAction.java

L32: public class ManageFavoritesAction extends AbstractAction {
L41: public static synchronized ManageFavoritesAction getInstance(JFTP jftp) {
L50: public void actionPerformed(ActionEvent evt) {

## src/main/java/com/myjavaworld/jftp/actions/NewLocalDirectoryAction.java

L32: public class NewLocalDirectoryAction implements ActionListener {
L41: public static synchronized NewLocalDirectoryAction getInstance(JFTP jftp) {
L50: public void actionPerformed(ActionEvent evt) {

## src/main/java/com/myjavaworld/jftp/actions/NewLocalFileAction.java

L33: public class NewLocalFileAction implements ActionListener {
L43: public static synchronized NewLocalFileAction getInstance(JFTP jftp) {
L52: public void actionPerformed(ActionEvent evt) {

## src/main/java/com/myjavaworld/jftp/actions/NewRemoteDirectoryAction.java

L33: public class NewRemoteDirectoryAction implements ActionListener {
L42: public static synchronized NewRemoteDirectoryAction getInstance(JFTP jftp) {
L51: public void actionPerformed(ActionEvent evt) {

## src/main/java/com/myjavaworld/jftp/actions/NewRemoteFileAction.java

L33: public class NewRemoteFileAction implements ActionListener {
L42: public static synchronized NewRemoteFileAction getInstance(JFTP jftp) {
L51: public void actionPerformed(ActionEvent evt) {

## src/main/java/com/myjavaworld/jftp/actions/NewSessionAction.java

L31: public class NewSessionAction implements ActionListener {
L40: public static synchronized NewSessionAction getInstance(JFTP jftp) {
L49: public void actionPerformed(ActionEvent evt) {

## src/main/java/com/myjavaworld/jftp/actions/OpenLocalFileAction.java

L34: public class OpenLocalFileAction implements ActionListener {
L43: public static synchronized OpenLocalFileAction getInstance(JFTP jftp) {
L52: public void actionPerformed(ActionEvent evt) {

## src/main/java/com/myjavaworld/jftp/actions/OpenRemoteFileAction.java

L36: public class OpenRemoteFileAction implements ActionListener {
L45: public static synchronized OpenRemoteFileAction getInstance(JFTP jftp) {
L54: public void actionPerformed(ActionEvent evt) {
L74: @Override
L75: public Object construct() {
L80: @Override
L81: public void finished() {

## src/main/java/com/myjavaworld/jftp/actions/PrintLocalFileAction.java

L34: public class PrintLocalFileAction implements ActionListener {
L43: public static synchronized PrintLocalFileAction getInstance(JFTP jftp) {
L52: public void actionPerformed(ActionEvent evt) {

## src/main/java/com/myjavaworld/jftp/actions/PrintRemoteFileAction.java

L36: public class PrintRemoteFileAction implements ActionListener {
L45: public static synchronized PrintRemoteFileAction getInstance(JFTP jftp) {
L54: public void actionPerformed(ActionEvent evt) {
L70: @Override
L71: public Object construct() {
L76: @Override
L77: public void finished() {

## src/main/java/com/myjavaworld/jftp/actions/ReconnectAction.java

L32: public class ReconnectAction implements ActionListener {
L41: public static synchronized ReconnectAction getInstance(JFTP jftp) {
L50: public void actionPerformed(ActionEvent evt) {

## src/main/java/com/myjavaworld/jftp/actions/RenameLocalFileAction.java

L34: public class RenameLocalFileAction implements ActionListener {
L43: public static synchronized RenameLocalFileAction getInstance(JFTP jftp) {
L52: public void actionPerformed(ActionEvent evt) {

## src/main/java/com/myjavaworld/jftp/actions/RenameRemoteFileAction.java

L33: public class RenameRemoteFileAction implements ActionListener {
L42: public static synchronized RenameRemoteFileAction getInstance(JFTP jftp) {
L51: public void actionPerformed(ActionEvent evt) {

## src/main/java/com/myjavaworld/jftp/actions/UploadAction.java

L32: public class UploadAction implements ActionListener {
L42: public static synchronized UploadAction getInstance(JFTP jftp) {
L51: public void actionPerformed(ActionEvent evt) {

## src/main/java/com/myjavaworld/jftp/actions/UploadAsAction.java

L34: public class UploadAsAction implements ActionListener {
L43: public static synchronized UploadAsAction getInstance(JFTP jftp) {
L52: public void actionPerformed(ActionEvent evt) {
L74: @Override
L75: public Object construct() {
L82: @Override
L83: public void finished() {

## src/main/java/com/myjavaworld/jftp/actions/ZipAndUploadAction.java

L37: public class ZipAndUploadAction implements ActionListener {
L46: public static synchronized ZipAndUploadAction getInstance(JFTP jftp) {
L55: public void actionPerformed(ActionEvent evt) {
L59: private void zipAndUpload() {
L86: @Override
L87: public Object construct() {
L119: @Override
L120: public void finished() {

## src/main/java/com/myjavaworld/jftp/ssl/CertificateDlg.java

L45: public class CertificateDlg extends MDialog implements ActionListener {
L76: public void actionPerformed(ActionEvent evt) {
L89: private void initComponents() {
L115: private Component getCommandButtons() {

## src/main/java/com/myjavaworld/jftp/ssl/CertificateManagerDlg.java

L73: public class CertificateManagerDlg extends MDialog implements ActionListener,
L74: ListSelectionListener, ChangeListener, MouseListener {
L104: public void actionPerformed(ActionEvent evt) {
L117: public void valueChanged(ListSelectionEvent evt) {
L130: public void stateChanged(ChangeEvent evt) {
L142: @Override
L143: public void windowOpened(WindowEvent evt) {
L148: public void mousePressed(MouseEvent evt) {
L151: public void mouseReleased(MouseEvent evt) {
L154: public void mouseClicked(MouseEvent evt) {
L170: public void mouseEntered(MouseEvent evt) {
L173: public void mouseExited(MouseEvent evt) {
L176: @Override
L177: protected void escape() {
L181: private void viewCertificate() {
L189: private void viewServerCertificate() {
L201: private void viewClientCertificate() {
L213: private void deleteCertificates() {
L221: private void deleteServerCertificates() {
L248: private void deleteClientCertificates() {
L275: private void importCertificates() {
L283: private void importServerCertificates() {
L324: private void importClientCertificates() {
L363: private void initComponents() {
L410: private Component getServerCertificatesTab() {
L498: private Component getCommandButtons() {
L529: class DeleteCertificateAction extends AbstractAction {
L531: public void actionPerformed(ActionEvent evt) {

## src/main/java/com/myjavaworld/jftp/ssl/CertificatePane.java

L41: public class CertificatePane extends JPanel {
L70: public void setCertificateChain(Certificate[] chain) {
L77: public Certificate[] getCertificateChain() {
L81: private void populateScreen() {
L87: private void populateGeneralPanel() {
L102: private void populateIssuerPanel() {
L112: private void populateSubjectPanel() {
L122: private void initComponents() {
L156: private Component getGeneralPanel() {
L249: private Component getIssuerPanel() {
L343: private Component getSubjectPanel() {

## src/main/java/com/myjavaworld/jftp/ssl/CertificateTableModel.java

L37: public class CertificateTableModel extends AbstractTableModel {
L54: public void setKeyStore(KeyStore keyStore) throws KeyStoreException {
L67: public KeyStore getKeyStore() {
L71: public int getColumnCount() {
L75: public int getRowCount() {
L79: @Override
L80: public String getColumnName(int col) {
L84: public Object getValueAt(int row, int col) {
L108: @Override
L109: public Class getColumnClass(int col) {
L116: public Certificate getCertificateAt(int row) {
L125: public String getAliasAt(int row) {

## src/main/java/com/myjavaworld/jftp/ssl/DNParser.java

L24: public class DNParser {
L52: public String getParameter(String param) {
L81: public static String getParameter(String distinguishedName, String param) {

## src/main/java/com/myjavaworld/jftp/ssl/JFTPKeyManager.java

L37: public class JFTPKeyManager implements X509KeyManager {
L50: public PrivateKey getPrivateKey(String alias) {
L54: public X509Certificate[] getCertificateChain(String alias) {
L58: public String[] getClientAliases(String keyType, Principal[] issuers) {
L62: public String[] getServerAliases(String keyType, Principal[] issuers) {
L66: public String chooseServerAlias(String keyType, Principal[] issuers,
L67: Socket socket) {
L71: public String chooseClientAlias(String[] keyType, Principal[] issuers,
L72: Socket socket) {

## src/main/java/com/myjavaworld/jftp/ssl/JFTPSSLContext.java

L35: public class JFTPSSLContext {
L37: public static SSLContext getSSLContext(JFTP jftp, String hostName)
L38: throws KeyManagementException, KeyStoreException,
L39: NoSuchAlgorithmException, UnrecoverableKeyException {

## src/main/java/com/myjavaworld/jftp/ssl/JFTPTrustManager.java

L37: public class JFTPTrustManager implements X509TrustManager {
L67: public X509Certificate[] getAcceptedIssuers() {
L71: public void checkClientTrusted(X509Certificate[] chain, String authType)
L72: throws CertificateException {
L76: public void checkServerTrusted(X509Certificate[] chain, String authType)
L77: throws CertificateException {
L110: private boolean isValidDate(X509Certificate[] chain) {
L130: private boolean isValidHost(X509Certificate[] chain) {
L149: private boolean isTrusted(X509Certificate[] chain) {

## src/main/java/com/myjavaworld/jftp/ssl/KeyStoreManager.java

L34: public class KeyStoreManager {
L41: private static synchronized void init() throws KeyStoreException {
L60: public static synchronized KeyStore getServerCertificateStore()
L61: throws KeyStoreException {
L75: public static synchronized KeyStore getClientCertificateStore()
L76: throws KeyStoreException {
L91: public static synchronized void addServerCertificate(Certificate[] chain)
L92: throws KeyStoreException {
L108: public static synchronized void addClientCertificate(Certificate[] chain)
L109: throws KeyStoreException {
L117: public static synchronized void deleteServerCertificate(String alias)
L118: throws KeyStoreException {
L126: public static synchronized void deleteClientCertificate(String alias)
L127: throws KeyStoreException {
L150: private static synchronized KeyStore getKeyStore(String fileName,
L151: char[] password) throws KeyStoreException {
L170: private static synchronized KeyStore getKeyStore(File file, char[] password)
L171: throws KeyStoreException {
L201: private static synchronized void saveServerCertificateStore()
L202: throws KeyStoreException {
L217: private static synchronized void saveClientCertificateStore()
L218: throws KeyStoreException {
L240: private static synchronized void addCertificate(KeyStore keyStore,
L241: Certificate[] chain) throws KeyStoreException {
L265: private static synchronized String getNextAlias(KeyStore keyStore)
L266: throws KeyStoreException {
L286: private static synchronized void deleteCertificate(KeyStore keyStore,
L287: String alias) throws KeyStoreException {
L303: private static synchronized void saveCertificateStore(File file,
L304: char[] password, KeyStore keyStore) throws KeyStoreException {

## src/main/java/com/myjavaworld/jftp/ssl/SecurityWarningDlg.java

L48: public class SecurityWarningDlg extends MDialog implements ActionListener {
L88: public static int showDialog(Component invoker, Certificate[] chain,
L89: boolean validDate, boolean validHost, boolean trusted) {
L104: public void actionPerformed(ActionEvent evt) {
L120: @Override
L121: protected void escape() {
L125: private void initComponents() {
L233: private Component getCommandButtons() {

## src/main/java/com/myjavaworld/util/CommonResources.java

L25: public class CommonResources {
L30: public static String getString(String key) {

## src/main/java/com/myjavaworld/util/Encoder.java

L22: public class Encoder {
L24: public static String hexEncode(byte[] input) {

## src/main/java/com/myjavaworld/util/FileChangeEvent.java

L24: public class FileChangeEvent extends EventObject {
L37: public File getFile() {
L41: public long getOldDate() {
L45: public long getnewDate() {

## src/main/java/com/myjavaworld/util/FileChangeListener.java

L23: public interface FileChangeListener extends EventListener {
L25: public void fileChanged(FileChangeEvent evt);

## src/main/java/com/myjavaworld/util/FileChangeMonitor.java

L34: public class FileChangeMonitor implements ActionListener {
L45: public synchronized void add(File file) {
L55: public void remove(File file) {
L59: public void addFileChangeListener(FileChangeListener listener) {
L63: public void removeFileChangeListener(FileChangeListener listener) {
L67: public void stopMonitor() {
L73: public void actionPerformed(ActionEvent evt) {
L90: protected void fireFileChanged(FileChangeEvent evt) {

## src/main/java/com/myjavaworld/util/FileUtilities.java

L28: public class FileUtilities {
L30: public static void copyFile(File source, File target) throws IOException {

## src/main/java/com/myjavaworld/util/ProgressEvent.java

L25: public class ProgressEvent extends EventObject {
L34: public int getProgress() {

## src/main/java/com/myjavaworld/util/ProgressListener.java

L25: public interface ProgressListener extends EventListener {
L27: public void progressChanged(ProgressEvent evt);

## src/main/java/com/myjavaworld/util/RandomKeyGenerator.java

L23: public class RandomKeyGenerator {
L38: public static String generate(int length) {
L58: public static String formatKey(String key) {

## src/main/java/com/myjavaworld/util/ResourceLoader.java

L29: public class ResourceLoader {
L31: public static ResourceBundle getBundle(String baseName) {
L35: public static ResourceBundle getBundle(String baseName, Locale locale) {
L45: public static ResourceBundle getBundle(String baseName, Locale locale,
L46: ClassLoader loader) {
L56: private static void fireResourceNotFound(String baseName, Locale locale) {

## src/main/java/com/myjavaworld/util/StatusEvent.java

L25: public class StatusEvent extends EventObject {
L34: public String getStatus() {

## src/main/java/com/myjavaworld/util/StatusListener.java

L25: public interface StatusListener extends EventListener {
L27: public void statusChanged(StatusEvent evt);

## src/main/java/com/myjavaworld/util/StringUtilities.java

L25: public class StringUtilities {
L27: public static String getFormattedMessage(String input) {
L31: public static String getFormattedMessage(String input, int chars) {

## src/main/java/com/myjavaworld/util/SystemUtil.java

L27: public class SystemUtil {
L73: public static boolean isMac() {
L77: public static String getOSName() {
L81: public static String getOSVersion() {
L85: public static String getJREVersion() {
L89: public static String getJREVendor() {
L93: public static String getJavaHome() {
L97: public static String getUserHome() {
L101: public static String getWorkingDirectory() {

## src/main/java/com/myjavaworld/zip/Unzip.java

L36: public class Unzip {
L61: public File getFile() {
L65: public void setTargetDirectory(File targetDirectory) {
L69: public File getTargetDirectory() {
L73: public void addZipListener(ZipListener l) {
L77: public void removeZipListener(ZipListener l) {
L81: public void addProgressListener(ProgressListener l) {
L85: public void removeProgressListener(ProgressListener l) {
L89: protected void fireBeginFileEvent(File file) {
L99: protected void fireEndFileEvent(File file) {
L109: protected void fireProgressEvent(int progress) {
L119: public void open() throws ZipException, IOException {
L126: public void close() throws IOException {
L134: public void unzip() throws IOException {
L153: private void unzipFile(ZipEntry entry) throws IOException {

## src/main/java/com/myjavaworld/zip/Zip.java

L38: public class Zip {
L69: public File getFile() {
L73: public void setFilter(Filter filter) {
L77: public Filter getFilter() {
L81: public void addZipListener(ZipListener l) {
L85: public void removeZipListener(ZipListener l) {
L89: public void addProgressListener(ProgressListener l) {
L93: public void removeProgressListener(ProgressListener l) {
L97: protected void fireBeginFileEvent(File file) {
L107: protected void fireEndFileEvent(File file) {
L117: protected void fireProgressEvent(int progress) {
L133: public File getRelativeTo() {
L144: public void setRelativeTo(File relativeTo) {
L159: public void open() throws IOException {
L172: public void close() throws IOException {
L185: public void addEntry(File file) throws IOException {
L219: private void addFile(File file) throws IOException {
L250: private String computeEntryName(File file) {

## src/main/java/com/myjavaworld/zip/ZipEvent.java

L23: public class ZipEvent extends EventObject {
L36: public int getType() {
L40: public String getFile() {

## src/main/java/com/myjavaworld/zip/ZipListener.java

L23: public interface ZipListener extends EventListener {
L25: public void beginFile(ZipEvent evt);
L27: public void endFile(ZipEvent evt);

## src/test/java/com/myjavaworld/jftp/BehaviorTestCase.java

L12: public abstract class BehaviorTestCase extends TestCase {
L16: private static Path createProfile() {
L26: protected void setUp() throws Exception {
L30: protected File dataFile(String name) {
L34: protected void tearDown() throws Exception {
L42: protected RemoteHost favorite(String name) {
L51: protected void readInAnotherJvm(String operation) throws Exception {

## src/test/java/com/myjavaworld/jftp/ConnectionConfigurationTest.java

L6: public class ConnectionConfigurationTest extends BehaviorTestCase {
L7: public void testNewConnectionUsesPlainFtpAndPassiveMode() {
L17: public void testHostWhitespaceAndMissingCredentialsAreNormalized() {
L28: public void testInvalidPortsFallBackWhileCustomPortIsKept() {
L38: public void testLoginCommandsSkipBlankLinesAndPreserveOrderAndSpaces() {
L48: public void testFtpsConfigurationSurvivesSerialization() throws Exception {

## src/test/java/com/myjavaworld/jftp/FavoritesPersistenceTest.java

L7: public class FavoritesPersistenceTest extends PersistenceTestCase {
L8: public void testSavedFavoritesCanBeReadByAnotherJvm() throws Exception {
L13: public void testFirstUseStartsEmpty() throws Exception {
L17: public void testAddingFavoritesPreservesOrderAndConnectionData() throws Exception {
L34: public void testEditingAndRemovingArePersisted() throws Exception {
L47: public void testNullAndEmptySaveClearExistingFavorites() throws Exception {
L56: public void testLegacyUnencryptedListCanBeReadRepeatedly() throws Exception {
L64: public void testDamagedFavoritesReportIoFailureAndKeepOriginalBytes() throws Exception {

## src/test/java/com/myjavaworld/jftp/LocalFilteringTest.java

L10: public class LocalFilteringTest extends BehaviorTestCase {
L11: private LocalFile file(String name, long modified) throws Exception {
L17: public void testDefaultFilterKeepsFilesAndDirectories() throws Exception {
L22: public void testListingIncludesMatchingFilesAndKeepsNavigationDirectories() throws Exception {
L31: public void testRegexCaseSensitivityIsUserSelectable() throws Exception {
L37: public void testDateRangeIncludesBothBoundariesAndRejectsOutside() throws Exception {
L45: public void testNameAndDateMustBothMatch() throws Exception {
L52: public void testExclusionInvertsFileMatchButKeepsDirectories() throws Exception {
L59: public void testHiddenAttributeParticipatesInInclusionAndExclusion() throws Exception {

## src/test/java/com/myjavaworld/jftp/PersistenceTestCase.java

L6: public abstract class PersistenceTestCase extends BehaviorTestCase {
L7: protected void setUp() throws Exception {

## src/test/java/com/myjavaworld/jftp/PreferencesPersistenceTest.java

L8: public class PreferencesPersistenceTest extends PersistenceTestCase {
L9: public void testPreferencesCanBeReadByAnotherJvm() throws Exception {
L17: public void testFirstUseCreatesUsableDefaults() throws Exception {
L27: public void testConnectionAndTransferSettingsSurviveReload() throws Exception {
L43: public void testUiLocaleDirectoryAndUpdateChoiceSurviveReload() throws Exception {
L56: public void testCertificateAndProxyConfigurationSurvivesWithoutOpeningStores() throws Exception {
L77: public void testSecondSaveReplacesPreviousValues() throws Exception {
L85: public void testDamagedPreferencesCurrentlyFallBackWithoutOverwriting() throws Exception {

## src/test/java/com/myjavaworld/jftp/StateProbe.java

L7: public class StateProbe {
L8: public static void main(String[] args) throws Exception {
L45: private static void require(boolean condition, String message) {

## src/test/java/com/myjavaworld/jftp/SygnityAppearanceTest.java

L15: public class SygnityAppearanceTest extends BehaviorTestCase {
L16: public void testOriginalToolbarActionsRemainInOrder() throws Exception {
L40: public void testDecorativeLogoIsVisibleAtRightWithoutReplacingButtons() throws Exception {
L69: public void testPackagedWordmarkRetainsOriginalAspectRatioAndTransparency() throws Exception {
L78: private static void onEdt(Runnable check) throws Exception {

