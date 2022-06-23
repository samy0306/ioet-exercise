# Resolution: Exercise IOET Schedules
The solution to the exercise was developed using Python 3.10.5, this solution allows to manage the processes through different related classes and their respective methods, which have been implemented seeking to comply with the principle of single responsibility (SOLID principles).
## Exercise:
The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame.
The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.
Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our examples below:
- Example 1:
INPUT
```
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
```
OUTPUT:
```
ASTRID-RENE: 2
ASTRID-ANDRES: 3
RENE-ANDRES: 2
```
- Example 2:
INPUT:
```
RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
```
OUTPUT:
```
RENE-ASTRID: 3
```
## Solution
To provide a solution to the problem posed, two models, two controllers and a main.py file have been defined, whose operating logic is explained below:
### Models:
- Employee
- Schedule
### Controllers
- controller
- payroll_controller.
### Main:
The main file imports the modules: controller and Payroll_controller, from which it calls the methods:
controller. calculateMatch(payroll.getPayroll("input.txt"))
where calculateMatch receives an array, the same that is returned by the getPayroll function getPayroll receives a .txt file that is where the input payrolls are stored.
getPayroll function
It receives as input parameter a .txt file, the same one that when being traversed line by line obtains the data of each line and divides them in 2 text strings.
With these two text strings it creates an object of type employee that is added to a list.
As a result of this function an array of employees is obtained.
### Employee Instance
    For the creation of employee type objects two input parameters are received: name and times, both are text strings (in the getPayroll function the text separated from name and times is sent).
    The employee constructor method is defined, which assigns the value sent from name to the object's own name attribute and on the other hand it declares a 'listTimes' array to which it sends the string times that is separated with the "Split (",")" function, then sent to the getTimes function.
### getTimes 
    This function is inside the employees class and receives as input an array, in this case the listTimes array, returning an array of time type objects.
    Finally, the result of the getTimes function is assigned to the times attribute of the person object.
### calculateMatch function
This function receives as input an array of person type objects, compares through the compare_Arrays function their respective times and prints the number of matches.
Through the iterators: iterator and iterator_auxiliary, it can access the current position and the next position of the payroll, obtaining its different attributes to compare, in the same way conditionals that allow controlling the error "index is out of range" are contemplated,
In addition, it contemplates a conditional and a while loop, which allow the comparison of each of the persons with all the possible combinations.
### Compare_Arrays
    This function receives as input two arrays of schedule type objects, these can be of different sizes. 
    It proceeds to go through them and compare their positions, being that it compares each item with all the items of the other array, this to find matches. The matches are checked with two blocks of if conditionals and counted with a 'counter' variable, which is returned.
    In short, it returns the number of times the two people's schedules matched.
## Instructions to run the project locally
Run the requirements.txt with the following command:
```
pip install -r requirements.txt
```
Run the following command in your working directory.
```
python main.py
```
## Tests execution
Run the following command in your working directory.
```
pytest -v
```
