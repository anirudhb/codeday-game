from flask import Flask, request

def serv(pipe):
    app = Flask(__name__)

    @app.route("/cmd", methods=["GET", "PUT", "PATCH"])
    def handle_command():
        if request.method == "GET":
            pipe.send({
                "type": "get_var",
                "name": request.args["name"]
            })
            pipe.poll()
            return str(pipe.recv())
        elif request.method == "PUT":
            pipe.send({
                "type": "set_var",
                "name": request.get_json()["name"],
                "value": request.get_json()["value"]
            })
            return ""
        elif request.method == "PATCH":
            print(request.data)
            pipe.send({
                "type": "command",
                "cmd": request.get_json()["cmd"]
            })
            return ""

    app.run()