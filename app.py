from flask import Flask, render_template, Response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/listen')
def listen():
    global count
    return {"attendence_list": list(attendence_set)}


def main():
    app.run(port=5000, debug=False)


if __name__ == "__main__":
    main()
