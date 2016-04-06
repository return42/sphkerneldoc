
.. _API-mpt-findImVolumes:

=================
mpt_findImVolumes
=================

*man mpt_findImVolumes(9)*

*4.6.0-rc1*

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

0 on success -EFAULT if read of config page header fails or data pointer not NULL -ENOMEM if pci_alloc failed
