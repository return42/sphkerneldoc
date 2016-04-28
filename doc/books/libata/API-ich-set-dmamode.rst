.. -*- coding: utf-8; mode: rst -*-

.. _API-ich-set-dmamode:

===============
ich_set_dmamode
===============

*man ich_set_dmamode(9)*

*4.6.0-rc5*

Initialize host controller PATA DMA timings


Synopsis
========

.. c:function:: void ich_set_dmamode( struct ata_port * ap, struct ata_device * adev )

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
