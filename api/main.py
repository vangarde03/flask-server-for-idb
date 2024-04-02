from flask import Flask, jsonify, request
from flask_cors import CORS
from db_server import execute_query

app = Flask(__name__)
# Allow requests from all origins to the /query endpoint
CORS(app, resources={r"/query": {"origins": "*"}})

# Your existing route and function definition


@app.route('/')
def home():
    return "Hello vercel"


@app.route("/about")
def about():
    return "Hello again"


# @app.route('/query', methods=['GET', 'POST'])
# def query_endpoint():
#     return "HELLO THERE"
#     if request.method == 'GET':
#         print("Received GET request to /query")
#         return jsonify({"message": "GET request received, but this endpoint only accepts POST requests"}), 405

#     data = request.json
#     print("Received request data:", data)
#     query = data.get('query')  # Get the query from the request
#     print("Query:", query)
#     result = execute_query(query)
#     print("Query result:", result)
#     return jsonify(result)


if __name__ == '__main__':
    app.run()