#START AND SCRIPT

class Translation(object):
    
    START_TEXT = """Hello {}
I am [Kareena Kapoor](t.me/HRZKareenaRobot), A Powerful Telegram Bot created for [HRZ Group](t.me/TheHRZTG).
Only authorized people can be use me. So don't waste your time dear 😄

@TheHRZTG"""

    
    HELP_TEXT = """
<b><i><u>How To Use Me!?</u></i></b>

<i>
-> Add Me To Any Group And Make Me Admin
-> Add Me To Your Desired Channel
</i>

<b>Bot Commands (Works Only In Groups) :</b>

    -> <code>/add chat_id</code>
                OR                  - To Connect A Group With A Channel (Bot Should Be Admin With Full Previlages In Both Group And Channel)
     <code>/add @Username</code>
     
    -> <code>/del chat_id</code>
                OR                  - To disconnect A Group With A Channel
     <code>/del @Username</code>
     
    -> <code>/delall</code>  - This Command Will Disconnect All Connected Channel With The Group And Deletes All Its File From DB
    
    -> <code>/settings</code> -  This Command Will Display You A Settings Pannel Instance Which Can Be Used To Tweek Bot's Settings Accordingly

            -> <code>Channel</code> - Button Will Show You All The Connected Chats With The Group And Will Show Buttons Correspnding To There Order For Furthur Controls
            
            -> <code>Filter Types</code> - Button Will Show You The 3 Filter Option Available In Bot... Pressing Each Buttons Will Either Enable or Disable Them And This Will Take Into Action As Soon As You Use Them Without The Need Of A Restart

            -> <code>Configure</code> - Button Will Helps You To Change No. of Pages/ Buttons Per Page/ Total Result Without Acutally Editing The Repo... Also It Provide Option To Enable/Disable For Showing Invite Link In Each Results
            
            -> <code>Status</code> - Button Will Shows The Stats Of Your Channel
            
@TheHRZTG
"""
    
    ABOUT_TEXT = """➥ Name   : [Kareena Kapoor](t.me/HRZKareenaRobot)
➥ Developer : [HRZ 🇮🇳](t.me/HRZRobot)   
➥ Updates   : [HRZ TG](t.me/TheHRZTG)
➥ Language  : [Python3](www.python.org)
➥ Library   : [Pyrogram](www.pyrogram.org)
➥ Database  : [Mango DB](www.mangodb.com)
➥ Server    : [Render](www.render.com)"""
    


    STATUS_TEXT = """★ Total Files: {}
★ Using Storage: {} MB
★ Free Storage: {} MB"""
