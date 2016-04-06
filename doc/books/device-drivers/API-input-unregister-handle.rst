
.. _API-input-unregister-handle:

=======================
input_unregister_handle
=======================

*man input_unregister_handle(9)*

*4.6.0-rc1*

unregister an input handle


Synopsis
========

.. c:function:: void input_unregister_handle( struct input_handle * handle )

Arguments
=========

``handle``
    handle to unregister


Description
===========

This function removes input handle from device's and handler's lists.

This function is supposed to be called from handler's ``disconnect`` method.
