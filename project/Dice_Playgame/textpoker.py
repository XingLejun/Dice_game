# textpoker.py --video dice poker using a text-based interface.

from dice import Dice
from pokerapp import PokerApp
from textinterface import TextInterface

inter = TextInterface()
app = PokerApp(inter)
app.run()