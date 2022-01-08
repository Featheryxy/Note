def say(message, times=1):#只有那些位于参数列表末尾的参数才能被赋予默认参数值，
                          #意即在函数的参数列表中拥有默认参数值的参数
                          # 不能位于没有默认参数值的参数之前
    print(message*times)

say('Hello')#times 默认为1
say("World ",5)