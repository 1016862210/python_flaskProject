from flask import Flask, render_template, request
from vsearch import search4letters
# 在chapter3有vsearch的代码
app = Flask(__name__)
# 资源管理页面一共有三个（index、entry、result）

@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results: '
    results = str(search4letters(phrase, letters))
    return render_template('results.html', the_title=title, the_phrase=phrase, the_letters=letters, the_results=results)

@app.route('/')
def index_page():
    return render_template('index.html')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')

if __name__ == '__main__':
    app.run(debug=True)