import bpy
from models.Material import *
BANK_PAHT = __file__.replace("models\MaterialMod.py", "") + "txt"

class MaterialMod:
    # ===== マテリアル作成メソッド ===== #
    def generate_material(mtr):
        #マテリアルを作成
        material = bpy.data.materials.new(mtr.name)
        #ノードを使える用にする
        material.use_nodes = True
        #ノードツリーを取得
        node_tree = material.node_tree
        #デフォルトノードを削除
        node_tree.nodes.clear()
        for node in mtr.nodes:
            
            node_tree.nodes.new(node)
        


    # ===== マテリアル保存メソッド ===== #

    def store_material():
        #アクティブオブジェクトを取得
        obj = bpy.context.object

        #オブジェクトのマテリアルを取得
        mtrSlots = obj.material_slots

        #マテリアル名を取得
        name = bpy.context.scene.myInputs.TextField_Name
        #ノードツリーを取得し、ノードとリンクを取得
        node_tree = mtrSlots[0].material.node_tree
        nodes = node_tree.nodes
        links = node_tree.links

        nodes_data = []
        for node in nodes:
            nodes_data.append(node.bl_idname) 
        links_data = []
        for link in links:
            links_data.append({"nodeOut":link.from_node.bl_idname,
                                "socketOut":link.from_socket.name,
                                "nodeIn": link.to_node.bl_idname,
                                "socketIn": link.to_socket.name
                                })
        #マテリアルオブジェクトを作成
        mtr = Material(name, nodes_data, links_data)

        mtrData = mtr.create_mtr_text()

        #ファイルに書き込む
        f = open(BANK_PAHT, "a")
        f.write(mtrData)
        f.close()
        #TODO マテリアルを保存した後、読み込み側パネルの選択肢を更新する
        #bpy.types.VIEW3D_PT_materialbank_Read.draw(bpy.types.VIEW3D_PT_materialbank_Read, bpy.context)
        
        


    # ===== テキストファイルからマテリアルオブジェクト（のリスト）取得メソッド ===== #
    def read_materials():
        #ファイルからテキストを読み込む
        f = open(BANK_PAHT, "r")
        data = f.read()
        f.close()
        #マテリアル毎に分割
        materials_data = data.split("\n")
        #最後のからの要素を削除
        materials_data.pop()
        materials = []
        for mtr_data in materials_data:
            mtr = mtr_data.split("/")
        
            #マテリアルのノードを文字列→リスト
            mtr[1] = mtr[1].replace("[", "")
            mtr[1] = mtr[1].replace("]", "")
            mtr[1] = mtr[1].replace("\'", "")
            mtr[1] = mtr[1].replace(" ", "")
            nodes = mtr[1].split(",")
            #リンクもリストに入れる
            mtr[2] = mtr[2].replace("[", "")
            mtr[2] = mtr[2].replace("]", "")
            mtr[2] = mtr[2].replace("\'", "")
            mtr[2] = mtr[2].replace(" ", "")
            links = mtr[2].split(",")


            materials.append(Material(mtr[0], nodes, links))
        
        return materials