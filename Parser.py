import os
import Weapon
import Defense
from xml.dom import minidom

from optparse import OptionParser

parser = OptionParser()

parser.add_option('--XmlDirectory', metavar='F', type='string', action='store', default='/tmp/mnt/Simulation', dest='XmlDirectory', help='specify input directory for Endless Space xml files')

(options, args) = parser.parse_args()

argv = []

#safeguard bools to kill the program before it does segmentation faults due to missing files
WeaponsLoaded  = False
DefensesLoaded = False

#top level structures for loading all necessary information
WeaponData = list()
DefenseData = list()

#Parsing module for getting descriptors of weapons, defenses and a basic hull out of the Endless Space xmls
for files in os.listdir(options.XmlDirectory): #loading all xml files
  if(files[len(files)-3:len(files)] != 'xml'): continue #ascertain to only load xml files
  #part 1: weapons
  if(files == 'WeaponModule.xml'):
	WeaponsLoaded = True
	xml = minidom.parse(options.XmlDirectory+ '/' + files) #read in WeaponModule.xml
	WeaponsList = xml.getElementsByTagName('WeaponModule') #read in WeaponModules
	counter = 0
	for node in WeaponsList:
	  name = node.attributes['Name'].value
	  if(name.find('Fake')   >= 0): continue #skip all the fakes
	  if(name.find('Hissho') >= 0): continue #skip all Hissho racial weapons
	  if(name.find('Swarm')  >= 0): continue #skip all Craver racial weapons
	  WeaponData.append(Weapon.struct()) #extend list of ROOT readable structs
	  Sim = node.getElementsByTagName('Simulation')
	  #enter all the values into the struct
	  WeaponData[counter].Name     = node.attributes['Name'].value
	  WeaponData[counter].MinDmg   = Sim[0].attributes['DamageMin'].value
	  WeaponData[counter].MaxDmg   = Sim[0].attributes['DamageMax'].value
	  WeaponData[counter].CritMult = Sim[0].attributes['CriticMultiplier'].value
	  WeaponData[counter].CritMod  = Sim[0].attributes['CriticChance'].value
	  WeaponData[counter].Evasion  = Sim[0].attributes['InterceptionEvasion'].value
	  WeaponData[counter].Shots    = Sim[0].attributes['NumberPerSalve'].value
	  WeaponData[counter].HitTime  = Sim[0].attributes['TurnBeforeReach'].value
	  WeaponData[counter].Reload   = Sim[0].attributes['TurnToReload'].value
	  WeaponData[counter].Accuracy = Sim[0].attributes['Accuracy'].value
	  for subtype in Sim:
	    Range = subtype.childNodes[3].toxml() #childNodes[3] -> range
	    Type = subtype.childNodes[1].toxml() #childNodes[1] -> Weapon type
	    if(Range.find('Long')     >= 0): WeaponData[counter].Range = 1
	    elif(Range.find('Medium') >= 0): WeaponData[counter].Range = 2
	    elif(Range.find('Short')  >= 0): WeaponData[counter].Range = 3
	    if(Type.find('Kinetic')   >= 0): WeaponData[counter].Type = 1
	    elif(Type.find('Laser')   >= 0): WeaponData[counter].Type = 2
	    elif(Type.find('Missile') >= 0): WeaponData[counter].Type = 3
	  WeaponData[counter].Cost = node.attributes['Cost'].value
	  WeaponData[counter].Tonnage = node.attributes['WeightFlat'].value	
	  WeaponData[counter].Level = node.attributes['Level'].value  
	  counter += 1 #get ready for the next entry
  #part 2: defenses
  if(files == 'DefenseModule.xml'):
	DefensesLoaded = True
        xml = minidom.parse(options.XmlDirectory+ '/' + files) #read in DefenseModule.xml
	DefensesList = xml.getElementsByTagName('DefenseModule') #read in DefenseModules
	counter = 0
	for node in DefensesList:
	  name = node.attributes['Name'].value
	  DefenseData.append(Defense.struct()) #extend list of ROOT readable structs
	  Sim = node.getElementsByTagName('Simulation')
	  #enter all the values into the struct
	  DefenseData[counter].Name     = node.attributes['Name'].value
	  DefenseData[counter].Intercept   = Sim[0].attributes['InterceptionAccuracy'].value
	  DefenseData[counter].Deflection   = Sim[0].attributes['DeflectionPerTurn'].value
	  DefenseData[counter].Absorption = Sim[0].attributes['Absorption'].value
	  DefenseData[counter].Defense  = Sim[0].attributes['Defense'].value
	  for subtype in Sim:
	    Type = subtype.childNodes[1].toxml() #childNodes[1] -> Defense type
	    if(Type.find('Kinetic')   >= 0): DefenseData[counter].Type = 1
	    elif(Type.find('Laser')   >= 0): DefenseData[counter].Type = 2
	    elif(Type.find('Missile') >= 0): DefenseData[counter].Type = 3
	  DefenseData[counter].Cost = node.attributes['Cost'].value
	  DefenseData[counter].Tonnage = node.attributes['WeightFlat'].value	  
	  DefenseData[counter].Level = node.attributes['Level'].value
	  counter += 1 #get ready for the next entry
