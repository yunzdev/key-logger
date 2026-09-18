from flask import Flask, request, jsonify

app = Flask(__name__) #server instance

logs = []

#in lista di tuple
with open("logs/keylog.txt", "r") as f:
    for line in f:
        line = line.strip()

        if "=" not in line:
            continue

        key, value = line.split("=", 1)
        logs.append((key.strip(), value.strip()))

print(logs)


@app.get("/logs")

def get_logs():
    return jsonify(logs)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000)

