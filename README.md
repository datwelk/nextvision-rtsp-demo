# How to run
- Modify the rtsp livestream url in `test.py` on line 26
- Build docker image: 
`$ docker build . -f Dockerfile -t liveop/nextvision-test`
- Run the docker image: 
`$ docker run liveop/nextvision-test`

If any red output appears, OpenCV failed to read from the RTSP stream. Potential debugging options include switching OpenCV backend from the default FFMPEG to for example `gstreamer`. Possibly, the `Dockerfile` can be adjusted to install the correct versions of FFMPEG and/or `gstreamer`. The preferred OpenCV backend can be chosen by suppling the `apiPreference` argument to the `VideoCapture` constructor, e.g. `cv2.VideoCapture(.., apiPreference=cv2.CAP_V4L)` for using Video4Linux. For Gstreamer, use `cv.CAP_GSTREAMER`. Full list here: https://docs.opencv.org/3.4.14/d4/d15/group__videoio__flags__base.html#ga023786be1ee68a9105bf2e48c700294d. 

To find out which backends are supported, run the following inside the docker image:
```
python3
import cv2
print cv2.getBuildInformation()
```