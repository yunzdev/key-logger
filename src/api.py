from flask import Flask, request, jsonify

app = Flask(__name__) #server instance

logs = []


@app.post("/addlogs")

def add_log():
  # Get the JSON data sent from the other side
  new_log = request.get_json()

  if not new_log:
    return jsonify({"error": "No JSON data provided"}), 400

  logs.append(new_log)
  return jsonify({"message": "Log added successfully!", "log": new_log}), 201



@app.get("/logs")

def get_logs():
    return jsonify(logs)





if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000)