from dm_control import mjcf
from dm_control import viewer
from optimal_agents.envs.dm_control_env import dm_control_test_env
import numpy as np

pendulum = mjcf.load('sample2.xml')

env = dm_control_test_env(morphology, arena=arenas.GM_Terrain())

action_spec = env.action_spec()


def random_policy(time_step):
    del time_step  # Unused.
    return np.random.uniform(low=action_spec.minimum,
                             high=action_spec.maximum,
                             size=action_spec.shape)


viewer.launch(env, policy=random_policy)
