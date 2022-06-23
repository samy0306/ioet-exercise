from models.schedule import schedule                                                                                                                        
class employee:
    def __init__(self, name, times):
        self.name = name
        listTimes = times.split(",")
        self.times =self.getEmployee(listTimes)
    
    def getEmployee(self,listTimes):
        timesDiv = []
        for i in listTimes:
            timesDiv.append(schedule(i[0:2], i[2:7], i[8:13]))
        return(timesDiv)
    











