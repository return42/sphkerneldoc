
.. _API-struct-usb-class-driver:

=======================
struct usb_class_driver
=======================

*man struct usb_class_driver(9)*

*4.6.0-rc1*

identifies a USB driver that wants to use the USB major number


Synopsis
========

.. code-block:: c

    struct usb_class_driver {
      char * name;
      char *(* devnode) (struct device *dev, umode_t *mode);
      const struct file_operations * fops;
      int minor_base;
    };


Members
=======

name
    the usb class device name for this driver. Will show up in sysfs.

devnode
    Callback to provide a naming hint for a possible device node to create.

fops
    pointer to the struct file_operations of this driver.

minor_base
    the start of the minor range for this driver.


Description
===========

This structure is used for the ``usb_register_dev`` and ``usb_unregister_dev`` functions, to consolidate a number of the parameters used for them.
