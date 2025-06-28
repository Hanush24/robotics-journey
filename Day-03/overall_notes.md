## 🚀 Goal:
- Master ROS2 Launch Files
- Learn to control services (SetPen)
- Automate node launching using Python-based launch files
- Use terminal like a robotics wizard to make a turtle draw a heart ❤️

---

## 📚 Topics Covered:
- ✅ ROS2 Launch Files (Python)
- ✅ How to launch multiple nodes together (Talker + Listener)
- ✅ Understanding `generate_launch_description()`
- ✅ Using `ros2 service call` with SetPen
- ✅ Drawing using keyboard (teleop)
- ✅ Creating custom Python script to draw a heart using teleport service

---

## 🤖 Commands I Practiced:
```bash
ros2 pkg create --build-type ament_python my_launch_pkg
mkdir -p launch
nano launch/my_robot_launch.py
ros2 launch my_launch_pkg my_robot_launch.py

ros2 service call /turtle1/set_pen turtlesim/srv/SetPen '{ "r": 255, "g": 0, "b": 0, "width": 5, "off": false }'
ros2 run turtlesim turtle_teleop_key

ros2 pkg create --build-type ament_python my_heart_bot --dependencies rclpy turtlesim
nano draw_heart.py  # placed inside my_heart_bot/my_heart_bot/
nano setup.py  # added entry point
colcon build
source install/setup.zsh
ros2 run my_heart_bot draw_heart
```

---

## ⚠️ Mistakes I Made (And Fixed):
- ❌ Forgot to include launch file in `setup.py` → ROS2 said "file not found"
  - ✅ Fixed by adding this to `setup.py`:
    ```python
    ('share/my_launch_pkg/launch', ['launch/my_robot_launch.py'])
    ```
- ❌ Used wrong quotes in service call → Got error: `attribute name must be string`
  - ✅ Fixed using:
    ```bash
    ros2 service call ... '{ "r": 255, ... }'
    ```
- ❌ Tried to run `ros2 run demo/nodes/cpp talker` (slash error)
  - ✅ Correct command: `ros2 run demo_nodes_cpp talker`
- ❌ My turtle didn’t draw → Forgot to set `off: false` in SetPen service
- ❌ Couldn't find `draw_heart.py` → Forgot it needs to be inside `my_heart_bot/my_heart_bot/`
- ❌ Entry point not working → Didn’t update `setup.py` properly

---

## 🎨 Fun Moments:
- Drew a heart with a turtle using teleport_absolute! 🐢💘
- Laughed when turtle started teleporting like Naruto after each coordinate.
- Felt like Iron Man after getting launch files to work — 1 command to start a robot army 😎

---

## 📦 Package Structure:
```
my_heart_bot/
├── setup.py
├── package.xml
└── my_heart_bot/
    ├── __init__.py
    └── draw_heart.py
```

---

## ❤️ Final Thoughts:
Today I felt like I was **talking to robots**, commanding turtles, and writing launch files like an automation wizard. ROS2 + services + Python made it fun, but debugging every step took time.

Mistakes? MANY. But fun? MAXIMUM 😄
