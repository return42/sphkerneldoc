.. -*- coding: utf-8; mode: rst -*-

====
of.c
====


.. _`usb_of_get_child_node`:

usb_of_get_child_node
=====================

.. c:function:: struct device_node *usb_of_get_child_node (struct device_node *parent, int portnum)

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

On success, a pointer to the device node, ``NULL`` on failure.

