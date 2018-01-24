
#!/usr/bin/env python 2.7.12

import psycopg2

DBNAME = "news"

def get_popular_articles():
    """Return the most popular articles, sorted by number of views"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("Select title, count from article_popularity order by count desc")
    results = c.fetchall()
    db.close()
    return results

def get_popular_authors():
    """Return the most popular authors, sorted by number of views"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("Select name, count from author_popularity order by count desc")
    results = c.fetchall()
    db.close()
    return results

def get_errors():
    """Return all days with more than 1 percernt error ocurrences"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("Select date, percent_total from request_proportions where status = '404 NOT FOUND' and percent_total > 0.01")
    results = c.fetchall()
    db.close()
    return results
