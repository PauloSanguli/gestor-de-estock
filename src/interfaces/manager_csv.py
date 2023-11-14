from abc import (ABC,abstractmethod)

class IManager(ABC):

    @abstractmethod
    def Read_csv():
        raise NotImplementedError("Implement the method Read")

    @abstractmethod
    def Write_csv():
        raise NotImplementedError("Implement the method Write")

    @abstractmethod
    def Delete_csv():
        raise NotImplementedError("Implment the method Delete")

    @abstractmethod
    def __Clean_csv_Path():
        raise NotImplementedError("Implement the method Clean")