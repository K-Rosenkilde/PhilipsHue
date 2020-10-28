
class huelight:
    def __init__(self, no, pin, direction, group):
#         print("Init huelight Class")
        self.dimdirection = direction 
        self.lightno = no
        self.GPIOPin = pin
        self.group = group
                    
                    
    def setdimdirection(self, dimdirection):
#         print('setname() called')
        self.__dimdirection=dimdirection
    
    def getdimdirection(self):
#        print('getdimdirection() called')
        return self.__dimdirection
    
#     def setdimdirection(self, dimdirection, light):
#         print('setname() called')
#         self.arrayOfLights[light].__dimdirection=dimdirection
    
    def getlightnumber(self, io):
#        print('getlightnumber() called')
        return self.__arrayOfLights.index(io)
    
    dimdirection=property(getdimdirection, setdimdirection)


class huelights:
    def __init__(self):
#        print("Init huelights Class")

        # creating list        
        self.list = []  
        # appending instances to list  
        self.list.append( huelight(1, 16, 'up',   2))  # Stairs 1
        self.list.append( huelight(2, 2, 'down', 2))  # Stairs 2
        self.list.append( huelight(3, 18, 'up',   2))  # Stairs 3
        self.list.append( huelight(4, 19, 'down', 4))  # Entre
        self.list.append( huelight(5, 17, 'up',   5))  # Billed Spot 
        self.list.append( huelight(6, 21, 'down', 0))  # Altan
        self.list.append( huelight(7, 22, 'up',   0))  # Bedroom
        self.list.append( huelight(8, 23, 'down', 0))  # Kuppel
        
        self.list.append( huelight(9,  8, 'up'  , 1))  # Hall 1
        self.list.append( huelight(10, 9, 'down', 0)) 
        self.list.append( huelight(11, 10, 'up',  1))  # Hall 2
        self.list.append( huelight(12, 11, 'down',0))  # Entre
        self.list.append( huelight(13, 12, 'up',  4))  # Dinner UP
        self.list.append( huelight(14, 13, 'down',4))  # Dinner Down
        self.list.append( huelight(15, 14, 'up',  0)) 
        self.list.append( huelight(16, 15, 'down',0))  # Hue Ambiance Spot test
        
        self.list.append( huelight(17, 1, 'up',   1))  # Hall 3
        self.list.append( huelight(18, 20,'down', 3))  # Balcony 2
        self.list.append( huelight(19, 3, 'up',   3))  # Balcony 1
        self.list.append( huelight(20, 4, 'down', 3))  # Balcony 3
        self.list.append( huelight(21, 5, 'up',   0)) 
        self.list.append( huelight(22, 6, 'down', 0)) 
        self.list.append( huelight(23, 7, 'up',   0)) 
        self.list.append( huelight(24, 15, 'down',0))
        

      
    def getlist(self):
#        print('getdimdirection() called')
        return self.list
    
    def getindex(self, GPIO):
#        print("getindex: " + str(GPIO) )
        i = 0 
        for obj in self.list:
            if obj.GPIOPin == GPIO :
#                print( obj.GPIOPin )
                index = i
#            print("Test: " + str(i) + " : "+ obj.dimdirection, obj.GPIOPin, obj.lightno )
            i += 1
#        print("Index: " + str(index))
        return index
    
    def grouplight(self, GPIO) :
        print("grouplight for Channel: " + str(channel) )
        group = self.list[index].group
        if group > 0 : 
            return True
        else:
            return False 
    
    
    def getgroup(self, GPIO):
#         print("getgroup: " + str(GPIO) )
        index = self.getindex(GPIO)
        group = self.list[index].group
#         print("group" + str(group))
        return group

    def getgrouplights(self, group):
#        print("getgrouplights: " + str(group) )
        lightnos = ""
        for obj in self.list:
            if obj.group == group :
#                print("lightno: " + str( obj.lightno ))
                lightnos = lightnos + " " + str(obj.lightno)
        return lightnos
        
    def getlight(self, GPIO):
#        print("getindexx: " + str(GPIO) )
        index = self.getindex(GPIO)
#        print("Indexxx: " +str(index))
        lightno = self.list[index].lightno
#       print("lightno: " + str(lightno))
        GPIOPin = self.list[index].GPIOPin
#        print("GPIOPin: " + str(GPIOPin))       
        dimdirection = self.list[index].dimdirection
#        print("dimdirection: " + str(dimdirection))
        return lightno

    def getdirection(self, GPIO):
        index = self.getindex(GPIO)
        dimdirection = self.list[index].dimdirection
#        print("dimdirection: " + str(dimdirection))
        return dimdirection
    
    def setdirection(self, GPIO, direction):
        index = self.getindex(GPIO)
        self.list[index].dimdirection = direction
#        print("dimdirection: " + str(dimdirection))
        
    myindex=property(getindex)
    lightslist=property(getlist)


H3 = huelights()
index = H3.getlight(18)

