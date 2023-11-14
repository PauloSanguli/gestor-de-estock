from tkinter import (Button, Entry, Frame, Label, Tk)
from tkinter import PhotoImage
from tkinter import ttk
from tkinter import END
from pallete import Colors
from src.view.utils.treeview import IoTreeview
from src.view.utils.events import EventsBTN


class Root():
    def __init__(self):
        self.root = Tk()
        self.color = Colors()
        self.__Root_propertyes()
        self.__Root_photoimages()
        self.__Root_widgets()
        self.__REFR()
        self.__Root_binds()
        self.__Root_places()
        self.__Root_ADD()
        self.__Root_ADD_binds()
        self.__Root_DEL()
        self.__Root_DEL_binds()


    def __Root_propertyes(self) -> None:
        self.root.title("To do pyhon")
        self.root.geometry("400x600+200+100")
        self.root.resizable(False,False)
        self.root.configure(background=self.color.primary_color)


    def __Root_photoimages(self) -> None:
        self.image_logo = PhotoImage(file="src/view/img/logo2.png")
        self.radius_name = PhotoImage(file="src/view/img/radius-1.png")
        self.radius_button = PhotoImage(file="src/view/img/radius-2.png")
        self.radius_buttonSmall = PhotoImage(file="src/view/img/radius-3.png")
        self.radius_buttonSmallest = PhotoImage(file="src/view/img/radius-4.png")


    def __Root_widgets(self) -> None:
        self.main_header = Frame(self.root,background=self.color.secondary_color)
        self.footer_header = Frame(self.root,background=self.color.primary_color)
        self.logo_header = Label(self.main_header,image=self.image_logo,bg=self.color.secondary_color)

        self.label_buttonSee_footer = Label(self.footer_header,image=self.radius_buttonSmallest,bg=self.color.primary_color)
        self.button_see = Button(self.label_buttonSee_footer,text="Se",bg=self.color.third_color,font=("4"),bd=0)
        self.label_buttonAdd_footer = Label(self.footer_header,image=self.radius_buttonSmallest,bg=self.color.primary_color)
        self.button_add = Button(self.label_buttonAdd_footer,text="Add",bg=self.color.third_color,font=("4"),bd=0)
        self.label_buttonDel_footer = Label(self.footer_header,image=self.radius_buttonSmallest,bg=self.color.primary_color)
        self.button_del = Button(self.label_buttonDel_footer,text="Del",bg=self.color.third_color,font=("4"),bd=0)
        self.label_buttonRefr_footer = Label(self.footer_header,image=self.radius_buttonSmallest,bg=self.color.primary_color)
        self.button_refr = Button(self.label_buttonRefr_footer,text="Refresh",bg=self.color.third_color,font=("4"),bd=0)

        self = IoTreeview(self)


    def __Root_places(self) -> None:
        self.main_header.place(relwidth=1.0,relheight=0.2)
        self.footer_header.place(relwidth=1.0,relheight=0.14,rely=0.86)
        self.logo_header.place(relx=0.34,rely=0.15)
        self.button_see.place(relheight=0.8,relwidth=0.8,relx=0.1,rely=0.1)
        self.button_add.place(relheight=0.8,relwidth=0.8,relx=0.1,rely=0.1)
        self.button_del.place(relheight=0.8,relwidth=0.8,relx=0.1,rely=0.1)
        self.button_refr.place(relheight=0.8,relwidth=0.8,relx=0.1,rely=0.1)

        self.main_treeview.place(rely=0.2,relheight=0.66,relwidth=1.0)
        self.scrollY_treview.pack(expand=True)
        self.scrollY_treview.place(relheight=1.0,relwidth=0.05,relx=0.95)

        self.label_buttonSee_footer.place(relx=0.05,rely=0.25)
        self.label_buttonAdd_footer.place(relx=0.28,rely=0.25)
        self.label_buttonDel_footer.place(relx=0.51,rely=0.25)
        self.label_buttonRefr_footer.place(relx=0.74,rely=0.25)

    def __Root_ADD(self) -> None:
        self.frame_add = Frame(self.root,bg=self.color.third_color)

        self.label_border = Label(self.frame_add,image=self.radius_name,bg=self.color.third_color)
        self.label_border.place(rely=0.20,relx=0.1)
        self.entry_name_work = Entry(self.label_border,bd=0,relief="solid",bg=self.color.third_color)
        self.entry_name_work.place(relheight=0.8,relwidth=0.8,rely=0.1,relx=0.1)
        self.label_entry_name = Label(self.frame_add,text="Name  work",background=self.color.third_color)
        self.label_entry_name.place(relheight=0.07,relx=0.1,rely=0.10)

        self.label_radius_entryCod = Label(self.frame_add,image=self.radius_buttonSmall,bg=self.color.third_color)
        self.label_radius_entryCod.place(relx=0.1,rely=0.44)
        self.entry_cod_work = Entry(self.label_radius_entryCod,bd=0,relief="solid",bg=self.color.third_color)
        self.entry_cod_work.place(relheight=0.8,relwidth=0.8,rely=0.1,relx=0.1)
        self.label_entry_cod = Label(self.frame_add,text="Cod work",background=self.color.third_color)
        self.label_entry_cod.place(relheight=0.07,relx=0.1,rely=0.34)

        self.label_radius_entryDate = Label(self.frame_add,image=self.radius_buttonSmall,bg=self.color.third_color)
        self.label_radius_entryDate.place(relx=0.5,rely=0.44)
        self.entry_date_work = Entry(self.label_radius_entryDate,bd=0,relief="solid",bg=self.color.third_color)
        self.entry_date_work.place(relheight=0.8,relwidth=0.8,rely=0.1,relx=0.1)
        self.label_entry_date = Label(self.frame_add,text="Date work",background=self.color.third_color)
        self.label_entry_date.place(relheight=0.07,relx=0.55,rely=0.34)

        self.label_radius_buttonInsert = Label(self.frame_add,image=self.radius_button,bg=self.color.third_color)
        self.label_radius_buttonInsert.place(relx=0.1,rely=0.62)
        self.button_insert_work = Button(self.label_radius_buttonInsert,text="Insert",bg=self.color.secondary_color,fg=self.color.third_color,bd=0)
        self.button_insert_work.place(relheight=0.8,relwidth=0.8,rely=0.1,relx=0.1)

        self.label_radius_buttonDelete = Label(self.frame_add,image=self.radius_button,bg=self.color.third_color)
        self.label_radius_buttonDelete.place(relx=0.1,rely=0.78)
        self.button_delete_entry = Button(self.label_radius_buttonDelete,text="Delete camps",bg=self.color.secondary_color,fg=self.color.third_color,bd=0)
        self.button_delete_entry.place(relheight=0.8,relwidth=0.8,rely=0.1,relx=0.1)



    def __Root_DEL(self) -> None:
        self.frame_del = Frame(self.root,bg=self.color.third_color)

        self.label_radius_EntryCodDel = Label(self.frame_del,image=self.radius_name,bg=self.color.third_color)
        self.label_radius_EntryCodDel.place(rely=0.30,relx=0.1)
        self.entry_cod_work_del = Entry(self.label_radius_EntryCodDel,bd=0,relief="solid",bg=self.color.third_color)
        self.entry_cod_work_del.place(relheight=0.8,relwidth=0.8,rely=0.1,relx=0.1)
        self.label_entry_cod_del = Label(self.frame_del,text="Cod work",background=self.color.third_color)
        self.label_entry_cod_del.place(relx=0.1,relheight=0.05,rely=0.24)

        self.label_radius_buttonDeleteDO = Label(self.frame_del,image=self.radius_button,bg=self.color.third_color)
        self.label_radius_buttonDeleteDO.place(rely=0.5,relx=0.1)
        self.button_del_work = Button(self.label_radius_buttonDeleteDO,text="Delete To do",bg=self.color.secondary_color,fg=self.color.third_color,bd=0)
        self.button_del_work.place(relheight=0.8,relwidth=0.8,rely=0.1,relx=0.1)

        self.label_radius_buttonDeleteDE = Label(self.frame_del,image=self.radius_button,bg=self.color.third_color)
        self.label_radius_buttonDeleteDE.place(rely=0.7,relx=0.1)
        self.button_delete_entry_del = Button(self.label_radius_buttonDeleteDE,text="Delete camps",bg=self.color.secondary_color,fg=self.color.third_color,bd=0)
        self.button_delete_entry_del.place(relheight=0.8,relwidth=0.8,rely=0.1,relx=0.1)


    def __REFR(self) -> None:
        try:
            self = IoTreeview(self)
            self.__Root_places()
            self.handler_csv = EventsBTN.Event_Refr(self)
            for self.line_csv in self.handler_csv:
                self.main_treeview.insert("",END,values=(self.line_csv[0],self.line_csv[2]))
        except IndexError:
            print("Nenhuma tarefa cadastrada!")


    def __Root_binds(self) -> None:
        self.button_add.bind("<1>",lambda e: self.__Root_display(button_add=[0,0.2,0.66,1.0]))
        self.button_del.bind("<1>",lambda e: self.__Root_display(button_del=[0,0.2,0.66,1.0]))
        self.button_refr.bind("<1>",lambda e: self.__REFR())
        self.button_see.bind("<1>",lambda e: self.__Root_display(button_see=[0,0.2,0.66,1.0,True]))

    def __Root_ADD_binds(self) -> None:

        self.button_insert_work.bind('<1>',lambda e: 
            EventsBTN.Event_add(self)
        )

        self.button_delete_entry.bind('<1>',lambda e: EventsBTN.Event_Clean_add(self))

    def __Root_DEL_binds(self) -> None:
        self.button_del_work.bind('<1>',lambda e:
            EventsBTN.Event_Del(self)
        )

        self.button_delete_entry_del.bind('<1>',lambda e: EventsBTN.Event_Clean_del(self))

    def __Root_display(self,button_add = [0,0,0,0], button_see = [0,0,0,0], button_del = [0,0,0,0]) -> None:
        self.frame_add.place(relx=button_add[0],rely=button_add[1],relheight=button_add[2],relwidth=button_add[3])
        self.frame_del.place(relx=button_del[0],rely=button_del[1],relheight=button_del[2],relwidth=button_del[3])
        self.main_treeview.place(relx=button_see[0],rely=button_see[1],relheight=button_see[2],relwidth=button_see[3])
        