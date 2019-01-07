#!/usr/bin/env python3
# database code for the news db
import psycopg2
import datetime
DBNAME = "news"

# What are the most popular articles of all time?
# Return sorted list by most popular article descending
# I am defining most popular as being the article that was visited the most
# By the way this does not include mistypes / failed requests, because
# as attempts to buy records don't count toward record popularity, I
# don't think failed URL requests should count toward article popularity


def get_popular_articles():
    try:
        db = psycopg2.connect(database=DBNAME)
    except:
        psycopg2.DatabaseError,
        print("Failed to connect to database.")
    c = db.cursor()
    c.execute('''SELECT a.slug, count(*) as visits  from
    log as l,
    articles as a
    WHERE a.slug = substr(l.path,10)
    GROUP BY a.slug ORDER BY visits desc;''')
    return c.fetchall()


# Who are the most popular article authors of all time?
# Return sorted list by most popular author descending

def get_popular_authors():
    try:
        db = psycopg2.connect(database=DBNAME)
    except:
        psycopg2.DatabaseError,
        print("Failed to connect to database.")
    c = db.cursor()
    c.execute('''SELECT au.name, count(*) from
    articles as a,
    authors as au,
    log as l
    WHERE a.author = au.id
    and a.slug = substr(l.path, 10)
    GROUP BY au.name
    ORDER BY count(*) desc;
    ''')
    return c.fetchall()

# On which days did more than 1% of requests lead to errors?
# Return sorted list  with day, and % of requests resulting
# in error (descending I'm assuming)

# First, Create the views that will make the error audit run:
# CREATE VIEW requests_per_day as SELECT to_char(time, 'Day, MM-DD-YYYY') as
# day, count(*) as requests FROM log
# GROUP BY day;


# CREATE VIEW errors_per_day as SELECT to_char(time, 'Day, MM-DD-YYYY') as
# day, count(*) as errors FROM log WHERE status != '200 OK'
# GROUP BY day;


def get_error_audit():
    try:
        db = psycopg2.connect(database=DBNAME)
    except:
        psycopg2.DatabaseError,
        print("Failed to connect to database.")
    c = db.cursor()
    c.execute('''
    SELECT r.day, 100 * errors/requests as percent FROM
    requests_per_day as r,
    errors_per_day as e
    WHERE r.day = e.day
    ''')
    return c.fetchall()
