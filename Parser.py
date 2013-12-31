import os
import Weapon
import Defense
import Hull
from xml.dom import minidom

#Parsing module for getting descriptors of weapons, defenses and a basic hull out of the Endless Space xmls

#part 1: weapons
def LoadWeapons(path):
  #top level structure for loading all necessary information
  WeaponData  = list()
  for files in os.listdir(path): #loading all xml files
    if(files[len(files)-3:len(files)] != 'xml'): continue #ascertain to only load xml files
    if(files == 'WeaponModule.xml'):
	xml = minidom.parse(path + '/' + files) #read in WeaponModule.xml
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
	    Type  = subtype.childNodes[1].toxml() #childNodes[1] -> Weapon type
	    if(Range.find('Long')     >= 0): WeaponData[counter].Range = 1
	    elif(Range.find('Medium') >= 0): WeaponData[counter].Range = 2
	    elif(Range.find('Short')  >= 0): WeaponData[counter].Range = 3
	    if(Type.find('Kinetic')   >= 0): WeaponData[counter].Type = 1
	    elif(Type.find('Laser')   >= 0): WeaponData[counter].Type = 2
	    elif(Type.find('Missile') >= 0): WeaponData[counter].Type = 3
	  WeaponData[counter].Cost    = node.attributes['Cost'].value
	  WeaponData[counter].Tonnage = node.attributes['WeightFlat'].value	
	  WeaponData[counter].Level   = node.attributes['Level'].value  
	  counter += 1 #get ready for the next entry
  if(len(WeaponData)>1): return WeaponData
  else: return -1

#part 2: defenses
def ChargeDefenses(path):
  #top level structure for loading all necessary information
  DefenseData  = list()
  for files in os.listdir(path): #loading all xml files
    if(files[len(files)-3:len(files)] != 'xml'): continue #ascertain to only load xml files
    if(files == 'DefenseModule.xml'):
        xml = minidom.parse(path + '/' + files) #read in DefenseModule.xml
	DefensesList = xml.getElementsByTagName('DefenseModule') #read in DefenseModules
	counter = 0
	for node in DefensesList:
	  name = node.attributes['Name'].value
	  DefenseData.append(Defense.struct()) #extend list of ROOT readable structs
	  Sim = node.getElementsByTagName('Simulation')
	  #enter all the values into the struct
	  DefenseData[counter].Name       = node.attributes['Name'].value
	  DefenseData[counter].Intercept  = Sim[0].attributes['InterceptionAccuracy'].value
	  DefenseData[counter].Deflection = Sim[0].attributes['DeflectionPerTurn'].value
	  DefenseData[counter].Absorption = Sim[0].attributes['Absorption'].value
	  DefenseData[counter].Defense    = Sim[0].attributes['Defense'].value
	  for subtype in Sim:
	    Type = subtype.childNodes[1].toxml() #childNodes[1] -> Defense type
	    if(Type.find('Kinetic')    >= 0): DefenseData[counter].Type = 1
	    elif(Type.find('Laser')    >= 0): DefenseData[counter].Type = 2
	    elif(Type.find('Missile')  >= 0): DefenseData[counter].Type = 3
	  DefenseData[counter].Cost    = node.attributes['Cost'].value
	  DefenseData[counter].Tonnage = node.attributes['WeightFlat'].value	  
	  DefenseData[counter].Level   = node.attributes['Level'].value
	  counter += 1 #get ready for the next entry
  if(len(DefenseData)>1): return DefenseData
  else: return -1

#part 3: hulls
def BuildHulls(path):
  #top level structure for loading all necessary information
  HullData  = list()
  for files in os.listdir(path): #loading all xml files
    if(files[len(files)-3:len(files)] != 'xml'): continue #ascertain to only load xml files
    if(files == 'Hull.xml'):
	HullLoaded = True
	xml = minidom.parse(path + '/' + files) #read in Hull.xml
	HullList = xml.getElementsByTagName('Hull') #read in Hull
	counter = 0
	for node in HullList:
	  name = node.attributes['Name'].value
	  if(name.find('Terran')      >= 0): continue #skip all UE racial hulls
	  if(name.find('Hissho')      >= 0): continue #skip all Hissho racial hulls
	  if(name.find('Swarm')       >= 0): continue #skip all Craver racial hulls
	  if(name.find('Emperor')     >= 0): continue #skip all Sheredyn racial hulls
	  if(name.find('Sophon')      >= 0): continue #skip all Sophon racial hulls
	  if(name.find('Horatio')     >= 0): continue #skip all Horatio racial hulls
	  if(name.find('Sower')       >= 0): continue #skip all Sower racial hulls
	  if(name.find('Amoeba')      >= 0): continue #skip all Amoeba racial hulls
	  if(name.find('Resistance')  >= 0): continue #skip all Pilgrm racial hulls
	  if(name.find('Automaton')   >= 0): continue #skip all Automaton racial hulls
	  if(name.find('Harmony')     >= 0): continue #skip all Harmony racial hulls
	  if(name.find('Vaulter')     >= 0): continue #skip all Vaulter racial hulls
	  if(name.find('Pirates')     >= 0): continue #skip all Pirate racial hulls
	  HullData.append(Hull.struct()) #extend list of ROOT readable structs
	  #enter all the values into the struct
	  HullData[counter].Name  		  = node.attributes['Name'].value
	  HullData[counter].MaxHealth  		  = node.attributes['MaxHealth'].value
	  HullData[counter].Tonnage 	 	  = node.attributes['MaxWeight'].value
	  HullData[counter].MaxSpecialSlotWeight  = node.attributes['MaxSpecialSlotWeight'].value
	  HullData[counter].CommandPoint 	  = node.attributes['CommandPoint'].value
	  HullData[counter].Evade 		  = node.attributes['Evade'].value
	  HullData[counter].Weakness	  	  = node.attributes['HullWeakness'].value
	  HullData[counter].EvasionDisorientation = node.attributes['EvasionDisorientation'].value
	  HullData[counter].Cost  		  = node.attributes['Cost'].value
	  counter += 1 #get ready for the next entry
  if(len(HullData)>1): return HullData
  else: return -1
