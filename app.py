from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

def run_systemctl_command(command):
    # This function runs the necessary systemctl commands
    result = subprocess.run(['sudo', 'systemctl', command, 'minecraft'], capture_output=True, text=True)
    return result.stdout

@app.route('/')
def index():
    # Check the status of the Minecraft service
    status_output = run_systemctl_command('status')
    if 'active (running)' in status_output:
        status = "ON"
    else:
        status = "OFF"
    return render_template('web_form.html', status=status)

@app.route('/start')
def start_server():
    run_systemctl_command('start')
    return redirect(url_for('web_form'))

@app.route('/stop')
def stop_server():
    run_systemctl_command('stop')
    return redirect(url_for('web_form'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
