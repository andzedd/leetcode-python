class Solution(object):
    def reverse(self, x):
        str_x = str(x)
        neg_limit= -0x80000000
        pos_limit= 0x7fffffff
        if x < 0:
            str_x = '-'+str_x[::-1][:-1]
        else:
            str_x = str_x[::-1]
        x = int(str_x)
        
        if x < 0:
            value = x & neg_limit
            if(value == neg_limit):
                return x
            else:
                return 0
        elif(x==0):
            return x
        else:
            val = x&pos_limit
            if(val==x):
                return x
            else:
                return 0