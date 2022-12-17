import tkinter as tk
from tkinter.constants import ANCHOR, TOP, BOTH, BOTTOM, CENTER, E, END, GROOVE, LEFT, N, RAISED, RIDGE, RIGHT, S, SUNKEN, W, X, Y
import tkinter.messagebox as tmsg
from PIL import Image, ImageTk
import requests


root = tk.Tk()

root.minsize(width=1200, height=750)
app_width = root.winfo_width()
app_height = root.winfo_height()
root.geometry(f'{app_width}x{app_width}')

root.title("Unit Converter")
# root.wm_iconbitmap("img/unit converter.ico")



class Screens:
    def __init__(self):

        self.url = "https://measurement-unit-converter.p.rapidapi.com/length/units"
        self.headers = {
            "X-RapidAPI-Key": "0760466864msh8d9d9885caceea6p1e6454jsnb3eaeb63d084",
            "X-RapidAPI-Host": "measurement-unit-converter.p.rapidapi.com"
        }
        response = requests.request("GET", self.url, headers=self.headers)
        self.data = response.json()
        
        self.frame = None
        self.main_screen()
    
    def main_screen(self, *args):
        # if self.frame is not None:
        #     self.frame.destroy()        

        def button_leave(e):
            statusvar.set("Main Page")
        def button_enter(e, w):
            statusvar.set(w)

        frame = tk.Canvas(root, highlightthickness = 0)
        frame.pack(anchor='w', side = LEFT)

        self.common_frame = tk.Canvas(root, highlightthickness=0)
        self.common_frame.pack(pady = 100)

        self.head= tk.Label(self.common_frame, text =" Convert ", font=("Lucida Handwriting", 50, "bold"), foreground= "black", background = "#00ccff",relief=RIDGE, border = 10)
        self.head.grid(pady =100)

        button_frames = tk.Canvas(frame, highlightthickness=0)
        button_frames.pack()

        buttons = [[
            Image.open('img/buttons/accel.png'),Image.open('img/buttons/angle.png')],[
                Image.open('img/buttons/area.png'),Image.open('img/buttons/charge.png')],[
                    Image.open('img/buttons/current.png'),Image.open('img/buttons/digital.png')],[
                        Image.open('img/buttons/energy.png'),Image.open('img/buttons/force.png')],[
                            Image.open('img/buttons/frequency.png'),Image.open('img/buttons/illuminance.png')],[
                                Image.open('img/buttons/length.png'),Image.open('img/buttons/mass.png')],[
                                    Image.open('img/buttons/parts-per.png'),Image.open('img/buttons/power.png')],[
                                        Image.open('img/buttons/pressure.png'),Image.open('img/buttons/speed.png')],[
                                            Image.open('img/buttons/temp.png'),Image.open('img/buttons/time.png')],[
                                                Image.open('img/buttons/voltage.png'),Image.open('img/buttons/volume.png')],[
                                                    Image.open('img/buttons/binary-decimal.png'),Image.open('img/buttons/currency.png')]
        ]
        words = [[
            'Acceleration','Angle'],[
                'Area','Charge'],[
                    'Current','Digital'],[
                        'Energy','Force'],[
                            'Frequency','Luminous Intensity'],[
                                'Length','Mass'],[
                                    'Parts-Per','Power'],[
                                        'Pressure','Speed'],[
                                            'Temperature','Time'],[
                                                'Voltage','Volume'],[
                                                    'Binary ⇌ Decimal','Currency']
        ]

        b = {}
        all_Functions = [[
            self.accel_Converter,self.angle_Converter],[
                self.area_Converter,self.charge_Converter],[
                    self.current_Converter,self.digital_Converter],[
                        self.energy_Converter,self.force_Converter],[
                            self.frequency_Converter,self.illuminance_Converter],[
                                self.length_Converter,self.mass_Converter],[
                                    self.partPer_Converter,self.power_Converter],[
                                        self.pressure_Converter,self.speed_Converter],[
                                            self.temperature_Converter,self.time_Converter],[
                                                self.voltage_Converter,self.volume_Converter],[
                                                    self.binarydecimal_Converter,self.currency_Converter]
        ]

        
        #buttons and functions........................
        for i in range(0, 11):
            for j in range(0,2):
                b[i, j] = tk.Button(button_frames, border = 0, command = all_Functions[i][j])
                b[i, j].grid(row = i+1, column = j+1,pady = 5, padx =30)
                

                word = words[i][j]
                imagest = buttons[i][j]
                
                resizest_image = imagest.resize((160,40))
                img_stand = ImageTk.PhotoImage(resizest_image)
                b[i, j].img_ref = img_stand
                b[i, j].config(image = img_stand,compound=TOP)
                
                b[i, j].bind("<Enter>", lambda e, w = word: button_enter(e, w))
                b[i, j].bind("<Leave>", button_leave)

        
        #Calculator Button.................
        def calc_button_enter(e):
            calc_button["bg"] = "light blue"
            statusvar.set("Calculator")
        def calc_button_leave(e):
            calc_button["bg"] = 'SystemButtonFace'
            statusvar.set("Main Page")

        calc_button = tk.Button(frame, bd = 0,font = ("Arial", 15, "bold"), command = open_Calculator)
        calc_button.pack(side=LEFT, padx = 50)

        image = Image.open("img/calculator.png")
        resize_image = image.resize((80,80))
        img_calc = ImageTk.PhotoImage(resize_image)
        calc_button.img_ref = img_calc
        calc_button.config(image = img_calc,compound=TOP)
        calc_button.bind("<Leave>", calc_button_leave)
        calc_button.bind("<Enter>", calc_button_enter)


        #Exit Button...........................
        def exit_window(): 
            iExit = tmsg.askquestion("Converter", "Do you want to exit ?")
            # root.wm_iconbitmap("img/converter.ico")
            if iExit=="yes":
                root.destroy()
                
        def exit_button_enter(e):
            exit_button["bg"] = "red"
            exit_button["fg"] = "blue"
            statusvar.set("Sorry to see you go")
        def exit_button_leave(e):
            exit_button["bg"] = 'blue'
            exit_button["fg"] = 'red'
            statusvar.set("Main Page")

        exit_button = tk.Button(frame, text = "Exit",bd = 0,font = ("Arial", 15, "bold"), fg = "red",bg = "blue", command = exit_window)
        exit_button.pack(side = RIGHT, padx=60,ipadx=10)

        image = Image.open("img/unit converter.png")
        resize_image = image.resize((45,40))
        img_exit = ImageTk.PhotoImage(resize_image)
        exit_button.img_ref = img_exit
        exit_button.config(image = img_exit,compound=TOP)
        exit_button.bind("<Leave>", exit_button_leave)
        exit_button.bind("<Enter>", exit_button_enter)
        
        # self.common_frame = tk.Canvas(root, highlightthickness=0)
        # self.common_frame.pack(expand = True)
        # self.calc_Canvas = calc_Canvas



#**********************************Convertion Designing Code**************************************
    def design_Function(self, *args):
        self.head.destroy()


        def on_click(event):
            self.in_entry.configure(state=tk.NORMAL, foreground='black')
            self.in_entry.delete(0, END)
            self.in_entry.unbind('<Button-1>', on_click_id)

        
        def snapHighlightToMouse(event):
            self.in_list.selection_clear(0, END)
            self.in_list.selection_set(self.in_list.nearest(event.y))

        def unhighlight():
            self.in_list.selection_clear(0, END)
        
        self.head_label = tk.Label(self.common_frame, font = ('Arial Rounded MT Bold', 50, 'bold'))
        self.head_label.grid(row = 1, column = 1,ipadx = 150, columnspan=3)

        in_label = tk.Label(self.common_frame, text= 'From: ', font = ('Times New Roman', 20, 'bold'))
        in_label.grid(row =2, column = 1, sticky='w', padx =50)


        self.in_list = tk.Listbox(self.common_frame, width = 25, height = 10, font = 'Vardana 12', background='sky blue')
        self.in_list.grid(row = 3, column=1, padx =50, sticky='w')
        self.in_list.bind('<Motion>', lambda event: snapHighlightToMouse(event))
        self.in_list.bind('<Enter>',  lambda event: snapHighlightToMouse(event))
        self.in_list.bind('<Leave>',  lambda _: unhighlight())

        self.in_entry = tk.Entry(self.common_frame,fg = '#9C9C9C', font = ('callibri', 15, 'bold'))
        self.in_entry.grid(row =4, column = 1, sticky='w', padx = 50)
        self.in_entry.insert(0, "Enter the value here")
        on_click_id = self.in_entry.bind('<Button-1>', on_click)

        out_label = tk.Label(self.common_frame, text = 'To: ', font = ('Times New Roman', 20, 'bold'))
        out_label.grid(row =2, column = 3,padx = 50, sticky='w')

        self.out_entry = tk.Entry(self.common_frame, font = ('callibri', 15, 'bold'))
        self.out_entry.grid(row =4, column = 3, padx = 50, sticky='w')

        self.out_list = tk.Listbox(self.common_frame, width = 25, height = 10, font = 'Vardana 12', background='sky blue')
        self.out_list.grid(row = 3, column=3, padx =50, sticky='w')

        self.res_label = tk.Label(self.common_frame, font = ('callibri', 15, 'bold'))
        self.res_label.grid(row = 5, column = 1, columnspan=2)

        self.convert_Button = tk.Button(self.common_frame,text = 'Convert', font = ('callibri', 15, 'bold'))
        self.convert_Button.grid(row = 6, column = 1, columnspan=3)




#*********************************Mass Converter Code**************************************
    def mass_Converter(self, *args):
        def convert_func():
            get_entry = float(self.in_entry.get())
            list_input = str(self.in_list.get(ANCHOR))
            
            list_out = str(self.out_list.get(ANCHOR))
            len_url = "https://measurement-unit-converter.p.rapidapi.com/mass"
            query_length = {"value": get_entry, "from":list_input, "to": list_out}
            response = requests.request("GET", len_url, headers=self.headers, params=query_length)
            data = response.json()
            self.out_entry.delete(0, END)
            self.out_entry.insert(1, f"{data['result']}")

        self.head.destroy()

        url_mass = self.url[:50] + "mass/units"
        mass_resp = requests.request("GET", url_mass, headers=self.headers)
        mass_data = mass_resp.json()
        li_mass = mass_data
        self.design_Function()
        for item in range(len(li_mass)):
            self.in_list.insert(END, li_mass[item])
            self.out_list.insert(END, li_mass[item])
        self.head_label.config(text = 'Mass')
        statusvar.set("Mass Converter")

        self.convert_Button.config(command=convert_func)



#**********************************Length Converter Code**************************************
    def length_Converter(self, *args):
        def convert_func():
            get_entry = float(self.in_entry.get())
            list_input = str(self.in_list.get(ANCHOR))
            list_out = str(self.out_list.get(ANCHOR))
            len_url = "https://measurement-unit-converter.p.rapidapi.com/length"
            query_length = {"value": get_entry, "from":list_input, "to": list_out}
            response = requests.request("GET", len_url, headers=self.headers, params=query_length)
            data = response.json()
            self.out_entry.delete(0, END)
            self.out_entry.insert(1, f"{data['result']}")

        self.head.destroy()

        li = self.data
        self.design_Function()
        for item in range(len(li)):
            self.in_list.insert(END, li[item])
            self.out_list.insert(END, li[item])
        self.head_label.config(text = 'Length')
        statusvar.set("Length Converter")


        self.convert_Button.config(command=convert_func)



#*********************************Temperature Converter Code**************************************
    def temperature_Converter(self, *args):
        def convert_func():
            get_entry = float(self.in_entry.get())
            list_input = str(self.in_list.get(ANCHOR))
            list_out = str(self.out_list.get(ANCHOR))
            len_url = "https://measurement-unit-converter.p.rapidapi.com/temperature"
            query_length = {"value": get_entry, "from":list_input, "to": list_out}
            response = requests.request("GET", len_url, headers=self.headers, params=query_length)
            data = response.json()
            self.out_entry.delete(0, END)
            self.out_entry.insert(1, f"{data['result']}")

        self.head.destroy()
        url_mass = self.url[:50] + "temperature/units"
        mass_resp = requests.request("GET", url_mass, headers=self.headers)
        mass_data = mass_resp.json()
        li_temp= mass_data

        self.design_Function()
        for item in range(len(li_temp)):
            self.in_list.insert(END, li_temp[item])
            self.out_list.insert(END, li_temp[item])
        self.head_label.config(text = 'Temperature')
        statusvar.set("Temperature Converter")

        self.convert_Button.config(command=convert_func)



#*********************************Time Converter Code**************************************
    def time_Converter(self, *args):
        def convert_func():
            get_entry = float(self.in_entry.get())
            list_input = str(self.in_list.get(ANCHOR))
            list_out = str(self.out_list.get(ANCHOR))
            len_url = "https://measurement-unit-converter.p.rapidapi.com/time"
            query_length = {"value": get_entry, "from":list_input, "to": list_out}
            response = requests.request("GET", len_url, headers=self.headers, params=query_length)
            data = response.json()
            self.out_entry.delete(0, END)
            self.out_entry.insert(1, f"{data['result']}")

        self.head.destroy()
        url_mass = self.url[:50] + "time/units"
        mass_resp = requests.request("GET", url_mass, headers=self.headers)
        mass_data = mass_resp.json()
        li_time= mass_data

        self.design_Function()
        for item in range(len(li_time)):
            self.in_list.insert(END, li_time[item])
            self.out_list.insert(END, li_time[item])
        self.head_label.config(text = 'Time')
        statusvar.set("Time Converter")

        self.convert_Button.config(command=convert_func)


#****************************************Acceleration Function**************************************
    def accel_Converter(self, *args):
        def convert_func():
            get_entry = float(self.in_entry.get())
            list_input = str(self.in_list.get(ANCHOR))
            list_out = str(self.out_list.get(ANCHOR))
            len_url = "https://measurement-unit-converter.p.rapidapi.com/acceleration"
            query_length = {"value": get_entry, "from":list_input, "to": list_out}
            response = requests.request("GET", len_url, headers=self.headers, params=query_length)
            data = response.json()
            self.out_entry.delete(0, END)
            self.out_entry.insert(1, f"{data['result']}")

        self.head.destroy()
        url_mass = self.url[:50] + "acceleration/units"
        mass_resp = requests.request("GET", url_mass, headers=self.headers)
        mass_data = mass_resp.json()
        li_time= mass_data

        self.design_Function()
        for item in range(len(li_time)):
            self.in_list.insert(END, li_time[item])
            self.out_list.insert(END, li_time[item])
        self.head_label.config(text = 'Acceleration')
        statusvar.set("Acceleration Converter")

        self.convert_Button.config(command=convert_func)



#****************************************Angle Function***************************************
    def angle_Converter(self, *args):
        def convert_func():
            get_entry = float(self.in_entry.get())
            list_input = str(self.in_list.get(ANCHOR))
            list_out = str(self.out_list.get(ANCHOR))
            len_url = "https://measurement-unit-converter.p.rapidapi.com/angle"
            query_length = {"value": get_entry, "from":list_input, "to": list_out}
            response = requests.request("GET", len_url, headers=self.headers, params=query_length)
            data = response.json()
            self.out_entry.delete(0, END)
            self.out_entry.insert(1, f"{data['result']}")

        self.head.destroy()
        url_mass = self.url[:50] + "angle/units"
        mass_resp = requests.request("GET", url_mass, headers=self.headers)
        mass_data = mass_resp.json()
        li_time= mass_data

        self.design_Function()
        for item in range(len(li_time)):
            self.in_list.insert(END, li_time[item])
            self.out_list.insert(END, li_time[item])
        self.head_label.config(text = 'Angle')
        statusvar.set("Angle Converter")

        self.convert_Button.config(command=convert_func)


#****************************************Area Function*****************************************
    def area_Converter(self, *args):
        def convert_func():
            get_entry = float(self.in_entry.get())
            list_input = str(self.in_list.get(ANCHOR))
            list_out = str(self.out_list.get(ANCHOR))
            len_url = "https://measurement-unit-converter.p.rapidapi.com/area"
            query_length = {"value": get_entry, "from":list_input, "to": list_out}
            response = requests.request("GET", len_url, headers=self.headers, params=query_length)
            data = response.json()
            self.out_entry.delete(0, END)
            self.out_entry.insert(1, f"{data['result']}")

        self.head.destroy()
        url_mass = self.url[:50] + "area/units"
        mass_resp = requests.request("GET", url_mass, headers=self.headers)
        mass_data = mass_resp.json()
        li_time= mass_data

        self.design_Function()
        for item in range(len(li_time)):
            self.in_list.insert(END, li_time[item])
            self.out_list.insert(END, li_time[item])
        self.head_label.config(text = 'Area')
        statusvar.set("Area Converter")

        self.convert_Button.config(command=convert_func)


#***************************************Charge Function***************************************
    def charge_Converter(self, *args):
        def convert_func():
            get_entry = float(self.in_entry.get())
            list_input = str(self.in_list.get(ANCHOR))
            list_out = str(self.out_list.get(ANCHOR))
            len_url = "https://measurement-unit-converter.p.rapidapi.com/charge"
            query_length = {"value": get_entry, "from":list_input, "to": list_out}
            response = requests.request("GET", len_url, headers=self.headers, params=query_length)
            data = response.json()
            self.out_entry.delete(0, END)
            self.out_entry.insert(1, f"{data['result']}")

        self.head.destroy()
        url_mass = self.url[:50] + "charge/units"
        mass_resp = requests.request("GET", url_mass, headers=self.headers)
        mass_data = mass_resp.json()
        li_time= mass_data

        self.design_Function()
        for item in range(len(li_time)):
            self.in_list.insert(END, li_time[item])
            self.out_list.insert(END, li_time[item])
        self.head_label.config(text = 'Charge')
        statusvar.set("Charge Converter")

        self.convert_Button.config(command=convert_func)
        


#*********************************************Current Function*******************************
    def current_Converter(self, *args):
        def convert_func():
            get_entry = float(self.in_entry.get())
            list_input = str(self.in_list.get(ANCHOR))
            list_out = str(self.out_list.get(ANCHOR))
            len_url = "https://measurement-unit-converter.p.rapidapi.com/current"
            query_length = {"value": get_entry, "from":list_input, "to": list_out}
            response = requests.request("GET", len_url, headers=self.headers, params=query_length)
            data = response.json()
            self.out_entry.delete(0, END)
            self.out_entry.insert(1, f"{data['result']}")

        self.head.destroy()
        url_mass = self.url[:50] + "current/units"
        mass_resp = requests.request("GET", url_mass, headers=self.headers)
        mass_data = mass_resp.json()
        li_time= mass_data

        self.design_Function()
        for item in range(len(li_time)):
            self.in_list.insert(END, li_time[item])
            self.out_list.insert(END, li_time[item])
        self.head_label.config(text = 'Current')
        statusvar.set("Current Converter")

        self.convert_Button.config(command=convert_func)



#***********************************Digital Function************************************
    def digital_Converter(self, *args):
        def convert_func():
            get_entry = float(self.in_entry.get())
            list_input = str(self.in_list.get(ANCHOR))
            list_out = str(self.out_list.get(ANCHOR))
            len_url = "https://measurement-unit-converter.p.rapidapi.com/digital"
            query_length = {"value": get_entry, "from":list_input, "to": list_out}
            response = requests.request("GET", len_url, headers=self.headers, params=query_length)
            data = response.json()
            self.out_entry.delete(0, END)
            self.out_entry.insert(1, f"{data['result']}")

        self.head.destroy()
        url_mass = self.url[:50] + "digital/units"
        mass_resp = requests.request("GET", url_mass, headers=self.headers)
        mass_data = mass_resp.json()
        li_time= mass_data

        self.design_Function()
        for item in range(len(li_time)):
            self.in_list.insert(END, li_time[item])
            self.out_list.insert(END, li_time[item])
        self.head_label.config(text = 'Digital')
        statusvar.set("Digital Converter")

        self.convert_Button.config(command=convert_func)



#***********************************************Energy Function*******************************        
    def energy_Converter(self, *args):
        def convert_func():
            get_entry = float(self.in_entry.get())
            list_input = str(self.in_list.get(ANCHOR))
            list_out = str(self.out_list.get(ANCHOR))
            len_url = "https://measurement-unit-converter.p.rapidapi.com/energy"
            query_length = {"value": get_entry, "from":list_input, "to": list_out}
            response = requests.request("GET", len_url, headers=self.headers, params=query_length)
            data = response.json()
            self.out_entry.delete(0, END)
            self.out_entry.insert(1, f"{data['result']}")

        self.head.destroy()
        url_mass = self.url[:50] + "energy/units"
        mass_resp = requests.request("GET", url_mass, headers=self.headers)
        mass_data = mass_resp.json()
        li_time= mass_data

        self.design_Function()
        for item in range(len(li_time)):
            self.in_list.insert(END, li_time[item])
            self.out_list.insert(END, li_time[item])
        self.head_label.config(text = 'Energy')
        statusvar.set("Energy Converter")

        self.convert_Button.config(command=convert_func)
        


#***************************Force Function***********************************
    def force_Converter(self, *args):
        def convert_func():
            get_entry = float(self.in_entry.get())
            list_input = str(self.in_list.get(ANCHOR))
            list_out = str(self.out_list.get(ANCHOR))
            len_url = "https://measurement-unit-converter.p.rapidapi.com/force"
            query_length = {"value": get_entry, "from":list_input, "to": list_out}
            response = requests.request("GET", len_url, headers=self.headers, params=query_length)
            data = response.json()
            self.out_entry.delete(0, END)
            self.out_entry.insert(1, f"{data['result']}")

        self.head.destroy()
        url_mass = self.url[:50] + "force/units"
        mass_resp = requests.request("GET", url_mass, headers=self.headers)
        mass_data = mass_resp.json()
        li_time= mass_data

        self.design_Function()
        for item in range(len(li_time)):
            self.in_list.insert(END, li_time[item])
            self.out_list.insert(END, li_time[item])
        self.head_label.config(text = 'Force')
        statusvar.set("Force Converter")

        self.convert_Button.config(command=convert_func)
        


#*******************************Frequency Function**********************************
    def frequency_Converter(self, *args):
        def convert_func():
            get_entry = float(self.in_entry.get())
            list_input = str(self.in_list.get(ANCHOR))
            list_out = str(self.out_list.get(ANCHOR))
            len_url = "https://measurement-unit-converter.p.rapidapi.com/frequency"
            query_length = {"value": get_entry, "from":list_input, "to": list_out}
            response = requests.request("GET", len_url, headers=self.headers, params=query_length)
            data = response.json()
            self.out_entry.delete(0, END)
            self.out_entry.insert(1, f"{data['result']}")

        self.head.destroy()
        url_mass = self.url[:50] + "frequency/units"
        mass_resp = requests.request("GET", url_mass, headers=self.headers)
        mass_data = mass_resp.json()
        li_time= mass_data

        self.design_Function()
        for item in range(len(li_time)):
            self.in_list.insert(END, li_time[item])
            self.out_list.insert(END, li_time[item])
        self.head_label.config(text = 'Frequency')
        statusvar.set("Frequency Converter")

        self.convert_Button.config(command=convert_func)
        

#******************************Parts-per Function********************************
    def partPer_Converter(self, *args):
        def convert_func():
            get_entry = float(self.in_entry.get())
            list_input = str(self.in_list.get(ANCHOR))
            list_out = str(self.out_list.get(ANCHOR))
            len_url = "https://measurement-unit-converter.p.rapidapi.com/partsPer"
            query_length = {"value": get_entry, "from":list_input, "to": list_out}
            response = requests.request("GET", len_url, headers=self.headers, params=query_length)
            data = response.json()
            self.out_entry.delete(0, END)
            self.out_entry.insert(1, f"{data['result']}")

        self.head.destroy()
        url_mass = self.url[:50] + "partsPer/units"
        mass_resp = requests.request("GET", url_mass, headers=self.headers)
        mass_data = mass_resp.json()
        li_time= mass_data

        self.design_Function()
        for item in range(len(li_time)):
            self.in_list.insert(END, li_time[item])
            self.out_list.insert(END, li_time[item])
        self.head_label.config(text = 'Parts-Per')
        statusvar.set("Parts-Per Converter")

        self.convert_Button.config(command=convert_func)



#**********************************Power Function****************************
    def power_Converter(self, *args):
        def convert_func():
            get_entry = float(self.in_entry.get())
            list_input = str(self.in_list.get(ANCHOR))
            list_out = str(self.out_list.get(ANCHOR))
            len_url = "https://measurement-unit-converter.p.rapidapi.com/power"
            query_length = {"value": get_entry, "from":list_input, "to": list_out}
            response = requests.request("GET", len_url, headers=self.headers, params=query_length)
            data = response.json()
            self.out_entry.delete(0, END)
            self.out_entry.insert(1, f"{data['result']}")

        self.head.destroy()
        url_mass = self.url[:50] + "power/units"
        mass_resp = requests.request("GET", url_mass, headers=self.headers)
        mass_data = mass_resp.json()
        li_time= mass_data

        self.design_Function()
        for item in range(len(li_time)):
            self.in_list.insert(END, li_time[item])
            self.out_list.insert(END, li_time[item])
        self.head_label.config(text = 'Power')
        statusvar.set("Power Converter")

        self.convert_Button.config(command=convert_func)



#******************************Pressure Function************************
    def pressure_Converter(self, *args):
        def convert_func():
            get_entry = float(self.in_entry.get())
            list_input = str(self.in_list.get(ANCHOR))
            list_out = str(self.out_list.get(ANCHOR))
            len_url = "https://measurement-unit-converter.p.rapidapi.com/pressure"
            query_length = {"value": get_entry, "from":list_input, "to": list_out}
            response = requests.request("GET", len_url, headers=self.headers, params=query_length)
            data = response.json()
            self.out_entry.delete(0, END)
            self.out_entry.insert(1, f"{data['result']}")

        self.head.destroy()
        url_mass = self.url[:50] + "pressure/units"
        mass_resp = requests.request("GET", url_mass, headers=self.headers)
        mass_data = mass_resp.json()
        li_time= mass_data

        self.design_Function()
        for item in range(len(li_time)):
            self.in_list.insert(END, li_time[item])
            self.out_list.insert(END, li_time[item])
        self.head_label.config(text = 'Pressure')
        statusvar.set("Pressure Converter")

        self.convert_Button.config(command=convert_func)



#*******************************Speed Function****************************
    def speed_Converter(self, *args):
        def convert_func():
            get_entry = float(self.in_entry.get())
            list_input = str(self.in_list.get(ANCHOR))
            list_out = str(self.out_list.get(ANCHOR))
            len_url = "https://measurement-unit-converter.p.rapidapi.com/speed"
            query_length = {"value": get_entry, "from":list_input, "to": list_out}
            response = requests.request("GET", len_url, headers=self.headers, params=query_length)
            data = response.json()
            self.out_entry.delete(0, END)
            self.out_entry.insert(1, f"{data['result']}")

        self.head.destroy()
        url_mass = self.url[:50] + "speed/units"
        mass_resp = requests.request("GET", url_mass, headers=self.headers)
        mass_data = mass_resp.json()
        li_time= mass_data

        self.design_Function()
        for item in range(len(li_time)):
            self.in_list.insert(END, li_time[item])
            self.out_list.insert(END, li_time[item])
        self.head_label.config(text = 'Speed')
        statusvar.set("Speed Converter")

        self.convert_Button.config(command=convert_func)



#******************************Voltage Function*************************
    def voltage_Converter(self, *args):
        def convert_func():
            get_entry = float(self.in_entry.get())
            list_input = str(self.in_list.get(ANCHOR))
            list_out = str(self.out_list.get(ANCHOR))
            len_url = "https://measurement-unit-converter.p.rapidapi.com/voltage"
            query_length = {"value": get_entry, "from":list_input, "to": list_out}
            response = requests.request("GET", len_url, headers=self.headers, params=query_length)
            data = response.json()
            self.out_entry.delete(0, END)
            self.out_entry.insert(1, f"{data['result']}")

        self.head.destroy()
        url_mass = self.url[:50] + "voltage/units"
        mass_resp = requests.request("GET", url_mass, headers=self.headers)
        mass_data = mass_resp.json()
        li_time= mass_data

        self.design_Function()
        for item in range(len(li_time)):
            self.in_list.insert(END, li_time[item])
            self.out_list.insert(END, li_time[item])
        self.head_label.config(text = 'Voltage')
        statusvar.set("Voltage Converter")

        self.convert_Button.config(command=convert_func)




#**************************************Volume Function**********************************
    def volume_Converter(self, *args):
        def convert_func():
            get_entry = float(self.in_entry.get())
            list_input = str(self.in_list.get(ANCHOR))
            list_out = str(self.out_list.get(ANCHOR))
            len_url = "https://measurement-unit-converter.p.rapidapi.com/volume"
            query_length = {"value": get_entry, "from":list_input, "to": list_out}
            response = requests.request("GET", len_url, headers=self.headers, params=query_length)
            data = response.json()
            self.out_entry.delete(0, END)
            self.out_entry.insert(1, f"{data['result']}")

        self.head.destroy()
        url_mass = self.url[:50] + "volume/units"
        mass_resp = requests.request("GET", url_mass, headers=self.headers)
        mass_data = mass_resp.json()
        li_time= mass_data

        self.design_Function()
        for item in range(len(li_time)):
            self.in_list.insert(END, li_time[item])
            self.out_list.insert(END, li_time[item])
        self.head_label.config(text = 'Volume')
        statusvar.set("Volume Converter")

        self.convert_Button.config(command=convert_func)
    
    
    
#**************************Illuminance Function******************************    
    def illuminance_Converter(self, *args):
        def convert_func():
            get_entry = float(self.in_entry.get())
            list_input = str(self.in_list.get(ANCHOR))
            list_out = str(self.out_list.get(ANCHOR))
            len_url = "https://measurement-unit-converter.p.rapidapi.com/illuminance"
            query_length = {"value": get_entry, "from":list_input, "to": list_out}
            response = requests.request("GET", len_url, headers=self.headers, params=query_length)
            data = response.json()
            self.out_entry.delete(0, END)
            self.out_entry.insert(1, f"{data['result']}")

        self.head.destroy()
        url_mass = self.url[:50] + "illuminance/units"
        mass_resp = requests.request("GET", url_mass, headers=self.headers)
        mass_data = mass_resp.json()
        li_time= mass_data

        self.design_Function()
        for item in range(len(li_time)):
            self.in_list.insert(END, li_time[item])
            self.out_list.insert(END, li_time[item])
        self.head_label.config(text = 'Illuminance')
        statusvar.set("Illuminance Converter")

        self.convert_Button.config(command=convert_func)
    
    
        


#*********************************Binary to Decimal Converter Code*******************************
    def binarydecimal_Converter(self, *args):
        from numpy import binary_repr
        import itertools
        
        binary_root = tk.Toplevel()

        width = root.winfo_width()
        height = root.winfo_height()
        binary_root.update()
        binary_root.background_image = background_image = PhotoImage(file = r"img/binary_wall.png")


        mainframe = Canvas(binary_root, height =height, width=width)
        mainframe.pack(fill = 'both', expand=True)
        mainframe.create_image(0, 0, image = background_image, anchor = 'nw')

        def decimal_2_bin(*args):
            try:
                value = int(decimal.get())
                binary.set(binary_repr(value, None))
            except ValueError:
                pass

        def BtoD():

            def main_function():
                value = 0
                binary = list(decimal_entry.get())
                for i in range(len(binary)):
                    digit = binary.pop()

                    if digit == '1':
                        value = value + pow(2, i)
                binary_output.delete(0, END)
                binary_output.insert(1, value)

            binary_output.delete(0, END)
            decimal_entry.delete(0, END)

            def info_button_leave(e, *args):
                info_enter.pack_forget()
            def info_button_enter(e):
                info_enter.pack(pady = 100,padx =50, anchor='e')

            note_var="Note: In Binary to Decimal\nconverter if you put any\ndecimal number in Binary\nfield, it will treat that\nnumber as zero!"
            info_enter = tk.Text(mainframe, width = 23,height=5, font = ("Bookman Old Styel", 11,'bold'))
            info_enter.insert(INSERT,note_var)
            info_enter.configure(state='disabled')
            
            i_image = Image.open("img/info_button.png")
            resized_image = i_image.resize((40,38), Image.ANTIALIAS)
            root.img_info = img_info = ImageTk.PhotoImage(resized_image)

            self.info_button = mainframe.create_image(f'{width/2+230}', 150, image = img_info)
            mainframe.tag_bind(self.info_button, "<Leave>", info_button_leave)
            mainframe.tag_bind(self.info_button, "<Enter>", info_button_enter)

            mainframe.itemconfig(main_head, text = "Binary To Decimal",font = ("Bookman Old Style",40,"bold"), fill = 'red')

            mainframe.itemconfig(first_head, text="Enter Binary Number:",font = ("Bookman Old Style", 25, "bold"), fill ='BLue')

            mainframe.itemconfig(second_head, text="Decimal", font = ("Bookman Old Style", 25, "bold"), fill = 'blue')

            calculat_button.configure(command = main_function)


        def DtoB():

            def decimal_2_bin(*args):
                try:
                    value = int(decimal.get())
                    binary.set(binary_repr(value, None))
                except ValueError:
                    pass

            binary_output.delete(0, tk.END)
            decimal_entry.delete(0, tk.END)
            
            mainframe.delete(self.info_button)

            mainframe.itemconfig(main_head, text = "Decimal To Binary",font = ("Bookman Old Style",40,"bold"), fill = 'red')

            mainframe.itemconfig(first_head, text="Enter Decimal Number:",font = ("Bookman Old Style", 25, "bold"), fill ='BLue')

            mainframe.itemconfig(second_head, text="Binary", font = ("Bookman Old Style", 25, "bold"), fill = 'blue')

            calculat_button.configure(command = decimal_2_bin)


        main_head = mainframe.create_text(f'{width/2}', 40, text = "Decimal To Binary",font = ("Bookman Old Style",40,"bold"), fill = 'red')


        first_head = mainframe.create_text(f'{width/2}', 110, text="Enter Decimal Integer:",font = ("Bookman Old Style", 25, "bold"), fill = 'blue')

        decimal = StringVar()
        decimal_entry = tk.Entry(mainframe, width=30, justify=CENTER,textvariable=decimal, font = ("Bookman Old Style", 15, "bold"))
        mainframe.create_window(f'{width/2}', 150, window = decimal_entry)

        second_head = mainframe.create_text(f'{width/2}',220, text="Binary", font = ("Bookman Old Style", 25, "bold"), fill = 'blue')

        binary = StringVar()
        binary_output = tk.Entry(mainframe, width=30,justify=CENTER, textvariable=binary, font = ("Bookman Old Style", 20, "bold"))
        mainframe.create_window(f'{width/2}',260, window = binary_output)


        calculat_button = tk.Button(mainframe, text="Calculate", command=decimal_2_bin,font = ("Bookman Old Style", 15, "bold"))
        calculat_button.pack()
        mainframe.create_window(f'{width/2}',320, window = calculat_button)

        decimal_entry.focus()
        root.bind("<Return>", decimal_2_bin)


        toggle_funcs = itertools.cycle((BtoD, DtoB))

        def toggle():
            func = next(toggle_funcs)
            func()

        cycle_button = tk.Button(mainframe,font = ("Bookman Old Style", 15, "bold"), text = "Binary ⇌ Decimal", command = toggle)
        cycle_button_window = mainframe.create_window(f'{width/2}', 420, window = cycle_button)

        back_button = tk.Button(mainframe,font = ("Bookman Old Style", 15, "bold"), text = "Back", command = binary_root.destroy)
        back_button_window = mainframe.create_window(f'{width/2}', 500, window = back_button)

        binary_root.mainloop()




#*********************************Currency Converter Code**************************************
    def currency_Converter(self, *args):
        from google_currency import convert
        CODES = {
        "AFN": "Afghan Afghani",
        "ALL": "Albanian Lek",
        "DZD": "Algerian Dinar",
        "AOA": "Angolan Kwanza",
        "ARS": "Argentine Peso",
        "AMD": "Armenian Dram",
        "AWG": "Aruban Florin",
        "AUD": "Australian Dollar",
        "AZN": "Azerbaijani Manat",
        "BSD": "Bahamian Dollar",
        "BHD": "Bahraini Dinar",
        "BBD": "Bajan dollar",
        "BDT": "Bangladeshi Taka",
        "BYR": "Belarusian Ruble",
        "BYN": "Belarusian Ruble",
        "BZD": "Belize Dollar",
        "BMD": "Bermudan Dollar",
        "BTN": "Bhutan currency",
        "BTC": "Bitcoin",
        "BCH": "Bitcoin Cash",
        "BOB": "Bolivian Boliviano",
        "BAM": "Bosnia-Herzegovina Convertible Mark",
        "BWP": "Botswanan Pula",
        "BRL": "Brazilian Real",
        "BND": "Brunei Dollar",
        "BGN": "Bulgarian Lev",
        "BIF": "Burundian Franc",
        "XPF": "CFP Franc",
        "KHR": "Cambodian riel",
        "CAD": "Canadian Dollar",
        "CVE": "Cape Verdean Escudo",
        "KYD": "Cayman Islands Dollar",
        "XAF": "Central African CFA franc",
        "CLP": "Chilean Peso",
        "CLF": "Chilean Unit of Account (UF)",
        "CNY": "Chinese Yuan",
        "CNH": "Chinese Yuan (offshore)",
        "COP": "Colombian Peso",
        "KMF": "Comorian franc",
        "CDF": "Congolese Franc",
        "CRC": "Costa Rican Colón",
        "HRK": "Croatian Kuna",
        "CUP": "Cuban Peso",
        "CZK": "Czech Koruna",
        "DKK": "Danish Krone",
        "DJF": "Djiboutian Franc",
        "DOP": "Dominican Peso",
        "XCD": "East Caribbean Dollar",
        "EGP": "Egyptian Pound",
        "ETH": "Ether",
        "ETB": "Ethiopian Birr",
        "EUR": "Euro",
        "FJD": "Fijian Dollar",
        "GMD": "Gambian dalasi",
        "GEL": "Georgian Lari",
        "GHC": "Ghanaian Cedi",
        "GHS": "Ghanaian Cedi",
        "GIP": "Gibraltar Pound",
        "GTQ": "Guatemalan Quetzal",
        "GNF": "Guinean Franc",
        "GYD": "Guyanaese Dollar",
        "HTG": "Haitian Gourde",
        "HNL": "Honduran Lempira",
        "HKD": "Hong Kong Dollar",
        "HUF": "Hungarian Forint",
        "ISK": "Icelandic Króna",
        "INR": "Indian Rupee",
        "IDR": "Indonesian Rupiah",
        "IRR": "Iranian Rial",
        "IQD": "Iraqi Dinar",
        "ILS": "Israeli New Shekel",
        "JMD": "Jamaican Dollar",
        "JPY": "Japanese Yen",
        "JOD": "Jordanian Dinar",
        "KZT": "Kazakhstani Tenge",
        "KES": "Kenyan Shilling",
        "KWD": "Kuwaiti Dinar",
        "KGS": "Kyrgystani Som",
        "LAK": "Laotian Kip",
        "LBP": "Lebanese pound",
        "LSL": "Lesotho loti",
        "LRD": "Liberian Dollar",
        "LYD": "Libyan Dinar",
        "LTC": "Litecoin",
        "MOP": "Macanese Pataca",
        "MKD": "Macedonian Denar",
        "MGA": "Malagasy Ariary",
        "MWK": "Malawian Kwacha",
        "MYR": "Malaysian Ringgit",
        "MVR": "Maldivian Rufiyaa",
        "MRO": "Mauritanian Ouguiya (1973–2017)",
        "MUR": "Mauritian Rupee",
        "MXN": "Mexican Peso",
        "MDL": "Moldovan Leu",
        "MAD": "Moroccan Dirham",
        "MZM": "Mozambican metical",
        "MZN": "Mozambican metical",
        "MMK": "Myanmar Kyat",
        "TWD": "New Taiwan dollar",
        "NAD": "Namibian dollar",
        "NPR": "Nepalese Rupee",
        "ANG": "Netherlands Antillean Guilder",
        "NZD": "New Zealand Dollar",
        "NIO": "Nicaraguan Córdoba",
        "NGN": "Nigerian Naira",
        "NOK": "Norwegian Krone",
        "OMR": "Omani Rial",
        "PKR": "Pakistani Rupee",
        "PAB": "Panamanian Balboa",
        "PGK": "Papua New Guinean Kina",
        "PYG": "Paraguayan Guarani",
        "PHP": "Philippine Piso",
        "PLN": "Poland złoty",
        "GBP": "Pound sterling",
        "QAR": "Qatari Rial",
        "ROL": "Romanian Leu",
        "RON": "Romanian Leu",
        "RUR": "Russian Ruble",
        "RUB": "Russian Ruble",
        "RWF": "Rwandan franc",
        "SVC": "Salvadoran Colón",
        "SAR": "Saudi Riyal",
        "CSD": "Serbian Dinar",
        "RSD": "Serbian Dinar",
        "SCR": "Seychellois Rupee",
        "SLL": "Sierra Leonean Leone",
        "SGD": "Singapore Dollar",
        "PEN": "Sol",
        "SBD": "Solomon Islands Dollar",
        "SOS": "Somali Shilling",
        "ZAR": "South African Rand",
        "KRW": "South Korean won",
        "VEF": "Sovereign Bolivar",
        "XDR": "Special Drawing Rights",
        "LKR": "Sri Lankan Rupee",
        "SSP": "Sudanese pound",
        "SDG": "Sudanese pound",
        "SRD": "Surinamese Dollar",
        "SZL": "Swazi Lilangeni",
        "SEK": "Swedish Krona",
        "CHF": "Swiss Franc",
        "TJS": "Tajikistani Somoni",
        "TZS": "Tanzanian Shilling",
        "THB": "Thai Baht",
        "TOP": "Tongan Paʻanga",
        "TTD": "Trinidad & Tobago Dollar",
        "TND": "Tunisian Dinar",
        "TRY": "Turkish lira",
        "TMM": "Turkmenistan manat",
        "TMT": "Turkmenistan manat",
        "UGX": "Ugandan Shilling",
        "UAH": "Ukrainian hryvnia",
        "AED": "United Arab Emirates Dirham",
        "USD": "United States Dollar",
        "UYU": "Uruguayan Peso",
        "UZS": "Uzbekistani Som",
        "VND": "Vietnamese dong",
        "XOF": "West African CFA franc",
        "YER": "Yemeni Rial",
        "ZMW": "Zambian Kwacha"
        }
        list1 = list(CODES.keys())
        import webbrowser
        try:
            from tkinter import Tk, Frame
        except ImportError:
            from tkinter import Tk, Frame

        
        iExit = tmsg.askquestion("Currency", "You will be directed to Online Currency Converter for current Updates of currencies!\nDo you want to go to Currency Converter?\n\n")
        root.wm_iconbitmap("img/unit converter.ico")
        if iExit=="yes":
            webbrowser.open_new(r"https://www.xe.com/currencyconverter/")
        # list2 = list(CODES.key())
        # def convert_func():
        #     get_entry = float(self.in_entry.get())
        #     list_input = str(self.in_list.get(ANCHOR))
        #     list_out = str(self.out_list.get(ANCHOR))
        #     responce = convert(list_input, list_out, get_entry)
        #     self.out_entry.delete(0, END)
        #     self.out_entry.insert(1, f"{responce[40:45]}")

        # self.head.destroy()
        # self.design_Function()
        # for item in range(len(list1)):
        #     self.in_list.insert(END, list1[item])
        #     self.out_list.insert(END, list1[item])
        # self.head_label.config(text = 'Currency')
        # statusvar.set("Currency Converter")

        # self.convert_Button.config(command=convert_func)




from tkinter import *
from PIL import Image,ImageTk
def open_Calculator(*args):
    import itertools
    import math
    # import tkinter.messagebox
    Calc_window = tk.Toplevel()
    Calc_window.title("Standard Calculator") 
    # Calc_window.wm_iconbitmap("img/unit converter.ico")
    Calc_window.configure(background = 'white') 
    Calc_window.resizable(width=False, height=False)
    Calc_window.geometry("480x645+450+90")

    calc = Frame(Calc_window)
    calc.pack()


    class Calc():
        def __init__(self):
            self.total = 0
            self.current = ''
            self.input_value = True
            self.check_sum = False
            self.op = ''
            self.result = False

        def numberEnter(self, num):
            self.result = False
            firstnum = txtDisplay.get()
            secondnum = str(num)
            if self.input_value:
                self.current = secondnum
                self.input_value = False
            else:
                if secondnum == '.':
                    if secondnum in firstnum:
                        return
                self.current = firstnum+secondnum
            self.display(self.current)
    
        def sum_of_total(self):
            self.result = True
            self.current = float(self.current)
            if self.check_sum == True:
                self.valid_function()
            else:
                self.total = float(txtDisplay.get())
    
        def display(self, value):
            txtDisplay.delete(0, END)
            txtDisplay.insert(0, value)
    
        def valid_function(self):
            if self.op == "add":
                self.total += self.current
            if self.op == "sub":
                self.total -= self.current
            if self.op == "multi":
                self.total *= self.current
            if self.op == "divide":
                self.total /= self.current
            if self.op == "mod":
                self.total %= self.current
            self.input_value = True
            self.check_sum = False
            self.display(self.total)
    
        def operation(self, op):
            self.current = float(self.current)
            if self.check_sum:
                self.valid_function()
            elif not self.result:
                self.total = self.current
                self.input_value = True
            self.check_sum = True
            self.op = op
            self.result = False
    
        def Clear_Entry(self):
            self.result = False
            self.current = "0"
            self.display(0)
            self.input_value = True
    
        def All_Clear_Entry(self):
            self.Clear_Entry()
            self.total = 0
    
        def pi(self):
            self.result = False
            self.current = math.pi
            self.display(self.current)
    
        def tau(self):
            self.result = False
            self.current = math.tau
            self.display(self.current)
    
        def e(self):
            self.result = False
            self.current = math.e
            self.display(self.current)
    
        def mathPM(self):
            self.result = False
            self.current = -(float(txtDisplay.get()))
            self.display(self.current)
    
        def squared(self):
            self.result = False
            self.current = math.sqrt(float(txtDisplay.get()))
            self.display(self.current)
    
        def cos(self):
            self.result = False
            self.current = math.cos(math.radians(float(txtDisplay.get())))
            self.display(self.current)
    
        def cosh(self):
            self.result = False
            self.current = math.cosh(math.radians(float(txtDisplay.get())))
            self.display(self.current)
    
        def tan(self):
            self.result = False
            self.current = math.tan(math.radians(float(txtDisplay.get())))
            self.display(self.current)
    
        def tanh(self):
            self.result = False
            self.current = math.tanh(math.radians(float(txtDisplay.get())))
            self.display(self.current)
    
        def sin(self):
            self.result = False
            self.current = math.sin(math.radians(float(txtDisplay.get())))
            self.display(self.current)
    
        def sinh(self):
            self.result = False
            self.current = math.sinh(math.radians(float(txtDisplay.get())))
            self.display(self.current)
    
        def log(self):
            self.result = False
            self.current = math.log(float(txtDisplay.get()))
            self.display(self.current)
    
        def exp(self):
            self.result = False
            self.current = math.exp(float(txtDisplay.get()))
            self.display(self.current)
    
        def acosh(self):
            self.result = False
            self.current = math.acosh(float(txtDisplay.get()))
            self.display(self.current)
    
        def asinh(self):
            self.result = False
            self.current = math.asinh(float(txtDisplay.get()))
            self.display(self.current)
    
        def expm1(self):
            self.result = False
            self.current = math.expm1(float(txtDisplay.get()))
            self.display(self.current)
    
        def lgamma(self):
            self.result = False
            self.current = math.lgamma(float(txtDisplay.get()))
            self.display(self.current)
    
        def degrees(self):
            self.result = False
            self.current = math.degrees(float(txtDisplay.get()))
            self.display(self.current)
    
        def log2(self):
            self.result = False
            self.current = math.log2(float(txtDisplay.get()))
            self.display(self.current)
    
        def log10(self):
            self.result = False
            self.current = math.log10(float(txtDisplay.get()))
            self.display(self.current)
    
        def log1p(self):
            self.result = False
            self.current = math.log1p(float(txtDisplay.get()))
            self.display(self.current)
    
    
    added_value = Calc()


    txtDisplay = tk.Entry(calc,
                    font=('Helvetica', 19,
                            'bold'),
                    bg='black',
                    fg='#90FF00',
                    bd=34,
                    width=29,
                    justify=RIGHT)
    
    txtDisplay.grid(row=0,
                    column=0,
                    columnspan=4,
                    pady=1, padx=2)
    
    txtDisplay.insert(0, "0")

    numberpad = "789456123"
    
    i = 0
    
    btn = []
    
    for j in range(2, 5):
    
        for k in range(3):
            btn.append(tk.Button(calc,
                            width=5,
                            height=1,
                            bg='#00F6FF',
                            fg='black',
                            font=('Calibri', 30, 'bold'),
                            bd=4, text=numberpad[i]))
    
            btn[i].grid(row=j, column=k, pady=1)
    
            btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
            i += 1

    btnClear = tk.Button(calc, text=chr(67),
                    width=5, height=1,
                    bg='#90FF00',
                    font=('Calibri', 30, 'bold'),
                    bd=4,
                    command=added_value.Clear_Entry).grid(
        row=1, column=0, pady=1)
    
    btnAllClear = tk.Button(calc, text=chr(67)+chr(69),
                        width=5, height=1,
                        bg='#90FF00',
                        font=('Calibri', 30, 'bold'),
                        bd=4,
                        command=added_value.All_Clear_Entry).grid(
        row=1, column=1, pady=1)
    
    btnsq = tk.Button(calc, text="\u221A", width=5,
                height=1, bg='#90FF00',
                font=('Calibri', 30, 'bold'),
                bd=4, command=added_value.squared).grid(
        row=1, column=2, pady=1)
    
    btnAdd = tk.Button(calc, text="+", width=5,
                    height=1, bg='#90FF00',
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=lambda: added_value.operation("add")
                    ).grid(row=1, column=3, pady=1)
    
    btnSub = tk.Button(calc, text="-", width=5,
                    height=1, bg='#90FF00',
                    font=('Calibri', 30, 'bold'),
                    bd=4,
                    command=lambda: added_value.operation("sub")
                    ).grid(row=2, column=3, pady=1)
    
    btnMul = tk.Button(calc, text="x", width=5, height=1,
                    bg='#90FF00',
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=lambda: added_value.operation("multi")
                    ).grid(row=3, column=3, pady=1)

    btnDiv = tk.Button(calc, text="/", width=5,
                    height=1, bg='#90FF00',
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=lambda: added_value.operation("divide")
                    ).grid(row=4, column=3, pady=1)
    
    btnZero = tk.Button(calc, text="0", width=5,
                    height=1, bg='#00F6FF',
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=lambda: added_value.numberEnter(0)
                    ).grid(row=5, column=0, pady=1)
    
    btnDot = tk.Button(calc, text=".", width=5,
                    height=1, bg='#90FF00',
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=lambda: added_value.numberEnter(".")
                    ).grid(row=5, column=1, pady=1)
    btnPM = tk.Button(calc, text=chr(177), width=5,
                height=1, bg='#90FF00',
                font=('Calibri', 30, 'bold'),
                bd=4, command=added_value.mathPM
                ).grid(row=5, column=2, pady=1)
    
    btnEquals = tk.Button(calc, text="=", width=5,
                    height=1, bg='#90FF00',
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=added_value.sum_of_total
                    ).grid(row=5, column=3, pady=1)
    # ROW 1 :

    btnPi = tk.Button(calc, text="π", width=5,
                height=1, bg='#90FF00',
                font=('Calibri', 30, 'bold'),
                bd=4, command=added_value.pi
                ).grid(row=1, column=4, pady=1)
    
    btnCos = tk.Button(calc, text="cos", width=5,
                    height=1, bg='#90FF00',
                    font=('Monotype Corsiva', 30, 'bold'),
                    bd=4, command=added_value.cos
                    ).grid(row=1, column=5, pady=1)
    
    btntan = tk.Button(calc, text="tan", width=5,
                    height=1, bg='#90FF00', 
                    font=('Monotype Corsiva', 30, 'bold'),
                    bd=4, command=added_value.tan
                    ).grid(row=1, column=6, pady=1)
    
    btnsin = tk.Button(calc, text="sin", width=5,
                    height=1, bg='#90FF00', 
                    font=('Monotype Corsiva', 30, 'bold'),
                    bd=4, command=added_value.sin
                    ).grid(row=1, column=7, pady=1)
    
    # ROW 2 :
    
    btn2Pi = tk.Button(calc, text="2π", width=5,
                    height=1, bg='#90FF00', 
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=added_value.tau
                    ).grid(row=2, column=4, pady=1)
    
    btnCosh = tk.Button(calc, text="cos h", width=5,
                    height=1, bg='#90FF00', 
                    font=('Monotype Corsiva', 30, 'bold'),
                    bd=4, command=added_value.cosh
                    ).grid(row=2, column=5, pady=1)
    
    btntanh = tk.Button(calc, text="tan h", width=5,
                    height=1, bg='#90FF00', 
                    font=('Monotype Corsiva', 30, 'bold'),
                    bd=4, command=added_value.tanh
                    ).grid(row=2, column=6, pady=1)
    
    btnsinh = tk.Button(calc, text="sin h", width=5,
                    height=1, bg='#90FF00', 
                    font=('Monotype Corsiva', 30, 'bold'),
                    bd=4, command=added_value.sinh
                    ).grid(row=2, column=7, pady=1)
    
    # ROW 3 :
    
    btnlog = tk.Button(calc, text="log", width=5,
                    height=1, bg='#90FF00', 
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=added_value.log
                    ).grid(row=3, column=4, pady=1)
    
    btnExp = tk.Button(calc, text="exp", width=5,
                    height=1, bg='#90FF00', 
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=added_value.exp
                    ).grid(row=3, column=5, pady=1)
    
    btnMod = tk.Button(calc, text="%", width=5,
                    height=1, bg='#90FF00', 
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=lambda: added_value.operation("mod")
                    ).grid(row=3, column=6, pady=1)
    
    btnE = tk.Button(calc, text="e", width=5,
                height=1, bg='#90FF00', 
                font=('Calibri', 30, 'bold'),
                bd=4, command=added_value.e
                ).grid(row=3, column=7, pady=1)
    
    # ROW 4 :
    
    btnlog10 = tk.Button(calc, text="log\u2081\u2080", width=5,
                    height=1, bg='#90FF00', 
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=added_value.log10
                    ).grid(row=4, column=4, pady=1)
    
    btncos = tk.Button(calc, text="log\u2081\u209A", width=5,
                    height=1, bg='#90FF00', 
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=added_value.log1p
                    ).grid(row=4, column=5, pady=1)
    
    btnexpm1 = tk.Button(calc, text="e\u00b2-1", width=5,
                    height=1, bg='#90FF00', 
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=added_value.expm1
                    ).grid(row=4, column=6, pady=1)
    
    btngamma = tk.Button(calc, text="Gamma\nln((x-1)!)", width=8,
                    height=2, bg='#90FF00', 
                    font=('Calibri', 19, 'bold'),
                    bd=4, command=added_value.lgamma
                    ).grid(row=4, column=7)
    # ROW 5 :
    
    btnlog2 = tk.Button(calc, text="log\u2082", width=5,
                    height=1, bg='#90FF00', 
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=added_value.log2
                    ).grid(row=5, column=4, pady=1)
    
    btndeg = tk.Button(calc, text="\u00b0r→\u00b0d", width=6,
                    height=1, bg='#90FF00', 
                    font=('california fb', 21, 'bold'),
                    bd=4, command=added_value.degrees, pady=15
                    ).grid(row=5, column=5, pady=1)
    
    btnacosh = tk.Button(calc, text="a cos h", width=5,
                    height=1, bg='#90FF00', 
                    font=('Monotype Corsiva', 30, 'bold'),
                    bd=4, command=added_value.acosh
                    ).grid(row=5, column=6, pady=1)
    
    btnasinh = tk.Button(calc, text="a sin h", width=5,
                    height=1, bg='#90FF00', 
                    font=('Monotype Corsiva', 30, 'bold'),
                    bd=4, command=added_value.asinh
                    ).grid(row=5, column=7, pady=1)
    
    lblDisplay = tk.Label(calc, text="SCIENTIFIC CALCULATOR",
                    font=('Helvetica', 22,
                            'bold'),
                    bg='red',
                    fg='WHITE',
                    bd=15,
                    width=24,height=2, justify=CENTER, relief=RAISED)
    lblDisplay.grid(row=0, column=4, columnspan=4, padx = 2)

    def iExit(): 
        Calc_window.destroy()
    
    def Scientific():
        Calc_window.resizable(width=False, height=False)
        Calc_window.geometry("960x645+0+0")
        Calc_window.title("Scientific Calculator")
    
    def Standard():
        Calc_window.resizable(width=False, height=False)
        Calc_window.geometry("480x645+0+0")
        Calc_window.title("Standard Calculator")

    toggle_funcs = itertools.cycle((Scientific, Standard))

    def toggle():
        func = next(toggle_funcs)
        func()

    button_frame = tk.Frame(Calc_window, background='white')
    button_frame.pack()

    exit_button = tk.Button(button_frame,bg = 'orange', bd = 6, command = iExit)
    exit_button.grid (row = 0, column = 0, padx=7)
    image = Image.open("img/back_button.png")
    resize_image = image.resize((61,50), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(resize_image)
    exit_button.img_ref = img
    exit_button.config(image = img, justify=LEFT)

    normal_scientific = tk.Button(button_frame, text = "Normal ⇌ Scientific",  border = 6, fg = 'red',bg = 'yellow',font = ("Bookman Old Style", 20,"bold"), command = toggle)
    normal_scientific.grid(row = 0,column=1, columnspan=4, pady=4)

    # image = Image.open("img/unit converter.png")
    # resize_image = image.resize((62,49), Image.ANTIALIAS)
    # img = ImageTk.PhotoImage(resize_image)
    # normal_scientific.img_ref = img
    # normal_scientific.config(image = img, compound=LEFT)





mainmenu = tk.Menu(root)

#File Menu Start here.
def saveMenu():
    pass

def openMenu():
    pass

def historyMenu():
    pass

def exit_window(): 
    iExit = tmsg.askquestion("Converter", "Do you want to exit ?")
    root.wm_iconbitmap("img/unit converter.ico")
    if iExit=="yes":
        root.destroy()
fileMenu = tk.Menu(mainmenu, tearoff = 0)

fileMenu.add_command(label = "Save", state='disabled')
fileMenu.add_command(label = "Open", state='disabled')
fileMenu.add_separator()
fileMenu.add_command(label = "History", state='disabled')
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = exit_window)
root.config(menu = mainmenu)
mainmenu.add_cascade(menu = fileMenu, label = "File")



#viewMenu Starts Here.
def fullsize():
    root.state(newstate = 'zoomed')

def originalSize():
    root.state(newstate='normal')

def zoomIn():
    pass

def zoomOut():
    pass

def fullScreen():
    pass

def lowQuality():
    pass

def mediumQuality():
    pass

def highQuality():
    pass

viewMenu= tk.Menu(mainmenu, tearoff = 0)
viewMenu.add_command(label = "Original Size", command = originalSize)
viewMenu.add_separator()
viewMenu.add_command(label = "Zoom In", state='disabled')
viewMenu.add_command(label = "Zoom Out", state='disabled')
viewMenu.add_separator()
viewMenu.add_command(label = "Full Screen", command = fullsize)
viewMenu.add_separator()
#Adding SubMenu to viewMenu.
qualityMenu = tk.Menu(viewMenu, tearoff = 0)
qualityMenu.add_command(label = "Low", state='disabled')
qualityMenu.add_command(label = "Medium", state='disabled')
qualityMenu.add_command(label = "High", state='disabled')
viewMenu.add_cascade(menu = qualityMenu, label = "Quality")
#to here.
root.config(menu = mainmenu)
mainmenu.add_cascade(menu = viewMenu, label = "View")


#Control Menu Starts Here.
def windowSize():
    def release():
        new_width = int(width_entry.get())
        new_height = int(height_entry.get())
        root.geometry(f'{new_width}x{new_height}')
        window_pop.destroy()
    
    window_pop = tk.Toplevel(root)
    window_pop.wm_iconbitmap("img/unit converter.ico")
    window_pop.grab_set()
    window_pop.geometry("370x170")


    width_label = tk.Label(window_pop, text = "Enter the width of window (in pixels):", font = 'Helvetica 12')
    width_label.grid(row = 1, column=1, pady = 10)
    width_entry = tk.Entry(window_pop, width = 10,font = 'Helvetica 12')
    width_entry.grid(row = 1, column = 2, padx = 2)
    height_label = tk.Label(window_pop, text = "Enter the Height of window (in pixels):", font = 'Helvetica 12')
    height_label.grid(row = 2, column=1, pady = 10)
    height_entry = tk.Entry(window_pop, width = 10,font = 'Helvetica 12')
    height_entry.grid(row = 2, column = 2, padx = 2)
    
    tk.Label(window_pop, text = "\"Minimum Size of Window is 1000x750\"", fg="red", font = "Helvetica 12").grid(row = 3, column =1, columnspan=2)
    
    change_button = tk.Button(window_pop, text = 'Change', command = release, font = ("Georgia", 14, "bold"), bg = 'light gray')
    change_button.grid(row = 4, column = 1, columnspan=2)

    window_pop.mainloop()

def backgroundColor():
    pass

def download():
    pass

def find():
    pass

def replace():
    pass

controlMenu= tk.Menu(mainmenu, tearoff = 0)
controlMenu.add_command(label = "Window Size", command = windowSize)
controlMenu.add_command(label = "Background Color", state = 'disabled')
controlMenu.add_separator()
#Adding subMenu to control Menu from here.
downloadMenu = tk.Menu(controlMenu, tearoff =0)
downloadMenu.add_command(label = "Basic Converter")
downloadMenu.add_command(label = "Length Converter")
controlMenu.add_cascade(menu = downloadMenu, label = "Download Data", state = 'disabled')
#to here
controlMenu.add_separator()
controlMenu.add_command(label = "Find", state = 'disabled')
controlMenu.add_command(label = "Replace", state = 'disabled')
root.config(menu = mainmenu)
mainmenu.add_cascade(menu = controlMenu, label = "Contol")

def about_us():
    tmsg.showinfo("About!", "This converter is made, to fulfil the purpose of mini project in 2nd year B.Tech. Which is made in *Python* using tkinter module.")
def contact_us():
    tmsg.showinfo("Contact", "E-mail: danish.00@gmail.com\nMobile No: 2245248765\n\nIf you have any suggestions or facing any issue related to the app, feel free to contact us.\n\nThank you for choosing us.")
helpMenu = tk.Menu(mainmenu, tearoff = 0)
helpMenu.add_command(label = "About", command=about_us)
helpMenu.add_command(label = "Contact", command=contact_us)
root.config(menu = mainmenu)
mainmenu.add_cascade(menu = helpMenu, label="Help")


#Sub title bar**********************************
def shift():
    x1,y1,x2,y2 = sub_Title.bbox("marquee")
    if(x2<0 or y1<0): 
        x1 = sub_Title.winfo_width()
        y1 = sub_Title.winfo_height()//2
        sub_Title.coords("marquee",x1,y1)
    else:
        sub_Title.move("marquee", -2, 0)
    sub_Title.after(1000//fps,shift)

sub_Title = tk.Canvas(root,background='yellow',)
sub_Title.pack(side = BOTTOM, fill = X)     
text_var="Made by MD.DANISH , MD.REHAN, JITENDRA KUMAR (B.Tech IIIrd Year)"
text=sub_Title.create_text(0,-2000,text=text_var,fill = 'red',font=('Times New Roman',15,'bold'),tags=("marquee"),anchor='w')
x1,y1,x2,y2 = sub_Title.bbox("marquee")
width1 = x2-x1
height1 = y2-y1
sub_Title['width']=width1
sub_Title['height']=height1
fps=40
shift()

#Sub title bar ends here************************





#status bar...................
statusvar = tk.StringVar()
statusvar.set("Main Page")
sbar = tk.Label(root, textvariable = statusvar, relief = SUNKEN, anchor = "w")
sbar.pack(side = BOTTOM, fill = X)



screen = Screens()

root.mainloop()

#highlightthickness = 0