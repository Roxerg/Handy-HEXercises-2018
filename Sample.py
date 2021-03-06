<<<<<<< HEAD
################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

=======
>>>>>>> 73b07a23e48b6a900a3f96c9e5c7f9ac91c31b8e
import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
import cv2
import time
import json
import math

def angle(v1,v2):
    top = (v1[0] * v2[0]) + (v1[1] * v2[1]) + (v1[2] * v2[2])
    bottom = math.sqrt((v1[0]*v1[0]) + (v1[1]*v1[1]) + (v1[2]*v1[2])) * math.sqrt((v2[0]*v2[0]) + (v2[1]*v2[1]) + (v2[2]*v2[2]))
    angle = math.acos(top/bottom)
    return angle

<<<<<<< HEAD
def main():
    controller = Leap.Controller()

    time.sleep(2)
    count = 0
    json_formatted_data_none = {}
    final_data = {}

    print("None")

    while controller.is_connected:
        frame = controller.frame()
        for hand in frame.hands:
            finger_dict = {}
=======
def dict_making(controller, count):
    json_formatted_data = {}
    while controller.is_connected:
        frame = controller.frame()
        finger_dict = {}
        if len(frame.hands) == 0 || hand.is_left:
            print("Put your hand")
            time.sleep(1)
            continue
        for hand in frame.hands:
>>>>>>> 73b07a23e48b6a900a3f96c9e5c7f9ac91c31b8e
            for finger in hand.fingers:
                if finger.type == 0:
                    continue
                angle12 = angle(finger.bone(1).direction, finger.bone(2).direction)
                angle23 = angle(finger.bone(2).direction, finger.bone(3).direction)
                angle3palm = angle(finger.bone(3).direction, hand.palm_normal)
                finger_dict[finger.type] = {"MPA": angle12, "PIA": angle23, "IPA": angle3palm}
<<<<<<< HEAD
            json_formatted_data_none[str(count)] = finger_dict
=======
        json_formatted_data[count] = finger_dict
>>>>>>> 73b07a23e48b6a900a3f96c9e5c7f9ac91c31b8e
        count = count + 1
        time.sleep(1)
        print(count)
        if count == 5:
            break
<<<<<<< HEAD

    final_data["none"] = json_formatted_data_none

    print("1")

    count = 0

    json_formatted_data_1 = {}

    while controller.is_connected:
        frame = controller.frame()
        for hand in frame.hands:
            finger_dict = {}
            for finger in hand.fingers:
                if finger.type == 0:
                    continue
                angle12 = angle(finger.bone(1).direction, finger.bone(2).direction)
                angle23 = angle(finger.bone(2).direction, finger.bone(3).direction)
                angle3palm = angle(finger.bone(3).direction, hand.palm_normal)
                finger_dict[finger.type] = {"MPA": angle12, "PIA": angle23, "IPA": angle3palm}
            json_formatted_data_1[str(count)] = finger_dict
        count = count + 1
        time.sleep(1)
        print(count)
        if count == 5:
            break

    final_data["1"] = json_formatted_data_1

    final_data = json.dumps(final_data)

    text_file = open("output_file.json", "r+")
    text_file.write(final_data)
    text_file.close()

=======
    return json_formatted_data

def main():
    controller = Leap.Controller()

    time.sleep(2)

    for i in range(0, 2):

        if i == 0:
            print "Training data collection"
        else:
            print "Testing data collection"

        final_data = {}

        print("Do None")
        count = 0
        json_formatted_data_none = {}
        json_formatted_data_none = dict_making(controller, count)
        final_data["none"] = json_formatted_data_none

        print("Do 1")
        time.sleep(1)
        count = 0
        json_formatted_data_1 = {}
        json_formatted_data_1 = dict_making(controller, count)
        final_data["1"] = json_formatted_data_1

        print("Do 2")
        time.sleep(1)
        count = 0
        json_formatted_data_2 = {}
        json_formatted_data_2 = dict_making(controller, count)
        final_data["2"] = json_formatted_data_2

        # Making json and writing to a json file
        final_data = json.dumps(final_data)
        if i == 0:
            file_name = "output_file.json"
        else:
            file_name = "output_file_test.json"
        text_file = open(file_name, "r+")
        text_file.write(final_data)
        text_file.close()

        time.sleep(1)
>>>>>>> 73b07a23e48b6a900a3f96c9e5c7f9ac91c31b8e

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
