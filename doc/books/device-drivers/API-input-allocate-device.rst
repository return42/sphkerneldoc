
.. _API-input-allocate-device:

=====================
input_allocate_device
=====================

*man input_allocate_device(9)*

*4.6.0-rc1*

allocate memory for new input device


Synopsis
========

.. c:function:: struct input_dev ⋆ input_allocate_device( void )

Arguments
=========

``void``
    no arguments


Description
===========

Returns prepared struct input_dev or ``NULL``.


NOTE
====

Use ``input_free_device`` to free devices that have not been registered; ``input_unregister_device`` should be used for already registered devices.
