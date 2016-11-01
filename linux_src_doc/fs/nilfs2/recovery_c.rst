.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/recovery.c

.. _`nilfs_compute_checksum`:

nilfs_compute_checksum
======================

.. c:function:: int nilfs_compute_checksum(struct the_nilfs *nilfs, struct buffer_head *bhs, u32 *sum, unsigned long offset, u64 check_bytes, sector_t start, unsigned long nblock)

    compute checksum of blocks continuously

    :param struct the_nilfs \*nilfs:
        nilfs object

    :param struct buffer_head \*bhs:
        buffer head of start block

    :param u32 \*sum:
        place to store result

    :param unsigned long offset:
        offset bytes in the first block

    :param u64 check_bytes:
        number of bytes to be checked

    :param sector_t start:
        DBN of start block

    :param unsigned long nblock:
        number of blocks to be checked

.. _`nilfs_read_super_root_block`:

nilfs_read_super_root_block
===========================

.. c:function:: int nilfs_read_super_root_block(struct the_nilfs *nilfs, sector_t sr_block, struct buffer_head **pbh, int check)

    read super root block

    :param struct the_nilfs \*nilfs:
        nilfs object

    :param sector_t sr_block:
        disk block number of the super root block

    :param struct buffer_head \*\*pbh:
        address of a buffer_head pointer to return super root buffer

    :param int check:
        CRC check flag

.. _`nilfs_read_log_header`:

nilfs_read_log_header
=====================

.. c:function:: struct buffer_head *nilfs_read_log_header(struct the_nilfs *nilfs, sector_t start_blocknr, struct nilfs_segment_summary **sum)

    read summary header of the specified log

    :param struct the_nilfs \*nilfs:
        nilfs object

    :param sector_t start_blocknr:
        start block number of the log

    :param struct nilfs_segment_summary \*\*sum:
        pointer to return segment summary structure

.. _`nilfs_validate_log`:

nilfs_validate_log
==================

.. c:function:: int nilfs_validate_log(struct the_nilfs *nilfs, u64 seg_seq, struct buffer_head *bh_sum, struct nilfs_segment_summary *sum)

    verify consistency of log

    :param struct the_nilfs \*nilfs:
        nilfs object

    :param u64 seg_seq:
        sequence number of segment

    :param struct buffer_head \*bh_sum:
        buffer head of summary block

    :param struct nilfs_segment_summary \*sum:
        segment summary struct

.. _`nilfs_read_summary_info`:

nilfs_read_summary_info
=======================

.. c:function:: void *nilfs_read_summary_info(struct the_nilfs *nilfs, struct buffer_head **pbh, unsigned int *offset, unsigned int bytes)

    read an item on summary blocks of a log

    :param struct the_nilfs \*nilfs:
        nilfs object

    :param struct buffer_head \*\*pbh:
        the current buffer head on summary blocks [in, out]

    :param unsigned int \*offset:
        the current byte offset on summary blocks [in, out]

    :param unsigned int bytes:
        byte size of the item to be read

.. _`nilfs_skip_summary_info`:

nilfs_skip_summary_info
=======================

.. c:function:: void nilfs_skip_summary_info(struct the_nilfs *nilfs, struct buffer_head **pbh, unsigned int *offset, unsigned int bytes, unsigned long count)

    skip items on summary blocks of a log

    :param struct the_nilfs \*nilfs:
        nilfs object

    :param struct buffer_head \*\*pbh:
        the current buffer head on summary blocks [in, out]

    :param unsigned int \*offset:
        the current byte offset on summary blocks [in, out]

    :param unsigned int bytes:
        byte size of the item to be skipped

    :param unsigned long count:
        number of items to be skipped

.. _`nilfs_scan_dsync_log`:

nilfs_scan_dsync_log
====================

.. c:function:: int nilfs_scan_dsync_log(struct the_nilfs *nilfs, sector_t start_blocknr, struct nilfs_segment_summary *sum, struct list_head *head)

    get block information of a log written for data sync

    :param struct the_nilfs \*nilfs:
        nilfs object

    :param sector_t start_blocknr:
        start block number of the log

    :param struct nilfs_segment_summary \*sum:
        log summary information

    :param struct list_head \*head:
        list head to add nilfs_recovery_block struct

.. _`nilfs_do_roll_forward`:

nilfs_do_roll_forward
=====================

.. c:function:: int nilfs_do_roll_forward(struct the_nilfs *nilfs, struct super_block *sb, struct nilfs_root *root, struct nilfs_recovery_info *ri)

    salvage logical segments newer than the latest checkpoint

    :param struct the_nilfs \*nilfs:
        nilfs object

    :param struct super_block \*sb:
        super block instance

    :param struct nilfs_root \*root:
        *undescribed*

    :param struct nilfs_recovery_info \*ri:
        pointer to a nilfs_recovery_info

.. _`nilfs_salvage_orphan_logs`:

nilfs_salvage_orphan_logs
=========================

.. c:function:: int nilfs_salvage_orphan_logs(struct the_nilfs *nilfs, struct super_block *sb, struct nilfs_recovery_info *ri)

    salvage logs written after the latest checkpoint

    :param struct the_nilfs \*nilfs:
        nilfs object

    :param struct super_block \*sb:
        super block instance

    :param struct nilfs_recovery_info \*ri:
        pointer to a nilfs_recovery_info struct to store search results.

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

    :param struct the_nilfs \*nilfs:
        the_nilfs

    :param struct nilfs_recovery_info \*ri:
        pointer to a nilfs_recovery_info struct to store search results.

.. _`nilfs_search_super_root.description`:

Description
-----------

nilfs_search_super_root() looks for the latest super-root from a partial
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

