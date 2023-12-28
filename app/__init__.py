from flask import Flask, jsonify

app = Flask(__name__)
application_online = True


# Endpoint returns a JSON response with "Hello World"
@app.route('/')
def hello_world():
    return jsonify(message="Hello World")


# Endpoint for Application Healthcheck
@app.route('/health')
def healthcheck():
    # Setting application status and details to success for demo purpose.
    # In future extend code to fetch application status and details.
    details_success = "Application is running smoothly"
    details_failure = "Application encountered error"

    if application_online:
        return jsonify(status="success", details=details_success), 200
    else:
        return jsonify(status="failure", details=details_failure), 500


if __name__ == '__main__':
    app.run(debug=False)
