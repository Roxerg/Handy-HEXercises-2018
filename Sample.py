################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
import cv2
import time

def main():
    controller = Leap.Controller()

    time.sleep(2)

    while controller.is_connected:
        frame = controller.frame()
        hands = frame.hands
        pointables = frame.pointables
        fingers = frame.fingers
        tools = frame.tools
        print(fingers[0].bone(1).direction)
        time.sleep(2)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
