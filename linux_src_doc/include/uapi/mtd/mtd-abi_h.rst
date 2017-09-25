.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/mtd/mtd-abi.h

.. _`mtd_write_req`:

struct mtd_write_req
====================

.. c:type:: struct mtd_write_req

    data structure for requesting a write operation

.. _`mtd_write_req.definition`:

Definition
----------

.. code-block:: c

    struct mtd_write_req {
        __u64 start;
        __u64 len;
        __u64 ooblen;
        __u64 usr_data;
        __u64 usr_oob;
        __u8 mode;
        __u8 padding[7];
    }

.. _`mtd_write_req.members`:

Members
-------

start
    start address

len
    length of data buffer

ooblen
    length of OOB buffer

usr_data
    user-provided data buffer

usr_oob
    user-provided OOB buffer

mode
    MTD mode (see "MTD operation modes")

padding
    reserved, must be set to 0

.. _`mtd_write_req.description`:

Description
-----------

This structure supports ioctl(MEMWRITE) operations, allowing data and/or OOB
writes in various modes. To write to OOB-only, set \ ``usr_data``\  == NULL, and to
write data-only, set \ ``usr_oob``\  == NULL. However, setting both \ ``usr_data``\  and
\ ``usr_oob``\  to NULL is not allowed.

.. _`mtd_ecc_stats`:

struct mtd_ecc_stats
====================

.. c:type:: struct mtd_ecc_stats

    error correction stats

.. _`mtd_ecc_stats.definition`:

Definition
----------

.. code-block:: c

    struct mtd_ecc_stats {
        __u32 corrected;
        __u32 failed;
        __u32 badblocks;
        __u32 bbtblocks;
    }

.. _`mtd_ecc_stats.members`:

Members
-------

corrected
    number of corrected bits

failed
    number of uncorrectable errors

badblocks
    number of bad blocks in this partition

bbtblocks
    number of blocks reserved for bad block tables

.. This file was automatic generated / don't edit.

