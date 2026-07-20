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


def fetch_eligible_pipelines():
    with mysql_conn() as conn:
        cur=conn.cursor(sql.cursors.DictCursor)
        cur.execute("select * from pipeline_config where active_flag=1")
        rows=cur.fetchall()
        cur.close()
    return rows



'''def insert_pipeline_execution(pipeline_name=None,status,total_records=None,good_records=None,bad_records=None,error_message=None):
    with mysql_conn() as conn:
        cur=conn.cursor()
        if status=="RUNNING":
            cur.execute(f"insert into pipeline_execution(pipeline_name,status,start_time) values(%s,%s,NOW())")
        elif status=="COMPLETED":
            cur.execute(f"insert into pipeline_execution(status,end_time,total_records,good_records,bad_records) values(%s,NOW(),%s,%s,%s)")
        elif status=="FAILED":
            cur.execute(f"insert into pipeline_execution(status,end_time,total_records,good_records,bad_records,error_message) values(%s,NOW(),%s,%s,%s,%s)")'''



def insert_execution(pipeline_name):
    with mysql_conn() as conn:
        cur=conn.cursor()
        cur.execute("insert into pipeline_execution(pipeline_name,status,start_time) values(%s,%s,NOW())",(pipeline_name,"RUNNING"))
        batch_id=cur.lastrowid
        conn.commit()
        cur.close()
    return batch_id

def update_completed(batch_id,total_records,good_records,bad_records):
    with mysql_conn() as conn:
        cur=conn.cursor()
        cur.execute("update pipeline_execution set status=%s,end_time=NOW(),total_records=%s,good_records=%s,bad_records=%s where batch_id=%s",("COMPLETED",total_records,good_records,bad_records,batch_id))
        conn.commit()
        cur.close()

def update_failed(batch_id,error_message,total_records=0,good_records=0,bad_records=0,):
    with mysql_conn() as conn:
        cur=conn.cursor()
        cur.execute("update pipeline_execution set status=%s,end_time=NOW(),total_records=%s,good_records=%s,bad_records=%s,error_message=%s where batch_id=%s",("FAILED",total_records,good_records,bad_records,error_message,batch_id))
        conn.commit()
        cur.close()