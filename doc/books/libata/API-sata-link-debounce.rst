.. -*- coding: utf-8; mode: rst -*-

.. _API-sata-link-debounce:

==================
sata_link_debounce
==================

*man sata_link_debounce(9)*

*4.6.0-rc5*

debounce SATA phy status


Synopsis
========

.. c:function:: int sata_link_debounce( struct ata_link * link, const unsigned long * params, unsigned long deadline )

Arguments
=========

``link``
    ATA link to debounce SATA phy status for

``params``
    timing parameters { interval, duratinon, timeout } in msec

``deadline``
    deadline jiffies for the operation


Description
===========

Make sure SStatus of ``link`` reaches stable state, determined by
holding the same value where DET is not 1 for ``duration`` polled every
``interval``, before ``timeout``. Timeout constraints the beginning of
the stable state. Because DET gets stuck at 1 on some controllers after
hot unplugging, this functions waits until timeout then returns 0 if DET
is stable at 1.

``timeout`` is further limited by ``deadline``. The sooner of the two is
used.


LOCKING
=======

Kernel thread context (may sleep)


RETURNS
=======

0 on success, -errno on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
