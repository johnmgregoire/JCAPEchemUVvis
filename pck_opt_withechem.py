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

filterstr1='_CA1'

os.chdir('C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/9997_CAs')
savefolder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/9997_optpck'+filterstr1
savefolderechem='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/9997_echempck'+filterstr1
fns=os.listdir(os.getcwd())

optfilterstr1=filterstr1
optfilterstr2='.opt'
optfns=[fn for fn in fns if optfilterstr1 in fn and optfilterstr2 in fn]

darkoptfns=[fn for fn in fns if optfilterstr2 in fn]
filterstr2='.txt'
txtfns=[fn for fn in fns if filterstr1 in fn and filterstr2 in fn]

def getheadattrs(fn, searchstrs=['%Sample=', '%Epoch=', '%code='], ev=True, readbytes=1000):
    f=open(fn, mode='r')
    s=f.read(readbytes)
    f.close()
    ret=[]
    for ss in searchstrs:
        vs=s.partition(ss)[2].partition('\n')[0].strip()
        ret+=[eval(vs)]
    return ret

temp=[getheadattrs(fn) for fn in txtfns]
smp, ep, code=numpy.array(temp).T
inds=numpy.argsort(ep)
smp=smp[inds]
ep=ep[inds]
code=code[inds]
txtfns=[txtfns[i] for i in inds]

srinds=numpy.where(code==1)[0]
srtxtfns=[txtfns[i] for i in srinds]
srsmp=smp[srinds]
srep=ep[srinds]


darkfilterstr=['DARK%d_' %i for i in range(5, 40)]
datafilterstr=['TRANS5_']

binoneside=5

ctrinds=numpy.arange(27,3050,11)

parseandbin=lambda arr: numpy.array([arr[i-binoneside:i+binoneside+1].mean() for i in ctrinds])

def readandinitprocess(rawd, interd, fns, fil1, filterlist):
    selfns=[[fn for fn in fns if fil1 in fn and fil2 in fn] for fil2 in filterlist]

    lens=[len(l) for l in selfns]
    if not numpy.all(numpy.array(lens)==1):
        print 'not right files for ', fil1, filterlist
        return
    intarr=[]
    for l, lab in zip(selfns, filterlist):
        for k, v in readopttxt(os.path.join(os.getcwd(), l[0])).iteritems():
            if not k.startswith('Wave'):
                intarr+=[v]
                rawd[lab+'_'+k]=v
                kinter=k
            else:
                rawd[k]=v
    interd[kinter]=parseandbin(numpy.array(intarr).mean(axis=0))

    return

srdlist=[]
for fn in srtxtfns:
    garbd={}
    interd={}
    readandinitprocess(garbd, interd, optfns, fn.partition(filterstr1)[0], datafilterstr)
    srdlist+=[interd]

datakey='Transmittance_0'

darkrawd={}
darkinterd={}
readandinitprocess(darkrawd, darkinterd, darkoptfns, 'Sample', darkfilterstr)
darkdata=darkinterd[datakey]*.99



for fn, e, sm, co in zip(txtfns, ep, smp, code):
    infod={}
    infod['sample_no']=sm
    infod['code']=co
    infod['Epoch']=e
    fomd={}
    rawd={}
    interd={}
    fnstart=fn.partition(filterstr1)[0]
    readandinitprocess(rawd, interd, optfns, fnstart, datafilterstr)
    sri0, sri1=numpy.argsort((srep-e)**2)[:2]
    srdata=numpy.array([srdlist[i][datakey] for i in [sri0, sri1]]).mean(axis=0)
    interd['Dark']=darkdata
    interd['SpectralReference']=srdata
    interd['SpectralReferenceSamples']=smp[srinds]
    interd['Transmission']=(interd[datakey]-darkdata)/(srdata-darkdata)
    interd['rawselectinds']=ctrinds
    interd['nm']=rawd['Wavelength(nm)'][ctrinds]
    interd['eV']=ev_nm(interd['nm'])
    
    #this is to fix couple saturated points - shoudl generally be removed
    i=numpy.argmin((interd['nm']-818.)**2)
    n=5
    wts=numpy.arange(1, n+1)/(n+1)
    interd['Transmission'][i:i+n]=interd['Transmission'][i-1]*(1-wts)+interd['Transmission'][i+n]*(wts)
    
    inds=numpy.where((interd['nm']>400)&(interd['nm']<900))[0]
    fomd['AveTrans_400_900']=IntegWL(interd['Transmission'], inds)
    fomd['AveAM15Trans_400_900']=AM15TransFcn(interd['Transmission'], inds)
    
    savePck(savefolder, fnstart,  info=infod, rawData=rawd, interData=interd, FOMs=fomd)
    #pylab.plot(interd['eV'], interd['Transmission'])


for fn, e, sm, co in zip(txtfns, ep, smp, code):
    infod={}
    infod['sample_no']=sm
    infod['code']=co
    infod['Epoch']=e
    fomd={}
    rawd={}
    interd={}
    fnstart=fn.partition(filterstr1)[0]
    echemd=readechemtxt(os.path.join(os.getcwd(), fn))
    for k, v in echemd.iteritems():
        if isinstance(v, numpy.ndarray):
            rawd[k]=v
    fomd['Iave']=rawd['I(A)'][-10:].mean()
    savePck(savefolderechem, fnstart,  info=infod, rawData=rawd, interData=interd, FOMs=fomd)
#>>> f=open('wl.pck',mode='w')
#>>> pickle.dump(interd['nm'],f)
#>>> f.close()
