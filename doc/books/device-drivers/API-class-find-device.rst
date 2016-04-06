
.. _API-class-find-device:

=================
class_find_device
=================

*man class_find_device(9)*

*4.6.0-rc1*

device iterator for locating a particular device


Synopsis
========

.. c:function:: struct device ⋆ class_find_device( struct class * class, struct device * start, const void * data, int (*match) struct device *, const void * )

Arguments
=========

``class``
    the class we're iterating

``start``
    Device to begin with

``data``
    data for the match function

``match``
    function to check device


Description
===========

This is similar to the ``class_for_each_dev`` function above, but it returns a reference to a device that is 'found' for later use, as determined by the ``match`` callback.

The callback should return 0 if the device doesn't match and non-zero if it does. If the callback returns non-zero, this function will return to the caller and not iterate over any
more devices.

Note, you will need to drop the reference with ``put_device`` after use.

``match`` is allowed to do anything including calling back into class code. There's no locking restriction.
