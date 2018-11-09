import random
class People():

    def __init__(self,dictionary,number):
        self.dictionary= dictionary
        self.number = number


    #选择投票或者弃权
    def Vote(self):
        print(self.dictionary)
        #存放投票结果
              
        while True:
            selection = input('>>Y/N:')

            if selection == 'Y':

                print(self.number)
                #选择投票对象
                sel = int(input('select from 1-4:'))

                if sel == self.number:
                    print('You can not select yourself')

                elif sel in range(1,4):
                    result = ('v_%d_%s'%(self.number,sel))
                    #将投票结果放入列表中
                    return(self.HandleVote(result))
                            
            elif selection == 'N':
                
                result=('q_%d_%s'%(self.number,'q'))
                return(self.HandleVote(result))
            
            else:
                print('Enter the right command!')
        
    



    def ShowRecord():
        pass

    def election():
        pass

    def speak():
        pass
    
    def HandleVote(self,result):
        global dictionary
        global VoteDict
        #为投票对象建立列表
        VList = []
        #将键值对翻转,显示有谁投了谁,建立的新字典
        new_dict = {}
        
        #v/n
        judge = result.split('_')[0]
        #玩家
        who = result.split('_')[1]
        #被投者
        state = result.split('_')[2]

        #如果玩家选择投票
        if judge == 'v':
            #将所有投票结果放入字典
            VoteDict[who] = state

            #所有投票结束
            if len(VoteDict) == 3:
                for k,v in VoteDict.items():
                    #将键值对颠倒,键为被投人,值为投票者,并显示
                    if v not in VList:
                        VList.append(v)

                        new_dict.setdefault(v,[]).append(k)
                    else:
                        new_dict.setdefault(v,[]).append(k)
                        
                
                print(new_dict)
                #计算哪位玩家被投次数最多,被淘汰,并更改状态1->0
                count = 0
                for k,v in new_dict.items():
                    number = len(v)
                    if number > count:
                        count = number
                for k,v in new_dict.items():
                    if len(v) == count:
                        print('name:',k)
                        dictionary[k]=0
                        print(dictionary)

                    
            
                

        # elif result == 'q':
        #     pass


    
    
dictionary = {'1':'1','2':'1','3':'1'}
VoteDict = {}

for i in range(1,4):
    number = i
    people = People(dictionary,number)
    people.Vote()   
