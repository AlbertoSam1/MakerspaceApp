# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from . functions_main_window import *
import sys
import os

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import *

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from . functions_main_window import *

# DATABASE FUNCTIONS
# ///////////////////////////////////////////////////////////////
from gui.core.functions import *

import asyncio

# PY WINDOW
# ///////////////////////////////////////////////////////////////


class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon" : "icon_home.svg",
            "btn_id" : "btn_home",
            "btn_text" : "Home",
            "btn_tooltip" : "Home page",
            "show_top" : True,
            "is_active" : True
        },
        {
            "btn_icon" : "no_icon.svg",
            "btn_id" : "btn_machine_shop",
            "btn_text" : "Machine Shop",
            "btn_tooltip" : "Machine Shop",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_settings.svg",
            "btn_id" : "btn_3dprint",
            "btn_text" : "3D Printing",
            "btn_tooltip" : "3D Printing",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_search.svg",
            "btn_id" : "btn_inventory",
            "btn_text" : "Inventory",
            "btn_tooltip" : "Open Inventory",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon": "icon_file.svg",
            "btn_id": "btn_monday",
            "btn_text": "Monday.com",
            "btn_tooltip": "Open Monday.com",
            "show_top": True,
            "is_active": False
        },
    ]

    # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        {
            "btn_icon" : "icon_search.svg",
            "btn_id" : "btn_search",
            "btn_tooltip" : "Search",
            "is_active" : False
        },
        {
            "btn_icon" : "icon_settings.svg",
            "btn_id" : "btn_top_settings",
            "btn_tooltip" : "Top settings",
            "is_active" : False
        },
        {
            "btn_icon": "icon_more_options.svg",
            "btn_id": "btn_top_logout",
            "btn_tooltip": "Logout",
            "is_active": False
        }
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])
        
        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to Makerspace App")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "Settings Left Column",
            icon_path = Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # EXAMPLE CUSTOM WIDGETS
        # Here are added the custom widgets to pages and columns that
        # were created using Qt Designer.
        # This is just an example and should be deleted when creating
        # your application.
        #
        # OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
        # You can access objects inside Qt Designer projects using
        # the objects below:
        #
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        ## ADD QLINEEDIT & PUSHBUTTON TO LOGIN FORM
        self.login_user_edit = PyLineEdit(context_color="utsa_ligth_grey_blue")
        self.login_pass_edit = PyLineEdit(context_color="utsa_ligth_grey_blue", )

        self.login_user_edit.setMinimumHeight(25)
        self.login_pass_edit.setMinimumHeight(25)

        self.login_pass_edit.setEchoMode(QLineEdit.Password)

        self.ui.load_pages.main_inputs_frame_layout.addWidget(self.login_user_edit)
        self.ui.load_pages.main_inputs_frame_layout.addWidget(self.login_pass_edit)

        ## ADD MAIN LOGO
        self.logo = QSvgWidget(Functions.set_svg_image("logo_home.svg"))
        self.ui.load_pages.logo_frame_layout.addWidget(self.logo, Qt.AlignCenter, Qt.AlignCenter)

        ## FORMAT WELCOME VIEW && LOGOUT
        self.welcome_image = QSvgWidget(Functions.set_svg_image("SEB_UTSA.svg"))
        self.ui.load_pages.welcome_image_logout_layout.addWidget(self.welcome_image, Qt.AlignCenter)

        # ADD LEFT MENU BUTTONS
        # Buttons openning web pages from inner tabs (ad url handling)

        # ADD WEBVIEW
        self.web_view = PyWebView()
        # self.settings["user_info"]["web_view"] = self.web_view
        # ADD Download Requests
        self.web_view.page().profile().downloadRequested.connect(self.on_downloadRequested)
        # ADD to Layout
        self.ui.load_pages.web_view_page_layout.addWidget(self.web_view)

        def open_web_view(parent, url=None):
            _username = Access["level"][parent.settings["user_info"]["access_level"]]["login_request"][0]
            _password = Access["level"][parent.settings["user_info"]["access_level"]]["login_request"][1]

            parent.btn_monday_left.setDisabled(True)
            try:
                if url is not None:
                    parent.web_view.set_url(url, [_username, _password])
                    # Change to Page 2
            except:
                parent.web_view.change_url(url)
            finally:
                MainFunctions.set_page(parent, self.ui.load_pages.page_2)
                self.btn_monday_left.setDisabled(False)

        ## General Monday.com View Button
        self.btn_monday_left = PyPushButton(
            text="Monday.com",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["utsa_orange"],
            objectName="btn_open_monday"
        )
        self.btn_monday_left.setMinimumHeight(40)
        self.btn_monday_left.clicked.connect(
            lambda: open_web_view(self, url="https://miu2021.monday.com/"))
        # ADD Layout
        self.ui.left_column.menus.monday_tab_layout.addWidget(self.btn_monday_left)
        self.btn_monday_left.hide()

        ## MACHINE SHOP

        # Job Dashboard
        self.btn_shop_left_1 = PyPushButton(
            text="Jobs Dashboard",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["utsa_orange"],
            objectName="btn_open_webview"
        )
        self.btn_shop_left_1.setMinimumHeight(40)
        self.btn_shop_left_1.clicked.connect(
            lambda: open_web_view(self, url="https://miu2021.monday.com/boards/1498781623"))
        # ADD Layout
        self.ui.left_column.menus.btn_ms_leftcol_layout.addWidget(self.btn_shop_left_1)
        self.btn_shop_left_1.hide()

        # Safety Training
        self.btn_ms_safety_training = PyPushButton(
            text="Safety Training",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["utsa_orange"],
            objectName="btn_safety_records_ms"
        )
        self.btn_ms_safety_training.setMinimumHeight(40)
        self.btn_ms_safety_training.clicked.connect(
            lambda: MainFunctions.set_page(self, self.ui.load_pages.page_3))
        # ADD Layout
        self.ui.left_column.menus.btn_safety_training_ms_layout.addWidget(self.btn_ms_safety_training)
        self.btn_ms_safety_training.hide()

        ## 3D Printing
        # Jobs Dashboard
        self.btn_printing_dashboard = PyPushButton(
            text="Jobs Dashboard",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["utsa_orange"],
            objectName="btn_3d_print_jobs"
        )
        self.btn_printing_dashboard.setMinimumHeight(40)
        self.btn_printing_dashboard.clicked.connect(
            lambda: open_web_view(self, url="https://miu2021.monday.com/boards/1637009663"))

        # ADD Layout
        self.ui.left_column.menus.btn_printing_dashboard_layout.addWidget(self.btn_printing_dashboard)
        self.btn_printing_dashboard.hide()

        ## ///////////////////////////////////////////////////////////////////////////////////
        ## Inventory
        # Overview
        self.btn_inventory_overview = PyPushButton(
            text="Inventory Overview",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["utsa_orange"],
            objectName="btn_inventory_overview"
        )
        self.btn_inventory_overview.setMinimumHeight(40)
        self.btn_inventory_overview.clicked.connect(
            lambda: MainFunctions.set_page(self, self.ui.load_pages.page_4))
        # ADD Layout
        self.ui.left_column.menus.btn_inventory_overview_layout.addWidget(self.btn_inventory_overview)
        self.btn_inventory_overview.hide()

        # Search
        self.btn_inventory_search = PyPushButton(
            text="Search Inventory",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["utsa_orange"],
            objectName="btn_search_inventory"
        )
        self.btn_inventory_search.setMinimumHeight(40)
        self.btn_inventory_search.clicked.connect(lambda: MainFunctions.set_page(self, self.ui.load_pages.page_5))
        # ADD Layout
        self.ui.left_column.menus.btn_inventory_search_layout.addWidget(self.btn_inventory_search)
        self.btn_inventory_search.hide()

        # Append
        self.btn_inventory_append = PyPushButton(
            text="Append Inventory",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["utsa_orange"],
            objectName="btn_append_inventory"
        )
        self.btn_inventory_append.setMinimumHeight(40)
        self.btn_inventory_append.clicked.connect(lambda: MainFunctions.set_page(self, self.ui.load_pages.page_5))
        # ADD Layout
        self.ui.left_column.menus.btn_inventory_search_layout.addWidget(self.btn_inventory_append)
        self.btn_inventory_append.hide()

        # Update
        self.btn_inventory_update = PyPushButton(
            text="Update Inventory",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["utsa_orange"],
            objectName="btn_update_inventory"
        )
        self.btn_inventory_update.setMinimumHeight(40)
        self.btn_inventory_update.clicked.connect(lambda: MainFunctions.set_page(self, self.ui.load_pages.page_6))
        # ADD Layout
        self.ui.left_column.menus.btn_inventory_update_layout.addWidget(self.btn_inventory_update)
        self.btn_inventory_update.hide()

        # Append
        self.btn_inventory_append = PyPushButton(
            text="Append Inventory",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["utsa_orange"],
            objectName="btn_append_inventory"
        )
        self.btn_inventory_append.setMinimumHeight(40)
        self.btn_inventory_append.clicked.connect(lambda: MainFunctions.set_page(self, self.ui.load_pages.page_7))
        # ADD Layout
        self.ui.left_column.menus.btn_inventory_append_layout.addWidget(self.btn_inventory_append)
        self.btn_inventory_append.hide()

        # Approve
        self.btn_inventory_approve = PyPushButton(
            text="Approve Inventory",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["utsa_orange"],
            objectName="btn_approve_inventory"
        )
        self.btn_inventory_approve.setMinimumHeight(40)
        self.btn_inventory_approve.clicked.connect(lambda: MainFunctions.set_page(self, self.ui.load_pages.page_8))
        # ADD Layout
        self.ui.left_column.menus.btn_inventory_approve_layout.addWidget(self.btn_inventory_approve)
        self.btn_inventory_approve.hide()

        # Denied
        self.btn_inventory_denied = PyPushButton(
            text="Denied Inventory",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["utsa_orange"],
            objectName="btn_denied_inventory"
        )
        self.btn_inventory_denied.setMinimumHeight(40)
        self.btn_inventory_denied.clicked.connect(lambda: MainFunctions.set_page(self, self.ui.load_pages.page_9))
        # ADD Layout
        self.ui.left_column.menus.btn_inventory_denied_layout.addWidget(self.btn_inventory_denied)
        self.btn_inventory_denied.hide()

        def handle_logout(parent, btns):
            parent.web_view.page().profile().cookieStore().deleteAllCookies()
            parent.web_view.loaded = False
            parent.web_view.page().deleteLater()

            MainFunctions.set_page(parent, parent.ui.load_pages.page_1)

            parent.settings["user_info"]["logged_in"] = False

            # Check if left column is visible
            if MainFunctions.left_column_is_visible(parent):
                # Show/hide
                MainFunctions.toggle_left_column(parent)
            # Check if right column is visible
            if MainFunctions.right_column_is_visible(parent):
                # Show/hide
                MainFunctions.toggle_right_column(parent)

            for i in btns:
                try:
                    i.hide()
                except IndexError:
                    break

        # ADD BUTTON FOR LOGOUT
        self.btn_logout = PyPushButton(
            text="Log Out",
            radius=10,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["utsa_orange"],
            objectName="btn_logout"
        )

        self.btn_logout.setMinimumHeight(40)
        btns = [self.btn_shop_left_1, self.btn_ms_safety_training, self.btn_printing_dashboard,
                self.btn_inventory_overview, self.btn_inventory_search, self.btn_inventory_update,
                self.btn_inventory_append, self.btn_inventory_approve, self.btn_inventory_denied,
                self.btn_monday_left, self.btn_logout]
        self.btn_logout.clicked.connect(lambda: handle_logout(self, btns))
        self.ui.right_column.logout_btn_layout.addWidget(self.btn_logout)

        # ADD BUTTON FOR LOGIN
        self.btn_login = PyPushButton(
            text="Log In",
            radius=10,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["utsa_orange"],
            objectName="btn_login"
        )

        self.btn_login.setMinimumHeight(40)
        self.btn_login.clicked.connect(lambda: Functions.handle_login(self,
                                                                      self.login_user_edit.text(),
                                                                      self.login_pass_edit.text(),
                                                                      btns))
        self.ui.load_pages.login_frame_layout.addWidget(self.btn_login)

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////

    # ADD WEBVIEW

    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)

