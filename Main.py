import Parser

from optparse import OptionParser

parser = OptionParser()

parser.add_option('--XmlDirectory', metavar='F', type='string', action='store', default='/tmp/mnt/Simulation', dest='XmlDirectory', help='specify input directory for Endless Space xml files')

(options, args) = parser.parse_args()

argv = []

#1 - load all xml data formats
WeaponData  = Parser.LoadWeapons(options.XmlDirectory)
DefenseData = Parser.ChargeDefenses(options.XmlDirectory)
HullData    = Parser.BuildHulls(options.XmlDirectory)
for Weapons  in range(0,len(WeaponData)):
  print WeaponData[Weapons].Name
for Defenses in range(0,len(DefenseData)):
  print DefenseData[Defenses].Name
for Hulls    in range(0,len(HullData)):
  print HullData[Hulls].Name

#2 - generate fleets (TBD)

#3 - simulate fleet fight (TBD)

#4 - fill histograms (TBD)

#5 - vary fleet parameters to fit target distribution (TBD)

#6 - redo from 3 until local minimum is hit (TBD)

#7 - write improved values to xml (TBD)
