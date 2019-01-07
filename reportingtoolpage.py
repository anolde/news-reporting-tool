#!/usr/bin/env python3
#
#

from flask import Flask, request, redirect, url_for
import jinja2

from reportingtool import get_popular_articles
from reportingtool import get_popular_authors
from reportingtool import get_error_audit

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>News Articles Tool</title>
    <style>
      h1, form { text-align: center; display: flex; }
      textarea { width: 400px; height: 100px; }
      div.result { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.name { color: #999 }
    </style>
  </head>
  <body>
    <h1>News Reporting Tool</h1>
    <form method=get>
      <div><button name="article" value=1 type="submit")>
      Get Best Articles</button></div>
      <div><button name="author" value=1 type="submit" >
      Get Best Authors</button></div>
      <div><button name="error" value=1 type="submit" >
      See Error Ratio Per Day</button></div>
    </form>
    <!-- post content will go here -->
        %s
        <br>
        %s
  </body>
</html>
'''
# HTML template for a result
result = '''
    <br>
    <div class=result><em class=name>%s</em><br>%s</div>
'''

tableName = '''
    <h2> %s </h2>
'''


@app.route('/', methods=['GET'])
def main():
    '''Main page.'''
    if request.args.get("article"):
        req = get_popular_articles()
        title = "Articles and Number of Requests"
    elif request.args.get("author"):
        req = get_popular_authors()
        title = "Authors and Number of Requests for Their Work"
    elif request.args.get("error"):
        req = get_error_audit()
        title = "Percent of Failed Requests Per Day"
    else:
        req = ""
        title = ""
    results = "".join(result % (column, value) for column, value in req)
    name = "".join(tableName % (title))
    html = HTML_WRAP % (name, results)
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
