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


#pylab.figure(figsize=(4.2, 3.6))
#fcn=lambda i:pylab.subplot(2, 2, i+1)
#axl=[fcn(i) for i in range(4)]
#
#for count, (ax, smp) in enumerate(zip(axl, [1059, 727, 1457, 1284])):
#    for fn in os.listdir(echemfolder):
#        if not fn.endswith('.pck') or not `smp` in fn:
#            continue
#        
#        p2=os.path.join(echemfolder, fn)
#        tup=loadPckKeys(p2, keys=['measurement_info', "fom", 'raw_arrays', 'intermediate_arrays'])
#        infod, fomd, rawd, interd=tup
#        
#
#        pylab.axes(ax)
#        plotbyseg((rawd['Ewe(V)']+vsh)*1000., interd['I(A)_SG']*1.e5)
#        if count==2:
#            pylab.ylabel('Current (mA/cm$^2$)', fontsize=11)
#            pylab.xlabel('$\eta$, OER overpotential (mV)', fontsize=11)
#        
#        pylab.xlim(40, 395)
#        pylab.ylim(-7, 60)
#        if count in [0, 1]:
#            for xlabel_i in ax.axes.get_xticklabels():
#                xlabel_i.set_visible(False)
#                xlabel_i.set_fontsize(0.0)
#        if count in [1, 3]:
#            for ylabel_i in ax.axes.get_yticklabels():
#                ylabel_i.set_visible(False)
#                ylabel_i.set_fontsize(0.0)
#                
#        ax2=pylab.twinx()
#        plotbyseg((interd['Ewe(V)_opt']+vsh)*1000., interd['optavetrans'], marker='.', linestyle='None')
#        if count==3:
#            pylab.ylabel('Transmission Efficiency', fontsize=11)
#        
#        
#        pylab.ylim(.5, .9)
#        pylab.xlim(40, 395)
#        
#        if count in [0, 2]:
#            for ylabel_i in ax2.axes.get_yticklabels():
#                ylabel_i.set_visible(False)
#                ylabel_i.set_fontsize(0.0)
#pylab.subplots_adjust(left=.15, right=.82, hspace=0.0, wspace=0.02, bottom=.16, top=.92)
#pylab.savefig(os.path.join(savefolder, 'IEffvsV_4samples.png'))
#pylab.savefig(os.path.join(savefolder, 'IEffvsV_4samples.eps'))
#
#pylab.figure(figsize=(4.2, 3.6))
#cols=[(.4, .4, .4), (.4, .4, .4),'r', 'g', 'b', 'k']
#labs=['Trans. Eff.', 'Current', '1st anodic', '1st cathodic', '2nd anodic', '2nd cathodic']
#
#for count, (c, l) in enumerate(zip(cols, labs)):
#    if count==0:
#        s='.'
#    else:
#        s='-'
#    pylab.plot([], [], s, c=c, label=l)
#pylab.legend()
#pylab.savefig(os.path.join(savefolder, 'IEffvsV_legend.png'))
#pylab.savefig(os.path.join(savefolder, 'IEffvsV_legend.eps'))


pylab.figure(figsize=(4.2, 3.6))
fcn=lambda i:pylab.subplot(1, 2, i+1)
axl=[fcn(i) for i in range(2)]

for count, (ax, smp) in enumerate(zip(axl, [1059, 727])):
    for fn in os.listdir(echemfolder):
        if not fn.endswith('.pck') or not `smp` in fn:
            continue
    
        p2=os.path.join(optfolder, fn)
        tup=loadPckKeys(p2, keys=['measurement_info', "fom", 'raw_arrays', 'intermediate_arrays'])
        infod, fomd, rawd, interd=tup
        
        inds=range(int(numpy.ceil(len(interd['t'])/4.)))
        t=interd['t'][inds]
        tarrs=interd['Transmission_t'][inds]
        nm=interd['nm']
        temp=len(inds)-1
        cols=[[1.*i/temp, 0, 1.-1.*i/temp] for i in range(len(inds))]
        
        pylab.axes(ax)
        for arr, c in zip(tarrs, cols):
            pylab.plot(nm, arr, c=c)
        pylab.xlim(380, 900)
        pylab.ylim(.35, .95)
        
        if count==0:
            pylab.ylabel('Spectral Transmission')
            pylab.xlabel('Wavelength (nm)')
        if count in [1]:
            for ylabel_i in ax.axes.get_yticklabels():
                ylabel_i.set_visible(False)
                ylabel_i.set_fontsize(0.0)
        
pylab.subplots_adjust(left=.15, right=.94, hspace=0.0, wspace=0.02, bottom=.16, top=.92)
pylab.savefig(os.path.join(savefolder, 'Tvsnmstack_2samples.png'))
pylab.savefig(os.path.join(savefolder, 'Tvsnmstack_2samples.eps'))
pylab.show()
