from urllib.request import urlopen
from json import loads
from urllib.error import HTTPError,URLError
import datetime

class get_all:

    def __init__(self,handle):

        self.handle= handle

        self.info_url = "https://codeforces.com/api/user.info?handles="+str(handle)

        self.status_url="https://codeforces.com/api/user.status?handle="+str(handle)

        self.contests_url='https://codeforces.com/api/user.rating?handle=' +str(handle)

        self.infofile=loads(urlopen(self.info_url).read())

        self.statusfile=loads(urlopen(self.status_url).read())

        self.contestsfile=loads(urlopen(self.contests_url).read())

    def get_info(self):
        self.name = ''

        self.country = ''

        self.city = ''

        self.Organization = ''

        self.friends = 0

        self.Rank = ''

        self.Rating = 0

        self.image = ''

        self.registered = ''

        self.info=self.infofile["result"][0]

        if('firstName' in self.info ) :       self.name =self.info['firstName']+' '

        if('lastName' in self.info):          self.name +=self.info['lastName']

        if('country' in self.info):           self.country = self.info['country']

        if('city' in self.info):              self.city = self.info['city']

        if('organization' in self.info):      self.Organization = self.info['organization']

        if("friendOfCount" in self.info):    self.friends = self.info["friendOfCount"]

        if ('rank' in self.info):             self.Rank = self.info['rank']

        if ('rating' in self.info):           self.Rating = self.info['rating']

        if('avatar' in self.info):            self.image = self.info['avatar']

        self.registered=datetime.datetime.fromtimestamp(self.info['registrationTimeSeconds']).strftime('%Y-%m-%d %H:%M:%S')

    def get_problem(self):

        self.problemfile = loads(urlopen(self.status_url).read())['result']

        self.languages=dict()

        self.verdict=dict()

        self.solved=list()

        self.solved_level=dict()

        self.unsolved_problem=list()
        self.tryed_problem=0
        self.unsolvedids=[]
        self.solved_tages=list()

        for i in self.problemfile:
            if i["programmingLanguage"] not in self.languages: self.languages[i["programmingLanguage"]]=1
            else: self.languages[i["programmingLanguage"]]+=1

            ''' 
        check every submition even accepted or no '''

            if i['problem'] not in self.solved: #check if submit accepted or no

                if i['verdict']=='OK' and i["author"]['participantType']=="PRACTICE": ## check if problem has condition ok or no to add it to solved

                    self.solved.append(i['problem']) ##add the problem to solved list
                    '''
                    if user just submitted many submittions after accepted case the we sure it's exited in unsolved dict we need to remove it  
                    such as :
                    try 
                    try 
                    try 
                    accepted 
                    try 
                    accepted
                    try 
                    it coming from up to down ;)
                    '''
                    if (i['problem'] in self.unsolved_problem): self.unsolved_problem.remove(i['problem'])

                else:
                    if i['problem'] not in self.unsolved_problem and i['author']['participantType']=='PRACTICE':
                        self.unsolved_problem.append(i['problem'])
        for i in self.problemfile:
            if i['verdict']=='OK' and i["author"]['participantType']=="PRACTICE":
                for tag in i['problem']['tags'] : ## starting add the solved tages to tages list :)#

                  #      '''check if tag existed before or no to avoid having many tags with same name '''
                    if (tag not in self.solved_tages): self.solved_tages.append(tag)####see above

              #          '''then levels section of problemsuch A,B,C,D,.... '''

                if (i['problem']['index'] not in self.solved_level) : self.solved_level[i['problem']['index']]=1 ### if level not existed make it
                else :  self.solved_level[i['problem']['index']]+=1
                    ##if existed add one to it
                   # '''    if the submit is not exited in solved the it's means it has no solution in the user submition
                    #because we search the problem from the last to previous it's meaning if it has solution it will meet us
                    #before ;)
                    #'''
            if i['verdict'] not in self.verdict: self.verdict[i['verdict']]=1
            else : self.verdict[i['verdict']]+=1
        self.tryed_problem+=len(self.unsolved_problem)
        for level in self.solved_level:
            self.tryed_problem+=self.solved_level[level]
    def get_contest(self,):
        self.number_of_contests=0
        self.number_of_contests+=len(self.contestsfile["result"])
        self.rank_list=list()
        self.rating_difference_list=list()
        self.Best_Rank=0
        self.worst_Rank=0
        self.max_up=0
        self.max_down=0
        if self.number_of_contests>0:
            for i in range(self.number_of_contests):
                self.rank_list.append(self.contestsfile["result"][i]['rank'])

                self.rating_difference_list.append(self.contestsfile["result"][i]['newRating']-self.contestsfile["result"][i]['oldRating'])
        if len(self.rank_list)>0:
            self.Best_Rank=min(self.rank_list)
            self.worst_Rank=max(self.rank_list)
        if len(self.rating_difference_list)>0:
            self.max_up=max(self.rating_difference_list)
            self.max_down=min(self.rating_difference_list)



   ####################################the comming section special for phase :)################################################

    def get_probelms_for_phase(self):
        self.phase1=list()
        self.phase2=list()
        self.phase3=list()
        for i in self.problemfile:
            datediffernce=datetime.datetime.now()-datetime.datetime.fromtimestamp(i['creationTimeSeconds'])
            if datediffernce.days<=6:
                self.phase1.append(i)
            elif datediffernce.days>6 and datediffernce.days<14:
                self.phase2.append(i)
            elif datediffernce.days>13 and datediffernce.days<=20:
                self.phase3.append(i)
            else: break
    def phase1_info(self):
        self.phase1_submitions=len(self.phase1)
        self.phase1_accepted=list()
        self.phase1_ids=list()
        self.phase1_accepted_ids=list()
        self.phase1_max_rated_problem=0
        self.phase1_av=0
        self.phase1_av_count=0
        self.phase1_max_problem=dict()
        self.phase1_solved=list()
        self.phase1_average=0
        self.phase1_virtual_count=0
        self.phase1_contestids=[]
        self.phase1_contestcount=0
        self.phase1_virtualids=[]
        for problem in self.phase1:
            if ( problem['id'] not in self.phase1_accepted_ids )  and problem['verdict']=="OK":
                self.phase1_solved+=[problem]
                if problem['author']['participantType']=='VIRTUAL' and problem['contestId'] not in self.phase1_virtualids:
                    self.phase1_virtual_count+=1
                    self.phase1_virtualids+=[problem['contestId']]
                if problem['author']['participantType']=='CONTESTANT' and problem['contestId'] not in self.phase1_contestids:
                    self.phase1_contestcount+=1
                    self.phase1_contestids+=[problem['contestId']]
                # if problem['author']['participantType'] != 'VIRTUAL':
                #     if self.phase1_max_rated_problem < problem['problem']['rating'] and problem['author']['participantType']=='PRACTICE' :
                #         self.phase1_max_rated_problem=problem['problem']['rating']
                #     self.phase1_av+=problem['author']['rating']
                #     self.phase1_av_count += 1
        if ( self.phase1_av_count>0):self.phase1_av/=self.phase1_av_count
    def phase2_info(self):
        self.phase2_submitions=len(self.phase2)
        self.phase2_accepted=list()
        self.phase2_ids=list()
        self.phase2_accepted_ids=list()
        self.phase2_max_rated_problem=0
        self.phase2_av=0
        self.phase2_av_count=0
        self.phase2_max_problem=dict()
        self.phase2_solved=list()
        self.phase2_average=0
        self.phase2_virtual_count=0
        self.phase2_contestids=[]
        self.phase2_contestcount=0
        self.phase2_virtualids=[]
        for problem in self.phase2:
            if ( problem['id'] not in self.phase2_accepted_ids )  and problem['verdict']=="OK":
                self.phase2_accepted_ids+=[problem['id']]
                self.phase2_solved+=[problem]
                if problem['author']['participantType']=='VIRTUAL' and problem['contestId'] not in self.phase2_virtualids:
                    self.phase2_virtual_count+=1
                    self.phase2_virtualids+=[problem['contestId']]
                if problem['author']['participantType']=='CONTESTANT' and problem['contestId'] not in self.phase2_contestids:
                    self.phase2_contestcount+=1
                    self.phase2_contestids+=[problem['contestId']]
                # if problem['author']['participantType'] != 'VIRTUAL':
                #     if self.phase2_max_rated_problem < problem['author']['rating'] and problem['author']['participantType']=='PRACTICE' :
                #         self.phase2_max_rated_problem=problem['author']['rating']
                #     self.phase2_av+=problem['author']['rating']
                #     self.phase2_av_count += 1
        if ( self.phase2_av_count>0):self.phase2_av/=self.phase2_av_count
    def phase3_info(self):
        self.phase3_submitions=len(self.phase3)
        self.phase3_accepted=list()
        self.phase3_ids=list()
        self.phase3_accepted_ids=list()
        self.phase3_max_rated_problem=0
        self.phase3_av=0
        self.phase3_av_count=0
        self.phase3_max_problem=dict()
        self.phase3_solved=list()
        self.phase3_average=0
        self.phase3_virtual_count=0
        self.phase3_contestids=[]
        self.phase3_contestcount=0

        self.phase3_virtualids=[]
        for problem in self.phase3:
            if ( problem['id'] not in self.phase3_accepted_ids )  and problem['verdict']=="OK":
                self.phase3_solved+=[problem]
                if problem['author']['participantType']=='VIRTUAL' and problem['contestId'] not in self.phase3_virtualids:
                    self.phase3_virtual_count+=1
                    self.phase3_virtualids+=[problem['contestId']]
                if problem['author']['participantType']=='CONTESTANT' and problem['contestId'] not in self.phase3_contestids:
                    self.phase3_contestcount+=1
                    self.phase3_contestids+=[problem['contestId']]
                # if problem['author']['participantType'] != 'VIRTUAL':
                #     if self.phase3_max_rated_problem < problem['author']['rating'] and problem['author']['participantType']=='PRACTICE' :
                #         self.phase3_max_rated_problem=problem['author']['rating']
                #     self.phase3_av+=problem['author']['rating']
                #     self.phase3_av_count += 1
        if ( self.phase3_av_count>0):self.phase3_av/=self.phase3_av_count
