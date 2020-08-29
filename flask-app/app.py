import os
from flask import Flask, render_template, url_for
app = Flask(__name__)



@app.route('/index.html')
@app.route('/')
def index():
    return render_template("index.html")


# -----------------------------------------
# --            ANALYSIS                 --
# -----------------------------------------
@app.route('/by_state.html')
def by_state():
    return render_template("by_state.html")

@app.route('/common_codes.html')
def common_codes():
    return render_template("common_codes.html")

# -----------------------------------------
# --              ERD                    --
# -----------------------------------------
@app.route('/erd.html')
def erd():
    return render_template("erd.html")

# -----------------------------------------
# --             DATA                    --
# -----------------------------------------

@app.route('/beneficiary.html')
def beneficiary():
    return render_template("beneficiary.html")

@app.route('/inpatient.html')
def inpatient():
    return render_template("inpatient.html")

@app.route('/outpatient.html')
def outpatient():
    return render_template("outpatient.html")

@app.route('/potential_fraud.html')
def potential_fraud():
    return render_template("potential_fraud.html")


# -----------------------------------------
# --             APP                     --
# -----------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
else:
    app.run()