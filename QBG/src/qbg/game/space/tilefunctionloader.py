import re
import copy
import os
from log4py import Logger
from qbg.config.loaders.loader import Loader
from qbg.game.space.tile import Tile 
from qbg.game.space.tile import TileFunction 

class TileFunctionLoader(Loader):
        
    def __init__(self,directories):
        Loader.__init__(self)
        splitter = re.compile(r'(\s+|\S+)')
        self.directories = splitter.findall(directories)
        self.data = []
        pass
    
    def load(self,data):
        for directory in self.directories:
            if(os.access(directory, os.F_OK)):
                self.loadFiles(directory, os.listdir(directory))
            else:
                self.log.error( directory + ' not exist') 
         
    
    def loadFiles(self,directory, filesList):
        
        for file in filesList:
            self.log.debug(file)
            parser = Loader.loadParserForFile(self,'tilefunction',directory+'/'+file)
            if parser != None:
                self.data.append(parser.loadInClass(TileFunction()))
    
    def getTileFunctionFromCode(self,code):  
        for tilefunction in self.data:
                if tilefunction.code == code:
                    return copy.deepcopy(tilefunction)
        return None
    
    def getTileFunctionFromDefinition(self,codes):  
        self.log.debug('Tiles code '+str(codes))
        
        returnFunctions = []
        
        for code in codes:
            function = self.getTileFunctionFromCode(code)
            if function != None:
                returnFunctions.append(function)        
            
        return returnFunctions
              
             