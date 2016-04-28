.. -*- coding: utf-8; mode: rst -*-

.. _API-input-inject-event:

==================
input_inject_event
==================

*man input_inject_event(9)*

*4.6.0-rc5*

send input event from input handler


Synopsis
========

.. c:function:: void input_inject_event( struct input_handle * handle, unsigned int type, unsigned int code, int value )

Arguments
=========

``handle``
    input handle to send event through

``type``
    type of the event

``code``
    event code

``value``
    value of the event


Description
===========

Similar to ``input_event`` but will ignore event if device is “grabbed”
and handle injecting event is not the one that owns the device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
