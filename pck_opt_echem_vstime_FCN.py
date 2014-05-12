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
darkfilterstr=['DARK%d_' %i for i in range(5, 20)]
##darkfilterstr=['DARK%d_' %i for i in range(5, 40)]
##datafilterstr=['TRANS4_','TRANS5_','TRANS6_','TRANS7_']
##datafilterstr=['TRANS8_','TRANS9_','TRANS10_']
datafilterstr='TRANS'


optfilterstr2='.opt'
filterstr2='.txt'

binoneside=5
ctrinds=numpy.arange(27,3050,11)

def optandeche_folder(folder, savefolder, savefolderechem, filterstr1, optfilterstr1, \
        filterstr2=filterstr2, optfilterstr2=optfilterstr2, datafilterstr=datafilterstr, darkfilterstr=darkfilterstr, binoneside=binoneside, ctrinds=ctrinds, \
        numCApts=10, testonly=False, numspecreftoskipatstart=2, echemSGnpts_o_bin=None, optSGnpts_o_bin=None, darkmult=.99, numcvsegs=0):

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

    srinds=numpy.where(code==1)[0]
    srtxtfns=[txtfns[i] for i in srinds]
    srsmp=smp[srinds]
    srep=ep[srinds]




    parseandbin=lambda arr: numpy.array([arr[i-binoneside:i+binoneside+1].mean() for i in ctrinds])

    def readandinitprocess(rawd, interd, fns, fil1, filterlist, testonly=False):
        if isinstance (filterlist, str):
            selfns=[[fn] for fn in fns if fil1 in fn and filterlist in fn]
            
        else:
            selfns=[[fn for fn in fns if fil1 in fn and fil2 in fn] for fil2 in filterlist]
            lens=[len(l) for l in selfns]
            #temp fix
            if not numpy.all(numpy.array(lens)==1):
                print 'trying to use backup plan for ', fil1, filterlist
                filterlist=['TRANS2_']
                selfns=[[fn for fn in fns if fil1 in fn and fil2 in fn] for fil2 in filterlist]
                lens=[len(l) for l in selfns]
            if not numpy.all(numpy.array(lens)==1):    
                print 'not right files for ', fil1, filterlist
                return 0
        
        if testonly:
            return 1
        
        timestrs=[fn[0].rpartition('.opt')[0].rpartition('_')[2] for fn in selfns]

        
        times=numpy.array([time.mktime(time.strptime(s.rpartition('.')[0],'%Y%m%d.%H%M%S')) for s in timestrs])
        times+=numpy.array([0.1*myeval(s.rpartition('.')[2]) for s in timestrs])
        sortinds=numpy.argsort(times)
        times=times[sortinds]-times.min()
        selfns=[selfns[i] for i in sortinds]
        
        intarr=[]
        for fnl in selfns:
            fn=fnl[0]
            lab='TRANS'+fn.partition('TRANS')[2].partition('_')[0]
            for k, v in readopttxt(os.path.join(os.getcwd(), fn)).iteritems():
                if not k.startswith('Wave'):
                    intarr+=[v]
                    rawd[lab+'_'+k]=v
                    
                    kinter=k
                else:
                    rawd[k]=v
        interd[kinter+'_t']=numpy.array([parseandbin(v) for v in intarr])
        interd['t']=times
        
        interd[kinter]=parseandbin(numpy.array(intarr).mean(axis=0))
        

        return 1

    datakey='Transmittance_0'
    
    srdlist=[]
    for fn in srtxtfns:
        garbd={}
        interd={}
        readandinitprocess(garbd, interd, optfns, fn.partition(filterstr1)[0], datafilterstr, testonly=False)
        interd[datakey]=(interd[datakey+'_t'][numspecreftoskipatstart:]).mean(axis=0)
        srdlist+=[interd]

    

    darkrawd={}
    darkinterd={}
    readandinitprocess(darkrawd, darkinterd, darkoptfns, 'Sample', darkfilterstr, testonly=False)
    darkdata=darkinterd[datakey]*darkmult


    opttimes_txt=[]
    optavetrans_txt=[]
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
        sri0, sri1=numpy.argsort((srep-e)**2)[:2]
        srdata=numpy.array([srdlist[i][datakey] for i in [sri0, sri1]]).mean(axis=0)
        interd['Dark']=darkdata
        interd['SpectralReference']=srdata
        interd['SpectralReferenceSamples']=smp[srinds]
        interd['Transmission']=(interd[datakey]-darkdata)/(srdata-darkdata)
        interd['Transmission_t']=numpy.array([(arr-darkdata)/(srdata-darkdata) for arr in interd[datakey+'_t']])
        interd['rawselectinds']=ctrinds
        interd['nm']=rawd['Wavelength(nm)'][ctrinds]
        interd['eV']=ev_nm(interd['nm'])
        
        #this is to fix couple saturated points - shoudl generally be removed
        i=numpy.argmin((interd['nm']-818.)**2)
        n=5
        wts=numpy.arange(1, n+1)/(n+1)
        interd['Transmission'][i:i+n]=interd['Transmission'][i-1]*(1-wts)+interd['Transmission'][i+n]*(wts)
        for j in range(len(interd['Transmission_t'])):
            interd['Transmission_t'][j, i:i+n]=interd['Transmission_t'][j, i-1]*(1-wts)+interd['Transmission_t'][j, i+n]*(wts)
        
        inds=numpy.where((interd['nm']>380)&(interd['nm']<900))[0]
        fomd['AveTrans_380_900']=IntegWL(interd['Transmission'], inds)
        fomd['AveAM15Trans_380_900']=AM15TransFcn(interd['Transmission'], inds)
        
        if not optSGnpts_o_bin is None:
            nptsoneside, order, binprior=optSGnpts_o_bin
            for j in range(len(interd['Transmission_t'])):
                interd['Transmission_t'][j]=savgolsmooth(interd['Transmission_t'][j], nptsoneside=nptsoneside, order = order, binprior=binprior)
                
        #save these things to interd but they are not appropriate length for plotting
        interd['AveTrans_380_900_t']=numpy.array([IntegWL(arr, inds) for arr in interd['Transmission_t']])
        interd['AveAM15Trans_380_900_t']=numpy.array([AM15TransFcn(arr, inds) for arr in interd['Transmission_t']])
        
        opttimes_txt+=[interd['t']]
        optavetrans_txt+=[interd['AveAM15Trans_380_900_t']]
        
        savePck(savefolder, fnstart,  info=infod, rawData=rawd, interData=interd, FOMs=fomd)
        #pylab.plot(interd['eV'], interd['Transmission'])


    if not savefolderechem is None:
        for fn, e, sm, co, opttimes, optavetrans in zip(txtfns, ep, smp, code, opttimes_txt, optavetrans_txt):
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
    
            for k, v in echemd.iteritems():
                if isinstance(v, numpy.ndarray):
                    rawd[k]=v
            
            inds=numpy.array([numpy.argmin((t-rawd['t(s)'])**2) for t in opttimes])
            midinds=list(numpy.int32(numpy.ceil((inds[1:]+inds[:-1])/2.)))
            parsetoopttimes=lambda arr:numpy.array([arr[i0:i1].mean() for i0, i1 in zip([0]+midinds, midinds+[len(rawd['t(s)'])])])
            if not echemSGnpts_o_bin is None:
                nptsoneside, order, binprior=echemSGnpts_o_bin
                #interd['I(A)_SG']=savgolsmooth(rawd['I(A)'], nptsoneside=nptsoneside, order = order, binprior=binprior)
                #here this is to smooth by segment - not generally applicable
                if numcvsegs>0:
                    a=len(rawd['I(A)'])
                    b=a//2
                    c=b//2
                    inds_segs=[range(0, c), range(c, b), range(b, b+c), range(b+c, a)]
                    interd['I(A)_SG']=rawd['I(A)'][:]
                    for inds in inds_segs:
                        interd['I(A)_SG'][inds]=savgolsmooth(rawd['I(A)'][inds], nptsoneside=nptsoneside, order = order, binprior=binprior)
        
            interd['rawselectinds']=list(inds)
            for k in ['Ewe(V)', 'I(A)', 't(s)']:
                interd[k+'_opt']=parsetoopttimes(rawd[k])
            interd['opttimes']=opttimes
            interd['optavetrans']=optavetrans
            
            savePck(savefolderechem, fnstart,  info=infod, rawData=rawd, interData=interd, FOMs=fomd)
            
#>>> f=open('wl.pck',mode='w')
#>>> pickle.dump(interd['nm'],f)
#>>> f.close()


#for filterstr1 in mainfiltlist:
#    savefolder=savefolderstart+filterstr1
#    savefolderechem=savefolderechemstart+filterstr1
#    optandeche_folder(folder, savefolder, savefolderechem, filterstr1, filterstr1, testonly=False)
