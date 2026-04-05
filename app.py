from flask import Flask, render_template, request
from recommender import get_recommendations

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    jobs = []
    
    if request.method == 'POST':
        skills = request.form['skills']
        jobs = get_recommendations(skills)
    
    return render_template('index.html', jobs=jobs)

if __name__ == "__main__":
    app.run(debug=True)
    