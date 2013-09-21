import urllib2

import scipy

import numpy

import datetime

class Date(object):
    def __init__(self,year,month,day):
        self.Month=month;
        self.Year=year;
        self.Day =day;


class CurveData(object):
    def __init__(self, stock_tag):
        today = datetime.date.today()

        startDate = Date(today.year-5,today.month,today.day)
        endDate   = Date(today.year,today.month,today.day)

        adress       = 'http://ichart.finance.yahoo.com/table.csv?s=' + stock_tag + '&a=' + str(startDate.Month - 1) + '&b=' + str(startDate.Day) + '&c=' + str(startDate.Year) + '&d=' + str(endDate.Month - 1) + '&e=' + str(endDate.Day) + '&f=' + str(endDate.Year) + '&g=d'+'&ignore=.csv'
        response     = urllib2.urlopen(adress)
        html         = response.read()
        self.curve   = [float(line.split(',')[1]) for line in html.split('\n')[1:-1]]
        self.date    = [line.split(',')[0] for line in html.split('\n')[1:-1]]
        self.curve   = self.curve[::-1]
        self.date    = self.date[::-1]



        ws =20;

        self.curve   = movingaverage(self.curve,ws)[ws:-ws]

        min_c = min(self.curve)
        max_c = max(self.curve)

        self.curve = (self.curve - min_c)/(max_c-min_c)*1000.0

        self.date    = self.date[ws:-ws]
        self.curve_p = numpy.gradient(self.curve)

    def __len__(self):
        return len(self.curve_p)

    def range(self, from_x, to_x):
        #from_x =max (0,from_x)
        #to_x= min (to_x,len(self.curve))
        return self.curve[from_x:to_x]

    def range_p(self, from_x, to_x):
        #from_x =max (0,from_x)
        #to_x= min (to_x,len(self.curve_p))
        return self.curve_p[from_x:to_x]


    def value_at_x(self, x):
        x=max(x,0)
        x=min(x,len(self.curve)-1)
        int_x  = int(x)
        int_x1 = int_x+1
        val    = x-int_x

        return self.curve[int_x]*(1-val)+self.curve[int_x1]*(val)

    def value_p_at_x(self,x):
        x=max(x,0)
        x=min(x,len(self.curve_p)-1)
        int_x  = int(x)
        int_x1 = int_x+1
        val    = x-int_x

        return self.curve_p[int_x]*(1-val)+self.curve_p[int_x1]*(val)


def movingaverage(data, window_size):
    window= numpy.ones(int(window_size))/float(window_size)
    return numpy.convolve(data, window, 'same')

    
cd = CurveData("VOLV-B.ST")

plot(cd.curve)
show()
