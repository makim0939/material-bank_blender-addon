import  bpy
from MaterialBank.models.MaterialMod import *
#ボタン
class Read_OT_Button(bpy.types.Operator):
    bl_idname = "button.read"
    bl_label = "Read"
    
    def execute(self, context):
        selected = context.scene.myInputs.Option_Materials
        materials = MaterialMod.read_materials()
        for mtr in materials:
            if mtr.name == selected:
                material = mtr

        MaterialMod.generate_material(material)  
        return {"FINISHED"}