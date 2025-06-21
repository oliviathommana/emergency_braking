#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from braking_interfaces.msg import BrakingInput
from std_msgs.msg import Bool, Float32

class EmergencyBrakeNode(Node):
    def __init__(self):
        super().__init__('emergency_brake_node')

        self.subscription = self.create_subscription(
            BrakingInput,
            '/braking_input',
            self.input_callback,
            10
        )

        # Publishers for braking and throttle control
        self.brake_pub = self.create_publisher(Bool, '/brake_command', 10)
        self.throttle_pub = self.create_publisher(Float32, '/throttle_command', 10)

        self.brake_threshold = 0.5  # m, can be tuned

    def input_callback(self, msg: BrakingInput):
        # Simple logic: If any object is closer than threshold, apply brakes
        min_distance = min(msg.distances) if msg.distances else float('inf')

        if min_distance < self.brake_threshold or (abs(msg.velocity_x) > 0 and min_distance < 1.0):
            self.get_logger().warn(f'Obstacle detected at {min_distance:.2f}m! Braking...')
            self.brake_pub.publish(Bool(data=True))
            self.throttle_pub.publish(Float32(data=0.0))
        else:
            self.get_logger().info('No danger detected. Releasing brake...')
            self.brake_pub.publish(Bool(data=False))
            self.throttle_pub.publish(Float32(data=1.0))  # Assume 1.0 is some nominal throttle

def main(args=None):
    rclpy.init(args=args)
    node = EmergencyBrakeNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

