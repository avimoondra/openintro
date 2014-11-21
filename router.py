from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
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

@app.route('/chap1/blocking')
def chap1_blocking():
    return render_template('blocking.html')

@app.route('/chap1/scatter_example')
def chap1_scatter():
    return render_template('scatter_example.html')

@app.route('/chap1/email50_lines_vs_chars')
def chap1_email50_lines_vs_chars():
    return render_template('email50_lines_vs_chars.html')

@app.route('/chap1/cars_price_vs_weight')
def chap1_cars_price_vs_weight():
    return render_template('cars_price_vs_weight.html')

@app.route('/chap1/emailCharsDotPlot')
def chap1_emailCharsDotPlot():
    return render_template('emailCharsDotPlot.html')

@app.route('/chap1/emailCharsDotPlotStacked')
def chap1_emailCharsDotPlotStacked():
    return render_template('emailCharsDotPlotStacked.html')

@app.route('/chap1/singleBiMultiModalPlots')
def chap1_singleBiMultiModalPlots():
    return render_template('singleBiMultiModalPlots.html')

if __name__ == '__main__':
    app.run()
