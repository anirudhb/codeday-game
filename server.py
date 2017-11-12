from flask import Flask, request, Response

def serv(pipe):
    app = Flask(__name__)

    @app.route("/cmd", methods=["GET", "PUT", "PATCH", "OPTIONS"])
    def handle_command():
        s = ""
        if request.method == "GET":
            pipe.send({
                "type": "get_var",
                "name": request.args["name"]
            })
            pipe.poll()
            s = str(pipe.recv())
        elif request.method == "PUT":
            pipe.send({
                "type": "set_var",
                "name": request.get_json()["name"],
                "value": request.get_json()["value"]
            })
        elif request.method == "PATCH":
            print(request.data)
            pipe.send({
                "type": "command",
                "cmd": request.get_json()["cmd"]
            })
        resp = Response(s, status=200)
        if request.method == "OPTIONS":
            resp.headers["Access-Control-Allow-Methods"] = "GET, PUT, PATCH"
            resp.headers["Access-Control-Allow-Headers"] = "Content-Type"
        resp.headers["Access-Control-Allow-Origin"] = "*"
        return resp

    app.run(host="0.0.0.0")