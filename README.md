
# Project: Data Modeling with Postgres

**Sparkify**, *a grown music streaming startup*, has decided to migrate their data and processes to aws cloud. This project aims to build an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights into what songs their users are listening to.


### Quick Start
*Assuming all the aws resources(s3, redshift) required are up and running.* 
1. Add aws redshift database and IAM role info to  `dwh.cfg`.
2. Run `create_tables.py` to create database and respective tables. Old tables will be dropped, if existing.
3. Run `etl.py` to to load data from S3 to staging tables on Redshift and finally to analytics tables on Redshift.
4. Run `analytic.ipynb` to test the analytic queries on the Redshift database.
5. Run `etl.py` to process the entire dataset.

*Recommending to shutdown and delete aws resources if not required instantly.*

### Structure

The file explorer is accessible using the button in left corner of the The repository contains the following elements:

-   `sql_queries.py` defines all the SQL queries required for the creation of the database schema and ETL pipeline.
-   `create_tables.py` creates the Sparkify tables.
-   `dwh.cfg` contains configurational details of aws resources.
-   `etl.py` defines the ETL pipeline. It load data from S3 to staging tables on Redshift. It also load data from staging tables to analytics tables on Redshift.`
-   `analytics.ipynb` runs the analytic queries on the Redshift database



### Database schema

The database contains the following **fact** table:
-   *songplays* - user song plays
```
songplays (
        songplay_id         INTEGER         IDENTITY(0,1)   PRIMARY KEY,
        start_time          TIMESTAMP       NOT NULL SORTKEY DISTKEY,
        user_id             INTEGER         NOT NULL,
        level               VARCHAR,
        song_id             VARCHAR         NOT NULL,
        artist_id           VARCHAR         NOT NULL,
        session_id          INTEGER,
        location            VARCHAR,
        user_agent          VARCHAR
        );
```
*songplays* has foreign keys to the following **dimension** tables:

-   *users*
```
users (
	user_id             INTEGER         NOT NULL SORTKEY PRIMARY KEY,
        first_name          VARCHAR         NOT NULL,
        last_name           VARCHAR         NOT NULL,
        gender              VARCHAR         NOT NULL,
        level               VARCHAR         NOT NULL
);
```
-   *songs*
```
songs (
	song_id             VARCHAR         NOT NULL SORTKEY PRIMARY KEY,
        title               VARCHAR         NOT NULL,
        artist_id           VARCHAR         NOT NULL,
        year                INTEGER         NOT NULL,
        duration            FLOAT
	);
```
-   *artists*
```
artists (
	artist_id           VARCHAR         NOT NULL SORTKEY PRIMARY KEY,
        name                VARCHAR         NOT NULL,
        location            VARCHAR,
        latitude            FLOAT,
        longitude           FLOAT
);
```
-   *time*
```
time (
	start_time          TIMESTAMP       NOT NULL DISTKEY SORTKEY PRIMARY KEY,
        hour                INTEGER         NOT NULL,
        day                 INTEGER         NOT NULL,
        week                INTEGER         NOT NULL,
        month               INTEGER         NOT NULL,
        year                INTEGER         NOT NULL,
        weekday             VARCHAR(20)     NOT NULL
);
```
#### Staging Tables

-   staging_events
-   staging_songs

### Example queries:
```
# load sql extention in jupyter notebook
%load_ext sql

%sql SELECT COUNT(*) FROM staging_events
## count
## 8056

%sql SELECT COUNT(*) FROM artists
## count
## 10025
```