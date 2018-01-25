#! /usr/bin/env python

import psycopg2

DBNAME = "news"


def perform_query(query):
    """Perform query on the deatabase"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def get_popular_articles():
    """Return the most popular articles, sorted by number of views"""
    return perform_query("""
        Select title,
               count
        from article_popularity
        order by count desc
        limit 3""")


def get_popular_authors():
    """Return the most popular authors, sorted by number of views"""
    return perform_query("""
        Select name,
               count
        from author_popularity
        order by count desc""")


def get_errors():
    """Return all days with more than 1 percernt error ocurrences"""
    return perform_query("""
        Select date,
               percent_total
        from request_proportions
        where status = '404 NOT FOUND'
          and percent_total > 0.01""")
