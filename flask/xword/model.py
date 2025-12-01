import DBcm  # type: ignore

import platform

if "aws" in platform.uname().release:
    creds = {
        "user": "c00166672",
        "password": "xwordpasswd",
        "host": "c00166672.mysql.pythonanywhere-services.com",
        "database": "c00166672$default",
    }
else:
    creds = {
        "user": "xworduser",
        "password": "xwordpasswd",
        "host": "localhost",
        "database": "xwordDB",
    }


def add_to_database(p, m):
    SQL = """
        insert into log
        (pattern, matches)
        values
         (%s, %s)       
    """
    with DBcm.UseDatabase(creds) as db:
        db.execute(SQL, (p, m))


def get_log_data(column="ts"):
    SQL = f"""
        select *
        from log
        order by {column} desc
    """
    with DBcm.UseDatabase(creds) as db:
        db.execute(SQL)
        res = db.fetchall()
    return res
