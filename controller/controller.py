class controller:   
     
    def compare_Arrays(scheduleEmployee1, scheduleEmployee2):
            counter = 0
            for i in scheduleEmployee1:
                for j in scheduleEmployee2:
                    if (i.day == j.day):
                        if ((i.hIn <= j.hIn and i.hIn >= j.hIn)or
                     (i.hIn > j.hIn and i.hOut >= j.hOut and i.hIn < j.hOut)or
                     ((i.hIn <= j.hIn and i.hOut >= j.hIn))):
                            counter += 1
            return(counter)

    def calculateMatch(payroll):
        iterator_auxiliar = 1
        iterator = 0
        while(iterator_auxiliar <= len(payroll)-1 and iterator < len(payroll)):
            counter = controller.compare_Arrays(payroll[iterator].times, payroll[iterator_auxiliar].times)
            print (payroll[iterator].name, "-", payroll[iterator_auxiliar].name,"=", counter)
            iterator_auxiliar += 1
            if(iterator_auxiliar == len(payroll)-1 and iterator < len(payroll)):
                iterator_auxiliar = iterator + 2
                iterator = iterator + 1
