# TODO



import socket


import time
from time import sleep

""" socat -x tcp-l:52382,fork,reuseaddr /dev/ttyACM0,raw,echo=0 """
""" socat -x tcp-l:52382,fork,reuseaddr tcp:172.168.193.199:4001 """
""" socat -x tcp-l:52382,fork,reuseaddr /dev/ttyUSB0,b57600,raw,echo=0 """
""" socat -x tcp-l:52382,fork,reuseaddr /dev/ttyUSB4,b9600,raw,echo=0 """ # thermal

host = "172.171.209.110"
port = 52382


def send_binary_sequence(binary_sequence):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        client_socket.sendall(bytes.fromhex(binary_sequence))
        client_socket.close()
        print(f"{binary_sequence} успешно отправлена на {host}:{port}")
    except Exception as e:
        print(f"Ошибка при отправке: {e}")


# binary_sequence = "c0 89 01 00 0a 81 09 04 01 FF c0"
# binary_sequence = "81 01 04 07 03 FF"   #zoom
# binary_sequence = "81010424720008FF"   # change Monitoring Mode   into 25 fps
# binary_sequence = "81010424 60 00 01 FF"   # change Digital Output
# binary_sequence = "8101041903FF"   # camera reset


# binary_sequence = "81 01 04 38 03 FF"   # CAM_Focus Manual Focus
# binary_sequence = "81 01 04 06 03 FF"   # CAM_DZoom off
# binary_sequence = "81 01 04 16 03 FF"   # CAM_Continuous FocusPosReply  OFF
# binary_sequence = "81 01 04 14 00 00 FF"    # CAM_HLC p: HLC level (0: Off, 1: Low, 2: Mid, 3: High) // q: HLC mask level (0: Off, 1: Low, 2: Mid, 3: High)
# binary_sequence = "81 01 04 6A 00 00 00 00 FF"   # CAM_ZoomPos ReplyIntervalTimeSet



# binary_sequence = "81 01 04 01 02 FF"    # CAM_ICR 02 ON  03 OFF
# binary_sequence = "81 09 04 01 FF"       # CAM_ICRModeInq    "y0 50 02 FF"   // 02 on - 03 off

# binary_sequence = "81 01 04 07 37 ff"      #cont move 1 = 0-7
# binary_sequence = "81 01 04 47 04 00 00 00 ff"  # Z=1

# binary_sequence = "81 01 04 47 00 04 07 08 ff"  # Z=0


# binary_sequence = "05 01 00 73 01 03 87 06"

# binary_sequence = "81 01 04 07 37 FF"

# binary_sequence = "81 01 04 19 01 FF"   #  LENS INIT

# CAM_Defog
# binary_sequence = "81 01 04 37 02 03 FF"  #  CAM_Defog    /// p: Defog level (1: low, 2: mid, 3: high)

# binary_sequence = "81 01 04 37 03 00 FF" # CAM_Defog off

# binary_sequence = "05 01 00 03 12 10 03 3c 00 00 00 38 11 00 00 3c 00 00 00 33 8a 00 00 58 06"  # move

# binary_sequence= "05 01 00 7a 03 01 01 03 7c 06" # wiper on

# binary_sequence= "ff 01 01 00 00 00 02"   # near
# binary_sequence= "ff 01 00 00 00 00 01"   # focus stop
# binary_sequence= "ff 01 00 80 00 00 81"   # far
# binary_sequence = "FF 01 00 07 00 42 4A"   # autofocus on
# binary_sequence = "DC 01 07 00 41 49"      # autofocus off

# send_binary_sequence(binary_sequence)



def send_focus_near(delay):
    focus_near = "ff 01 01 00 00 00 02"
    focus_stop = "ff 01 00 00 00 00 01"
    send_binary_sequence(focus_near)
    sleep(delay)
    send_binary_sequence(focus_stop)

def send_focus_far(delay):
    focus_far = "ff 01 00 80 00 00 81"
    focus_stop = "ff 01 00 00 00 00 01"
    send_binary_sequence(focus_far)
    sleep(delay)
    send_binary_sequence(focus_stop)

# send_focus_near(5)

# send_focus_far(0.1)




def send_continuous_zoom_after_direct_zoom():
    cont_move_1 = "81 01 04 07 27 FF" # cont move +7
    cont_move_2 = "81 01 04 07 35 FF"  # cont move -5
    cont_move_3 = "81 01 04 07 35 FF"
    cont_move_4 = "81 01 04 07 37 FF"  # cont move -7
    sleep = 0.3
    # binary_sequence = "81 01 04 47 00 04 07 08 ff"  # Z=0
    visca_stop = "81 01 04 07 00 ff"
    send_binary_sequence(cont_move_1, host, port)
    time.sleep(sleep)
    # send_binary_sequence(visca_stop,host,port)
    # time.sleep(sleep)

    # while True:
        # send_binary_sequence(cont_move_2, host, port)
        # time.sleep(sleep)
        # # send_binary_sequence(visca_stop,host,port)
        # # time.sleep(sleep)
        # send_binary_sequence(cont_move_4, host, port)
        # time.sleep(sleep)
        # send_binary_sequence(visca_stop, host, port)
        # time.sleep(sleep)
        # send_binary_sequence(cont_move_1, host, port)
        # time.sleep(sleep)
        # send_binary_sequence(visca_stop, host, port)
        # time.sleep(sleep)

        # return send_continuous_zoom_after_direct_zoom()

# send_continuous_zoom_after_direct_zoom()



def while_send_binary(delay):
    dir_zoom_0 = "81 01 04 47 00 04 07 08 ff"  # Z=0
    cont_zoom_move_forward = "81 01 04 07 21 ff"  # cont move 1 = 0-7
    dir_zoom_1 = "81 01 04 47 04 00 00 00 ff"  # Z=1
    cont_zoom_move_back = "81 01 04 07 31 ff"  # cont move 1 = 0-7
    print(f"{delay} sec")

    while True:
        send_binary_sequence(dir_zoom_1, host, port)
        time.sleep(delay)

        send_binary_sequence(cont_zoom_move_back, host, port)
        time.sleep(delay)

        send_binary_sequence(dir_zoom_0, host, port)
        time.sleep(delay)

        send_binary_sequence(cont_zoom_move_forward, host, port)
        time.sleep(delay)

        send_binary_sequence(dir_zoom_0, host, port)
        time.sleep(delay)





# while_send_binary(0.1)



