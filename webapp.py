from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response1")
def render_response1():
        weeks = float(request.args['weeks'])
        reply = weeks * 7
        return render_template('response1.html', response1 = reply)
@app.route("/page1.html")
def render_page1():
    return render_template('page1.html')
@app.route("/page2.html")
def render_page2():
    return render_template('page2.html')

@app.route("/response2")
def render_response2():
   days = float(request.args['days'])
        reply = days * 24
        return render_template('response2.html', response2 = reply)
    return render_template('response2.html', response = reply)
    
    
@app.route("/page3.html")
def render_page3():
    return render_template('page3.html')

@app.route("/response3")
def render_response3():
    minutes = float(request.args['minutes'])
        reply = minutes * 60
        return render_template('response3.html', response3 = reply)
    return render_template('response3.html', response = reply)
                 
if __name__=="__main__":
    app.run(debug=False, port=54321)
