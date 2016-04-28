.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-create-legacy-files:

=======================
pci_create_legacy_files
=======================

*man pci_create_legacy_files(9)*

*4.6.0-rc5*

create legacy I/O port and memory files


Synopsis
========

.. c:function:: void pci_create_legacy_files( struct pci_bus * b )

Arguments
=========

``b``
    bus to create files under


Description
===========

Some platforms allow access to legacy I/O port and ISA memory space on a
per-bus basis. This routine creates the files and ties them into their
associated read, write and mmap files from pci-sysfs.c

On error unwind, but don't propagate the error to the caller as it is ok
to set up the PCI bus without these files.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
