#!/usr/bin/python
def schedule(series):
	res=[]
	tmp=dict()
	helper(series,0,res,tmp)
	return res
def helper(series,start,res,tmp):
	print tmp
	if len(tmp)==len(series):
		res.append(tmp.copy())
		return 
	else:
		for movie,times in series.iteritems():
			if movie not in tmp and max(times)>=start:
				for time in times:
					if time>=start:
						tmp[movie] = time
						helper(series,time+1,res,tmp)
						del tmp[movie]
#								 break

#d = {"MadMax": [12, 13, 16, 17],
#"Zootopia": [12, 15, 19], 
#"StarWar": [11, 17, 18]}

d = {"a":[9,15],
"b":[14],
"c":[9,16]}
print schedule(d)