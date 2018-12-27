import bpy
import mathutils
import math

startFrame = 0
endFrame = 150
sequencePath = "path/2/objfiles"
bpy.context.scene.frame_start = 0
bpy.context.scene.frame_end = endFrame - startFrame
current_Frame = 0

bpy.data.objects["Camera"].location = mathutils.Vector((0.0, -4.5, 1))
bpy.data.objects["Camera"].rotation_euler = mathutils.Euler((math.radians(90.0),0.0,  0.0), 'XYZ')

bpy.data.objects["Lamp"].location = mathutils.Vector((2.0, -5.0, 4))
bpy.data.objects["Lamp"].select = True
bpy.data.objects["Lamp"].keyframe_insert(data_path='location', frame=startFrame)
bpy.ops.transform.translate(value=(-4, 0, 0))
bpy.data.objects["Lamp"].keyframe_insert(data_path='location', frame=endFrame/2)
bpy.ops.transform.translate(value=(4, 0, 0))
bpy.data.objects["Lamp"].keyframe_insert(data_path='location', frame=endFrame)

bpy.ops.object.select_all(action = 'DESELECT')

for i in range(startFrame,endFrame):
    file = "%s%04d.obj" % (sequencePath,i)
    mesh = bpy.ops.import_scene.obj(filepath = file,filter_glob="*.obj")#,axis_forward='-X', axis_up='Z')

    bpy.ops.object.shade_smooth()

    bpy.context.selected_objects[0].hide_render = True
    bpy.context.selected_objects[0].keyframe_insert(data_path = "hide_render",index=-1,frame = 0)
    bpy.context.selected_objects[0].keyframe_insert(data_path = "hide_render",index=-1,frame = current_Frame +1)
    bpy.context.selected_objects[0].hide_render = False
    bpy.context.selected_objects[0].keyframe_insert(data_path = "hide_render",index=-1,frame = current_Frame )
    
    bpy.context.selected_objects[0].hide = True
    bpy.context.selected_objects[0].keyframe_insert(data_path = "hide",index=-1,frame = 0)
    bpy.context.selected_objects[0].keyframe_insert(data_path = "hide",index=-1,frame = current_Frame +1)
    bpy.context.selected_objects[0].hide = False
    bpy.context.selected_objects[0].keyframe_insert(data_path = "hide",index=-1,frame = current_Frame )
    bpy.ops.object.select_all(action = 'DESELECT')
    
    current_Frame += 1