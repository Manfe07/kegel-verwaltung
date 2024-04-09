from flask import Flask, send_file, render_template, redirect
import configparser

app = Flask(__name__) 


config = configparser.ConfigParser()
config.read('/config/config.ini')

app.config['SECRET_KEY'] = config['Flask']['SECRET_KEY']
app.config['DEBUG'] = True

@app.route('/',methods = ['GET'])
def index():
    return render_template('index.html')

# main driver function
if __name__ == '__main__':
    app.run()

