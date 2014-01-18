from ROOT import TRandom3

def Compute(minDmg, maxDmg, critChance, critMult, Defense, HullWeakness):
  #typecast all the strings to floats
  minDmg = float(minDmg)
  maxDmg = float(maxDmg)
  critChance = float(critChance)
  critMult = float(critMult)
  Defense = float(Defense)
  HullWeakness = float(HullWeakness)
  #calculate the dmg output
  DmgGenerator = TRandom3(0) #initialize random generator for damage
  Dmg = DmgGenerator.Uniform(1)*(maxDmg-minDmg)+maxDmg #calculate bare damage
  CritGenerator = TRandom3(0) #initialize random generator for crit
  if(CritGenerator.Uniform(1) <= critChance) or (critChance == 0): critMult = 1 #set critical multiplicator to 1, if there is no crit (either by design or chance)
  Dmg *= critMult #apply critical hit
  if(HullWeakness > 0): Dmg *= 1-1/(1+HullWeakness/Defense) #apply defense mitigation, if possible
  return Dmg
