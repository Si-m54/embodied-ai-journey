import gymnasium as gym
import gymnasium_robotics
import imageio

# FetchReach：机械臂末端走到目标点。最简单的机器人任务。
env = gym.make("FetchReach-v4", render_mode="rgb_array")
obs, info = env.reset(seed=42)

frames = []
for step in range(60):
    action = env.action_space.sample()   # 随机动作，先不用懂，能跑就行
    obs, reward, terminated, truncated, info = env.step(action)
    frames.append(env.render())
    if terminated or truncated:
        obs, info = env.reset()

env.close()
imageio.mimsave("week01/first_robot.gif", frames, fps=20)
print("done")