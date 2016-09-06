'''
Created on Sep 5, 2016

@author: Jared
'''

from slackclient import SlackClient
import configparser

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("info.config")
    
    BOT_NAME = config.get('SectionOne', 'BOT_NAME')
    slack_client = SlackClient(config.get('SectionOne', 'SLACK_API_TOKEN'))
    
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        # retrieve all users so we can find our bot
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
    else:
        print("could not find bot user with the name " + BOT_NAME)