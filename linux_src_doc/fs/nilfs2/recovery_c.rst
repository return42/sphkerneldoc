.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/recovery.c

.. _`nilfs_compute_checksum`:

nilfs_compute_checksum
======================

.. c:function:: int nilfs_compute_checksum(struct the_nilfs *nilfs, struct buffer_head *bhs, u32 *sum, unsigned long offset, u64 check_bytes, sector_t start, unsigned long nblock)

    compute checksum of blocks continuously

    :param nilfs:
        nilfs object
    :type nilfs: struct the_nilfs \*

    :param bhs:
        buffer head of start block
    :type bhs: struct buffer_head \*

    :param sum:
        place to store result
    :type sum: u32 \*

    :param offset:
        offset bytes in the first block
    :type offset: unsigned long

    :param check_bytes:
        number of bytes to be checked
    :type check_bytes: u64

    :param start:
        DBN of start block
    :type start: sector_t

    :param nblock:
        number of blocks to be checked
    :type nblock: unsigned long

.. _`nilfs_read_super_root_block`:

nilfs_read_super_root_block
===========================

.. c:function:: int nilfs_read_super_root_block(struct the_nilfs *nilfs, sector_t sr_block, struct buffer_head **pbh, int check)

    read super root block

    :param nilfs:
        nilfs object
    :type nilfs: struct the_nilfs \*

    :param sr_block:
        disk block number of the super root block
    :type sr_block: sector_t

    :param pbh:
        address of a buffer_head pointer to return super root buffer
    :type pbh: struct buffer_head \*\*

    :param check:
        CRC check flag
    :type check: int

.. _`nilfs_read_log_header`:

nilfs_read_log_header
=====================

.. c:function:: struct buffer_head *nilfs_read_log_header(struct the_nilfs *nilfs, sector_t start_blocknr, struct nilfs_segment_summary **sum)

    read summary header of the specified log

    :param nilfs:
        nilfs object
    :type nilfs: struct the_nilfs \*

    :param start_blocknr:
        start block number of the log
    :type start_blocknr: sector_t

    :param sum:
        pointer to return segment summary structure
    :type sum: struct nilfs_segment_summary \*\*

.. _`nilfs_validate_log`:

nilfs_validate_log
==================

.. c:function:: int nilfs_validate_log(struct the_nilfs *nilfs, u64 seg_seq, struct buffer_head *bh_sum, struct nilfs_segment_summary *sum)

    verify consistency of log

    :param nilfs:
        nilfs object
    :type nilfs: struct the_nilfs \*

    :param seg_seq:
        sequence number of segment
    :type seg_seq: u64

    :param bh_sum:
        buffer head of summary block
    :type bh_sum: struct buffer_head \*

    :param sum:
        segment summary struct
    :type sum: struct nilfs_segment_summary \*

.. _`nilfs_read_summary_info`:

nilfs_read_summary_info
=======================

.. c:function:: void *nilfs_read_summary_info(struct the_nilfs *nilfs, struct buffer_head **pbh, unsigned int *offset, unsigned int bytes)

    read an item on summary blocks of a log

    :param nilfs:
        nilfs object
    :type nilfs: struct the_nilfs \*

    :param pbh:
        the current buffer head on summary blocks [in, out]
    :type pbh: struct buffer_head \*\*

    :param offset:
        the current byte offset on summary blocks [in, out]
    :type offset: unsigned int \*

    :param bytes:
        byte size of the item to be read
    :type bytes: unsigned int

.. _`nilfs_skip_summary_info`:

nilfs_skip_summary_info
=======================

.. c:function:: void nilfs_skip_summary_info(struct the_nilfs *nilfs, struct buffer_head **pbh, unsigned int *offset, unsigned int bytes, unsigned long count)

    skip items on summary blocks of a log

    :param nilfs:
        nilfs object
    :type nilfs: struct the_nilfs \*

    :param pbh:
        the current buffer head on summary blocks [in, out]
    :type pbh: struct buffer_head \*\*

    :param offset:
        the current byte offset on summary blocks [in, out]
    :type offset: unsigned int \*

    :param bytes:
        byte size of the item to be skipped
    :type bytes: unsigned int

    :param count:
        number of items to be skipped
    :type count: unsigned long

.. _`nilfs_scan_dsync_log`:

nilfs_scan_dsync_log
====================

.. c:function:: int nilfs_scan_dsync_log(struct the_nilfs *nilfs, sector_t start_blocknr, struct nilfs_segment_summary *sum, struct list_head *head)

    get block information of a log written for data sync

    :param nilfs:
        nilfs object
    :type nilfs: struct the_nilfs \*

    :param start_blocknr:
        start block number of the log
    :type start_blocknr: sector_t

    :param sum:
        log summary information
    :type sum: struct nilfs_segment_summary \*

    :param head:
        list head to add nilfs_recovery_block struct
    :type head: struct list_head \*

.. _`nilfs_do_roll_forward`:

nilfs_do_roll_forward
=====================

.. c:function:: int nilfs_do_roll_forward(struct the_nilfs *nilfs, struct super_block *sb, struct nilfs_root *root, struct nilfs_recovery_info *ri)

    salvage logical segments newer than the latest checkpoint

    :param nilfs:
        nilfs object
    :type nilfs: struct the_nilfs \*

    :param sb:
        super block instance
    :type sb: struct super_block \*

    :param root:
        *undescribed*
    :type root: struct nilfs_root \*

    :param ri:
        pointer to a nilfs_recovery_info
    :type ri: struct nilfs_recovery_info \*

.. _`nilfs_salvage_orphan_logs`:

nilfs_salvage_orphan_logs
=========================

.. c:function:: int nilfs_salvage_orphan_logs(struct the_nilfs *nilfs, struct super_block *sb, struct nilfs_recovery_info *ri)

    salvage logs written after the latest checkpoint

    :param nilfs:
        nilfs object
    :type nilfs: struct the_nilfs \*

    :param sb:
        super block instance
    :type sb: struct super_block \*

    :param ri:
        pointer to a nilfs_recovery_info struct to store search results.
    :type ri: struct nilfs_recovery_info \*

.. _`nilfs_salvage_orphan_logs.return-value`:

Return Value
------------

On success, 0 is returned.  On error, one of the following
negative error code is returned.

\ ``-EINVAL``\  - Inconsistent filesystem state.

\ ``-EIO``\  - I/O error

\ ``-ENOSPC``\  - No space left on device (only in a panic state).

\ ``-ERESTARTSYS``\  - Interrupted.

\ ``-ENOMEM``\  - Insufficient memory available.

.. _`nilfs_search_super_root`:

nilfs_search_super_root
=======================

.. c:function:: int nilfs_search_super_root(struct the_nilfs *nilfs, struct nilfs_recovery_info *ri)

    search the latest valid super root

    :param nilfs:
        the_nilfs
    :type nilfs: struct the_nilfs \*

    :param ri:
        pointer to a nilfs_recovery_info struct to store search results.
    :type ri: struct nilfs_recovery_info \*

.. _`nilfs_search_super_root.description`:

Description
-----------

\ :c:func:`nilfs_search_super_root`\  looks for the latest super-root from a partial
segment pointed by the superblock.  It sets up struct the_nilfs through
this search. It fills nilfs_recovery_info (ri) required for recovery.

.. _`nilfs_search_super_root.return-value`:

Return Value
------------

On success, 0 is returned.  On error, one of the following
negative error code is returned.

\ ``-EINVAL``\  - No valid segment found

\ ``-EIO``\  - I/O error

\ ``-ENOMEM``\  - Insufficient memory available.

.. This file was automatic generated / don't edit.

