import pickle
import sys
sys.path.append('../')
import optimal_agents
from dm_control import viewer
from optimal_agents.morphology import arenas
from optimal_agents.envs.dm_control_env import dm_control_test_env



with open("best_morphology.pkl","rb") as file_handle:
    morphology = pickle.load(file_handle)
    env = dm_control_test_env(morphology, arena=arenas.GM_Terrain())
    def random_policy(time_step):
        del time_step  # Unused.
        return np.random.uniform(low=action_spec.minimum,
                                high=action_spec.maximum,
                                size=action_spec.shape)

    viewer.launch(env, policy=random_policy)
    # print(retrieved_data)