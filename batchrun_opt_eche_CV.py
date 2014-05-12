from pck_opt_echem_vstime_FCN import *
from combine_opt_eche_pcks import *

###*****************************
print 'STARTING 10157 CV3 0.5 s spectra'
folder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/10157_CV3'
savefolder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/10157_optpck_CV3'
savefolderechem='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/10157_echempck_CV3'
filterstr1='_CV3'

darkfilterstr=['DARK%d_' %i for i in range(5, 40)]
#datafilterstr=['TRANS%d_' %i for i in range(1, 142)]
datafilterstr='_TRANS'
optandeche_folder(folder, savefolder, savefolderechem, filterstr1, filterstr1, datafilterstr=datafilterstr, darkfilterstr=darkfilterstr, numCApts=0, echemSGnpts_o_bin=(9, 3, 4), optSGnpts_o_bin=(8, 2, 0), testonly=False,darkmult=1.064, numcvsegs=4)



###*****************************
#print 'STARTING 10157 CA5 1s spectra'
#folder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/10157_CA5'
#savefolder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/10157_optpck_CA5'
#savefolderechem='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/10157_echempck_CA5'
#filterstr1='_CA5'
#
#darkfilterstr=['DARK%d_' %i for i in range(5, 23)]
##datafilterstr=['TRANS%d_' %i for i in range(1, 142)]
#datafilterstr='_TRANS'
#optandeche_folder(folder, savefolder, savefolderechem, filterstr1, filterstr1, datafilterstr=datafilterstr, darkfilterstr=darkfilterstr, numCApts=0, echemSGnpts_o_bin=(4, 1, 0), optSGnpts_o_bin=(8, 2, 0), testonly=False, darkmult=1.019)
#
