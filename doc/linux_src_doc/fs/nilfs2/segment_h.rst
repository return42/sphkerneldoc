.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/segment.h

.. _`nilfs_recovery_info`:

struct nilfs_recovery_info
==========================

.. c:type:: struct nilfs_recovery_info

    Recovery information

.. _`nilfs_recovery_info.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_recovery_info {
        int ri_need_recovery;
        sector_t ri_super_root;
        __u64 ri_cno;
        sector_t ri_lsegs_start;
        sector_t ri_lsegs_end;
        u64 ri_lsegs_start_seq;
        struct list_head ri_used_segments;
        sector_t ri_pseg_start;
        u64 ri_seq;
        __u64 ri_segnum;
        __u64 ri_nextnum;
    }

.. _`nilfs_recovery_info.members`:

Members
-------

ri_need_recovery
    Recovery status

ri_super_root
    Block number of the last super root

ri_cno
    *undescribed*

ri_lsegs_start
    Region for roll-forwarding (start block number)

ri_lsegs_end
    Region for roll-forwarding (end block number)

ri_lsegs_start_seq
    *undescribed*

ri_used_segments
    List of segments to be mark active

ri_pseg_start
    Block number of the last partial segment

ri_seq
    Sequence number on the last partial segment

ri_segnum
    Segment number on the last partial segment

ri_nextnum
    Next segment number on the last partial segment

.. _`nilfs_cstage`:

struct nilfs_cstage
===================

.. c:type:: struct nilfs_cstage

    Context of collection stage

.. _`nilfs_cstage.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_cstage {
        int scnt;
        unsigned int flags;
        struct nilfs_inode_info *dirty_file_ptr;
        struct nilfs_inode_info *gc_inode_ptr;
    }

.. _`nilfs_cstage.members`:

Members
-------

scnt
    Stage count, must be accessed via wrappers:
    \ :c:func:`nilfs_sc_cstage_inc`\ , \ :c:func:`nilfs_sc_cstage_set`\ , \ :c:func:`nilfs_sc_cstage_get`\ 

flags
    State flags

dirty_file_ptr
    Pointer on dirty_files list, or inode of a target file

gc_inode_ptr
    Pointer on the list of gc-inodes

.. _`nilfs_sc_info`:

struct nilfs_sc_info
====================

.. c:type:: struct nilfs_sc_info

    Segment constructor information

.. _`nilfs_sc_info.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_sc_info {
        struct super_block *sc_super;
        struct nilfs_root *sc_root;
        unsigned long sc_nblk_inc;
        struct list_head sc_dirty_files;
        struct list_head sc_gc_inodes;
        struct list_head sc_iput_queue;
        struct work_struct sc_iput_work;
        __u64 *sc_freesegs;
        size_t sc_nfreesegs;
        struct nilfs_inode_info *sc_dsync_inode;
        loff_t sc_dsync_start;
        loff_t sc_dsync_end;
        struct list_head sc_segbufs;
        struct list_head sc_write_logs;
        unsigned long sc_segbuf_nblocks;
        struct nilfs_segment_buffer *sc_curseg;
        struct nilfs_cstage sc_stage;
        struct nilfs_segsum_pointer sc_finfo_ptr;
        struct nilfs_segsum_pointer sc_binfo_ptr;
        unsigned long sc_blk_cnt;
        unsigned long sc_datablk_cnt;
        unsigned long sc_nblk_this_inc;
        time_t sc_seg_ctime;
        __u64 sc_cno;
        unsigned long sc_flags;
        spinlock_t sc_state_lock;
        unsigned long sc_state;
        unsigned long sc_flush_request;
        wait_queue_head_t sc_wait_request;
        wait_queue_head_t sc_wait_daemon;
        wait_queue_head_t sc_wait_task;
        __u32 sc_seq_request;
        __u32 sc_seq_accepted;
        __u32 sc_seq_done;
        int sc_sync;
        unsigned long sc_interval;
        unsigned long sc_mjcp_freq;
        unsigned long sc_lseg_stime;
        unsigned long sc_watermark;
        struct timer_list sc_timer;
        struct task_struct *sc_task;
    }

.. _`nilfs_sc_info.members`:

Members
-------

sc_super
    Back pointer to super_block struct

sc_root
    root object of the current filesystem tree

sc_nblk_inc
    Block count of current generation

sc_dirty_files
    List of files to be written

sc_gc_inodes
    List of GC inodes having blocks to be written

sc_iput_queue
    list of inodes for which iput should be done

sc_iput_work
    work struct to defer iput call

sc_freesegs
    array of segment numbers to be freed

sc_nfreesegs
    number of segments on \ ``sc_freesegs``\ 

sc_dsync_inode
    inode whose data pages are written for a sync operation

sc_dsync_start
    start byte offset of data pages

sc_dsync_end
    end byte offset of data pages (inclusive)

sc_segbufs
    List of segment buffers

sc_write_logs
    List of segment buffers to hold logs under writing

sc_segbuf_nblocks
    Number of available blocks in segment buffers.

sc_curseg
    Current segment buffer

sc_stage
    Collection stage

sc_finfo_ptr
    pointer to the current finfo struct in the segment summary

sc_binfo_ptr
    pointer to the current binfo struct in the segment summary

sc_blk_cnt
    Block count of a file

sc_datablk_cnt
    Data block count of a file

sc_nblk_this_inc
    Number of blocks included in the current logical segment

sc_seg_ctime
    Creation time

sc_cno
    checkpoint number of current log

sc_flags
    Internal flags

sc_state_lock
    spinlock for sc_state and so on

sc_state
    Segctord state flags

sc_flush_request
    inode bitmap of metadata files to be flushed

sc_wait_request
    Client request queue

sc_wait_daemon
    Daemon wait queue

sc_wait_task
    Start/end wait queue to control segctord task

sc_seq_request
    Request counter

sc_seq_accepted
    *undescribed*

sc_seq_done
    Completion counter

sc_sync
    Request of explicit sync operation

sc_interval
    Timeout value of background construction

sc_mjcp_freq
    Frequency of creating checkpoints

sc_lseg_stime
    Start time of the latest logical segment

sc_watermark
    Watermark for the number of dirty buffers

sc_timer
    Timer for segctord

sc_task
    current thread of segctord

.. This file was automatic generated / don't edit.

