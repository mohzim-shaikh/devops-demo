from flask import Flask, jsonify

app = Flask(__name__)
application_status = "success"


# Endpoint returns a JSON response with "Hello World"
@app.route('/')
def hello_world():
    return jsonify(message="Hello World")


# Endpoint for Application Healthcheck
@app.route('/health')
def healthcheck():
    # Setting application status and details to success for demo purpose.
    # In future extend code to fetch application status and details.
    # application_status = "success"
    details_success = "Application is running smoothly"
    details_failure = "Application encountered error processing this request"

    if application_status == "success":
        return jsonify(status="success", details=details_success), 200
    else:
        return jsonify(status="failure", details=details_failure), 500


if __name__ == '__main__':
    app.run(debug=False)
