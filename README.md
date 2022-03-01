# Vehicle GUI Example

Calculating the annual tax on your Vehicle in Ireland is determined by the amount of carbon dioxide emissions your Vehicle emits.

Google the rules for car tax in ireland to figure out how to calculate the annual tax based on the cars CO2 emissions. 

To simplify the exercise we will use a more straightforward version of the rule.

If the c02 emissions of the vehicle is less than or equal to 90 grammes per kilometre the tax should be €150 per year. If it is greater than 90 the tax should be €200 per year.

# Part 1
Use this rule to implement the following Vehicle.py class

![alt text](Vehicle.png)


The getters should return the values associated with the attributes they refer to. 
The \__str\__() function should return the reg number, make and model of the vehicle with spaces in between

# Part 2
Implement the following Simple Gui which gets data from the user about a Vehicle
![alt text](VehicleGUI.png)

# Part 3
Create a function which will be called when the button is pressed. The function should instantiate a Vehicle object based on the data input by the user. The function should then out_put the annual car tax for the Vehicle

