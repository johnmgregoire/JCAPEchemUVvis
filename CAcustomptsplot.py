import os,numpy,pylab,pickle

echemfolder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/10157_echempck_CA5'
optfolder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/10157_optpck_CA5'
savefolder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/imagesandsummary/10157_CA5'

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
        


pylab.figure(figsize=(4.2, 3.6))
fcn=lambda i:pylab.subplot(2, 1, i+1)
axl=[fcn(i) for i in range(2)]

for count, (ax, smp) in enumerate(zip(axl, [1457, 727])):
    for fn in os.listdir(echemfolder):
        if not fn.endswith('.pck') or not `smp` in fn:
            continue
    
        p2=os.path.join(echemfolder, fn)
        tup=loadPckKeys(p2, keys=['measurement_info', "fom", 'raw_arrays', 'intermediate_arrays'])
        infod, fomd, rawd, interd=tup

        
        pylab.axes(ax)

        pylab.plot((rawd['t(s)']), interd['I(A)_SG']*1.e5)
        
        pylab.ylim(0, 25)
        if count==1:
            pylab.ylabel('Current (mA/cm$^2$)')
            pylab.xlabel('time (s)')
            
        ax2=pylab.twinx()
        pylab.plot((interd['t(s)_opt']), interd['optavetrans'], 'g-',  marker='.')
        
        
        pylab.xlim(-1, 181)
        pylab.ylim(.5, .6)
        
        if count==1:
            pylab.ylabel('Transmission Efficiency')
        if count in [0]:
            for xlabel_i in ax.axes.get_xticklabels():
                xlabel_i.set_visible(False)
                xlabel_i.set_fontsize(0.0)
        
pylab.subplots_adjust(left=.15, right=.83, hspace=0.0, wspace=0.02, bottom=.16, top=.92)
pylab.savefig(os.path.join(savefolder, 'IEffvst_2samples.png'))
pylab.savefig(os.path.join(savefolder, 'IEffvst_2samples.eps'))
pylab.show()
