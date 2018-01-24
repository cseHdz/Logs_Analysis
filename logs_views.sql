
--
-- Name: article_popularity; Type: VIEW; Schema: public;
-- Join articles and log tables by articles.slug
--

CREATE VIEW article_popularity as
select  articles.title,
        count(log.id) as count
from articles
left join (select replace(log.path,'/article/','') as new_path, id from log) log
  on articles.slug = log.new_path
group by articles.title;

--
-- Name: author_popularity; Type: VIEW; Schema: public;
-- Join authors and articles tables by author.id
-- Count ocurrences by joining tables by articles.slug
--

CREATE VIEW author_popularity as
select  authors.name,
        count(log.id) as count
from articles
left join (select replace(log.path,'/article/','') as new_path, id from log) log
  on articles.slug = log.new_path
left join
  authors on articles.author = authors.id
group by authors.name;

--
-- Name: request_proportions; Type: VIEW; Schema: public;
-- Calculate percentage of total for each request on each day
--
create view request_proportions as
select log_dt.date,
      log_dt.status,
      count/ sum(count) over(partition by log_dt.date) as percent_total
from (select log.date,
        log.status,
        count(log.id) as count
from (select log.status, log.id, cast(log.time as DATE) date from log) log
group by log.date, log.status) log_dt;
