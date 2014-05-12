import os,numpy,pylab,pickle

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
        

def plotbyseg(x, y, nsegs=4, cols=['r', 'g', 'b', 'k'], **kwargs):
    a=len(x)
    b=a//2
    c=b//2
    inds_segs=[range(0, c), range(c, b), range(b, b+c), range(b+c, a)]
    for inds, c in zip(inds_segs, cols):
        pylab.plot(x[inds], y[inds], c=c, markeredgecolor=c, **kwargs)
        

for fn in os.listdir(optfolder):
    if not fn.endswith('.pck') or not '1059' in fn:
        continue
    
    p2=os.path.join(optfolder, fn)
    tup=loadPckKeys(p2, keys=['measurement_info', "fom", 'raw_arrays', 'intermediate_arrays'])
    infod, fomd, rawd, interd=tup
    
#    inds=range(len(interd['t'])//4)
#    t=interd['t'][inds]
#    tarrs=interd['Transmission_t'][inds]
#    nm=interd['nm']
#    temp=len(inds)-1
#    cols=[[1.*i/temp, 0, 1.-1.*i/temp] for i in range(len(inds))]
#    
#    pylab.figure()
#    for arr, c in zip(tarrs, cols):
#        pylab.plot(nm, arr, c=c)
    dark=interd['Dark']
    sr=interd['SpectralReference']
    trans=interd['Transmittance_0']
    
    #CV3 727
    #dgrid=zip([.95, 1., 1.05, 1.1, 1.15], ['r', 'g', 'b', 'k', 'm'])
    #sgrid=zip([.9, .95, 1., 1.05, 1.1], [':', '--', '-', '-.', ':'])
    #dgrid=zip([.95, 1., 1.05, 1.1], ['r', 'g', 'b', 'k'])
    #sgrid=zip([1., 1.05], ['-', '-.'])
#    dgrid=zip([1.07, 1.075, 1.08, 1.085], ['r', 'g', 'b', 'k'])
#    sgrid=zip([1.], ['-'])
    #CA5 727
#    dgrid=zip([.95, 1., 1.05, 1.1, 1.15], ['r', 'g', 'b', 'k', 'm'])
#    sgrid=zip([.9, .95, 1., 1.05, 1.1], [':', '--', '-', '-.', ':'])
#    dgrid=zip([.95, 1., 1.05, 1.1, 1.15], ['r', 'g', 'b', 'k', 'm'])
#    sgrid=zip([.9, .95, 1., 1.05, 1.1], [':', '--', '-', '-.', ':'])
#    dgrid=zip([1.01, 1.02, 1.03, 1.04], ['r', 'g', 'b', 'k', 'm'])
#    sgrid=zip([1.], [ '-'])

    #CV3 1059
#    dgrid=zip([.95, 1., 1.05, 1.1, 1.15], ['r', 'g', 'b', 'k', 'm'])
#    sgrid=zip([.9, .95, 1., 1.05, 1.1], [':', '--', '-', '-.', ':'])
#    dgrid=zip([1., 1.01, 1.02, 1.03, 1.04], ['r', 'g', 'b', 'k', 'm'])
#    sgrid=zip([1., 1.01, 1.02, 1.03, 1.04], [':', '--', '-', '-.', ':'])
    dgrid=zip([1., ], ['r'])
    sgrid=zip([1., 1.01, 1.015, 1.02], [':', '--', '-', '-.'])
    
    for df, col in dgrid:
        for sf, style in sgrid:
            t=(trans-dark*df)/(sr*sf-dark*df)
            pylab.plot(t, col+style)
            
pylab.plot(interd['Transmission'], 'y')
pylab.ylim(.2, 1.1)
pylab.show()
