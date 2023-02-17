
from abc import ABC, abstractmethod

    
class PageBuilder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @property
    @abstractmethod
    def product(self) -> None:
        pass



class ActualPageBuilder(PageBuilder):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    def product(self) -> None:
        pass

    @property
    def product(self) -> None:
        pass

class Row(ABC):
    
    @property
    @abstractmethod
    def type(self) -> None:
        pass

class BorderRowBold(ABC):
    
    @property
    @abstractmethod
    def type(self) -> None:
        pass



class Table():
    def __init__(self, colsNo) -> None:
        self.parts = []
        self.colsNo = colsNo


    def add(self, part: Any) -> None:
        if len(part) != self.colsNo:
            self.parts.append(part)
        
    def generateTable():
        projectRows = """"""
        page = """<div align="left">
    <table style="margin-right: calc(6%); width: 94%; border-color: black; width: 100%;border-collapse: collapse;">
        <tbody id="regtable">
            <tr id="regtable">
                <td style="background-color: rgb(209, 213, 216); width:50%" id="regtable">
                    <p style="text-align: center;">Details of Research</p>
                </td>
                <td style="background-color: rgb(209, 213, 216);" id="regtable">
                    <p style="text-align: center;">Start Date</p>
                </td>
                <td style="background-color: rgb(209, 213, 216);" id="regtable">
                    <p style="text-align: center;">End Date</p>
                </td>
                <td style="background-color: rgb(209, 213, 216);" id="regtable">
                    <p style="text-align: center;">Status (Completed/On-going)</p>
                </td>
            </tr>
            <tr id="regtable">
                <td id="regtable">
                    <p>Pemphigus and Pemphigoid comparison</p>
                </td>
                <td id="regtable" style="text-align:center">
                    <p>1 Jan 2015</p>
                </td>
                <td id="regtable" style="text-align:center">
                    <p>31 Apr 2016</p>
                </td>
                <td id="regtable" style="text-align:center">
                    <p>Completed</p>
                </td>
            </tr>
            """+ projectRows + """
            
        </tbody>
    </table>
</div>"""


