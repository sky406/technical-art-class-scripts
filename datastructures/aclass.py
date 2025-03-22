class Transform():
    def __init__(self,
                 position:tuple[float]=[0.0,0.0,0.0],
                 rotation:tuple[float]=[0.0,0.0,0.0],
                 scale:tuple[float]=[1.0,1.0,1.0]):
        """ 
        position, rotation and scale are all float tuples with three values in the form of (x,y,z)
        these are the parts of 
        
        """
        self.pos:tuple[float] = position #the position of the transform
        self.rot:tuple[float] = rotation #the transforms current orientaion
        self.scale:tuple[float] = scale #the transforms current scale
        
    """ methods for manipulating the transform """
    def move(self,x:float=0,y:float=0,z:float=0): 
        """ moves the transform by the x, y nd z value """
        pass

    def setRot(self,x:float=0,y:float=0,z:float=0):
        """ sets the rotation of the transform to a specific value """
        pass
    
    def addRot(self,x:float=0,y:float=0,z:float=0):
        """ adds to the current rotaion of the transform """
        pass
    
    def setScale(self,x:float=1,y:float=1,z:float=1,uniform:float=1):
        """ 
        scale the shape by x, y or z ammount or uniformly
        use the uniform parameter to scale all sides at once  
        """
        pass

    def moveTo(self,x:float,y:float,z:float):
        """ moves the transform to a specfic x, y and z location """
        pass


    """ the next three are just getters for the variables technically useless but i feel like python curses me if i fon't make these """
    def getPos(self):
        return self.pos
    
    def getScale(self):
        return self.scale
    
    def getRot(self):
        return self.rot
    
