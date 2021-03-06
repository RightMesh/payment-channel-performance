
from flask import Flask, render_template, request
from get_db import *
from get_db_3d import *
import json

app = Flask(__name__)


# @app.route("/,  methods=['GET', 'POST']")
@app.route("/")
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route("/count", methods=['GET'])
def count():
    (count_total,count_details) = get_count()
    result = str(count_total) + '  ' + str(count_details)
    return result

@app.route("/summary", methods=['GET'])
def summary(num=0):
    results = get_summary(num)
    return json.dumps(results)

@app.route("/coststat", methods=['GET'])
def coststat():
    results = get_cost_stat()
    return json.dumps(results)

@app.route("/costmedian", methods=['GET'])
def costmedian():
    results = get_cost_median_stat()
    return json.dumps(results)

@app.route("/costavg", methods=['GET'])
def costavg():
    results = get_cost_avg_stat()
    return json.dumps(results)

@app.route("/gasstat", methods=['GET'])
def gasstat():
    results = get_gas_stat()
    return json.dumps(results)

@app.route("/gasmedian", methods=['GET'])
def gasmedian():
    results = get_gas_median_stat()
    return json.dumps(results)

@app.route("/gasavg", methods=['GET'])
def gasavg():
    results = get_gas_avg_stat()
    return json.dumps(results)

@app.route("/waitingminedtime", methods=['GET'])
def waitingminedtimestat():
    results = get_waiting_mined_time()
    return json.dumps(results)

@app.route("/minedavg", methods=['GET'])
def minedavg():
    results = get_avg_mined_time()
    return json.dumps(results)

@app.route("/minedmedian", methods=['GET'])
def minedmedian():
    results = get_median_mined_time()
    return json.dumps(results)

@app.route("/waitingtime", methods=['GET'])
def waitingtimestat():
    results = get_waiting_time()
    return json.dumps(results)

@app.route("/blockavggas", methods=['GET'])
def blockavggas():
    results = get_block_avg_gas()
    return json.dumps(results)

@app.route("/blockavgcost", methods=['GET'])
def blockavgcost():
    results = get_block_avg_cost()
    return json.dumps(results)

@app.route("/blockandfee", methods=['GET'])
def blockandgas():
    results = get_block_and_fee()
    return json.dumps(results)

####################################################
@app.route("/gasstat3d", methods=['GET'])
def gasstat3d():
    results = get_gas_stat_3d()
    return json.dumps(results)


@app.route("/stat3d", methods=['GET'])
def stat3d():
    results = get_stat_3d()
    return json.dumps(results)
#######################################################

@app.route("/postsummary", methods=['POST'])
def postsummary():
    file = 'data.json'
    result = update_summary(file)
    return ('number of items updated: ' + str(result))

@app.route("/postreport", methods=['POST'])
def postreport():
    result = generate_report(file)
    return ('number of report generated: ' + str(result))   
if __name__ == "__main__":
    
    # Save a copy of summary db whenever the summary container restarts
    file = '/data/test/data.json'
    results = get_summary_all()
    write_to_file(file, results)
    
    # Start flask application with access from localhost
    app.run(host='0.0.0.0')









