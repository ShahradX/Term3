from tkinter import *
from pytube import YouTube




#Display

root = Tk()

root.geometry('500x500')

root.resizable(0,0)

root.title("Youtube Downloader")

Label(root,text = 'Youtube Video Downloader', font ='Constantia 20 bold').pack()




#Link_field

link = StringVar()
Label(root, text = 'Video Link:', font = 'Constantia 15 bold').place(x= 190 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)



#Start_downloading

def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'Download Finished', font = 'Constantia 15', bg = "#178E11").place(x= 150 , y = 210)  
Button(root,text = 'Download', font = 'Constantia 15 bold' ,bg = "#101242", padx = 2, command = Downloader).place(x=180 ,y = 150)


#Second_Link_Field
link = StringVar()
Label(root, text= 'Second Video Link:', font = 'Constantia 15 bold').place(x = 150, y = 250)
Second_link_field = Entry(root, width = 70, textvariable= link).place(x = 32, y = 280)

#Start_Downloading

def second_Downloader() :
    second_url = YouTube(str(link.get()))
    second_video = second_url.streams.first()
    second_video.download()
    Label(root, text = ' Second Download Finished', font= 'Constantia 15', bg = "#0B6F06").place(x=115 , y= 400)
Button(root, text= 'Download', font = 'Constantia 15 bold', bg = "#101242", padx= 2, command= second_Downloader).place(x=180, y=340)


    
    


root.mainloop()