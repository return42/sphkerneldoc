
.. _API-input-ff-destroy:

================
input_ff_destroy
================

*man input_ff_destroy(9)*

*4.6.0-rc1*

frees force feedback portion of input device


Synopsis
========

.. c:function:: void input_ff_destroy( struct input_dev * dev )

Arguments
=========

``dev``
    input device supporting force feedback


Description
===========

This function is only needed in error path as input core will automatically free force feedback structures when device is destroyed.
