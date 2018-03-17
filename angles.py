import Leap, math,sys

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
        for hand in frame.hands:
            normal = hand.palm_normal
            for finger in hand.fingers:
                print(self.finger_names[finger.type] + " metacarpal-proximal angle: " + str(self._angle(finger.bone(0).direction,finger.bone(1).direction))+ " proximal-intermediate angle: " + str(self._angle(finger.bone(1).direction,finger.bone(2).direction)) + " intermediate-palm angle: "+  str(self._angle(finger.bone(2).direction,normal)) + "\n")

    def _dotproduct(self,v1,v2):
        return sum((a*b) for a,b in zip(v1,v2))

    def _length(self, v):
        return math.sqrt(self._dotproduct(v,v))

    def _angle(self, v1, v2):
        return math.acos(self._dotproduct(v1, v2) / (self._length(v1) * self._length(v2)))

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

    