from flask import *
app = Flask(__name__)



@app.route('/index.html')
@app.route('/')
def index():
    return render_template("index.html")

# -----------------------------------------
# --             DATA                    --
# -----------------------------------------

@app.route('/data/beneficiary.html')
def beneficiary():
    return render_template("beneficiary.html")

@app.route('/data/inpatient.html')
def inpatient():
    return render_template("inpatient.html")

@app.route('/data/outpatient.html')
def outpatient():
    return render_template("outpatient.html")

@app.route('/data/potential_fraud.html')
def potential_fraud():
    return render_template("potential_fraud.html")



# -----------------------------------------
# --             APP                     --
# -----------------------------------------

if __name__ == "__main__":
    app.run(debug=True)