# Pour la compilation par Nuitka ou PyInstaller
import os, sys
def get_resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
        if hasattr(sys, '_MEIPASS'):
            base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

from flask import Flask, Response, request
import dumbaiss, sys
import webview

app = Flask("DumbAIss")
window = None

back, blacklist, dico, rep, question, synonyme, blackwords = dumbaiss.setup()

html = Response(open(get_resource_path("./files/index.html"), encoding="utf-8").read(), content_type='text/html')
css = Response(open(get_resource_path("./files/style.css"), encoding="utf-8").read(), content_type='text/css')
js = Response(open(get_resource_path("./files/script.js"), encoding="utf-8").read(), content_type='application/javascript')
jq = Response(open(get_resource_path("./files/jquery.js"), encoding="utf-8").read(), content_type='application/javascript')

@app.route("/")
def home():
    return html

@app.route("/style.css")
def style():
    return css

@app.route("/jquery.js")
def jquery():
    return jq

@app.route("/script.js")
def script():
    return js

@app.route("/api/close")
def close():
    global back, blacklist, dico, rep, question, synonyme, blackwords, window

    if window:
        dumbaiss.close(blacklist, dico, rep, question, synonyme)
        window.destroy()
        return {"status": "200"}
    else:
        return {"status": "400"}

@app.route("/api/reset")
def reset():
    global back, blacklist, dico, rep, question, synonyme, blackwords
    back, blacklist, dico, rep, question, synonyme, blackwords = dumbaiss.setup()

    return {"status": "200"}

@app.route("/api/ask")
def ask():
    global back, blacklist, dico, rep, question, synonyme, blackwords
    inter = request.args.get('question')
    reponse1, reponse = dumbaiss.liste(inter)

    if rep == -1:
        return {"status": "404"}
    else:
        choix = dumbaiss.scan(back, reponse1, blacklist, rep, question, synonyme, blackwords, reponse)
        verif, nombre, dico, rep, choisitexte = dumbaiss.chose(dico, rep, choix)

        if verif == False:
            return {"status": "200", "response": choisitexte}
        else:
            return {"status": "404"}

@app.route("/api/learn")
def learn():
    global back, blacklist, dico, rep, question, synonyme, blackwords
    inter = request.args.get('question')
    _input = request.args.get('response')
    reponse1, reponse = dumbaiss.liste(inter)

    if rep == -1:
        back, dico, rep, question = dumbaiss._first(dico, rep, question, reponse, _input)
    else:
        back, dico, rep, question, reponse = dumbaiss._ask(back, dico, rep, question, reponse, _input)
    
    return {"status": "200"}

if __name__ == "__main__":
    window = webview.create_window("DumbAIss", app, resizable=False, frameless=True, easy_drag=False)
    webview.start(ssl=True, gui="qt")
