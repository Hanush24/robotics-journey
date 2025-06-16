# File: talker.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HanushTalker(Node):
    def __init__(self):
        super().__init__('hanush_talker')
        self.publisher_ = self.create_publisher(String, 'hanush_talk', 10)
        timer_period = 1  # every 1 second
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f"Yo this is Hanush message #{self.i}"
        self.publisher_.publish(msg)
        self.get_logger().info(f"📤 Published: {msg.data}")
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    node = HanushTalker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
