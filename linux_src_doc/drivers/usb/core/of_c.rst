.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/core/of.c

.. _`usb_of_get_device_node`:

usb_of_get_device_node
======================

.. c:function:: struct device_node *usb_of_get_device_node(struct usb_device *hub, int port1)

    get a USB device node

    :param struct usb_device \*hub:
        hub to which device is connected

    :param int port1:
        one-based index of port

.. _`usb_of_get_device_node.description`:

Description
-----------

Look up the node of a USB device given its parent hub device and one-based
port number.

.. _`usb_of_get_device_node.return`:

Return
------

A pointer to the node with incremented refcount if found, or
\ ``NULL``\  otherwise.

.. _`usb_of_has_combined_node`:

usb_of_has_combined_node
========================

.. c:function:: bool usb_of_has_combined_node(struct usb_device *udev)

    determine whether a device has a combined node

    :param struct usb_device \*udev:
        USB device

.. _`usb_of_has_combined_node.description`:

Description
-----------

Determine whether a USB device has a so called combined node which is
shared with its sole interface. This is the case if and only if the device

.. _`usb_of_has_combined_node.has-a-node-and-its-decriptors-report-the-following`:

has a node and its decriptors report the following
--------------------------------------------------


1) bDeviceClass is 0 or 9, and
2) bNumConfigurations is 1, and
3) bNumInterfaces is 1.

.. _`usb_of_has_combined_node.return`:

Return
------

True iff the device has a device node and its descriptors match the
criteria for a combined node.

.. _`usb_of_get_interface_node`:

usb_of_get_interface_node
=========================

.. c:function:: struct device_node *usb_of_get_interface_node(struct usb_device *udev, u8 config, u8 ifnum)

    get a USB interface node

    :param struct usb_device \*udev:
        USB device of interface

    :param u8 config:
        configuration value

    :param u8 ifnum:
        interface number

.. _`usb_of_get_interface_node.description`:

Description
-----------

Look up the node of a USB interface given its USB device, configuration
value and interface number.

.. _`usb_of_get_interface_node.return`:

Return
------

A pointer to the node with incremented refcount if found, or
\ ``NULL``\  otherwise.

.. _`usb_of_get_companion_dev`:

usb_of_get_companion_dev
========================

.. c:function:: struct device *usb_of_get_companion_dev(struct device *dev)

    Find the companion device

    :param struct device \*dev:
        the device pointer to find a companion

.. _`usb_of_get_companion_dev.description`:

Description
-----------

Find the companion device from platform bus.

Takes a reference to the returned struct device which needs to be dropped
after use.

.. _`usb_of_get_companion_dev.return`:

Return
------

On success, a pointer to the companion device, \ ``NULL``\  on failure.

.. This file was automatic generated / don't edit.

