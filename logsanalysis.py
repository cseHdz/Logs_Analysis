#! /usr/bin/env python

# Logs analysis

from logsdb import get_popular_articles, get_popular_authors, get_errors
import psycopg2


def main():
    articles_analysis()
    authors_analysis()
    errors_analysis()


def articles_analysis():
    """ List the most popular articles by number of views"""
    print("\nMost popular articles:\n")
    results = get_popular_articles()

    for title, views in results:
        print '"{}"'.format(title) + " - " + str(views)


def authors_analysis():
    """ List the most popular authors by number of views"""
    print("\nMost popular authors:\n")
    results = get_popular_authors()

    for author, views in results:
        print author + " - " + str(views)


def errors_analysis():
    """ List all days with more than 1% errors"""
    print("\nDays with more than 1% errors:\n")
    results = get_errors()

    for date, percentage in results:
        print("{:%b %d, %Y}".format(date) + " - " +
              "{0:.1%}".format(percentage) + " errors")


main()
