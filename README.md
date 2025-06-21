# Emergency Braking Node (ROS 2)

A ROS 2 package that implements an **emergency braking system** for autonomous or assisted vehicles. The node subscribes to sensor inputs and calculates braking commands in real-time.

## 📦 Package Name
`emergency_brake`

---

## 🚀 Features

- Real-time emergency braking logic
- Subscribes to sensor input and vehicle dynamics data
- Publishes braking commands to an actuator system
- ROS 2 compliant (tested on Humble)

---

## 📂 Directory Structure

⚙️ Working of the Node
The Emergency Braking Node is designed to monitor the environment and vehicle dynamics in real-time to determine if emergency braking is necessary.

Here’s how it works:

Input Subscription (/braking_input):

The node subscribes to a topic that carries sensor data and vehicle dynamics.

Typical fields in the input message might include:

distance_x, distance_y → Relative positions of obstacles

velocity_x, velocity_y → Current speed of the vehicle

objects → Detected objects (e.g., 'car', 'pedestrian')

distances → Distance to obstacles

rpm_fl, rpm_fr, rpm_rl, rpm_rr → Wheel RPMs

Decision Logic:

The node uses the input data to calculate whether an obstacle is dangerously close.

If the detected object is within a critical distance threshold and the vehicle is moving toward it → the node decides to brake.

Basic example logic (conceptual):

python
Copy
Edit
if min(distances) < safe_distance_threshold:
    brake = True
else:
    brake = False
Output Publishing (/brake_command):

The node publishes a braking command (usually True or False, or a structured message) to the /brake_command topic.

This output can then be used by an actuator controller or simulation to actually stop the vehicle.

Real-Time Operation:

The process of receiving data, processing it, and publishing braking decisions happens continuously while the node is active.

