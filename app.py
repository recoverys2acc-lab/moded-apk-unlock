from flask import Flask, render_template, redirect

app = Flask(__name__)

SHORTENER_LINK = "https://gplinks.co/ohoczy6"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download')
def download():
    return redirect(SHORTENER_LINK)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    