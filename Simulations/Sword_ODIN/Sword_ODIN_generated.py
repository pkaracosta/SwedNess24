#!/usr/bin/env python3
# Automatically generated file. 
# Format:    Python script code
# McStas <http://www.mcstas.org>
# Instrument: Sword_ODIN.instr (Sword_Odin)
# Date:       Wed Sep  6 07:18:36 2023
# File:       Sword_ODIN_generated.py

import mcstasscript as ms

# Python McStas instrument description
instr = ms.McStas_instr("Sword_Odin_generated", author = "McCode Py-Generator", origin = "ESS DMSC")

# Add collected DEPENDENCY strings
instr.set_dependency(' -I@MCCODE_LIB@/share/ -DFUNNEL ')

# *****************************************************************************
# * Start of instrument 'Sword_Odin' generated code
# *****************************************************************************
# MCSTAS system dir is "/Users/pkwi/McStas/mcstas/3.x-dev/"


# *****************************************************************************
# * instrument 'Sword_Odin' and components DECLARE
# *****************************************************************************

# Instrument parameters:

chopper_mode = instr.add_parameter('double', 'chopper_mode', value=5, comment='Parameter type (double) added by McCode py-generator')
Lambda = instr.add_parameter('double', 'Lambda', value=0, comment='Parameter type (double) added by McCode py-generator')
Sample = instr.add_parameter('double', 'Sample', value=1, comment='Parameter type (double) added by McCode py-generator')
pinhole_diameter = instr.add_parameter('double', 'pinhole_diameter', value=0.1, comment='Parameter type (double) added by McCode py-generator')
pinhole_detector_distance = instr.add_parameter('double', 'pinhole_detector_distance', value=10.0, comment='Parameter type (double) added by McCode py-generator')
pinhole_sample_distance = instr.add_parameter('double', 'pinhole_sample_distance', value=9, comment='Parameter type (double) added by McCode py-generator')
X_sample_pos = instr.add_parameter('double', 'X_sample_pos', value=0.0, comment='Parameter type (double) added by McCode py-generator')
Y_sample_pos = instr.add_parameter('double', 'Y_sample_pos', value=0.0, comment='Parameter type (double) added by McCode py-generator')
angle = instr.add_parameter('double', 'angle', value=0, comment='Parameter type (double) added by McCode py-generator')
Zoom = instr.add_parameter('double', 'Zoom', value=1, comment='Parameter type (double) added by McCode py-generator')

component_definition_metadata = {
}
instr.append_declare(r'''
double sword_height;
double rust_thickness;
double blade_mask_radius;
double blade_tip_mask_radius;
double cut_radius;
double cut_depth;
double sword_depth;
double sword_width;
double blade_start_width;
double blade_top_width;
double blade_tip_start_width;
double core_width_top;
double core_side_top_length;
double core_width_bottom;
double core_side_bottom_length;
double width_angle;
double cut_angle;
double radius_multiply;
double tip_x_multiplier;

double tip_height;

double blade_angle_deg;
double blade_angle_tip_deg;

char rust_string[128];
char spacial_resolution[128];
char wavelength_spectrum[128];
int rust_used;
double Fe3O4_content;
double Fe2O3_content;
double FeOOH_content;
double mixture;

double Dlambda;
double L_min;
double L_max;
''')


instr.append_initialize(r'''

rust_used=1;
Fe3O4_content = 0.34;
Fe2O3_content = 0.33;
FeOOH_content = 0.33;
mixture=0.1;


sword_width = 0.06;
blade_start_width = 0.032;
sword_depth = 0.015/2.0;
sword_height = 0.6;
rust_thickness = 0.002;
blade_mask_radius = 0.07;
cut_depth = 0.002/1.5;
cut_radius = (0.5*blade_start_width*0.5*blade_start_width+cut_depth*cut_depth)/2.0/cut_depth;
core_width_top = 0.032;
core_side_top_length = core_width_top/sqrt(2);
core_width_bottom = 0.0404;
width_angle = 1.0/8.0;
cut_angle = 1.0/6.0;
blade_tip_start_width = -0.0;
blade_tip_mask_radius = 0.07;



core_side_bottom_length = core_width_bottom/sqrt(2);



tip_height = 0.21;
tip_x_multiplier = -0.5;
radius_multiply = 1.0;

// Calculate sword slope
blade_angle_deg = 180/3.14159*atan((core_width_bottom-core_width_top)/sword_height);
blade_angle_tip_deg = 180/3.14159*atan((0.8*core_width_top)/tip_height);

// change in width
blade_top_width = blade_start_width - 2.0*(core_width_bottom-core_width_top);


if (rust_used == 0){sprintf(rust_string, "Fe3O4");}
if (rust_used == 1){sprintf(rust_string, "Fe2O3");}
if (rust_used == 2){sprintf(rust_string, "FeOOH");}
if (rust_used == 3){sprintf(rust_string, "iron_mix");}
if (rust_used == 4){sprintf(rust_string, "Fe_alpha");}
if (rust_used == 5){sprintf(rust_string, "rust_mix");}


if (chopper_mode == 0){sprintf(wavelength_spectrum, "Filters/I_lambda_C0.dat"); Dlambda = 0.1;}
if (chopper_mode == 1){sprintf(wavelength_spectrum, "Filters/I_lambda_C1.dat"); Dlambda = 0.05;}
if (chopper_mode == 2){sprintf(wavelength_spectrum, "Filters/I_lambda_C2.dat"); Dlambda = 0.04;}
if (chopper_mode == 3){sprintf(wavelength_spectrum, "Filters/I_lambda_C3.dat"); Dlambda = 0.03;}
if (chopper_mode == 4){sprintf(wavelength_spectrum, "Filters/I_lambda_C4.dat"); Dlambda = 0.02;}
if (chopper_mode == 5){sprintf(wavelength_spectrum, "Filters/I_lambda_C5.dat"); Dlambda = 0.25;}


if (Lambda < 1.0){Lambda=0;}
if (Lambda > 10.0){Lambda=0;}
if (Lambda == 0){
L_min = 0.0;
L_max = 10.0;
}
else{
L_min = Lambda-0.1;
L_max = Lambda+0.1;
}

if (chopper_mode == 5){
L_min = 0.0;
L_max = 10.0;
}

if (chopper_mode < 0){chopper_mode=5;}
if (chopper_mode > 5){chopper_mode=5;}

if (pinhole_detector_distance < 10){pinhole_detector_distance=10;}
if (pinhole_detector_distance > 25){pinhole_detector_distance=25;}

if (pinhole_sample_distance < 1){pinhole_sample_distance=1;}
if (pinhole_sample_distance > 25){pinhole_sample_distance=25;}

if (pinhole_diameter < 0.01){pinhole_diameter=0.01;}
if (pinhole_diameter > 0.1){pinhole_diameter=0.1;}

if (Sample < 0){Sample=0;}
if (Sample > 1){Sample=0;}

if (Zoom < 1){Zoom=1;}
if (Zoom > 10){Zoom=10;}

sprintf(spacial_resolution, "Filters/2D_Filter_n600_25m.dat");

''')


# *****************************************************************************
# * instrument 'Sword_Odin' TRACE
# *****************************************************************************

# Comp instance a1, placement and parameters
a1 = instr.add_component('a1','Progress_bar')

a1.profile = '"NULL"'
a1.percent = '10'
a1.flag_save = '0'
a1.minutes = '0'

# Comp instance source_gen, placement and parameters
source_gen = instr.add_component('source_gen','Source_gen', AT=['0', '0', '0'], AT_RELATIVE='a1', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='a1')

source_gen.flux_file = 'wavelength_spectrum'
source_gen.xdiv_file = '"NULL"'
source_gen.ydiv_file = '"NULL"'
source_gen.radius = 'pinhole_diameter'
source_gen.dist = 'pinhole_detector_distance + 0.01'
source_gen.focus_xw = '0.3 / Zoom'
source_gen.focus_yh = '0.3 / Zoom'
source_gen.focus_aw = '0'
source_gen.focus_ah = '0'
source_gen.E0 = '0'
source_gen.dE = '0'
source_gen.lambda0 = '0'
source_gen.dlambda = '0'
source_gen.I1 = '1'
source_gen.yheight = '0.1'
source_gen.xwidth = '0.1'
source_gen.verbose = '1'
source_gen.T1 = '0'
source_gen.flux_file_perAA = '0'
source_gen.flux_file_log = '0'
source_gen.Lmin = 'L_min'
source_gen.Lmax = 'L_max'
source_gen.Emin = '0'
source_gen.Emax = '0'
source_gen.T2 = '0'
source_gen.I2 = '0'
source_gen.T3 = '0'
source_gen.I3 = '0'
source_gen.zdepth = '0'
source_gen.target_index = '+ 1'

# Comp instance graph, placement and parameters
graph = instr.add_component('graph','Arm', AT=['0', '0', '0.002'], AT_RELATIVE='a1', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='a1')


# Comp instance Lamb_Dif, placement and parameters
Lamb_Dif = instr.add_component('Lamb_Dif','Wavelength_Diffuser', AT=['0', '0', '0.003'], AT_RELATIVE='a1', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='a1')

Lamb_Dif.dlambda = 'Dlambda'

# Comp instance init, placement and parameters
init = instr.add_component('init','Union_init')


# Comp instance Al_incoherent, placement and parameters
Al_incoherent = instr.add_component('Al_incoherent','Incoherent_process')

Al_incoherent.sigma = '4 * 0.0082'
Al_incoherent.f_QE = '0'
Al_incoherent.gamma = '0'
Al_incoherent.packing_factor = '1'
Al_incoherent.unit_cell_volume = '66.4'
Al_incoherent.interact_fraction = '-1'
Al_incoherent.init = '"init"'

# Comp instance Al_powder, placement and parameters
Al_powder = instr.add_component('Al_powder','Powder_process')

Al_powder.reflections = '"Al.laz"'
Al_powder.packing_factor = '1'
Al_powder.Vc = '0'
Al_powder.delta_d_d = '0'
Al_powder.DW = '0'
Al_powder.nb_atoms = '1'
Al_powder.d_phi = '0'
Al_powder.density = '0'
Al_powder.weight = '0'
Al_powder.barns = '1'
Al_powder.Strain = '0'
Al_powder.interact_fraction = '-1'
Al_powder.format = '{ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 }'
Al_powder.init = '"init"'

# Comp instance Al, placement and parameters
Al = instr.add_component('Al','Union_make_material')

Al.process_string = '"Al_incoherent,Al_powder"'
Al.my_absorption = '100 * 4 * 0.231 / 66.4'
Al.absorber = '0'
Al.init = '"init"'

# Comp instance Fe_incoherent, placement and parameters
Fe_incoherent = instr.add_component('Fe_incoherent','Incoherent_process')

Fe_incoherent.sigma = '2 * 0.4'
Fe_incoherent.f_QE = '0'
Fe_incoherent.gamma = '0'
Fe_incoherent.packing_factor = '1'
Fe_incoherent.unit_cell_volume = '24.04'
Fe_incoherent.interact_fraction = '-1'
Fe_incoherent.init = '"init"'

# Comp instance Fe_powder, placement and parameters
Fe_powder = instr.add_component('Fe_powder','Powder_process')

Fe_powder.reflections = '"Fe.laz"'
Fe_powder.packing_factor = '1'
Fe_powder.Vc = '0'
Fe_powder.delta_d_d = '0'
Fe_powder.DW = '0'
Fe_powder.nb_atoms = '1'
Fe_powder.d_phi = '0'
Fe_powder.density = '0'
Fe_powder.weight = '0'
Fe_powder.barns = '1'
Fe_powder.Strain = '0'
Fe_powder.interact_fraction = '-1'
Fe_powder.format = '{ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 }'
Fe_powder.init = '"init"'

# Comp instance Fe, placement and parameters
Fe = instr.add_component('Fe','Union_make_material')

Fe.process_string = '"NULL"'
Fe.my_absorption = '100 * 2 * 2.56 / 24.04'
Fe.absorber = '0'
Fe.init = '"init"'

# Comp instance Fe_alpha_incoherent, placement and parameters
Fe_alpha_incoherent = instr.add_component('Fe_alpha_incoherent','Incoherent_process')

Fe_alpha_incoherent.sigma = '0.80000'
Fe_alpha_incoherent.f_QE = '0'
Fe_alpha_incoherent.gamma = '0'
Fe_alpha_incoherent.packing_factor = '1'
Fe_alpha_incoherent.unit_cell_volume = '23.55352'
Fe_alpha_incoherent.interact_fraction = '-1'
Fe_alpha_incoherent.init = '"init"'

# Comp instance Fe_alpha_powder, placement and parameters
Fe_alpha_powder = instr.add_component('Fe_alpha_powder','Powder_process')

Fe_alpha_powder.reflections = '"alpha_Fe.laz"'
Fe_alpha_powder.packing_factor = '1'
Fe_alpha_powder.Vc = '0'
Fe_alpha_powder.delta_d_d = '0'
Fe_alpha_powder.DW = '0'
Fe_alpha_powder.nb_atoms = '1'
Fe_alpha_powder.d_phi = '0'
Fe_alpha_powder.density = '0'
Fe_alpha_powder.weight = '0'
Fe_alpha_powder.barns = '1'
Fe_alpha_powder.Strain = '0'
Fe_alpha_powder.interact_fraction = '-1'
Fe_alpha_powder.format = '{ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 }'
Fe_alpha_powder.init = '"init"'

# Comp instance Fe_alpha, placement and parameters
Fe_alpha = instr.add_component('Fe_alpha','Union_make_material')

Fe_alpha.process_string = '"NULL"'
Fe_alpha.my_absorption = '100 * 5.12000 / 23.55352'
Fe_alpha.absorber = '0'
Fe_alpha.init = '"init"'

# Comp instance cementite_incoherent, placement and parameters
cementite_incoherent = instr.add_component('cementite_incoherent','Incoherent_process')

cementite_incoherent.sigma = '4.80398'
cementite_incoherent.f_QE = '0'
cementite_incoherent.gamma = '0'
cementite_incoherent.packing_factor = '1'
cementite_incoherent.unit_cell_volume = '155.15118'
cementite_incoherent.interact_fraction = '-1'
cementite_incoherent.init = '"init"'

# Comp instance cementite_powder, placement and parameters
cementite_powder = instr.add_component('cementite_powder','Powder_process')

cementite_powder.reflections = '"cementite_300K.laz"'
cementite_powder.packing_factor = '1'
cementite_powder.Vc = '0'
cementite_powder.delta_d_d = '0'
cementite_powder.DW = '0'
cementite_powder.nb_atoms = '1'
cementite_powder.d_phi = '0'
cementite_powder.density = '0'
cementite_powder.weight = '0'
cementite_powder.barns = '1'
cementite_powder.Strain = '0'
cementite_powder.interact_fraction = '-1'
cementite_powder.format = '{ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 }'
cementite_powder.init = '"init"'

# Comp instance cementite, placement and parameters
cementite = instr.add_component('cementite','Union_make_material')

cementite.process_string = '"NULL"'
cementite.my_absorption = '100 * 30.73400 / 155.15118'
cementite.absorber = '0'
cementite.init = '"init"'

# Comp instance mix_Fe_alpha_incoherent, placement and parameters
mix_Fe_alpha_incoherent = instr.add_component('mix_Fe_alpha_incoherent','Incoherent_process')

mix_Fe_alpha_incoherent.sigma = '0.80000'
mix_Fe_alpha_incoherent.f_QE = '0'
mix_Fe_alpha_incoherent.gamma = '0'
mix_Fe_alpha_incoherent.packing_factor = '1.0 - mixture'
mix_Fe_alpha_incoherent.unit_cell_volume = '23.55352'
mix_Fe_alpha_incoherent.interact_fraction = '-1'
mix_Fe_alpha_incoherent.init = '"init"'

# Comp instance mix_cementite_incoherent, placement and parameters
mix_cementite_incoherent = instr.add_component('mix_cementite_incoherent','Incoherent_process')

mix_cementite_incoherent.sigma = '4.80398'
mix_cementite_incoherent.f_QE = '0'
mix_cementite_incoherent.gamma = '0'
mix_cementite_incoherent.packing_factor = 'mixture'
mix_cementite_incoherent.unit_cell_volume = '155.15118'
mix_cementite_incoherent.interact_fraction = '-1'
mix_cementite_incoherent.init = '"init"'

# Comp instance mix_Fe_alpha_powder, placement and parameters
mix_Fe_alpha_powder = instr.add_component('mix_Fe_alpha_powder','Powder_process')

mix_Fe_alpha_powder.reflections = '"alpha_Fe.laz"'
mix_Fe_alpha_powder.packing_factor = '1.0 - mixture'
mix_Fe_alpha_powder.Vc = '0'
mix_Fe_alpha_powder.delta_d_d = '0'
mix_Fe_alpha_powder.DW = '0'
mix_Fe_alpha_powder.nb_atoms = '1'
mix_Fe_alpha_powder.d_phi = '0'
mix_Fe_alpha_powder.density = '0'
mix_Fe_alpha_powder.weight = '0'
mix_Fe_alpha_powder.barns = '1'
mix_Fe_alpha_powder.Strain = '0'
mix_Fe_alpha_powder.interact_fraction = '-1'
mix_Fe_alpha_powder.format = '{ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 }'
mix_Fe_alpha_powder.init = '"init"'

# Comp instance mix_cementite_powder, placement and parameters
mix_cementite_powder = instr.add_component('mix_cementite_powder','Powder_process')

mix_cementite_powder.reflections = '"cementite_300K.laz"'
mix_cementite_powder.packing_factor = 'mixture'
mix_cementite_powder.Vc = '0'
mix_cementite_powder.delta_d_d = '0'
mix_cementite_powder.DW = '0'
mix_cementite_powder.nb_atoms = '1'
mix_cementite_powder.d_phi = '0'
mix_cementite_powder.density = '0'
mix_cementite_powder.weight = '0'
mix_cementite_powder.barns = '1'
mix_cementite_powder.Strain = '0'
mix_cementite_powder.interact_fraction = '-1'
mix_cementite_powder.format = '{ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 }'
mix_cementite_powder.init = '"init"'

# Comp instance iron_mix, placement and parameters
iron_mix = instr.add_component('iron_mix','Union_make_material')

iron_mix.process_string = '"NULL"'
iron_mix.my_absorption = 'mixture * 100 * 30.73400 / 155.15118 + ( 1.0 - mixture ) * 100 * 5.12000 / 23.55352'
iron_mix.absorber = '0'
iron_mix.init = '"init"'

# Comp instance Fe3O4_incoherent, placement and parameters
Fe3O4_incoherent = instr.add_component('Fe3O4_incoherent','Incoherent_process')

Fe3O4_incoherent.sigma = '2.40639'
Fe3O4_incoherent.f_QE = '0'
Fe3O4_incoherent.gamma = '0'
Fe3O4_incoherent.packing_factor = '1'
Fe3O4_incoherent.unit_cell_volume = '157.15089'
Fe3O4_incoherent.interact_fraction = '-1'
Fe3O4_incoherent.init = '"init"'

# Comp instance Fe3O4_powder, placement and parameters
Fe3O4_powder = instr.add_component('Fe3O4_powder','Powder_process')

Fe3O4_powder.reflections = '"Fe3O4_mp-19306_computed.laz"'
Fe3O4_powder.packing_factor = '1'
Fe3O4_powder.Vc = '0'
Fe3O4_powder.delta_d_d = '0'
Fe3O4_powder.DW = '0'
Fe3O4_powder.nb_atoms = '1'
Fe3O4_powder.d_phi = '0'
Fe3O4_powder.density = '0'
Fe3O4_powder.weight = '0'
Fe3O4_powder.barns = '1'
Fe3O4_powder.Strain = '0'
Fe3O4_powder.interact_fraction = '-1'
Fe3O4_powder.format = '{ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 }'
Fe3O4_powder.init = '"init"'

# Comp instance Fe3O4, placement and parameters
Fe3O4 = instr.add_component('Fe3O4','Union_make_material')

Fe3O4.process_string = '"Fe3O4_incoherent,Fe3O4_powder"'
Fe3O4.my_absorption = '100 * 15.36152 / 157.15089'
Fe3O4.absorber = '0'
Fe3O4.init = '"init"'

# Comp instance Fe2O3_incoherent, placement and parameters
Fe2O3_incoherent = instr.add_component('Fe2O3_incoherent','Incoherent_process')

Fe2O3_incoherent.sigma = '4.81438'
Fe2O3_incoherent.f_QE = '0'
Fe2O3_incoherent.gamma = '0'
Fe2O3_incoherent.packing_factor = '1'
Fe2O3_incoherent.unit_cell_volume = '302.72198'
Fe2O3_incoherent.interact_fraction = '-1'
Fe2O3_incoherent.init = '"init"'

# Comp instance Fe2O3_powder, placement and parameters
Fe2O3_powder = instr.add_component('Fe2O3_powder','Powder_process')

Fe2O3_powder.reflections = '"Fe2O3.laz"'
Fe2O3_powder.packing_factor = '1'
Fe2O3_powder.Vc = '0'
Fe2O3_powder.delta_d_d = '0'
Fe2O3_powder.DW = '0'
Fe2O3_powder.nb_atoms = '1'
Fe2O3_powder.d_phi = '0'
Fe2O3_powder.density = '0'
Fe2O3_powder.weight = '0'
Fe2O3_powder.barns = '1'
Fe2O3_powder.Strain = '0'
Fe2O3_powder.interact_fraction = '-1'
Fe2O3_powder.format = '{ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 }'
Fe2O3_powder.init = '"init"'

# Comp instance Fe2O3, placement and parameters
Fe2O3 = instr.add_component('Fe2O3','Union_make_material')

Fe2O3.process_string = '"Fe2O3_incoherent,Fe2O3_powder"'
Fe2O3.my_absorption = '100 * 30.72342 / 302.72198'
Fe2O3.absorber = '0'
Fe2O3.init = '"init"'

# Comp instance FeOOH_incoherent, placement and parameters
FeOOH_incoherent = instr.add_component('FeOOH_incoherent','Incoherent_process')

FeOOH_incoherent.sigma = '322.63895'
FeOOH_incoherent.f_QE = '0'
FeOOH_incoherent.gamma = '0'
FeOOH_incoherent.packing_factor = '1'
FeOOH_incoherent.unit_cell_volume = '302.72198'
FeOOH_incoherent.interact_fraction = '-1'
FeOOH_incoherent.init = '"init"'

# Comp instance FeOOH_powder, placement and parameters
FeOOH_powder = instr.add_component('FeOOH_powder','Powder_process')

FeOOH_powder.reflections = '"FeOOH.laz"'
FeOOH_powder.packing_factor = '1'
FeOOH_powder.Vc = '0'
FeOOH_powder.delta_d_d = '0'
FeOOH_powder.DW = '0'
FeOOH_powder.nb_atoms = '1'
FeOOH_powder.d_phi = '0'
FeOOH_powder.density = '0'
FeOOH_powder.weight = '0'
FeOOH_powder.barns = '1'
FeOOH_powder.Strain = '0'
FeOOH_powder.interact_fraction = '-1'
FeOOH_powder.format = '{ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 }'
FeOOH_powder.init = '"init"'

# Comp instance FeOOH, placement and parameters
FeOOH = instr.add_component('FeOOH','Union_make_material')

FeOOH.process_string = '"FeOOH_incoherent,FeOOH_powder"'
FeOOH.my_absorption = '100 * 11.57192 / 302.72198'
FeOOH.absorber = '0'
FeOOH.init = '"init"'

# Comp instance Fe3O4_incoherent2, placement and parameters
Fe3O4_incoherent2 = instr.add_component('Fe3O4_incoherent2','Incoherent_process')

Fe3O4_incoherent2.sigma = '2.40639'
Fe3O4_incoherent2.f_QE = '0'
Fe3O4_incoherent2.gamma = '0'
Fe3O4_incoherent2.packing_factor = 'Fe3O4_content'
Fe3O4_incoherent2.unit_cell_volume = '157.15089'
Fe3O4_incoherent2.interact_fraction = '-1'
Fe3O4_incoherent2.init = '"init"'

# Comp instance Fe3O4_powder2, placement and parameters
Fe3O4_powder2 = instr.add_component('Fe3O4_powder2','Powder_process')

Fe3O4_powder2.reflections = '"Fe3O4_mp-19306_computed.laz"'
Fe3O4_powder2.packing_factor = 'Fe3O4_content'
Fe3O4_powder2.Vc = '0'
Fe3O4_powder2.delta_d_d = '0'
Fe3O4_powder2.DW = '0'
Fe3O4_powder2.nb_atoms = '1'
Fe3O4_powder2.d_phi = '0'
Fe3O4_powder2.density = '0'
Fe3O4_powder2.weight = '0'
Fe3O4_powder2.barns = '1'
Fe3O4_powder2.Strain = '0'
Fe3O4_powder2.interact_fraction = '-1'
Fe3O4_powder2.format = '{ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 }'
Fe3O4_powder2.init = '"init"'

# Comp instance Fe2O3_incoherent2, placement and parameters
Fe2O3_incoherent2 = instr.add_component('Fe2O3_incoherent2','Incoherent_process')

Fe2O3_incoherent2.sigma = '4.81438'
Fe2O3_incoherent2.f_QE = '0'
Fe2O3_incoherent2.gamma = '0'
Fe2O3_incoherent2.packing_factor = 'Fe2O3_content'
Fe2O3_incoherent2.unit_cell_volume = '302.72198'
Fe2O3_incoherent2.interact_fraction = '-1'
Fe2O3_incoherent2.init = '"init"'

# Comp instance Fe2O3_powder2, placement and parameters
Fe2O3_powder2 = instr.add_component('Fe2O3_powder2','Powder_process')

Fe2O3_powder2.reflections = '"Fe2O3.laz"'
Fe2O3_powder2.packing_factor = 'Fe2O3_content'
Fe2O3_powder2.Vc = '0'
Fe2O3_powder2.delta_d_d = '0'
Fe2O3_powder2.DW = '0'
Fe2O3_powder2.nb_atoms = '1'
Fe2O3_powder2.d_phi = '0'
Fe2O3_powder2.density = '0'
Fe2O3_powder2.weight = '0'
Fe2O3_powder2.barns = '1'
Fe2O3_powder2.Strain = '0'
Fe2O3_powder2.interact_fraction = '-1'
Fe2O3_powder2.format = '{ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 }'
Fe2O3_powder2.init = '"init"'

# Comp instance FeOOH_incoherent2, placement and parameters
FeOOH_incoherent2 = instr.add_component('FeOOH_incoherent2','Incoherent_process')

FeOOH_incoherent2.sigma = '322.63895'
FeOOH_incoherent2.f_QE = '0'
FeOOH_incoherent2.gamma = '0'
FeOOH_incoherent2.packing_factor = 'FeOOH_content'
FeOOH_incoherent2.unit_cell_volume = '302.72198'
FeOOH_incoherent2.interact_fraction = '-1'
FeOOH_incoherent2.init = '"init"'

# Comp instance FeOOH_powder2, placement and parameters
FeOOH_powder2 = instr.add_component('FeOOH_powder2','Powder_process')

FeOOH_powder2.reflections = '"FeOOH.laz"'
FeOOH_powder2.packing_factor = 'FeOOH_content'
FeOOH_powder2.Vc = '0'
FeOOH_powder2.delta_d_d = '0'
FeOOH_powder2.DW = '0'
FeOOH_powder2.nb_atoms = '1'
FeOOH_powder2.d_phi = '0'
FeOOH_powder2.density = '0'
FeOOH_powder2.weight = '0'
FeOOH_powder2.barns = '1'
FeOOH_powder2.Strain = '0'
FeOOH_powder2.interact_fraction = '-1'
FeOOH_powder2.format = '{ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 }'
FeOOH_powder2.init = '"init"'

# Comp instance rust_mix, placement and parameters
rust_mix = instr.add_component('rust_mix','Union_make_material')

rust_mix.process_string = '"Fe3O4_incoherent2,Fe3O4_powder2,Fe2O3_incoherent2,Fe2O3_powder2,FeOOH_incoherent2,FeOOH_powder2"'
rust_mix.my_absorption = 'Fe3O4_content * 100 * 15.36152 / 157.15089 + Fe2O3_content * 100 * 30.72342 / 302.72198 + FeOOH_content * 100 * 11.57192 / 302.72198'
rust_mix.absorber = '0'
rust_mix.init = '"init"'

# Comp instance Fe3O4_incoherent3, placement and parameters
Fe3O4_incoherent3 = instr.add_component('Fe3O4_incoherent3','Incoherent_process')

Fe3O4_incoherent3.sigma = '2.40639'
Fe3O4_incoherent3.f_QE = '0'
Fe3O4_incoherent3.gamma = '0'
Fe3O4_incoherent3.packing_factor = '0.25'
Fe3O4_incoherent3.unit_cell_volume = '157.15089'
Fe3O4_incoherent3.interact_fraction = '-1'
Fe3O4_incoherent3.init = '"init"'

# Comp instance Fe3O4_powder3, placement and parameters
Fe3O4_powder3 = instr.add_component('Fe3O4_powder3','Powder_process')

Fe3O4_powder3.reflections = '"Fe3O4_mp-19306_computed.laz"'
Fe3O4_powder3.packing_factor = '0.25'
Fe3O4_powder3.Vc = '0'
Fe3O4_powder3.delta_d_d = '0'
Fe3O4_powder3.DW = '0'
Fe3O4_powder3.nb_atoms = '1'
Fe3O4_powder3.d_phi = '0'
Fe3O4_powder3.density = '0'
Fe3O4_powder3.weight = '0'
Fe3O4_powder3.barns = '1'
Fe3O4_powder3.Strain = '0'
Fe3O4_powder3.interact_fraction = '-1'
Fe3O4_powder3.format = '{ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 }'
Fe3O4_powder3.init = '"init"'

# Comp instance Fe2O3_incoherent3, placement and parameters
Fe2O3_incoherent3 = instr.add_component('Fe2O3_incoherent3','Incoherent_process')

Fe2O3_incoherent3.sigma = '4.81438'
Fe2O3_incoherent3.f_QE = '0'
Fe2O3_incoherent3.gamma = '0'
Fe2O3_incoherent3.packing_factor = '0.25'
Fe2O3_incoherent3.unit_cell_volume = '302.72198'
Fe2O3_incoherent3.interact_fraction = '-1'
Fe2O3_incoherent3.init = '"init"'

# Comp instance Fe2O3_powder3, placement and parameters
Fe2O3_powder3 = instr.add_component('Fe2O3_powder3','Powder_process')

Fe2O3_powder3.reflections = '"Fe2O3.laz"'
Fe2O3_powder3.packing_factor = '0.25'
Fe2O3_powder3.Vc = '0'
Fe2O3_powder3.delta_d_d = '0'
Fe2O3_powder3.DW = '0'
Fe2O3_powder3.nb_atoms = '1'
Fe2O3_powder3.d_phi = '0'
Fe2O3_powder3.density = '0'
Fe2O3_powder3.weight = '0'
Fe2O3_powder3.barns = '1'
Fe2O3_powder3.Strain = '0'
Fe2O3_powder3.interact_fraction = '-1'
Fe2O3_powder3.format = '{ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 }'
Fe2O3_powder3.init = '"init"'

# Comp instance FeOOH_incoherent3, placement and parameters
FeOOH_incoherent3 = instr.add_component('FeOOH_incoherent3','Incoherent_process')

FeOOH_incoherent3.sigma = '322.63895'
FeOOH_incoherent3.f_QE = '0'
FeOOH_incoherent3.gamma = '0'
FeOOH_incoherent3.packing_factor = '0.5'
FeOOH_incoherent3.unit_cell_volume = '302.72198'
FeOOH_incoherent3.interact_fraction = '-1'
FeOOH_incoherent3.init = '"init"'

# Comp instance FeOOH_powder3, placement and parameters
FeOOH_powder3 = instr.add_component('FeOOH_powder3','Powder_process')

FeOOH_powder3.reflections = '"FeOOH.laz"'
FeOOH_powder3.packing_factor = '0.5'
FeOOH_powder3.Vc = '0'
FeOOH_powder3.delta_d_d = '0'
FeOOH_powder3.DW = '0'
FeOOH_powder3.nb_atoms = '1'
FeOOH_powder3.d_phi = '0'
FeOOH_powder3.density = '0'
FeOOH_powder3.weight = '0'
FeOOH_powder3.barns = '1'
FeOOH_powder3.Strain = '0'
FeOOH_powder3.interact_fraction = '-1'
FeOOH_powder3.format = '{ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 }'
FeOOH_powder3.init = '"init"'

# Comp instance rust_mix_FeOOH_High, placement and parameters
rust_mix_FeOOH_High = instr.add_component('rust_mix_FeOOH_High','Union_make_material')

rust_mix_FeOOH_High.process_string = '"Fe3O4_incoherent2,Fe3O4_powder2,Fe2O3_incoherent2,Fe2O3_powder2,FeOOH_incoherent2,FeOOH_powder2"'
rust_mix_FeOOH_High.my_absorption = '0.25 * 100 * 15.36152 / 157.15089 + 0.25 * 100 * 30.72342 / 302.72198 + 0.5 * 100 * 11.57192 / 302.72198'
rust_mix_FeOOH_High.absorber = '0'
rust_mix_FeOOH_High.init = '"init"'

# Comp instance Fe3O4_incoherent4, placement and parameters
Fe3O4_incoherent4 = instr.add_component('Fe3O4_incoherent4','Incoherent_process')

Fe3O4_incoherent4.sigma = '2.40639'
Fe3O4_incoherent4.f_QE = '0'
Fe3O4_incoherent4.gamma = '0'
Fe3O4_incoherent4.packing_factor = '0.5'
Fe3O4_incoherent4.unit_cell_volume = '157.15089'
Fe3O4_incoherent4.interact_fraction = '-1'
Fe3O4_incoherent4.init = '"init"'

# Comp instance Fe3O4_powder4, placement and parameters
Fe3O4_powder4 = instr.add_component('Fe3O4_powder4','Powder_process')

Fe3O4_powder4.reflections = '"Fe3O4_mp-19306_computed.laz"'
Fe3O4_powder4.packing_factor = '0.25'
Fe3O4_powder4.Vc = '0'
Fe3O4_powder4.delta_d_d = '0'
Fe3O4_powder4.DW = '0'
Fe3O4_powder4.nb_atoms = '1'
Fe3O4_powder4.d_phi = '0'
Fe3O4_powder4.density = '0'
Fe3O4_powder4.weight = '0'
Fe3O4_powder4.barns = '1'
Fe3O4_powder4.Strain = '0'
Fe3O4_powder4.interact_fraction = '-1'
Fe3O4_powder4.format = '{ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 }'
Fe3O4_powder4.init = '"init"'

# Comp instance Fe2O3_incoherent4, placement and parameters
Fe2O3_incoherent4 = instr.add_component('Fe2O3_incoherent4','Incoherent_process')

Fe2O3_incoherent4.sigma = '4.81438'
Fe2O3_incoherent4.f_QE = '0'
Fe2O3_incoherent4.gamma = '0'
Fe2O3_incoherent4.packing_factor = '0.25'
Fe2O3_incoherent4.unit_cell_volume = '302.72198'
Fe2O3_incoherent4.interact_fraction = '-1'
Fe2O3_incoherent4.init = '"init"'

# Comp instance Fe2O3_powder4, placement and parameters
Fe2O3_powder4 = instr.add_component('Fe2O3_powder4','Powder_process')

Fe2O3_powder4.reflections = '"Fe2O3.laz"'
Fe2O3_powder4.packing_factor = '0.25'
Fe2O3_powder4.Vc = '0'
Fe2O3_powder4.delta_d_d = '0'
Fe2O3_powder4.DW = '0'
Fe2O3_powder4.nb_atoms = '1'
Fe2O3_powder4.d_phi = '0'
Fe2O3_powder4.density = '0'
Fe2O3_powder4.weight = '0'
Fe2O3_powder4.barns = '1'
Fe2O3_powder4.Strain = '0'
Fe2O3_powder4.interact_fraction = '-1'
Fe2O3_powder4.format = '{ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 }'
Fe2O3_powder4.init = '"init"'

# Comp instance FeOOH_incoherent4, placement and parameters
FeOOH_incoherent4 = instr.add_component('FeOOH_incoherent4','Incoherent_process')

FeOOH_incoherent4.sigma = '322.63895'
FeOOH_incoherent4.f_QE = '0'
FeOOH_incoherent4.gamma = '0'
FeOOH_incoherent4.packing_factor = '0.25'
FeOOH_incoherent4.unit_cell_volume = '302.72198'
FeOOH_incoherent4.interact_fraction = '-1'
FeOOH_incoherent4.init = '"init"'

# Comp instance FeOOH_powder4, placement and parameters
FeOOH_powder4 = instr.add_component('FeOOH_powder4','Powder_process')

FeOOH_powder4.reflections = '"FeOOH.laz"'
FeOOH_powder4.packing_factor = '0.5'
FeOOH_powder4.Vc = '0'
FeOOH_powder4.delta_d_d = '0'
FeOOH_powder4.DW = '0'
FeOOH_powder4.nb_atoms = '1'
FeOOH_powder4.d_phi = '0'
FeOOH_powder4.density = '0'
FeOOH_powder4.weight = '0'
FeOOH_powder4.barns = '1'
FeOOH_powder4.Strain = '0'
FeOOH_powder4.interact_fraction = '-1'
FeOOH_powder4.format = '{ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 }'
FeOOH_powder4.init = '"init"'

# Comp instance rust_mix_Fe3O4_High, placement and parameters
rust_mix_Fe3O4_High = instr.add_component('rust_mix_Fe3O4_High','Union_make_material')

rust_mix_Fe3O4_High.process_string = '"Fe3O4_incoherent2,Fe3O4_powder2,Fe2O3_incoherent2,Fe2O3_powder2,FeOOH_incoherent2,FeOOH_powder2"'
rust_mix_Fe3O4_High.my_absorption = '0.5 * 100 * 15.36152 / 157.15089 + 0.25 * 100 * 30.72342 / 302.72198 + 0.25 * 100 * 11.57192 / 302.72198'
rust_mix_Fe3O4_High.absorber = '0'
rust_mix_Fe3O4_High.init = '"init"'

# Comp instance Turn_table_center, placement and parameters
Turn_table_center = instr.add_component('Turn_table_center','Arm', AT=['X_sample_pos', 'Y_sample_pos', 'pinhole_sample_distance'], AT_RELATIVE='graph', ROTATED=['0', 'angle', '0'], ROTATED_RELATIVE='graph')


# Comp instance object_center, placement and parameters
object_center = instr.add_component('object_center','Arm', AT=['0', '0', '0'], AT_RELATIVE='Turn_table_center', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='Turn_table_center')


# Comp instance blade_rust_side_1, placement and parameters
blade_rust_side_1 = instr.add_component('blade_rust_side_1','Union_sphere', AT=['sword_width + 0.065', '-0.065', '0'], AT_RELATIVE='object_center', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='object_center')

blade_rust_side_1.material_string = '"FeOOH"'
blade_rust_side_1.priority = '100'
blade_rust_side_1.radius = '0.1'
blade_rust_side_1.visualize = '1'
blade_rust_side_1.target_index = '0'
blade_rust_side_1.target_x = '0'
blade_rust_side_1.target_y = '0'
blade_rust_side_1.target_z = '0'
blade_rust_side_1.focus_aw = '0'
blade_rust_side_1.focus_ah = '0'
blade_rust_side_1.focus_xw = '0'
blade_rust_side_1.focus_xh = '0'
blade_rust_side_1.focus_r = '0'
blade_rust_side_1.p_interact = '0'
blade_rust_side_1.mask_string = '0'
blade_rust_side_1.mask_setting = '0'
blade_rust_side_1.number_of_activations = '1'
blade_rust_side_1.init = '"init"'

# Comp instance blade_rust_side_2, placement and parameters
blade_rust_side_2 = instr.add_component('blade_rust_side_2','Union_sphere', AT=['sword_width + 0.068', '0.065001', '0'], AT_RELATIVE='object_center', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='object_center')

blade_rust_side_2.material_string = '"FeOOH"'
blade_rust_side_2.priority = '99'
blade_rust_side_2.radius = '0.10001'
blade_rust_side_2.visualize = '1'
blade_rust_side_2.target_index = '0'
blade_rust_side_2.target_x = '0'
blade_rust_side_2.target_y = '0'
blade_rust_side_2.target_z = '0'
blade_rust_side_2.focus_aw = '0'
blade_rust_side_2.focus_ah = '0'
blade_rust_side_2.focus_xw = '0'
blade_rust_side_2.focus_xh = '0'
blade_rust_side_2.focus_r = '0'
blade_rust_side_2.p_interact = '0'
blade_rust_side_2.mask_string = '0'
blade_rust_side_2.mask_setting = '0'
blade_rust_side_2.number_of_activations = '1'
blade_rust_side_2.init = '"init"'

# Comp instance blade_rust_side_3, placement and parameters
blade_rust_side_3 = instr.add_component('blade_rust_side_3','Union_sphere', AT=['sword_width + 0.06', '0.0', '0'], AT_RELATIVE='object_center', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='object_center')

blade_rust_side_3.material_string = '"FeOOH"'
blade_rust_side_3.priority = '98'
blade_rust_side_3.radius = '0.10002'
blade_rust_side_3.visualize = '1'
blade_rust_side_3.target_index = '0'
blade_rust_side_3.target_x = '0'
blade_rust_side_3.target_y = '0'
blade_rust_side_3.target_z = '0'
blade_rust_side_3.focus_aw = '0'
blade_rust_side_3.focus_ah = '0'
blade_rust_side_3.focus_xw = '0'
blade_rust_side_3.focus_xh = '0'
blade_rust_side_3.focus_r = '0'
blade_rust_side_3.p_interact = '0'
blade_rust_side_3.mask_string = '0'
blade_rust_side_3.mask_setting = '0'
blade_rust_side_3.number_of_activations = '1'
blade_rust_side_3.init = '"init"'

# Comp instance blade_iron_side_1, placement and parameters
blade_iron_side_1 = instr.add_component('blade_iron_side_1','Union_box', AT=['0.062', '0', '0'], AT_RELATIVE='object_center', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='object_center')

blade_iron_side_1.material_string = '"iron_mix"'
blade_iron_side_1.priority = '90'
blade_iron_side_1.xwidth = '0.12002'
blade_iron_side_1.yheight = 'sword_height + 0.0002'
blade_iron_side_1.zdepth = 'sword_depth * 2.0 + 0.0002'
blade_iron_side_1.xwidth2 = '-1'
blade_iron_side_1.yheight2 = '-1'
blade_iron_side_1.visualize = '1'
blade_iron_side_1.target_index = '0'
blade_iron_side_1.target_x = '0'
blade_iron_side_1.target_y = '0'
blade_iron_side_1.target_z = '0'
blade_iron_side_1.focus_aw = '0'
blade_iron_side_1.focus_ah = '0'
blade_iron_side_1.focus_xw = '0'
blade_iron_side_1.focus_xh = '0'
blade_iron_side_1.focus_r = '0'
blade_iron_side_1.p_interact = '0'
blade_iron_side_1.mask_string = '0'
blade_iron_side_1.mask_setting = '0'
blade_iron_side_1.number_of_activations = '1'
blade_iron_side_1.init = '"init"'

# Comp instance blade_mask_1, placement and parameters
blade_mask_1 = instr.add_component('blade_mask_1','Union_cylinder', AT=['blade_start_width * 0.5', '0', 'blade_mask_radius - sword_depth * 0.5'], AT_RELATIVE='object_center', ROTATED=['width_angle', '0', 'blade_angle_deg'], ROTATED_RELATIVE='object_center')

blade_mask_1.material_string = '0'
blade_mask_1.priority = '0'
blade_mask_1.radius = 'radius_multiply * blade_mask_radius'
blade_mask_1.yheight = 'sword_height + 0.10001'
blade_mask_1.visualize = '1'
blade_mask_1.target_index = '0'
blade_mask_1.target_x = '0'
blade_mask_1.target_y = '0'
blade_mask_1.target_z = '0'
blade_mask_1.focus_aw = '0'
blade_mask_1.focus_ah = '0'
blade_mask_1.focus_xw = '0'
blade_mask_1.focus_xh = '0'
blade_mask_1.focus_r = '0'
blade_mask_1.p_interact = '0'
blade_mask_1.mask_string = '"blade_rust_side_1,blade_rust_side_2,blade_rust_side_3,blade_iron_side_1"'
blade_mask_1.mask_setting = '"All"'
blade_mask_1.number_of_activations = '1'
blade_mask_1.init = '"init"'

# Comp instance blade_mask_2, placement and parameters
blade_mask_2 = instr.add_component('blade_mask_2','Union_cylinder', AT=['blade_start_width * 0.5', '0', '- blade_mask_radius + sword_depth * 0.5'], AT_RELATIVE='object_center', ROTATED=['- width_angle', '0', 'blade_angle_deg'], ROTATED_RELATIVE='object_center')

blade_mask_2.material_string = '0'
blade_mask_2.priority = '0'
blade_mask_2.radius = 'radius_multiply * blade_mask_radius'
blade_mask_2.yheight = 'sword_height + 0.10002'
blade_mask_2.visualize = '1'
blade_mask_2.target_index = '0'
blade_mask_2.target_x = '0'
blade_mask_2.target_y = '0'
blade_mask_2.target_z = '0'
blade_mask_2.focus_aw = '0'
blade_mask_2.focus_ah = '0'
blade_mask_2.focus_xw = '0'
blade_mask_2.focus_xh = '0'
blade_mask_2.focus_r = '0'
blade_mask_2.p_interact = '0'
blade_mask_2.mask_string = '"blade_rust_side_1,blade_rust_side_2,blade_rust_side_3,blade_iron_side_1"'
blade_mask_2.mask_setting = '"All"'
blade_mask_2.number_of_activations = '1'
blade_mask_2.init = '"init"'

# Comp instance blade_mask_25, placement and parameters
blade_mask_25 = instr.add_component('blade_mask_25','Union_box', AT=['blade_start_width', '0', '0'], AT_RELATIVE='object_center', ROTATED=['width_angle', '0', 'blade_angle_deg'], ROTATED_RELATIVE='object_center')

blade_mask_25.material_string = '0'
blade_mask_25.priority = '0'
blade_mask_25.xwidth = '0.6'
blade_mask_25.yheight = 'sword_height + 0.0001'
blade_mask_25.zdepth = 'sword_depth * 3.0 + 0.0001'
blade_mask_25.xwidth2 = '-1'
blade_mask_25.yheight2 = '-1'
blade_mask_25.visualize = '1'
blade_mask_25.target_index = '0'
blade_mask_25.target_x = '0'
blade_mask_25.target_y = '0'
blade_mask_25.target_z = '0'
blade_mask_25.focus_aw = '0'
blade_mask_25.focus_ah = '0'
blade_mask_25.focus_xw = '0'
blade_mask_25.focus_xh = '0'
blade_mask_25.focus_r = '0'
blade_mask_25.p_interact = '0'
blade_mask_25.mask_string = '"blade_rust_side_1,blade_rust_side_2,blade_rust_side_3,blade_iron_side_1"'
blade_mask_25.mask_setting = '"All"'
blade_mask_25.number_of_activations = '1'
blade_mask_25.init = '"init"'

# Comp instance blade_rust_iron_core_side_1, placement and parameters
blade_rust_iron_core_side_1 = instr.add_component('blade_rust_iron_core_side_1','Union_box', AT=['0.062', '0', '0'], AT_RELATIVE='object_center', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='object_center')

blade_rust_iron_core_side_1.material_string = '"iron_mix"'
blade_rust_iron_core_side_1.priority = '200'
blade_rust_iron_core_side_1.xwidth = '0.12001'
blade_rust_iron_core_side_1.yheight = 'sword_height + 0.0001'
blade_rust_iron_core_side_1.zdepth = 'sword_depth * 2.0 + 0.0001'
blade_rust_iron_core_side_1.xwidth2 = '-1'
blade_rust_iron_core_side_1.yheight2 = '-1'
blade_rust_iron_core_side_1.visualize = '1'
blade_rust_iron_core_side_1.target_index = '0'
blade_rust_iron_core_side_1.target_x = '0'
blade_rust_iron_core_side_1.target_y = '0'
blade_rust_iron_core_side_1.target_z = '0'
blade_rust_iron_core_side_1.focus_aw = '0'
blade_rust_iron_core_side_1.focus_ah = '0'
blade_rust_iron_core_side_1.focus_xw = '0'
blade_rust_iron_core_side_1.focus_xh = '0'
blade_rust_iron_core_side_1.focus_r = '0'
blade_rust_iron_core_side_1.p_interact = '0'
blade_rust_iron_core_side_1.mask_string = '0'
blade_rust_iron_core_side_1.mask_setting = '0'
blade_rust_iron_core_side_1.number_of_activations = '1'
blade_rust_iron_core_side_1.init = '"init"'

# Comp instance rust_mask_1, placement and parameters
rust_mask_1 = instr.add_component('rust_mask_1','Union_cylinder', AT=['blade_start_width * 0.5', '0', 'blade_mask_radius - sword_depth * 0.5'], AT_RELATIVE='object_center', ROTATED=['width_angle', '0', 'blade_angle_deg'], ROTATED_RELATIVE='object_center')

rust_mask_1.material_string = '0'
rust_mask_1.priority = '0'
rust_mask_1.radius = 'blade_mask_radius * 0.98'
rust_mask_1.yheight = '0.5 * sword_height + 0.10001'
rust_mask_1.visualize = '1'
rust_mask_1.target_index = '0'
rust_mask_1.target_x = '0'
rust_mask_1.target_y = '0'
rust_mask_1.target_z = '0'
rust_mask_1.focus_aw = '0'
rust_mask_1.focus_ah = '0'
rust_mask_1.focus_xw = '0'
rust_mask_1.focus_xh = '0'
rust_mask_1.focus_r = '0'
rust_mask_1.p_interact = '0'
rust_mask_1.mask_string = '"blade_rust_iron_core_side_1"'
rust_mask_1.mask_setting = '"All"'
rust_mask_1.number_of_activations = '1'
rust_mask_1.init = '"init"'

# Comp instance rust_mask_2, placement and parameters
rust_mask_2 = instr.add_component('rust_mask_2','Union_cylinder', AT=['blade_start_width * 0.5', '0', '- blade_mask_radius + sword_depth * 0.5'], AT_RELATIVE='object_center', ROTATED=['- width_angle', '0', 'blade_angle_deg'], ROTATED_RELATIVE='object_center')

rust_mask_2.material_string = '0'
rust_mask_2.priority = '0'
rust_mask_2.radius = 'blade_mask_radius * 0.98'
rust_mask_2.yheight = '0.5 * sword_height + 0.10002'
rust_mask_2.visualize = '1'
rust_mask_2.target_index = '0'
rust_mask_2.target_x = '0'
rust_mask_2.target_y = '0'
rust_mask_2.target_z = '0'
rust_mask_2.focus_aw = '0'
rust_mask_2.focus_ah = '0'
rust_mask_2.focus_xw = '0'
rust_mask_2.focus_xh = '0'
rust_mask_2.focus_r = '0'
rust_mask_2.p_interact = '0'
rust_mask_2.mask_string = '"blade_rust_iron_core_side_1"'
rust_mask_2.mask_setting = '"All"'
rust_mask_2.number_of_activations = '1'
rust_mask_2.init = '"init"'

# Comp instance blade_iron_side_2, placement and parameters
blade_iron_side_2 = instr.add_component('blade_iron_side_2','Union_box', AT=['-0.061', '0', '0'], AT_RELATIVE='object_center', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='object_center')

blade_iron_side_2.material_string = '"iron_mix"'
blade_iron_side_2.priority = '101'
blade_iron_side_2.xwidth = '0.12'
blade_iron_side_2.yheight = 'sword_height'
blade_iron_side_2.zdepth = 'sword_depth * 2.0'
blade_iron_side_2.xwidth2 = '-1'
blade_iron_side_2.yheight2 = '-1'
blade_iron_side_2.visualize = '1'
blade_iron_side_2.target_index = '0'
blade_iron_side_2.target_x = '0'
blade_iron_side_2.target_y = '0'
blade_iron_side_2.target_z = '0'
blade_iron_side_2.focus_aw = '0'
blade_iron_side_2.focus_ah = '0'
blade_iron_side_2.focus_xw = '0'
blade_iron_side_2.focus_xh = '0'
blade_iron_side_2.focus_r = '0'
blade_iron_side_2.p_interact = '0'
blade_iron_side_2.mask_string = '0'
blade_iron_side_2.mask_setting = '0'
blade_iron_side_2.number_of_activations = '1'
blade_iron_side_2.init = '"init"'

# Comp instance blade_mask_3, placement and parameters
blade_mask_3 = instr.add_component('blade_mask_3','Union_cylinder', AT=['- blade_start_width * 0.5', '0', 'blade_mask_radius - sword_depth * 0.5'], AT_RELATIVE='object_center', ROTATED=['width_angle', '0', '- blade_angle_deg'], ROTATED_RELATIVE='object_center')

blade_mask_3.material_string = '0'
blade_mask_3.priority = '0'
blade_mask_3.radius = 'radius_multiply * blade_mask_radius'
blade_mask_3.yheight = 'sword_height + 0.10003'
blade_mask_3.visualize = '1'
blade_mask_3.target_index = '0'
blade_mask_3.target_x = '0'
blade_mask_3.target_y = '0'
blade_mask_3.target_z = '0'
blade_mask_3.focus_aw = '0'
blade_mask_3.focus_ah = '0'
blade_mask_3.focus_xw = '0'
blade_mask_3.focus_xh = '0'
blade_mask_3.focus_r = '0'
blade_mask_3.p_interact = '0'
blade_mask_3.mask_string = '"blade_iron_side_2"'
blade_mask_3.mask_setting = '"All"'
blade_mask_3.number_of_activations = '1'
blade_mask_3.init = '"init"'

# Comp instance blade_mask_4, placement and parameters
blade_mask_4 = instr.add_component('blade_mask_4','Union_cylinder', AT=['- blade_start_width * 0.5', '0', '- blade_mask_radius + sword_depth * 0.5'], AT_RELATIVE='object_center', ROTATED=['- width_angle', '0', '- blade_angle_deg'], ROTATED_RELATIVE='object_center')

blade_mask_4.material_string = '0'
blade_mask_4.priority = '0'
blade_mask_4.radius = 'radius_multiply * blade_mask_radius'
blade_mask_4.yheight = 'sword_height + 0.10004'
blade_mask_4.visualize = '1'
blade_mask_4.target_index = '0'
blade_mask_4.target_x = '0'
blade_mask_4.target_y = '0'
blade_mask_4.target_z = '0'
blade_mask_4.focus_aw = '0'
blade_mask_4.focus_ah = '0'
blade_mask_4.focus_xw = '0'
blade_mask_4.focus_xh = '0'
blade_mask_4.focus_r = '0'
blade_mask_4.p_interact = '0'
blade_mask_4.mask_string = '"blade_iron_side_2"'
blade_mask_4.mask_setting = '"All"'
blade_mask_4.number_of_activations = '1'
blade_mask_4.init = '"init"'

# Comp instance rust_core, placement and parameters
rust_core = instr.add_component('rust_core','Union_box', AT=['0', '0', '0'], AT_RELATIVE='object_center', ROTATED=['-90', '0', '45'], ROTATED_RELATIVE='object_center')

rust_core.material_string = 'rust_string'
rust_core.priority = '202'
rust_core.xwidth = 'core_side_bottom_length'
rust_core.yheight = 'core_side_bottom_length'
rust_core.zdepth = 'sword_height -0.0001'
rust_core.xwidth2 = 'core_side_top_length'
rust_core.yheight2 = 'core_side_top_length'
rust_core.visualize = '1'
rust_core.target_index = '0'
rust_core.target_x = '0'
rust_core.target_y = '0'
rust_core.target_z = '0'
rust_core.focus_aw = '0'
rust_core.focus_ah = '0'
rust_core.focus_xw = '0'
rust_core.focus_xh = '0'
rust_core.focus_r = '0'
rust_core.p_interact = '0'
rust_core.mask_string = '0'
rust_core.mask_setting = '0'
rust_core.number_of_activations = '1'
rust_core.init = '"init"'

# Comp instance hard_core, placement and parameters
hard_core = instr.add_component('hard_core','Union_box', AT=['0', '0', '0'], AT_RELATIVE='object_center', ROTATED=['-90', '0', '45'], ROTATED_RELATIVE='object_center')

hard_core.material_string = '"iron_mix"'
hard_core.priority = '203'
hard_core.xwidth = 'core_side_bottom_length - rust_thickness * 2.0'
hard_core.yheight = 'core_side_bottom_length - rust_thickness * 2.0'
hard_core.zdepth = 'sword_height -0.0002'
hard_core.xwidth2 = 'core_side_top_length - rust_thickness * 2.0'
hard_core.yheight2 = 'core_side_top_length - rust_thickness * 2.0'
hard_core.visualize = '1'
hard_core.target_index = '0'
hard_core.target_x = '0'
hard_core.target_y = '0'
hard_core.target_z = '0'
hard_core.focus_aw = '0'
hard_core.focus_ah = '0'
hard_core.focus_xw = '0'
hard_core.focus_xh = '0'
hard_core.focus_r = '0'
hard_core.p_interact = '0'
hard_core.mask_string = '0'
hard_core.mask_setting = '0'
hard_core.number_of_activations = '1'
hard_core.init = '"init"'

# Comp instance side_cut_1, placement and parameters
side_cut_1 = instr.add_component('side_cut_1','Union_cylinder', AT=['0', '0', 'cut_radius + sword_depth * 0.5 - cut_depth + 0.0001'], AT_RELATIVE='object_center', ROTATED=['- cut_angle + 0.00001', '0', '0'], ROTATED_RELATIVE='object_center')

side_cut_1.material_string = '"Vacuum"'
side_cut_1.priority = '1000'
side_cut_1.radius = 'cut_radius'
side_cut_1.yheight = 'sword_height + 2 * tip_height + 0.2'
side_cut_1.visualize = '1'
side_cut_1.target_index = '0'
side_cut_1.target_x = '0'
side_cut_1.target_y = '0'
side_cut_1.target_z = '0'
side_cut_1.focus_aw = '0'
side_cut_1.focus_ah = '0'
side_cut_1.focus_xw = '0'
side_cut_1.focus_xh = '0'
side_cut_1.focus_r = '0'
side_cut_1.p_interact = '0'
side_cut_1.mask_string = '0'
side_cut_1.mask_setting = '0'
side_cut_1.number_of_activations = '1'
side_cut_1.init = '"init"'

# Comp instance side_cut_2, placement and parameters
side_cut_2 = instr.add_component('side_cut_2','Union_cylinder', AT=['0', '0', '- cut_radius - sword_depth * 0.5 + cut_depth + 0.0001'], AT_RELATIVE='object_center', ROTATED=['cut_angle + 0.00002', '0', '0'], ROTATED_RELATIVE='object_center')

side_cut_2.material_string = '"Vacuum"'
side_cut_2.priority = '1001'
side_cut_2.radius = 'cut_radius'
side_cut_2.yheight = 'sword_height + 2 * tip_height + 0.1'
side_cut_2.visualize = '1'
side_cut_2.target_index = '0'
side_cut_2.target_x = '0'
side_cut_2.target_y = '0'
side_cut_2.target_z = '0'
side_cut_2.focus_aw = '0'
side_cut_2.focus_ah = '0'
side_cut_2.focus_xw = '0'
side_cut_2.focus_xh = '0'
side_cut_2.focus_r = '0'
side_cut_2.p_interact = '0'
side_cut_2.mask_string = '0'
side_cut_2.mask_setting = '0'
side_cut_2.number_of_activations = '1'
side_cut_2.init = '"init"'

# Comp instance blade_iron_side_tip_1, placement and parameters
blade_iron_side_tip_1 = instr.add_component('blade_iron_side_tip_1','Union_box', AT=['0.06', 'sword_height * 0.5 + tip_height * 0.5 -0.0001', '0'], AT_RELATIVE='object_center', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='object_center')

blade_iron_side_tip_1.material_string = '"iron_mix"'
blade_iron_side_tip_1.priority = '300'
blade_iron_side_tip_1.xwidth = '0.12 -0.0002'
blade_iron_side_tip_1.yheight = 'tip_height'
blade_iron_side_tip_1.zdepth = 'sword_depth * 2.0 -0.001'
blade_iron_side_tip_1.xwidth2 = '-1'
blade_iron_side_tip_1.yheight2 = '-1'
blade_iron_side_tip_1.visualize = '1'
blade_iron_side_tip_1.target_index = '0'
blade_iron_side_tip_1.target_x = '0'
blade_iron_side_tip_1.target_y = '0'
blade_iron_side_tip_1.target_z = '0'
blade_iron_side_tip_1.focus_aw = '0'
blade_iron_side_tip_1.focus_ah = '0'
blade_iron_side_tip_1.focus_xw = '0'
blade_iron_side_tip_1.focus_xh = '0'
blade_iron_side_tip_1.focus_r = '0'
blade_iron_side_tip_1.p_interact = '0'
blade_iron_side_tip_1.mask_string = '0'
blade_iron_side_tip_1.mask_setting = '0'
blade_iron_side_tip_1.number_of_activations = '1'
blade_iron_side_tip_1.init = '"init"'

# Comp instance blade_mask_tip_1, placement and parameters
blade_mask_tip_1 = instr.add_component('blade_mask_tip_1','Union_cylinder', AT=['blade_top_width * 0.5 * tip_x_multiplier', 'sword_height * 0.5 + tip_height * 0.5 -0.0001', 'blade_tip_mask_radius - sword_depth * 0.5 * 0.8'], AT_RELATIVE='object_center', ROTATED=['2.5 * width_angle', '0', 'blade_angle_tip_deg'], ROTATED_RELATIVE='object_center')

blade_mask_tip_1.material_string = '0'
blade_mask_tip_1.priority = '0'
blade_mask_tip_1.radius = 'blade_tip_mask_radius'
blade_mask_tip_1.yheight = 'tip_height + 0.10001'
blade_mask_tip_1.visualize = '1'
blade_mask_tip_1.target_index = '0'
blade_mask_tip_1.target_x = '0'
blade_mask_tip_1.target_y = '0'
blade_mask_tip_1.target_z = '0'
blade_mask_tip_1.focus_aw = '0'
blade_mask_tip_1.focus_ah = '0'
blade_mask_tip_1.focus_xw = '0'
blade_mask_tip_1.focus_xh = '0'
blade_mask_tip_1.focus_r = '0'
blade_mask_tip_1.p_interact = '0'
blade_mask_tip_1.mask_string = '"blade_iron_side_tip_1"'
blade_mask_tip_1.mask_setting = '"All"'
blade_mask_tip_1.number_of_activations = '1'
blade_mask_tip_1.init = '"init"'

# Comp instance blade_mask_tip_2, placement and parameters
blade_mask_tip_2 = instr.add_component('blade_mask_tip_2','Union_cylinder', AT=['blade_top_width * 0.5 * tip_x_multiplier', 'sword_height * 0.5 + tip_height * 0.5 -0.0001', '- blade_tip_mask_radius + sword_depth * 0.5 * 0.8'], AT_RELATIVE='object_center', ROTATED=['-2.5 * width_angle', '0', 'blade_angle_tip_deg'], ROTATED_RELATIVE='object_center')

blade_mask_tip_2.material_string = '0'
blade_mask_tip_2.priority = '0'
blade_mask_tip_2.radius = 'blade_tip_mask_radius'
blade_mask_tip_2.yheight = 'tip_height + 0.10002'
blade_mask_tip_2.visualize = '1'
blade_mask_tip_2.target_index = '0'
blade_mask_tip_2.target_x = '0'
blade_mask_tip_2.target_y = '0'
blade_mask_tip_2.target_z = '0'
blade_mask_tip_2.focus_aw = '0'
blade_mask_tip_2.focus_ah = '0'
blade_mask_tip_2.focus_xw = '0'
blade_mask_tip_2.focus_xh = '0'
blade_mask_tip_2.focus_r = '0'
blade_mask_tip_2.p_interact = '0'
blade_mask_tip_2.mask_string = '"blade_iron_side_tip_1"'
blade_mask_tip_2.mask_setting = '"All"'
blade_mask_tip_2.number_of_activations = '1'
blade_mask_tip_2.init = '"init"'

# Comp instance blade_rust_side_tip_2, placement and parameters
blade_rust_side_tip_2 = instr.add_component('blade_rust_side_tip_2','Union_sphere', AT=['-0.88 * sword_width', '0.5 * sword_height + 0.5 * tip_height', '0'], AT_RELATIVE='object_center', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='object_center')

blade_rust_side_tip_2.material_string = '"Fe2O3"'
blade_rust_side_tip_2.priority = '291'
blade_rust_side_tip_2.radius = '0.044'
blade_rust_side_tip_2.visualize = '1'
blade_rust_side_tip_2.target_index = '0'
blade_rust_side_tip_2.target_x = '0'
blade_rust_side_tip_2.target_y = '0'
blade_rust_side_tip_2.target_z = '0'
blade_rust_side_tip_2.focus_aw = '0'
blade_rust_side_tip_2.focus_ah = '0'
blade_rust_side_tip_2.focus_xw = '0'
blade_rust_side_tip_2.focus_xh = '0'
blade_rust_side_tip_2.focus_r = '0'
blade_rust_side_tip_2.p_interact = '0'
blade_rust_side_tip_2.mask_string = '0'
blade_rust_side_tip_2.mask_setting = '0'
blade_rust_side_tip_2.number_of_activations = '1'
blade_rust_side_tip_2.init = '"init"'

# Comp instance blade_rust_side_tip_3, placement and parameters
blade_rust_side_tip_3 = instr.add_component('blade_rust_side_tip_3','Union_sphere', AT=['-0.83 * sword_width', '0.55 * sword_height + 0.5 * tip_height', '0'], AT_RELATIVE='object_center', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='object_center')

blade_rust_side_tip_3.material_string = '"Fe2O3"'
blade_rust_side_tip_3.priority = '292'
blade_rust_side_tip_3.radius = '0.044'
blade_rust_side_tip_3.visualize = '1'
blade_rust_side_tip_3.target_index = '0'
blade_rust_side_tip_3.target_x = '0'
blade_rust_side_tip_3.target_y = '0'
blade_rust_side_tip_3.target_z = '0'
blade_rust_side_tip_3.focus_aw = '0'
blade_rust_side_tip_3.focus_ah = '0'
blade_rust_side_tip_3.focus_xw = '0'
blade_rust_side_tip_3.focus_xh = '0'
blade_rust_side_tip_3.focus_r = '0'
blade_rust_side_tip_3.p_interact = '0'
blade_rust_side_tip_3.mask_string = '0'
blade_rust_side_tip_3.mask_setting = '0'
blade_rust_side_tip_3.number_of_activations = '1'
blade_rust_side_tip_3.init = '"init"'

# Comp instance blade_rust_side_tip_4, placement and parameters
blade_rust_side_tip_4 = instr.add_component('blade_rust_side_tip_4','Union_sphere', AT=['-0.96 * sword_width', '0.45 * sword_height + 0.5 * tip_height', '0'], AT_RELATIVE='object_center', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='object_center')

blade_rust_side_tip_4.material_string = '"Fe2O3"'
blade_rust_side_tip_4.priority = '293'
blade_rust_side_tip_4.radius = '0.045'
blade_rust_side_tip_4.visualize = '1'
blade_rust_side_tip_4.target_index = '0'
blade_rust_side_tip_4.target_x = '0'
blade_rust_side_tip_4.target_y = '0'
blade_rust_side_tip_4.target_z = '0'
blade_rust_side_tip_4.focus_aw = '0'
blade_rust_side_tip_4.focus_ah = '0'
blade_rust_side_tip_4.focus_xw = '0'
blade_rust_side_tip_4.focus_xh = '0'
blade_rust_side_tip_4.focus_r = '0'
blade_rust_side_tip_4.p_interact = '0'
blade_rust_side_tip_4.mask_string = '0'
blade_rust_side_tip_4.mask_setting = '0'
blade_rust_side_tip_4.number_of_activations = '1'
blade_rust_side_tip_4.init = '"init"'

# Comp instance blade_iron_side_tip_2, placement and parameters
blade_iron_side_tip_2 = instr.add_component('blade_iron_side_tip_2','Union_box', AT=['-0.06', 'sword_height * 0.5 + tip_height * 0.5 -0.0001', '0'], AT_RELATIVE='object_center', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='object_center')

blade_iron_side_tip_2.material_string = '"iron_mix"'
blade_iron_side_tip_2.priority = '290'
blade_iron_side_tip_2.xwidth = '0.12 -0.0002'
blade_iron_side_tip_2.yheight = 'tip_height'
blade_iron_side_tip_2.zdepth = 'sword_depth * 2.0 -0.001'
blade_iron_side_tip_2.xwidth2 = '-1'
blade_iron_side_tip_2.yheight2 = '-1'
blade_iron_side_tip_2.visualize = '1'
blade_iron_side_tip_2.target_index = '0'
blade_iron_side_tip_2.target_x = '0'
blade_iron_side_tip_2.target_y = '0'
blade_iron_side_tip_2.target_z = '0'
blade_iron_side_tip_2.focus_aw = '0'
blade_iron_side_tip_2.focus_ah = '0'
blade_iron_side_tip_2.focus_xw = '0'
blade_iron_side_tip_2.focus_xh = '0'
blade_iron_side_tip_2.focus_r = '0'
blade_iron_side_tip_2.p_interact = '0'
blade_iron_side_tip_2.mask_string = '0'
blade_iron_side_tip_2.mask_setting = '0'
blade_iron_side_tip_2.number_of_activations = '1'
blade_iron_side_tip_2.init = '"init"'

# Comp instance blade_mask_tip_3, placement and parameters
blade_mask_tip_3 = instr.add_component('blade_mask_tip_3','Union_cylinder', AT=['- blade_top_width * 0.5 * tip_x_multiplier', 'sword_height * 0.5 + tip_height * 0.5 -0.0001', 'blade_tip_mask_radius - sword_depth * 0.5 * 0.8'], AT_RELATIVE='object_center', ROTATED=['2.5 * width_angle', '0', '- blade_angle_tip_deg'], ROTATED_RELATIVE='object_center')

blade_mask_tip_3.material_string = '0'
blade_mask_tip_3.priority = '0'
blade_mask_tip_3.radius = 'blade_tip_mask_radius'
blade_mask_tip_3.yheight = 'tip_height + 0.10003'
blade_mask_tip_3.visualize = '1'
blade_mask_tip_3.target_index = '0'
blade_mask_tip_3.target_x = '0'
blade_mask_tip_3.target_y = '0'
blade_mask_tip_3.target_z = '0'
blade_mask_tip_3.focus_aw = '0'
blade_mask_tip_3.focus_ah = '0'
blade_mask_tip_3.focus_xw = '0'
blade_mask_tip_3.focus_xh = '0'
blade_mask_tip_3.focus_r = '0'
blade_mask_tip_3.p_interact = '0'
blade_mask_tip_3.mask_string = '"blade_iron_side_tip_2,blade_rust_side_tip_3,blade_rust_side_tip_4,blade_rust_side_tip_2"'
blade_mask_tip_3.mask_setting = '"All"'
blade_mask_tip_3.number_of_activations = '1'
blade_mask_tip_3.init = '"init"'

# Comp instance blade_mask_tip_4, placement and parameters
blade_mask_tip_4 = instr.add_component('blade_mask_tip_4','Union_cylinder', AT=['- blade_top_width * 0.5 * tip_x_multiplier', 'sword_height * 0.5 + tip_height * 0.5 -0.0001', '- blade_tip_mask_radius + sword_depth * 0.5 * 0.8'], AT_RELATIVE='object_center', ROTATED=['-2.5 * width_angle', '0', '- blade_angle_tip_deg'], ROTATED_RELATIVE='object_center')

blade_mask_tip_4.material_string = '0'
blade_mask_tip_4.priority = '0'
blade_mask_tip_4.radius = 'blade_tip_mask_radius'
blade_mask_tip_4.yheight = 'tip_height + 0.10004'
blade_mask_tip_4.visualize = '1'
blade_mask_tip_4.target_index = '0'
blade_mask_tip_4.target_x = '0'
blade_mask_tip_4.target_y = '0'
blade_mask_tip_4.target_z = '0'
blade_mask_tip_4.focus_aw = '0'
blade_mask_tip_4.focus_ah = '0'
blade_mask_tip_4.focus_xw = '0'
blade_mask_tip_4.focus_xh = '0'
blade_mask_tip_4.focus_r = '0'
blade_mask_tip_4.p_interact = '0'
blade_mask_tip_4.mask_string = '"blade_iron_side_tip_2,blade_rust_side_tip_3,blade_rust_side_tip_4,blade_rust_side_tip_2"'
blade_mask_tip_4.mask_setting = '"All"'
blade_mask_tip_4.number_of_activations = '1'
blade_mask_tip_4.init = '"init"'

# Comp instance blade_side_iron_core_tip_2, placement and parameters
blade_side_iron_core_tip_2 = instr.add_component('blade_side_iron_core_tip_2','Union_box', AT=['-0.06', 'sword_height * 0.5 + tip_height * 0.5 + 0.0001', '0'], AT_RELATIVE='object_center', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='object_center')

blade_side_iron_core_tip_2.material_string = '"iron_mix"'
blade_side_iron_core_tip_2.priority = '301'
blade_side_iron_core_tip_2.xwidth = '0.12 -0.0003'
blade_side_iron_core_tip_2.yheight = 'tip_height + 0.0001'
blade_side_iron_core_tip_2.zdepth = 'sword_depth * 2.0 -0.001'
blade_side_iron_core_tip_2.xwidth2 = '-1'
blade_side_iron_core_tip_2.yheight2 = '-1'
blade_side_iron_core_tip_2.visualize = '1'
blade_side_iron_core_tip_2.target_index = '0'
blade_side_iron_core_tip_2.target_x = '0'
blade_side_iron_core_tip_2.target_y = '0'
blade_side_iron_core_tip_2.target_z = '0'
blade_side_iron_core_tip_2.focus_aw = '0'
blade_side_iron_core_tip_2.focus_ah = '0'
blade_side_iron_core_tip_2.focus_xw = '0'
blade_side_iron_core_tip_2.focus_xh = '0'
blade_side_iron_core_tip_2.focus_r = '0'
blade_side_iron_core_tip_2.p_interact = '0'
blade_side_iron_core_tip_2.mask_string = '0'
blade_side_iron_core_tip_2.mask_setting = '0'
blade_side_iron_core_tip_2.number_of_activations = '1'
blade_side_iron_core_tip_2.init = '"init"'

# Comp instance blade_mask_tip_5, placement and parameters
blade_mask_tip_5 = instr.add_component('blade_mask_tip_5','Union_cylinder', AT=['- blade_top_width * 0.5 * tip_x_multiplier', 'sword_height * 0.5 + tip_height * 0.5 -0.0001', 'blade_tip_mask_radius - sword_depth * 0.5 * 0.8'], AT_RELATIVE='object_center', ROTATED=['2.5 * width_angle', '0', '- blade_angle_tip_deg'], ROTATED_RELATIVE='object_center')

blade_mask_tip_5.material_string = '0'
blade_mask_tip_5.priority = '0'
blade_mask_tip_5.radius = 'blade_tip_mask_radius * 0.99'
blade_mask_tip_5.yheight = '0.75 * tip_height + 0.0003'
blade_mask_tip_5.visualize = '1'
blade_mask_tip_5.target_index = '0'
blade_mask_tip_5.target_x = '0'
blade_mask_tip_5.target_y = '0'
blade_mask_tip_5.target_z = '0'
blade_mask_tip_5.focus_aw = '0'
blade_mask_tip_5.focus_ah = '0'
blade_mask_tip_5.focus_xw = '0'
blade_mask_tip_5.focus_xh = '0'
blade_mask_tip_5.focus_r = '0'
blade_mask_tip_5.p_interact = '0'
blade_mask_tip_5.mask_string = '"blade_side_iron_core_tip_2"'
blade_mask_tip_5.mask_setting = '"All"'
blade_mask_tip_5.number_of_activations = '1'
blade_mask_tip_5.init = '"init"'

# Comp instance blade_mask_tip_6, placement and parameters
blade_mask_tip_6 = instr.add_component('blade_mask_tip_6','Union_cylinder', AT=['- blade_top_width * 0.5 * tip_x_multiplier', 'sword_height * 0.5 + tip_height * 0.5 -0.0001', '- blade_tip_mask_radius + sword_depth * 0.5 * 0.8'], AT_RELATIVE='object_center', ROTATED=['-2.5 * width_angle', '0', '- blade_angle_tip_deg'], ROTATED_RELATIVE='object_center')

blade_mask_tip_6.material_string = '0'
blade_mask_tip_6.priority = '0'
blade_mask_tip_6.radius = 'blade_tip_mask_radius * 0.99'
blade_mask_tip_6.yheight = '0.75 * tip_height + 0.0002'
blade_mask_tip_6.visualize = '1'
blade_mask_tip_6.target_index = '0'
blade_mask_tip_6.target_x = '0'
blade_mask_tip_6.target_y = '0'
blade_mask_tip_6.target_z = '0'
blade_mask_tip_6.focus_aw = '0'
blade_mask_tip_6.focus_ah = '0'
blade_mask_tip_6.focus_xw = '0'
blade_mask_tip_6.focus_xh = '0'
blade_mask_tip_6.focus_r = '0'
blade_mask_tip_6.p_interact = '0'
blade_mask_tip_6.mask_string = '"blade_side_iron_core_tip_2"'
blade_mask_tip_6.mask_setting = '"All"'
blade_mask_tip_6.number_of_activations = '1'
blade_mask_tip_6.init = '"init"'

# Comp instance rust_core_tip, placement and parameters
rust_core_tip = instr.add_component('rust_core_tip','Union_box', AT=['0', 'sword_height * 0.5 + ( tip_height -0.05 ) * 0.5 -0.0003', '0'], AT_RELATIVE='object_center', ROTATED=['-90', '0', '45'], ROTATED_RELATIVE='object_center')

rust_core_tip.material_string = 'rust_string'
rust_core_tip.priority = '302'
rust_core_tip.xwidth = 'core_side_top_length -0.001'
rust_core_tip.yheight = 'core_side_top_length -0.001'
rust_core_tip.zdepth = 'tip_height -0.05'
rust_core_tip.xwidth2 = '2.0 * rust_thickness + 0.0001'
rust_core_tip.yheight2 = '2.0 * rust_thickness + 0.0001'
rust_core_tip.visualize = '1'
rust_core_tip.target_index = '0'
rust_core_tip.target_x = '0'
rust_core_tip.target_y = '0'
rust_core_tip.target_z = '0'
rust_core_tip.focus_aw = '0'
rust_core_tip.focus_ah = '0'
rust_core_tip.focus_xw = '0'
rust_core_tip.focus_xh = '0'
rust_core_tip.focus_r = '0'
rust_core_tip.p_interact = '0'
rust_core_tip.mask_string = '0'
rust_core_tip.mask_setting = '0'
rust_core_tip.number_of_activations = '1'
rust_core_tip.init = '"init"'

# Comp instance hard_core_tip, placement and parameters
hard_core_tip = instr.add_component('hard_core_tip','Union_box', AT=['0', 'sword_height * 0.5 + ( tip_height -0.05 ) * 0.5 -0.0001', '0'], AT_RELATIVE='object_center', ROTATED=['-90', 'sword_height * 0.5 -0.0001', '45'], ROTATED_RELATIVE='object_center')

hard_core_tip.material_string = '"iron_mix"'
hard_core_tip.priority = '303'
hard_core_tip.xwidth = 'core_side_top_length - rust_thickness * 2.0 -0.001'
hard_core_tip.yheight = 'core_side_top_length - rust_thickness * 2.0 -0.001'
hard_core_tip.zdepth = 'tip_height -0.05'
hard_core_tip.xwidth2 = '0.0001'
hard_core_tip.yheight2 = '0.0001'
hard_core_tip.visualize = '1'
hard_core_tip.target_index = '0'
hard_core_tip.target_x = '0'
hard_core_tip.target_y = '0'
hard_core_tip.target_z = '0'
hard_core_tip.focus_aw = '0'
hard_core_tip.focus_ah = '0'
hard_core_tip.focus_xw = '0'
hard_core_tip.focus_xh = '0'
hard_core_tip.focus_r = '0'
hard_core_tip.p_interact = '0'
hard_core_tip.mask_string = '0'
hard_core_tip.mask_setting = '0'
hard_core_tip.number_of_activations = '1'
hard_core_tip.init = '"init"'

# Comp instance left_blade_guard, placement and parameters
left_blade_guard = instr.add_component('left_blade_guard','Union_box', AT=['0.0451', '- sword_height * 0.5 -0.015', '0'], AT_RELATIVE='object_center', ROTATED=['0', '90', '0'], ROTATED_RELATIVE='object_center')

left_blade_guard.material_string = '"iron_mix"'
left_blade_guard.priority = '1050'
left_blade_guard.xwidth = '0.03'
left_blade_guard.yheight = '0.045'
left_blade_guard.zdepth = '0.09'
left_blade_guard.xwidth2 = '0.02'
left_blade_guard.yheight2 = '0.02'
left_blade_guard.visualize = '1'
left_blade_guard.target_index = '0'
left_blade_guard.target_x = '0'
left_blade_guard.target_y = '0'
left_blade_guard.target_z = '0'
left_blade_guard.focus_aw = '0'
left_blade_guard.focus_ah = '0'
left_blade_guard.focus_xw = '0'
left_blade_guard.focus_xh = '0'
left_blade_guard.focus_r = '0'
left_blade_guard.p_interact = '0'
left_blade_guard.mask_string = '0'
left_blade_guard.mask_setting = '0'
left_blade_guard.number_of_activations = '1'
left_blade_guard.init = '"init"'

# Comp instance right_blade_guard, placement and parameters
right_blade_guard = instr.add_component('right_blade_guard','Union_box', AT=['-0.0451', '- sword_height * 0.5 -0.015', '0'], AT_RELATIVE='object_center', ROTATED=['0', '-90', '0'], ROTATED_RELATIVE='object_center')

right_blade_guard.material_string = '"iron_mix"'
right_blade_guard.priority = '1051'
right_blade_guard.xwidth = '0.03'
right_blade_guard.yheight = '0.045'
right_blade_guard.zdepth = '0.09'
right_blade_guard.xwidth2 = '0.02'
right_blade_guard.yheight2 = '0.02'
right_blade_guard.visualize = '1'
right_blade_guard.target_index = '0'
right_blade_guard.target_x = '0'
right_blade_guard.target_y = '0'
right_blade_guard.target_z = '0'
right_blade_guard.focus_aw = '0'
right_blade_guard.focus_ah = '0'
right_blade_guard.focus_xw = '0'
right_blade_guard.focus_xh = '0'
right_blade_guard.focus_r = '0'
right_blade_guard.p_interact = '0'
right_blade_guard.mask_string = '0'
right_blade_guard.mask_setting = '0'
right_blade_guard.number_of_activations = '1'
right_blade_guard.init = '"init"'

# Comp instance handle, placement and parameters
handle = instr.add_component('handle','Union_cylinder', AT=['0', '- sword_height * 0.5 -0.03 -0.15 * 0.5', '0'], AT_RELATIVE='object_center', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='object_center')

handle.material_string = '"iron_mix"'
handle.priority = '1052'
handle.radius = '0.02'
handle.yheight = '0.15'
handle.visualize = '1'
handle.target_index = '0'
handle.target_x = '0'
handle.target_y = '0'
handle.target_z = '0'
handle.focus_aw = '0'
handle.focus_ah = '0'
handle.focus_xw = '0'
handle.focus_xh = '0'
handle.focus_r = '0'
handle.p_interact = '0'
handle.mask_string = '0'
handle.mask_setting = '0'
handle.number_of_activations = '1'
handle.init = '"init"'

# Comp instance handle_end, placement and parameters
handle_end = instr.add_component('handle_end','Union_sphere', AT=['0', '- sword_height * 0.5 -0.03 -0.15', '0'], AT_RELATIVE='object_center', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='object_center')

handle_end.material_string = '"iron_mix"'
handle_end.priority = '1053'
handle_end.radius = '0.03'
handle_end.visualize = '1'
handle_end.target_index = '0'
handle_end.target_x = '0'
handle_end.target_y = '0'
handle_end.target_z = '0'
handle_end.focus_aw = '0'
handle_end.focus_ah = '0'
handle_end.focus_xw = '0'
handle_end.focus_xh = '0'
handle_end.focus_r = '0'
handle_end.p_interact = '0'
handle_end.mask_string = '0'
handle_end.mask_setting = '0'
handle_end.number_of_activations = '1'
handle_end.init = '"init"'

# Comp instance sample_mount, placement and parameters
sample_mount = instr.add_component('sample_mount','Union_box', AT=['- sword_width * 0.20', 'sword_height * 0.3', '- sword_depth * 0.50 -0.0075'], AT_RELATIVE='object_center', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='object_center')

sample_mount.material_string = '"Al"'
sample_mount.priority = '10000'
sample_mount.xwidth = 'sword_width * 0.5'
sample_mount.yheight = 'sword_height * 1.5'
sample_mount.zdepth = '0.01'
sample_mount.xwidth2 = '-1'
sample_mount.yheight2 = '-1'
sample_mount.visualize = '1'
sample_mount.target_index = '0'
sample_mount.target_x = '0'
sample_mount.target_y = '0'
sample_mount.target_z = '0'
sample_mount.focus_aw = '0'
sample_mount.focus_ah = '0'
sample_mount.focus_xw = '0'
sample_mount.focus_xh = '0'
sample_mount.focus_r = '0'
sample_mount.p_interact = '0'
sample_mount.mask_string = '0'
sample_mount.mask_setting = '0'
sample_mount.number_of_activations = '1'
sample_mount.init = '"init"'

# Comp instance Holder_1, placement and parameters
Holder_1 = instr.add_component('Holder_1','Union_box', AT=['0', '0.0', '0'], AT_RELATIVE='object_center', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='object_center')

Holder_1.material_string = '"Al"'
Holder_1.priority = '10002'
Holder_1.xwidth = 'sword_width * 3'
Holder_1.yheight = '0.04'
Holder_1.zdepth = 'sword_depth * 3'
Holder_1.xwidth2 = 'sword_width * 3'
Holder_1.yheight2 = '0.04'
Holder_1.visualize = '1'
Holder_1.target_index = '0'
Holder_1.target_x = '0'
Holder_1.target_y = '0'
Holder_1.target_z = '0'
Holder_1.focus_aw = '0'
Holder_1.focus_ah = '0'
Holder_1.focus_xw = '0'
Holder_1.focus_xh = '0'
Holder_1.focus_r = '0'
Holder_1.p_interact = '0'
Holder_1.mask_string = '0'
Holder_1.mask_setting = '0'
Holder_1.number_of_activations = '1'
Holder_1.init = '"init"'

# Comp instance sample_holder_1_mask_1, placement and parameters
sample_holder_1_mask_1 = instr.add_component('sample_holder_1_mask_1','Union_box', AT=['0.042', '0.0', '0'], AT_RELATIVE='object_center', ROTATED=['0', '0.0', '0'], ROTATED_RELATIVE='object_center')

sample_holder_1_mask_1.material_string = '0'
sample_holder_1_mask_1.priority = '0'
sample_holder_1_mask_1.xwidth = '0.005'
sample_holder_1_mask_1.yheight = '0.02'
sample_holder_1_mask_1.zdepth = '0.0085 * 2'
sample_holder_1_mask_1.xwidth2 = '-1'
sample_holder_1_mask_1.yheight2 = '-1'
sample_holder_1_mask_1.visualize = '1'
sample_holder_1_mask_1.target_index = '0'
sample_holder_1_mask_1.target_x = '0'
sample_holder_1_mask_1.target_y = '0'
sample_holder_1_mask_1.target_z = '0'
sample_holder_1_mask_1.focus_aw = '0'
sample_holder_1_mask_1.focus_ah = '0'
sample_holder_1_mask_1.focus_xw = '0'
sample_holder_1_mask_1.focus_xh = '0'
sample_holder_1_mask_1.focus_r = '0'
sample_holder_1_mask_1.p_interact = '0'
sample_holder_1_mask_1.mask_string = '"Holder_1"'
sample_holder_1_mask_1.mask_setting = '"Any"'
sample_holder_1_mask_1.number_of_activations = '1'
sample_holder_1_mask_1.init = '"init"'

# Comp instance sample_holder_1_mask_2, placement and parameters
sample_holder_1_mask_2 = instr.add_component('sample_holder_1_mask_2','Union_box', AT=['-0.042', '0.0', '0'], AT_RELATIVE='object_center', ROTATED=['0', '0.0', '0'], ROTATED_RELATIVE='object_center')

sample_holder_1_mask_2.material_string = '0'
sample_holder_1_mask_2.priority = '0'
sample_holder_1_mask_2.xwidth = '0.005'
sample_holder_1_mask_2.yheight = '0.02'
sample_holder_1_mask_2.zdepth = '0.0085 * 2'
sample_holder_1_mask_2.xwidth2 = '-1'
sample_holder_1_mask_2.yheight2 = '-1'
sample_holder_1_mask_2.visualize = '1'
sample_holder_1_mask_2.target_index = '0'
sample_holder_1_mask_2.target_x = '0'
sample_holder_1_mask_2.target_y = '0'
sample_holder_1_mask_2.target_z = '0'
sample_holder_1_mask_2.focus_aw = '0'
sample_holder_1_mask_2.focus_ah = '0'
sample_holder_1_mask_2.focus_xw = '0'
sample_holder_1_mask_2.focus_xh = '0'
sample_holder_1_mask_2.focus_r = '0'
sample_holder_1_mask_2.p_interact = '0'
sample_holder_1_mask_2.mask_string = '"Holder_1"'
sample_holder_1_mask_2.mask_setting = '"Any"'
sample_holder_1_mask_2.number_of_activations = '1'
sample_holder_1_mask_2.init = '"init"'

# Comp instance sample_holder_1_mask_3, placement and parameters
sample_holder_1_mask_3 = instr.add_component('sample_holder_1_mask_3','Union_box', AT=['0', '0.0', '0.0065'], AT_RELATIVE='object_center', ROTATED=['0', '0.0', '0'], ROTATED_RELATIVE='object_center')

sample_holder_1_mask_3.material_string = '0'
sample_holder_1_mask_3.priority = '0'
sample_holder_1_mask_3.xwidth = '0.09'
sample_holder_1_mask_3.yheight = '0.02'
sample_holder_1_mask_3.zdepth = '0.005'
sample_holder_1_mask_3.xwidth2 = '-1'
sample_holder_1_mask_3.yheight2 = '-1'
sample_holder_1_mask_3.visualize = '1'
sample_holder_1_mask_3.target_index = '0'
sample_holder_1_mask_3.target_x = '0'
sample_holder_1_mask_3.target_y = '0'
sample_holder_1_mask_3.target_z = '0'
sample_holder_1_mask_3.focus_aw = '0'
sample_holder_1_mask_3.focus_ah = '0'
sample_holder_1_mask_3.focus_xw = '0'
sample_holder_1_mask_3.focus_xh = '0'
sample_holder_1_mask_3.focus_r = '0'
sample_holder_1_mask_3.p_interact = '0'
sample_holder_1_mask_3.mask_string = '"Holder_1"'
sample_holder_1_mask_3.mask_setting = '"Any"'
sample_holder_1_mask_3.number_of_activations = '1'
sample_holder_1_mask_3.init = '"init"'

# Comp instance sample_holder_1_mask_4, placement and parameters
sample_holder_1_mask_4 = instr.add_component('sample_holder_1_mask_4','Union_box', AT=['0', '0.0', '-0.0065'], AT_RELATIVE='object_center', ROTATED=['0', '0.0', '0'], ROTATED_RELATIVE='object_center')

sample_holder_1_mask_4.material_string = '0'
sample_holder_1_mask_4.priority = '0'
sample_holder_1_mask_4.xwidth = '0.09'
sample_holder_1_mask_4.yheight = '0.02'
sample_holder_1_mask_4.zdepth = '0.005'
sample_holder_1_mask_4.xwidth2 = '-1'
sample_holder_1_mask_4.yheight2 = '-1'
sample_holder_1_mask_4.visualize = '1'
sample_holder_1_mask_4.target_index = '0'
sample_holder_1_mask_4.target_x = '0'
sample_holder_1_mask_4.target_y = '0'
sample_holder_1_mask_4.target_z = '0'
sample_holder_1_mask_4.focus_aw = '0'
sample_holder_1_mask_4.focus_ah = '0'
sample_holder_1_mask_4.focus_xw = '0'
sample_holder_1_mask_4.focus_xh = '0'
sample_holder_1_mask_4.focus_r = '0'
sample_holder_1_mask_4.p_interact = '0'
sample_holder_1_mask_4.mask_string = '"Holder_1"'
sample_holder_1_mask_4.mask_setting = '"Any"'
sample_holder_1_mask_4.number_of_activations = '1'
sample_holder_1_mask_4.init = '"init"'

# Comp instance Holder_2, placement and parameters
Holder_2 = instr.add_component('Holder_2','Union_box', AT=['0', '0.25', '0'], AT_RELATIVE='object_center', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='object_center')

Holder_2.material_string = '"Al"'
Holder_2.priority = '10003'
Holder_2.xwidth = 'sword_width * 3'
Holder_2.yheight = '0.04'
Holder_2.zdepth = 'sword_depth * 3'
Holder_2.xwidth2 = 'sword_width * 3'
Holder_2.yheight2 = '0.04'
Holder_2.visualize = '1'
Holder_2.target_index = '0'
Holder_2.target_x = '0'
Holder_2.target_y = '0'
Holder_2.target_z = '0'
Holder_2.focus_aw = '0'
Holder_2.focus_ah = '0'
Holder_2.focus_xw = '0'
Holder_2.focus_xh = '0'
Holder_2.focus_r = '0'
Holder_2.p_interact = '0'
Holder_2.mask_string = '0'
Holder_2.mask_setting = '0'
Holder_2.number_of_activations = '1'
Holder_2.init = '"init"'

# Comp instance sample_holder_2_mask_1, placement and parameters
sample_holder_2_mask_1 = instr.add_component('sample_holder_2_mask_1','Union_box', AT=['0.036', '0.25', '0'], AT_RELATIVE='object_center', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='object_center')

sample_holder_2_mask_1.material_string = '0'
sample_holder_2_mask_1.priority = '0'
sample_holder_2_mask_1.xwidth = '0.005'
sample_holder_2_mask_1.yheight = '0.02'
sample_holder_2_mask_1.zdepth = 'sword_depth * 2.0'
sample_holder_2_mask_1.xwidth2 = '-1'
sample_holder_2_mask_1.yheight2 = '-1'
sample_holder_2_mask_1.visualize = '1'
sample_holder_2_mask_1.target_index = '0'
sample_holder_2_mask_1.target_x = '0'
sample_holder_2_mask_1.target_y = '0'
sample_holder_2_mask_1.target_z = '0'
sample_holder_2_mask_1.focus_aw = '0'
sample_holder_2_mask_1.focus_ah = '0'
sample_holder_2_mask_1.focus_xw = '0'
sample_holder_2_mask_1.focus_xh = '0'
sample_holder_2_mask_1.focus_r = '0'
sample_holder_2_mask_1.p_interact = '0'
sample_holder_2_mask_1.mask_string = '"Holder_2"'
sample_holder_2_mask_1.mask_setting = '"Any"'
sample_holder_2_mask_1.number_of_activations = '1'
sample_holder_2_mask_1.init = '"init"'

# Comp instance sample_holder_2_mask_2, placement and parameters
sample_holder_2_mask_2 = instr.add_component('sample_holder_2_mask_2','Union_box', AT=['-0.036', '0.25', '0'], AT_RELATIVE='object_center', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='object_center')

sample_holder_2_mask_2.material_string = '0'
sample_holder_2_mask_2.priority = '0'
sample_holder_2_mask_2.xwidth = '0.005'
sample_holder_2_mask_2.yheight = '0.02'
sample_holder_2_mask_2.zdepth = 'sword_depth * 2.0'
sample_holder_2_mask_2.xwidth2 = '-1'
sample_holder_2_mask_2.yheight2 = '-1'
sample_holder_2_mask_2.visualize = '1'
sample_holder_2_mask_2.target_index = '0'
sample_holder_2_mask_2.target_x = '0'
sample_holder_2_mask_2.target_y = '0'
sample_holder_2_mask_2.target_z = '0'
sample_holder_2_mask_2.focus_aw = '0'
sample_holder_2_mask_2.focus_ah = '0'
sample_holder_2_mask_2.focus_xw = '0'
sample_holder_2_mask_2.focus_xh = '0'
sample_holder_2_mask_2.focus_r = '0'
sample_holder_2_mask_2.p_interact = '0'
sample_holder_2_mask_2.mask_string = '"Holder_2"'
sample_holder_2_mask_2.mask_setting = '"Any"'
sample_holder_2_mask_2.number_of_activations = '1'
sample_holder_2_mask_2.init = '"init"'

# Comp instance sample_holder_2_mask_3, placement and parameters
sample_holder_2_mask_3 = instr.add_component('sample_holder_2_mask_3','Union_box', AT=['0', '0.25', '0.0055'], AT_RELATIVE='object_center', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='object_center')

sample_holder_2_mask_3.material_string = '0'
sample_holder_2_mask_3.priority = '0'
sample_holder_2_mask_3.xwidth = '0.078'
sample_holder_2_mask_3.yheight = '0.02'
sample_holder_2_mask_3.zdepth = '0.005'
sample_holder_2_mask_3.xwidth2 = '-1'
sample_holder_2_mask_3.yheight2 = '-1'
sample_holder_2_mask_3.visualize = '1'
sample_holder_2_mask_3.target_index = '0'
sample_holder_2_mask_3.target_x = '0'
sample_holder_2_mask_3.target_y = '0'
sample_holder_2_mask_3.target_z = '0'
sample_holder_2_mask_3.focus_aw = '0'
sample_holder_2_mask_3.focus_ah = '0'
sample_holder_2_mask_3.focus_xw = '0'
sample_holder_2_mask_3.focus_xh = '0'
sample_holder_2_mask_3.focus_r = '0'
sample_holder_2_mask_3.p_interact = '0'
sample_holder_2_mask_3.mask_string = '"Holder_2"'
sample_holder_2_mask_3.mask_setting = '"Any"'
sample_holder_2_mask_3.number_of_activations = '1'
sample_holder_2_mask_3.init = '"init"'

# Comp instance sample_holder_2_mask_4, placement and parameters
sample_holder_2_mask_4 = instr.add_component('sample_holder_2_mask_4','Union_box', AT=['0', '0.25', '-0.0055'], AT_RELATIVE='object_center', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='object_center')

sample_holder_2_mask_4.material_string = '0'
sample_holder_2_mask_4.priority = '0'
sample_holder_2_mask_4.xwidth = '0.078'
sample_holder_2_mask_4.yheight = '0.02'
sample_holder_2_mask_4.zdepth = '0.005'
sample_holder_2_mask_4.xwidth2 = '-1'
sample_holder_2_mask_4.yheight2 = '-1'
sample_holder_2_mask_4.visualize = '1'
sample_holder_2_mask_4.target_index = '0'
sample_holder_2_mask_4.target_x = '0'
sample_holder_2_mask_4.target_y = '0'
sample_holder_2_mask_4.target_z = '0'
sample_holder_2_mask_4.focus_aw = '0'
sample_holder_2_mask_4.focus_ah = '0'
sample_holder_2_mask_4.focus_xw = '0'
sample_holder_2_mask_4.focus_xh = '0'
sample_holder_2_mask_4.focus_r = '0'
sample_holder_2_mask_4.p_interact = '0'
sample_holder_2_mask_4.mask_string = '"Holder_2"'
sample_holder_2_mask_4.mask_setting = '"Any"'
sample_holder_2_mask_4.number_of_activations = '1'
sample_holder_2_mask_4.init = '"init"'

# Comp instance Holder_3, placement and parameters
Holder_3 = instr.add_component('Holder_3','Union_box', AT=['0', '-0.25', '0'], AT_RELATIVE='object_center', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='object_center')

Holder_3.material_string = '"Al"'
Holder_3.priority = '10004'
Holder_3.xwidth = 'sword_width * 3.0'
Holder_3.yheight = '0.04'
Holder_3.zdepth = 'sword_depth * 3.0'
Holder_3.xwidth2 = 'sword_width * 1.52'
Holder_3.yheight2 = '0.04'
Holder_3.visualize = '1'
Holder_3.target_index = '0'
Holder_3.target_x = '0'
Holder_3.target_y = '0'
Holder_3.target_z = '0'
Holder_3.focus_aw = '0'
Holder_3.focus_ah = '0'
Holder_3.focus_xw = '0'
Holder_3.focus_xh = '0'
Holder_3.focus_r = '0'
Holder_3.p_interact = '0'
Holder_3.mask_string = '0'
Holder_3.mask_setting = '0'
Holder_3.number_of_activations = '1'
Holder_3.init = '"init"'

# Comp instance sample_holder_3_mask_1, placement and parameters
sample_holder_3_mask_1 = instr.add_component('sample_holder_3_mask_1','Union_box', AT=['0.047', '-0.25', '0'], AT_RELATIVE='object_center', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='object_center')

sample_holder_3_mask_1.material_string = '0'
sample_holder_3_mask_1.priority = '0'
sample_holder_3_mask_1.xwidth = '0.005'
sample_holder_3_mask_1.yheight = '0.02'
sample_holder_3_mask_1.zdepth = 'sword_depth * 1.9'
sample_holder_3_mask_1.xwidth2 = '-1'
sample_holder_3_mask_1.yheight2 = '-1'
sample_holder_3_mask_1.visualize = '1'
sample_holder_3_mask_1.target_index = '0'
sample_holder_3_mask_1.target_x = '0'
sample_holder_3_mask_1.target_y = '0'
sample_holder_3_mask_1.target_z = '0'
sample_holder_3_mask_1.focus_aw = '0'
sample_holder_3_mask_1.focus_ah = '0'
sample_holder_3_mask_1.focus_xw = '0'
sample_holder_3_mask_1.focus_xh = '0'
sample_holder_3_mask_1.focus_r = '0'
sample_holder_3_mask_1.p_interact = '0'
sample_holder_3_mask_1.mask_string = '"Holder_3"'
sample_holder_3_mask_1.mask_setting = '"Any"'
sample_holder_3_mask_1.number_of_activations = '1'
sample_holder_3_mask_1.init = '"init"'

# Comp instance sample_holder_3_mask_2, placement and parameters
sample_holder_3_mask_2 = instr.add_component('sample_holder_3_mask_2','Union_box', AT=['-0.047', '-0.25', '0'], AT_RELATIVE='object_center', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='object_center')

sample_holder_3_mask_2.material_string = '0'
sample_holder_3_mask_2.priority = '0'
sample_holder_3_mask_2.xwidth = '0.005'
sample_holder_3_mask_2.yheight = '0.02'
sample_holder_3_mask_2.zdepth = 'sword_depth * 1.9'
sample_holder_3_mask_2.xwidth2 = '-1'
sample_holder_3_mask_2.yheight2 = '-1'
sample_holder_3_mask_2.visualize = '1'
sample_holder_3_mask_2.target_index = '0'
sample_holder_3_mask_2.target_x = '0'
sample_holder_3_mask_2.target_y = '0'
sample_holder_3_mask_2.target_z = '0'
sample_holder_3_mask_2.focus_aw = '0'
sample_holder_3_mask_2.focus_ah = '0'
sample_holder_3_mask_2.focus_xw = '0'
sample_holder_3_mask_2.focus_xh = '0'
sample_holder_3_mask_2.focus_r = '0'
sample_holder_3_mask_2.p_interact = '0'
sample_holder_3_mask_2.mask_string = '"Holder_3"'
sample_holder_3_mask_2.mask_setting = '"Any"'
sample_holder_3_mask_2.number_of_activations = '1'
sample_holder_3_mask_2.init = '"init"'

# Comp instance sample_holder_3_mask_3, placement and parameters
sample_holder_3_mask_3 = instr.add_component('sample_holder_3_mask_3','Union_box', AT=['0', '-0.25', '0.007'], AT_RELATIVE='object_center', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='object_center')

sample_holder_3_mask_3.material_string = '0'
sample_holder_3_mask_3.priority = '0'
sample_holder_3_mask_3.xwidth = '0.1'
sample_holder_3_mask_3.yheight = '0.02'
sample_holder_3_mask_3.zdepth = '0.005'
sample_holder_3_mask_3.xwidth2 = '-1'
sample_holder_3_mask_3.yheight2 = '-1'
sample_holder_3_mask_3.visualize = '1'
sample_holder_3_mask_3.target_index = '0'
sample_holder_3_mask_3.target_x = '0'
sample_holder_3_mask_3.target_y = '0'
sample_holder_3_mask_3.target_z = '0'
sample_holder_3_mask_3.focus_aw = '0'
sample_holder_3_mask_3.focus_ah = '0'
sample_holder_3_mask_3.focus_xw = '0'
sample_holder_3_mask_3.focus_xh = '0'
sample_holder_3_mask_3.focus_r = '0'
sample_holder_3_mask_3.p_interact = '0'
sample_holder_3_mask_3.mask_string = '"Holder_3"'
sample_holder_3_mask_3.mask_setting = '"Any"'
sample_holder_3_mask_3.number_of_activations = '1'
sample_holder_3_mask_3.init = '"init"'

# Comp instance sample_holder_3_mask_4, placement and parameters
sample_holder_3_mask_4 = instr.add_component('sample_holder_3_mask_4','Union_box', AT=['0', '-0.25', '-0.007'], AT_RELATIVE='object_center', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='object_center')

sample_holder_3_mask_4.material_string = '0'
sample_holder_3_mask_4.priority = '0'
sample_holder_3_mask_4.xwidth = '0.1'
sample_holder_3_mask_4.yheight = '0.02'
sample_holder_3_mask_4.zdepth = '0.005'
sample_holder_3_mask_4.xwidth2 = '-1'
sample_holder_3_mask_4.yheight2 = '-1'
sample_holder_3_mask_4.visualize = '1'
sample_holder_3_mask_4.target_index = '0'
sample_holder_3_mask_4.target_x = '0'
sample_holder_3_mask_4.target_y = '0'
sample_holder_3_mask_4.target_z = '0'
sample_holder_3_mask_4.focus_aw = '0'
sample_holder_3_mask_4.focus_ah = '0'
sample_holder_3_mask_4.focus_xw = '0'
sample_holder_3_mask_4.focus_xh = '0'
sample_holder_3_mask_4.focus_r = '0'
sample_holder_3_mask_4.p_interact = '0'
sample_holder_3_mask_4.mask_string = '"Holder_3"'
sample_holder_3_mask_4.mask_setting = '"Any"'
sample_holder_3_mask_4.number_of_activations = '1'
sample_holder_3_mask_4.init = '"init"'

# Comp instance detector_exit, placement and parameters
detector_exit = instr.add_component('detector_exit','Union_box', AT=['0', '0', 'pinhole_detector_distance + 0.05'], AT_RELATIVE='graph', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='graph')

detector_exit.material_string = '"Exit"'
detector_exit.priority = '10000000'
detector_exit.xwidth = '0.3'
detector_exit.yheight = '0.3'
detector_exit.zdepth = '0.101'
detector_exit.xwidth2 = '-1'
detector_exit.yheight2 = '-1'
detector_exit.visualize = '1'
detector_exit.target_index = '0'
detector_exit.target_x = '0'
detector_exit.target_y = '0'
detector_exit.target_z = '0'
detector_exit.focus_aw = '0'
detector_exit.focus_ah = '0'
detector_exit.focus_xw = '0'
detector_exit.focus_xh = '0'
detector_exit.focus_r = '0'
detector_exit.p_interact = '0'
detector_exit.mask_string = '0'
detector_exit.mask_setting = '0'
detector_exit.number_of_activations = '1'
detector_exit.init = '"init"'

# Comp instance Sword, placement and parameters
Sword = instr.add_component('Sword','Union_master', AT=['0', '0', '0'], AT_RELATIVE='a1', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='a1')
# WHEN ( Sample == 1 ) at Sword
Sword.set_WHEN('( Sample == 1 )')

Sword.verbal = '1'
Sword.list_verbal = '0'
Sword.finally_verbal = '0'
Sword.allow_inside_start = '0'
Sword.enable_tagging = '0'
Sword.history_limit = '300000'
Sword.enable_conditionals = '1'
Sword.inherit_number_of_scattering_events = '0'
Sword.init = '"init"'

# Comp instance Stop, placement and parameters
Stop = instr.add_component('Stop','Union_stop', AT=['0', '0', '0'], AT_RELATIVE='a1', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='a1')


# Comp instance screen, placement and parameters
screen = instr.add_component('screen','PSD_monitor_Filter', AT=['0', '0', 'pinhole_detector_distance'], AT_RELATIVE='graph', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='graph')

screen.nx = '300'
screen.ny = '300'
screen.nL = '200'
screen.filter_pixels = '600'
screen.filename = '"absoprtion_picture.dat"'
screen.xmin = '-0.05'
screen.xmax = '0.05'
screen.ymin = '-0.05'
screen.ymax = '0.05'
screen.xwidth = '0.3'
screen.yheight = '0.3'
screen.restore_neutron = '0'
screen.nowritefile = '0'
screen.TwoD_filename = 'spacial_resolution'
screen.L_filename = 'wavelength_spectrum'
screen.Lmin = '0'
screen.Lmax = '10'
screen.aply_xy_filter = '1'
screen.filter_xmin = '-0.8'
screen.filter_xmax = '0.8'
screen.filter_ymin = '-0.8'
screen.filter_ymax = '0.8'
screen.pinhol_filter_distance = '25.025'
screen.pinhol_detector_distance = 'pinhole_detector_distance'
screen.smoothing = '3.0'
screen.zoom = 'Zoom'

# Comp instance L_monitor, placement and parameters
L_monitor = instr.add_component('L_monitor','L_monitor', AT=['0.0', '0.0', 'pinhole_detector_distance'], AT_RELATIVE='screen', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='screen')

L_monitor.nL = '200'
L_monitor.filename = '"I_lambda.dat"'
L_monitor.nowritefile = '0'
L_monitor.xmin = '-0.05'
L_monitor.xmax = '0.05'
L_monitor.ymin = '-0.05'
L_monitor.ymax = '0.05'
L_monitor.xwidth = '1'
L_monitor.yheight = '1'
L_monitor.Lmin = '0'
L_monitor.Lmax = '10'
L_monitor.restore_neutron = '1'

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


# end of generated Python code Sword_ODIN_generated.py 
