.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-std-prereset:

================
ata_std_prereset
================

*man ata_std_prereset(9)*

*4.6.0-rc5*

prepare for reset


Synopsis
========

.. c:function:: int ata_std_prereset( struct ata_link * link, unsigned long deadline )

Arguments
=========

``link``
    ATA link to be reset

``deadline``
    deadline jiffies for the operation


Description
===========

``link`` is about to be reset. Initialize it. Failure from prereset
makes libata abort whole reset sequence and give up that port, so
prereset should be best-effort. It does its best to prepare for reset
sequence but if things go wrong, it should just whine, not fail.


LOCKING
=======

Kernel thread context (may sleep)


RETURNS
=======

0 on success, -errno otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
