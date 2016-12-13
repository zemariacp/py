
'''
	This file contains some usefull functions.
	They can be used by simply importing them into your script:

	import j_utils as ju 

	Examples:
		exec_cmd(['rm','-rf', DST_PATH+'*'],1)
		exec_cmd(['mkdir', DST_PATH+'train'],1)
		exec_cmd(['mkdir', DST_PATH+'train/pos'],1)

		list, idx = get_uniq_idx(seq, idfun=None): 

		pos,neg = split_pos_neg_uniq(X_tr,Y_tr)
		pos,neg = split_pos_neg_uniq(X_te,Y_te)


		copy_files(pos,PNG_PATH,DST_PATH+'train/pos/')
		copy_files(neg_tr,PNG_PATH,DST_PATH+'train/neg/')
		copy_files(pos,PNG_PATH,DST_PATH+'valid/pos/')
		copy_files(neg,PNG_PATH,DST_PATH+'valid/pos/')

'''


#import cPickle as pickle
#from random import shuffle
import subprocess




#---- function def----------------------------------------

#---- COPY FILES ----
def copy_files(lst,src,dst):
    for f in lst:
	exec_cmd(['cp', src+f, dst],0)
    return 0




#---- EXEC COMMAND ----
def exec_cmd(lst_cmd_args,strip_newline):
    # where lst_cmd_args is of the format:
    #		['du', '-sh', '/modelState/']
    p = subprocess.Popen(lst_cmd_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if strip_newline:
        out=out.strip()
        err=err.strip()
    return out

#---- GET INDEXES FOR ELEMENTS IN LIST THAT ARE UNIQUE ----
def get_uniq_idx(seq, idfun=None): 
   # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   idx = []
   i=0
   for item in seq:
	marker = idfun(item)
	# in old Python versions:
	# if seen.has_key(marker)
	# but in new ones:
	if marker in seen:
	    i+=1
	    continue
	seen[marker] = 1
	result.append(item)
	idx.append(i)
	i+=1
   return result, idx

#---- SPLIT ELEMENTS IN LIST ACCORDING TO THEIR LABEL (1/0), REMOVES REPEATED ELEMENTS ----
def split_pos_neg_uniq(seq, labels, idfun=None): 
   # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   pos = []
   neg = []
   i=0
   for item in seq:
	marker = idfun(item)
	# in old Python versions:
	# if seen.has_key(marker)
	# but in new ones:
	if marker in seen:
	    i+=1
	    continue
	seen[marker] = 1
	if labels[i]==1:
	    pos.append(item)
	else:
	    neg.append(item)
	i+=1
   return pos, neg





