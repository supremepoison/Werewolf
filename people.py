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
        VoteList = []
        
        
        
        judge = result.split('_')[0]
        who = result.split('_')[1]
        state = result.split('_')[2]

        if judge == 'v':

            VoteDict[who] = state

            if len(VoteDict) == 3:
                for k,v in VoteDict.items():
                    if v not in VoteList:
                        VoteList.append(v)
                    
                    

                # new_dict = {v:k for k,v in VoteDict.items()}
            # if state not in VoteList:           
            #     VoteList.append(state)
            #     StatList = []
            #     StatList.append(who)
            
            
                print (new_dict) 
            



            # print(VoteDict)           

        elif result == 'q':
            pass


    
    
dictionary = {1:1,2:1,3:1}
VoteDict = {}

for i in range(1,4):
    number = i
    people = People(dictionary,number)
    people.Vote()   
