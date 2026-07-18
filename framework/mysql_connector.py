import pymysql as sql
from contextlib import contextmanager

mysql={
    "host":"database-1.ctymuoa0sutj.ap-south-2.rds.amazonaws.com",
    "port":"3306",
    "user":"admin",
    "password":"ashu63004",
    "database":"retail_lakehouse_metadata"
}

@contextmanager
def mysql_conn():
    conn=sql.connect(host=mysql["host"],port=int(mysql["port"]),user=mysql["user"],password=mysql["password"],database=mysql["database"])

    try:
        yield conn
    except Exception as e:
        print(f"Error in mysql connection {e}")
    finally:
        conn.close()


def fetch_eligible_table():
    with mysql_conn() as conn:
        cur=conn.cursor(sql.cursors.DictCursor)
        cur.execute("select * from pipeline_config where active_flag=1")
        rows=cur.fetchall()
        cur.close()
    return rows
