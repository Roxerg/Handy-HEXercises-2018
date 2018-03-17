import Leap, math,sys
from json import load, dump
from pprint import pprint
from time import sleep

def angle(v1,v2):
    top = (v1[0] * v2[0]) + (v1[1] * v2[1]) + (v1[2] * v2[2])
    bottom = math.sqrt((v1[0]*v1[0]) + (v1[1]*v1[1]) + (v1[2]*v1[2])) * math.sqrt((v2[0]*v2[0]) + (v2[1]*v2[1]) + (v2[2]*v2[2]))
    angle = math.acos(top/bottom)
    return angle


class AngleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_init(self, controller):
        self.index = sys.argv[1]
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

    def on_disconnect(self, controller):
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        frame = controller.frame()
        #print("boo")
        # Get hands
        for hand in frame.hands:

            handType = "Left hand" if hand.is_left else "Right hand"

            print "  %s, id %d, position: %s" % (
                handType, hand.id, hand.palm_position)

            # Get the hand's normal vector and direction
            # normal = hand.palm_normal

            # Get fingers
            with open("rawdata.json", "r") as infile:
                data = load(infile)
            for finger in hand.fingers:
                #do some json shit idk
                current = data[self.index]
                newBOI = {
                            "metacarpal":{
                                "direction" : tuple(finger.bone(0).direction),
                                "length" : finger.bone(0).length
                            },
                            "proximal":{
                                "direction" : tuple(finger.bone(1).direction),
                                "length" : finger.bone(1).length
                            },
                            "intermediate":{
                                "direction" : tuple(finger.bone(2).direction),
                                "length" : finger.bone(2).length
                            },
                            "distal":{
                                "direction" : tuple(finger.bone(3).direction),
                                "length" : finger.bone(3).length
                            }
                            }
                pprint(newBOI)
                current.append(newBOI)
                data[self.index] = current
            with open("rawdata.json") as outfile:
                dump(outfile, data)

    

def main():
    # Create a sample listener and controller
    controller = Leap.Controller()
    sleep(5)
<<<<<<< HEAD

<<<<<<< HEAD
    def angle(self, v1, v2):
        return math.acos(self._dotproduct(v1, v2) / (v1.length * v2.length))
=======
    #to keep shit spicy
    controller.set_policy(Leap.Controller.POLICY_BACKGROUND_FRAMES)
    controller.set_policy(Leap.Controller.POLICY_IMAGES)
    controller.set_policy(Leap.Controller.POLICY_OPTIMIZE_HMD)
    index = sys.argv[1]


    while controller.is_connected:
        frame = controller.frame()
        #print("boo")
        # Get hands
        for hand in frame.hands:
            handType = "Left hand" if hand.is_left else "Right hand"
>>>>>>> 565f8a8e6ccb2bcf9fd66070468e9125f62fb8ec

=======

    #to keep shit spicy
    controller.set_policy(Leap.Controller.POLICY_BACKGROUND_FRAMES)
    controller.set_policy(Leap.Controller.POLICY_IMAGES)
    controller.set_policy(Leap.Controller.POLICY_OPTIMIZE_HMD)
    index = sys.argv[1]


    while controller.is_connected:
        frame = controller.frame()
        #print("boo")
        # Get hands
        for hand in frame.hands:
            handType = "Left hand" if hand.is_left else "Right hand"

>>>>>>> 73b07a23e48b6a900a3f96c9e5c7f9ac91c31b8e
            print "  %s, id %d, position: %s" % (
                    handType, hand.id, hand.palm_position)

                # Get the hand's normal vector and direction
                # normal = hand.palm_normal

                # Get fingers
            with open("rawdata.json", "r") as infile:
                data = load(infile)

            print "Skrrt" 
                    #do some json shit idk
            current = data[index]
            newBOI = {
            "1":{"MPA":angle(hand.finger(1).bone(0).direction,hand.finger(1).bone(1).direction),
            "PIA":angle(hand.finger(1).bone(1).direction,hand.finger(1).bone(2).direction),
            "IPA":angle(hand.finger(1).bone(2).direction,hand.palm_normal)
        },
        "2":{"MPA":angle(hand.finger(2).bone(0).direction,hand.finger(2).bone(1).direction),
            "PIA":angle(hand.finger(2).bone(1).direction,hand.finger(2).bone(2).direction),
            "IPA":angle(hand.finger(2).bone(2).direction,hand.palm_normal)
        },
        "3":{"MPA":angle(hand.finger(3).bone(0).direction,hand.finger(3).bone(1).direction),
            "PIA":angle(hand.finger(3).bone(1).direction,hand.finger(3).bone(2).direction),
            "IPA":angle(hand.finger(3).bone(2).direction,hand.palm_normal)
        },
        "4":{"MPA":angle(hand.finger(4).bone(0).direction,hand.finger(4).bone(1).direction),
            "PIA":angle(hand.finger(4).bone(1).direction,hand.finger(4).bone(2).direction),
            "IPA":angle(hand.finger(4).bone(2).direction,hand.palm_normal)
        }
    }
            pprint(newBOI)
            current.append(newBOI)
            data[index] = current
            with open("rawdata.json", "w") as outfile:
                dump(data, outfile)

    # Have the sample listener receive events from the controller
    #controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        pass


if __name__ == "__main__":
    main()