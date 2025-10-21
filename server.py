from flask import Flask, request, jsonify
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

# Configure these for your SMTP provider
SMTP_SERVER = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.environ.get('SMTP_PORT', 587))
SMTP_USER = os.environ.get('SMTP_USER', 'your_email@gmail.com')
SMTP_PASS = os.environ.get('SMTP_PASS', 'your_app_password')
TO_EMAIL = 'wesley.earl@earlybirdstrategiesllc.com'

@app.route('/quote', methods=['POST'])
def quote():
    data = request.form
    name = data.get('name', '')
    phone = data.get('phone', '')
    email = data.get('email', '')
    company = data.get('company', '')
    services = ', '.join(request.form.getlist('services[]'))
    details = data.get('project-details', '')

    msg = EmailMessage()
    msg['Subject'] = 'New Quote Request from Earlybird Strategies Website'
    msg['From'] = SMTP_USER
    msg['To'] = TO_EMAIL
    msg.set_content(f"""
Name: {name}
Phone: {phone}
Email: {email}
Company: {company}
Services Needed: {services}
Project Details: {details}
""")

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.send_message(msg)
        return jsonify({'success': True, 'message': 'Quote request sent successfully.'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
