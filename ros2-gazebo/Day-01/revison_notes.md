⚙️ ROS2 Day 1 – Relearned, Reinforced, and Felt Like a Cyborg LOL 🤖

Yo future Hanush!
Today was wild, bro. I actually re-did everything I learned yesterday because I totally forgot all those source /opt/ros/jazzy/whatever.bla.bla.bash commands 💀.
But damn, this time I went harder — learned deeper and even fixed a few mistakes. Let’s go through it in full Hanush-vibe 🧢:
🚀 ROS Setup (a.k.a. wearing my superhero suit 🦸)

First thing first — anytime I open terminal, I gotta wear my ROS2 power suit:

source /opt/ros/jazzy/setup.zsh

If I don’t wear this suit, nothing ROS-related will work.
Lesson learned: ALWAYS DO THIS FIRST like brushing teeth before you talk to humans 😤🪥

📢 Running ROS2's Talker & Listener

Broooo these are like two robots — one keeps talking like Rabbit (💙) and the other one just listens like me.

Terminal 1:

ros2 run demo_nodes_cpp talker

Terminal 2:

ros2 run demo_nodes_cpp listener

Now these two just keep blabbering through /chatter — which is their hangout spot (topic lol).
🛰️ Exploring Topics

Ran these to spy on what's going on behind the scenes:

ros2 topic list
ros2 topic echo /chatter
ros2 topic info /chatter

🔥 Echo command was like a WhatsApp voice message monitor.
🔥 Info command told me what data format was being sent.
🔥 Felt like I became the robot bro — started saying random words like “ros2”, “topic”, “cpp”, “echo”, “chatterrrrrrrrrr” 😭💀

⚠️ Mistakes I Made Today (And How I Fixed Them)

Mistake 1: I tried ros2 run my_robot_talks talker and it shouted at me:

Package 'my_robot_talks' not found

Fix: I forgot to build the workspace!

So I did this:

sudo apt install python3-colcon-common-extensions
cd ~/ros2_ws
colcon build
source install/setup.zsh

Boom 💥 custom pub/sub started working!



.........................................................................

✅ What I Actually Achieved Today

    Re-ran official talker & listener

    Explored /chatter topic

    Understood source commands properly

    Understood colcon usage

    Fixed custom publisher/subscriber errors

    Felt like a ROS-powered chatbot for a minute 🤣

    Documented everything the Hanush way
