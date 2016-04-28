.. -*- coding: utf-8; mode: rst -*-

.. _API-ich-pata-cable-detect:

=====================
ich_pata_cable_detect
=====================

*man ich_pata_cable_detect(9)*

*4.6.0-rc5*

Probe host controller cable detect info


Synopsis
========

.. c:function:: int ich_pata_cable_detect( struct ata_port * ap )

Arguments
=========

``ap``
    Port for which cable detect info is desired


Description
===========

Read 80c cable indicator from ATA PCI device's PCI config register. This
register is normally set by firmware (BIOS).


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
