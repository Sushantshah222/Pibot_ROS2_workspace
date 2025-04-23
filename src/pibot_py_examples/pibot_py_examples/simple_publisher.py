import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class SimplePublisher(Node):
    def __init__(self):
        super().__init__('simple_publisher')
        self.publisher_ = self.create_publisher(String, 'chatter', 10)

        self.counter_ = 0 
        self.frequency_ = 1.0
        
        self.get_logger().info(f"SimplePublisher node has been started at {self.frequency_}Hz.")
        self.timer_ = self.create_timer(self.frequency_, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = f"Hello, world! {self.counter_}"
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing: '{msg.data}'")
        self.counter_ += 1


def main():
    rclpy.init()
    simple_publisher = SimplePublisher()

    try:
        rclpy.spin(simple_publisher)
    except KeyboardInterrupt:
        pass
    finally:
        simple_publisher.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()