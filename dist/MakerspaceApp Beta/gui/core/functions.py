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

        query = f'''SELECT * FROM private.login_credentials WHERE username = %s;'''
        params = (user,)

        output = connection.select(query, params)

        try:
            if output[0][1] == password:

                '''a_file = open("ResourceDir/app_data.json", "r")
                Globals.app_data = json.load(a_file)
                a_file.close()

                Globals.app_data["app_user"]['username'] = output[0][0]
                Globals.app_data["app_user"]['access'] = output[0][2]

                a_file = open("ResourceDir/app_data.json", "w")
                json.dump(Globals.app_data, a_file, sort_keys=True, indent=4, separators=(',', ': '))
                a_file.close()'''

                parent.settings["user_info"]["username"] = output[0][0]
                parent.settings["user_info"]["access_level"] = output[0][2]

                print(parent.settings["user_info"]["access_level"])

                for i in Access["level"][parent.settings["user_info"]["access_level"]]:
                    try:
                        btns[i].show()
                    except IndexError:
                        break
            else:
                QMessageBox.warning(parent, 'Error', 'Bad user or password')
        except IndexError as error:
            QMessageBox.warning(parent, 'Error', 'Bad user or password')
