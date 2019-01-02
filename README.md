# news-reporting-tool
A Udacity Full Stack Degree project that is an internal reporting tool for a test database for a news website

## Prerequisites
1. Python3
2. Postgresql
3. Psycopg2 python library
4. News database provided by Udacity.com (file too large to upload on GitHub)
5. terminal ie Git bash
6. vagrant/virtual box environment


## How To Use
1. launch your vagrant virtual machine from a terminal by cd'ing into the directory where you downloded it and type `vagrant up`
2. log into the virtual machine by typing `vagrant ssh`
3. create the views specified in `reportingtool.py` 
  a. type `psql -d news` in bash and hit enter
  b. run lines 45-46 in the comments of `reportingtool.py` by copying them from the python file into your bash
  c.repeat b with line 48
4. cd into news-reporting-tool and launch via python `python reportingtoolpage.py`
5. click on one of the three buttons to view the results
