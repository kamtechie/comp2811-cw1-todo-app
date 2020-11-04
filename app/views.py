from app import app, db
from app.models import Task
from flask import Flask, flash, redirect, render_template, request
from datetime import datetime

@app.route('/')
@app.route('/index')
def tasks_list():
    tasks = Task.query.all()
    return render_template('home.html', tasks=tasks)


@app.route('/task', methods=['POST'])
def add_task():
    form = request.form
    print(form);
    if not form["name"] or not form["desc"] or not form["date"]:
        flash('Fields missing for new task', "error")
        return redirect('/')
    task = Task(date_added=datetime.strptime(form["date"], "%Y-%m-%d").date(), title=form["name"], description=form["desc"], isComplete=False)
    db.session.add(task)
    db.session.commit()
    return redirect('/')


@app.route('/toggle', methods=['POST'])
def toggle_status():
    task_id = request.form['task_id']
    task = Task.query.get(task_id)
    task.isComplete = not task.isComplete
    db.session.commit()
    return str(task), 200


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/')


@app.route('/finished')
def resolve_tasks():
    tasks = Task.query.all()
    for task in tasks:
        if not task:
            return redirect('/')
        if not task.done:
            task.done = True
    db.session.commit()
    return redirect('/')
