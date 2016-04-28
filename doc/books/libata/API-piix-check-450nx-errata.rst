.. -*- coding: utf-8; mode: rst -*-

.. _API-piix-check-450nx-errata:

=======================
piix_check_450nx_errata
=======================

*man piix_check_450nx_errata(9)*

*4.6.0-rc5*

Check for problem 450NX setup


Synopsis
========

.. c:function:: int piix_check_450nx_errata( struct pci_dev * ata_dev )

Arguments
=========

``ata_dev``
    the PCI device to check


Description
===========

Check for the present of 450NX errata #19 and errata #25. If they are
found return an error code so we can turn off DMA


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
