from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET','POST'])
def top():
    return render_template('top.html')

@app.route('/math')
def math():
    return render_template('math.html')

@app.route('/complex1')
def complex1():
    return render_template('complex1.html')

@app.route('/complex2')
def complex2():
    return render_template('complex2.html')

@app.route('/complex3')
def complex3():
    return render_template('complex3.html')

@app.route('/machineLearning1')
def machineLearning1():
    return render_template('machineLearning1.html')



def main():
    app.debug = False
    app.run()

if __name__ == '__main__':
    main()
