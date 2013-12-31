import math
import Ship

#simple 1 weapon module type, 1 defense module type ship
def SimpleShip(Space, Health, WeaponNr, WeaponWeight, DefenseNr, DefenseWeight, Weakness, Maneuverability, Ratio):
  Inventory = Ship.struct()
  Inventory.Health	  = int(Health)
  Inventory.WeaponIndex   = int(WeaponNr)
  Inventory.WeaponNumber  = int(math.floor(Ratio*float(Space)/float(WeaponWeight)))
  Inventory.DefenseIndex  = int(DefenseNr)
  Inventory.DefenseNumber = int(math.floor((float(Space)-Inventory.WeaponNumber*float(WeaponWeight))/float(DefenseWeight)))
  Inventory.HullWeakness  = int(Weakness)
  Inventory.Maneuver      = float(Maneuverability)
  return Inventory
   
