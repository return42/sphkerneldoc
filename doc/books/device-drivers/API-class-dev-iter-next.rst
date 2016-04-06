
.. _API-class-dev-iter-next:

===================
class_dev_iter_next
===================

*man class_dev_iter_next(9)*

*4.6.0-rc1*

iterate to the next device


Synopsis
========

.. c:function:: struct device ⋆ class_dev_iter_next( struct class_dev_iter * iter )

Arguments
=========

``iter``
    class iterator to proceed


Description
===========

Proceed ``iter`` to the next device and return it. Returns NULL if iteration is complete.

The returned device is referenced and won't be released till iterator is proceed to the next device or exited. The caller is free to do whatever it wants to do with the device
including calling back into class code.
