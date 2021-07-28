# ///////////////////////////////////////////////////////////////
#
# The theme was made by Wanderson M.Pimienta
# The original proejct with all credits can be found here: 
# PROJECT MADE WITH: Qt Designer and PySide6 (Currently using PySide2 to allow for web integrations)
# V: 0.0.1
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.uis.windows.main_window.functions_main_window import *
import sys
import os

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT PY ONE DARK WINDOWS
# ///////////////////////////////////////////////////////////////
# MAIN WINDOW
from gui.uis.windows.main_window import *

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"
# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check function by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # Get TOP button settings
        top_btn_settings = MainFunctions.get_title_bar_btn(self, "btn_top_settings")

        '''
        Use this when button needs to open a page
        # Button to open page 1
        if btn.objectName() == "btn_home":
            # Select menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Change to Page 1
            MainFunctions.set_page(self, self.ui.load_pages.page_1)'''

        # Button to open page 1
        if btn.objectName() == "btn_home":
            # Select menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Change to Page 1
            MainFunctions.set_page(self, self.ui.load_pages.page_1)

            # Close both side panels
            if MainFunctions.left_column_is_visible(self):
                MainFunctions.toggle_left_column(self)
            if MainFunctions.right_column_is_visible(self):
                MainFunctions.toggle_right_column(self)
            
        # Button to open left column 1 as machine shop
        if btn.objectName() == "btn_machine_shop" or btn.objectName() == "btn_close_left_column":
            # deselect top settings button
            top_btn_settings.set_active(False)

            # Check if left column is visible
            if not MainFunctions.left_column_is_visible(self):
                # Show/hide
                MainFunctions.toggle_left_column(self)
                # Select menu
                self.ui.left_menu.select_only_one(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    # Deselect all tabs
                    self.ui.left_menu.deselect_all_tab()
                    # Show/hide
                    MainFunctions.toggle_left_column(self)

                # select tab
                self.ui.left_menu.select_only_one(btn.objectName())

            # Change left column page
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu=self.ui.left_column.menus.menu_1,
                    title="Machine Shop Tab",
                    icon_path=Functions.set_svg_icon("icon_settings.svg")
                )

        # Button to open left column 2 as 3D printing
        if btn.objectName() == "btn_3dprint" or btn.objectName() == "btn_close_left_column":
            # deselect top settings button
            top_btn_settings.set_active(False)
            # Check if left column is visible
            if not MainFunctions.left_column_is_visible(self):
                # Show/hide
                MainFunctions.toggle_left_column(self)
                # Select menu
                self.ui.left_menu.select_only_one(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    # Deselect all tabs
                    self.ui.left_menu.deselect_all_tab()
                    # Show/hide
                    MainFunctions.toggle_left_column(self)

                # select tab
                self.ui.left_menu.select_only_one(btn.objectName())

            # Change left column page
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu=self.ui.left_column.menus.menu_3_3dprinting,
                    title="3D Print Tab",
                    icon_path=Functions.set_svg_icon("icon_settings.svg")
                )

        # Button to open left column 3 as Inventory
        if btn.objectName() == "btn_inventory" or btn.objectName() == "btn_close_left_column":
            # deselect top settings button
            top_btn_settings.set_active(False)
            # Check if left column is visible
            if not MainFunctions.left_column_is_visible(self):
                # Show/hide
                MainFunctions.toggle_left_column(self)
                # Select menu
                self.ui.left_menu.select_only_one(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    # Deselect all tabs
                    self.ui.left_menu.deselect_all_tab()
                    # Show/hide
                    MainFunctions.toggle_left_column(self)

                # select tab
                self.ui.left_menu.select_only_one(btn.objectName())

            # Change left column page
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu=self.ui.left_column.menus.menu_2_inventory,
                    title="Inventory Tab",
                    icon_path=Functions.set_svg_icon("icon_search.svg")
                )

        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////
        
        # SETTINGS TITLE BAR
        if btn.objectName() == "btn_top_settings":
            # Toogle Active
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
            else:
                btn.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)

            # Get Left Menu Btn            
            # top_settings = MainFunctions.get_left_menu_btn(self, "btn_settings")
            # top_settings.set_active_tab(False)            

        # DEBUG
        print(f"Button {btn.objectName()}, clicked!")

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        print(f"Button {btn.objectName()}, released!")

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec_())