from flask import Flask, render_template

app = Flask(__name__)

# Test Selection
@app.route("/")
@app.route("/test/select")
def test_select():
    return render_template("testselect.html")


# Subject Pages
@app.route("/ms_office")
def ms_office():
    return render_template("Ms_Office.html")


@app.route("/adv_excel")
def adv_excel():
    return render_template("Adv_excel.html")


@app.route("/tally")
def tally():
    return render_template("Tally.html")


@app.route("/daf")
def daf():
    return render_template("DAF.html")


@app.route("/graphics")
def graphics():
    return render_template("Graphics.html")


@app.route("/crash_course")
def crash_course():
    return render_template("Crash_Course.html")


# Result
@app.route("/result")
def result():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)