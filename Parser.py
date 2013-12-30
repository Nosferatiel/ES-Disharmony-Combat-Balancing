import os
import Weapon
from xml.dom import minidom

from optparse import OptionParser

parser = OptionParser()

parser.add_option('--XmlDirectory', metavar='F', type='string', action='store', default='/tmp/mnt/Simulation', dest='XmlDirectory', help='specify input directory for Endless Space xml files')

(options, args) = parser.parse_args()

argv = []

#safeguard bools to kill the program before it does segmentation faults due to missing files
WeaponsLoaded = False

#top level structures for loading all necessary information
WeaponData = list()

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
	  if(name.find('Fake') > 0): continue #skip all the fakes
	  WeaponData.append(Weapon.struct()) #extend list of ROOT readable structs
	  Sim = node.getElementsByTagName('Simulation')
	  #enter all the values into the struct
	  WeaponData[counter].Name = node.attributes['Name'].value
	  WeaponData[counter].MinDmg = Sim[0].attributes['DamageMin'].value
	  WeaponData[counter].MaxDmg = Sim[0].attributes['DamageMax'].value
	  WeaponData[counter].CritMult = Sim[0].attributes['CriticMultiplier'].value
	  WeaponData[counter].CritMod = Sim[0].attributes['CriticChance'].value
	  WeaponData[counter].Evasion = Sim[0].attributes['InterceptionEvasion'].value
	  WeaponData[counter].Shots = Sim[0].attributes['NumberPerSalve'].value
	  WeaponData[counter].HitTime = Sim[0].attributes['TurnBeforeReach'].value
	  WeaponData[counter].Reload = Sim[0].attributes['TurnToReload'].value
	  WeaponData[counter].Accuracy = Sim[0].attributes['Accuracy'].value
	  for subtype in Sim:
	    Range = subtype.getElementsByTagName('RangeClass')
	    Class = subtype.getElementsByTagName('WeaponClass')
	    print subtype.childNodes[3].nodeName #how the hell do I get the valueof this???
	    #WeaponData[counter].Range = Range[0].value
	    #WeaponData[counter].Type = Weapon[0].value
	  WeaponData[counter].Cost = node.attributes['Cost'].value
	  WeaponData[counter].Tonnage = node.attributes['WeightFlat'].value	  
	  counter += 1 #get ready for the next entry
	print WeaponData[10].Accuracy
	print len(WeaponData)
