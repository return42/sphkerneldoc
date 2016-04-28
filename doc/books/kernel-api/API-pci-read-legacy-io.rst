.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-read-legacy-io:

==================
pci_read_legacy_io
==================

*man pci_read_legacy_io(9)*

*4.6.0-rc5*

read byte(s) from legacy I/O port space


Synopsis
========

.. c:function:: ssize_t pci_read_legacy_io( struct file * filp, struct kobject * kobj, struct bin_attribute * bin_attr, char * buf, loff_t off, size_t count )

Arguments
=========

``filp``
    open sysfs file

``kobj``
    kobject corresponding to file to read from

``bin_attr``
    struct bin_attribute for this file

``buf``
    buffer to store results

``off``
    offset into legacy I/O port space

``count``
    number of bytes to read


Description
===========

Reads 1, 2, or 4 bytes from legacy I/O port space using an arch specific
callback routine (pci_legacy_read).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
