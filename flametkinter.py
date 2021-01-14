# import all functions from the tkinter 
from tkinter import *
import time
import os
from tkinter import messagebox as mb

# function for removing common characters 
# with their respective occurrences 
def remove_match_char(list1, list2): 

	for i in range(len(list1)) : 
		for j in range(len(list2)) : 

			# if common character is found 
			# then remove that character 
			# and return list of concatenated 
			# list with Ture Flag 
			if list1[i] == list2[j] : 
				c = list1[i] 

				# remove character from the list 
				list1.remove(c) 
				list2.remove(c) 

				# concatenation of two list elements with * 
				# * is act as border mark here 
				list3 = list1 + ["*"] + list2 

				# return the concatenated list with True flag 
				return [list3, True] 

	# no common characters is found 
	# return the concatenated list with False flag 
	list3 = list1 + ["*"] + list2 
	return [list3, False] 


# function for telling the relationship status 
def tell_status() : 
	
	# take a 1st player name from Player1_field entry box 
	p1 = Player1_field.get() 

	# converted all letters into lower case 
	p1 = p1.lower() 

	# replace any space with empty string 
	p1.replace(" ", "") 

	# make a list of letters or characters 
	p1_list = list(p1) 

	# take a 2nd player name from Player2_field entry box 
	p2 = Player2_field.get() 
	p2 = p2.lower() 
	p2.replace(" ", "") 
	p2_list = list(p2) 

	# taking a flag as True initially 
	proceed = True
	
	# keep calling remove_match_char function 
	# untill common characters is found or 
	# keep looping untill proceed flag is True 
	while proceed : 

		# function calling and store return value 
		ret_list = remove_match_char(p1_list, p2_list) 

		# take out concatenated list from return list 
		con_list = ret_list[0] 

		# take out flag value from return list 
		proceed = ret_list[1] 

		# find the index of "*" / border mark 
		star_index = con_list.index("*") 

		# list slicing perform 
		
		# all characters before * store in p1_list 
		p1_list = con_list[ : star_index] 

		# all characters after * store in p2_list 
		p2_list = con_list[star_index + 1 : ] 


	# count total remaining characters 
	count = len(p1_list) + len(p2_list) 

	# list of FLAMES acronym 
	result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"] 

	# keep looping untill only one item 
	# is not remaining in the result list 
	while len(result) > 1 : 

		# store that index value from 
		# where we have to perform slicing. 
		split_index = (count % len(result) - 1) 

		# this steps is done for performing 
		# anticlock-wise circular fashion counting. 
		if split_index >= 0 : 

			# list slicing 
			right = result[split_index + 1 : ] 
			left = result[ : split_index] 

			# list concatenation 
			result = right + left 

		else : 
			result = result[ : len(result) - 1] 

	# insert method inserting the 
		# value in the text entry box. 
	Status_field.insert(10, result[0]) 


# Function for clearing the 
# contents of all text entry boxes 
def clear_all() : 
	Player1_field.delete(0, END) 
	Player2_field.delete(0, END) 
	Status_field.delete(0, END) 
	
	# set focus on the Player1_field entry box 
	Player1_field.focus_set() 



	
# Create a GUI window 
rt = Tk()
 

# Set the configuration of GUI window 
rt.geometry("1600x800+0+0") 

# set the name of tkinter GUI window 
rt.title("Flames Game") 
########################################################################################################################
Tops=Frame(rt,width = 1600,height = 50,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(rt,width = 550,height = 700,relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(rt,width = 300,height = 700,relief=SUNKEN)
f2.pack(side=RIGHT)
########################################################################################################################
lblInfo=Label(Tops,font=("arial",30,"bold"),text="WELCOME TO FLAMES",fg="Steel Blue",bd=10,anchor="w")
lblInfo.pack()

localtime=time.asctime(time.localtime(time.time()))#DATE TIME FUNCTION

lblDateTime=Label(Tops,font=("arial",20,"bold"),text=localtime,fg="Steel Blue",bd=10,anchor="w")
lblDateTime.pack()

lblInfo=Label(Tops,font=("arial",23,"bold"),text=" ",fg="Steel Blue",bd=10,anchor="w")
lblInfo.pack()

lblInfo=Label(Tops,font=("arial",23,"bold"),text="PRESS START BUTTON TO START THE GAME ",fg="Steel Blue",bd=10,anchor="w")
lblInfo.pack()
#########################################################################################################################
def start():
        global root
        root=Toplevel(rt)
        root.geometry("1600x800+0+0")
        root.title("FLAMES")
        
        global label1
        global label2
        global label3
        global label4
        global label5
        global label6
        global label7
        global label8
        global Player1_field
        global Player2_field
        global Status_field
        Tops1=Frame(root,width = 1600,height = 50,relief=SUNKEN)
        Tops1.pack(side=TOP)

        f11=Frame(root,width = 550,height = 700,relief=SUNKEN)
        f11.pack(side=LEFT)

        f21=Frame(root,width = 300,height = 700,relief=SUNKEN)
        f21.pack(side=RIGHT)

        # Create a Player 1 Name: label 
        label1 = Label(Tops1, font=('arial',30,'bold'), text = "Player 1 Name", fg = 'black',bg="powder Blue") 

        # Create a Player 2 Name: label 
        label2 = Label(Tops1, font=('arial',30,'bold'), text = "Player 2 Name", fg = 'black',bg="powder Blue") 
                

        # Create a Relation Status: label 
        label3 = Label(Tops1, font=('arial',30,'bold'), text = "Relationship Status", fg = 'black',bg="powder Blue")
        label4 = Label(Tops1, font=('arial',30,'bold'), text = " ")
        label5 = Label(Tops1, font=('arial',30,'bold'), text = " ")
        label6 = Label(Tops1, font=('arial',30,'bold'), text = " ")
        label7 = Label(Tops1, font=('arial',30,'bold'), text = " ")
        label8 = Label(Tops1, font=('arial',30,'bold'), text = " ") 





        # grid method is used for placing 
        # the widgets at respective positions 
        # in table like structure . 
        

        # Create a text entry box 
        # for filling or typing the information. 
        Player1_field = Entry(Tops1, font=('arial',30,'bold')) 
        Player2_field = Entry(Tops1, font=('arial',30,'bold')) 
        Status_field  = Entry(Tops1, font=('arial',30,'bold')) 

        # grid method is used for placing 
        # the widgets at respective positions 
        # in table like structure . 
        # ipadx keyword argument set width of entry space .
        label8.pack()
        label1.pack()
        Player1_field.pack()

        label6.pack()

        label2.pack()
        Player2_field.pack() 

        

        # Create a Submit Button and attached 
        # to tell_status function 
        button1 = Button(Tops1,font=('arial',20),bg='powder blue',fg='black', text = "Submit",command = tell_status) 

        # Create a Clear Button and attached 
        # to clear_all function 
        button2 = Button(Tops1,font=('arial',20),bg='powder blue',fg='black', text = "Clear", command = clear_all) 

        # grid method is used for placing 
        # the widgets at respective positions 
        # in table like structure
        label4.pack()
        button1.pack()

        label5.pack()

        label3.pack() 
        Status_field.pack()

        label7.pack()
        
        button2.pack() 

        # Start the GUI 
        root.mainloop() 


#########################################################################################################################
lblInfo=Label(Tops,font=("arial",23,"bold"),text=" ",fg="Steel Blue",bd=10,anchor="w")
lblInfo.pack()

btn15=Button(rt,padx=16,pady=16,bd=8,fg="black",font=("arial",18,"bold"),text="START",bg="powder blue",
                    command=start,anchor="w",width=10,height=0,compound="c")
btn15.place(x=220,y=420)
def call(): 
	res = mb.askquestion('Exit Application', 'Do you really want to exit') 
	
	if res == 'yes' : 
		rt.destroy() 
		
	else : 
		mb.showinfo('Return', 'Returning to main application') 



btn16=Button(rt,padx=16,pady=16,bd=8,fg="black",font=("arial",18,"bold"),text="Quit",bg="powder blue",
                    command=call,anchor="w",width=10,height=0,compound="c")
btn16.place(x=620,y=420)

rt.mainloop()
