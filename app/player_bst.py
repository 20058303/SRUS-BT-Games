from app.player_bnode import PlayerBNode
from app.player import Player


class PlayerBST:
    def __init__(self):
        self.RootNode = None

    def Insert(self, player):
        if self.RootNode is None:
            self.RootNode = PlayerBNode(player)
        else:
            currentNode = self.RootNode
            while True:
                if player.name < currentNode.player.name:
                    if currentNode.leftNode is not None:
                        currentNode = currentNode.leftNode
                    else:
                        currentNode.leftNode = PlayerBNode(player)
                        break
                elif player.name > currentNode.player.name:
                    if currentNode.rightNode is not None:
                        currentNode = currentNode.rightNode
                    else:
                        currentNode.rightNode = PlayerBNode(player)
                        break
                elif player.name == currentNode.player.name:
                    currentNode.player = player
                    break

    def Search(self, string):
        if self.RootNode is None:
            return False

        elif self.RootNode.player.name == string:
            return self.RootNode

        else:
            currentNode = self.RootNode
            while True:
                if currentNode.player.name == string:
                    return currentNode

                elif string < currentNode.player.name:
                    if currentNode.leftNode is not None:
                        currentNode = currentNode.leftNode
                    else:
                        return False

                elif string > currentNode.player.name:
                    if currentNode.rightNode is not None:
                        currentNode = currentNode.rightNode
                    else:
                        return False
