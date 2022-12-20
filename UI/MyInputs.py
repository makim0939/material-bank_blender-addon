import bpy
from models.MaterialMod import *
#カスタムインプット
class MyInputs(bpy.types.PropertyGroup):
    #テキストボックス
    TextField_Name: bpy.props.StringProperty(
        name="Name",
        maxlen=32
    )

    #オプション入力
    #選択が更新された時に呼び出されるメソッド
    def update_material_selection(self, context):
        print(self.Option_Materials.items)

    def get_option_items(self, context):
        #テキストファイルからマテリアルを読み込み
        materials = MaterialMod.read_materials()
        #選択肢入力に必要なパラメータitemsを作成
        option_items = []
        for material in materials:
            #マテリアル情報のタプルをリストに追加していく
            option_items.append((material.name, material.name, ""))
        return option_items

    Option_Materials: bpy.props.EnumProperty(
        name = "Material",
        items = get_option_items,
        update = update_material_selection
    )

