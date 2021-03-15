
from json import load

'''frequency=daily|monthly|yearly'''
def query(frequency,date,country):
    with open(f"data/{frequency}_json.json") as file:
        json=load(file)
        by_country=[ entry for entry in json if entry['Country']==country]
        if len(by_country)==0:
            return "wrong Country"
        
        date=[ entry for entry in by_country if entry['Date']==date  ]
        if len(date)==0:
            return "wrong Date"

        return date.pop()['Value']



''' Testing Code '''
from unittest import TestCase, main
class Test(TestCase):
    def test(self):    
        ''' Testing for future/illegals date '''    
        self.assertNotEqual(query("daily","2084-01-30","India"),"wrong date","Accepting Illegal Date")
        self.assertNotEqual(query("daily","2004-02-30","India"),"wrong date","Accepting Illegal Date")
        
        ''' Testing for Output '''
        self.assertEqual(query("daily","2002-01-01","India"),None,"Returning wrong value")
        self.assertNotEqual(query("daily","2002-01-07","india"),"45.8","Accepting Wrong Country")
        


Test().main()
