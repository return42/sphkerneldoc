
.. _API-ata-wait-after-reset:

====================
ata_wait_after_reset
====================

*man ata_wait_after_reset(9)*

*4.6.0-rc1*

wait for link to become ready after reset


Synopsis
========

.. c:function:: int ata_wait_after_reset( struct ata_link * link, unsigned long deadline, int (*check_ready) struct ata_link *link )

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

Wait for ``link`` to become ready after reset.


LOCKING
=======

EH context.


RETURNS
=======

0 if ``linke`` is ready before ``deadline``; otherwise, -errno.
