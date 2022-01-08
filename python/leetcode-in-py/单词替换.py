# coding = gbk

# 杈撳叆: dict(璇嶅吀) = ["cat", "bat", "rat"]
#      sentence(鍙ュ瓙) = "the cattle was rattled by the battery"
# 杈撳嚭: "the cat was rat by the bat"


class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        
        dict = set(dict)
        str_list = sentence.split(' ')
        ret = []
        
        for str1 in str_list:
            flag = True
            for i in range(len(str1)):
                if str1[:i] in dict:
                    ret.append(str1[:i])
                    flag = False
                    break
            if flag:
                ret.append(str1)
        
        return ' '.join(ret)
            
            
