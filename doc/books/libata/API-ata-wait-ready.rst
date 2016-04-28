.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-wait-ready:

==============
ata_wait_ready
==============

*man ata_wait_ready(9)*

*4.6.0-rc5*

wait for link to become ready


Synopsis
========

.. c:function:: int ata_wait_ready( struct ata_link * link, unsigned long deadline, int (*check_ready) struct ata_link *link )

Arguments
=========

``link``
    link to be waited on

``deadline``
    deadline jiffies for the operation

``check_ready``
    callback to check link readiness


Description
===========

Wait for ``link`` to become ready. ``check_ready`` should return
positive number if ``link`` is ready, 0 if it isn't, -ENODEV if link
doesn't seem to be occupied, other errno for other error conditions.

Transient -ENODEV conditions are allowed for ATA_TMOUT_FF_WAIT.


LOCKING
=======

EH context.


RETURNS
=======

0 if ``linke`` is ready before ``deadline``; otherwise, -errno.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
