from flask import Flask, render_template, request
from modules import item

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("base.html")


@app.route('/result_page')
def result_page():
    search = request.args.get('search')
    soup = item.search_content(search)
    videos = item.every_video(soup)

    print(search)
    return render_template("result_page.html", search=search, videos = videos)


if __name__ == '__main__':
    app.run(port=5001)
