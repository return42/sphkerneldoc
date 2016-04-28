.. -*- coding: utf-8; mode: rst -*-

.. _API-sata-std-hardreset:

==================
sata_std_hardreset
==================

*man sata_std_hardreset(9)*

*4.6.0-rc5*

COMRESET w/o waiting or classification


Synopsis
========

.. c:function:: int sata_std_hardreset( struct ata_link * link, unsigned int * class, unsigned long deadline )

Arguments
=========

``link``
    link to reset

``class``
    resulting class of attached device

``deadline``
    deadline jiffies for the operation


Description
===========

Standard SATA COMRESET w/o waiting or classification.


LOCKING
=======

Kernel thread context (may sleep)


RETURNS
=======

0 if link offline, -EAGAIN if link online, -errno on errors.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
