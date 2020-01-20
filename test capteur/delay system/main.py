
import pycom
import time

periode = 500000

def fib(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a+b

time.sleep(0.1)

ref_time = time.ticks_us()


for i in range(0,100):
    start_time = time.ticks_us()

    fib(i)

    end_time = time.ticks_us()

    time.sleep(( periode - ( end_time - start_time ) )/1000000 )
    #print("time.delay("+str(periode - ( end_time - start_time ))+")")
    print("fib_time", (end_time-start_time))

    f_end_time = time.ticks_us()
    print("time: ", f_end_time - start_time)

tot_time =  time.ticks_us() - ref_time

print("tot_time = ", tot_time)
