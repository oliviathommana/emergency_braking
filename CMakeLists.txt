cmake_minimum_required(VERSION 3.5)
project(emergency_brake)

# Dependencies for custom messages
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Declare the message file
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/BrakingInput.msg"
)

ament_package()

