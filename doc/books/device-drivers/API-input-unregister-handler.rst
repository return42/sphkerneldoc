
.. _API-input-unregister-handler:

========================
input_unregister_handler
========================

*man input_unregister_handler(9)*

*4.6.0-rc1*

unregisters an input handler


Synopsis
========

.. c:function:: void input_unregister_handler( struct input_handler * handler )

Arguments
=========

``handler``
    handler to be unregistered


Description
===========

This function disconnects a handler from its input devices and removes it from lists of known handlers.
