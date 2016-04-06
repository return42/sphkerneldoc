
.. _hostside:

===============================
Host-Side Data Types and Macros
===============================

The host side API exposes several layers to drivers, some of which are more necessary than others. These support lifecycle models for host side drivers and devices, and support
passing buffers through usbcore to some HCD that performs the I/O for the device driver.


.. toctree::
    :maxdepth: 1

    API-struct-usb-host-endpoint
    API-struct-usb-interface
    API-struct-usb-interface-cache
    API-struct-usb-host-config
    API-struct-usb-device
    API-usb-hub-for-each-child
    API-usb-interface-claimed
    API-usb-make-path
    API-USB-DEVICE
    API-USB-DEVICE-VER
    API-USB-DEVICE-INTERFACE-CLASS
    API-USB-DEVICE-INTERFACE-PROTOCOL
    API-USB-DEVICE-INTERFACE-NUMBER
    API-USB-DEVICE-INFO
    API-USB-INTERFACE-INFO
    API-USB-DEVICE-AND-INTERFACE-INFO
    API-USB-VENDOR-AND-INTERFACE-INFO
    API-struct-usbdrv-wrap
    API-struct-usb-driver
    API-struct-usb-device-driver
    API-struct-usb-class-driver
    API-module-usb-driver
    API-struct-urb
    API-usb-fill-control-urb
    API-usb-fill-bulk-urb
    API-usb-fill-int-urb
    API-usb-urb-dir-in
    API-usb-urb-dir-out
    API-struct-usb-sg-request
