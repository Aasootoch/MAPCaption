import pyrogram, os, asyncio

try: app_id = int(os.environ.get("app_id", '22420478'))
except Exception as app_id: print(f"App ID Invalid {app_id}")
try: api_hash = os.environ.get("api_hash", '5938b801d270c81afd3ad8581aba7960')
except Exception as api_id: print(f"Api Hash Invalid {api_hash}")
try: bot_token = os.environ.get("bot_token", '6435704169:AAGE7p6Y77X8wN8N74QSyrPooSQSiuwXgb8')
except Exception as bot_token: print(f"Bot Token Invalid {bot_token}")
try: custom_caption = os.environ.get("custom_caption", "𝖩𝗈𝗂𝗇  ➥ 「 [@𝖬𝖠𝖯𝖮𝗋𝗂𝗀𝗂𝗇𝖺𝗅𝗌](https://t.me/MAPOriginals) 」")
except Exception as custom_caption: print(f"Custom Caption Invalid {custom_caption}")

AutoCaptionBotV2 = pyrogram.Client(
   name="AutoCaptionBotV2", api_id=app_id, api_hash=api_hash, bot_token=bot_token)

start_message = """
<b>Hello {}</b>
<b>I am an Auto Channel Caption Editor Bot.</b>
"""

@AutoCaptionBotV2.on_message(pyrogram.filters.private & pyrogram.filters.command(["start"]))
def start_command(bot, update):
  update.reply(start_message.format(update.from_user.mention))

@AutoCaptionBotV2.on_message(pyrogram.filters.channel)
def edit_caption(bot, update: pyrogram.types.Message):
  if custom_caption and update.media and update.caption != None and custom_caption not in str(update.caption) : 
      try:
          update.edit("<b>"+str(update.caption) + "\n\n" + custom_caption+"</b>")
      except pyrogram.errors.MessageNotModified: pass    
  else:
      return
    
AutoCaptionBotV2.run()
