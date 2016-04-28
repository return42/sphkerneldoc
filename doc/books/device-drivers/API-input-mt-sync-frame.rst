.. -*- coding: utf-8; mode: rst -*-

.. _API-input-mt-sync-frame:

===================
input_mt_sync_frame
===================

*man input_mt_sync_frame(9)*

*4.6.0-rc5*

synchronize mt frame


Synopsis
========

.. c:function:: void input_mt_sync_frame( struct input_dev * dev )

Arguments
=========

``dev``
    input device with allocated MT slots


Description
===========

Close the frame and prepare the internal state for a new one. Depending
on the flags, marks unused slots as inactive and performs pointer
emulation.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
