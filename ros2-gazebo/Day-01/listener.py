# File: listener.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HanushListener(Node):
    def __init__(self):
        super().__init__('hanush_listener')
        self.subscription = self.create_subscription(
            String,
            'hanush_talk',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        self.get_logger().info(f"👂 Heard: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = HanushListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
