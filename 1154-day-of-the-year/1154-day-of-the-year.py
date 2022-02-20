class Solution:
    def dayOfYear(self, date: str) -> int:
        if int(date[0:4]) in [1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]:
            if int(date[5:7])==1:
                return int(date[8:10])
            if int(date[5:7])==2:
                return (31+int(date[8:10]))
            if int(date[5:7])==3:
                return (31+29+int(date[8:10]))
            if int(date[5:7])==4:
                return (31+29+31+int(date[8:10]))
            if int(date[5:7])==5:
                return (31+29+31+30+int(date[8:10]))
            if int(date[5:7])==6:
                return (31+29+31+30+31+int(date[8:10]))
            if int(date[5:7])==7:
                return (31+29+31+30+31+30+int(date[8:10]))
            if int(date[5:7])==8:
                return (31+29+31+30+31+30+31+int(date[8:10]))
            if int(date[5:7])==9:
                return (31+29+31+30+31+30+31+31+int(date[8:10]))
            if int(date[5:7])==10:
                return (31+29+31+30+31+30+31+31+30+int(date[8:10]))
            if int(date[5:7])==11:
                return (31+29+31+30+31+30+31+31+30+31+int(date[8:10]))
            if int(date[5:7])==12:
                return (31+29+31+30+31+30+31+31+30+31+30+int(date[8:10]))
            
            
        else:
            if int(date[5:7])==1:
                return int(date[8:10])
            if int(date[5:7])==2:
                return (31+int(date[8:10]))
            if int(date[5:7])==3:
                return (31+28+int(date[8:10]))
            if int(date[5:7])==4:
                return (31+28+31+int(date[8:10]))
            if int(date[5:7])==5:
                return (31+28+31+30+int(date[8:10]))
            if int(date[5:7])==6:
                return (31+28+31+30+31+int(date[8:10]))
            if int(date[5:7])==7:
                return (31+28+31+30+31+30+int(date[8:10]))
            if int(date[5:7])==8:
                return (31+28+31+30+31+30+31+int(date[8:10]))
            if int(date[5:7])==9:
                return (31+28+31+30+31+30+31+31+int(date[8:10]))
            if int(date[5:7])==10:
                return (31+28+31+30+31+30+31+31+30+int(date[8:10]))
            if int(date[5:7])==11:
                return (31+28+31+30+31+30+31+31+30+31+int(date[8:10]))
            if int(date[5:7])==12:
                return (31+28+31+30+31+30+31+31+30+31+30+int(date[8:10]))
            

            
            
                
            
            
        