# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import os

from qt_core import *
from gui.core.database_functions import Database
from gui.core.json_settings import Settings
from gui.access.levels import Access


# APP FUNCTIONS
# ///////////////////////////////////////////////////////////////
class Functions:
    settings = Settings()
    settings = settings.items

    # SET SVG ICON
    # ///////////////////////////////////////////////////////////////
    @staticmethod
    def set_svg_icon(icon_name):
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/svg_icons/"
        path = os.path.join(app_path, folder)
        icon = os.path.normpath(os.path.join(path, icon_name))
        return icon

    # SET SVG IMAGE
    # ///////////////////////////////////////////////////////////////
    @staticmethod
    def set_svg_image(icon_name):
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/svg_images/"
        path = os.path.join(app_path, folder)
        icon = os.path.normpath(os.path.join(path, icon_name))
        return icon

    # SET IMAGE
    # ///////////////////////////////////////////////////////////////
    @staticmethod
    def set_image(image_name):
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/images/"
        path = os.path.join(app_path, folder)
        image = os.path.normpath(os.path.join(path, image_name))
        return image

    # HANDLE LOGIN
    # ///////////////////////////////////////////////////////////////
    @staticmethod
    def handle_login(parent, user, password, btns):
        connection = Database()

        try:
            query = f'''SELECT * FROM private.login_credentials WHERE username = %s;'''
            params = (user,)
            output = connection.select(query, params)
        except TimeoutError:
            output = None

        try:
            if output is None:
                output = [["", ""]]
                output[0][1] = "#########"
            if output[0][1] == password:

                parent.settings["user_info"]["username"] = output[0][0]
                parent.settings["user_info"]["access_level"] = output[0][2]

                for i in Access["level"][parent.settings["user_info"]["access_level"]]["pages"]:
                    try:
                        btns[i].show()
                    except IndexError:
                        break

                '''_username = Access["level"][parent.settings["user_info"]["access_level"]]["login_request"][0]
                _password = Access["level"][parent.settings["user_info"]["access_level"]]["login_request"][1]

                parent.web_view.set_url("https://miu2021.monday.com/auth/login_monday/email_password",
                                        [_username, _password])'''
                parent.ui.load_pages.pages.setCurrentWidget(parent.ui.load_pages.page_10)
                parent.settings["user_info"]["logged_in"] = True
            else:
                QMessageBox.warning(parent, 'Error', 'Bad user or password')
        except IndexError as error:
            print(error)
            QMessageBox.warning(parent, 'Error', 'Bad user or password')

        finally:
            parent.login_user_edit.clear()
            parent.login_pass_edit.clear()
