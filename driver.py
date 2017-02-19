import sys
import webAccess
import stlmanipulator
import time
#import stlrender

text = input('Input text to render:')
webAccess.generate_stl(text)
time.sleep(5)
stlmanipulator.rotate('openjscad.stl')
#stlrender('rotated_openjscad.stl')
