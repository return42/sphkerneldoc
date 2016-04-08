
.. _API-sata-link-hardreset:

===================
sata_link_hardreset
===================

*man sata_link_hardreset(9)*

*4.6.0-rc1*

reset link via SATA phy reset


Synopsis
========

.. c:function:: int sata_link_hardreset( struct ata_link * link, const unsigned long * timing, unsigned long deadline, bool * online, int (*check_ready) struct ata_link * )

Arguments
=========

``link``
    link to reset

``timing``
    timing parameters { interval, duratinon, timeout } in msec

``deadline``
    deadline jiffies for the operation

``online``
    optional out parameter indicating link onlineness

``check_ready``
    optional callback to check link readiness


Description
===========

SATA phy-reset ``link`` using DET bits of SControl register. After hardreset, link readiness is waited upon using ``ata_wait_ready`` if ``check_ready`` is specified. LLDs are
allowed to not specify ``check_ready`` and wait itself after this function returns. Device classification is LLD's responsibility.

⋆\ ``online`` is set to one iff reset succeeded and ``link`` is online after reset.


LOCKING
=======

Kernel thread context (may sleep)


RETURNS
=======

0 on success, -errno otherwise.
