from Vehicle import Vehicle
from tkinter import *
class MyFirstGUI:
    
    def __init__(self, master):
        self.vehicleList = []
        self.master = master
        master.title("A simple GUI")

        
        self.label1 = Label(master, text="Enter your Reg Number")
        self.label1.pack()
   
        self.entry1 = Entry()
        self.entry1.pack()

        self.label2 = Label(master, text="Enter Make")
        self.label2.pack()

        self.entry2 = Entry()
        self.entry2.pack()

        self.label3 = Label(master, text="Enter Model")
        self.label3.pack()
   
        self.entry3 = Entry()
        self.entry3.pack()

        self.label4 = Label(master, text="Enter CO2 Emissions")
        self.label4.pack()
   
        self.entry4 = Entry()
        self.entry4.pack()


        #self.quit = Button(master, text="QUIT", command=self.hello)
        #self.quit.pack()

        self.getCO2 = Button(master, text="Get Tax", command=self.getTax)
        self.getCO2.pack()


    def getTax(self):
        thisVehicle = Vehicle(self.entry1.get(),self.entry2.get(),self.entry3.get(),int(self.entry4.get()))
        print("the Tax for this Vehicle is ", thisVehicle.get_annual_tax())

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
