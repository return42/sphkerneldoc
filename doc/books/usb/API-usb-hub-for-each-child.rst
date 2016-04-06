
.. _API-usb-hub-for-each-child:

======================
usb_hub_for_each_child
======================

*man usb_hub_for_each_child(9)*

*4.6.0-rc1*

iterate over all child devices on the hub


Synopsis
========

.. c:function:: usb_hub_for_each_child( hdev, port1, child )

Arguments
=========

``hdev``
    USB device belonging to the usb hub

``port1``
    portnum associated with child device

``child``
    child device pointer
