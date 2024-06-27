from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

problems = [
    {'id': 1, 'question': '2 + 2 = ?', 'answer': '4'},
    {'id': 2, 'question': '3 * 5 = ?', 'answer': '15'}
]


@app.route('/')
def index():
    return render_template('index.html', problems=problems)


@app.route('/check_answer', methods=['POST'])
def check_answer():
    problem_id = int(request.form['problem_id'])
    user_answer = request.form['answer']

    for problem in problems:
        if problem['id'] == problem_id:
            if user_answer == problem['answer']:
                flash('정답입니다!', 'success')
            else:
                flash('오답입니다. 다시 시도해 주세요.', 'danger')
            break

    return render_template('index.html', problems=problems)

if __name__ == '__main__':
    app.run(debug=True)
