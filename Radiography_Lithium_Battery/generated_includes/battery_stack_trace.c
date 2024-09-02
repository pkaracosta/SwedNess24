// Start of trace section for generated battery_stack
// Seperator box with low priority and all edges
COMPONENT seperator = Union_box(
xwidth=battery_width,yheight=battery_thickness_m,zdepth=battery_depth,
priority=50,material_string="Electrolyte")
AT (0,0,0) RELATIVE samplearm

COMPONENT battery_bottom = Arm()
AT (0,-0.5*battery_thickness_m,0) RELATIVE seperator

// Positive electrode box
COMPONENT positive_electrode_layer_0 = Union_box(
xwidth=battery_width-end_safety,zdepth=battery_depth-end_safety,
yheight=2*positive_electrode_thickness_m+positive_foil_thickness_m,
priority=50.1 + 0.0,material_string="LiFePO4")
AT (0,positive_foil_center[0],0) RELATIVE battery_bottom

// Positive foil box
COMPONENT positive_foil_layer_0 = Union_box(
xwidth=battery_width-2*end_safety,yheight=positive_foil_thickness_m,zdepth=battery_depth-2*end_safety,
priority=50.2 + 0.0,material_string="Aluminum")
AT (0,positive_foil_center[0],0) RELATIVE battery_bottom

// Negative electrode box
COMPONENT negative_electrode_layer_0 = Union_box(
xwidth=battery_width-end_safety,zdepth=battery_depth-end_safety,
yheight=2*negative_electrode_thickness_m+negative_foil_thickness_m,
priority=50.4 + 0.0,material_string="LiC6")
AT (0,negative_foil_center[0],0) RELATIVE battery_bottom

// Negative foil box
COMPONENT negative_foil_layer_0 = Union_box(
xwidth=battery_width-2*end_safety,yheight=positive_foil_thickness_m,zdepth=battery_depth-2*end_safety,
priority=50.5 + 0.0,material_string="Copper")
AT (0,negative_foil_center[0],0) RELATIVE battery_bottom

// Positive electrode box
COMPONENT positive_electrode_layer_1 = Union_box(
xwidth=battery_width-end_safety,zdepth=battery_depth-end_safety,
yheight=2*positive_electrode_thickness_m+positive_foil_thickness_m,
priority=50.1 + 1.0,material_string="LiFePO4")
AT (0,positive_foil_center[1],0) RELATIVE battery_bottom

// Positive foil box
COMPONENT positive_foil_layer_1 = Union_box(
xwidth=battery_width-2*end_safety,yheight=positive_foil_thickness_m,zdepth=battery_depth-2*end_safety,
priority=50.2 + 1.0,material_string="Aluminum")
AT (0,positive_foil_center[1],0) RELATIVE battery_bottom

// Negative electrode box
COMPONENT negative_electrode_layer_1 = Union_box(
xwidth=battery_width-end_safety,zdepth=battery_depth-end_safety,
yheight=2*negative_electrode_thickness_m+negative_foil_thickness_m,
priority=50.4 + 1.0,material_string="LiC6")
AT (0,negative_foil_center[1],0) RELATIVE battery_bottom

// Negative foil box
COMPONENT negative_foil_layer_1 = Union_box(
xwidth=battery_width-2*end_safety,yheight=positive_foil_thickness_m,zdepth=battery_depth-2*end_safety,
priority=50.5 + 1.0,material_string="Copper")
AT (0,negative_foil_center[1],0) RELATIVE battery_bottom

// Positive electrode box
COMPONENT positive_electrode_layer_2 = Union_box(
xwidth=battery_width-end_safety,zdepth=battery_depth-end_safety,
yheight=2*positive_electrode_thickness_m+positive_foil_thickness_m,
priority=50.1 + 2.0,material_string="LiFePO4")
AT (0,positive_foil_center[2],0) RELATIVE battery_bottom

// Positive foil box
COMPONENT positive_foil_layer_2 = Union_box(
xwidth=battery_width-2*end_safety,yheight=positive_foil_thickness_m,zdepth=battery_depth-2*end_safety,
priority=50.2 + 2.0,material_string="Aluminum")
AT (0,positive_foil_center[2],0) RELATIVE battery_bottom

// Negative electrode box
COMPONENT negative_electrode_layer_2 = Union_box(
xwidth=battery_width-end_safety,zdepth=battery_depth-end_safety,
yheight=2*negative_electrode_thickness_m+negative_foil_thickness_m,
priority=50.4 + 2.0,material_string="LiC6")
AT (0,negative_foil_center[2],0) RELATIVE battery_bottom

// Negative foil box
COMPONENT negative_foil_layer_2 = Union_box(
xwidth=battery_width-2*end_safety,yheight=positive_foil_thickness_m,zdepth=battery_depth-2*end_safety,
priority=50.5 + 2.0,material_string="Copper")
AT (0,negative_foil_center[2],0) RELATIVE battery_bottom

// Positive electrode box
COMPONENT positive_electrode_layer_3 = Union_box(
xwidth=battery_width-end_safety,zdepth=battery_depth-end_safety,
yheight=2*positive_electrode_thickness_m+positive_foil_thickness_m,
priority=50.1 + 3.0,material_string="LiFePO4")
AT (0,positive_foil_center[3],0) RELATIVE battery_bottom

// Positive foil box
COMPONENT positive_foil_layer_3 = Union_box(
xwidth=battery_width-2*end_safety,yheight=positive_foil_thickness_m,zdepth=battery_depth-2*end_safety,
priority=50.2 + 3.0,material_string="Aluminum")
AT (0,positive_foil_center[3],0) RELATIVE battery_bottom

// Negative electrode box
COMPONENT negative_electrode_layer_3 = Union_box(
xwidth=battery_width-end_safety,zdepth=battery_depth-end_safety,
yheight=2*negative_electrode_thickness_m+negative_foil_thickness_m,
priority=50.4 + 3.0,material_string="LiC6")
AT (0,negative_foil_center[3],0) RELATIVE battery_bottom

// Negative foil box
COMPONENT negative_foil_layer_3 = Union_box(
xwidth=battery_width-2*end_safety,yheight=positive_foil_thickness_m,zdepth=battery_depth-2*end_safety,
priority=50.5 + 3.0,material_string="Copper")
AT (0,negative_foil_center[3],0) RELATIVE battery_bottom

// Positive electrode box
COMPONENT positive_electrode_layer_4 = Union_box(
xwidth=battery_width-end_safety,zdepth=battery_depth-end_safety,
yheight=2*positive_electrode_thickness_m+positive_foil_thickness_m,
priority=50.1 + 4.0,material_string="LiFePO4")
AT (0,positive_foil_center[4],0) RELATIVE battery_bottom

// Positive foil box
COMPONENT positive_foil_layer_4 = Union_box(
xwidth=battery_width-2*end_safety,yheight=positive_foil_thickness_m,zdepth=battery_depth-2*end_safety,
priority=50.2 + 4.0,material_string="Aluminum")
AT (0,positive_foil_center[4],0) RELATIVE battery_bottom

// Negative electrode box
COMPONENT negative_electrode_layer_4 = Union_box(
xwidth=battery_width-end_safety,zdepth=battery_depth-end_safety,
yheight=2*negative_electrode_thickness_m+negative_foil_thickness_m,
priority=50.4 + 4.0,material_string="LiC6")
AT (0,negative_foil_center[4],0) RELATIVE battery_bottom

// Negative foil box
COMPONENT negative_foil_layer_4 = Union_box(
xwidth=battery_width-2*end_safety,yheight=positive_foil_thickness_m,zdepth=battery_depth-2*end_safety,
priority=50.5 + 4.0,material_string="Copper")
AT (0,negative_foil_center[4],0) RELATIVE battery_bottom

// Positive electrode box
COMPONENT positive_electrode_layer_5 = Union_box(
xwidth=battery_width-end_safety,zdepth=battery_depth-end_safety,
yheight=2*positive_electrode_thickness_m+positive_foil_thickness_m,
priority=50.1 + 5.0,material_string="LiFePO4")
AT (0,positive_foil_center[5],0) RELATIVE battery_bottom

// Positive foil box
COMPONENT positive_foil_layer_5 = Union_box(
xwidth=battery_width-2*end_safety,yheight=positive_foil_thickness_m,zdepth=battery_depth-2*end_safety,
priority=50.2 + 5.0,material_string="Aluminum")
AT (0,positive_foil_center[5],0) RELATIVE battery_bottom

// Negative electrode box
COMPONENT negative_electrode_layer_5 = Union_box(
xwidth=battery_width-end_safety,zdepth=battery_depth-end_safety,
yheight=2*negative_electrode_thickness_m+negative_foil_thickness_m,
priority=50.4 + 5.0,material_string="LiC6")
AT (0,negative_foil_center[5],0) RELATIVE battery_bottom

// Negative foil box
COMPONENT negative_foil_layer_5 = Union_box(
xwidth=battery_width-2*end_safety,yheight=positive_foil_thickness_m,zdepth=battery_depth-2*end_safety,
priority=50.5 + 5.0,material_string="Copper")
AT (0,negative_foil_center[5],0) RELATIVE battery_bottom

// Positive electrode box
COMPONENT positive_electrode_layer_6 = Union_box(
xwidth=battery_width-end_safety,zdepth=battery_depth-end_safety,
yheight=2*positive_electrode_thickness_m+positive_foil_thickness_m,
priority=50.1 + 6.0,material_string="LiFePO4")
AT (0,positive_foil_center[6],0) RELATIVE battery_bottom

// Positive foil box
COMPONENT positive_foil_layer_6 = Union_box(
xwidth=battery_width-2*end_safety,yheight=positive_foil_thickness_m,zdepth=battery_depth-2*end_safety,
priority=50.2 + 6.0,material_string="Aluminum")
AT (0,positive_foil_center[6],0) RELATIVE battery_bottom

// Negative electrode box
COMPONENT negative_electrode_layer_6 = Union_box(
xwidth=battery_width-end_safety,zdepth=battery_depth-end_safety,
yheight=2*negative_electrode_thickness_m+negative_foil_thickness_m,
priority=50.4 + 6.0,material_string="LiC6")
AT (0,negative_foil_center[6],0) RELATIVE battery_bottom

// Negative foil box
COMPONENT negative_foil_layer_6 = Union_box(
xwidth=battery_width-2*end_safety,yheight=positive_foil_thickness_m,zdepth=battery_depth-2*end_safety,
priority=50.5 + 6.0,material_string="Copper")
AT (0,negative_foil_center[6],0) RELATIVE battery_bottom

// Positive electrode box
COMPONENT positive_electrode_layer_7 = Union_box(
xwidth=battery_width-end_safety,zdepth=battery_depth-end_safety,
yheight=2*positive_electrode_thickness_m+positive_foil_thickness_m,
priority=50.1 + 7.0,material_string="LiFePO4")
AT (0,positive_foil_center[7],0) RELATIVE battery_bottom

// Positive foil box
COMPONENT positive_foil_layer_7 = Union_box(
xwidth=battery_width-2*end_safety,yheight=positive_foil_thickness_m,zdepth=battery_depth-2*end_safety,
priority=50.2 + 7.0,material_string="Aluminum")
AT (0,positive_foil_center[7],0) RELATIVE battery_bottom

// Negative electrode box
COMPONENT negative_electrode_layer_7 = Union_box(
xwidth=battery_width-end_safety,zdepth=battery_depth-end_safety,
yheight=2*negative_electrode_thickness_m+negative_foil_thickness_m,
priority=50.4 + 7.0,material_string="LiC6")
AT (0,negative_foil_center[7],0) RELATIVE battery_bottom

// Negative foil box
COMPONENT negative_foil_layer_7 = Union_box(
xwidth=battery_width-2*end_safety,yheight=positive_foil_thickness_m,zdepth=battery_depth-2*end_safety,
priority=50.5 + 7.0,material_string="Copper")
AT (0,negative_foil_center[7],0) RELATIVE battery_bottom

// Positive electrode box
COMPONENT positive_electrode_layer_8 = Union_box(
xwidth=battery_width-end_safety,zdepth=battery_depth-end_safety,
yheight=2*positive_electrode_thickness_m+positive_foil_thickness_m,
priority=50.1 + 8.0,material_string="LiFePO4")
AT (0,positive_foil_center[8],0) RELATIVE battery_bottom

// Positive foil box
COMPONENT positive_foil_layer_8 = Union_box(
xwidth=battery_width-2*end_safety,yheight=positive_foil_thickness_m,zdepth=battery_depth-2*end_safety,
priority=50.2 + 8.0,material_string="Aluminum")
AT (0,positive_foil_center[8],0) RELATIVE battery_bottom

// Negative electrode box
COMPONENT negative_electrode_layer_8 = Union_box(
xwidth=battery_width-end_safety,zdepth=battery_depth-end_safety,
yheight=2*negative_electrode_thickness_m+negative_foil_thickness_m,
priority=50.4 + 8.0,material_string="LiC6")
AT (0,negative_foil_center[8],0) RELATIVE battery_bottom

// Negative foil box
COMPONENT negative_foil_layer_8 = Union_box(
xwidth=battery_width-2*end_safety,yheight=positive_foil_thickness_m,zdepth=battery_depth-2*end_safety,
priority=50.5 + 8.0,material_string="Copper")
AT (0,negative_foil_center[8],0) RELATIVE battery_bottom

// Positive electrode box
COMPONENT positive_electrode_layer_9 = Union_box(
xwidth=battery_width-end_safety,zdepth=battery_depth-end_safety,
yheight=2*positive_electrode_thickness_m+positive_foil_thickness_m,
priority=50.1 + 9.0,material_string="LiFePO4")
AT (0,positive_foil_center[9],0) RELATIVE battery_bottom

// Positive foil box
COMPONENT positive_foil_layer_9 = Union_box(
xwidth=battery_width-2*end_safety,yheight=positive_foil_thickness_m,zdepth=battery_depth-2*end_safety,
priority=50.2 + 9.0,material_string="Aluminum")
AT (0,positive_foil_center[9],0) RELATIVE battery_bottom

// Negative electrode box
COMPONENT negative_electrode_layer_9 = Union_box(
xwidth=battery_width-end_safety,zdepth=battery_depth-end_safety,
yheight=2*negative_electrode_thickness_m+negative_foil_thickness_m,
priority=50.4 + 9.0,material_string="LiC6")
AT (0,negative_foil_center[9],0) RELATIVE battery_bottom

// Negative foil box
COMPONENT negative_foil_layer_9 = Union_box(
xwidth=battery_width-2*end_safety,yheight=positive_foil_thickness_m,zdepth=battery_depth-2*end_safety,
priority=50.5 + 9.0,material_string="Copper")
AT (0,negative_foil_center[9],0) RELATIVE battery_bottom

