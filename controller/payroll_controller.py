from models.employee import employee

class payroll:

    def getPayroll(file): 
        resume = list()
        try:
            file = open (file,'r')
        except(FileNotFoundError, IOError): 
            print("Something went wrong when opening the file")
        for line in file:
            x = line.split("=")
            resume.append(employee(x[0],x[1]))
        return(resume)


