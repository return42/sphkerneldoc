
.. _API-nand-lock:

=========
nand_lock
=========

*man nand_lock(9)*

*4.6.0-rc1*

[REPLACEABLE] locks all blocks present in the device


Synopsis
========

.. c:function:: int nand_lock( struct mtd_info * mtd, loff_t ofs, uint64_t len )

Arguments
=========

``mtd``
    mtd info

``ofs``
    offset to start unlock from

``len``
    length to unlock


Description
===========

This feature is not supported in many NAND parts. 'Micron' NAND parts do have this feature, but it allows only to lock all blocks, not for specified range for block. Implementing
'lock' feature by making use of 'unlock', for now.

Returns lock status.
