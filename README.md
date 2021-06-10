# pingi
pingi is a command line tool which is able to measure continuously the ping reply time.

# How to use it

The user has the possibility to choose the ping destination address or ip <code>-d</code> and the ping interval <code>-i</code> in seconds. 
In following example, a ping is sent every 0.5 seconds to the host <code>www.srf.ch</code>.
```
> python pingi.py -d "www.srf.ch" -i 0.5
pingi: www.srf.ch , interval [s]: 0.5
..........   22:12:58 -> Success rate = 100.0  , Avg. ping reply [s] = 0.04225916862487793
..........   22:13:04 -> Success rate = 100.0  , Avg. ping reply [s] = 0.039688634872436526
..........   22:13:09 -> Success rate = 100.0  , Avg. ping reply [s] = 0.03984115918477376
...
```
Every 10th ping, an intermediate (trivial) statistic is shown.
