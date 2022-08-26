import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    Copy staging tables from s3 to redshift.
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    Loads data into facts and dimesion table from staging tables inside redshift.
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Loads configurational details of aws resources. 
    
    - Establishes connection with the sparkify database and gets
    cursor to it.  
    
    - Load data from S3 to staging tables on Redshift. 
    
    - Finally, closes the connection. 
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    print('1. Connected')
    cur = conn.cursor()
    print('2. Created Cursor')
    
    print('3. Loading to staging...')
    load_staging_tables(cur, conn)
    print('3. Loaded to staging - completed')
    print('4. Inserting into tables...')
    insert_tables(cur, conn)
    print('4. Insertion into tables - completed')

    conn.close()
    print('5. Closed the connection')


if __name__ == "__main__":
    main()