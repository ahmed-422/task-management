from flask import Flask, render_template, request, redirect, url_for,session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,static_folder="assets")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
db =SQLAlchemy(app)

class TaskItem(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    completed = db.Column(db.Boolean, default = False)

    def __repr__(self):
        return f'<TaskItem {self.id}'


@app.route('/', methods =['GET','POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        if content.strip() != '':
            new_item = TaskItem(content = content)
            db.session.add(new_item)
            db.session.commit()
            return redirect('/')
    
    items = TaskItem.query.all()
    print(items)
    return render_template('index.html', items = items)
    

@app.route('/complete_task/<int:item_id>')
def complete_task(item_id):
    item = TaskItem.query.get_or_404(item_id)
    item.completed = True
    db.session.commit()

   
    return redirect('/')


@app.route('/edit_task/<int:item_id>')
def edit_task(item_id):
    item = TaskItem.query.get_or_404(item_id)
    return redirect('/')

@app.route('/delete_task/<int:item_id>',methods =('GET','POST'))
def delete_task(item_id):
    item = TaskItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
