from flask import (
    Flask,
    jsonify,
    request,
    json
)

import settings

app = Flask(__name__)

def check_token(token):
    return token == settings.SLACK_TOKEN or settings.SLACK_TOKEN == ""


@app.route('/slash/<string:command>', methods=["POST"])
def slash_command(command):
    if command not in settings.ENABLED_COMMANDS:
        return jsonify(dict(text="{0} is not an enabled slash-command".format(command),
                            response_type="ephemeral"))

    token = request.form.get('token')

    if not check_token(token):
        return "Invalid source"

    channel_id = request.form.get('channel_id')
    channel_name = request.form.get('channel_name')
    team_id = request.form.get('team_id')
    user_id = request.form.get('user_id')
    text = request.form.get('text')
    trigger_id = request.form.get('trigger_id')
    response = settings.ENABLED_COMMANDS[command].receive(
        channel_id, channel_name, team_id, user_id, text, trigger_id
    )
    return jsonify(response)

@app.route('/action', methods=["POST"])
def action_request():
    payload = json.loads(request.form.get('payload'))
    namespace = payload['callback_id'].split('.')[0]
    token = payload['token']
    if not check_token(token):
        return "Invalid source"
    del(payload['token'])
    if namespace not in settings.ENABLED_ACTIONS:
        message = "{0} is not an enabled action.".format(namespace)
        return jsonify(dict(text=message,
                            response_type="ephemeral"))
    response = settings.ENABLED_ACTIONS[namespace].receive(payload)
    return jsonify(response)


if __name__ == '__main__':
    app.run()
