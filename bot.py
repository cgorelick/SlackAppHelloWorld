import os
import logging
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

load_dotenv()

token = os.environ.get("SLACK_BOT_TOKEN")

client = WebClient(token)
logger = logging.getLogger(__name__)

#set channel ID from a channel name
channel_name = "sandbox"
channel_id = None
try:
    # Call the conversations.list method using the WebClient
    for result in client.conversations_list():
        if channel_id is not None:
            break
        for channel in result["channels"]:
            if channel["name"] == channel_name:
                channel_id = channel["id"]
                print(f"Found conversation ID: {channel_id}")
                break
 
except SlackApiError as e:
    print(f"Error: {e}")

try:
    # Call the conversations.list method using the WebClient
    result = client.chat_postMessage(
        channel=channel_id,
        text="Hello world!"
    )
    # Print result, which includes information about the message (like TS)
    print(result)

except SlackApiError as e:
    print(f"Error: {e}")