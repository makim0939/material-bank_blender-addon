import bpy
from MaterialBank.UI.MyInputs import * 
class MaterialBank_PT_Read(bpy.types.Panel):
    bl_idname = "VIEW3D_PT_materialbank_Read"
    bl_label = "Read"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MTRBank"

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene.myInputs, "Option_Materials")
        layout.operator("button.read")