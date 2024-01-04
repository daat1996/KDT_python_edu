# 터틀 그래픽스로 그림 그리기
import turtle as t
t.shape('turtle')

n, l =map(int, input().split())



for i in range(n):
    t.fd(100)
    t.rt((360/n)*2)
    t.fd(100)
    t.lt(360/n)



t.mainloop()