class script(object):
    START_TXT = """Hey {} 
I'm Powerful Auto-Filter Bot You Can Use Me As A Auto-filter in Your Group,

Its Easy To Use Me : Just Add Me To Your Group As Admin, 
Thats All, i will Provide Movies There.

⚠ ️More Help Check Help Button Below

😎 Powered by @MaximXRobot
"""
    HELP_TXT = """

❏ Available Commands
┣ /start - Check I'm Alive..
┣ /status - Bot Status
┣ /info - User info 
┣ /id - User id
┣ /stats - Db status  
┗ /broadcast - Broadcast (Owner Only)
"""
    ABOUT_TXT = """𝑀𝑦 𝑁𝑎𝑚𝑒 {}
┏ 𝐶𝑟𝑒𝑎𝑡𝑜𝑟: <a href=https://t.me/MaximXRobot>I𝗓υɱi 和泉</a>
┣ 𝐿𝑖𝑏𝑟𝑎𝑟𝑦 : 𝑷𝒚𝒓𝒐𝒈𝒓𝒂𝒎
┣ 𝐿𝑎𝑛𝑔𝑢𝑎𝑔𝑒 : 𝑷𝒚𝒕𝒉𝒐𝒏
┣ 𝐷𝑎𝑡𝑎𝑏𝑎𝑠𝑒 : 𝑴𝒐𝒏𝒈𝒐 𝑫𝑩
┣ 𝐵𝑜𝑡 𝑆𝑒𝑟𝑣𝑒𝑟 : 𝑯𝒆𝒓𝒐𝒌𝒖
┗ 𝐵𝑢𝑖𝑙𝑑 𝑆𝑡𝑎𝑡𝑢𝑠 : v0.2"""
    SOURCE_TXT = """<b>NOTE: </b>
- Zero Two Is A Open Source Project. 
- Source Code - <a href=https://github.com/AL3X-Github/ZeroTwo>Zero Two</a>

<b>My Master: </b><a href=https://t.me/MaximXRobot>I𝗓υɱi 和泉</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter Is The Feature Were Users Can Set Automated Replies For A Particular Keyword And Zero Two Will Respond Whenever A Keyword Is Found The Message

<b>NOTE:</b>
1. Zero Two Should Have Admin Privillage.
2. Only Admins Can Add Filters In A Chat.
3. Alert Buttons Have A Limit Of 64 Characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Zero Two Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. ZeroTwo supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/MaximXRobot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
These Are The Extra Features Of Zero Two.

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This Module Only Works For My Admins.

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """┏ 𝑻𝒐𝒕𝒂𝒍 𝑭𝒊𝒍𝒆𝒔: <code>{}</code>
┣ 𝑇𝑜𝑡𝑎𝑙 𝑈𝑠𝑒𝑟𝑠: <code>{}</code>
┣ 𝑻𝒐𝒕𝒂𝒍 𝑪𝒉𝒂𝒕𝒔: <code>{}</code>
┣ 𝑈𝑠𝑒𝑑 𝑆𝑡𝑜𝑟𝑎𝑔𝑒: <code>{}</code> 
┗ 𝑭𝒓𝒆𝒆 𝑺𝒕𝒐𝒓𝒂𝒈𝒆: <code>{}</code> """
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
