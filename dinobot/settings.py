# This token is used to verify slack
import commands.cv as cv
import actions.cv as cv_action

SLACK_TOKEN = ""

ADMINS = [
    # (team_id, user_id)
]

WEBHOOK_URL_MAPPING = {
    # "name" -> "url"
}

ENABLED_COMMANDS = {
    "cv": cv
}

ENABLED_ACTIONS = {
    "cv": cv_action
}
