import ldap3
from ldap3 import Server, Connection
import psycopg2
from django.conf import settings

image_path = settings.MEDIA_ROOT


def connexion_ad2000(email_util, passw_util):
    server = Server("10.10.10.11", get_info=ldap3.ALL)
    try:
        conn = Connection(server, email_util, passw_util, auto_bind=True)
        if conn:
            ad_2000 = email_util.split("GROUPE-HASNAOUI\\")[1]
            conn.search(
                search_base="dc=groupe-hasnaoui,dc=local",
                search_filter="(sAMAccountName=" + ad_2000 + ")",
                attributes=(
                    "sAMAccountName",
                    "mail",
                    "title",
                    "displayName",
                    "thumbnailPhoto",
                ),
            )

            result_string = str(conn.entries[0])
            Name = result_string.split("displayName: ")[1]
            Name = Name.split("\r\n")[0]
            mail = result_string.split("mail: ")[1]
            mail = mail.split()[0]
            title = result_string.split("title: ")[1]
            title = title.split("\r\n")[0]
            thumbnailPhoto = conn.entries[0].thumbnailPhoto.value
            dict = {"name": Name, "mail": mail, "ad_2000": ad_2000, "title": title}
            if thumbnailPhoto is None:
                dict["thumbnailPhoto"] = ""
            else:
                dict["thumbnailPhoto"] = thumbnailPhoto
                open(f"{image_path}/{ad_2000}.png", "wb").write(
                    conn.entries[0].thumbnailPhoto.value
                )
            msg = dict
        else:
            msg = "deco"
    except Exception:
        msg = "deco"
    return msg


def connexion_email(email_util, passw_util):
    server = Server("10.10.10.11", get_info=ldap3.ALL)
    try:
        conn = Connection(server, email_util, passw_util, auto_bind=True)
        if conn:
            conn.search(
                search_base="dc=groupe-hasnaoui,dc=local",
                search_filter="(sAMAccountName=" + ad_2000 + ")",
                attributes=(
                    "sAMAccountName",
                    "mail",
                    "title",
                    "displayName",
                    "thumbnailPhoto",
                ),
            )
            result_string = str(conn.entries[0])
            Name = result_string.split("displayName: ")[1]
            Name = Name.split("\r\n")[0]
            ad_2000 = result_string.split("sAMAccountName: ")[1]
            ad_2000 = ad_2000.split()[0]
            title = result_string.split("title: ")[1]
            title = title.split("\r\n")[0]
            thumbnailPhoto = conn.entries[0].thumbnailPhoto.value
            dict = {
                "name": Name,
                "mail": email_util,
                "ad_2000": ad_2000,
                "title": title,
            }
            if thumbnailPhoto is None:
                dict["thumbnailPhoto"] = ""
            else:
                dict["thumbnailPhoto"] = thumbnailPhoto
                open(f"{image_path}/{ad_2000}.png", "wb").write(
                    conn.entries[0].thumbnailPhoto.value
                )
            msg = dict
        else:
            msg = "deco"
    except Exception as e:
        msg = e

    return msg
