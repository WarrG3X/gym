import gym
import click
import gym_dobot.envs as envs
from scipy.misc import imsave


@click.command()
@click.option('--env', default="FetchReach-v1", help='Which environment to run (Eg. - FetchReach)')
@click.option('--render',default=True,help='Whether to render the environment')
@click.option('--steps',default=100,help='Number of timesteps to run the environment each time')
def main(env,render,steps):
    env = gym.make(env)

    while True:
        observation = env.reset()
        for i in range(steps):
            if render:
                env.render()
                # img = env.capture()
                # imsave('test.png',img)
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)

if __name__=='__main__':
    main()