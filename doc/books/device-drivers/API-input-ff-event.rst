.. -*- coding: utf-8; mode: rst -*-

.. _API-input-ff-event:

==============
input_ff_event
==============

*man input_ff_event(9)*

*4.6.0-rc5*

generic handler for force-feedback events


Synopsis
========

.. c:function:: int input_ff_event( struct input_dev * dev, unsigned int type, unsigned int code, int value )

Arguments
=========

``dev``
    input device to send the effect to

``type``
    event type (anything but EV_FF is ignored)

``code``
    event code

``value``
    event value


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
