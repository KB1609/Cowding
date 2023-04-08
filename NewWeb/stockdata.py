from flask import Flask, redirect,Blueprint, url_for, render_template, request
import yfinance as yf
import pandas as pd 
import os 

stockdata = Blueprint('stockdata', __name__)

print(os.getcwd())

# datas= yf.download("AAPL", period="10y")
# dataku = list(datas.to_records(index=False))

# data_tuple = tuple(dataku)
# print(data_tuple)

@stockdata.route("/prediction")
def prediction():
    datas= yf.download("BBRI.JK", period="1y")

    labels = datas.index.strftime('%Y-%m-%d').tolist()
    values = datas['Adj Close'].tolist()


    # labels = [row[0] for row in data_tuple]
    # values = [row[5] for row in data_tuple]
    
    return render_template("predict.html",labels = labels, values = values )

# print (historical_data.tail(5))

# downloadfromyfinance = yf.download("AAPL", period='2y')

# down1 = yf.download("AAPL", period='1w')
# print(down1)

# down = yf.Ticker("AAPL")
# downdata = down.history(period='1w')
# downdata.to_csv('D:/Kuliah/Semester 8/#SKRIPSI/#DEV/Web/Cowding/NewWeb/data/datatest.csv')

@stockdata.route("/search", methods = ["POST", "GET"])
def searchstock():

    if request.method == "POST":
        stocks = request.form["search"]

        #get data from yahoo finance
        datas= yf.download(f"{stocks}", period="1y")
        if datas.empty:
            checksymbol = "not valid"
            return render_template("searchstock.html",checksymbol = checksymbol)
        else:
            checksymbol = "valid"
            print(datas)
            datas_sorted = datas.sort_values(by='Date', ascending=False)


            # Get the company name
            company_info = yf.Ticker(stocks)        
            company_name = company_info.info['longName']

            labels = datas.index.strftime('%Y-%m-%d').tolist()
            values = datas['Adj Close'].tolist()

            # pack variables into dictionary 
            mydata = {
                'labels' : labels,
                'values' : values,
                'symbol' : stocks,
                'company_name' : company_name
            }
            return render_template("searchstock.html", checksymbol = checksymbol, mydata = mydata, dataframe = datas_sorted.to_html())
    else:
        return render_template("index.html")

   


    # labels = [row[0] for row in data_tuple]
    # values = [row[5] for row in data_tuple]
    
    # return render_template("predict.html",labels = labels, values = values )


@stockdata.route("/chsearch", methods = ["POST", "GET"])
def checksearchstock():

    if request.method == "POST":
        stocks = request.form["search"]
        #get data from yahoo finance
        datas= yf.download(f"{stocks}", period="1y")
        if datas.empty:
            return render_template("base.html", checksymbol = "not valid")
        else:
            return render_template("base.html", checksymbol = "valid")

    else:
        return render_template("index.html")