from poke_env.player.player import Player
import numpy as np



class ModelPlayer(Player):

    '''
    Model is a trained tf/keras model. Implements the predict function.
    '''
    def __init__(self, model, env_player, player_configuration=None, server_configuration=None):
        super().__init__(player_configuration, server_configuration)
        self.model = model
        print(model.summary())
        self.env_player = env_player

    def choose_move(self, battle):
        embed_battle = self.env_player.embed_battle(battle)
        embed_battle = embed_battle.reshape(1,1,embed_battle.shape[0])
        vals = self.model.predict(embed_battle)
        action = np.argmax(vals)
        return self.env_player._action_to_move(action, battle)
