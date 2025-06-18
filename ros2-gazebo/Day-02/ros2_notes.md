# 🧠 ROS2 + Gazebo Day 2 - My Exploration Log
---

## 🌟 What I Did Today 

Today I got curious... I had no plan, no mission, just vibes 🌀  
I launched Gazebo to check what’s inside... and BOOM... I saw a small turtle robot moving around!

---

## 🐢 What Happened Exactly

- I installed TurtleBot3 packages (after some fixing)
- I ran a launch file (don’t remember exact command but it launched a robot in a Gazebo world)
- The robot looked super small at first, I zoomed in to confirm — YES, it was a turtlebot!! 🐢
- I used **W, A, S, D** keys to move it around manually
- It actually moved! It wasn't fake! I was controlling a robot in simulation!

---

## 🕹️ What I Think Was Going On

- Some **teleop node** (like keyboard control) was running in the background
- That node published commands to `/cmd_vel` topic (maybe)
- The robot subscribed to that and moved forward/backward/rotate

---

## 🧠 New Concepts I Realized (Even if I didn't know them fully yet)

- **Nodes** can be launched via terminal and can run in background
- One node can read keyboard input and send velocity messages
- Another node (the robot's brain) can receive that and move the robot
- This is real ROS2 magic happening — pub/sub in real robot control!!

---


Today was my "I did it" moment. No tutorials. No steps. Just explored like a mad robot scientist.  
And guess what? IT WORKED 🔥

