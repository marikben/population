from tkinter import * 

filename = "countries.txt"
countries = []
root = Tk()
root.geometry("300x300+0+0")
root.resizable(0,0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
f1 = Frame(root, bg="blue")
f2 = Frame(root, bg="red")
f3 = Frame(root, bg="green")
f4 = Frame(root, bg="yellow")

try:
    with open(filename) as file_object:
            for line in file_object:
                line = line.strip()
                countries.append(line)
except Exception as exc:
    print("An error occurred while opening the file: ", exc)        
            
for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, columnspan=2, sticky='news')
       
def findCountry(event):
    updatelist = []
    file1 = open(filename, 'r')
    for line in file1:
            line = line.strip()
            updatelist.append(line)
    countries = updatelist
    find = fcountry.get()
    index = 0
    poptxt = ""
    for line in countries:
        index +=1
        if line.lower() == find.lower():
            poptxt = "The population of "+line+" is: "+countries[index]
            break
        else:
            poptxt = find+" could not be found,\n please check your entry"
    populabel["text"] = poptxt

def addCountry(event):
    name = a1.get()
    try:
        amount = int(a2.get())
        errormsg["text"] = "Success!"
    except ValueError:
        errormsg["text"] = "Population must me a number"
    except:
        errormsg["text"] = "Something went wrong"
    new = "\n "+name+"\n "+str(amount)
    file1 = open(filename, 'a')
    file1.write(new)
    
heading = Label(f1, text="Please pick an action from above")
heading.pack(side=TOP)
fcountry = Entry(f4, bg="white")
fcountry.pack()
searchbtn = Button(f4, text="Search")
searchbtn.bind("<Button-1>", findCountry)
searchbtn.pack()
populabel = Label(f4, text="")
populabel.pack()
q1 = Label(f3, text="Country: ")
q1.grid(row=1, column=0)
a1 = Entry(f3)
a1.grid(row=1, column=1, columnspan=2)
q2 = Label(f3, text="Population: ")
q2.grid(row=2, column=0)
a2 = Entry(f3)
a2.grid(row=2, column=1, columnspan=2)
btn = Button(f3, text="Add")
btn.grid(row=3, column=1)
btn.bind("<Button-1>", addCountry)
errormsg = Label(f3, text="")
errormsg.grid(row=4, column=1)
def allCountries():
    updatelist = []
    file1 = open(filename, 'r')
    for line in file1:
            line = line.strip()
            updatelist.append(line)
    countries = updatelist
    l1 = Label(f2, text="Country")
    l1.grid(row=0,column=1)
    listbox1 = Listbox(f2)
    listbox1.grid(row=1,column=1, padx=(10))
    scrollbar1 = Scrollbar(f2)
    scrollbar1.grid(row=1, column=1,sticky=N+S+E)
    listbox1.config(yscrollcommand = scrollbar1.set)
    scrollbar1.config(command = listbox1.yview)
    l2 = Label(f2, text="Population")
    l2.grid(row=0,column=2, sticky='')
    listbox2 = Listbox(f2)
    listbox2.grid(row=1,column=2, padx=(10))
    scrollbar2 = Scrollbar(f2)
    scrollbar2.grid(row=1, column=2,sticky=N+S+E)
    listbox2.config(yscrollcommand = scrollbar2.set)
    scrollbar2.config(command = listbox2.yview)
    biggest = Label(f2, text="")
    biggest.grid(row=2, column=0, columnspan=3)
    f2.tkraise()
    index = 0
    big = int(countries[1])
    for i in range(len(countries)):
        item = countries[i]
        if i%2 == 0 or i==0:
            listbox1.insert(i, item)
        else:
            listbox2.insert(i, item)
            
    for x in range(len(countries)):
        if x%2!=0:
            if int(countries[x])>big:
                big = int(countries[x])
                index = x-1
        biggest["text"] = "The country with the biggest population is\n"+countries[index]+": "+str(big)

def newCountry():
    
    f3.tkraise()
    

menu = Menu(root)
menu.add_command(label="Home", command=lambda: f1.tkraise())
menu.add_command(label="All countries", command=allCountries)
menu.add_command(label="Add a new country", command=newCountry)
menu.add_command(label="Search", command=lambda: f4.tkraise())
root.config(menu=menu)

f1.tkraise()
root.mainloop()
