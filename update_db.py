print("UPDATE DB TOP LEVEL")
#!/usr/bin/env python

from db_connection import update_db


def run():
    update_db()
    print("DONE UPDATING DB")


if __name__ == '__main__':
    print("UPDATE DB STARTING")
    run()
