# Resource Project

**Movie Reviews**

Attributes:

* name (string)
* review (string)
* rating (string)
* genre (string)
* release_year (string)

## Schema

```sql
CREATE TABLE movies (
id INTEGER PRIMARY KEY,
name TEXT,
review TEXT,
rating TEXT,
genre TEXT,
release_year TEXT);
```

## REST Endpoints

Name                           | Method | Path
-------------------------------|--------|------------------
Retrieve movie collection | GET    | /movies
Retrieve movie member     | GET    | /movies/*\<id\>*
Create movie member       | POST   | /movies
Update movie member       | PUT    | /movies/*\<id\>*
Delete movie member       | DELETE | /movies/*\<id\>*