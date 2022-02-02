i=input;p=print;from secrets import token_urlsafe as r
def O():p(r(int(50)))
def T():
 for _ in range(int(input('# '))):p(r(int(50)))
def M():
 u=i('1 Create Password\n2 ...\n\n')
 if u=='1':O()
 if u=='2':T()
 if u!='12':M()
M()
