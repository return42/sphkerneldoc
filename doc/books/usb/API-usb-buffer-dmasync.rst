.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-buffer-dmasync:

==================
usb_buffer_dmasync
==================

*man usb_buffer_dmasync(9)*

*4.6.0-rc5*

synchronize DMA and CPU view of buffer(s)


Synopsis
========

.. c:function:: void usb_buffer_dmasync( struct urb * urb )

Arguments
=========

``urb``
    urb whose transfer_buffer/setup_packet will be synchronized


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
