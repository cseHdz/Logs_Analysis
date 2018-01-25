# Logs_Analysis

## Requirements
Database: news - Data can be found [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

Interpreter: Python 2 or Python 3

Libraries: psycopg2

An environment running PostgreSQL

This project was created using a VirtualBox/Vagrant with Ubuntu 16.04.3 LTS.

## Overview
This repository covers the requirements for Udacity - Full Stack Web Development Project 3.

The project performs the following tasks:
1. List the three most popular articles (sorted by views)
2. List the three most popular authors (sorted by views)
3. List all the dates with a request error rate greater than 1%

To run this project:
- Load the data to the database by running: `psql -d news -f newsdata.sql`
- Run `psql -d news -f logs_views.sql` to create the views
- Run `loganalysis.py` with the line `./logsanalysis.py` or `python logsanalysis.py`

## Views used for Log Analysis

### 1. article_popularity
Join articles and log tables by articles.slug
```sql
CREATE VIEW article_popularity as
select  articles.title,
        count(log.id) as count
from articles
left join (select replace(log.path,'/article/','') as new_path, id from log) log
  on articles.slug = log.new_path
group by articles.title;
```

### 2. author_popularity
Join authors and articles tables by author.id
Count ocurrences by joining tables by articles.slug
```sql
CREATE VIEW author_popularity as
select  authors.name,
        count(log.id) as count
from articles
left join (select replace(log.path,'/article/','') as new_path, id from log) log
  on articles.slug = log.new_path
left join
  authors on articles.author = authors.id
group by authors.name;
```
### 3. request_proportions
Calculate percentage of total for each request on each day
```sql
create view request_proportions as
select log_dt.date,
      log_dt.status,
      count/ sum(count) over(partition by log_dt.date) as percent_total
from (select log.date,
        log.status,
        count(log.id) as count
from (select log.status, log.id, cast(log.time as DATE) date from log) log
group by log.date, log.status) log_dt;
```
