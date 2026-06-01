"""
Presentation layer - user interface (ROS2 node)
"""
from .go2_driver_node import Go2DriverNode

if not self.simulation:
    self.webrtc_adapter = WebRTCAdapter(...)
else:
    self.webrtc_adapter = None

__all__ = ['Go2DriverNode'] 
