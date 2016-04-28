.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-findImVolumes:

=================
mpt_findImVolumes
=================

*man mpt_findImVolumes(9)*

*4.6.0-rc5*

Identify IDs of hidden disks and RAID Volumes


Synopsis
========

.. c:function:: int mpt_findImVolumes( MPT_ADAPTER * ioc )

Arguments
=========

``ioc``
    Pointer to a Adapter Strucutre


Return
======

0 on success -EFAULT if read of config page header fails or data pointer
not NULL -ENOMEM if pci_alloc failed


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
