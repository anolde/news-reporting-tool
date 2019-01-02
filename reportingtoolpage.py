#!/usr/bin/env python3
#
#

from flask import Flask, request, redirect, url_for

from reportingtool import get_popular_authors, get_error_audit, get_popular_articles
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
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.date { color: #999 }
    </style>
  </head>
  <body>
    <h1>News Reporting Tool</h1>
    <form method=get>
      <div><button name="article" value=1 type="submit")>Get Best Articles</button></div>
      <div><button name="author" value=1 type="submit" >Get Best Authors</button></div>
      <div><button name="error" value=1 type="submit" >See Error Ratio Per Day</button></div>
    </form>
    <!-- post content will go here -->
%s
  </body>
</html>
'''

# HTML template for response
POST = '''\
    <div class=post><em class=date>%s</em><br>%s</div>
'''


@app.route('/', methods=['GET'])
def main():
    '''Main page.'''
    if request.args.get("article"):
        results = get_popular_articles()
    elif request.args.get("author"):
        results = get_popular_authors()
    elif request.args.get("error"):
        results = get_error_audit()
    else:
        results = ""
    html = HTML_WRAP % results
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
