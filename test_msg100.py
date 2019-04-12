from meross_iot.api import MerossHttpClient
from logging import DEBUG
from meross_iot.supported_devices.power_plugs import set_debug_level
import getpass


if __name__=='__main__':
    set_debug_level(DEBUG)
    print("-----------------------------------------")
    print("Welcome to the MSG100 test script. Thank you for helping me in testing this device!")
    print("-----------------------------------------")

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

        command = input("Your command (O for opening, C for closing, Q for quitting): ")
        cmd = command.strip().lower()
        if cmd == 'o':
            print("Opening...")
            msg100.turn_on_channel(0)
        elif cmd == 'c':
            print("Closing")
            msg100.turn_on_channel(0)
        elif cmd == 'q':
            print("Quitting")
            exit(0)
        else:
            print("Invalid command provided.")
            cmd = None
