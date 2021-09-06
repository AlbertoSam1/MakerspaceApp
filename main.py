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
from tika import parser
import requests
import json

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

from gui.access.levels import Access

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

        # Temp file
        self.temp_file = None
        self.temp_file_path = None
        self.current_quote_id = None

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check function by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    @Slot("QWebEngineDownloadItem*")
    def on_downloadRequested(self, download):
        # old_path = download.url().path()  # download.path()
        # suffix = QFileInfo(old_path).suffix()
        # path, _ = QFileDialog.getSaveFileName(self, "Save File", old_path, "*." + suffix)
        # this one worked path = "gui/temp_files/temp_quote.pdf"
        self.temp_file_path = "gui/temp_files/temp_quote.pdf"

        if self.temp_file_path:
            download.setPath(self.temp_file_path)
            download.accept()
            download.finished.connect(self.download_upload2monday)

    def download_upload2monday(self):
        raw = parser.from_file(self.temp_file_path)
        text = raw['content'].split("\n")
        self.current_quote_id = None
        p = None

        for i in text:
            if 'Quote No.' in i:
                p = i.split(" ")
                self.current_quote_id = p[-1]

        if p is not None:
            self.monday_file_label_mutation()

    def monday_file_label_mutation(self):
        apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjEyMzM1MzIyMSwidWlkIjoyMzM2NDc0MiwiaWFkIjoiMjAyMS0wOS0wNFQxMzoxNDowMC42MTNaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6OTQ3NDk3MCwicmduIjoidXNlMSJ9.aG-yZgvcVuY1m45UkZwjscOYRmOTVZezt-aoS0m5XX0"
        apiUrl = "https://api.monday.com/v2"
        headers = {"Authorization": apiKey}

        query = '''query ($boardID:Int!, $quoteID:String!) {
        items_by_column_values (board_id:$boardID , column_id: "numbers", column_value: $quoteID) {id name}}'''

        board_id = 1498781623
        vars2 = {
            'boardID': board_id,
            'quoteID': self.current_quote_id
        }

        data = {'query': query, 'variables': vars2}
        r = requests.post(url=apiUrl, json=data, headers=headers)  # make request

        data_1 = r.json()
        column_id = data_1['data']['items_by_column_values'][0]["id"]
        # Upload file based on column ID
        url = "https://api.monday.com/v2/file"
        payload = {
            'query': 'mutation add_file($file: File!, $itemID: Int!) {add_file_to_column(item_id: $itemID, column_id: "files_1", file: $file) {id}}',
            'variables': f'{{"itemID": {column_id}}}', 'map': '{"pdf": "variables.file"}'}

        files = [('pdf', (f"quoteID-{self.current_quote_id}.pdf", open(self.temp_file_path, 'rb'), 'pdf/pdf'))]

        headers = {'Authorization': apiKey, }

        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        # Change status column

        query5 = 'mutation ($myItemID: Int!, $columnVals: JSON!) { change_multiple_column_values (board_id:1498781623, item_id:$myItemID, column_values:$columnVals) { id } }'

        vars = {
            'myItemID': int(column_id),
            'columnVals': json.dumps({
                'status': {'label': 'Waiting Agreement'}
            })
        }

        data = {'query': query5, 'variables': vars}
        requests.post(url=apiUrl, json=data, headers=headers)  # make request
        # Debug
        # print(r.json())

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

            # Change to Page 1 - Select between welcome page view or login page view
            # This might have a bug sometimes
            if self.settings["user_info"]["logged_in"]:
                MainFunctions.set_page(self, self.ui.load_pages.page_10)
            else:
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

        # Monday.com Button
        if btn.objectName() == "btn_monday" or btn.objectName() == "btn_close_left_column":
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
                    menu=self.ui.left_column.menus.menu_4_monday,
                    title="Monday.com Tab",
                    icon_path=Functions.set_svg_icon("icon_file.svg")
                )

        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////
        
        # SETTINGS TITLE BAR
        if btn.objectName() == "btn_top_settings":
            # Toogle Active
            if not MainFunctions.right_column_is_visible(self):
                # Show / Hide
                MainFunctions.toggle_right_column(self)
            else:
                # Show / Hide
                MainFunctions.toggle_right_column(self)

            MainFunctions.set_right_column_menu(self, menu=self.ui.right_column.menu_2)
            # Get Left Menu Btn
            # top_settings = MainFunctions.get_left_menu_btn(self, "btn_settings")
            # top_settings.set_active_tab(False)

        """
        btns = [self.btn_shop_left_1, self.btn_ms_safety_training, self.btn_printing_dashboard,
                self.btn_inventory_overview, self.btn_inventory_search, self.btn_inventory_update,
                self.btn_inventory_append, self.btn_inventory_approve, self.btn_inventory_denied,
                self.btn_monday_left]
        # SETTINGS LOGOUT
        if btn.objectName() == "btn_top_logout":
            if self.settings["user_info"]["logged_in"]:
                self.settings["user_info"]["logged_in"] = False

                # Check if left column is visible
                if MainFunctions.left_column_is_visible(self):
                    # Show/hide
                    MainFunctions.toggle_left_column(self)
                # Check if right column is visible
                if MainFunctions.right_column_is_visible(self):
                    # Show/hide
                    MainFunctions.toggle_right_column(self)

                self.settings["user_info"]["web_view"].page().profile().cookieStore().deleteAllCookies()
                # Access["level"][self.settings["user_info"]["access_level"]]["login_request"][0] = ""
                # Access["level"][self.settings["user_info"]["access_level"]]["login_request"][1] = ""

                for i in btns:
                    i.hide()

                self.settings["user_info"]["web_view"] = None
                MainFunctions.set_page(self, self.ui.load_pages.page_1)"""

        # SETTINGS LOGOUT
        if btn.objectName() == "btn_top_logout":
            # Toogle Active
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
            else:
                btn.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)

            MainFunctions.set_right_column_menu(self, menu=self.ui.right_column.menu_1)

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
