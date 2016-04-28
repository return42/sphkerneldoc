.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-buffer-map:

==============
usb_buffer_map
==============

*man usb_buffer_map(9)*

*4.6.0-rc5*

create DMA mapping(s) for an urb


Synopsis
========

.. c:function:: struct urb * usb_buffer_map( struct urb * urb )

Arguments
=========

``urb``
    urb whose transfer_buffer/setup_packet will be mapped


Description
===========

URB_NO_TRANSFER_DMA_MAP is added to urb->transfer_flags if the
operation succeeds. If the device is connected to this system through a
non-DMA controller, this operation always succeeds.

This call would normally be used for an urb which is reused, perhaps as
the target of a large periodic transfer, with ``usb_buffer_dmasync``
calls to synchronize memory and dma state.

Reverse the effect of this call with ``usb_buffer_unmap``.


Return
======

Either ``NULL`` (indicating no buffer could be mapped), or ``urb``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
