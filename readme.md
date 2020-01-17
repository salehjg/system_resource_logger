A simple python2 script to log system resources over time using python-psutil!

# Installation
For CentOS 7.6:
```
sudo yum install python-matplotlib.x86_64
sudo pip2 install numpy psutil xlwt tqdm
```

# Usage
To start logging:
```
python2 log.py
```
  
To plot the logged data:
```
python2 plot.py
```

To export logged data into an excel file:
```
python2 export_to_excel.py
```
  
<p align="center"><img src="https://github.com/salehjg/system_resource_logger/blob/master/99_example_plot_output.png" /></p>

