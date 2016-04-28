.. -*- coding: utf-8; mode: rst -*-

.. _API-input-event:

===========
input_event
===========

*man input_event(9)*

*4.6.0-rc5*

report new input event


Synopsis
========

.. c:function:: void input_event( struct input_dev * dev, unsigned int type, unsigned int code, int value )

Arguments
=========

``dev``
    device that generated the event

``type``
    type of the event

``code``
    event code

``value``
    value of the event


Description
===========

This function should be used by drivers implementing various input
devices to report input events. See also ``input_inject_event``.


NOTE
====

``input_event`` may be safely used right after input device was
allocated with ``input_allocate_device``, even before it is registered
with ``input_register_device``, but the event will not reach any of the
input handlers. Such early invocation of ``input_event`` may be used to
'seed' initial state of a switch or initial position of absolute axis,
etc.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
