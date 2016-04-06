
.. _API-input-register-handle:

=====================
input_register_handle
=====================

*man input_register_handle(9)*

*4.6.0-rc1*

register a new input handle


Synopsis
========

.. c:function:: int input_register_handle( struct input_handle * handle )

Arguments
=========

``handle``
    handle to register


Description
===========

This function puts a new input handle onto device's and handler's lists so that events can flow through it once it is opened using ``input_open_device``.

This function is supposed to be called from handler's ``connect`` method.
