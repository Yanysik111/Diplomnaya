from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    texts = Text.query.order_by(Text.id.desc()).all()
    return render_template('index.html', texts=texts)

@app.route('/add-text', methods=['POST'])
def add_text():
    new_text = Text(text=request.form['text'])
    db.session.add(new_text)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)