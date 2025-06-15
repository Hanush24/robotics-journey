# 🤖 ROS2 Day 1 – Hanush's Jazzy Ride into Robotics

## 🧠 What I Learned Today

### ✅ ROS2 Environment Setup
- Ran the essential **setup command** before using ROS2 tools:
  ```bash
  source /opt/ros/jazzy/setup.bash  # (or setup.zsh if you're using ZSH)

    Learned that this command is mandatory for every new terminal.

    Felt like a robot chanting:

        "source... jazzy... bash... subscriber... nodes... echo..." 🤖💬

✅ Running Default ROS2 Nodes

    Executed the built-in talker/listener demo:

        Terminal 1:

ros2 run demo_nodes_cpp talker

Terminal 2:

        ros2 run demo_nodes_cpp listener

    Understood that these nodes communicate over the topic /chatter.

✅ Topic Exploration

    Listed all current topics:

ros2 topic list

Echoed a topic to see live data:

ros2 topic echo /chatter

Got info about a topic:

    ros2 topic info /chatter

💡 Realization: ROS2 doesn’t show /chatter unless talker is active.
Yeah, took a minute to digest that 😅
🛠️ Challenges Faced

    Hardest Part: Memorizing those prompts like:

        source /opt/ros/jazzy/setup.bash

        ros2 run demo_nodes_cpp talker

        ros2 topic echo /chatter

    Even for a second... I felt like I WAS THE ROBOT 😵‍💫
    Blabbering: "ros2... jazzy... source... subscriber... echo... bash..." 😂

🔥 My Progress Summary
Topic	Status
Environment Setup	✅ Done
Default Nodes (Talker/Listener)	✅ Done
Topic Commands	✅ Done
Understanding Pub-Sub	✅ Getting there
Mental Breakdown	😵 Happened
Recovery	💪 Bounced back
