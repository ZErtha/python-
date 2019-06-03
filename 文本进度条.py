import time
s=50
print('执行开始'.center(s//2,'-'))
start=time.perf_counter()
for i in range(s+1):
    a='*'*i
    b='.'*(s-i)
    c=(i/s)*100
    d=time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,d),end='')
    time.sleep(0.1)
print('执行结束'.center(s//2,'-'))
    
