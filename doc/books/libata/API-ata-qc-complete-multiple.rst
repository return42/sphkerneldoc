
.. _API-ata-qc-complete-multiple:

========================
ata_qc_complete_multiple
========================

*man ata_qc_complete_multiple(9)*

*4.6.0-rc1*

Complete multiple qcs successfully


Synopsis
========

.. c:function:: int ata_qc_complete_multiple( struct ata_port * ap, u32 qc_active )

Arguments
=========

``ap``
    port in question

``qc_active``
    new qc_active mask


Description
===========

Complete in-flight commands. This functions is meant to be called from low-level driver's interrupt routine to complete requests normally. ap->qc_active and ``qc_active`` is
compared and commands are completed accordingly.

Always use this function when completing multiple NCQ commands from IRQ handlers instead of calling ``ata_qc_complete`` multiple times to keep IRQ expect status properly in sync.


LOCKING
=======

spin_lock_irqsave(host lock)


RETURNS
=======

Number of completed commands on success, -errno otherwise.
