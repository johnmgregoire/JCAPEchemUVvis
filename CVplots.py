import os,numpy,pylab,pickle

echemfolder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/10157_echempck_CV3'
optfolder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/10157_optpck_CV3'
savefolder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/imagesandsummary/10157_CV3'

vsh=-0.125
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
        
for fn in os.listdir(echemfolder):
    if not fn.endswith('.pck'):
        continue
    
    p2=os.path.join(echemfolder, fn)
    tup=loadPckKeys(p2, keys=['measurement_info', "fom", 'raw_arrays', 'intermediate_arrays'])
    infod, fomd, rawd, interd=tup
    pylab.figure()
    
#    pylab.subplot(211)
#    pylab.title(fn)
#    pylab.plot(interd['opttimes'], interd['optavetrans'])
#    pylab.subplot(212)
#    pylab.plot(interd['Ewe(V)_opt'], interd['optavetrans'])
    pylab.title(fn)
    
    plotbyseg((rawd['Ewe(V)']+vsh)*1000., interd['I(A)_SG']*1.e5)
    pylab.ylabel('Current (mA/cm$^2$)')
    pylab.xlabel('$\eta$, OER overpotential (mV)')
    ax2=pylab.twinx()
    plotbyseg((interd['Ewe(V)_opt']+vsh)*1000., interd['optavetrans'], marker='.')
    pylab.ylabel('Transmission Efficiency')
    pylab.savefig(os.path.join(savefolder, fn.replace('.pck', '_IEffvsV.png')))
    pylab.savefig(os.path.join(savefolder, fn.replace('.pck', '_IEffvsV.eps')))
    #print len(interd['opttimes']), len(interd['optavetrans'])
    
#pylab.show()


for fn in os.listdir(optfolder):
    if not fn.endswith('.pck'):
        continue
    
    p2=os.path.join(optfolder, fn)
    tup=loadPckKeys(p2, keys=['measurement_info', "fom", 'raw_arrays', 'intermediate_arrays'])
    infod, fomd, rawd, interd=tup
    
    inds=range(len(interd['t'])//4)
    t=interd['t'][inds]
    tarrs=interd['Transmission_t'][inds]
    nm=interd['nm']
    temp=len(inds)-1
    cols=[[1.*i/temp, 0, 1.-1.*i/temp] for i in range(len(inds))]
    
    pylab.figure()
    for arr, c in zip(tarrs, cols):
        pylab.plot(nm, arr, c=c)
    pylab.title(fn)
    pylab.ylabel('Spectral Transmission')
    pylab.xlabel('Wavelength (nm)')
    pylab.savefig(os.path.join(savefolder, fn.replace('.pck', '_Tvsnmstack.png')))
    pylab.savefig(os.path.join(savefolder, fn.replace('.pck', '_Tvsnmstack.eps')))
