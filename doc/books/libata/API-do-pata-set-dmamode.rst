
.. _API-do-pata-set-dmamode:

===================
do_pata_set_dmamode
===================

*man do_pata_set_dmamode(9)*

*4.6.0-rc1*

Initialize host controller PATA PIO timings


Synopsis
========

.. c:function:: void do_pata_set_dmamode( struct ata_port * ap, struct ata_device * adev, int isich )

Arguments
=========

``ap``
    Port whose timings we are configuring

``adev``
    Drive in question

``isich``
    set if the chip is an ICH device


Description
===========

Set UDMA mode for device, in host controller PCI config space.


LOCKING
=======

None (inherited from caller).
