from tkinter import ttk
from tkinter.ttk import Treeview


def IoTreeview(self) -> any:

    self.main_treeview = ttk.Treeview(self.root,columns=("col0,col1","col2"))
    self.main_treeview.heading("#0",text="")        
    self.main_treeview.column("#0",width="0")        
    self.main_treeview.heading("#1",text="Work name")        
    self.main_treeview.column("#1",width="200")        
    self.main_treeview.heading("#2",text="Date")
    self.main_treeview.column("#2",width="200")
    self.scrollY_treview = ttk.Scrollbar(self.main_treeview,orient="vertical")
    self.main_treeview.configure(yscroll=self.scrollY_treview.set)

    return self