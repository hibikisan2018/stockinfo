# N225&FX notification program

This program is to notify the N225 price and JPN/USD price through LINE notity.

## 1. Usage
  python3 sendLineMessage2.py [-h] [-l LOG] tokenfile

  - positional arguments:  tokenfile
   'tokenfile' is put in the same directory as "sendLineMessage2.py" and 
   the token code for LINE notify is described in this file. It's better to 
   setting the permission code in this file for security.
   
   example) $ cmode 700 .linetoken

  - optional arguments:
    -h, --help         show this help message and exit
    -l LOG, --log LOG  if you check the log, please set this argument
  
## 2. Remarks
 - Depandencies: bs4, requests
 - If the program cannot find the objective CSS selector, it repeats to
   pearse the web site every 10 minutes by 5 times until the CSS selector
   is found.
