#!/bin/bash
for ((number=1;number < 1000;number++)){
    cat  /sys/bus/iio/devices/iio\:device0/in_voltage0_raw 1>> value.txt
}