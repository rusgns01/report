import gym				# (1)

env = gym.make("FrozenLake-v1", render_mode='human', is_slippery=False) # (2)
print(env.observation_space.n)		# (3)
print(env.action_space.n)
env.reset()				# (4)

n=30
env.render()				
for i in range(n):			# (5)
  action = env.action_space.sample() 	# (6)
  state, reward, done, truncated, info = env.step(action)  # (7)
  print(f"({action}, {state}, {reward})", end="->")
  env.render()				# (8)
  if done: break			# (9)

env.close()