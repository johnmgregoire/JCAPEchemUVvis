import time, copy, pickle
import os, os.path
import sys
import numpy, pylab

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

os.chdir(os.path.join(os.getcwd(),'am15'))
#set this to 1 for generating the AM1.5 array indexed by the wavelength range or your data, and then change to 0 to use this as a library of functions
if 0:
    p='am15.txt'

    f=open(p, mode='r')
    ls=f.readlines()
    f.close()

    wl=[]
    W_m2_nm=[]
    for l in ls[2:]:
        a, b=l.split('\t')[0:4:2]
        wl+=[myeval(a)]
        W_m2_nm+=[myeval(b)]

    wl=numpy.array(wl)
    W_m2_nm=numpy.array(W_m2_nm)


    f=open('wl.pck')#this is a pickle file of the array of wavelengths to be used in data anlalysis (from the spectrometer)
    wlgrid=pickle.load(f)
    f.close()

    W_m2_nm_grid=numpy.interp(wlgrid, wl, W_m2_nm)

    f=open('W_m2_nm.pck', mode='w')#this is the file to be used in batch analysis
    pickle.dump(W_m2_nm_grid, f)
    f.close()

    
    pylab.plot(wl, W_m2_nm, 'k')
    pylab.plot(wlgrid, W_m2_nm_grid, 'r:')
    
    integfcn=lambda inds: numpy.abs((W_m2_nm[inds[:-1]]*(wl[inds[1:]]-wl[inds[:-1]])).sum())

    inds=numpy.where(wl<wlgrid.min())[0]
    indsall=numpy.arange(len(wl))

    print 'total AM1.5 W/m2 and UV energy frac out of range: ', integfcn(indsall), integfcn(inds)/integfcn(indsall)
    indsrange=numpy.where((wl>wlgrid.min())&(wl<wlgrid.max()))[0]
    print 'W/m2 in this range: ', integfcn(indsrange)
    print 'frac total power in this range: ', integfcn(indsrange)/integfcn(indsall)
    pylab.show()

else:
    f=open('W_m2_nm.pck', mode='r')
    AM15_W_m2_nm=pickle.load(f)
    f.close()
    
    f=open('wl.pck')
    wl=pickle.load(f)
    f.close()
    #define the 2 utility functions to be sued for batch analysis
    IntegWL=lambda arr, inds:(arr[inds[:-1]]*(wl[inds[1:]]-wl[inds[:-1]])).sum()/(wl[inds[1:]]-wl[inds[:-1]]).sum()
    AM15TransFcn=lambda t, inds:IntegWL(t*AM15_W_m2_nm, inds)/IntegWL(AM15_W_m2_nm, inds)
