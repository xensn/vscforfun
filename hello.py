def closest_object(roundTrips):
    #Perform the parsing of roundTrips input here
    total = []
    closestObject = []
    speed_list = roundTrips.split(',')
    if len(speed_list) != 5:
            closestObject = [-1,-1]
    
    else:
        for i,x in enumerate(speed_list):
            dist = (float(speed_list[i]) * 344 ) / 2
            total.append(dist)
        
            closestObject = [total.index(min(total)), min(total)]    

    
    
    return closestObject#Do not remove this line