from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def top():
    return render_template('top.html')

@app.route('/high_math')
def high_math():
    return render_template('high_math.html')



def main():
    app.debug = True
    app.run()

if __name__ == '__main__':
    main()
