length = 700
velocity = 90

time_hrs = (length//velocity)
time_min = ((length%velocity)/90)*60
time_sec = ((length/velocity)- time_hrs - int(time_min)/60)*3600

print(f'Time is {time_hrs} hrs {int(time_min)} min and {round(time_sec)} seconds')

