import bpy
from models.MaterialMod import *
#ボタン
class Store_OT_Button(bpy.types.Operator):
    bl_idname = "button.store"
    bl_label = "Store"
    
    def execute(self, context):

        #入力されたマテリアル名を取得
        materialName = bpy.context.scene.myInputs.TextField_Name
        #同じマテリアル名があるかをチェック
        materials = MaterialMod.read_materials()
        for mtr in materials:
            if materialName == mtr.name:
                print("既存のマテリアル名") 
                return {"FINISHED"}

        MaterialMod.store_material()
        return {"FINISHED"}
