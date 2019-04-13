from meross_iot.api import MerossHttpClient
from logging import DEBUG, ERROR, FileHandler
from os import path
from meross_iot.supported_devices.power_plugs import set_debug_level, l, h
import getpass


LOGFILE = path.abspath('./msg100.log')

h.setLevel(ERROR)
f = FileHandler(LOGFILE)
f.setLevel(DEBUG)
l.addHandler(f)


if __name__=='__main__':
    set_debug_level(DEBUG)

    print("-----------------------------------------")
    print("Welcome to the MSG100 test script. Thank you for helping me in testing this device!")
    print("-----------------------------------------")
    print("All low-level lows will be saved to %s" % LOGFILE)
    print("Please enter your meross cloud email and password. That would allow me to perform some tests.")
    EMAIL = input("Your meross EMAIL: ")
    PASSWORD = getpass.getpass("Your meross PASSWORD: ")

    print("Connecting to HTTP-API...")
    api = MerossHttpClient(EMAIL, PASSWORD)
    devices = api.list_supported_devices()

    print("Looking for the meross MSG100")
    msg100 = None
    for d in devices:
        if d._type == 'msg100':
            msg100 = d

    if msg100 is None:
        print("I was unable to find the MSG100 device... is that connected and registered?")
        exit(1)

    print("Found MSG100 named %s" % msg100._name)
    print("Let's see whats the Garage status right now...")

    print("-------------------------")
    print("Now it's your turn. Try to play with the garage and report if it's working or not.")

    cmd = None
    while cmd != 'q':
        str_state = "OPEN" if msg100.get_garage_door_open_state() == 1 else "CLOSED"
        print("Reported garage state is: %s. Go check if that is true!" % str_state)
        print("Commands:")
        print("OPEN with TOGGLEX: O")
        print("CLOSE with TOGGLEX: C")
        print("OPEN with GARAGE_DOOR_STATE with UUID+CHANNEL: O1")
        print("CLOSE with GARAGE_DOOR_STATE with UUID+CHANNEL: C1")
        print("OPEN with GARAGE_DOOR_STATE with UUID: O2")
        print("CLOSE with GARAGE_DOOR_STATE with UUID: C2")
        print("QUIT: Q")
        command = input("Your command: ")
        cmd = command.strip().lower()
        if cmd == 'o':
            print("O: Opening...")
            msg100.turn_on_channel(channel=0)
        elif cmd == 'c':
            print("C: Closing...")
            msg100.turn_off_channel(channel=0)
        elif cmd == 'o1':
            print("O1: Opening...")
            msg100.test_operate_garage_door_1(status=1, channel=0)
        elif cmd == 'c1':
            print("C1: Closing...")
            msg100.test_operate_garage_door_1(status=0, channel=0)
        elif cmd == 'o2':
            print("O2: Opening...")
            msg100.test_operate_garage_door_2(status=1, channel=0)
        elif cmd == 'c2':
            print("C2: Closing...")
            msg100.test_operate_garage_door_2(status=0, channel=0)
        elif cmd == 'q':
            print("Quitting!")
            exit(0)
        else:
            print("Invalid command provided.")
            cmd = None
