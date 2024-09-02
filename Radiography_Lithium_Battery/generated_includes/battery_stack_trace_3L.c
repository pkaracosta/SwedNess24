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
