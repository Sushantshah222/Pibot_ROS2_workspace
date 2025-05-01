import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ubuntu/Pibot_ROS2_workspace/src/install/pibot_py_examples'
