
# !/usr/bin/env python 2.7

# Logs analysis

from logsdb import get_popular_articles, get_popular_authors, get_errors
import psycopg2


def main():
    articles_analysis()
    authors_analysis()
    errors_analysis()


def articles_analysis():
    print("\nMost popular articles:\n")
    results = get_popular_articles()

    for record in results:
        print '"{}"'.format(record[0]) + " - " + str(record[1])


def authors_analysis():
    print("\nMost popular authors:\n")
    results = get_popular_authors()

    for record in results:
        print record[0] + " - " + str(record[1])


def errors_analysis():
    print("\nDays with more than 1% errors:\n")
    results = get_errors()

    for record in results:
        print("{:%b %d, %Y}".format(record[0]) + " - " +
              "{0:.1f}%".format(record[1]*100) + " errors")


main()
