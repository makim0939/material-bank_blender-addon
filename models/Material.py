class Material:
    def __init__(self, name, nodes, links):
        self.name = name
        #ノード名のリスト
        self.nodes = nodes
        #ノードの接続情報の辞書型オブジェクトのリスト
        self.links = links
        

    def create_mtr_text(self):
        text = ""
        #マテリアル名を記述
        text += str(self.name)
        text += "/"
        #追加するノード名のリストを記述
        text += str(self.nodes)
        text += "/"
        #リンク（辞書型)のリストを記述
        text += str(self.links)
        text += "\n" 

        return text


