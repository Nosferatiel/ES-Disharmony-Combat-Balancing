import Parser
import Launch
import Damage
import Hit

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
Index_Hull    = 1
Index_Weapon  = 0
Index_Defense = 0
WeaponFill   = 0.7 #describes the percentage of ship space filled by weaponry
#generate ship struct with full loadout information
ShipInventoryA = Launch.SimpleShip(HullData[Index_Hull].Tonnage, HullData[Index_Hull].MaxHealth, Index_Weapon, WeaponData[Index_Weapon].Tonnage, DefenseData[Index_Defense].Type, DefenseData[Index_Defense].Tonnage, HullData[Index_Hull].Weakness, HullData[Index_Hull].Evade, WeaponFill)
ShipInventoryB = ShipInventoryA #clone, for now
#3 - simulate fleet fight (TBD)
for phase in range(1,4): #phase loop from 1 to 3
  for round in range (1,6): #round loop from 1 to 5
    InitialDeflection  = float(DefenseData[ShipInventoryA.DefenseIndex].Deflection)
    InitialDeflection *= float(ShipInventoryA.DefenseNumber) #initial deflection number for kinetics, not sure this is really per round?
    InitialEvasion = ShipInventoryA.Maneuver
    for salvoA in range (0, ShipInventoryA.WeaponNumber):
        if(WeaponData[ShipInventoryA.WeaponIndex].Type == 1): HitA = Hit.Kinetic(WeaponData[ShipInventoryA.WeaponIndex].Accuracy, InitialEvasion, WeaponData[ShipInventoryA.WeaponIndex].Shots, InitialDeflection)
	if(HitA == 666): continue 	#all shots absorbed
	elif(HitA  < 0):	  	#Deflection is slowly consumed
          InitialDeflection += HitA
	elif(HitA == 0):
	  if(InitialEvasion - 0.05 >= 0): InitialEvasion -= 0.05  #next evasion will be harder
	  else:                           InitialEvasion  = 0	  #no more fleeing
	elif(HitA  > 0): 	  	#actual damage is being done
	  DmgA = Damage.Compute(WeaponData[ShipInventoryA.WeaponIndex].MinDmg, WeaponData[ShipInventoryA.WeaponIndex].MaxDmg, WeaponData[ShipInventoryA.WeaponIndex].CritMult, WeaponData[ShipInventoryA.WeaponIndex].CritMod, DefenseData[ShipInventoryB.DefenseIndex].Defense*ShipInventoryB.DefenseNumber, ShipInventoryB.HullWeakness)
	  DmgA *= HitA
#4 - fill histograms (TBD)

#5 - vary fleet parameters to fit target distribution (TBD)

#6 - redo from 3 until local minimum is hit (TBD)

#7 - write improved values to xml (TBD)
