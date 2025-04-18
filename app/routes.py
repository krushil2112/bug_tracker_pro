from flask import Blueprint, render_template, request, redirect, url_for
main = Blueprint('main', __name__)

bugs = []

@main.route('/')
def index():
    return render_template('index.html', bugs=bugs)

@main.route('/add', methods=['POST'])
def add_bug():
    title = request.form['title']
    priority = request.form['priority']
    status = 'Open'
    bug = {'id': len(bugs) + 1, 'title': title, 'priority': priority, 'status': status}
    bugs.append(bug)
    return redirect(url_for('main.index'))

@main.route('/update/<int:bug_id>', methods=['POST'])
def update_bug(bug_id):
    status = request.form['status']
    for bug in bugs:
        if bug['id'] == bug_id:
            bug['status'] = status
            break
    return redirect(url_for('main.index'))