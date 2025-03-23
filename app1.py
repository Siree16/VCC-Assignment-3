from flask import Flask, request, jsonify, render_template
import math
import psutil
import requests
import logging
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
migration_active = False  # Global variable to track migration state
# Configure logging
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Global variable to track migration state
migration_active = False

# Email configuration
sender_email = "m23cse023@iitj.ac.in"
receiver_email = "sireejaa2014@gmail.com"
email_password ="pswd"

# Function to send email notifications
def send_email(subject, body):
    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, email_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        logging.info("Email sent successfully!")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

# Function to log events
def log_event(message):
    logging.info(message)
    print(message)  # Print to console for real-time monitoring

# Factorial Calculation
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Prime Number Check
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Fibonacci Sequence
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) <= n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Sum of Digits
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Palindrome Check
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# Migrate Tasks to GCP
def migrate_to_gcp(number):
    gcp_url = "http://10.128.0.18:5001/calculate"  # Replace with your GCP VM's external IP
    response = requests.post(gcp_url, json={"number": number})
    return response.json()

# Default Route
@app.route('/')
def home():
    return render_template('index.html')

# Calculate Route
@app.route('/calculate', methods=['POST'])
def calculate():
    global migration_active  # Declare migration_active as a global variable
    try:
        data = request.json
        if not data or 'number' not in data:
            return jsonify({"error": "Invalid input: 'number' is required"}), 400

        number = int(data['number'])

        # Check CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)
        log_event(f"Current CPU Usage: {cpu_usage}%")

        # Notify if CPU usage exceeds 75%
        if cpu_usage > 75:
            if not migration_active:
                log_event("CPU usage exceeded 75%. Starting migration to GCP...")
                send_email("Migration Started", f"CPU usage is {cpu_usage}%. Migrating tasks to GCP.")
                migration_active = True

            # Migrate tasks to GCP
            gcp_result = migrate_to_gcp(number)
            result = {
                "factorial": gcp_result["factorial"],
                "is_prime": is_prime(number),
                "fibonacci": gcp_result["fibonacci"],
                "sum_of_digits": sum_of_digits(number),
                "is_palindrome": is_palindrome(number)
            }
        else:
            if migration_active:
                log_event("CPU usage normalized. Stopping migration to GCP.")
                send_email("Migration Stopped", f"CPU usage is {cpu_usage}%. Tasks are now running locally.")
                migration_active = False

            log_event("Running tasks locally.")
            result = {
                "factorial": factorial(number),
                "is_prime": is_prime(number),
                "fibonacci": fibonacci(number),
                "sum_of_digits": sum_of_digits(number),
                "is_palindrome": is_palindrome(number)
            }

        return jsonify(result)

    except Exception as e:
        log_event(f"Error in /calculate: {str(e)}")
        return jsonify({"error": str(e)}), 500
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
