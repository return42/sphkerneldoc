.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-dev-xfermask:

================
ata_dev_xfermask
================

*man ata_dev_xfermask(9)*

*4.6.0-rc5*

Compute supported xfermask of the given device


Synopsis
========

.. c:function:: void ata_dev_xfermask( struct ata_device * dev )

Arguments
=========

``dev``
    Device to compute xfermask for


Description
===========

Compute supported xfermask of ``dev`` and store it in dev->*_mask. This
function is responsible for applying all known limits including host
controller limits, device blacklist, etc...


LOCKING
=======

None.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
