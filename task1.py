#-*- coding: utf-8 -*-
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/AnnTask1',methods=['GET','POST'])
def main_page():
    a, b, res = '','',''
    
    if request.method == 'POST':
        a = request.form.get('a')     
        b = request.form.get('b')  
        
        res = -1
        if 'summa' in request.form:
            res = str(a + b)
        else:
            res = str(a - b) 
        
    return render_template('main_page.html',params={'a':a,'b':b,'res':res})

if __name__ == '__main__':
    app.run()
