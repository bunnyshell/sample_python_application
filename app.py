from flask import Flask, render_template
import sys

app = Flask(__name__)

version = ''

try:
    version = "%s.%s" % (sys.version_info.major, sys.version_info.minor)
except Exception as e:
    pass

@app.route('/')
def index():
    return render_template('index.html', version=version)
