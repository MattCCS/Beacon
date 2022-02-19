
import sqlite3


CONNECTION_STRING = "records.db"
CON = None


def ensure_db_connection(cxn_string=CONNECTION_STRING):
    global CON
    if CON is None:
        set_database(cxn_string)


def set_database(cxn_string):
    global CON
    CON = sqlite3.connect(cxn_string)
    CON.execute(
        "CREATE TABLE IF NOT EXISTS records (\
            id INTEGER PRIMARY KEY AUTOINCREMENT, \
            value VARCHAR NULL, \
            error VARCHAR NULL, \
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP \
        )"
    )


def get_all_ordered_by_recency():
    ensure_db_connection()
    results = CON.execute("SELECT value, error, date FROM records ORDER BY ID DESC")
    try:
        return list(results)
    except IndexError as exc:
        print(exc)
        raise


def insert(value=None, error=None):
    ensure_db_connection()
    CON.execute("INSERT OR REPLACE INTO records(value, error) VALUES (?, ?)", (value, error))
    CON.commit()


def main():
    ensure_db_connection()


if __name__ == '__main__':
    main()
