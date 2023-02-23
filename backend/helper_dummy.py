
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
    def __init__(self, colsNo, struct) -> None:
        self.parts = []
        self.colsNo = colsNo
        self.rowStruct = ""


        # """<tr id="regtable">
        #         <td id="regtable">
        #             <p><b>Abdominal tap</b></p>
        #         </td>
        #         <td id="regtable">
        #             <p style="text-align: center;">2</p>
        #         </td>
        #         <td id="regtable">
        #             <p style="text-align: center;">Indirect supervision</p>
        #         </td>
        #     </tr>"""


    def add(self, part: Any) -> None:
        if len(part) != self.colsNo:
            self.parts.append(part)

    def addCenterRow(self):
        self.rowStruct += """<td id="regtable">
                    <p style="text-align: center;">2</p>
                </td>"""
        
    def generateTable():
        procedureLogsRows = """"""
        page = """ <!-- Procedures Credentialing SECTION: -->

<p style="text-align: center; background-color: rgb(0, 0, 0); width:100%; font-family: Calibri, sans-serif; line-height: 1.5;"><span style="color: rgb(255, 255, 255); background-color: rgb(0, 0, 0); width:100%"><b>PROCEDURES CREDENTIALING</b></span></p>
<p><br></p>
<p>Examples: RISE Award, best HO/MO during a particular posting, best oral speaker</p>
<p><br></p>
<div align="left">
    <table style="margin-right: calc(6%); width: 94%; border-color: black; width: 100%;border-collapse: collapse;">
        <tbody id="regtable">
            <tr id="regtable">
                <td style="background-color: rgb(209, 213, 216); width: 50%" id="regtable">
                    <p style="text-align: center;"><b>Procedures</b></p>
                </td>
                <td style="background-color: rgb(209, 213, 216); width: 25%" id="regtable">
                    <p style="text-align: center;"><b>Number of Procedures Logged</b></p>
                </td>
                <td style="background-color: rgb(209, 213, 216);width: 25%" id="regtable">
                    <p style="text-align: center;"><b>Level of Supervision</b></p>
                </td>
            </tr>
            <tr id="regtable">
                <td id="regtable">
                    <p><b>Abdominal tap</b></p>
                </td>
                <td id="regtable">
                    <p style="text-align: center;">2</p>
                </td>
                <td id="regtable">
                    <p style="text-align: center;">Indirect supervision</p>
                </td>
            </tr>
            """ + procedureLogsRows + """
        </tbody>
    </table>
</div>
"""


