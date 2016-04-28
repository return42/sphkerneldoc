.. -*- coding: utf-8; mode: rst -*-

.. _API-input-register-handler:

======================
input_register_handler
======================

*man input_register_handler(9)*

*4.6.0-rc5*

register a new input handler


Synopsis
========

.. c:function:: int input_register_handler( struct input_handler * handler )

Arguments
=========

``handler``
    handler to be registered


Description
===========

This function registers a new input handler (interface) for input
devices in the system and attaches it to all input devices that are
compatible with the handler.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
