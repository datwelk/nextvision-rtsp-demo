import cv2
import time
from termcolor import colored

def start(url):
    cap = cv2.VideoCapture(url)
    count = 0

    while True:
        if not cap.isOpened():
            print(colored('Failed to open stream. Retry in 5 seconds...', 'red'))
            time.sleep(5)
            start(url)
            return
        
        try:
            (status, frame) = cap.read()
            
            if frame is None:
                print(colored("Failed to read frame..", 'red'))
            else:
                print(colored("Got frame!", 'green'))
                count += 1

            if count == 30:
                return
        except Exception as e:
            print(colored("Failed to read frame with exception: " + e, 'red'))

if __name__ == '__main__':
    stream_url = '<STREAM URL HERE>'
    working_non_next_vision_stream_url = 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov'
    start(stream_url)