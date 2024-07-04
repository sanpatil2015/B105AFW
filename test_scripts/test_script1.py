from generic.base_class import BaseClass
from generic.utility import Excel
class Test_Case1(BaseClass):

    def test_script1(self):
        data= Excel.get_data(self.XLPATH,'tc1',2,3)
        print("Excel data",data)
        print(self.driver.title)