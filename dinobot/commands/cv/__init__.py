def help(*args, **kwargs):
    """
    Help command

    This command returns information about the bot and commands it can run
    """
    return dict(text="Not implemented",
                response_type="ephemeral")


#### Initialization for cv command ####
def receive(channel_id, channel_name, team_id, user_id, text, trigger_id):
    """
    Receive a slash command to the `cv` base command

    cv <command> <params>
    """
    command = text.split()[0]
    params = text.split()[1:]

    if command == "help":
        return help()
