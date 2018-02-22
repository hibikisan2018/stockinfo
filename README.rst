This program is to notify the N225 price and JPN/USD price through LINE notity.

1. Install
  You can install with pip below.

  pip install stockinfo

2. Usage
  stockinfo [-h] [-l LOG] token

  positional arguments:
    token              the token of LINE notify

  optional arguments:
    -h, --help         show this help message and exit
    -l LOG, --log LOG  define log level
  
3. Remarks
 - Depandencies: bs4, requests
 - If the program cannot find the objective CSS selector, it repeats to
   pearse the web site every 10 minutes by 5 times until the CSS selector
   is found.
