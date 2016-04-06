
.. _API-struct-usb-device-driver:

========================
struct usb_device_driver
========================

*man struct usb_device_driver(9)*

*4.6.0-rc1*

identifies USB device driver to usbcore


Synopsis
========

.. code-block:: c

    struct usb_device_driver {
      const char * name;
      int (* probe) (struct usb_device *udev);
      void (* disconnect) (struct usb_device *udev);
      int (* suspend) (struct usb_device *udev, pm_message_t message);
      int (* resume) (struct usb_device *udev, pm_message_t message);
      struct usbdrv_wrap drvwrap;
      unsigned int supports_autosuspend:1;
    };


Members
=======

name
    The driver name should be unique among USB drivers, and should normally be the same as the module name.

probe
    Called to see if the driver is willing to manage a particular device. If it is, probe returns zero and uses ``dev_set_drvdata`` to associate driver-specific data with the
    device. If unwilling to manage the device, return a negative errno value.

disconnect
    Called when the device is no longer accessible, usually because it has been (or is being) disconnected or the driver's module is being unloaded.

suspend
    Called when the device is going to be suspended by the system.

resume
    Called when the device is being resumed by the system.

drvwrap
    Driver-model core structure wrapper.

supports_autosuspend
    if set to 0, the USB core will not allow autosuspend for devices bound to this driver.


Description
===========

USB drivers must provide all the fields listed above except drvwrap.
