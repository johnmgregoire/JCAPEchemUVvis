from pck_opt_withechem_FCN import *
from combine_opt_eche_pcks import *

##*****************************
#print 'STARTING 9997 as prep 1 s spectra'
#folder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/9997_asprep'
#savefolder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/9997_optpck_asprep'
#savefolderechem=None
#filterstr1='_OCV0'
#
#darkfilterstr=['DARK%d_' %i for i in range(5, 20)]
#datafilterstr=['TRANS1_','TRANS2_']
#
#for partname in ['part1', 'part2', 'part3']:
#    optandeche_folder(os.path.join(folder, partname), savefolder, savefolderechem, filterstr1, filterstr1, datafilterstr=datafilterstr, darkfilterstr=darkfilterstr, testonly=False)
#
#darkfilterstr=['DARK%d_' %i for i in range(5, 40)]
#datafilterstr=['TRANS1_']
#partname='partswith0.5s'
#optandeche_folder(os.path.join(folder, partname), savefolder, savefolderechem, filterstr1, filterstr1, datafilterstr=datafilterstr, darkfilterstr=darkfilterstr, testonly=False)
#
###trying to use backup plan for  Sample2104_x-124_y-18_A0B0C0D0 ['TRANS1_']
###not right files for  Sample2104_x-124_y-18_A0B0C0D0 ['TRANS2_']
###trying to use backup plan for  Sample874_x-95_y-56_A10B10C65D15 ['TRANS1_']
###not right files for  Sample874_x-95_y-56_A10B10C65D15 ['TRANS2_']
###trying to use backup plan for  Sample2104_x-124_y-18_A0B0C0D0 ['TRANS1_']
###not right files for  Sample2104_x-124_y-18_A0B0C0D0 ['TRANS2_']


##*****************************
#print 'STARTING 10157 as prep 0.5 s spectra'
#folder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/10157_asprep'
#savefolder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/10157_optpck_asprep'
#savefolderechem=None
#filterstr1='_OCV0'
#
#darkfilterstr=['DARK%d_' %i for i in range(5, 40)]
#datafilterstr=['TRANS1_','TRANS2_']
#
#for partname in ['part1', 'part2']:
#    optandeche_folder(os.path.join(folder, partname), savefolder, savefolderechem, filterstr1, filterstr1, datafilterstr=datafilterstr, darkfilterstr=darkfilterstr, testonly=False)

##*****************************
#print 'STARTING 9997 CA6 1s and 0.5s spectra'
#folder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/9997_CA6'
#savefolder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/9997_optpck_CA6'
#savefolderechem='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/9997_echempck_CA6'
#filterstr1='_CA6'
#
#darkfilterstr=['DARK%d_' %i for i in range(5, 20)]
#datafilterstr=['TRANS8_','TRANS9_','TRANS10_']
#
#partname='9997_CA6_part1_1s'
#optandeche_folder(os.path.join(folder, partname), savefolder, savefolderechem, filterstr1, filterstr1, datafilterstr=datafilterstr, darkfilterstr=darkfilterstr, numCApts=25, testonly=False)
#
#darkfilterstr=['DARK%d_' %i for i in range(5, 40)]
#datafilterstr=['TRANS14_','TRANS15_','TRANS16_', 'TRANS17_','TRANS18_','TRANS19_']
#
#partname='9997_CA6_part2_0.5s'
#optandeche_folder(os.path.join(folder, partname), savefolder, savefolderechem, filterstr1, filterstr1, datafilterstr=datafilterstr, darkfilterstr=darkfilterstr, numCApts=25, testonly=False)
#
###trying to use backup plan for  Sample664_x-59_y-62_A0B0C0D0 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample1544_x-26_y-34_A0B0C0D0 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample543_x-73_y-66_A55B5C30D10 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample75_x-32_y-80_A50B0C50D0 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample664_x-59_y-62_A0B0C0D0 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample663_x-57_y-62_A10B65C15D10 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample662_x-55_y-62_A10B70C10D10 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample661_x-53_y-62_A10B75C5D10 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample660_x-51_y-62_A10B80C0D10 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample659_x-49_y-62_A15B0C75D10 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample658_x-47_y-62_A15B5C70D10 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample657_x-45_y-62_A15B10C65D10 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample656_x-43_y-62_A0B0C0D0 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample655_x-41_y-62_A15B15C60D10 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample1557_x-53_y-34_A15B40C5D40 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample1556_x-51_y-34_A15B45C0D40 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample1555_x-49_y-34_A20B0C40D40 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample1554_x-47_y-34_A20B5C35D40 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample1553_x-45_y-34_A20B10C30D40 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample1551_x-41_y-34_A20B15C25D40 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample1550_x-39_y-34_A20B20C20D40 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample1549_x-37_y-34_A20B25C15D40 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample1548_x-34_y-34_A20B30C10D40 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample1547_x-32_y-34_A20B35C5D40 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample1546_x-30_y-34_A20B40C0D40 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample1545_x-28_y-34_A25B0C35D40 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample1544_x-26_y-34_A0B0C0D0 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample1543_x-24_y-34_A25B5C30D40 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample1542_x-22_y-34_A25B10C25D40 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample1541_x-20_y-34_A25B15C20D40 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample1540_x-18_y-34_A25B20C15D40 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample1539_x-16_y-34_A25B25C10D40 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample1538_x-14_y-34_A25B30C5D40 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']
###trying to use backup plan for  Sample1537_x-12_y-34_A25B35C0D40 ['TRANS14_', 'TRANS15_', 'TRANS16_', 'TRANS17_', 'TRANS18_', 'TRANS19_']

##*****************************
#print 'STARTING 10157 CA1 and CA6 '
#folder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/10157_CA1CA6'
#savefolderstart='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/10157_optpck'
#savefolderechemstart='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/10157_echempck'
#mainfiltlist=['_CA1', '_CA6']
#
#
#darkfilterstr=['DARK%d_' %i for i in range(5, 20)]
#
#datafilterstr1=['TRANS5_','TRANS6_']
#datafilterstr2=['TRANS8_','TRANS9_']
#
#
#for filterstr1, datafilterstr, npts in zip(mainfiltlist, [datafilterstr1, datafilterstr2], [10, 25]):
#    for partname in ['part3']:
#        savefolder=savefolderstart+filterstr1
#        savefolderechem=savefolderechemstart+filterstr1
#        optandeche_folder(os.path.join(folder, partname), savefolder, savefolderechem, filterstr1, filterstr1, datafilterstr=datafilterstr, darkfilterstr=darkfilterstr, numCApts=npts, testonly=False)

##part1:
##    trying to use backup plan for  Sample1804_x-35_y-26_A35B30C25D10 ['TRANS5_', 'TRANS6_']
##trying to use backup plan for  Sample1666_x-14_y-30_A15B30C40D15 ['TRANS5_', 'TRANS6_']
##trying to use backup plan for  Sample1270_x-120_y-44_A30B20C40D10 ['TRANS5_', 'TRANS6_']
##trying to use backup plan for  Sample1826_x-79_y-26_A25B35C25D15 ['TRANS8_', 'TRANS9_']
##trying to use backup plan for  Sample1819_x-65_y-26_A10B20C60D10 ['TRANS8_', 'TRANS9_']
##trying to use backup plan for  Sample1815_x-57_y-26_A55B5C40D0 ['TRANS8_', 'TRANS9_']
##trying to use backup plan for  Sample1810_x-47_y-26_A35B10C35D20 ['TRANS8_', 'TRANS9_']
##trying to use backup plan for  Sample1806_x-39_y-26_A60B5C30D5 ['TRANS8_', 'TRANS9_']
##trying to use backup plan for  Sample1805_x-37_y-26_A0B10C20D70 ['TRANS8_', 'TRANS9_']
##trying to use backup plan for  Sample1559_x-57_y-34_A5B15C65D15 ['TRANS8_', 'TRANS9_']
##trying to use backup plan for  Sample1453_x-102_y-38_A30B20C30D20 ['TRANS8_', 'TRANS9_']
##trying to use backup plan for  Sample1447_x-89_y-38_A75B5C5D15 ['TRANS8_', 'TRANS9_']


##  **********************************
#print 'STARTING 10157 combine optP, CA1, CA6'
#folder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/10157_optpck'
#savefolderstart='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/10157_optpck'
#asprepfolder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/10157_optpck_asprep'
#mainfiltlist=['_CA1','_CA6']
#def addtl_fom_calcfcn(fomd):
#    #fomd['CA2vCA1_AM15Trans']=fomd['CA2_AveAM15Trans_380_900']/fomd['CA1_AveAM15Trans_380_900']
#    fomd['CA6vCA1_AM15Trans']=fomd['CA6_AveAM15Trans_380_900']/fomd['CA1_AveAM15Trans_380_900']
#    #fomd['CA5vCA2_AM15Trans']=fomd['CA5_AveAM15Trans_380_900']/fomd['CA2_AveAM15Trans_380_900']
#    fomd['CA6vAP_AM15Trans']=fomd['CA6_AveAM15Trans_380_900']/fomd['AveAM15Trans_380_900']
#    #fomd['CA2vAP_AM15Trans']=fomd['CA2_AveAM15Trans_380_900']/fomd['AveAM15Trans_380_900']
#    fomd['CA1vAP_AM15Trans']=fomd['CA1_AveAM15Trans_380_900']/fomd['AveAM15Trans_380_900']
#
#combinepcks(folder, savefolderstart, mainfiltlist, asprepfolder, addtl_fom_calcfcn=addtl_fom_calcfcn)    


##  **********************************
#print 'STARTING 9997 CA1,2,5 '
#mainfiltlist=['_CA1', '_CA2', '_CA5']
#folder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/9997_CAs'
#savefolderstart='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/9997_optpck'
#savefolderechemstart='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/9997_echempck'
#
#darkfilterstr=['DARK%d_' %i for i in range(5, 20)]
#
#datafilterstr1=['TRANS5_','TRANS6_']
##datafilterstr2=['TRANS8_','TRANS9_']
#
#
#for filterstr1, datafilterstr in zip(mainfiltlist, [datafilterstr1, datafilterstr1, datafilterstr1]):
#    savefolder=savefolderstart+filterstr1
#    savefolderechem=savefolderechemstart+filterstr1
#    optandeche_folder(folder, savefolder, savefolderechem, filterstr1, filterstr1, datafilterstr=datafilterstr, darkfilterstr=darkfilterstr, numCApts=10, testonly=False)
###
###trying to use backup plan for  Sample951_x-122_y-54_A45B25C10D20 ['TRANS5_', 'TRANS6_']
###
###
###trying to use backup plan for  Sample1154_x-14_y-46_A30B0C45D25 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample1153_x-12_y-46_A30B5C40D25 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample1101_x-37_y-48_A60B5C10D25 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample1030_x-22_y-50_A15B25C40D20 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample1026_x-14_y-50_A15B45C20D20 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample961_x-12_y-52_A40B30C10D20 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample978_x-47_y-52_A35B5C40D20 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample934_x-87_y-54_A55B25C0D20 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample927_x-73_y-54_A65B0C15D20 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample925_x-69_y-54_A65B10C5D20 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample918_x-55_y-54_A75B5C0D20 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample917_x-53_y-54_A80B0C0D20 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample914_x-47_y-54_A0B10C75D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample913_x-45_y-54_A0B15C70D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample911_x-41_y-54_A0B20C65D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample910_x-39_y-54_A0B25C60D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample908_x-34_y-54_A0B35C50D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample906_x-30_y-54_A0B45C40D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample903_x-24_y-54_A0B55C30D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample901_x-20_y-54_A0B65C20D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample900_x-18_y-54_A0B70C15D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample898_x-14_y-54_A0B80C5D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample897_x-12_y-54_A0B85C0D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample837_x-20_y-56_A20B15C50D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample838_x-22_y-56_A20B10C55D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample844_x-34_y-56_A15B60C10D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample863_x-73_y-56_A10B55C20D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample868_x-83_y-56_A10B35C40D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample831_x-138_y-58_A20B40C25D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample830_x-136_y-58_A20B45C20D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample805_x-85_y-58_A30B20C35D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample799_x-73_y-58_A30B45C10D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample798_x-71_y-58_A30B50C5D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample797_x-69_y-58_A30B55C0D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample796_x-67_y-58_A35B0C50D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample795_x-65_y-58_A35B5C45D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample793_x-61_y-58_A35B15C35D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample788_x-51_y-58_A35B35C15D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample783_x-41_y-58_A40B0C45D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample775_x-24_y-58_A40B35C10D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample773_x-20_y-58_A40B45C0D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample772_x-18_y-58_A45B0C40D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample771_x-16_y-58_A45B5C35D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample769_x-12_y-58_A45B15C25D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample705_x-12_y-60_A0B70C20D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample716_x-34_y-60_A0B20C70D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample729_x-61_y-60_A70B15C0D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample733_x-69_y-60_A65B20C0D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample734_x-71_y-60_A65B15C5D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample737_x-77_y-60_A65B5C15D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample739_x-81_y-60_A60B25C0D15 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample687_x-106_y-62_A5B50C35D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample684_x-99_y-62_A5B65C20D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample669_x-69_y-62_A10B40C40D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample667_x-65_y-62_A10B50C30D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample666_x-63_y-62_A10B55C25D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample662_x-55_y-62_A10B70C10D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample659_x-49_y-62_A15B0C75D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample651_x-32_y-62_A15B35C40D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample647_x-24_y-62_A15B50C25D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample646_x-22_y-62_A15B55C20D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample643_x-16_y-62_A15B70C5D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample641_x-12_y-62_A20B0C70D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample583_x-24_y-64_A35B40C15D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample587_x-32_y-64_A35B25C30D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample593_x-45_y-64_A35B0C55D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample601_x-61_y-64_A30B30C30D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample607_x-73_y-64_A30B0C60D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample611_x-81_y-64_A25B55C10D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample617_x-93_y-64_A25B30C35D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample623_x-106_y-64_A25B0C65D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample626_x-112_y-64_A20B65C5D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample575_x-138_y-66_A40B15C35D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample572_x-132_y-66_A40B30C20D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample570_x-128_y-66_A40B40C10D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample567_x-122_y-66_A40B50C0D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample562_x-112_y-66_A45B20C25D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample559_x-106_y-66_A45B30C15D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample542_x-71_y-66_A55B10C25D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample540_x-67_y-66_A55B20C15D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample539_x-65_y-66_A55B25C10D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample538_x-63_y-66_A55B30C5D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample537_x-61_y-66_A55B35C0D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample532_x-51_y-66_A60B15C15D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample530_x-47_y-66_A60B25C5D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample529_x-45_y-66_A60B30C0D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample525_x-37_y-66_A65B10C15D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample522_x-30_y-66_A65B25C0D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample519_x-24_y-66_A70B5C15D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample518_x-22_y-66_A70B10C10D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample515_x-16_y-66_A75B0C15D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample449_x-12_y-68_A10B45C40D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample453_x-20_y-68_A10B25C60D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample458_x-30_y-68_A10B5C80D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample460_x-34_y-68_A5B90C0D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample462_x-39_y-68_A5B80C10D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample463_x-41_y-68_A5B75C15D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample465_x-45_y-68_A5B70C20D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample467_x-49_y-68_A5B60C30D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample479_x-73_y-68_A5B5C85D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample483_x-81_y-68_A0B90C5D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample489_x-93_y-68_A0B65C30D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample491_x-97_y-68_A0B55C40D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample494_x-103_y-68_A0B40C55D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample505_x-126_y-68_A90B0C0D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample506_x-128_y-68_A85B5C0D10 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample445_x-134_y-70_A10B60C25D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample434_x-112_y-70_A15B20C60D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample431_x-106_y-70_A15B30C50D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample427_x-97_y-70_A15B50C30D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample425_x-93_y-70_A15B60C20D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample423_x-89_y-70_A15B65C15D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample422_x-87_y-70_A15B70C10D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample421_x-85_y-70_A15B75C5D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample415_x-73_y-70_A20B15C60D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample414_x-71_y-70_A20B20C55D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample412_x-67_y-70_A20B30C45D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample406_x-55_y-70_A20B55C20D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample404_x-51_y-70_A20B65C10D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample403_x-49_y-70_A20B70C5D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample402_x-47_y-70_A20B75C0D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample401_x-45_y-70_A25B0C70D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample397_x-37_y-70_A25B15C55D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample396_x-34_y-70_A25B20C50D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample395_x-32_y-70_A25B25C45D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample394_x-30_y-70_A25B30C40D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample393_x-28_y-70_A25B35C35D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample391_x-24_y-70_A25B40C30D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample390_x-22_y-70_A25B45C25D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample387_x-16_y-70_A25B60C10D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample386_x-14_y-70_A25B65C5D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample322_x-14_y-72_A50B20C25D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample324_x-18_y-72_A50B10C35D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample325_x-20_y-72_A50B5C40D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample329_x-28_y-72_A45B45C5D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample330_x-30_y-72_A45B40C10D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample331_x-32_y-72_A45B35C15D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample332_x-34_y-72_A45B30C20D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample333_x-37_y-72_A45B25C25D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample335_x-41_y-72_A45B15C35D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample338_x-47_y-72_A45B5C45D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample340_x-51_y-72_A40B55C0D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample348_x-67_y-72_A40B20C35D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample353_x-77_y-72_A40B0C55D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample354_x-79_y-72_A35B60C0D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample359_x-89_y-72_A35B35C25D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample363_x-97_y-72_A35B20C40D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample364_x-99_y-72_A35B15C45D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample377_x-126_y-72_A30B30C35D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample319_x-138_y-74_A50B30C15D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample318_x-136_y-74_A50B35C10D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample314_x-128_y-74_A55B5C35D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample311_x-122_y-74_A55B15C25D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample294_x-87_y-74_A65B5C25D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample287_x-73_y-74_A70B0C25D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample284_x-67_y-74_A70B15C10D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample277_x-53_y-74_A75B15C5D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample274_x-47_y-74_A80B5C10D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample269_x-37_y-74_A85B5C5D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample268_x-34_y-74_A85B10C0D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample267_x-32_y-74_A90B0C5D5 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample262_x-22_y-74_A0B5C95D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample257_x-12_y-74_A0B30C70D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample193_x-12_y-76_A15B10C75D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample196_x-18_y-76_A10B90C0D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample197_x-20_y-76_A10B85C5D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample199_x-24_y-76_A10B75C15D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample203_x-32_y-76_A10B60C30D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample215_x-57_y-76_A10B5C85D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample220_x-67_y-76_A5B85C10D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample223_x-73_y-76_A5B70C25D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample226_x-79_y-76_A5B60C35D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample250_x-128_y-76_A0B60C40D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample191_x-138_y-78_A15B15C70D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample183_x-122_y-78_A15B50C35D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample175_x-106_y-78_A15B85C0D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample174_x-103_y-78_A20B0C80D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample172_x-99_y-78_A20B10C70D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample169_x-93_y-78_A20B25C55D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample167_x-89_y-78_A20B30C50D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample166_x-87_y-78_A20B35C45D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample163_x-81_y-78_A20B50C30D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample161_x-77_y-78_A20B60C20D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample159_x-73_y-78_A20B65C15D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample158_x-71_y-78_A20B70C10D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample150_x-55_y-78_A25B20C55D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample148_x-51_y-78_A25B30C45D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample146_x-47_y-78_A25B40C35D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample145_x-45_y-78_A25B45C30D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample142_x-39_y-78_A25B55C20D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample141_x-37_y-78_A25B60C15D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample139_x-32_y-78_A25B70C5D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample138_x-30_y-78_A25B75C0D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample132_x-18_y-78_A30B20C50D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample131_x-16_y-78_A30B25C45D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample130_x-14_y-78_A30B30C40D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample129_x-12_y-78_A30B35C35D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample65_x-12_y-80_A50B45C5D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample68_x-18_y-80_A50B30C20D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample71_x-24_y-80_A50B15C35D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample74_x-30_y-80_A50B5C45D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample75_x-32_y-80_A50B0C50D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample81_x-45_y-80_A45B35C20D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample87_x-57_y-80_A45B5C50D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample91_x-65_y-80_A40B55C5D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample94_x-71_y-80_A40B40C20D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample95_x-73_y-80_A40B35C25D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample125_x-134_y-80_A30B50C20D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample50_x-112_y-82_A60B5C35D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample49_x-110_y-82_A60B10C30D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample47_x-106_y-82_A60B15C25D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample38_x-87_y-82_A65B10C25D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample36_x-83_y-82_A65B20C15D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample30_x-71_y-82_A70B5C25D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample26_x-63_y-82_A70B25C5D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample20_x-51_y-82_A75B15C10D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample18_x-47_y-82_A75B25C0D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample15_x-41_y-82_A80B5C15D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample11_x-32_y-82_A85B0C15D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample10_x-30_y-82_A85B5C10D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample5_x-20_y-82_A90B5C5D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample3_x-16_y-82_A95B0C5D0 ['TRANS5_', 'TRANS6_']
###trying to use backup plan for  Sample2_x-14_y-82_A95B5C0D0 ['TRANS5_', 'TRANS6_']

#  **********************************
print 'STARTING 9997 combine optP, CA1, CA6. ignore CA2 and CA 5 because the echem is bad'
folder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/9997_optpck'
savefolderstart='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/9997_optpck'
asprepfolder='C:/Users/Gregoire/Documents/CaltechWork/echemuvvis/transmittance_potential/9997_optpck_asprep'
mainfiltlist=['_CA1','_CA6']
def addtl_fom_calcfcn(fomd):
    #fomd['CA2vCA1_AM15Trans']=fomd['CA2_AveAM15Trans_380_900']/fomd['CA1_AveAM15Trans_380_900']
    fomd['CA6vCA1_AM15Trans']=fomd['CA6_AveAM15Trans_380_900']/fomd['CA1_AveAM15Trans_380_900']
    #fomd['CA5vCA2_AM15Trans']=fomd['CA5_AveAM15Trans_380_900']/fomd['CA2_AveAM15Trans_380_900']
    fomd['CA6vAP_AM15Trans']=fomd['CA6_AveAM15Trans_380_900']/fomd['AveAM15Trans_380_900']
    #fomd['CA2vAP_AM15Trans']=fomd['CA2_AveAM15Trans_380_900']/fomd['AveAM15Trans_380_900']
    fomd['CA1vAP_AM15Trans']=fomd['CA1_AveAM15Trans_380_900']/fomd['AveAM15Trans_380_900']

combinepcks(folder, savefolderstart, mainfiltlist, asprepfolder, addtl_fom_calcfcn=addtl_fom_calcfcn)    
