from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('page1.html')

@app.route("/response")
def render_response():
    time_convert_dict = {
        WEEK: {DAY: Decimal('7')},
    }
    return render_template('response1.html', response = reply)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
    
    
@app.route("/")
def render_main():
    return render_template('page2.html')

@app.route("/response")
def render_response():
    time_convert_dict = {
        DAY: {HRS: Decimal('24')},
    }
    return render_template('response2.html', response = reply)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
    
    
    @app.route("/")
def render_main():
    return render_template('page3.html')

@app.route("/response")
def render_response():
    time_convert_dict = {
        HRS: {MIN: Decimal('60')},
    }
    return render_template('response3.html', response = reply)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)

