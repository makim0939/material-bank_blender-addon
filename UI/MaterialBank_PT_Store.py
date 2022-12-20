import bpy
from MaterialBank.UI.MyInputs import * 
#パネル
class MaterialBank_PT_Store(bpy.types.Panel):
    bl_idname = "VIEW3D_PT_materialbank_sotre"
    bl_label = "Store"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MTRBank"

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene.myInputs, "TextField_Name")
        layout.operator("button.store")
