# Logs_Analysis
Logs Analysis Project

This repository covers the requirements for Udacity - Full Stack Web Development Project 3.
To run this project run `loganalysis.py` on Terminal.

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
### 2. request_proportions
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
