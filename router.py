from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def modules_list():
    return render_template('index.html')

@app.route('/chap1/srs')
def chap1_srs():
    return render_template('srs.html')

@app.route('/chap1/cluster')
def chap1_cluster():
    return render_template('cluster.html')

@app.route('/chap1/stratas')
def chap1_stratas():
    return render_template('stratas.html')

@app.route('/chap1/pop_to_sample')
def chap1_pop_to_sample():
    return render_template('pop_to_sample.html')

@app.route('/chap1/pop_to_sample_graduates')
def chap1_pop_to_sample_graduates():
    return render_template('pop_to_sample_graduates.html')

@app.route('/chap1/survey_sample')
def chap1_survey_sample():
    return render_template('survey_sample.html')

if __name__ == '__main__':
    app.run()