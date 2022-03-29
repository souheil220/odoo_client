import psycopg2
from psycopg2 import Error
import datetime


class SQLConnexion:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def connection(self):
        try:
            # Connect to an existing database
            connection = psycopg2.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database,
            )

            # Create a cursor to perform database operations
            cursor = connection.cursor()
            # Print PostgreSQL details
            print("PostgreSQL server information")
            print(connection.get_dsn_parameters(), "\n")
            # Executing a SQL query
            cursor.execute("SELECT version();")
            # Fetch result
            record = cursor.fetchone()
            print("You are connected to - ", record, "\n")
            return [cursor, connection]

        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def closeConnection(self, cursor, connection):
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

    def get_bad_clients(self, cursor):
        sqlQuery = """select DISTINCT rp.id,rp.name,x_rc,x_nif,x_nis,x_art,is_person  from (
                      (select id,name,x_rc,x_nif,x_nis,x_art,is_person 
                      from res_partner 
                      where x_rc is null 
                      or x_nif is null 
                      or x_nis is null
                      or x_art is null  )as rp
                      inner join account_invoice 
                      on rp.id = account_invoice.partner_id
                        )"""
        cursor.execute(sqlQuery)
        data = cursor.fetchall()
        return data

    def update_client_infos(
        self,
        cursor,
        connection,
        x_rc,
        x_nif,
        x_nis,
        x_art,
        x_is_professional_non_commercial,
        x_is_professional_identity_ref,
        x_identity_ref_issuing_authority,
        x_identity_ref_delivery_date,
        x_person_identity,
        is_person,
        id,
    ):
        print(type(x_identity_ref_delivery_date))
        sqlQuery = """UPDATE res_partner 
                    SET x_rc = '{}',
                    x_nif = '{}',
                    x_nis = '{}',
                    x_art = '{}',
                    x_is_professional_non_commercial = {},
                    x_is_professional_identity_ref='{}', 
                    x_identity_ref_issuing_authority = '{}',
                    x_identity_ref_delivery_date = '{}',
                    x_person_identity = '{}',
                    is_person = {}
                    where id ={} 
                    """.format(
            x_rc,
            x_nif,
            x_nis,
            x_art,
            x_is_professional_non_commercial,
            x_is_professional_identity_ref,
            x_identity_ref_issuing_authority,
            x_identity_ref_delivery_date,
            x_person_identity,
            is_person,
            id,
        )
        cursor.execute(sqlQuery)
        connection.commit()
