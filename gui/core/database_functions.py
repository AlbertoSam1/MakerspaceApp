# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import psycopg2
from gui.core.json_settings import Settings

# DATABASE FUNCTIONS
# ///////////////////////////////////////////////////////////////


class Database:
    def __init__(self) -> None:
        settings = Settings()
        self.settings = settings.items

    def select(self, sql, params):
        results = None
        connection = None
        cursor = None

        try:
            # DATABASE_CREDENTIALS is import at the beginning of the script from system_info module
            connection = psycopg2.connect(user=self.settings["database_info"]['user'],
                                          password=self.settings["database_info"]['password'],
                                          host=self.settings["database_info"]['host'],
                                          port=self.settings["database_info"]['port'],
                                          database=self.settings["database_info"]['database'])

            cursor = connection.cursor()
            # print(cursor.mogrify(sql, params))
            query = cursor.mogrify(sql, params)
            cursor.execute(query)

            results = cursor.fetchall()
            connection.commit()

        except (Exception, psycopg2.Error) as error:
            print("Error fetching data from PostgreSQL: ", error)

        finally:
            # closing database connection
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed \n")

                return results
