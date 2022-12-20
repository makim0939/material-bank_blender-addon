bl_info = {
    "name": "Material Bank",
    "author": "takoyaki3329",
    "version": (1, 0),
    "blender": (3, 2, 2),
    "location": "View3D > Sidebar",
    "description": "Store and use your favorite materials",
    "warning": "",
    "doc_url": "",
    "category": "3D View",
}




import bpy 
from models.Material import *
from models.MaterialMod import *
from UI.MaterialBank_PT_Read import *
from UI.MaterialBank_PT_Store import *
from UI.MyInputs import *
from UI.Read_OT_Button import *
from UI.Store_OT_Button import *
# ===== UIクラスの登録 ===== #

def register():
    #UIのクラスを登録
    #自作プロパティ
    bpy.utils.register_class(MyInputs)
    #マテリアル保存用
    bpy.utils.register_class(MaterialBank_PT_Store)
    bpy.utils.register_class(Store_OT_Button)
    #マテリアル読み込み用
    bpy.utils.register_class(MaterialBank_PT_Read)
    bpy.utils.register_class(Read_OT_Button)

    #何やってるかいまいちわからん、、、
    bpy.types.Scene.myInputs = bpy.props.PointerProperty(type=MyInputs)


def unregister():
    #自作プロパティ
    bpy.utils.unregister_class(MyInputs)
    #マテリアル保存用
    bpy.utils.unregister_class(MaterialBank_PT_Store)
    bpy.utils.unregister_class(Store_OT_Button)
    #マテリアル読み込み用
    bpy.utils.unregister_class(MaterialBank_PT_Read)
    bpy.utils.unregister_class(Read_OT_Button)

    del bpy.types.Scene.myInputs

if __name__ == "__main__":
    register()