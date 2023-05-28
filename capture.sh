pkill libcamera-hello
libcamera-jpeg -n -t1 -o $(date +%Y-%m-%d_%H-%M-%S).jpg
mv *.jpg /home/konsta/raspicamera/captures/
./start.sh
