# agent_logic/main.py
from flask import Flask, request, jsonify
from graph import build_graph

app = Flask(__name__)
graph = build_graph()

@app.route("/api/query", methods=["POST"])
def query():
    data = request.json
    query_text = data.get("query", "")
    state = {"query": query_text}
    result = graph.invoke({"state": state})
    return jsonify({"response": result.get("final_response", "")})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
