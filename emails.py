# import resend
# import os
# from flask import Flask, jsonify
# from config import app

# class Email(Emails):
#     def get(self):
#         emails = [emails.to_dict() for emails in Emails.query.all()]
#         return emails,200

# resend.api_key = 're_UbpYmRBa_BdXWECDfmiTkVewCFnPu9X6L'


# @app.route("/emails")
# def index():
#     params = {
#         "from": "GreenTracker <onboarding@resend.dev>",
#         "to": ["delivered@resend.dev"],
#         "subject": "Hi there",
#         "html": "<strong>Welcome to GreenTracker. How may we support you?</strong>",
#     }

#     r = resend.Emails.send(params)
#     return jsonify(r)


