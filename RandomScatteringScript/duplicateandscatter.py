import maya.cmds as cmds
import random

window_name = "duplicateAndScatterWindow"

if cmds.window(window_name, exists=True):
    cmds.deleteUI(window_name)

window = cmds.window(window_name, title="Duplicate and Scatter Objects", widthHeight=(300, 100))
cmds.columnLayout(adjustableColumn=True)

amount_field = cmds.intField(minValue=1, value=1)
radius_field = cmds.floatField(minValue=0.1, value=1.0)


def duplicate_and_scatter_objects(*args):
    amount_value = cmds.intField(amount_field, query=True, value=True)
    radius_value = cmds.floatField(radius_field, query=True, value=True)
    
    selected_objects = cmds.ls(selection=True) or []
    
    for obj in selected_objects:
        obj_position = cmds.xform(obj, query=True, translation=True, worldSpace=True)
        
        for _ in range(amount_value):
            duplicated_objects = cmds.duplicate(obj)
            new_object = duplicated_objects[0]
            
            random_x = random.uniform(-radius_value, radius_value)
            random_y = random.uniform(-radius_value, radius_value)
            random_z = random.uniform(-radius_value, radius_value)
            
            cmds.move(obj_position[0] + random_x, obj_position[1] + random_y, obj_position[2] + random_z, new_object)
            
            
cmds.button(label="OK", command=duplicate_and_scatter_objects)
cmds.button(label="Cancel", command=lambda *args: cmds.deleteUI(window_name))

cmds.showWindow(window_name)
