from flask import Flask, request, render_template
import csv

app = Flask(__name__)

def getData(category):
    data = []
    youtuber = ["", "", ""]
    
    if category == "game":
        basic = "/game/DDDD/table.csv"
        youtuber[0] = "DDDD"
        youtuber[1] = "Kimjaewon"
        youtuber[2] = "WoojooHama"
        wc = "../static/Game/DDDD/word_cloud.jpg"
        cor = "../static/Game/DDDD/correlation.jpg"
        sim = "../static/Game/DDDD/similarity.jpg"
    elif category == "mukbang":
        basic = "/mukbang/Hatnim/table.csv"
        youtuber[0] = "Hatnim"
        youtuber[1] = "HongSound"
        youtuber[2] = "HeungSam"
        wc = "../static/Mukbang/Hatnim/word_cloud.jpg"
        cor = "../static/Mukbang/Hatnim/correlation.jpg"
        sim = "../static/Mukbang/Hatnim/similarity.jpg"
    elif category == "comedy":
        basic = "/comedy/Jjw/table.csv"
        youtuber[0] = "Jjw"
        youtuber[1] = "Bms"
        youtuber[2] = "Wootso"
        wc = "../static/comedy/Jjw/word_cloud.jpg"
        cor = "../static/comedy/Jjw/correlation.jpg"
        sim = "../static/comedy/Jjw/similarity.jpg"
    elif category == "animal":
        basic = "/animal/Kang/table.csv"
        youtuber[0] = "Kang"
        youtuber[1] = "SueAndTree"
        youtuber[2] = "Hahaha"
        wc = "../static/Animal/Kang/word_cloud.jpg"
        cor = "../static/Animal/Kang/correlation.jpg"
        sim = "../static/Animal/Kang/similarity.jpg"
    elif category == "beauty":
        basic = "/beauty/Daddoa/table.csv"
        youtuber[0] = "Daddoa"
        youtuber[1] = "Hyojin"
        youtuber[2] = "SsinNim"
        wc = "../static/beauty/Daddoa/word_cloud.jpg"
        cor = "../static/beauty/Daddoa/correlation.jpg"
        sim = "../static/beauty/Daddoa/similarity.jpg"
        pass
    
    file = open("./static/" + basic, "r", encoding="utf8")
    reader = csv.reader(file)
    
    for info in reader:
        info.pop(0)
        data.append(info)
    data = data[1:11]
    file.close()
    
    return (data, wc, cor, sim, youtuber)

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/content/<category>")
def data(category):
    data, wc, cor, sim, youtuber = getData(category)
    return render_template("content.html", category=category, data=data, wc=wc, cor=cor, sim=sim, youtuber=youtuber)

if __name__ == "__main__":
    app.run(debug=True)