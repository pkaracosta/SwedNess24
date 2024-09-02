#!/usr/bin/env python3
# Automatically generated file. 
# Format:    Python script code
# McStas <http://www.mcstas.org>
# Instrument: Radiography_Lithium_Battery.instr (Radiography_absorbing_edge)
# Date:       Wed Sep  6 07:20:12 2023
# File:       Radiography_Lithium_Battery_generated.py

import mcstasscript as ms

# Python McStas instrument description
instr = ms.McStas_instr("Radiography_absorbing_edge_generated", author = "McCode Py-Generator", origin = "ESS DMSC")

# Add collected DEPENDENCY strings
instr.set_dependency(' -I@MCCODE_LIB@/share/ -DFUNNEL ')

# *****************************************************************************
# * Start of instrument 'Radiography_absorbing_edge' generated code
# *****************************************************************************
# MCSTAS system dir is "/Users/pkwi/McStas/mcstas/3.x-dev/"


# *****************************************************************************
# * instrument 'Radiography_absorbing_edge' and components DECLARE
# *****************************************************************************

# Instrument parameters:

D = instr.add_parameter('double', 'D', value=0.01, comment='Parameter type (double) added by McCode py-generator')
L = instr.add_parameter('double', 'L', value=5, comment='Parameter type (double) added by McCode py-generator')
l = instr.add_parameter('double', 'l', value=0.10, comment='Parameter type (double) added by McCode py-generator')
sample_used = instr.add_parameter('double', 'sample_used', value=0, comment='Parameter type (double) added by McCode py-generator')
battery_charge = instr.add_parameter('double', 'battery_charge', value=1.0, comment='Parameter type (double) added by McCode py-generator')

component_definition_metadata = {
}
instr.append_declare(r'''
  double L0  = 5.0;   
double thickness_one_layer_um;
double thickness_one_layer_m;
double thickness_all_layers_um;
double battery_thickness_um;
double battery_thickness_m;

double negative_foil_thickness_m;
double negative_electrode_thickness_m;
double seperator_thickness_m;
double positive_electrode_thickness_m;
double positive_foil_thickness_m;

double LiC6_inc,LiC6_abs;
double LiFePO4_inc,LiFePO4_abs;


// Remember to add generated include declare section
// declare section for battery_stack 
double number_of_layers = 10.000000;
double positive_foil_center[10];
double positive_foil_offset_um;
double positive_foil_offset_m;
double negative_foil_center[10];
double negative_foil_offset_um;
double negative_foil_offset_m;
int counter;


double battery_width;
double battery_depth;
double negative_foil_thickness_um;
double negative_electrode_thickness_um;
double seperator_thickness_um;
double positive_electrode_thickness_um;
double positive_foil_thickness_um;
double end_safety;

double sample_xoff ; /* Sample x offset */
double det_w = 0.10;
double det_h = 0.10;  
double sample_x=0.10;
double sample_y=0.10;
double sigma_inc=1e-4;/*Smallest possible value close to 0 where the absorption XS is still correctly calculated in the Incoherent component*/
double sqrt2=1.414214;         
double frac_interact=1e-6; // set to something close to zero since we don't want to look at inchorent scattering. But do not set to 0 since then the scattering from sigma_inc will be considered            

double sigma_abs=5.08;
double Vc=13.827;
double sample_z=0.01;

double Rota=90;
''')


instr.append_initialize(r'''


sample_xoff  = sample_x/2*sqrt(2); /* Sample x offset */

if (sample_used == 1){Rota = 0;}

battery_width=0.02;
battery_depth=0.01;
negative_foil_thickness_um=100;
negative_electrode_thickness_um=150;
seperator_thickness_um=80;
positive_electrode_thickness_um=190;
positive_foil_thickness_um=95;
end_safety=0.0001;

negative_foil_thickness_m=negative_foil_thickness_um * 1E-6;
negative_electrode_thickness_m=negative_electrode_thickness_um * 1E-6;
seperator_thickness_m=seperator_thickness_um * 1E-6;
positive_electrode_thickness_m=positive_electrode_thickness_um * 1E-6;
positive_foil_thickness_m=positive_foil_thickness_um * 1E-6;

// Calculate layer thickness
thickness_one_layer_um=2*negative_electrode_thickness_um+negative_foil_thickness_um+2*seperator_thickness_um+2*positive_electrode_thickness_um+positive_foil_thickness_um;
thickness_one_layer_m = thickness_one_layer_um * 1E-6;

thickness_all_layers_um=number_of_layers*thickness_one_layer_um;

// Add extra layer of seperator on top
battery_thickness_um = thickness_all_layers_um + seperator_thickness_um;
battery_thickness_m = battery_thickness_um * 1E-6;



// Li content in LiC6 part depends on charge level, and thus do the cross sections for incoherent / absorption

//LiC6 attenuation factors (inc,abs) (1.5562,118.5159)
//C6 attenuation factors (inc,abs) (0.0113,0.0397)

LiC6_inc = 0.0113 + battery_charge*(1.5562-0.0113);
LiC6_abs = 0.0397 + battery_charge*(118.5159-0.0397);

//LiFePO4 attenuation factors (inc,abs) (1.8253,100.6390)
//FePO4 attenuation factors (inc,abs) (0.0221,0.43554)

LiFePO4_inc = 1.8253 - battery_charge*(1.8253-0.0221);
LiFePO4_abs = 100.6390 - battery_charge*(100.6390-0.43554);


// Remember to add generated include initialize section
// Start of initialize for generated battery_stack
positive_foil_offset_um = seperator_thickness_um + positive_electrode_thickness_um + 0.5*positive_foil_thickness_um;
negative_foil_offset_um = 2.0*seperator_thickness_um + 2.0*positive_electrode_thickness_um + positive_foil_thickness_um + negative_electrode_thickness_um + 0.5*negative_foil_thickness_um;
positive_foil_offset_m = positive_foil_offset_um * 1E-6;
negative_foil_offset_m = negative_foil_offset_um * 1E-6;
for (counter=0;counter<number_of_layers;counter++) {
  positive_foil_center[counter] = positive_foil_offset_m + (double)counter*thickness_one_layer_m;
  negative_foil_center[counter] = negative_foil_offset_m + (double)counter*thickness_one_layer_m;
}







''')


# *****************************************************************************
# * instrument 'Radiography_absorbing_edge' TRACE
# *****************************************************************************

# Comp instance init, placement and parameters
init = instr.add_component('init','Union_init')


# Comp instance Copper_Incoherent, placement and parameters
Copper_Incoherent = instr.add_component('Copper_Incoherent','Incoherent_process')

Copper_Incoherent.sigma = '4.6701'
Copper_Incoherent.f_QE = '0'
Copper_Incoherent.gamma = '0'
Copper_Incoherent.packing_factor = '1'
Copper_Incoherent.unit_cell_volume = '100'
Copper_Incoherent.interact_fraction = '-1'
Copper_Incoherent.init = '"init"'

# Comp instance Copper_Powder, placement and parameters
Copper_Powder = instr.add_component('Copper_Powder','Powder_process')

Copper_Powder.reflections = '"Cu.laz"'
Copper_Powder.packing_factor = '1'
Copper_Powder.Vc = '0'
Copper_Powder.delta_d_d = '0'
Copper_Powder.DW = '0'
Copper_Powder.nb_atoms = '1'
Copper_Powder.d_phi = '0'
Copper_Powder.density = '0'
Copper_Powder.weight = '0'
Copper_Powder.barns = '1'
Copper_Powder.Strain = '0'
Copper_Powder.interact_fraction = '-1'
Copper_Powder.format = '{ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 }'
Copper_Powder.init = '"init"'

# Comp instance Copper, placement and parameters
Copper = instr.add_component('Copper','Union_make_material')

Copper.process_string = '"Copper_Incoherent,Copper_Powder"'
Copper.my_absorption = '32.0961'
Copper.absorber = '0'
Copper.init = '"init"'

# Comp instance LiC6_incoherent, placement and parameters
LiC6_incoherent = instr.add_component('LiC6_incoherent','Incoherent_process')

LiC6_incoherent.sigma = 'LiC6_inc'
LiC6_incoherent.f_QE = '0'
LiC6_incoherent.gamma = '0'
LiC6_incoherent.packing_factor = '1'
LiC6_incoherent.unit_cell_volume = '100'
LiC6_incoherent.interact_fraction = '-1'
LiC6_incoherent.init = '"init"'

# Comp instance LiC6_fake_powder, placement and parameters
LiC6_fake_powder = instr.add_component('LiC6_fake_powder','Powder_battery_process')

LiC6_fake_powder.reflections = '"C_battery.laz"'
LiC6_fake_powder.packing_factor = '1'
LiC6_fake_powder.Vc = '0'
LiC6_fake_powder.delta_d_d = '0'
LiC6_fake_powder.DW = '0'
LiC6_fake_powder.nb_atoms = '1'
LiC6_fake_powder.d_phi = '0'
LiC6_fake_powder.density = '0'
LiC6_fake_powder.weight = '0'
LiC6_fake_powder.barns = '1'
LiC6_fake_powder.Strain = '0'
LiC6_fake_powder.interact_fraction = '-1'
LiC6_fake_powder.temperature = '300'
LiC6_fake_powder.charge_level = 'battery_charge'
LiC6_fake_powder.format = '{ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 }'
LiC6_fake_powder.init = '"init"'

# Comp instance LiC6, placement and parameters
LiC6 = instr.add_component('LiC6','Union_make_material')

LiC6.process_string = '"LiC6_incoherent,LiC6_fake_powder"'
LiC6.my_absorption = 'LiC6_abs'
LiC6.absorber = '0'
LiC6.init = '"init"'

# Comp instance POE_incoherent, placement and parameters
POE_incoherent = instr.add_component('POE_incoherent','Incoherent_process')

POE_incoherent.sigma = '476.7338'
POE_incoherent.f_QE = '0'
POE_incoherent.gamma = '0'
POE_incoherent.packing_factor = '1'
POE_incoherent.unit_cell_volume = '100'
POE_incoherent.interact_fraction = '-1'
POE_incoherent.init = '"init"'

# Comp instance Electrolyte, placement and parameters
Electrolyte = instr.add_component('Electrolyte','Union_make_material')

Electrolyte.process_string = '"POE_incoherent"'
Electrolyte.my_absorption = '1.9862'
Electrolyte.absorber = '0'
Electrolyte.init = '"init"'

# Comp instance LiFePO4_incoherent, placement and parameters
LiFePO4_incoherent = instr.add_component('LiFePO4_incoherent','Incoherent_process')

LiFePO4_incoherent.sigma = 'LiFePO4_inc'
LiFePO4_incoherent.f_QE = '0'
LiFePO4_incoherent.gamma = '0'
LiFePO4_incoherent.packing_factor = '1'
LiFePO4_incoherent.unit_cell_volume = '100'
LiFePO4_incoherent.interact_fraction = '-1'
LiFePO4_incoherent.init = '"init"'

# Comp instance LiFePO4_powder, placement and parameters
LiFePO4_powder = instr.add_component('LiFePO4_powder','Powder_process')

LiFePO4_powder.reflections = '"LiFePO4.lau"'
LiFePO4_powder.packing_factor = '1'
LiFePO4_powder.Vc = '0'
LiFePO4_powder.delta_d_d = '0'
LiFePO4_powder.DW = '0'
LiFePO4_powder.nb_atoms = '1'
LiFePO4_powder.d_phi = '0'
LiFePO4_powder.density = '0'
LiFePO4_powder.weight = '0'
LiFePO4_powder.barns = '1'
LiFePO4_powder.Strain = '0'
LiFePO4_powder.interact_fraction = '-1'
LiFePO4_powder.format = '{ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 }'
LiFePO4_powder.init = '"init"'

# Comp instance LiFePO4, placement and parameters
LiFePO4 = instr.add_component('LiFePO4','Union_make_material')

LiFePO4.process_string = '"LiFePO4_incoherent,LiFePO4_powder"'
LiFePO4.my_absorption = 'LiFePO4_abs'
LiFePO4.absorber = '0'
LiFePO4.init = '"init"'

# Comp instance Aluminum_incoherent, placement and parameters
Aluminum_incoherent = instr.add_component('Aluminum_incoherent','Incoherent_process')

Aluminum_incoherent.sigma = '0.0494'
Aluminum_incoherent.f_QE = '0'
Aluminum_incoherent.gamma = '0'
Aluminum_incoherent.packing_factor = '1'
Aluminum_incoherent.unit_cell_volume = '100'
Aluminum_incoherent.interact_fraction = '-1'
Aluminum_incoherent.init = '"init"'

# Comp instance Aluminum_Powder, placement and parameters
Aluminum_Powder = instr.add_component('Aluminum_Powder','Powder_process')

Aluminum_Powder.reflections = '"Al.laz"'
Aluminum_Powder.packing_factor = '1'
Aluminum_Powder.Vc = '0'
Aluminum_Powder.delta_d_d = '0'
Aluminum_Powder.DW = '0'
Aluminum_Powder.nb_atoms = '1'
Aluminum_Powder.d_phi = '0'
Aluminum_Powder.density = '0'
Aluminum_Powder.weight = '0'
Aluminum_Powder.barns = '1'
Aluminum_Powder.Strain = '0'
Aluminum_Powder.interact_fraction = '-1'
Aluminum_Powder.format = '{ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 }'
Aluminum_Powder.init = '"init"'

# Comp instance Aluminum, placement and parameters
Aluminum = instr.add_component('Aluminum','Union_make_material')

Aluminum.process_string = '"Aluminum_incoherent,Aluminum_Powder"'
Aluminum.my_absorption = '1.3920'
Aluminum.absorber = '0'
Aluminum.init = '"init"'

# Comp instance Origin, placement and parameters
Origin = instr.add_component('Origin','Progress_bar')

Origin.profile = '"NULL"'
Origin.percent = '10'
Origin.flag_save = '0'
Origin.minutes = '0'

# Comp instance source, placement and parameters
source = instr.add_component('source','Source_gen', AT=['0', '0', '0'], AT_RELATIVE='Origin', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Origin')

source.flux_file = '"NULL"'
source.xdiv_file = '"NULL"'
source.ydiv_file = '"NULL"'
source.radius = '0.0'
source.dist = 'L0'
source.focus_xw = 'D'
source.focus_yh = 'D'
source.focus_aw = '0'
source.focus_ah = '0'
source.E0 = '0'
source.dE = '0'
source.lambda0 = '1.798'
source.dlambda = '1'
source.I1 = '1'
source.yheight = '0.1'
source.xwidth = '0.1'
source.verbose = '0'
source.T1 = '0'
source.flux_file_perAA = '0'
source.flux_file_log = '0'
source.Lmin = '0'
source.Lmax = '0'
source.Emin = '0'
source.Emax = '0'
source.T2 = '0'
source.I2 = '0'
source.T3 = '0'
source.I3 = '0'
source.zdepth = '0'
source.target_index = '1'

# Comp instance pinhole, placement and parameters
pinhole = instr.add_component('pinhole','Slit', AT=['0', '0', 'L0'], AT_RELATIVE='source', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='source')

pinhole.xmin = 'UNSET'
pinhole.xmax = 'UNSET'
pinhole.ymin = 'UNSET'
pinhole.ymax = 'UNSET'
pinhole.radius = 'D / 2'
pinhole.xwidth = 'UNSET'
pinhole.yheight = 'UNSET'

# Comp instance incoherent, placement and parameters
incoherent = instr.add_component('incoherent','Incoherent', AT=['0', '0', '0.001'], AT_RELATIVE='pinhole', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='pinhole')

incoherent.geometry = '0'
incoherent.radius = '0'
incoherent.xwidth = '1'
incoherent.yheight = '1'
incoherent.zdepth = '0.001'
incoherent.thickness = '0'
incoherent.target_x = '0'
incoherent.target_y = '0'
incoherent.target_z = 'L + l + battery_depth'
incoherent.focus_r = '0'
incoherent.focus_xw = '0.006'
incoherent.focus_yh = 'battery_width * 1.1'
incoherent.focus_aw = '0'
incoherent.focus_ah = '0'
incoherent.target_index = '0'
incoherent.pack = '1'
incoherent.p_interact = '1'
incoherent.f_QE = '0'
incoherent.gamma = '0'
incoherent.Etrans = '0'
incoherent.deltaE = '0'
incoherent.sigma_abs = '0.0001'
incoherent.sigma_inc = '0.0001'
incoherent.Vc = '1'
incoherent.concentric = '0'
incoherent.order = '0'

# Comp instance samplearm, placement and parameters
samplearm = instr.add_component('samplearm','Arm', AT=['0', '0', 'L'], AT_RELATIVE='pinhole', ROTATED=['0', '0', 'Rota'], ROTATED_RELATIVE='pinhole')


# Comp instance seperator, placement and parameters
seperator = instr.add_component('seperator','Union_box', AT=['0', '0', '0'], AT_RELATIVE='samplearm', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='samplearm')

seperator.material_string = '"Electrolyte"'
seperator.priority = '50'
seperator.xwidth = 'battery_width'
seperator.yheight = 'battery_thickness_m'
seperator.zdepth = 'battery_depth'
seperator.xwidth2 = '-1'
seperator.yheight2 = '-1'
seperator.visualize = '1'
seperator.target_index = '0'
seperator.target_x = '0'
seperator.target_y = '0'
seperator.target_z = '0'
seperator.focus_aw = '0'
seperator.focus_ah = '0'
seperator.focus_xw = '0'
seperator.focus_xh = '0'
seperator.focus_r = '0'
seperator.p_interact = '0'
seperator.mask_string = '0'
seperator.mask_setting = '0'
seperator.number_of_activations = '1'
seperator.init = '"init"'

# Comp instance battery_bottom, placement and parameters
battery_bottom = instr.add_component('battery_bottom','Arm', AT=['0', '-0.5 * battery_thickness_m', '0'], AT_RELATIVE='seperator', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='seperator')


# Comp instance positive_electrode_layer_0, placement and parameters
positive_electrode_layer_0 = instr.add_component('positive_electrode_layer_0','Union_box', AT=['0', 'positive_foil_center [ 0 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

positive_electrode_layer_0.material_string = '"LiFePO4"'
positive_electrode_layer_0.priority = '50.1 + 0.0'
positive_electrode_layer_0.xwidth = 'battery_width - end_safety'
positive_electrode_layer_0.yheight = '2 * positive_electrode_thickness_m + positive_foil_thickness_m'
positive_electrode_layer_0.zdepth = 'battery_depth - end_safety'
positive_electrode_layer_0.xwidth2 = '-1'
positive_electrode_layer_0.yheight2 = '-1'
positive_electrode_layer_0.visualize = '1'
positive_electrode_layer_0.target_index = '0'
positive_electrode_layer_0.target_x = '0'
positive_electrode_layer_0.target_y = '0'
positive_electrode_layer_0.target_z = '0'
positive_electrode_layer_0.focus_aw = '0'
positive_electrode_layer_0.focus_ah = '0'
positive_electrode_layer_0.focus_xw = '0'
positive_electrode_layer_0.focus_xh = '0'
positive_electrode_layer_0.focus_r = '0'
positive_electrode_layer_0.p_interact = '0'
positive_electrode_layer_0.mask_string = '0'
positive_electrode_layer_0.mask_setting = '0'
positive_electrode_layer_0.number_of_activations = '1'
positive_electrode_layer_0.init = '"init"'

# Comp instance positive_foil_layer_0, placement and parameters
positive_foil_layer_0 = instr.add_component('positive_foil_layer_0','Union_box', AT=['0', 'positive_foil_center [ 0 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

positive_foil_layer_0.material_string = '"Aluminum"'
positive_foil_layer_0.priority = '50.2 + 0.0'
positive_foil_layer_0.xwidth = 'battery_width -2 * end_safety'
positive_foil_layer_0.yheight = 'positive_foil_thickness_m'
positive_foil_layer_0.zdepth = 'battery_depth -2 * end_safety'
positive_foil_layer_0.xwidth2 = '-1'
positive_foil_layer_0.yheight2 = '-1'
positive_foil_layer_0.visualize = '1'
positive_foil_layer_0.target_index = '0'
positive_foil_layer_0.target_x = '0'
positive_foil_layer_0.target_y = '0'
positive_foil_layer_0.target_z = '0'
positive_foil_layer_0.focus_aw = '0'
positive_foil_layer_0.focus_ah = '0'
positive_foil_layer_0.focus_xw = '0'
positive_foil_layer_0.focus_xh = '0'
positive_foil_layer_0.focus_r = '0'
positive_foil_layer_0.p_interact = '0'
positive_foil_layer_0.mask_string = '0'
positive_foil_layer_0.mask_setting = '0'
positive_foil_layer_0.number_of_activations = '1'
positive_foil_layer_0.init = '"init"'

# Comp instance negative_electrode_layer_0, placement and parameters
negative_electrode_layer_0 = instr.add_component('negative_electrode_layer_0','Union_box', AT=['0', 'negative_foil_center [ 0 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

negative_electrode_layer_0.material_string = '"LiC6"'
negative_electrode_layer_0.priority = '50.4 + 0.0'
negative_electrode_layer_0.xwidth = 'battery_width - end_safety'
negative_electrode_layer_0.yheight = '2 * negative_electrode_thickness_m + negative_foil_thickness_m'
negative_electrode_layer_0.zdepth = 'battery_depth - end_safety'
negative_electrode_layer_0.xwidth2 = '-1'
negative_electrode_layer_0.yheight2 = '-1'
negative_electrode_layer_0.visualize = '1'
negative_electrode_layer_0.target_index = '0'
negative_electrode_layer_0.target_x = '0'
negative_electrode_layer_0.target_y = '0'
negative_electrode_layer_0.target_z = '0'
negative_electrode_layer_0.focus_aw = '0'
negative_electrode_layer_0.focus_ah = '0'
negative_electrode_layer_0.focus_xw = '0'
negative_electrode_layer_0.focus_xh = '0'
negative_electrode_layer_0.focus_r = '0'
negative_electrode_layer_0.p_interact = '0'
negative_electrode_layer_0.mask_string = '0'
negative_electrode_layer_0.mask_setting = '0'
negative_electrode_layer_0.number_of_activations = '1'
negative_electrode_layer_0.init = '"init"'

# Comp instance negative_foil_layer_0, placement and parameters
negative_foil_layer_0 = instr.add_component('negative_foil_layer_0','Union_box', AT=['0', 'negative_foil_center [ 0 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

negative_foil_layer_0.material_string = '"Copper"'
negative_foil_layer_0.priority = '50.5 + 0.0'
negative_foil_layer_0.xwidth = 'battery_width -2 * end_safety'
negative_foil_layer_0.yheight = 'positive_foil_thickness_m'
negative_foil_layer_0.zdepth = 'battery_depth -2 * end_safety'
negative_foil_layer_0.xwidth2 = '-1'
negative_foil_layer_0.yheight2 = '-1'
negative_foil_layer_0.visualize = '1'
negative_foil_layer_0.target_index = '0'
negative_foil_layer_0.target_x = '0'
negative_foil_layer_0.target_y = '0'
negative_foil_layer_0.target_z = '0'
negative_foil_layer_0.focus_aw = '0'
negative_foil_layer_0.focus_ah = '0'
negative_foil_layer_0.focus_xw = '0'
negative_foil_layer_0.focus_xh = '0'
negative_foil_layer_0.focus_r = '0'
negative_foil_layer_0.p_interact = '0'
negative_foil_layer_0.mask_string = '0'
negative_foil_layer_0.mask_setting = '0'
negative_foil_layer_0.number_of_activations = '1'
negative_foil_layer_0.init = '"init"'

# Comp instance positive_electrode_layer_1, placement and parameters
positive_electrode_layer_1 = instr.add_component('positive_electrode_layer_1','Union_box', AT=['0', 'positive_foil_center [ 1 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

positive_electrode_layer_1.material_string = '"LiFePO4"'
positive_electrode_layer_1.priority = '50.1 + 1.0'
positive_electrode_layer_1.xwidth = 'battery_width - end_safety'
positive_electrode_layer_1.yheight = '2 * positive_electrode_thickness_m + positive_foil_thickness_m'
positive_electrode_layer_1.zdepth = 'battery_depth - end_safety'
positive_electrode_layer_1.xwidth2 = '-1'
positive_electrode_layer_1.yheight2 = '-1'
positive_electrode_layer_1.visualize = '1'
positive_electrode_layer_1.target_index = '0'
positive_electrode_layer_1.target_x = '0'
positive_electrode_layer_1.target_y = '0'
positive_electrode_layer_1.target_z = '0'
positive_electrode_layer_1.focus_aw = '0'
positive_electrode_layer_1.focus_ah = '0'
positive_electrode_layer_1.focus_xw = '0'
positive_electrode_layer_1.focus_xh = '0'
positive_electrode_layer_1.focus_r = '0'
positive_electrode_layer_1.p_interact = '0'
positive_electrode_layer_1.mask_string = '0'
positive_electrode_layer_1.mask_setting = '0'
positive_electrode_layer_1.number_of_activations = '1'
positive_electrode_layer_1.init = '"init"'

# Comp instance positive_foil_layer_1, placement and parameters
positive_foil_layer_1 = instr.add_component('positive_foil_layer_1','Union_box', AT=['0', 'positive_foil_center [ 1 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

positive_foil_layer_1.material_string = '"Aluminum"'
positive_foil_layer_1.priority = '50.2 + 1.0'
positive_foil_layer_1.xwidth = 'battery_width -2 * end_safety'
positive_foil_layer_1.yheight = 'positive_foil_thickness_m'
positive_foil_layer_1.zdepth = 'battery_depth -2 * end_safety'
positive_foil_layer_1.xwidth2 = '-1'
positive_foil_layer_1.yheight2 = '-1'
positive_foil_layer_1.visualize = '1'
positive_foil_layer_1.target_index = '0'
positive_foil_layer_1.target_x = '0'
positive_foil_layer_1.target_y = '0'
positive_foil_layer_1.target_z = '0'
positive_foil_layer_1.focus_aw = '0'
positive_foil_layer_1.focus_ah = '0'
positive_foil_layer_1.focus_xw = '0'
positive_foil_layer_1.focus_xh = '0'
positive_foil_layer_1.focus_r = '0'
positive_foil_layer_1.p_interact = '0'
positive_foil_layer_1.mask_string = '0'
positive_foil_layer_1.mask_setting = '0'
positive_foil_layer_1.number_of_activations = '1'
positive_foil_layer_1.init = '"init"'

# Comp instance negative_electrode_layer_1, placement and parameters
negative_electrode_layer_1 = instr.add_component('negative_electrode_layer_1','Union_box', AT=['0', 'negative_foil_center [ 1 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

negative_electrode_layer_1.material_string = '"LiC6"'
negative_electrode_layer_1.priority = '50.4 + 1.0'
negative_electrode_layer_1.xwidth = 'battery_width - end_safety'
negative_electrode_layer_1.yheight = '2 * negative_electrode_thickness_m + negative_foil_thickness_m'
negative_electrode_layer_1.zdepth = 'battery_depth - end_safety'
negative_electrode_layer_1.xwidth2 = '-1'
negative_electrode_layer_1.yheight2 = '-1'
negative_electrode_layer_1.visualize = '1'
negative_electrode_layer_1.target_index = '0'
negative_electrode_layer_1.target_x = '0'
negative_electrode_layer_1.target_y = '0'
negative_electrode_layer_1.target_z = '0'
negative_electrode_layer_1.focus_aw = '0'
negative_electrode_layer_1.focus_ah = '0'
negative_electrode_layer_1.focus_xw = '0'
negative_electrode_layer_1.focus_xh = '0'
negative_electrode_layer_1.focus_r = '0'
negative_electrode_layer_1.p_interact = '0'
negative_electrode_layer_1.mask_string = '0'
negative_electrode_layer_1.mask_setting = '0'
negative_electrode_layer_1.number_of_activations = '1'
negative_electrode_layer_1.init = '"init"'

# Comp instance negative_foil_layer_1, placement and parameters
negative_foil_layer_1 = instr.add_component('negative_foil_layer_1','Union_box', AT=['0', 'negative_foil_center [ 1 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

negative_foil_layer_1.material_string = '"Copper"'
negative_foil_layer_1.priority = '50.5 + 1.0'
negative_foil_layer_1.xwidth = 'battery_width -2 * end_safety'
negative_foil_layer_1.yheight = 'positive_foil_thickness_m'
negative_foil_layer_1.zdepth = 'battery_depth -2 * end_safety'
negative_foil_layer_1.xwidth2 = '-1'
negative_foil_layer_1.yheight2 = '-1'
negative_foil_layer_1.visualize = '1'
negative_foil_layer_1.target_index = '0'
negative_foil_layer_1.target_x = '0'
negative_foil_layer_1.target_y = '0'
negative_foil_layer_1.target_z = '0'
negative_foil_layer_1.focus_aw = '0'
negative_foil_layer_1.focus_ah = '0'
negative_foil_layer_1.focus_xw = '0'
negative_foil_layer_1.focus_xh = '0'
negative_foil_layer_1.focus_r = '0'
negative_foil_layer_1.p_interact = '0'
negative_foil_layer_1.mask_string = '0'
negative_foil_layer_1.mask_setting = '0'
negative_foil_layer_1.number_of_activations = '1'
negative_foil_layer_1.init = '"init"'

# Comp instance positive_electrode_layer_2, placement and parameters
positive_electrode_layer_2 = instr.add_component('positive_electrode_layer_2','Union_box', AT=['0', 'positive_foil_center [ 2 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

positive_electrode_layer_2.material_string = '"LiFePO4"'
positive_electrode_layer_2.priority = '50.1 + 2.0'
positive_electrode_layer_2.xwidth = 'battery_width - end_safety'
positive_electrode_layer_2.yheight = '2 * positive_electrode_thickness_m + positive_foil_thickness_m'
positive_electrode_layer_2.zdepth = 'battery_depth - end_safety'
positive_electrode_layer_2.xwidth2 = '-1'
positive_electrode_layer_2.yheight2 = '-1'
positive_electrode_layer_2.visualize = '1'
positive_electrode_layer_2.target_index = '0'
positive_electrode_layer_2.target_x = '0'
positive_electrode_layer_2.target_y = '0'
positive_electrode_layer_2.target_z = '0'
positive_electrode_layer_2.focus_aw = '0'
positive_electrode_layer_2.focus_ah = '0'
positive_electrode_layer_2.focus_xw = '0'
positive_electrode_layer_2.focus_xh = '0'
positive_electrode_layer_2.focus_r = '0'
positive_electrode_layer_2.p_interact = '0'
positive_electrode_layer_2.mask_string = '0'
positive_electrode_layer_2.mask_setting = '0'
positive_electrode_layer_2.number_of_activations = '1'
positive_electrode_layer_2.init = '"init"'

# Comp instance positive_foil_layer_2, placement and parameters
positive_foil_layer_2 = instr.add_component('positive_foil_layer_2','Union_box', AT=['0', 'positive_foil_center [ 2 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

positive_foil_layer_2.material_string = '"Aluminum"'
positive_foil_layer_2.priority = '50.2 + 2.0'
positive_foil_layer_2.xwidth = 'battery_width -2 * end_safety'
positive_foil_layer_2.yheight = 'positive_foil_thickness_m'
positive_foil_layer_2.zdepth = 'battery_depth -2 * end_safety'
positive_foil_layer_2.xwidth2 = '-1'
positive_foil_layer_2.yheight2 = '-1'
positive_foil_layer_2.visualize = '1'
positive_foil_layer_2.target_index = '0'
positive_foil_layer_2.target_x = '0'
positive_foil_layer_2.target_y = '0'
positive_foil_layer_2.target_z = '0'
positive_foil_layer_2.focus_aw = '0'
positive_foil_layer_2.focus_ah = '0'
positive_foil_layer_2.focus_xw = '0'
positive_foil_layer_2.focus_xh = '0'
positive_foil_layer_2.focus_r = '0'
positive_foil_layer_2.p_interact = '0'
positive_foil_layer_2.mask_string = '0'
positive_foil_layer_2.mask_setting = '0'
positive_foil_layer_2.number_of_activations = '1'
positive_foil_layer_2.init = '"init"'

# Comp instance negative_electrode_layer_2, placement and parameters
negative_electrode_layer_2 = instr.add_component('negative_electrode_layer_2','Union_box', AT=['0', 'negative_foil_center [ 2 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

negative_electrode_layer_2.material_string = '"LiC6"'
negative_electrode_layer_2.priority = '50.4 + 2.0'
negative_electrode_layer_2.xwidth = 'battery_width - end_safety'
negative_electrode_layer_2.yheight = '2 * negative_electrode_thickness_m + negative_foil_thickness_m'
negative_electrode_layer_2.zdepth = 'battery_depth - end_safety'
negative_electrode_layer_2.xwidth2 = '-1'
negative_electrode_layer_2.yheight2 = '-1'
negative_electrode_layer_2.visualize = '1'
negative_electrode_layer_2.target_index = '0'
negative_electrode_layer_2.target_x = '0'
negative_electrode_layer_2.target_y = '0'
negative_electrode_layer_2.target_z = '0'
negative_electrode_layer_2.focus_aw = '0'
negative_electrode_layer_2.focus_ah = '0'
negative_electrode_layer_2.focus_xw = '0'
negative_electrode_layer_2.focus_xh = '0'
negative_electrode_layer_2.focus_r = '0'
negative_electrode_layer_2.p_interact = '0'
negative_electrode_layer_2.mask_string = '0'
negative_electrode_layer_2.mask_setting = '0'
negative_electrode_layer_2.number_of_activations = '1'
negative_electrode_layer_2.init = '"init"'

# Comp instance negative_foil_layer_2, placement and parameters
negative_foil_layer_2 = instr.add_component('negative_foil_layer_2','Union_box', AT=['0', 'negative_foil_center [ 2 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

negative_foil_layer_2.material_string = '"Copper"'
negative_foil_layer_2.priority = '50.5 + 2.0'
negative_foil_layer_2.xwidth = 'battery_width -2 * end_safety'
negative_foil_layer_2.yheight = 'positive_foil_thickness_m'
negative_foil_layer_2.zdepth = 'battery_depth -2 * end_safety'
negative_foil_layer_2.xwidth2 = '-1'
negative_foil_layer_2.yheight2 = '-1'
negative_foil_layer_2.visualize = '1'
negative_foil_layer_2.target_index = '0'
negative_foil_layer_2.target_x = '0'
negative_foil_layer_2.target_y = '0'
negative_foil_layer_2.target_z = '0'
negative_foil_layer_2.focus_aw = '0'
negative_foil_layer_2.focus_ah = '0'
negative_foil_layer_2.focus_xw = '0'
negative_foil_layer_2.focus_xh = '0'
negative_foil_layer_2.focus_r = '0'
negative_foil_layer_2.p_interact = '0'
negative_foil_layer_2.mask_string = '0'
negative_foil_layer_2.mask_setting = '0'
negative_foil_layer_2.number_of_activations = '1'
negative_foil_layer_2.init = '"init"'

# Comp instance positive_electrode_layer_3, placement and parameters
positive_electrode_layer_3 = instr.add_component('positive_electrode_layer_3','Union_box', AT=['0', 'positive_foil_center [ 3 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

positive_electrode_layer_3.material_string = '"LiFePO4"'
positive_electrode_layer_3.priority = '50.1 + 3.0'
positive_electrode_layer_3.xwidth = 'battery_width - end_safety'
positive_electrode_layer_3.yheight = '2 * positive_electrode_thickness_m + positive_foil_thickness_m'
positive_electrode_layer_3.zdepth = 'battery_depth - end_safety'
positive_electrode_layer_3.xwidth2 = '-1'
positive_electrode_layer_3.yheight2 = '-1'
positive_electrode_layer_3.visualize = '1'
positive_electrode_layer_3.target_index = '0'
positive_electrode_layer_3.target_x = '0'
positive_electrode_layer_3.target_y = '0'
positive_electrode_layer_3.target_z = '0'
positive_electrode_layer_3.focus_aw = '0'
positive_electrode_layer_3.focus_ah = '0'
positive_electrode_layer_3.focus_xw = '0'
positive_electrode_layer_3.focus_xh = '0'
positive_electrode_layer_3.focus_r = '0'
positive_electrode_layer_3.p_interact = '0'
positive_electrode_layer_3.mask_string = '0'
positive_electrode_layer_3.mask_setting = '0'
positive_electrode_layer_3.number_of_activations = '1'
positive_electrode_layer_3.init = '"init"'

# Comp instance positive_foil_layer_3, placement and parameters
positive_foil_layer_3 = instr.add_component('positive_foil_layer_3','Union_box', AT=['0', 'positive_foil_center [ 3 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

positive_foil_layer_3.material_string = '"Aluminum"'
positive_foil_layer_3.priority = '50.2 + 3.0'
positive_foil_layer_3.xwidth = 'battery_width -2 * end_safety'
positive_foil_layer_3.yheight = 'positive_foil_thickness_m'
positive_foil_layer_3.zdepth = 'battery_depth -2 * end_safety'
positive_foil_layer_3.xwidth2 = '-1'
positive_foil_layer_3.yheight2 = '-1'
positive_foil_layer_3.visualize = '1'
positive_foil_layer_3.target_index = '0'
positive_foil_layer_3.target_x = '0'
positive_foil_layer_3.target_y = '0'
positive_foil_layer_3.target_z = '0'
positive_foil_layer_3.focus_aw = '0'
positive_foil_layer_3.focus_ah = '0'
positive_foil_layer_3.focus_xw = '0'
positive_foil_layer_3.focus_xh = '0'
positive_foil_layer_3.focus_r = '0'
positive_foil_layer_3.p_interact = '0'
positive_foil_layer_3.mask_string = '0'
positive_foil_layer_3.mask_setting = '0'
positive_foil_layer_3.number_of_activations = '1'
positive_foil_layer_3.init = '"init"'

# Comp instance negative_electrode_layer_3, placement and parameters
negative_electrode_layer_3 = instr.add_component('negative_electrode_layer_3','Union_box', AT=['0', 'negative_foil_center [ 3 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

negative_electrode_layer_3.material_string = '"LiC6"'
negative_electrode_layer_3.priority = '50.4 + 3.0'
negative_electrode_layer_3.xwidth = 'battery_width - end_safety'
negative_electrode_layer_3.yheight = '2 * negative_electrode_thickness_m + negative_foil_thickness_m'
negative_electrode_layer_3.zdepth = 'battery_depth - end_safety'
negative_electrode_layer_3.xwidth2 = '-1'
negative_electrode_layer_3.yheight2 = '-1'
negative_electrode_layer_3.visualize = '1'
negative_electrode_layer_3.target_index = '0'
negative_electrode_layer_3.target_x = '0'
negative_electrode_layer_3.target_y = '0'
negative_electrode_layer_3.target_z = '0'
negative_electrode_layer_3.focus_aw = '0'
negative_electrode_layer_3.focus_ah = '0'
negative_electrode_layer_3.focus_xw = '0'
negative_electrode_layer_3.focus_xh = '0'
negative_electrode_layer_3.focus_r = '0'
negative_electrode_layer_3.p_interact = '0'
negative_electrode_layer_3.mask_string = '0'
negative_electrode_layer_3.mask_setting = '0'
negative_electrode_layer_3.number_of_activations = '1'
negative_electrode_layer_3.init = '"init"'

# Comp instance negative_foil_layer_3, placement and parameters
negative_foil_layer_3 = instr.add_component('negative_foil_layer_3','Union_box', AT=['0', 'negative_foil_center [ 3 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

negative_foil_layer_3.material_string = '"Copper"'
negative_foil_layer_3.priority = '50.5 + 3.0'
negative_foil_layer_3.xwidth = 'battery_width -2 * end_safety'
negative_foil_layer_3.yheight = 'positive_foil_thickness_m'
negative_foil_layer_3.zdepth = 'battery_depth -2 * end_safety'
negative_foil_layer_3.xwidth2 = '-1'
negative_foil_layer_3.yheight2 = '-1'
negative_foil_layer_3.visualize = '1'
negative_foil_layer_3.target_index = '0'
negative_foil_layer_3.target_x = '0'
negative_foil_layer_3.target_y = '0'
negative_foil_layer_3.target_z = '0'
negative_foil_layer_3.focus_aw = '0'
negative_foil_layer_3.focus_ah = '0'
negative_foil_layer_3.focus_xw = '0'
negative_foil_layer_3.focus_xh = '0'
negative_foil_layer_3.focus_r = '0'
negative_foil_layer_3.p_interact = '0'
negative_foil_layer_3.mask_string = '0'
negative_foil_layer_3.mask_setting = '0'
negative_foil_layer_3.number_of_activations = '1'
negative_foil_layer_3.init = '"init"'

# Comp instance positive_electrode_layer_4, placement and parameters
positive_electrode_layer_4 = instr.add_component('positive_electrode_layer_4','Union_box', AT=['0', 'positive_foil_center [ 4 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

positive_electrode_layer_4.material_string = '"LiFePO4"'
positive_electrode_layer_4.priority = '50.1 + 4.0'
positive_electrode_layer_4.xwidth = 'battery_width - end_safety'
positive_electrode_layer_4.yheight = '2 * positive_electrode_thickness_m + positive_foil_thickness_m'
positive_electrode_layer_4.zdepth = 'battery_depth - end_safety'
positive_electrode_layer_4.xwidth2 = '-1'
positive_electrode_layer_4.yheight2 = '-1'
positive_electrode_layer_4.visualize = '1'
positive_electrode_layer_4.target_index = '0'
positive_electrode_layer_4.target_x = '0'
positive_electrode_layer_4.target_y = '0'
positive_electrode_layer_4.target_z = '0'
positive_electrode_layer_4.focus_aw = '0'
positive_electrode_layer_4.focus_ah = '0'
positive_electrode_layer_4.focus_xw = '0'
positive_electrode_layer_4.focus_xh = '0'
positive_electrode_layer_4.focus_r = '0'
positive_electrode_layer_4.p_interact = '0'
positive_electrode_layer_4.mask_string = '0'
positive_electrode_layer_4.mask_setting = '0'
positive_electrode_layer_4.number_of_activations = '1'
positive_electrode_layer_4.init = '"init"'

# Comp instance positive_foil_layer_4, placement and parameters
positive_foil_layer_4 = instr.add_component('positive_foil_layer_4','Union_box', AT=['0', 'positive_foil_center [ 4 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

positive_foil_layer_4.material_string = '"Aluminum"'
positive_foil_layer_4.priority = '50.2 + 4.0'
positive_foil_layer_4.xwidth = 'battery_width -2 * end_safety'
positive_foil_layer_4.yheight = 'positive_foil_thickness_m'
positive_foil_layer_4.zdepth = 'battery_depth -2 * end_safety'
positive_foil_layer_4.xwidth2 = '-1'
positive_foil_layer_4.yheight2 = '-1'
positive_foil_layer_4.visualize = '1'
positive_foil_layer_4.target_index = '0'
positive_foil_layer_4.target_x = '0'
positive_foil_layer_4.target_y = '0'
positive_foil_layer_4.target_z = '0'
positive_foil_layer_4.focus_aw = '0'
positive_foil_layer_4.focus_ah = '0'
positive_foil_layer_4.focus_xw = '0'
positive_foil_layer_4.focus_xh = '0'
positive_foil_layer_4.focus_r = '0'
positive_foil_layer_4.p_interact = '0'
positive_foil_layer_4.mask_string = '0'
positive_foil_layer_4.mask_setting = '0'
positive_foil_layer_4.number_of_activations = '1'
positive_foil_layer_4.init = '"init"'

# Comp instance negative_electrode_layer_4, placement and parameters
negative_electrode_layer_4 = instr.add_component('negative_electrode_layer_4','Union_box', AT=['0', 'negative_foil_center [ 4 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

negative_electrode_layer_4.material_string = '"LiC6"'
negative_electrode_layer_4.priority = '50.4 + 4.0'
negative_electrode_layer_4.xwidth = 'battery_width - end_safety'
negative_electrode_layer_4.yheight = '2 * negative_electrode_thickness_m + negative_foil_thickness_m'
negative_electrode_layer_4.zdepth = 'battery_depth - end_safety'
negative_electrode_layer_4.xwidth2 = '-1'
negative_electrode_layer_4.yheight2 = '-1'
negative_electrode_layer_4.visualize = '1'
negative_electrode_layer_4.target_index = '0'
negative_electrode_layer_4.target_x = '0'
negative_electrode_layer_4.target_y = '0'
negative_electrode_layer_4.target_z = '0'
negative_electrode_layer_4.focus_aw = '0'
negative_electrode_layer_4.focus_ah = '0'
negative_electrode_layer_4.focus_xw = '0'
negative_electrode_layer_4.focus_xh = '0'
negative_electrode_layer_4.focus_r = '0'
negative_electrode_layer_4.p_interact = '0'
negative_electrode_layer_4.mask_string = '0'
negative_electrode_layer_4.mask_setting = '0'
negative_electrode_layer_4.number_of_activations = '1'
negative_electrode_layer_4.init = '"init"'

# Comp instance negative_foil_layer_4, placement and parameters
negative_foil_layer_4 = instr.add_component('negative_foil_layer_4','Union_box', AT=['0', 'negative_foil_center [ 4 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

negative_foil_layer_4.material_string = '"Copper"'
negative_foil_layer_4.priority = '50.5 + 4.0'
negative_foil_layer_4.xwidth = 'battery_width -2 * end_safety'
negative_foil_layer_4.yheight = 'positive_foil_thickness_m'
negative_foil_layer_4.zdepth = 'battery_depth -2 * end_safety'
negative_foil_layer_4.xwidth2 = '-1'
negative_foil_layer_4.yheight2 = '-1'
negative_foil_layer_4.visualize = '1'
negative_foil_layer_4.target_index = '0'
negative_foil_layer_4.target_x = '0'
negative_foil_layer_4.target_y = '0'
negative_foil_layer_4.target_z = '0'
negative_foil_layer_4.focus_aw = '0'
negative_foil_layer_4.focus_ah = '0'
negative_foil_layer_4.focus_xw = '0'
negative_foil_layer_4.focus_xh = '0'
negative_foil_layer_4.focus_r = '0'
negative_foil_layer_4.p_interact = '0'
negative_foil_layer_4.mask_string = '0'
negative_foil_layer_4.mask_setting = '0'
negative_foil_layer_4.number_of_activations = '1'
negative_foil_layer_4.init = '"init"'

# Comp instance positive_electrode_layer_5, placement and parameters
positive_electrode_layer_5 = instr.add_component('positive_electrode_layer_5','Union_box', AT=['0', 'positive_foil_center [ 5 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

positive_electrode_layer_5.material_string = '"LiFePO4"'
positive_electrode_layer_5.priority = '50.1 + 5.0'
positive_electrode_layer_5.xwidth = 'battery_width - end_safety'
positive_electrode_layer_5.yheight = '2 * positive_electrode_thickness_m + positive_foil_thickness_m'
positive_electrode_layer_5.zdepth = 'battery_depth - end_safety'
positive_electrode_layer_5.xwidth2 = '-1'
positive_electrode_layer_5.yheight2 = '-1'
positive_electrode_layer_5.visualize = '1'
positive_electrode_layer_5.target_index = '0'
positive_electrode_layer_5.target_x = '0'
positive_electrode_layer_5.target_y = '0'
positive_electrode_layer_5.target_z = '0'
positive_electrode_layer_5.focus_aw = '0'
positive_electrode_layer_5.focus_ah = '0'
positive_electrode_layer_5.focus_xw = '0'
positive_electrode_layer_5.focus_xh = '0'
positive_electrode_layer_5.focus_r = '0'
positive_electrode_layer_5.p_interact = '0'
positive_electrode_layer_5.mask_string = '0'
positive_electrode_layer_5.mask_setting = '0'
positive_electrode_layer_5.number_of_activations = '1'
positive_electrode_layer_5.init = '"init"'

# Comp instance positive_foil_layer_5, placement and parameters
positive_foil_layer_5 = instr.add_component('positive_foil_layer_5','Union_box', AT=['0', 'positive_foil_center [ 5 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

positive_foil_layer_5.material_string = '"Aluminum"'
positive_foil_layer_5.priority = '50.2 + 5.0'
positive_foil_layer_5.xwidth = 'battery_width -2 * end_safety'
positive_foil_layer_5.yheight = 'positive_foil_thickness_m'
positive_foil_layer_5.zdepth = 'battery_depth -2 * end_safety'
positive_foil_layer_5.xwidth2 = '-1'
positive_foil_layer_5.yheight2 = '-1'
positive_foil_layer_5.visualize = '1'
positive_foil_layer_5.target_index = '0'
positive_foil_layer_5.target_x = '0'
positive_foil_layer_5.target_y = '0'
positive_foil_layer_5.target_z = '0'
positive_foil_layer_5.focus_aw = '0'
positive_foil_layer_5.focus_ah = '0'
positive_foil_layer_5.focus_xw = '0'
positive_foil_layer_5.focus_xh = '0'
positive_foil_layer_5.focus_r = '0'
positive_foil_layer_5.p_interact = '0'
positive_foil_layer_5.mask_string = '0'
positive_foil_layer_5.mask_setting = '0'
positive_foil_layer_5.number_of_activations = '1'
positive_foil_layer_5.init = '"init"'

# Comp instance negative_electrode_layer_5, placement and parameters
negative_electrode_layer_5 = instr.add_component('negative_electrode_layer_5','Union_box', AT=['0', 'negative_foil_center [ 5 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

negative_electrode_layer_5.material_string = '"LiC6"'
negative_electrode_layer_5.priority = '50.4 + 5.0'
negative_electrode_layer_5.xwidth = 'battery_width - end_safety'
negative_electrode_layer_5.yheight = '2 * negative_electrode_thickness_m + negative_foil_thickness_m'
negative_electrode_layer_5.zdepth = 'battery_depth - end_safety'
negative_electrode_layer_5.xwidth2 = '-1'
negative_electrode_layer_5.yheight2 = '-1'
negative_electrode_layer_5.visualize = '1'
negative_electrode_layer_5.target_index = '0'
negative_electrode_layer_5.target_x = '0'
negative_electrode_layer_5.target_y = '0'
negative_electrode_layer_5.target_z = '0'
negative_electrode_layer_5.focus_aw = '0'
negative_electrode_layer_5.focus_ah = '0'
negative_electrode_layer_5.focus_xw = '0'
negative_electrode_layer_5.focus_xh = '0'
negative_electrode_layer_5.focus_r = '0'
negative_electrode_layer_5.p_interact = '0'
negative_electrode_layer_5.mask_string = '0'
negative_electrode_layer_5.mask_setting = '0'
negative_electrode_layer_5.number_of_activations = '1'
negative_electrode_layer_5.init = '"init"'

# Comp instance negative_foil_layer_5, placement and parameters
negative_foil_layer_5 = instr.add_component('negative_foil_layer_5','Union_box', AT=['0', 'negative_foil_center [ 5 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

negative_foil_layer_5.material_string = '"Copper"'
negative_foil_layer_5.priority = '50.5 + 5.0'
negative_foil_layer_5.xwidth = 'battery_width -2 * end_safety'
negative_foil_layer_5.yheight = 'positive_foil_thickness_m'
negative_foil_layer_5.zdepth = 'battery_depth -2 * end_safety'
negative_foil_layer_5.xwidth2 = '-1'
negative_foil_layer_5.yheight2 = '-1'
negative_foil_layer_5.visualize = '1'
negative_foil_layer_5.target_index = '0'
negative_foil_layer_5.target_x = '0'
negative_foil_layer_5.target_y = '0'
negative_foil_layer_5.target_z = '0'
negative_foil_layer_5.focus_aw = '0'
negative_foil_layer_5.focus_ah = '0'
negative_foil_layer_5.focus_xw = '0'
negative_foil_layer_5.focus_xh = '0'
negative_foil_layer_5.focus_r = '0'
negative_foil_layer_5.p_interact = '0'
negative_foil_layer_5.mask_string = '0'
negative_foil_layer_5.mask_setting = '0'
negative_foil_layer_5.number_of_activations = '1'
negative_foil_layer_5.init = '"init"'

# Comp instance positive_electrode_layer_6, placement and parameters
positive_electrode_layer_6 = instr.add_component('positive_electrode_layer_6','Union_box', AT=['0', 'positive_foil_center [ 6 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

positive_electrode_layer_6.material_string = '"LiFePO4"'
positive_electrode_layer_6.priority = '50.1 + 6.0'
positive_electrode_layer_6.xwidth = 'battery_width - end_safety'
positive_electrode_layer_6.yheight = '2 * positive_electrode_thickness_m + positive_foil_thickness_m'
positive_electrode_layer_6.zdepth = 'battery_depth - end_safety'
positive_electrode_layer_6.xwidth2 = '-1'
positive_electrode_layer_6.yheight2 = '-1'
positive_electrode_layer_6.visualize = '1'
positive_electrode_layer_6.target_index = '0'
positive_electrode_layer_6.target_x = '0'
positive_electrode_layer_6.target_y = '0'
positive_electrode_layer_6.target_z = '0'
positive_electrode_layer_6.focus_aw = '0'
positive_electrode_layer_6.focus_ah = '0'
positive_electrode_layer_6.focus_xw = '0'
positive_electrode_layer_6.focus_xh = '0'
positive_electrode_layer_6.focus_r = '0'
positive_electrode_layer_6.p_interact = '0'
positive_electrode_layer_6.mask_string = '0'
positive_electrode_layer_6.mask_setting = '0'
positive_electrode_layer_6.number_of_activations = '1'
positive_electrode_layer_6.init = '"init"'

# Comp instance positive_foil_layer_6, placement and parameters
positive_foil_layer_6 = instr.add_component('positive_foil_layer_6','Union_box', AT=['0', 'positive_foil_center [ 6 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

positive_foil_layer_6.material_string = '"Aluminum"'
positive_foil_layer_6.priority = '50.2 + 6.0'
positive_foil_layer_6.xwidth = 'battery_width -2 * end_safety'
positive_foil_layer_6.yheight = 'positive_foil_thickness_m'
positive_foil_layer_6.zdepth = 'battery_depth -2 * end_safety'
positive_foil_layer_6.xwidth2 = '-1'
positive_foil_layer_6.yheight2 = '-1'
positive_foil_layer_6.visualize = '1'
positive_foil_layer_6.target_index = '0'
positive_foil_layer_6.target_x = '0'
positive_foil_layer_6.target_y = '0'
positive_foil_layer_6.target_z = '0'
positive_foil_layer_6.focus_aw = '0'
positive_foil_layer_6.focus_ah = '0'
positive_foil_layer_6.focus_xw = '0'
positive_foil_layer_6.focus_xh = '0'
positive_foil_layer_6.focus_r = '0'
positive_foil_layer_6.p_interact = '0'
positive_foil_layer_6.mask_string = '0'
positive_foil_layer_6.mask_setting = '0'
positive_foil_layer_6.number_of_activations = '1'
positive_foil_layer_6.init = '"init"'

# Comp instance negative_electrode_layer_6, placement and parameters
negative_electrode_layer_6 = instr.add_component('negative_electrode_layer_6','Union_box', AT=['0', 'negative_foil_center [ 6 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

negative_electrode_layer_6.material_string = '"LiC6"'
negative_electrode_layer_6.priority = '50.4 + 6.0'
negative_electrode_layer_6.xwidth = 'battery_width - end_safety'
negative_electrode_layer_6.yheight = '2 * negative_electrode_thickness_m + negative_foil_thickness_m'
negative_electrode_layer_6.zdepth = 'battery_depth - end_safety'
negative_electrode_layer_6.xwidth2 = '-1'
negative_electrode_layer_6.yheight2 = '-1'
negative_electrode_layer_6.visualize = '1'
negative_electrode_layer_6.target_index = '0'
negative_electrode_layer_6.target_x = '0'
negative_electrode_layer_6.target_y = '0'
negative_electrode_layer_6.target_z = '0'
negative_electrode_layer_6.focus_aw = '0'
negative_electrode_layer_6.focus_ah = '0'
negative_electrode_layer_6.focus_xw = '0'
negative_electrode_layer_6.focus_xh = '0'
negative_electrode_layer_6.focus_r = '0'
negative_electrode_layer_6.p_interact = '0'
negative_electrode_layer_6.mask_string = '0'
negative_electrode_layer_6.mask_setting = '0'
negative_electrode_layer_6.number_of_activations = '1'
negative_electrode_layer_6.init = '"init"'

# Comp instance negative_foil_layer_6, placement and parameters
negative_foil_layer_6 = instr.add_component('negative_foil_layer_6','Union_box', AT=['0', 'negative_foil_center [ 6 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

negative_foil_layer_6.material_string = '"Copper"'
negative_foil_layer_6.priority = '50.5 + 6.0'
negative_foil_layer_6.xwidth = 'battery_width -2 * end_safety'
negative_foil_layer_6.yheight = 'positive_foil_thickness_m'
negative_foil_layer_6.zdepth = 'battery_depth -2 * end_safety'
negative_foil_layer_6.xwidth2 = '-1'
negative_foil_layer_6.yheight2 = '-1'
negative_foil_layer_6.visualize = '1'
negative_foil_layer_6.target_index = '0'
negative_foil_layer_6.target_x = '0'
negative_foil_layer_6.target_y = '0'
negative_foil_layer_6.target_z = '0'
negative_foil_layer_6.focus_aw = '0'
negative_foil_layer_6.focus_ah = '0'
negative_foil_layer_6.focus_xw = '0'
negative_foil_layer_6.focus_xh = '0'
negative_foil_layer_6.focus_r = '0'
negative_foil_layer_6.p_interact = '0'
negative_foil_layer_6.mask_string = '0'
negative_foil_layer_6.mask_setting = '0'
negative_foil_layer_6.number_of_activations = '1'
negative_foil_layer_6.init = '"init"'

# Comp instance positive_electrode_layer_7, placement and parameters
positive_electrode_layer_7 = instr.add_component('positive_electrode_layer_7','Union_box', AT=['0', 'positive_foil_center [ 7 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

positive_electrode_layer_7.material_string = '"LiFePO4"'
positive_electrode_layer_7.priority = '50.1 + 7.0'
positive_electrode_layer_7.xwidth = 'battery_width - end_safety'
positive_electrode_layer_7.yheight = '2 * positive_electrode_thickness_m + positive_foil_thickness_m'
positive_electrode_layer_7.zdepth = 'battery_depth - end_safety'
positive_electrode_layer_7.xwidth2 = '-1'
positive_electrode_layer_7.yheight2 = '-1'
positive_electrode_layer_7.visualize = '1'
positive_electrode_layer_7.target_index = '0'
positive_electrode_layer_7.target_x = '0'
positive_electrode_layer_7.target_y = '0'
positive_electrode_layer_7.target_z = '0'
positive_electrode_layer_7.focus_aw = '0'
positive_electrode_layer_7.focus_ah = '0'
positive_electrode_layer_7.focus_xw = '0'
positive_electrode_layer_7.focus_xh = '0'
positive_electrode_layer_7.focus_r = '0'
positive_electrode_layer_7.p_interact = '0'
positive_electrode_layer_7.mask_string = '0'
positive_electrode_layer_7.mask_setting = '0'
positive_electrode_layer_7.number_of_activations = '1'
positive_electrode_layer_7.init = '"init"'

# Comp instance positive_foil_layer_7, placement and parameters
positive_foil_layer_7 = instr.add_component('positive_foil_layer_7','Union_box', AT=['0', 'positive_foil_center [ 7 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

positive_foil_layer_7.material_string = '"Aluminum"'
positive_foil_layer_7.priority = '50.2 + 7.0'
positive_foil_layer_7.xwidth = 'battery_width -2 * end_safety'
positive_foil_layer_7.yheight = 'positive_foil_thickness_m'
positive_foil_layer_7.zdepth = 'battery_depth -2 * end_safety'
positive_foil_layer_7.xwidth2 = '-1'
positive_foil_layer_7.yheight2 = '-1'
positive_foil_layer_7.visualize = '1'
positive_foil_layer_7.target_index = '0'
positive_foil_layer_7.target_x = '0'
positive_foil_layer_7.target_y = '0'
positive_foil_layer_7.target_z = '0'
positive_foil_layer_7.focus_aw = '0'
positive_foil_layer_7.focus_ah = '0'
positive_foil_layer_7.focus_xw = '0'
positive_foil_layer_7.focus_xh = '0'
positive_foil_layer_7.focus_r = '0'
positive_foil_layer_7.p_interact = '0'
positive_foil_layer_7.mask_string = '0'
positive_foil_layer_7.mask_setting = '0'
positive_foil_layer_7.number_of_activations = '1'
positive_foil_layer_7.init = '"init"'

# Comp instance negative_electrode_layer_7, placement and parameters
negative_electrode_layer_7 = instr.add_component('negative_electrode_layer_7','Union_box', AT=['0', 'negative_foil_center [ 7 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

negative_electrode_layer_7.material_string = '"LiC6"'
negative_electrode_layer_7.priority = '50.4 + 7.0'
negative_electrode_layer_7.xwidth = 'battery_width - end_safety'
negative_electrode_layer_7.yheight = '2 * negative_electrode_thickness_m + negative_foil_thickness_m'
negative_electrode_layer_7.zdepth = 'battery_depth - end_safety'
negative_electrode_layer_7.xwidth2 = '-1'
negative_electrode_layer_7.yheight2 = '-1'
negative_electrode_layer_7.visualize = '1'
negative_electrode_layer_7.target_index = '0'
negative_electrode_layer_7.target_x = '0'
negative_electrode_layer_7.target_y = '0'
negative_electrode_layer_7.target_z = '0'
negative_electrode_layer_7.focus_aw = '0'
negative_electrode_layer_7.focus_ah = '0'
negative_electrode_layer_7.focus_xw = '0'
negative_electrode_layer_7.focus_xh = '0'
negative_electrode_layer_7.focus_r = '0'
negative_electrode_layer_7.p_interact = '0'
negative_electrode_layer_7.mask_string = '0'
negative_electrode_layer_7.mask_setting = '0'
negative_electrode_layer_7.number_of_activations = '1'
negative_electrode_layer_7.init = '"init"'

# Comp instance negative_foil_layer_7, placement and parameters
negative_foil_layer_7 = instr.add_component('negative_foil_layer_7','Union_box', AT=['0', 'negative_foil_center [ 7 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

negative_foil_layer_7.material_string = '"Copper"'
negative_foil_layer_7.priority = '50.5 + 7.0'
negative_foil_layer_7.xwidth = 'battery_width -2 * end_safety'
negative_foil_layer_7.yheight = 'positive_foil_thickness_m'
negative_foil_layer_7.zdepth = 'battery_depth -2 * end_safety'
negative_foil_layer_7.xwidth2 = '-1'
negative_foil_layer_7.yheight2 = '-1'
negative_foil_layer_7.visualize = '1'
negative_foil_layer_7.target_index = '0'
negative_foil_layer_7.target_x = '0'
negative_foil_layer_7.target_y = '0'
negative_foil_layer_7.target_z = '0'
negative_foil_layer_7.focus_aw = '0'
negative_foil_layer_7.focus_ah = '0'
negative_foil_layer_7.focus_xw = '0'
negative_foil_layer_7.focus_xh = '0'
negative_foil_layer_7.focus_r = '0'
negative_foil_layer_7.p_interact = '0'
negative_foil_layer_7.mask_string = '0'
negative_foil_layer_7.mask_setting = '0'
negative_foil_layer_7.number_of_activations = '1'
negative_foil_layer_7.init = '"init"'

# Comp instance positive_electrode_layer_8, placement and parameters
positive_electrode_layer_8 = instr.add_component('positive_electrode_layer_8','Union_box', AT=['0', 'positive_foil_center [ 8 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

positive_electrode_layer_8.material_string = '"LiFePO4"'
positive_electrode_layer_8.priority = '50.1 + 8.0'
positive_electrode_layer_8.xwidth = 'battery_width - end_safety'
positive_electrode_layer_8.yheight = '2 * positive_electrode_thickness_m + positive_foil_thickness_m'
positive_electrode_layer_8.zdepth = 'battery_depth - end_safety'
positive_electrode_layer_8.xwidth2 = '-1'
positive_electrode_layer_8.yheight2 = '-1'
positive_electrode_layer_8.visualize = '1'
positive_electrode_layer_8.target_index = '0'
positive_electrode_layer_8.target_x = '0'
positive_electrode_layer_8.target_y = '0'
positive_electrode_layer_8.target_z = '0'
positive_electrode_layer_8.focus_aw = '0'
positive_electrode_layer_8.focus_ah = '0'
positive_electrode_layer_8.focus_xw = '0'
positive_electrode_layer_8.focus_xh = '0'
positive_electrode_layer_8.focus_r = '0'
positive_electrode_layer_8.p_interact = '0'
positive_electrode_layer_8.mask_string = '0'
positive_electrode_layer_8.mask_setting = '0'
positive_electrode_layer_8.number_of_activations = '1'
positive_electrode_layer_8.init = '"init"'

# Comp instance positive_foil_layer_8, placement and parameters
positive_foil_layer_8 = instr.add_component('positive_foil_layer_8','Union_box', AT=['0', 'positive_foil_center [ 8 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

positive_foil_layer_8.material_string = '"Aluminum"'
positive_foil_layer_8.priority = '50.2 + 8.0'
positive_foil_layer_8.xwidth = 'battery_width -2 * end_safety'
positive_foil_layer_8.yheight = 'positive_foil_thickness_m'
positive_foil_layer_8.zdepth = 'battery_depth -2 * end_safety'
positive_foil_layer_8.xwidth2 = '-1'
positive_foil_layer_8.yheight2 = '-1'
positive_foil_layer_8.visualize = '1'
positive_foil_layer_8.target_index = '0'
positive_foil_layer_8.target_x = '0'
positive_foil_layer_8.target_y = '0'
positive_foil_layer_8.target_z = '0'
positive_foil_layer_8.focus_aw = '0'
positive_foil_layer_8.focus_ah = '0'
positive_foil_layer_8.focus_xw = '0'
positive_foil_layer_8.focus_xh = '0'
positive_foil_layer_8.focus_r = '0'
positive_foil_layer_8.p_interact = '0'
positive_foil_layer_8.mask_string = '0'
positive_foil_layer_8.mask_setting = '0'
positive_foil_layer_8.number_of_activations = '1'
positive_foil_layer_8.init = '"init"'

# Comp instance negative_electrode_layer_8, placement and parameters
negative_electrode_layer_8 = instr.add_component('negative_electrode_layer_8','Union_box', AT=['0', 'negative_foil_center [ 8 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

negative_electrode_layer_8.material_string = '"LiC6"'
negative_electrode_layer_8.priority = '50.4 + 8.0'
negative_electrode_layer_8.xwidth = 'battery_width - end_safety'
negative_electrode_layer_8.yheight = '2 * negative_electrode_thickness_m + negative_foil_thickness_m'
negative_electrode_layer_8.zdepth = 'battery_depth - end_safety'
negative_electrode_layer_8.xwidth2 = '-1'
negative_electrode_layer_8.yheight2 = '-1'
negative_electrode_layer_8.visualize = '1'
negative_electrode_layer_8.target_index = '0'
negative_electrode_layer_8.target_x = '0'
negative_electrode_layer_8.target_y = '0'
negative_electrode_layer_8.target_z = '0'
negative_electrode_layer_8.focus_aw = '0'
negative_electrode_layer_8.focus_ah = '0'
negative_electrode_layer_8.focus_xw = '0'
negative_electrode_layer_8.focus_xh = '0'
negative_electrode_layer_8.focus_r = '0'
negative_electrode_layer_8.p_interact = '0'
negative_electrode_layer_8.mask_string = '0'
negative_electrode_layer_8.mask_setting = '0'
negative_electrode_layer_8.number_of_activations = '1'
negative_electrode_layer_8.init = '"init"'

# Comp instance negative_foil_layer_8, placement and parameters
negative_foil_layer_8 = instr.add_component('negative_foil_layer_8','Union_box', AT=['0', 'negative_foil_center [ 8 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

negative_foil_layer_8.material_string = '"Copper"'
negative_foil_layer_8.priority = '50.5 + 8.0'
negative_foil_layer_8.xwidth = 'battery_width -2 * end_safety'
negative_foil_layer_8.yheight = 'positive_foil_thickness_m'
negative_foil_layer_8.zdepth = 'battery_depth -2 * end_safety'
negative_foil_layer_8.xwidth2 = '-1'
negative_foil_layer_8.yheight2 = '-1'
negative_foil_layer_8.visualize = '1'
negative_foil_layer_8.target_index = '0'
negative_foil_layer_8.target_x = '0'
negative_foil_layer_8.target_y = '0'
negative_foil_layer_8.target_z = '0'
negative_foil_layer_8.focus_aw = '0'
negative_foil_layer_8.focus_ah = '0'
negative_foil_layer_8.focus_xw = '0'
negative_foil_layer_8.focus_xh = '0'
negative_foil_layer_8.focus_r = '0'
negative_foil_layer_8.p_interact = '0'
negative_foil_layer_8.mask_string = '0'
negative_foil_layer_8.mask_setting = '0'
negative_foil_layer_8.number_of_activations = '1'
negative_foil_layer_8.init = '"init"'

# Comp instance positive_electrode_layer_9, placement and parameters
positive_electrode_layer_9 = instr.add_component('positive_electrode_layer_9','Union_box', AT=['0', 'positive_foil_center [ 9 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

positive_electrode_layer_9.material_string = '"LiFePO4"'
positive_electrode_layer_9.priority = '50.1 + 9.0'
positive_electrode_layer_9.xwidth = 'battery_width - end_safety'
positive_electrode_layer_9.yheight = '2 * positive_electrode_thickness_m + positive_foil_thickness_m'
positive_electrode_layer_9.zdepth = 'battery_depth - end_safety'
positive_electrode_layer_9.xwidth2 = '-1'
positive_electrode_layer_9.yheight2 = '-1'
positive_electrode_layer_9.visualize = '1'
positive_electrode_layer_9.target_index = '0'
positive_electrode_layer_9.target_x = '0'
positive_electrode_layer_9.target_y = '0'
positive_electrode_layer_9.target_z = '0'
positive_electrode_layer_9.focus_aw = '0'
positive_electrode_layer_9.focus_ah = '0'
positive_electrode_layer_9.focus_xw = '0'
positive_electrode_layer_9.focus_xh = '0'
positive_electrode_layer_9.focus_r = '0'
positive_electrode_layer_9.p_interact = '0'
positive_electrode_layer_9.mask_string = '0'
positive_electrode_layer_9.mask_setting = '0'
positive_electrode_layer_9.number_of_activations = '1'
positive_electrode_layer_9.init = '"init"'

# Comp instance positive_foil_layer_9, placement and parameters
positive_foil_layer_9 = instr.add_component('positive_foil_layer_9','Union_box', AT=['0', 'positive_foil_center [ 9 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

positive_foil_layer_9.material_string = '"Aluminum"'
positive_foil_layer_9.priority = '50.2 + 9.0'
positive_foil_layer_9.xwidth = 'battery_width -2 * end_safety'
positive_foil_layer_9.yheight = 'positive_foil_thickness_m'
positive_foil_layer_9.zdepth = 'battery_depth -2 * end_safety'
positive_foil_layer_9.xwidth2 = '-1'
positive_foil_layer_9.yheight2 = '-1'
positive_foil_layer_9.visualize = '1'
positive_foil_layer_9.target_index = '0'
positive_foil_layer_9.target_x = '0'
positive_foil_layer_9.target_y = '0'
positive_foil_layer_9.target_z = '0'
positive_foil_layer_9.focus_aw = '0'
positive_foil_layer_9.focus_ah = '0'
positive_foil_layer_9.focus_xw = '0'
positive_foil_layer_9.focus_xh = '0'
positive_foil_layer_9.focus_r = '0'
positive_foil_layer_9.p_interact = '0'
positive_foil_layer_9.mask_string = '0'
positive_foil_layer_9.mask_setting = '0'
positive_foil_layer_9.number_of_activations = '1'
positive_foil_layer_9.init = '"init"'

# Comp instance negative_electrode_layer_9, placement and parameters
negative_electrode_layer_9 = instr.add_component('negative_electrode_layer_9','Union_box', AT=['0', 'negative_foil_center [ 9 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

negative_electrode_layer_9.material_string = '"LiC6"'
negative_electrode_layer_9.priority = '50.4 + 9.0'
negative_electrode_layer_9.xwidth = 'battery_width - end_safety'
negative_electrode_layer_9.yheight = '2 * negative_electrode_thickness_m + negative_foil_thickness_m'
negative_electrode_layer_9.zdepth = 'battery_depth - end_safety'
negative_electrode_layer_9.xwidth2 = '-1'
negative_electrode_layer_9.yheight2 = '-1'
negative_electrode_layer_9.visualize = '1'
negative_electrode_layer_9.target_index = '0'
negative_electrode_layer_9.target_x = '0'
negative_electrode_layer_9.target_y = '0'
negative_electrode_layer_9.target_z = '0'
negative_electrode_layer_9.focus_aw = '0'
negative_electrode_layer_9.focus_ah = '0'
negative_electrode_layer_9.focus_xw = '0'
negative_electrode_layer_9.focus_xh = '0'
negative_electrode_layer_9.focus_r = '0'
negative_electrode_layer_9.p_interact = '0'
negative_electrode_layer_9.mask_string = '0'
negative_electrode_layer_9.mask_setting = '0'
negative_electrode_layer_9.number_of_activations = '1'
negative_electrode_layer_9.init = '"init"'

# Comp instance negative_foil_layer_9, placement and parameters
negative_foil_layer_9 = instr.add_component('negative_foil_layer_9','Union_box', AT=['0', 'negative_foil_center [ 9 ]', '0'], AT_RELATIVE='battery_bottom', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='battery_bottom')

negative_foil_layer_9.material_string = '"Copper"'
negative_foil_layer_9.priority = '50.5 + 9.0'
negative_foil_layer_9.xwidth = 'battery_width -2 * end_safety'
negative_foil_layer_9.yheight = 'positive_foil_thickness_m'
negative_foil_layer_9.zdepth = 'battery_depth -2 * end_safety'
negative_foil_layer_9.xwidth2 = '-1'
negative_foil_layer_9.yheight2 = '-1'
negative_foil_layer_9.visualize = '1'
negative_foil_layer_9.target_index = '0'
negative_foil_layer_9.target_x = '0'
negative_foil_layer_9.target_y = '0'
negative_foil_layer_9.target_z = '0'
negative_foil_layer_9.focus_aw = '0'
negative_foil_layer_9.focus_ah = '0'
negative_foil_layer_9.focus_xw = '0'
negative_foil_layer_9.focus_xh = '0'
negative_foil_layer_9.focus_r = '0'
negative_foil_layer_9.p_interact = '0'
negative_foil_layer_9.mask_string = '0'
negative_foil_layer_9.mask_setting = '0'
negative_foil_layer_9.number_of_activations = '1'
negative_foil_layer_9.init = '"init"'

# Comp instance battery, placement and parameters
battery = instr.add_component('battery','Union_master', AT=['0', '0', '0'], AT_RELATIVE='samplearm', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='samplearm')
# WHEN ( sample_used == 0 ) at battery
battery.set_WHEN('( sample_used == 0 )')

battery.verbal = '1'
battery.list_verbal = '0'
battery.finally_verbal = '0'
battery.allow_inside_start = '0'
battery.enable_tagging = '0'
battery.history_limit = '300000'
battery.enable_conditionals = '1'
battery.inherit_number_of_scattering_events = '0'
battery.init = '"init"'

# Comp instance Stop, placement and parameters
Stop = instr.add_component('Stop','Union_stop', AT=['0', '0', '0'], AT_RELATIVE='samplearm', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='samplearm')


# Comp instance edge_sample, placement and parameters
edge_sample = instr.add_component('edge_sample','Incoherent', AT=['sample_x / 2', '0', '0'], AT_RELATIVE='samplearm', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='samplearm')
# WHEN ( sample_used == 1 ) at edge_sample
edge_sample.set_WHEN('( sample_used == 1 )')

edge_sample.geometry = '0'
edge_sample.radius = '0'
edge_sample.xwidth = 'sample_x'
edge_sample.yheight = 'sample_y'
edge_sample.zdepth = 'sample_z'
edge_sample.thickness = '0'
edge_sample.target_x = 'det_w'
edge_sample.target_y = 'det_h'
edge_sample.target_z = '0'
edge_sample.focus_r = '0'
edge_sample.focus_xw = '0'
edge_sample.focus_yh = '0'
edge_sample.focus_aw = '0'
edge_sample.focus_ah = '0'
edge_sample.target_index = '1'
edge_sample.pack = '1'
edge_sample.p_interact = 'frac_interact'
edge_sample.f_QE = '0'
edge_sample.gamma = '0'
edge_sample.Etrans = '0'
edge_sample.deltaE = '0'
edge_sample.sigma_abs = 'sigma_abs'
edge_sample.sigma_inc = 'sigma_inc'
edge_sample.Vc = 'Vc'
edge_sample.concentric = '0'
edge_sample.order = '0'

# Comp instance PSD_1cm_detector_50mum, placement and parameters
PSD_1cm_detector_50mum = instr.add_component('PSD_1cm_detector_50mum','PSD_monitor', AT=['0', '0', 'L + l + battery_depth'], AT_RELATIVE='pinhole', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='pinhole')

PSD_1cm_detector_50mum.nx = '500'
PSD_1cm_detector_50mum.ny = '200'
PSD_1cm_detector_50mum.filename = '"2D_PSD_detector"'
PSD_1cm_detector_50mum.xmin = '-0.05'
PSD_1cm_detector_50mum.xmax = '0.05'
PSD_1cm_detector_50mum.ymin = '-0.05'
PSD_1cm_detector_50mum.ymax = '0.05'
PSD_1cm_detector_50mum.xwidth = '0.006'
PSD_1cm_detector_50mum.yheight = 'battery_width'
PSD_1cm_detector_50mum.restore_neutron = '1'
PSD_1cm_detector_50mum.nowritefile = '0'

# Comp instance edge_monitor_50mum, placement and parameters
edge_monitor_50mum = instr.add_component('edge_monitor_50mum','PSDlin_monitor', AT=['0', '0', 'L + l + 0.0001'], AT_RELATIVE='pinhole', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='pinhole')

edge_monitor_50mum.nbins = '500'
edge_monitor_50mum.filename = '"edge_monitor"'
edge_monitor_50mum.xmin = '-0.05'
edge_monitor_50mum.xmax = '0.05'
edge_monitor_50mum.ymin = '-0.05'
edge_monitor_50mum.ymax = '0.05'
edge_monitor_50mum.nowritefile = '0'
edge_monitor_50mum.xwidth = '0.006'
edge_monitor_50mum.yheight = 'battery_width'
edge_monitor_50mum.restore_neutron = '0'
edge_monitor_50mum.vertical = '0'

# Comp instance edge_monitor_diff, placement and parameters
edge_monitor_diff = instr.add_component('edge_monitor_diff','PSDlin_diff_monitor', AT=['0', '0', 'L + l + 0.0002'], AT_RELATIVE='pinhole', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='pinhole')

edge_monitor_diff.nx = '50'
edge_monitor_diff.filename = '"edge_monitor_zoom"'
edge_monitor_diff.xmin = '-0.00031'
edge_monitor_diff.xmax = '0.00026'
edge_monitor_diff.ymin = '-0.05'
edge_monitor_diff.ymax = '0.05'
edge_monitor_diff.nowritefile = '0'
edge_monitor_diff.xwidth = '0'
edge_monitor_diff.yheight = '0.02'
edge_monitor_diff.restore_neutron = '0'

# Instruct McStasscript not to 'check everythng'
instr.settings(checks=False)
# (also, this is where one can add e.g. seed=1000, ncount=1e7, mpi=8, openacc=True, force_compile=False etc.)


# Visualise with default parameters.
instr.show_instrument()


# Generate a dataset with default parameters.
data = instr.backengine()

# Overview plot:
ms.make_sub_plot(data)


# Other useful commands follow...

# One plot pr. window
#ms.make_plot(data)

# Load another dataset
#data2 = ms.load_data('some_other_folder')

# Adjusting a specific plot
#ms.name_plot_options("PSD_4PI", data, log=1, colormap="hot", orders_of_mag=5)


# Bring up the 'interface' - only relevant in Jupyter
#%matplotlib widget
#import mcstasscript.jb_interface as ms_widget
#ms_widget.show(data)


# Bring up the simulation 'interface' - only relevant in Jupyter
#%matplotlib widget
#import mcstasscript.jb_interface as ms_widget
#sim_widget = ms_widget.SimInterface(instr)
#sim_widget.show_interface()
#data = sim_widget.get_data()


# end of generated Python code Radiography_Lithium_Battery_generated.py 
