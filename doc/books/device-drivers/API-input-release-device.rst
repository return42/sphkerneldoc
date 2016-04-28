.. -*- coding: utf-8; mode: rst -*-

.. _API-input-release-device:

====================
input_release_device
====================

*man input_release_device(9)*

*4.6.0-rc5*

release previously grabbed device


Synopsis
========

.. c:function:: void input_release_device( struct input_handle * handle )

Arguments
=========

``handle``
    input handle that owns the device


Description
===========

Releases previously grabbed device so that other input handles can start
receiving input events. Upon release all handlers attached to the device
have their ``start`` method called so they have a change to synchronize
device state with the rest of the system.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
