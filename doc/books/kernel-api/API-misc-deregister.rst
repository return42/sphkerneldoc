
.. _API-misc-deregister:

===============
misc_deregister
===============

*man misc_deregister(9)*

*4.6.0-rc1*

unregister a miscellaneous device


Synopsis
========

.. c:function:: void misc_deregister( struct miscdevice * misc )

Arguments
=========

``misc``
    device to unregister


Description
===========

Unregister a miscellaneous device that was previously successfully registered with ``misc_register``.
