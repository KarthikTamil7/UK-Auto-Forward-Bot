from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "5264bf4663e9159565603522f58d3c18")
      API_ID = int(getenv("API_ID", 11973721))
      AS_COPY = True if getenv("AS_COPY", True) == "True" else False
      PICS = getenv('PICS', 'https://telegra.ph/file/0cc81f5c4df05837d8b05.jpg')
      BOT_TOKEN = getenv("BOT_TOKEN", "5949999646:AAGNAzsUTMutsqtnSk2R4MkGgCQ0uMtqbIU")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001861300920:-1001811940117 -1001786688631 -1001436081117 -1001780758150 -1001721348234 -1001780697340 -1001698854544 -1001593574364 -1001519485548").replace("\n", " ").split(' '))
