.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-hub-clear-tt-buffer:

=======================
usb_hub_clear_tt_buffer
=======================

*man usb_hub_clear_tt_buffer(9)*

*4.6.0-rc5*

clear control/bulk TT state in high speed hub


Synopsis
========

.. c:function:: int usb_hub_clear_tt_buffer( struct urb * urb )

Arguments
=========

``urb``
    an URB associated with the failed or incomplete split transaction


Description
===========

High speed HCDs use this to tell the hub driver that some split control
or bulk transaction failed in a way that requires clearing internal
state of a transaction translator. This is normally detected (and
reported) from interrupt context.

It may not be possible for that hub to handle additional full (or low)
speed transactions until that state is fully cleared out.


Return
======

0 if successful. A negative error code otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
