import os,numpy,pylab,pickle
from GenAM15 import AM15TransFcn, IntegWL

from echem_plate_fcns import *
echemfolder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/10157_echempck_CV3'
optfolder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/10157_optpck_CV3'
savefolder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/imagesandsummary/10157_CV3'

#echemfolder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/10157_echempck_CA5'
#optfolder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/10157_optpck_CA5'
#savefolder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/imagesandsummary/10157_CA5'

def loadPckKeys(p, keys=None):
    try:
        f=open(p, mode='r')
        d=pickle.load(f)
        f.close()
        if keys is None:
            keys=d.keys()
        return [d[k] for k in keys]
    except:
        return None
        
def savePck(savefolder, fn, version=1, info={}, FOMs={}, rawData={}, interData={}, params={}):
    savepath = os.path.join(savefolder, fn+'.pck')
    with open(savepath, 'w') as pckfile:
        saveDict=dict([(k, v) for k, v in zip(\
            ["version", "measurement_info", "fom", "raw_arrays", \
            "intermediate_arrays", "function_parameters"], \
            [version, info, FOMs, rawData, interData, params])])
        pickle.dump(saveDict, pckfile)
        

for fn in os.listdir(optfolder):
    if not fn.endswith('.pck') or not '1059' in fn or 'MOD' in fn:
        continue
    
    p2=os.path.join(optfolder, fn)
    tup=loadPckKeys(p2, keys=['measurement_info', "fom", 'raw_arrays', 'intermediate_arrays'])
    infod, fomd, rawd, interd=tup
    
    sf=1.01
    
    datakey='Transmittance_0'
    
   
    darkdata=interd['Dark']
    srdata=interd['SpectralReference']*sf
    interd['Transmission']=(interd[datakey]-darkdata)/(srdata-darkdata)
    interd['Transmission_t']=numpy.array([(arr-darkdata)/(srdata-darkdata) for arr in interd[datakey+'_t']])
    
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
    
    nptsoneside, order, binprior=(8, 2, 0)
    for j in range(len(interd['Transmission_t'])):
        interd['Transmission_t'][j]=savgolsmooth(interd['Transmission_t'][j], nptsoneside=nptsoneside, order = order, binprior=binprior)
    
    optavetrans=interd['AveAM15Trans_380_900_t']
    
    savePck(optfolder, fn.replace('.pck', '_MOD'),  info=infod, rawData=rawd, interData=interd, FOMs=fomd)

for fn in os.listdir(echemfolder):
    if not fn.endswith('.pck') or not '1059' in fn or 'MOD' in fn:
        continue
    
    p2=os.path.join(echemfolder, fn)
    tup=loadPckKeys(p2, keys=['measurement_info', "fom", 'raw_arrays', 'intermediate_arrays'])
    infod, fomd, rawd, interd=tup

    interd['optavetrans']=optavetrans
    
    savePck(echemfolder, fn.replace('.pck', '_MOD'),  info=infod, rawData=rawd, interData=interd, FOMs=fomd)
    
