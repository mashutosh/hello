class Organizer(object):
    """ A class to """

    def __init__(self, n, ):
        """ Initialization """
        self.total_no_of_hours = n

    def parseCSVInput(self, csv_input):
        """
        """
        presenter_list = []
        res = csv_input.split('#')
        for item in res:
            presenter_list.append(tuple(item.split(',')))
        return presenter_list

    def organiseEvent(self, presenter_list):
	max_hrs = self.total_no_of_hours
	final_time_list = []
	import itertools as it
        #import pdb;pdb.set_trace()
	jj = list(it.combinations(presenter_list,3))
        print jj
	for i in jj:
	    checker = 0
	    break_flag = False
	    for item in i:
		p_hours = float(item[1])     
		if p_hours > max_hrs/2 or checker > max_hrs:
		    break_flag = True
		    break
		checker = checker + p_hours
	    
	    if checker <= max_hrs and not break_flag: 
		final_time_list.append(i)
	return final_time_list
    
    def organiseEventOptimumCost(self, presenter_list):
	from operator import itemgetter
	final_time_list = []
	for i in presenter_list:
	    checker = 0
	    for item in i:
		p_cost = item[2]       
		checker = checker + int(p_cost)
	    final_time_list.append((i,checker))
	print final_time_list
	return sorted(final_time_list,key=itemgetter(1))[0][0]
    

if __name__=='__main__':
    csv_input = "p1,2,100#p2,2,200#p3,2,250#p4,5,100"
    organiser_obj = Organizer(6.0)
    pattern = organiser_obj.parseCSVInput(csv_input)
    print pattern
    final_time_list = organiser_obj.organiseEvent(pattern)
    print final_time_list
    if len(final_time_list) > 1:
        final_time_list = organiser_obj.organiseEventOptimumCost(final_time_list)

