
.. _API-device-find-child:

=================
device_find_child
=================

*man device_find_child(9)*

*4.6.0-rc1*

device iterator for locating a particular device.


Synopsis
========

.. c:function:: struct device ⋆ device_find_child( struct device * parent, void * data, int (*match) struct device *dev, void *data )

Arguments
=========

``parent``
    parent struct device

``data``
    Data to pass to match function

``match``
    Callback function to check device


Description
===========

This is similar to the ``device_for_each_child`` function above, but it returns a reference to a device that is 'found' for later use, as determined by the ``match`` callback.

The callback should return 0 if the device doesn't match and non-zero if it does. If the callback returns non-zero and a reference to the current device can be obtained, this
function will return to the caller and not iterate over any more devices.


NOTE
====

you will need to drop the reference with ``put_device`` after use.
