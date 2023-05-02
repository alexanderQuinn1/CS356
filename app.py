from flask import Flask, render_template, request
import pika
import json

app = Flask(__name__)

@app.route('/')
def run_app():
    return render_template('dashboard.html')

@app.route('/dashboard.html')
def run_dashboard():
    return render_template('dashboard.html')

@app.route('/productionLine.html')
def run_productionLine():
    return render_template('productionLine.html')

@app.route('/productionSchedule.html')
def run_productionSchedule():
    return render_template('productionSchedule.html')

@app.route('/qualityAssurance.html')
def run_qualityAssurance():
    return render_template('qualityAssurance.html')

@app.route('/maintenanceLog.html')
def run_maintenanceLog():
    return render_template('maintenanceLog.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)