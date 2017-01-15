from aco_funs import *
from aco_ant import Ant
import sqlite3

def aco_setup(input_file,depo):
    dataM=readData(input_file)
    distM=createDistanceMatrix(dataM)
    locCount=len(dataM)

    initSol=initSolution(depo,dataM,distM)
    
    rt={    'dataM':dataM,
            'distM':distM,
            'locCount':locCount,
            'initSol':initSol}
    return(rt)    

def aco_run(dataM,distM,depo,locCount,initSolution,alpha,BRCP,iterCount,colSize):
    phiM01= [[float(1)/initSolution['vehicleCount'] for i in range(locCount)] for j in range(locCount)]
    phiM02= [[float(1)/initSolution['distance'] for i in range(locCount)] for j in range(locCount)]
    phiM1= [[float(1)/initSolution['vehicleCount'] for i in range(locCount)] for j in range(locCount)]
    phiM2= [[float(1)/initSolution['distance'] for i in range(locCount)] for j in range(locCount)]


    vehicleCount1=initSolution['vehicleCount']
    vehicleCount2=initSolution['vehicleCount']

    tour1=initSolution['tour']
    tour2=initSolution['tour']
    tour_fl1=initSolution['tour_fl']
    tour_fl2=initSolution['tour_fl']

    bestArcs1=[]
    bestArcs2=[]
    bestSolution=initSolution


    for iteration in range(iterCount):
        #visitedArcs1=[]
        #visitedArcs2=[]
        for colony in range(colSize):

            colony1=Ant(vehicleCount=vehicleCount1,dataM=dataM)
            colony2=Ant(vehicleCount=vehicleCount2,dataM=dataM)
            solution1=colony1.calculate(dataM,distM,phiM1,depo,tour1,tour_fl1)
            solution2=colony2.calculate(dataM,distM,phiM2,depo,tour2,tour_fl2)
            
            #Full Solution 1
            if solution1['visitedCount']==locCount-1:
                vehicleCount1-=1
                tour1=solution1['tour']
                tour_fl1=solution1['tour_fl']
                

                if bestSolution['vehicleCount']>solution1['vehicleCount']:
                    bestSolution=solution1
                    bestArcs1=[]
                    vehicleCount2=solution1['vehicleCount']
                    for loc in tour1:
                        bestArcs1.append((loc,tour1[loc]))
                    for loc in tour_fl1:
                        bestArcs1.append((depo,loc))
                
                    print('colony 1')
                    print('alpha\t',alpha)
                    print('iteration\t',iteration)
                    print('colony\t\t',colony)
                    print('vehicleCount\t',solution1['vehicleCount'])
                    print('distance\t',solution1['distance'])
                    print('****************\n')

            #Full Solution 2
            if solution2['visitedCount']==locCount-1:
                
                tour2=solution2['tour']
                tour_fl2=solution2['tour_fl']
                
                if bestSolution['distance']>solution2['distance']:
                    bestSolution=solution2
                    bestArcs2=[]
                    for loc in tour2:
                        bestArcs2.append((loc,tour2[loc]))
                    for loc in tour_fl2:
                        bestArcs2.append((depo,loc))
                    
                    print('colony 2')
                    print('alpha\t',alpha)
                    print('iteration\t',iteration)
                    print('colony\t\t',colony)
                    print('vehicleCount\t',solution2['vehicleCount'])
                    print('distance\t',solution2['distance'])
                    print('****************\n')

            #evaporation
            for loc in solution1['tour']:
                locFrom=loc
                locTo=solution1['tour'][loc]
                phiM1[locFrom][locTo]=(1-alpha)*phiM1[locFrom][locTo]+alpha*phiM01[locFrom][locTo]
           
            for loc in solution2['tour']:
                locFrom=loc
                locTo=solution2['tour'][loc]
                phiM2[locFrom][locTo]=(1-alpha)*phiM2[locFrom][locTo]+alpha*phiM02[locFrom][locTo]
           
        #phi updates

        for arc in bestArcs1:
            locFrom=arc[0]
            locTo=arc[1]
            phiM1[locFrom][locTo]=(1-alpha)*phiM1[locFrom][locTo]+alpha/((bestSolution['vehicleCount']))

        for arc in bestArcs2:
            locFrom=arc[0]
            locTo=arc[1]
            phiM2[locFrom][locTo]=(1-alpha)*phiM2[locFrom][locTo]+alpha/bestSolution['distance']

        
    return bestSolution        
