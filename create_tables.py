import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Loads configurational details of aws resources. 
    
    - Establishes connection with the sparkify database and gets
    cursor to it.  
    
    - Drops all the tables, if existing.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    print('1. Connected')
    cur = conn.cursor()
    print('2. Created Cursor')
    
    print('3. Dropping tables if already exists...')
    drop_tables(cur, conn)
    print('3. Drop tables if already exists - completed')
    print('4.Creating tables...')
    create_tables(cur, conn)
    print('4.Creation of tables - completed')
    
    conn.close()
    print('5. Closed the connection')


if __name__ == "__main__":
    main()