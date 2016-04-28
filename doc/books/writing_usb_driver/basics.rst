.. -*- coding: utf-8; mode: rst -*-

.. _basics:

================
Linux USB Basics
================

If you are going to write a Linux USB driver, please become familiar
with the USB protocol specification. It can be found, along with many
other useful documents, at the USB home page (see Resources). An
excellent introduction to the Linux USB subsystem can be found at the
USB Working Devices List (see Resources). It explains how the Linux USB
subsystem is structured and introduces the reader to the concept of USB
urbs (USB Request Blocks), which are essential to USB drivers.

The first thing a Linux USB driver needs to do is register itself with
the Linux USB subsystem, giving it some information about which devices
the driver supports and which functions to call when a device supported
by the driver is inserted or removed from the system. All of this
information is passed to the USB subsystem in the usb_driver structure.
The skeleton driver declares a usb_driver as:


.. code-block:: c

    static struct usb_driver skel_driver = {
            .name        = "skeleton",
            .probe       = skel_probe,
            .disconnect  = skel_disconnect,
            .fops        = &skel_fops,
            .minor       = USB_SKEL_MINOR_BASE,
            .id_table    = skel_table,
    };

The variable name is a string that describes the driver. It is used in
informational messages printed to the system log. The probe and
disconnect function pointers are called when a device that matches the
information provided in the id_table variable is either seen or
removed.

The fops and minor variables are optional. Most USB drivers hook into
another kernel subsystem, such as the SCSI, network or TTY subsystem.
These types of drivers register themselves with the other kernel
subsystem, and any user-space interactions are provided through that
interface. But for drivers that do not have a matching kernel subsystem,
such as MP3 players or scanners, a method of interacting with user space
is needed. The USB subsystem provides a way to register a minor device
number and a set of file_operations function pointers that enable this
user-space interaction. The skeleton driver needs this kind of
interface, so it provides a minor starting number and a pointer to its
file_operations functions.

The USB driver is then registered with a call to usb_register, usually
in the driver's init function, as shown here:


.. code-block:: c

    static int __init usb_skel_init(void)
    {
            int result;

            /* register this driver with the USB subsystem */
            result = usb_register(&skel_driver);
            if (result < 0) {
                    err("usb_register failed for the "__FILE__ "driver."
                        "Error number %d", result);
                    return -1;
            }

            return 0;
    }
    module_init(usb_skel_init);

When the driver is unloaded from the system, it needs to deregister
itself with the USB subsystem. This is done with the usb_deregister
function:


.. code-block:: c

    static void __exit usb_skel_exit(void)
    {
            /* deregister this driver with the USB subsystem */
            usb_deregister(&skel_driver);
    }
    module_exit(usb_skel_exit);

To enable the linux-hotplug system to load the driver automatically when
the device is plugged in, you need to create a MODULE_DEVICE_TABLE.
The following code tells the hotplug scripts that this module supports a
single device with a specific vendor and product ID:


.. code-block:: c

    /* table of devices that work with this driver */
    static struct usb_device_id skel_table [] = {
            { USB_DEVICE(USB_SKEL_VENDOR_ID, USB_SKEL_PRODUCT_ID) },
            { }                      /* Terminating entry */
    };
    MODULE_DEVICE_TABLE (usb, skel_table);

There are other macros that can be used in describing a usb_device_id
for drivers that support a whole class of USB drivers. See usb.h for
more information on this.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
