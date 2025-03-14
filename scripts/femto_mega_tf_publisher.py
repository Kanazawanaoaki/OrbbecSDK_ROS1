#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import tf
from geometry_msgs.msg import TransformStamped

def broadcast_tf():
    rospy.init_node('tf_broadcaster')

    broadcaster = tf.TransformBroadcaster()

    rate = rospy.Rate(10.0)

    while not rospy.is_shutdown():
        translation = (0.1768, 0.0086, 0.0039)
        rotation = (0.004946, -0.00796, -0.000587, 0.999956)

        broadcaster.sendTransform(
            translation,
            rotation,
            rospy.Time.now(),
            'femto_mega_link',
            'head_mount_link'
        )

        rate.sleep()

if __name__ == '__main__':
    try:
        broadcast_tf()
    except rospy.ROSInterruptException:
        pass
