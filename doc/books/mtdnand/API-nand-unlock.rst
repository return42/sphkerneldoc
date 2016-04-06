
.. _API-nand-unlock:

===========
nand_unlock
===========

*man nand_unlock(9)*

*4.6.0-rc1*

[REPLACEABLE] unlocks specified locked blocks


Synopsis
========

.. c:function:: int nand_unlock( struct mtd_info * mtd, loff_t ofs, uint64_t len )

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

Returns unlock status.
