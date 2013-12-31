import Parser
import Launch

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
#configure ship type and loadout here (later on subject to variation)
Index_Hull    = 0
Index_Weapon  = 0
Index_Defense = 0
WeaponFill   = 0.3 #describes the percentage of ship space filled by weaponry
#generate ship struct with full loadout information
ShipInventoryA = Launch.SimpleShip(HullData[Index_Hull].Tonnage, HullData[Index_Hull].MaxHealth, WeaponData[Index_Weapon].Type, WeaponData[Index_Weapon].Tonnage, DefenseData[Index_Defense].Type, DefenseData[Index_Defense].Tonnage, HullData[Index_Hull].Weakness, HullData[Index_Hull].Evade, WeaponFill)
#3 - simulate fleet fight (TBD)

#4 - fill histograms (TBD)

#5 - vary fleet parameters to fit target distribution (TBD)

#6 - redo from 3 until local minimum is hit (TBD)

#7 - write improved values to xml (TBD)
