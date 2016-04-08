
.. _API-sata-link-resume:

================
sata_link_resume
================

*man sata_link_resume(9)*

*4.6.0-rc1*

resume SATA link


Synopsis
========

.. c:function:: int sata_link_resume( struct ata_link * link, const unsigned long * params, unsigned long deadline )

Arguments
=========

``link``
    ATA link to resume SATA

``params``
    timing parameters { interval, duratinon, timeout } in msec

``deadline``
    deadline jiffies for the operation


Description
===========

Resume SATA phy ``link`` and debounce it.


LOCKING
=======

Kernel thread context (may sleep)


RETURNS
=======

0 on success, -errno on failure.
