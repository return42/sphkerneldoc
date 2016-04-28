.. -*- coding: utf-8; mode: rst -*-

.. _API-input-unregister-handler:

========================
input_unregister_handler
========================

*man input_unregister_handler(9)*

*4.6.0-rc5*

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

This function disconnects a handler from its input devices and removes
it from lists of known handlers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
