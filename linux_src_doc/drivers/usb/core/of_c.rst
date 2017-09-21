.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/core/of.c

.. _`usb_of_get_child_node`:

usb_of_get_child_node
=====================

.. c:function:: struct device_node *usb_of_get_child_node(struct device_node *parent, int portnum)

    Find the device node match port number

    :param struct device_node \*parent:
        the parent device node

    :param int portnum:
        the port number which device is connecting

.. _`usb_of_get_child_node.description`:

Description
-----------

Find the node from device tree according to its port number.

.. _`usb_of_get_child_node.return`:

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

