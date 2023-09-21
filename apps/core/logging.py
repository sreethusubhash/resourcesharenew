from .utils import MetaSingleton
from enum import Enum


class LevelEnum(Enum):
    info = 'INFO'
    critical = 'CRITICAL'
    #TODO:Add more options(ERROR,WARNING,)
    
class Logging(metaclass=MetaSingleton):
    def __init__(self,file_name:str):
        self.file_name = file_name
    def _write_log(self,level,message:str):
        """Write to the log file"""
    
        with open(self.file_name,'a') as f:
            f.write(f"[{level.name}] {message}\n")
            #critical msg goes here
            
            
    #create level specific methods
    def info(self,message:str):
        self._write_log(LevelEnum.info,message)
    def critical(self,message:str):
        self._write_log(LevelEnum.critical,message)
    def error(self,message:str):
        self._write_log(LevelEnum.critical,message)
    def warning(self,message:str):
        self._write_log(LevelEnum.critical,message)
    #TODO:Add more level specific methods here
    #critical
    #error
    #warning
    