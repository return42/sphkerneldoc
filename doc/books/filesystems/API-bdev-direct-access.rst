
.. _API-bdev-direct-access:

==================
bdev_direct_access
==================

*man bdev_direct_access(9)*

*4.6.0-rc1*

Get the address for directly-accessibly memory


Synopsis
========

.. c:function:: long bdev_direct_access( struct block_device * bdev, struct blk_dax_ctl * dax )

Arguments
=========

``bdev``
    The device containing the memory

``dax``
    control and output parameters for ->direct_access


Description
===========

If a block device is made up of directly addressable memory, this function will tell the caller the PFN and the address of the memory. The address may be directly dereferenced
within the kernel without the need to call ``ioremap``, ``kmap`` or similar. The PFN is suitable for inserting into page tables.


Return
======

negative errno if an error occurs, otherwise the number of bytes accessible at this address.
