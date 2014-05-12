import os,numpy,pylab,pickle

echemfolder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/10157_echempck_CA5'
optfolder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/10157_optpck_CA5'
savefolder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/imagesandsummary/10157_CA5'

vsh=-0.095
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
        

        
for fn in os.listdir(echemfolder):
    if not fn.endswith('.pck'):
        continue
    
    p2=os.path.join(echemfolder, fn)
    tup=loadPckKeys(p2, keys=['measurement_info', "fom", 'raw_arrays', 'intermediate_arrays'])
    infod, fomd, rawd, interd=tup
    pylab.figure()
    

    pylab.title(fn)
    
    pylab.plot((rawd['t(s)']), interd['I(A)_SG']*1.e5)
    pylab.ylabel('Current (mA/cm$^2$)')
    pylab.xlabel('time (s)')
    ax2=pylab.twinx()
    pylab.plot((interd['t(s)_opt']), interd['optavetrans'], 'g-',  marker='.')
    pylab.ylabel('Transmission Efficiency')
    pylab.savefig(os.path.join(savefolder, fn.replace('.pck', '_IEffvst.png')))
    pylab.savefig(os.path.join(savefolder, fn.replace('.pck', '_IEffvst.eps')))
    #print len(interd['opttimes']), len(interd['optavetrans'])
    
#pylab.show()

