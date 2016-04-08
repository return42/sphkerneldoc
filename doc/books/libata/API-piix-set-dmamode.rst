
.. _API-piix-set-dmamode:

================
piix_set_dmamode
================

*man piix_set_dmamode(9)*

*4.6.0-rc1*

Initialize host controller PATA DMA timings


Synopsis
========

.. c:function:: void piix_set_dmamode( struct ata_port * ap, struct ata_device * adev )

Arguments
=========

``ap``
    Port whose timings we are configuring

``adev``
    um


Description
===========

Set MW/UDMA mode for device, in host controller PCI config space.


LOCKING
=======

None (inherited from caller).
