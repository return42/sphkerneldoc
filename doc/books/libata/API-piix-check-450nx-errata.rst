
.. _API-piix-check-450nx-errata:

=======================
piix_check_450nx_errata
=======================

*man piix_check_450nx_errata(9)*

*4.6.0-rc1*

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

Check for the present of 450NX errata #19 and errata #25. If they are found return an error code so we can turn off DMA
