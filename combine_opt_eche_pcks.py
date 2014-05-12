import time, copy, pickle
import os, os.path
import sys
import numpy, pylab
from echem_plate_fcns import *
from GenAM15 import AM15TransFcn, IntegWL
def myeval(c):
    if c=='None':
        c=None
    elif c=='nan' or c=='NaN':
        c=numpy.nan
    else:
        temp=c.lstrip('0')
        if (temp=='' or temp=='.') and '0' in c:
            c=0
        else:
            c=eval(temp)
    return c

    
ev_nm=lambda x:1239.8/x


    
#folder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/9997_CAs'
#savefolderstart='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/9997_optpck'
##savefolderechemstart='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/9997_echempck'
#asprepfolder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/9997asprepared_newportsource_pck'
#
#filterlist=['_CA1', '_CA2', '_CA5']


def combinepcks(folder, savefolderstart, filterlist, asprepfolder, addtl_fom_calcfcn=None, fnmodfcn=None):#as prep folder will have keys remain as-is and filterlist has filter prepended
    fnsall=[os.listdir(savefolderstart+filterstr1) for count, filterstr1 in enumerate(filterlist)]
    fnsinters=set(os.listdir(asprepfolder))
#    if not fnmodfcn is None:
#        fnsall=[[fnmodfcn(fn) for fn in fns] for fns in fnsall]
#        fnsinters=set([fnmodfcn(fn) for fn in list(fnsinters)])
    for fns in fnsall:
        fnsinters=fnsinters.intersection(set(fns))

    for fn in fnsinters:
        infod={}
        rawd={}
        interd={}
        fomd={}
        
        p=os.path.join(asprepfolder, fn)
        f=open(p, mode='r')
        filed=pickle.load(f)
        f.close()
        if count==0:
            infod=copy.copy(filed['measurement_info'])
        for d, maink in zip([fomd, rawd, interd], ["fom", "raw_arrays", "intermediate_arrays"]):
            for k, v in filed[maink].iteritems():
                if k in ['rawselectinds', 'Wavelength(nm)', 'nm', 'eV']:
                    d[k]=v
                else:
                    d[k]=v
        for count, filterstr1 in enumerate(filterlist):
            p=os.path.join(savefolderstart+filterstr1, fn)
            f=open(p, mode='r')
            filed=pickle.load(f)
            f.close()
            if count==0:
                infod=copy.copy(filed['measurement_info'])
            for d, maink in zip([fomd, rawd, interd], ["fom", "raw_arrays", "intermediate_arrays"]):
                for k, v in filed[maink].iteritems():
                    if k in ['rawselectinds', 'Wavelength(nm)', 'nm', 'eV']:
                        d[k]=v
                    else:
                        d[filterstr1[1:]+'_'+k]=v
            
        #extra calculations
        if not addtl_fom_calcfcn is None:
            addtl_fom_calcfcn(fomd)
        savePck(savefolderstart, fn,  info=infod, rawData=rawd, interData=interd, FOMs=fomd)
