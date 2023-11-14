from src.CSV_handler.manager import ManagerCSV
from tkinter import END, Button,Entry

class EventsBTN():
    
    def Event_add(self) -> None:
        customer_name = self.entry_name_work.get()
        customer_id = self.entry_cod_work.get()
        customer_date = self.entry_date_work.get()

        if customer_name.strip() != "" and customer_id.strip() != "" and customer_date.strip() != "":

            ManagerCSV.Write_csv(
                name_work=customer_name,
                id_work=customer_id,
                date_work=customer_date
            )

    def Event_Del(self) -> None:
        customer_id = self.entry_cod_work_del.get()

        ManagerCSV.Delete_csv(
            id_work=customer_id
        )

    def Event_Refr(self) -> None:
        return ManagerCSV.Read_csv()

    def Event_Clean_add(self) -> None:
        self.entry_name_work.delete(0,END)
        self.entry_cod_work.delete(0,END)
        self.entry_date_work.delete(0,END)

    def Event_Clean_del(self) -> None:
        self.entry_cod_work_del.delete(0,END)