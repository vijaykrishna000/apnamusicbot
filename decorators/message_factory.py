from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from utils import logInfo, logException, config, mongoDBClient


def getMessage(message, action, errorMsg=""):
    try:
        extra_options = {
            "-video": "Stream the video file in video chat.",
            "-audio": "Stream just the audio.",
            "-repeat": "ye supported hai ab iska mtlb mat puchna.",
            "-res720": "Stream the audio/video in the provided quality/resolution.",
            "-lipsync": "Use this if audio is not in sync with video",
        }
        if action == "start-private-message":
            send_message = f"**Hi 🎵 {message.chat.first_name if hasattr(message.chat, 'first_name') else 'User'}**"
            send_message = (
                send_message
                + f"\n\n**[This Music Player]({config.get('BOT_URL')})** is a [BJ Thing]({config.get('PARENT_URL')})."
            )
            send_message = (
                send_message
                + f"\n__It is designed to fuck your brain.__"
            )
            send_message = (
                send_message
                + f"\n\n**So why wait 🌀 add the bot to a group and get started 🎧"
            )
            return send_message, getReplyKeyBoard(message, action)
        elif action == "start-group-message":
            send_message = f"**Thank you for adding [Music Player]({config.get('BOT_URL')})🎵**"
            send_message = (
                send_message
                + f"\n\n**[Music Player]({config.get('BOT_URL')})** is a [BJ totka]({config.get('PARENT_URL')})."
            )
            send_message = (
                send_message
                + f"\n__It is designed to fuck your brain.__"
            )
            if not mongoDBClient.client:
                send_message = (
                    send_message
                    + f"\n\n**Few things before we get started**\n`• make sure the bot is an admin in this group`\n`• make sure you provided USERBOT_SESSION value in env`"
                )
            else:
                send_message = (
                    send_message
                    + f"\n\n**Few things before we get started**\n`• make sure the bot is an admin in this group`\n`• make sure group admin has authorized the bot`"
                )
            send_message = send_message + f"\n\nSend /help for available options."
            return send_message, getReplyKeyBoard(message, action)
        elif action == "no-auth-docs":
            send_message = f"__Oops! I was unable to find and initiated authorization. Note that they are valid only for 10 mins.__"
            send_message = (
                send_message
                + f"\n\nAdd the bot to your group, send /start in group and then tap on authorize button in that group."
            )
            return send_message, getReplyKeyBoard(message, "no-auth-docs")

        elif action == "help-private-message":
            send_message = f"**VoiceChat Music Player**\n**Source Code :** [Repository]({config.get('GITHUB_REPO')})"
            send_message = (
                send_message
                + f"\n\n**[Voice Chat Music Player]({config.get('BOT_URL')})** is a [SkTechHub Product]({config.get('PARENT_URL')})."
            )
            send_message = send_message + f"\n\n__**Available Commands**__"
            send_message = (
                send_message
                + f"\n• **/start : ** __Shows welcome message and add to group button.__"
            )
            if mongoDBClient.client:
                send_message = (
                    send_message
                    + f"\n• **/auth : ** __Authorizes the bot, mandatory for playing songs/video.__"
                )
            send_message = (
                send_message + f"\n• **/help : ** __Shows the available commands.__"
            )
            if mongoDBClient.client:
                send_message = (
                    send_message
                    + f"\n\n__• You first add the bot to a group/channel.__\n"
                    + f"__• Provide admin rights to the bot in the group/channel.__\n"
                    + f"__• Send /start in that group/channel and click on **Authorize Button**.__\n"
                    + f"__• Bot will send you the message with next steps, follow them and that's all.__\n"
                    + f"__• Send `help` in the group/channel to view the playback commands.__"
                )
            else:
                send_message = (
                    send_message
                    + f"\n\n__• You first add the bot to a group/channel.__\n"
                    + f"__• Provide admin rights to the bot in the group/channel.__\n"
                    + f"__• Send `help` in the group/channel to view the playback commands.__"
                )
            send_message = (
                send_message + f"\n\n**__For any issues contact @vijaykrishna0__**"
            )
            return send_message, getReplyKeyBoard(message, action)

        elif action == "help-group-message":
            send_message = f"**Music Player**\n"
            send_message = (
                send_message
                + f"\n\n**[Music Player]({config.get('BOT_URL')})** is a BJ kand."
            )
            send_message = send_message + f"\n\n__**Available Commands**__"
            send_message = (
                send_message
                + f"\n• **/start : ** __Shows authorization steps (mandatory).__"
            )
            send_message = (
                send_message
                + f"\n• **/play media name|url  : ** __Plays the given media.__"
            )
            for k, v in extra_options.items():
                send_message = send_message + f"\n\t\t\t\t **{k}** : __{v}__"
            send_message = (
                send_message
                + f"\n`/play coldplay -video -res480` → __Plays coldplay video in 480p.__"
            )
            send_message = send_message + f"\n• **/stop : ** __Stop the playback.__"
            send_message = send_message + f"\n• **/pause : ** __Pause the playback.__"
            send_message = send_message + f"\n• **/resume : ** __Resume the playback.__"
            send_message = (
                send_message
                + f"\n• **/skip : ** __Skip and play the next media waiting in queue.__"
            )
            send_message = (
                send_message + f"\n• **/help : ** __Shows the available commands.__"
            )
            send_message = (
                send_message + f"\n\n**__For any issues contact @vijaykrishna0__**"
            )
            return send_message, getReplyKeyBoard(message, action)

        elif action == "chat-not-allowed":
            send_message = f"**😖 Sorry but this chat is not yet allowed to access the service. You can always check the demo in [Support Group]({config.get('SUPPORT_GROUP')}).**"
            send_message = (
                send_message
                + f"\n\n**Why ❓**\n- __Due to high usage we have restricted the usage of the bot in just our [Support Group]({config.get('SUPPORT_GROUP')}) __"
            )
            send_message = (
                send_message
                + f"\n- __Join the [Support Group]({config.get('SUPPORT_GROUP')}) to access the bot or deploy your own bot __ **Source Code :** [Github]({config.get('GITHUB_REPO')})"
            )

            return send_message, getReplyKeyBoard(message, action)

        elif action == "start-voice-chat":
            send_message = (
                f"**Please start a voice chat and then send the command again**"
            )
            send_message = (
                send_message
                + f"\n1. __To start a group chat, you can head over to your group’s description page.__"
            )
            send_message = (
                send_message
                + f"\n2. __Then tap the three-dot button next to Mute and Search start a Voice Chat.__"
            )
            return send_message, getReplyKeyBoard(message, action)

    except Exception as ex:
        logException(f"**__Error in getMessages: {ex}__**", True)


def getReplyKeyBoard(message, action):
    try:
        if action in ["start-private-message", "help-private-message"]:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "➕ Add the bot to Group ➕",
                            url=f"{config.get('BOT_URL')}?startgroup=bot",
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "👥 Support Group", url=f"{config.get('SUPPORT_GROUP')}"
                        ),
                        InlineKeyboardButton(
                            "📔 Source Code", url=f"{config.get('GITHUB_REPO')}"
                        ),
                    ],
                ]
            )
            return keyboard
        elif action == "start-group-message":
            rows = [
                [
                    InlineKeyboardButton(
                        "👥 Support Group", url=f"{config.get('SUPPORT_GROUP')}"
                    ),
                    InlineKeyboardButton(
                        "📔 Source Code", url=f"{config.get('GITHUB_REPO')}"
                    ),
                ]
            ]
            if mongoDBClient.client:
                rows.insert(
                    0,
                    [
                        InlineKeyboardButton(
                            "🤖 Authorize the bot 🤖",
                            callback_data=f"authorize-user-bot",
                        ),
                    ],
                )
            keyboard = InlineKeyboardMarkup(rows)
            return keyboard
        elif action == "chat-not-allowed":
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "🏁 Use In Demo Group", url=f"{config.get('SUPPORT_GROUP')}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "📔 Source Code", url=f"{config.get('GITHUB_REPO')}"
                        ),
                    ],
                ]
            )
            return keyboard
        return None
    except Exception as ex:
        logException(f"**__Error in getReplyKeyBoard: {ex}__**", True)
