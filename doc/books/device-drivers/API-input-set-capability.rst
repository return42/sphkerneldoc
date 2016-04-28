.. -*- coding: utf-8; mode: rst -*-

.. _API-input-set-capability:

====================
input_set_capability
====================

*man input_set_capability(9)*

*4.6.0-rc5*

mark device as capable of a certain event


Synopsis
========

.. c:function:: void input_set_capability( struct input_dev * dev, unsigned int type, unsigned int code )

Arguments
=========

``dev``
    device that is capable of emitting or accepting event

``type``
    type of the event (EV_KEY, EV_REL, etc...)

``code``
    event code


Description
===========

In addition to setting up corresponding bit in appropriate capability
bitmap the function also adjusts dev->evbit.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
