from ROOT import TRandom3

def Kinetic(Accuracy, Evasion, Shots, Deflection):
  #typecast all the variables for hit
  Accuracy = float(Accuracy)
  Evasion  = float(Evasion)
  #initialize hit random generator
  HitRandom = TRandom3(0)
  Hit = Accuracy * (1 - Evasion) #calculate hit
  if  (Hit < 0.1): Hit = 0.1     #lower bound
  elif(Hit > 0.9): Hit = 0.9     #upper bound
  if(Hit < HitRandom.Uniform(1)): return 0 #0 is returned for evasion
  else:
    #typecast all variables for deflection
    Shots      = float(Shots)
    Deflection = float(Deflection)
    if  (Shots  > Deflection): return (Shots - Deflection)	#return positive number for hitting shots
    elif(Shots == Deflection): return 666			#if the shots have been called, completely, return exception
    else:                      return (-Shots)			#return negative number for more deflection
