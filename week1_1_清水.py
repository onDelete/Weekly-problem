# coding = utf-8



def function(strs):
    if strs == '': return '请输入字符串！'
    
    if strs != None:
        length = len(strs)
        if length == 1: return 'palindrome'
        lists = []
        for i in xrange(length):
            lists.append(strs[length-1-i])
        srts = ''.join(lists)
        if srts == strs: return 'palindrome'
        
        return srts
    
    
if __name__ == '__main__':
    strs = raw_input('输入字符串：')
    print function(strs)
