import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

class JointStateListener(Node):
    def __init__(self):
        super().__init__('joint_state_listener')
        # create_subscription is from class Node (rclpy.node) -->
        # create_subscription(
        #   <message type>,
        #   <topic to subscribe>,
        #   <call to custom function>,
        #   queue size (how many messages can be stored in the queue if they
        # arrive faster than they're being processed),
        # )
        self.subscription = self.create_subscription(
            JointState,
            '/joint_states',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        self.get_logger().info('Received joint states:')
        for name, position in zip(msg.name, msg.position):
            self.get_logger().info(f'Joint: {name}, Position: {position}')

def main(args=None):
    rclpy.init(args=args)
    joint_state_listener = JointStateListener()
    rclpy.spin(joint_state_listener)
    joint_state_listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()