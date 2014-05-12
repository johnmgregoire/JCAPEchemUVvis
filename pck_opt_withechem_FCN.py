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


    
#folder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/9997_CA6_part2_0.5s'
#savefolderstart='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/9997_optpck'
#savefolderechemstart='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/9997_echempck'
#
#
##mainfiltlist=['_CA1', '_CA2', '_CA5']
#mainfiltlist=['_CA6']
#
#
darkfilterstr=['DARK%d_' %i for i in range(5, 20)]#make list of all DARK<integer> string to be average to create a dark spectrum for analysis
##darkfilterstr=['DARK%d_' %i for i in range(5, 40)]
##datafilterstr=['TRANS4_','TRANS5_','TRANS6_','TRANS7_']
##datafilterstr=['TRANS8_','TRANS9_','TRANS10_']
datafilterstr=['TRANS14_','TRANS15_','TRANS16_', 'TRANS17_','TRANS18_','TRANS19_']#in data files, these averaged together to create data spectrum


optfilterstr2='.opt'
filterstr2='.txt'

binoneside=5 # bin the spectra by 2*this number +1
ctrinds=numpy.arange(27,3050,2*binoneside+1)#range of indeces corresponding to useful range of wavelengths

def optandeche_folder(folder, savefolder, savefolderechem, filterstr1, optfilterstr1, \
        filterstr2=filterstr2, optfilterstr2=optfilterstr2, datafilterstr=datafilterstr, darkfilterstr=darkfilterstr, binoneside=binoneside, ctrinds=ctrinds, \
        numCApts=10, testonly=False):

    os.chdir(folder)

    fns=os.listdir(os.getcwd())

    optfns=[fn for fn in fns if optfilterstr1 in fn and optfilterstr2 in fn]
    txtfns=[fn for fn in fns if filterstr1 in fn and filterstr2 in fn]
    darkoptfns=[fn for fn in fns if optfilterstr2 in fn]

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

    srinds=numpy.where(code==1)[0] #code =1 means spectral reference
    srtxtfns=[txtfns[i] for i in srinds] #assembly list of sectral reference files to be used later
    srsmp=smp[srinds]
    srep=ep[srinds]




    parseandbin=lambda arr: numpy.array([arr[i-binoneside:i+binoneside+1].mean() for i in ctrinds])

    def readandinitprocess(rawd, interd, fns, fil1, filterlist, testonly=False):
        selfns=[[fn for fn in fns if fil1 in fn and fil2 in fn] for fil2 in filterlist]
        lens=[len(l) for l in selfns]
        #temp fix
        if not numpy.all(numpy.array(lens)==1):
            print 'trying to use backup plan for ', fil1, filterlist
            filterlist=['TRANS2_'] #this is the "backup plan" for what data files to use if can't find the specified ones
            selfns=[[fn for fn in fns if fil1 in fn and fil2 in fn] for fil2 in filterlist]
            lens=[len(l) for l in selfns]
        if not numpy.all(numpy.array(lens)==1):    
            print 'not right files for ', fil1, filterlist
            return 0
        if testonly:
            return 1
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

        return 1

    srdlist=[]
    for fn in srtxtfns:
        garbd={}
        interd={}
        readandinitprocess(garbd, interd, optfns, fn.partition(filterstr1)[0], datafilterstr, testonly=False)
        srdlist+=[interd]

    datakey='Transmittance_0'

    darkrawd={}
    darkinterd={}
    readandinitprocess(darkrawd, darkinterd, darkoptfns, 'Sample', darkfilterstr, testonly=False)
    darkdata=darkinterd[datakey]*.99 #always underestimate dark spectrum but this may need to be changed


    #this for loop process optical data for each sample
    for fn, e, sm, co in zip(txtfns, ep, smp, code):
        infod={}
        infod['sample_no']=sm
        infod['code']=co
        infod['Epoch']=e
        fomd={}
        rawd={}
        interd={}
        fnstart=fn.partition(filterstr1)[0]
        if not readandinitprocess(rawd, interd, optfns, fnstart, datafilterstr, testonly=testonly):
            continue
        if testonly:
            continue
        sri0, sri1=numpy.argsort((srep-e)**2)[:2]#finds the 2 spectral ref measurements with timestamp closest to data file
        srdata=numpy.array([srdlist[i][datakey] for i in [sri0, sri1]]).mean(axis=0)#average these 2 spec ref files to get the reference spectrum
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
        interd['Transmission'][i:i+n]=interd['Transmission'][i-1]*(1-wts)+interd['Transmission'][i+n]*(wts)#overwrite indexes that have saturation problem
        #comment out above here if no saturation problems
        
        #now calculate figures of merit
        inds=numpy.where((interd['nm']>380)&(interd['nm']<900))[0]
        fomd['AveTrans_380_900']=IntegWL(interd['Transmission'], inds)
        fomd['AveAM15Trans_380_900']=AM15TransFcn(interd['Transmission'], inds)
        
        savePck(savefolder, fnstart,  info=infod, rawData=rawd, interData=interd, FOMs=fomd)
        #pylab.plot(interd['eV'], interd['Transmission'])
    
    #this for loop process echem data for each sample
    if not savefolderechem is None:
        for fn, e, sm, co in zip(txtfns, ep, smp, code):
            if testonly:
                continue
            infod={}
            infod['sample_no']=sm
            infod['code']=co
            infod['Epoch']=e
            fomd={}
            rawd={}
            interd={}
            fnstart=fn.partition(filterstr1)[0]
            echemd=readechemtxt(os.path.join(os.getcwd(), fn))
            if not (numCApts is None):
                for k, v in echemd.iteritems():
                    if isinstance(v, numpy.ndarray):
                        rawd[k]=v
                if len(rawd['I(A)'])<numCApts:
                    n=int(.8*len(rawd['I(A)']))
                else:
                    n=numCApts
                fomd['Iave']=rawd['I(A)'][-n:].mean()
            savePck(savefolderechem, fnstart,  info=infod, rawData=rawd, interData=interd, FOMs=fomd)
#>>> f=open('wl.pck',mode='w')
#>>> pickle.dump(interd['nm'],f)
#>>> f.close()


#for filterstr1 in mainfiltlist:
#    savefolder=savefolderstart+filterstr1
#    savefolderechem=savefolderechemstart+filterstr1
#    optandeche_folder(folder, savefolder, savefolderechem, filterstr1, filterstr1, testonly=False)
