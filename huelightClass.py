
class huelight:
    def __init__(self, direction, pin, no):
        print("Init huelight Class")
        self.dimdirection = direction 
        self.GPIOPin = pin
        self.lightno = no
                    
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
        print("Init huelights Class")
        # creating list        
        self.list = []  
  
        # appending instances to list  
        self.list.append( huelight('up', 1, 16) ) 
        self.list.append( huelight('up', 2, 17) ) 
        self.list.append( huelight('up', 3, 18) ) 
#     list.append( huelight('up', 4, 16) ) 
#     list.append( huelight('up', 5, 17) ) 
#     list.append( huelight('up', 6, 18) ) 
#     list.append( huelight('up', 7, 16) ) 
#     list.append( huelight('up', 8, 17) ) 
#     list.append( huelight('up', 9, 18) ) 
#     list.append( huelight('up', 10, 16) ) 
#     list.append( huelight('up', 11, 17) ) 
#     list.append( huelight('up', 12, 18) ) 
#     list.append( huelight('up', 13, 16) ) 
#     list.append( huelight('up', 14, 17) ) 
#     list.append( huelight('up', 15, 18) ) 
#     list.append( huelight('up', 16, 16) ) 
#     list.append( huelight('up', 17, 17) ) 
#     list.append( huelight('up', 18, 18) )
#     list.append( huelight('up', 17, 17) ) 
#     list.append( huelight('up', 18, 18) )

#         for obj in self.list: 
#             print( obj.dimdirection, obj.GPIOPin, obj.lightno,  sep =' ' ) 
      
    def getlist(self):
#        print('getdimdirection() called')
        return self.list
    
    def getindex(self, GPIO):
        i = 0 
        for obj in self.list:
            if obj.GPIOPin == GPIO :
                index = i
            print( obj.dimdirection, obj.GPIOPin, obj.lightno,  sep =' ' ) 
        return index
    
    index = property (getindex)
    lightslist=property(getlist)

