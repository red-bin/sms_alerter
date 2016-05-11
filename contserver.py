#!/usr/bin/python2.7


from twilio.rest import TwilioRestClient
import sqlite3
 
# Find these values at https://twilio.com/user/account
 
def send_message(from_="MG0ec44303bffbb9c38e90b736e14912de", to = "+18478992608", body="Test"):
    from_ = from_
    to = to
    body=body
    message = client.messages.create(to=to, from_=from_, body=body)

    return message

import simplejson as json
from StringIO import StringIO

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        data = str(request.form['data'])

        json_data = json.loads(data)[0]

        device_id = str(json_data['DeviceID'])
        contact_id = str(json_data['ContactID'])

        message = "%s %s %s" % (device_id, contact_id, json_data['Message'])

        conn = sqlite3.connect('conntech.db')
        c = conn.cursor()
        c.execute("INSERT INTO statuses VALUES ('%s','%s','%s','%s')" % (device_id, contact_id, message, data))
        conn.commit()
        c.close()

        ret = send_message(body=message)

        return True

api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    conn = sqlite3.connect('conntech.db')
    c = conn.cursor()

    try:
        c.execute("SELECT * FROM statuses limit 1")
    except:
        c.execute("CREATE TABLE statuses (device_id, contact_id, message, data)")

    c.close()

    
    app.run(debug=True, host='0.0.0.0')
