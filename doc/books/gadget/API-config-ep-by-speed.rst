.. -*- coding: utf-8; mode: rst -*-

.. _API-config-ep-by-speed:

==================
config_ep_by_speed
==================

*man config_ep_by_speed(9)*

*4.6.0-rc5*

configures the given endpoint according to gadget speed.


Synopsis
========

.. c:function:: int config_ep_by_speed( struct usb_gadget * g, struct usb_function * f, struct usb_ep * _ep )

Arguments
=========

``g``
    pointer to the gadget

``f``
    usb function

``_ep``
    the endpoint to configure


Return
======

error code, 0 on success

This function chooses the right descriptors for a given endpoint
according to gadget speed and saves it in the endpoint desc field. If
the endpoint already has a descriptor assigned to it - overwrites it
with currently corresponding descriptor. The endpoint maxpacket field is
updated according to the chosen descriptor.


Note
====

the supplied function should hold all the descriptors for supported
speeds


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
