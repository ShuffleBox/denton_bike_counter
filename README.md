# Bike and Pedestrian counter data

## About
The City of Denton has two permanent bike and pedestrian usage counters installed
on the Denton Branch Rail Trail (Denton Katy Trail).  These counters are produced
by Eco-Counter and were installed July 23, 2014. Link: [Eco-Counter Multi-Nature Counter](https://www.eco-compteur.com/en/products/multi-range/multi-nature)

These counters detect traffic using directed PIR motion sensors and inductive loop
sensors.  Pedestrians will trigger motion detection in with the PIR sensor while a
bicycle will trigger both the PIR and inductive loop.  The counts from these are
reported back to "the cloud" (Eco-Counter) where they can be evaluated with
Eco-Counter generated analytics or the data exported for external analysis.

### Also
The City has also deployed temporary "tube" counters to evaluate bike lane usage in
recent changes like the Eagle St. lane reconfiguration (road diet.)  These are
the counters that look like rubber hoses laid across the road.  Except in this
instance, it's just the bike lane width. Link: [Eco-Counter Tube Counter](https://www.eco-compteur.com/en/products/tubes-range)

This type of data gathering is usually over a short time span in order to evaluate
a specific occurrence or event.

## About the data

Data provided was exported in CSV format and does include descriptive headers.

>Date,Hour,Pedestrians,Cyclist  
13/08/2014,0:00,27,86   
14/08/2014,0:00,42,132  
15/08/2014,0:00,49,89  
16/08/2014,0:00,49,91  
17/08/2014,0:00,36,61  

## Could do's
* Compare data year to year.  Hopefully we'd see an increase in utilization.
    * Visualizations
* Relate to weather.  I'd expect to see an increase when the weather has been
nice is that true?
* Build workflow to make this data more accessible (automation)
    * A task runner to export from Eco-Counter and import on the OpenData Portal?
