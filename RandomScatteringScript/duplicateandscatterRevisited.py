import maya.cmds as cmds
import random

def duplicate_objects(x_range, y_range, z_range, num_duplicates):
    # Get selected object
    selection = cmds.ls(selection=True)
    if not selection:
        cmds.warning("Please select an object to duplicate.")
        return
    
    obj = selection[0]
    
    # Duplicate and randomize position and rotation
    for i in range(num_duplicates):
        dup = cmds.duplicate(obj)[0]
        x_pos = random.uniform(-x_range, x_range)
        y_pos = random.uniform(-y_range, y_range)
        z_pos = random.uniform(-z_range, z_range)
        cmds.move(x_pos, y_pos, z_pos, dup)
        
        x_rot = random.uniform(-15, 15)
        y_rot = random.uniform(-15, 15)
        z_rot = random.uniform(-15, 15)
        cmds.rotate(x_rot, y_rot, z_rot, dup, relative=True)
        
        cmds.select(clear=True)

# Create UI
if cmds.window('duplicateObjectsWindow', exists=True):
    cmds.deleteUI('duplicateObjectsWindow')

window = cmds.window('duplicateObjectsWindow', title='Duplicate Objects', widthHeight=(300, 150))
cmds.columnLayout(adjustableColumn=True)
cmds.text(label='Enter Range for X Direction:')
x_range_field = cmds.floatFieldGrp('x_range', numberOfFields=1, label='X Range', value1=5.0)
cmds.text(label='Enter Range for Y Direction:')
y_range_field = cmds.floatFieldGrp('y_range', numberOfFields=1, label='Y Range', value1=5.0)
cmds.text(label='Enter Range for Z Direction:')
z_range_field = cmds.floatFieldGrp('z_range', numberOfFields=1, label='Z Range', value1=5.0)
cmds.text(label='Enter Number of Duplicates:')
num_duplicates_field = cmds.intFieldGrp('num_duplicates', numberOfFields=1, label='Number of Duplicates', value1=5)

# Callback function to retrieve input values and call duplicate_objects function
def duplicate_callback(*args):
    x_range = cmds.floatFieldGrp(x_range_field, query=True, value1=True)
    y_range = cmds.floatFieldGrp(y_range_field, query=True, value1=True)
    z_range = cmds.floatFieldGrp(z_range_field, query=True, value1=True)
    num_duplicates = cmds.intFieldGrp(num_duplicates_field, query=True, value1=True)
    duplicate_objects(x_range, y_range, z_range, num_duplicates)

cmds.button(label='Duplicate', command=duplicate_callback)
cmds.showWindow(window)
