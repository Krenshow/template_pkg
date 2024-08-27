import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class TemplatePkg(Node):

    def __init__(self):
        super().__init__('template_pkg')

        # publisher
        self.publisher_ = self.create_publisher(String, 'topic_pub', 10)
        
        # subscriber
        self.subscription = self.create_subscription(String, 'topic_sub', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

    # publisher
    def process_data(self, data):
        msg = String()
        msg.data = data + '.' # processing data
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        
    # subscriber
    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        self.process_data(msg.data)


def main(args=None):
    rclpy.init(args=args)

    tp = TemplatePkg()

    rclpy.spin(tp)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    tp.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
