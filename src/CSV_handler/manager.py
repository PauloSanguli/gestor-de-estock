import csv
import os
from src.interfaces.manager_csv import IManager

class ManagerCSV(IManager):


    def Read_csv() -> list:
        file_path = f"{os.getcwd()}/src/CSV_handler/csv_filepath/works.csv"
        with open(file_path,mode="r") as file_handler:
            handler_csv = csv.reader(file_handler,delimiter=",")
            list_handlers_csv = []
            for line_table in handler_csv:
                list_handlers_csv.append(line_table)
            file_handler.close()

            return list_handlers_csv.copy()


    def Write_csv(name_work: str, id_work: str, date_work: str) -> None:
        file_path = f"{os.getcwd()}/src/CSV_handler/csv_filepath/works.csv"
        with open(file_path,mode="+a") as file_handler:
            file_handler.writelines(f"{name_work},{id_work},{date_work}"+"\n")
            file_handler.close()


    def Delete_csv(id_work: str) -> None:
        file_path = f"{os.getcwd()}/src/CSV_handler/csv_filepath/works.csv"
        handler_csv = ManagerCSV.Read_csv()
        ManagerCSV.__Clean_csv_Path()
        if len(handler_csv) != 0:
            for pos_csv,line_csv in enumerate(handler_csv):
                if line_csv[1] != id_work:
                    ManagerCSV.Write_csv(line_csv[0],line_csv[1],line_csv[2])

          
    def __Clean_csv_Path() -> None:
        file_path = f"{os.getcwd()}/src/CSV_handler/csv_filepath/works.csv"
        with open(file_path,mode="w") as file_handler:
            file_handler.close()
