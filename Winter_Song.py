#		python code
#		script_name:Winter Song
#
#		author:Paramvir Singh
#		description:
#

from earsketch import *
from random import *

init()


beatPattern = "00-00--00-00--0-"
makeBeat(YG_TRAP_BASS_4,1,2.0,beatPattern)

def trap():
  setTempo(randint(100,150))
  instrumentList = ("RD_TRAP_DRUM_PART_26", "RD_TRAP_BASSDROPS_2", "RD_TRAP_SFX_GATEDRISE_1")
  fitMedia(CIARA_SET_THEME_MAIN_2,3,1,20)
  fitMedia(RD_TRAP_DRUM_PART_1,4,4,20)
  fitMedia(RD_TRAP_DRUM_PART_21,5,1,20)
  for even in range(5,18):
    if(even % 2 == 0):
      print(even)
      fitMedia(instrumentList[0],6,even,even*2.2)
      fitMedia(instrumentList[1],7,even,even*2.4)
    else:
      fitMedia(instrumentList[2],8,even,even*2)


def pop():
  setTempo(120)
  instrumentList = ("RD_POP_ARPBASS_1", "RD_POP_SOLODRUMPART_1", "RD_POP_SOLODRUMPART_9")
  fitMedia(CIARA_MELANIN_THEME_TUBA_1,3,1,20)
  fitMedia(RD_POP_SYNTHBASS_2,4,4,20)
  fitMedia(RD_POP_SYNTHBASS_6,5,1,20)
  for even in range(5,18):
    if(even % 2 == 0):
      print(even)
      fitMedia(instrumentList[0],6,even,even*2.2)
      fitMedia(instrumentList[1],7,even,even*2.4)
    else:
      fitMedia(instrumentList[2],8,even,even*2)


def rock():
  setTempo(randint(100,150))
  instrumentList = ("RD_ROCK_POPELECTRICBASS_2", "RD_ROCK_POPELECTRICBASS_11", "RD_ROCK_POPELECTRICBASS_16")
  fitMedia(CIARA_MELANIN_DRUMBEAT_1,3,1,20)
  fitMedia(RD_ROCK_POPELECTRICLEAD_1,4,4,20)
  fitMedia(RD_ROCK_POPLEADSTRUM_GUITAR_6,5,1,20)
  for even in range(5,18):
    if(even % 2 == 0):
      print(even)
      fitMedia(instrumentList[0],6,even,even*2.2)
      fitMedia(instrumentList[1],7,even,even*2.4)
    else:
      fitMedia(instrumentList[2],8,even,even*2)

selection = int(input("What genre would you like? 1)Rock,  2)Pop,  3)Trap"))
if(selection == 1):
  rock()
if(selection == 2):
  pop()
if(selection == 3):
  trap()
finish()
