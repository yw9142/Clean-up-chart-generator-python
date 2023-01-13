from datetime import datetime
from itertools import accumulate
from bisect import bisect
from random import randrange
from unicodedata import name as unicode_name
import pyperclip

# Set the unicode version.
# Your system may not support Unicode 7.0 charecters just yet! So hipster.
UNICODE_VERSION = 6

# Sauce: http://www.unicode.org/charts/PDF/U1F300.pdf
EMOJI_RANGES_UNICODE = {
  6: [('\U0001F300', '\U0001F320'), ('\U0001F330', '\U0001F335'),
      ('\U0001F337', '\U0001F37C'), ('\U0001F380', '\U0001F393'),
      ('\U0001F3A0', '\U0001F3C4'), ('\U0001F3C6', '\U0001F3CA'),
      ('\U0001F3E0', '\U0001F3F0'), ('\U0001F400', '\U0001F43E'),
      ('\U0001F440', ), ('\U0001F442', '\U0001F4F7'),
      ('\U0001F4F9', '\U0001F4FC'), ('\U0001F500', '\U0001F53C'),
      ('\U0001F540', '\U0001F543'), ('\U0001F550', '\U0001F567'),
      ('\U0001F5FB', '\U0001F5FF')],
  7: [('\U0001F300', '\U0001F32C'), ('\U0001F330', '\U0001F37D'),
      ('\U0001F380', '\U0001F3CE'), ('\U0001F3D4', '\U0001F3F7'),
      ('\U0001F400', '\U0001F4FE'), ('\U0001F500', '\U0001F54A'),
      ('\U0001F550', '\U0001F579'), ('\U0001F57B', '\U0001F5A3'),
      ('\U0001F5A5', '\U0001F5FF')],
  8: [('\U0001F300', '\U0001F579'), ('\U0001F57B', '\U0001F5A3'),
      ('\U0001F5A5', '\U0001F5FF')]
}

NO_NAME_ERROR = '(No name found for this codepoint)'


def random_emoji(unicode_version=6):
  if unicode_version in EMOJI_RANGES_UNICODE:
    emoji_ranges = EMOJI_RANGES_UNICODE[unicode_version]
  else:
    emoji_ranges = EMOJI_RANGES_UNICODE[-1]

  # Weighted distribution
  count = [ord(r[-1]) - ord(r[0]) + 1 for r in emoji_ranges]
  weight_distr = list(accumulate(count))

  # Get one point in the multiple ranges
  point = randrange(weight_distr[-1])

  # Select the correct range
  emoji_range_idx = bisect(weight_distr, point)
  emoji_range = emoji_ranges[emoji_range_idx]

  # Calculate the index in the selected range
  point_in_range = point
  if emoji_range_idx != 0:
    point_in_range = point - weight_distr[emoji_range_idx - 1]

  # Emoji 😄
  emoji = chr(ord(emoji_range[0]) + point_in_range)
  emoji_name = unicode_name(emoji, NO_NAME_ERROR).capitalize()
  emoji_codepoint = "U+{}".format(hex(ord(emoji))[2:].upper())

  return (emoji)


# ---------------------------------------------------------------------------------------
# file = open("TextFile.txt", "w");

user = {
  "강동석": True,
  "정재우": True,
  "이은학": True,
  "이승민": True,
  "김동민": True,
  "박용훈": False,
  "김태경": True,
  "김현호": False,
  "민일": True,
  "백재범": True,
  "우현하": True,
  "전진욱": True,
  
  "김정운": True,
  "김정훈": True,
  "이민혁": False,
  "최영민": True,
  "최재용": True,
  "허은빈": True,
  
  "문창민": True,
  "이주석": True,
  "지태우": True,
  "최진교": True,
  
  "손도현": False,
  "안규보": False,
  "이승기": False,
  "이현재": False,
  "장수원": False,
  "정지환": False,
  "조정재": False,
  "한재진": False,
}

area_before = [
  "사관실", "독사", "마대", "마대", "마대", "사이드", "휴체", "휴체", "휴체", "신세", "신세", "화장실",
  "화장실", "화장실", "화장실"
]

area_after = [
  "사관실", "독사", "마대", "마대", "마대", "사이드", "휴체", "휴체", "휴체", "신세", "신세", "화장실",
  "화장실", "화장실", "화장실"
]

#1 False 인원 제거
lst = [i for i, j in user.items() if j == True]

#2 청소표 인원 맞추기
if datetime.today().day < 16:
  while len(lst) != len(area_before):
    lst.pop(0)
else:
  while len(lst) != len(area_after):
    lst.pop(0)

with open("TextFile.txt", "w") as file:
  file.write(
    f"{random_emoji(UNICODE_VERSION)} {datetime.today().year}년 {datetime.today().month}월 {datetime.today().day}일 {random_emoji(UNICODE_VERSION)}\n"
  )
  if datetime.today().day < 16:
    for i in range(len(area_before)):
      file.write(f"{lst[i]} - {area_before[i]}\n")
  else:
    for i in range(len(area_after)):
      file.write(f"{lst[i]} - {area_after[i]}\n")

file.close()
