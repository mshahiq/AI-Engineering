class find_spy:

    def __init__(self,nump,list_of_pairs) -> None:
        self.nump = nump
        self.list_of_pairs = list_of_pairs

    def find_spy_in_pairs(self):

        if self.nump<=0 or (len(self.list_of_pairs)>self.nump):
            return -1   
        for lp in self.list_of_pairs:
            if (len(lp)!=2):
                return -1
            
        list_of_nonspies = []
        for i in self.list_of_pairs:
            list_of_nonspies.append(i[1])

        list_of_spies = []
        for i in self.list_of_pairs:
            if i[0] not in list_of_nonspies:
                list_of_spies.append(i[0])

        chance_spies = {}

        for i in list_of_spies:

            chance_spies[i] = chance_spies.get(i,0)+1

        for key,values in chance_spies.items():

            if values > 1:
                return key

        if len(list_of_spies)<=0:
            return 0 

detect_the_spy = find_spy(3,[['felix', 'lara'], ['felix', 'jeno'], ['lara', 'jeno']])

# detect_the_spy = find_spy(3,[['felix', 'lara'], ['lara', 'jeno'], ['lara', 'felix']])

print(detect_the_spy.find_spy_in_pairs())