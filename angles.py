import Leap, math,sys

def angle(v1, v2):
    return math.acos(dotproduct([x*v1.length for x in v1.direction], [x*v2.length for x in v2.direction]) / (v1.length * v2.length))
def dotproduct(v1,v2):
    return v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2]


class AngleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_init(self, controller):
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
            for finger in hand.fingers:
                print("skreeeeeeeee")
                boo = str(angle(finger.bone(0),finger.bone(1)))
                print ("MPA: " + boo)
                print "reeee"

    

def main():
    # Create a sample listener and controller
    listener = AngleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()

    