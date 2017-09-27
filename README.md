# MemeBot 3000
## Description
This is a small meme bot for discord, written in python 3.6 using discord.py
## Dependencies 
* Discord.py
### Installing dependencies
You can run deps.sh on **Linux**
```bash
$ sudo sh deps.sh
```
Or deps.bat on **Windows**
```
Double click in explorer *sigh*
```

## Running the MemeBot with PM2
If you require 100% uptime, you can use the **PM2** with the pyhton interpreter mananger to keep it afk online, all the time.
```bash
$ sudo apt get update
$ sudo apt install pm2
$ pm2 start Bot.py --interpreter python3
$ pm2 status 
```
You should now have Bot running on your pm2 management page

