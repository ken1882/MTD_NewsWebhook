from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

VerboseLevel = 3

NEWS_TAG = {
    1: 'MAINTENANCE',
    2: 'UPDATE',
    3: 'GACHA',
    4: 'EVENT',
    5: 'CAMPAIGN',
    6: 'BUG',
    7: 'MISC',
}

NEWS_ICON = {
    1: 'https://cdn-icons-png.flaticon.com/512/777/777081.png',
    2: 'https://cdn.icon-icons.com/icons2/1508/PNG/512/updatemanager_104426.png',
    3: 'https://cdn-icons-png.flaticon.com/512/4230/4230567.png',
    4: 'https://cdn-icons-png.flaticon.com/512/4285/4285436.png',
    5: 'https://cdn-icons-png.flaticon.com/512/3867/3867424.png',
    6: 'https://www.iconsdb.com/icons/preview/red/error-7-xxl.png',
    7: 'https://cdn-icons-png.flaticon.com/512/1827/1827301.png'
}

NEWS_COLOR = {
    1: 0xfc3aef,
    2: 0x5299f7,
    3: 0xfad73c,
    4: 0x50faf4,
    5: 0xff5cb0,
    6: 0xdb043e,
    7: 0xcccccc,
}

VOCAB_JP = {
    'NEWS_TAG': {
        1: 'メンテナンス',
        2: 'アップデート',
        3: 'ガチャ',
        4: 'イベント',
        5: 'キャンペーン',
        6: '不具合',
        7: 'その他',
    }
}

def format_curtime():
  return datetime.strftime(datetime.now(), '%H:%M:%S')

def log_error(*args, **kwargs):
  if VerboseLevel >= 1:
    print(f"[{format_curtime()}] [ERROR]:", *args, **kwargs)

def log_warning(*args, **kwargs):
  if VerboseLevel >= 2:
    print(f"[{format_curtime()}] [WARNING]:", *args, **kwargs)

def log_info(*args, **kwargs):
  if VerboseLevel >= 3:
    print(f"[{format_curtime()}] [INFO]:", *args, **kwargs)

def log_debug(*args, **kwargs):
  if VerboseLevel >= 4:
    print(f"[{format_curtime()}] [DEBUG]:", *args, **kwargs)