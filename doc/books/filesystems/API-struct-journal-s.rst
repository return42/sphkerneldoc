.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-journal-s:

================
struct journal_s
================

*man struct journal_s(9)*

*4.6.0-rc5*

The journal_s type is the concrete type associated with journal_t.


Synopsis
========

.. code-block:: c

    struct journal_s {
      unsigned long j_flags;
      int j_errno;
      struct buffer_head * j_sb_buffer;
      journal_superblock_t * j_superblock;
      int j_format_version;
      rwlock_t j_state_lock;
      int j_barrier_count;
      struct mutex j_barrier;
      transaction_t * j_running_transaction;
      transaction_t * j_committing_transaction;
      transaction_t * j_checkpoint_transactions;
      wait_queue_head_t j_wait_transaction_locked;
      wait_queue_head_t j_wait_done_commit;
      wait_queue_head_t j_wait_commit;
      wait_queue_head_t j_wait_updates;
      wait_queue_head_t j_wait_reserved;
      struct mutex j_checkpoint_mutex;
      unsigned long j_head;
      unsigned long j_tail;
      unsigned long j_free;
      unsigned long j_first;
      unsigned long j_last;
      struct block_device * j_dev;
      int j_blocksize;
      unsigned long long j_blk_offset;
      struct block_device * j_fs_dev;
      unsigned int j_maxlen;
      atomic_t j_reserved_credits;
      spinlock_t j_list_lock;
      struct inode * j_inode;
      tid_t j_tail_sequence;
      tid_t j_transaction_sequence;
      tid_t j_commit_sequence;
      tid_t j_commit_request;
      __u8 j_uuid[16];
      struct task_struct * j_task;
      int j_max_transaction_buffers;
      unsigned long j_commit_interval;
      struct timer_list j_commit_timer;
      spinlock_t j_revoke_lock;
      struct jbd2_revoke_table_s * j_revoke;
      struct jbd2_revoke_table_s * j_revoke_table[2];
      struct buffer_head ** j_wbuf;
      int j_wbufsize;
      pid_t j_last_sync_writer;
      spinlock_t j_history_lock;
      struct proc_dir_entry * j_proc_entry;
      struct transaction_stats_s j_stats;
      void * j_private;
    };


Members
=======

j_flags
    General journaling state flags

j_errno
    Is there an outstanding uncleared error on the journal (from a prior
    abort)?

j_sb_buffer
    First part of superblock buffer

j_superblock
    Second part of superblock buffer

j_format_version
    Version of the superblock format

j_state_lock
    Protect the various scalars in the journal

j_barrier_count
    Number of processes waiting to create a barrier lock

j_barrier
    The barrier lock itself

j_running_transaction
    The current running transaction..

j_committing_transaction
    the transaction we are pushing to disk

j_checkpoint_transactions
    a linked circular list of all transactions waiting for checkpointing

j_wait_transaction_locked
    Wait queue for waiting for a locked transaction to start committing,
    or for a barrier lock to be released

j_wait_done_commit
    Wait queue for waiting for commit to complete

j_wait_commit
    Wait queue to trigger commit

j_wait_updates
    Wait queue to wait for updates to complete

j_wait_reserved
    Wait queue to wait for reserved buffer credits to drop

j_checkpoint_mutex
    Mutex for locking against concurrent checkpoints

j_head
    Journal head - identifies the first unused block in the journal

j_tail
    Journal tail - identifies the oldest still-used block in the
    journal.

j_free
    Journal free - how many free blocks are there in the journal?

j_first
    The block number of the first usable block

j_last
    The block number one beyond the last usable block

j_dev
    Device where we store the journal

j_blocksize
    blocksize for the location where we store the journal.

j_blk_offset
    starting block offset for into the device where we store the journal

j_fs_dev
    Device which holds the client fs. For internal journal this will be
    equal to j_dev

j_maxlen
    Total maximum capacity of the journal region on disk.

j_reserved_credits
    Number of buffers reserved from the running transaction

j_list_lock
    Protects the buffer lists and internal buffer state.

j_inode
    Optional inode where we store the journal. If present, all journal
    block numbers are mapped into this inode via ``bmap``.

j_tail_sequence
    Sequence number of the oldest transaction in the log

j_transaction_sequence
    Sequence number of the next transaction to grant

j_commit_sequence
    Sequence number of the most recently committed transaction

j_commit_request
    Sequence number of the most recent transaction wanting commit

j_uuid[16]
    Uuid of client object.

j_task
    Pointer to the current commit thread for this journal

j_max_transaction_buffers
    Maximum number of metadata buffers to allow in a single compound
    commit transaction

j_commit_interval
    What is the maximum transaction lifetime before we begin a commit?

j_commit_timer
    The timer used to wakeup the commit thread

j_revoke_lock
    Protect the revoke table

j_revoke
    The revoke table - maintains the list of revoked blocks in the
    current transaction.

j_revoke_table[2]
    alternate revoke tables for j_revoke

j_wbuf
    array of buffer_heads for jbd2_journal_commit_transaction

j_wbufsize
    maximum number of buffer_heads allowed in j_wbuf, the number that
    will fit in j_blocksize

j_last_sync_writer
    most recent pid which did a synchronous write

j_history_lock
    Protect the transactions statistics history

j_proc_entry
    procfs entry for the jbd statistics directory

j_stats
    Overall statistics

j_private
    An opaque pointer to fs-private information.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
