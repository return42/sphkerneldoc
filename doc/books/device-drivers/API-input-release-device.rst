
.. _API-input-release-device:

====================
input_release_device
====================

*man input_release_device(9)*

*4.6.0-rc1*

release previously grabbed device


Synopsis
========

.. c:function:: void input_release_device( struct input_handle * handle )

Arguments
=========

``handle``
    input handle that owns the device


Description
===========

Releases previously grabbed device so that other input handles can start receiving input events. Upon release all handlers attached to the device have their ``start`` method called
so they have a change to synchronize device state with the rest of the system.
