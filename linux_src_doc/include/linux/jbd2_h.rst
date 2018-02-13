.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/jbd2.h

.. _`handle_t`:

typedef handle_t
================

.. c:type:: typedef handle_t

    The handle_t type represents a single atomic update being performed by some process.

.. _`handle_t.description`:

Description
-----------

All filesystem modifications made by the process go
through this handle.  Recursive operations (such as quota operations)
are gathered into a single update.

The buffer credits field is used to account for journaled buffers
being modified by the running process.  To ensure that there is
enough log space for all outstanding operations, we need to limit the
number of outstanding buffers possible at any time.  When the
operation completes, any buffer credits not used are credited back to
the transaction, so that at all times we know how many buffers the
outstanding updates on a transaction might possibly touch.

This is an opaque datatype.

.. _`journal_t`:

typedef journal_t
=================

.. c:type:: typedef journal_t

    The journal_t maintains all of the journaling state information for a single filesystem.

.. _`journal_t.description`:

Description
-----------

journal_t is linked to from the fs superblock structure.

We use the journal_t to keep track of all outstanding transaction
activity on the filesystem, and to manage the state of the log
writing process.

This is an opaque datatype.

.. _`jbd2_inode`:

struct jbd2_inode
=================

.. c:type:: struct jbd2_inode

    The jbd_inode type is the structure linking inodes in ordered mode present in a transaction so that we can sync them during commit.

.. _`jbd2_inode.definition`:

Definition
----------

.. code-block:: c

    struct jbd2_inode {
        transaction_t *i_transaction;
        transaction_t *i_next_transaction;
        struct list_head i_list;
        struct inode *i_vfs_inode;
        unsigned long i_flags;
    }

.. _`jbd2_inode.members`:

Members
-------

i_transaction

    Which transaction does this inode belong to? Either the running
    transaction or the committing one. [j_list_lock]

i_next_transaction

    Pointer to the running transaction modifying inode's data in case
    there is already a committing transaction touching it. [j_list_lock]

i_list
    List of inodes in the i_transaction [j_list_lock]

i_vfs_inode

    VFS inode this inode belongs to [constant for lifetime of structure]

i_flags
    Flags of inode [j_list_lock]

.. _`journal_s`:

struct journal_s
================

.. c:type:: struct journal_s

    The journal_s type is the concrete type associated with journal_t.

.. _`journal_s.definition`:

Definition
----------

.. code-block:: c

    struct journal_s {
        unsigned long j_flags;
        int j_errno;
        struct buffer_head *j_sb_buffer;
        journal_superblock_t *j_superblock;
        int j_format_version;
        rwlock_t j_state_lock;
        int j_barrier_count;
        struct mutex j_barrier;
        transaction_t *j_running_transaction;
        transaction_t *j_committing_transaction;
        transaction_t *j_checkpoint_transactions;
        wait_queue_head_t j_wait_transaction_locked;
        wait_queue_head_t j_wait_done_commit;
        wait_queue_head_t j_wait_commit;
        wait_queue_head_t j_wait_updates;
        wait_queue_head_t j_wait_reserved;
        struct mutex j_checkpoint_mutex;
        struct buffer_head *j_chkpt_bhs[JBD2_NR_BATCH];
        unsigned long j_head;
        unsigned long j_tail;
        unsigned long j_free;
        unsigned long j_first;
        unsigned long j_last;
        struct block_device *j_dev;
        int j_blocksize;
        unsigned long long j_blk_offset;
        char j_devname[BDEVNAME_SIZE+24];
        struct block_device *j_fs_dev;
        unsigned int j_maxlen;
        atomic_t j_reserved_credits;
        spinlock_t j_list_lock;
        struct inode *j_inode;
        tid_t j_tail_sequence;
        tid_t j_transaction_sequence;
        tid_t j_commit_sequence;
        tid_t j_commit_request;
        __u8 j_uuid[16];
        struct task_struct *j_task;
        int j_max_transaction_buffers;
        unsigned long j_commit_interval;
        struct timer_list j_commit_timer;
        spinlock_t j_revoke_lock;
        struct jbd2_revoke_table_s *j_revoke;
        struct jbd2_revoke_table_s *j_revoke_table[2];
        struct buffer_head **j_wbuf;
        int j_wbufsize;
        pid_t j_last_sync_writer;
        u64 j_average_commit_time;
        u32 j_min_batch_time;
        u32 j_max_batch_time;
        void (*j_commit_callback)(journal_t *, transaction_t *);
        spinlock_t j_history_lock;
        struct proc_dir_entry *j_proc_entry;
        struct transaction_stats_s j_stats;
        unsigned int j_failed_commit;
        void *j_private;
        struct crypto_shash *j_chksum_driver;
        __u32 j_csum_seed;
    #ifdef CONFIG_DEBUG_LOCK_ALLOC
        struct lockdep_map j_trans_commit_map;
    #endif
    }

.. _`journal_s.members`:

Members
-------

j_flags
    General journaling state flags [j_state_lock]

j_errno

    Is there an outstanding uncleared error on the journal (from a prior
    abort)? [j_state_lock]

j_sb_buffer
    The first part of the superblock buffer.

j_superblock
    The second part of the superblock buffer.

j_format_version
    Version of the superblock format.

j_state_lock
    Protect the various scalars in the journal.

j_barrier_count

    Number of processes waiting to create a barrier lock [j_state_lock]

j_barrier
    The barrier lock itself.

j_running_transaction

    Transactions: The current running transaction...
    [j_state_lock] [caller holding open handle]

j_committing_transaction

    the transaction we are pushing to disk
    [j_state_lock] [caller holding open handle]

j_checkpoint_transactions

    ... and a linked circular list of all transactions waiting for
    checkpointing. [j_list_lock]

j_wait_transaction_locked

    Wait queue for waiting for a locked transaction to start committing,
    or for a barrier lock to be released.

j_wait_done_commit
    Wait queue for waiting for commit to complete.

j_wait_commit
    Wait queue to trigger commit.

j_wait_updates
    Wait queue to wait for updates to complete.

j_wait_reserved

    Wait queue to wait for reserved buffer credits to drop.

j_checkpoint_mutex

    Semaphore for locking against concurrent checkpoints.

j_chkpt_bhs

    List of buffer heads used by the checkpoint routine.  This
    was moved from \ :c:func:`jbd2_log_do_checkpoint`\  to reduce stack
    usage.  Access to this array is controlled by the
    \ ``j_checkpoint_mutex``\ .  [j_checkpoint_mutex]

j_head

    Journal head: identifies the first unused block in the journal.
    [j_state_lock]

j_tail

    Journal tail: identifies the oldest still-used block in the journal.
    [j_state_lock]

j_free

    Journal free: how many free blocks are there in the journal?
    [j_state_lock]

j_first

    The block number of the first usable block in the journal
    [j_state_lock].

j_last

    The block number one beyond the last usable block in the journal
    [j_state_lock].

j_dev
    Device where we store the journal.

j_blocksize
    Block size for the location where we store the journal.

j_blk_offset

    Starting block offset into the device where we store the journal.

j_devname
    Journal device name.

j_fs_dev

    Device which holds the client fs.  For internal journal this will be
    equal to j_dev.

j_maxlen
    Total maximum capacity of the journal region on disk.

j_reserved_credits

    Number of buffers reserved from the running transaction.

j_list_lock
    Protects the buffer lists and internal buffer state.

j_inode

    Optional inode where we store the journal.  If present, all
    journal block numbers are mapped into this inode via \ :c:func:`bmap`\ .

j_tail_sequence

    Sequence number of the oldest transaction in the log [j_state_lock]

j_transaction_sequence

    Sequence number of the next transaction to grant [j_state_lock]

j_commit_sequence

    Sequence number of the most recently committed transaction
    [j_state_lock].

j_commit_request

    Sequence number of the most recent transaction wanting commit
    [j_state_lock]

j_uuid

    Journal uuid: identifies the object (filesystem, LVM volume etc)
    backed by this journal.  This will eventually be replaced by an array
    of uuids, allowing us to index multiple devices within a single
    journal and to perform atomic updates across them.

j_task
    Pointer to the current commit thread for this journal.

j_max_transaction_buffers

    Maximum number of metadata buffers to allow in a single compound
    commit transaction.

j_commit_interval

    What is the maximum transaction lifetime before we begin a commit?

j_commit_timer
    The timer used to wakeup the commit thread.

j_revoke_lock
    Protect the revoke table.

j_revoke

    The revoke table - maintains the list of revoked blocks in the
    current transaction.

j_revoke_table
    Alternate revoke tables for j_revoke.

j_wbuf
    Array of bhs for jbd2_journal_commit_transaction.

j_wbufsize

    Size of \ ``j_wbuf``\  array.

j_last_sync_writer

    The pid of the last person to run a synchronous operation
    through the journal.

j_average_commit_time

    The average amount of time in nanoseconds it takes to commit a
    transaction to disk. [j_state_lock]

j_min_batch_time

    Minimum time that we should wait for additional filesystem operations
    to get batched into a synchronous handle in microseconds.

j_max_batch_time

    Maximum time that we should wait for additional filesystem operations
    to get batched into a synchronous handle in microseconds.

j_commit_callback

    This function is called when a transaction is closed.

j_history_lock
    Protect the transactions statistics history.

j_proc_entry
    procfs entry for the jbd statistics directory.

j_stats
    Overall statistics.

j_failed_commit
    Failed journal commit ID.

j_private

    An opaque pointer to fs-private information.  ext3 puts its
    superblock pointer here.

j_chksum_driver

    Reference to checksum algorithm driver via cryptoapi.

j_csum_seed

    Precomputed journal UUID checksum for seeding other checksums.

j_trans_commit_map

    Lockdep entity to track transaction commit dependencies. Handles
    hold this "lock" for read, when we wait for commit, we acquire the
    "lock" for writing. This matches the properties of jbd2 journalling
    where the running transaction has to wait for all handles to be
    dropped to commit that transaction and also acquiring a handle may
    require transaction commit to finish.

.. This file was automatic generated / don't edit.

