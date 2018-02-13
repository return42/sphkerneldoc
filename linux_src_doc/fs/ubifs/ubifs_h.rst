.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/ubifs.h

.. _`ubifs_old_idx`:

struct ubifs_old_idx
====================

.. c:type:: struct ubifs_old_idx

    index node obsoleted since last commit start.

.. _`ubifs_old_idx.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_old_idx {
        struct rb_node rb;
        int lnum;
        int offs;
    }

.. _`ubifs_old_idx.members`:

Members
-------

rb
    rb-tree node

lnum
    LEB number of obsoleted index node

offs
    offset of obsoleted index node

.. _`ubifs_scan_node`:

struct ubifs_scan_node
======================

.. c:type:: struct ubifs_scan_node

    UBIFS scanned node information.

.. _`ubifs_scan_node.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_scan_node {
        struct list_head list;
        union ubifs_key key;
        unsigned long long sqnum;
        int type;
        int offs;
        int len;
        void *node;
    }

.. _`ubifs_scan_node.members`:

Members
-------

list
    list of scanned nodes

key
    key of node scanned (if it has one)

sqnum
    sequence number

type
    type of node scanned

offs
    offset with LEB of node scanned

len
    length of node scanned

node
    raw node

.. _`ubifs_scan_leb`:

struct ubifs_scan_leb
=====================

.. c:type:: struct ubifs_scan_leb

    UBIFS scanned LEB information.

.. _`ubifs_scan_leb.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_scan_leb {
        int lnum;
        int nodes_cnt;
        struct list_head nodes;
        int endpt;
        void *buf;
    }

.. _`ubifs_scan_leb.members`:

Members
-------

lnum
    logical eraseblock number

nodes_cnt
    number of nodes scanned

nodes
    list of struct ubifs_scan_node

endpt
    end point (and therefore the start of empty space)

buf
    buffer containing entire LEB scanned

.. _`ubifs_gced_idx_leb`:

struct ubifs_gced_idx_leb
=========================

.. c:type:: struct ubifs_gced_idx_leb

    garbage-collected indexing LEB.

.. _`ubifs_gced_idx_leb.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_gced_idx_leb {
        struct list_head list;
        int lnum;
        int unmap;
    }

.. _`ubifs_gced_idx_leb.members`:

Members
-------

list
    list

lnum
    LEB number

unmap
    OK to unmap this LEB

.. _`ubifs_gced_idx_leb.description`:

Description
-----------

This data structure is used to temporary store garbage-collected indexing
LEBs - they are not released immediately, but only after the next commit.
This is needed to guarantee recoverability.

.. _`ubifs_inode`:

struct ubifs_inode
==================

.. c:type:: struct ubifs_inode

    UBIFS in-memory inode description.

.. _`ubifs_inode.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_inode {
        struct inode vfs_inode;
        unsigned long long creat_sqnum;
        unsigned long long del_cmtno;
        unsigned int xattr_size;
        unsigned int xattr_cnt;
        unsigned int xattr_names;
        unsigned int dirty:1;
        unsigned int xattr:1;
        unsigned int bulk_read:1;
        unsigned int compr_type:2;
        struct mutex ui_mutex;
        spinlock_t ui_lock;
        loff_t synced_i_size;
        loff_t ui_size;
        int flags;
        pgoff_t last_page_read;
        pgoff_t read_in_a_row;
        int data_len;
        void *data;
    }

.. _`ubifs_inode.members`:

Members
-------

vfs_inode
    VFS inode description object

creat_sqnum
    sequence number at time of creation

del_cmtno
    commit number corresponding to the time the inode was deleted,
    protected by \ ``c``\ ->commit_sem;

xattr_size
    summarized size of all extended attributes in bytes

xattr_cnt
    count of extended attributes this inode has

xattr_names
    sum of lengths of all extended attribute names belonging to
    this inode

dirty
    non-zero if the inode is dirty

xattr
    non-zero if this is an extended attribute inode

bulk_read
    non-zero if bulk-read should be used

compr_type
    default compression type used for this inode

ui_mutex
    serializes inode write-back with the rest of VFS operations,
    serializes "clean <-> dirty" state changes, serializes bulk-read,
    protects \ ``dirty``\ , \ ``bulk_read``\ , \ ``ui_size``\ , and \ ``xattr_size``\ 

ui_lock
    protects \ ``synced_i_size``\ 

synced_i_size
    synchronized size of inode, i.e. the value of inode size
    currently stored on the flash; used only for regular file
    inodes

ui_size
    inode size used by UBIFS when writing to flash

flags
    inode flags (@UBIFS_COMPR_FL, etc)

last_page_read
    page number of last page read (for bulk read)

read_in_a_row
    number of consecutive pages read in a row (for bulk read)

data_len
    length of the data attached to the inode

data
    inode's data

.. _`ubifs_inode.description`:

Description
-----------

\ ``ui_mutex``\  exists for two main reasons. At first it prevents inodes from
being written back while UBIFS changing them, being in the middle of an VFS
operation. This way UBIFS makes sure the inode fields are consistent. For
example, in 'ubifs_rename()' we change 3 inodes simultaneously, and
write-back must not write any of them before we have finished.

The second reason is budgeting - UBIFS has to budget all operations. If an
operation is going to mark an inode dirty, it has to allocate budget for
this. It cannot just mark it dirty because there is no guarantee there will
be enough flash space to write the inode back later. This means UBIFS has
to have full control over inode "clean <-> dirty" transitions (and pages
actually). But unfortunately, VFS marks inodes dirty in many places, and it
does not ask the file-system if it is allowed to do so (there is a notifier,
but it is not enough), i.e., there is no mechanism to synchronize with this.
So UBIFS has its own inode dirty flag and its own mutex to serialize
"clean <-> dirty" transitions.

The \ ``synced_i_size``\  field is used to make sure we never write pages which are
beyond last synchronized inode size. See 'ubifs_writepage()' for more
information.

The \ ``ui_size``\  is a "shadow" variable for \ ``inode``\ ->i_size and UBIFS uses
\ ``ui_size``\  instead of \ ``inode``\ ->i_size. The reason for this is that UBIFS cannot
make sure \ ``inode``\ ->i_size is always changed under \ ``ui_mutex``\ , because it
cannot call 'truncate_setsize()' with \ ``ui_mutex``\  locked, because it would
deadlock with 'ubifs_writepage()' (see file.c). All the other inode fields
are changed under \ ``ui_mutex``\ , so they do not need "shadow" fields. Note, one
could consider to rework locking and base it on "shadow" fields.

.. _`ubifs_unclean_leb`:

struct ubifs_unclean_leb
========================

.. c:type:: struct ubifs_unclean_leb

    records a LEB recovered under read-only mode.

.. _`ubifs_unclean_leb.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_unclean_leb {
        struct list_head list;
        int lnum;
        int endpt;
    }

.. _`ubifs_unclean_leb.members`:

Members
-------

list
    list

lnum
    LEB number of recovered LEB

endpt
    offset where recovery ended

.. _`ubifs_unclean_leb.description`:

Description
-----------

This structure records a LEB identified during recovery that needs to be
cleaned but was not because UBIFS was mounted read-only. The information
is used to clean the LEB when remounting to read-write mode.

.. _`ubifs_lprops`:

struct ubifs_lprops
===================

.. c:type:: struct ubifs_lprops

    logical eraseblock properties.

.. _`ubifs_lprops.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_lprops {
        int free;
        int dirty;
        int flags;
        int lnum;
        union {
            struct list_head list;
            int hpos;
        } ;
    }

.. _`ubifs_lprops.members`:

Members
-------

free
    amount of free space in bytes

dirty
    amount of dirty space in bytes

flags
    LEB properties flags (see above)

lnum
    LEB number

{unnamed_union}
    anonymous

list
    list of same-category lprops (for LPROPS_EMPTY and LPROPS_FREEABLE)

hpos
    heap position in heap of same-category lprops (other categories)

.. _`ubifs_lpt_lprops`:

struct ubifs_lpt_lprops
=======================

.. c:type:: struct ubifs_lpt_lprops

    LPT logical eraseblock properties.

.. _`ubifs_lpt_lprops.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_lpt_lprops {
        int free;
        int dirty;
        unsigned tgc:1;
        unsigned cmt:1;
    }

.. _`ubifs_lpt_lprops.members`:

Members
-------

free
    amount of free space in bytes

dirty
    amount of dirty space in bytes

tgc
    trivial GC flag (1 => unmap after commit end)

cmt
    commit flag (1 => reserved for commit)

.. _`ubifs_lp_stats`:

struct ubifs_lp_stats
=====================

.. c:type:: struct ubifs_lp_stats

    statistics of eraseblocks in the main area.

.. _`ubifs_lp_stats.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_lp_stats {
        int empty_lebs;
        int taken_empty_lebs;
        int idx_lebs;
        long long total_free;
        long long total_dirty;
        long long total_used;
        long long total_dead;
        long long total_dark;
    }

.. _`ubifs_lp_stats.members`:

Members
-------

empty_lebs
    number of empty LEBs

taken_empty_lebs
    number of taken LEBs

idx_lebs
    number of indexing LEBs

total_free
    total free space in bytes (includes all LEBs)

total_dirty
    total dirty space in bytes (includes all LEBs)

total_used
    total used space in bytes (does not include index LEBs)

total_dead
    total dead space in bytes (does not include index LEBs)

total_dark
    total dark space in bytes (does not include index LEBs)

.. _`ubifs_lp_stats.description`:

Description
-----------

The \ ``taken_empty_lebs``\  field counts the LEBs that are in the transient state
of having been "taken" for use but not yet written to. \ ``taken_empty_lebs``\  is
needed to account correctly for \ ``gc_lnum``\ , otherwise \ ``empty_lebs``\  could be
used by itself (in which case 'unused_lebs' would be a better name). In the
case of \ ``gc_lnum``\ , it is "taken" at mount time or whenever a LEB is retained
by GC, but unlike other empty LEBs that are "taken", it may not be written
straight away (i.e. before the next commit start or unmount), so either
\ ``gc_lnum``\  must be specially accounted for, or the current approach followed
i.e. count it under \ ``taken_empty_lebs``\ .

\ ``empty_lebs``\  includes \ ``taken_empty_lebs``\ .

\ ``total_used``\ , \ ``total_dead``\  and \ ``total_dark``\  fields do not account indexing
LEBs.

.. _`ubifs_cnode`:

struct ubifs_cnode
==================

.. c:type:: struct ubifs_cnode

    LEB Properties Tree common node.

.. _`ubifs_cnode.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_cnode {
        struct ubifs_nnode *parent;
        struct ubifs_cnode *cnext;
        unsigned long flags;
        int iip;
        int level;
        int num;
    }

.. _`ubifs_cnode.members`:

Members
-------

parent
    parent nnode

cnext
    next cnode to commit

flags
    flags (%DIRTY_LPT_NODE or \ ``OBSOLETE_LPT_NODE``\ )

iip
    index in parent

level
    level in the tree (zero for pnodes, greater than zero for nnodes)

num
    node number

.. _`ubifs_pnode`:

struct ubifs_pnode
==================

.. c:type:: struct ubifs_pnode

    LEB Properties Tree leaf node.

.. _`ubifs_pnode.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_pnode {
        struct ubifs_nnode *parent;
        struct ubifs_cnode *cnext;
        unsigned long flags;
        int iip;
        int level;
        int num;
        struct ubifs_lprops lprops[UBIFS_LPT_FANOUT];
    }

.. _`ubifs_pnode.members`:

Members
-------

parent
    parent nnode

cnext
    next cnode to commit

flags
    flags (%DIRTY_LPT_NODE or \ ``OBSOLETE_LPT_NODE``\ )

iip
    index in parent

level
    level in the tree (always zero for pnodes)

num
    node number

lprops
    LEB properties array

.. _`ubifs_nbranch`:

struct ubifs_nbranch
====================

.. c:type:: struct ubifs_nbranch

    LEB Properties Tree internal node branch.

.. _`ubifs_nbranch.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_nbranch {
        int lnum;
        int offs;
        union {
            struct ubifs_nnode *nnode;
            struct ubifs_pnode *pnode;
            struct ubifs_cnode *cnode;
        } ;
    }

.. _`ubifs_nbranch.members`:

Members
-------

lnum
    LEB number of child

offs
    offset of child

{unnamed_union}
    anonymous

nnode
    nnode child

pnode
    pnode child

cnode
    cnode child

.. _`ubifs_nnode`:

struct ubifs_nnode
==================

.. c:type:: struct ubifs_nnode

    LEB Properties Tree internal node.

.. _`ubifs_nnode.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_nnode {
        struct ubifs_nnode *parent;
        struct ubifs_cnode *cnext;
        unsigned long flags;
        int iip;
        int level;
        int num;
        struct ubifs_nbranch nbranch[UBIFS_LPT_FANOUT];
    }

.. _`ubifs_nnode.members`:

Members
-------

parent
    parent nnode

cnext
    next cnode to commit

flags
    flags (%DIRTY_LPT_NODE or \ ``OBSOLETE_LPT_NODE``\ )

iip
    index in parent

level
    level in the tree (always greater than zero for nnodes)

num
    node number

nbranch
    branches to child nodes

.. _`ubifs_lpt_heap`:

struct ubifs_lpt_heap
=====================

.. c:type:: struct ubifs_lpt_heap

    heap of categorized lprops.

.. _`ubifs_lpt_heap.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_lpt_heap {
        struct ubifs_lprops **arr;
        int cnt;
        int max_cnt;
    }

.. _`ubifs_lpt_heap.members`:

Members
-------

arr
    heap array

cnt
    number in heap

max_cnt
    maximum number allowed in heap

.. _`ubifs_lpt_heap.description`:

Description
-----------

There are \ ``LPROPS_HEAP_CNT``\  heaps.

.. _`ubifs_wbuf`:

struct ubifs_wbuf
=================

.. c:type:: struct ubifs_wbuf

    UBIFS write-buffer.

.. _`ubifs_wbuf.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_wbuf {
        struct ubifs_info *c;
        void *buf;
        int lnum;
        int offs;
        int avail;
        int used;
        int size;
        int jhead;
        int (*sync_callback)(struct ubifs_info *c, int lnum, int free, int pad);
        struct mutex io_mutex;
        spinlock_t lock;
        struct hrtimer timer;
        unsigned int no_timer:1;
        unsigned int need_sync:1;
        int next_ino;
        ino_t *inodes;
    }

.. _`ubifs_wbuf.members`:

Members
-------

c
    UBIFS file-system description object

buf
    write-buffer (of min. flash I/O unit size)

lnum
    logical eraseblock number the write-buffer points to

offs
    write-buffer offset in this logical eraseblock

avail
    number of bytes available in the write-buffer

used
    number of used bytes in the write-buffer

size
    write-buffer size (in [@c->min_io_size, \ ``c``\ ->max_write_size] range)

jhead
    journal head the mutex belongs to (note, needed only to shut lockdep
    up by 'mutex_lock_nested()).

sync_callback
    write-buffer synchronization callback

io_mutex
    serializes write-buffer I/O

lock
    serializes \ ``buf``\ , \ ``lnum``\ , \ ``offs``\ , \ ``avail``\ , \ ``used``\ , \ ``next_ino``\  and \ ``inodes``\ 
    fields

timer
    write-buffer timer

no_timer
    non-zero if this write-buffer does not have a timer

need_sync
    non-zero if the timer expired and the wbuf needs sync'ing

next_ino
    points to the next position of the following inode number

inodes
    stores the inode numbers of the nodes which are in wbuf

.. _`ubifs_wbuf.description`:

Description
-----------

The write-buffer synchronization callback is called when the write-buffer is
synchronized in order to notify how much space was wasted due to
write-buffer padding and how much free space is left in the LEB.

.. _`ubifs_wbuf.note`:

Note
----

the fields \ ``buf``\ , \ ``lnum``\ , \ ``offs``\ , \ ``avail``\  and \ ``used``\  can be read under
spin-lock or mutex because they are written under both mutex and spin-lock.
\ ``buf``\  is appended to under mutex but overwritten under both mutex and
spin-lock. Thus the data between \ ``buf``\  and \ ``buf``\  + \ ``used``\  can be read under
spinlock.

.. _`ubifs_bud`:

struct ubifs_bud
================

.. c:type:: struct ubifs_bud

    bud logical eraseblock.

.. _`ubifs_bud.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_bud {
        int lnum;
        int start;
        int jhead;
        struct list_head list;
        struct rb_node rb;
    }

.. _`ubifs_bud.members`:

Members
-------

lnum
    logical eraseblock number

start
    where the (uncommitted) bud data starts

jhead
    journal head number this bud belongs to

list
    link in the list buds belonging to the same journal head

rb
    link in the tree of all buds

.. _`ubifs_jhead`:

struct ubifs_jhead
==================

.. c:type:: struct ubifs_jhead

    journal head.

.. _`ubifs_jhead.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_jhead {
        struct ubifs_wbuf wbuf;
        struct list_head buds_list;
        unsigned int grouped:1;
    }

.. _`ubifs_jhead.members`:

Members
-------

wbuf
    head's write-buffer

buds_list
    list of bud LEBs belonging to this journal head

grouped
    non-zero if UBIFS groups nodes when writing to this journal head

.. _`ubifs_jhead.description`:

Description
-----------

Note, the \ ``buds``\  list is protected by the \ ``c``\ ->buds_lock.

.. _`ubifs_zbranch`:

struct ubifs_zbranch
====================

.. c:type:: struct ubifs_zbranch

    key/coordinate/length branch stored in znodes.

.. _`ubifs_zbranch.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_zbranch {
        union ubifs_key key;
        union {
            struct ubifs_znode *znode;
            void *leaf;
        } ;
        int lnum;
        int offs;
        int len;
    }

.. _`ubifs_zbranch.members`:

Members
-------

key
    key

{unnamed_union}
    anonymous

znode
    znode address in memory

leaf
    *undescribed*

lnum
    LEB number of the target node (indexing node or data node)

offs
    target node offset within \ ``lnum``\ 

len
    target node length

.. _`ubifs_znode`:

struct ubifs_znode
==================

.. c:type:: struct ubifs_znode

    in-memory representation of an indexing node.

.. _`ubifs_znode.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_znode {
        struct ubifs_znode *parent;
        struct ubifs_znode *cnext;
        unsigned long flags;
        unsigned long time;
        int level;
        int child_cnt;
        int iip;
        int alt;
        int lnum;
        int offs;
        int len;
        struct ubifs_zbranch zbranch[];
    }

.. _`ubifs_znode.members`:

Members
-------

parent
    parent znode or NULL if it is the root

cnext
    next znode to commit

flags
    znode flags (%DIRTY_ZNODE, \ ``COW_ZNODE``\  or \ ``OBSOLETE_ZNODE``\ )

time
    last access time (seconds)

level
    level of the entry in the TNC tree

child_cnt
    count of child znodes

iip
    index in parent's zbranch array

alt
    lower bound of key range has altered i.e. child inserted at slot 0

lnum
    LEB number of the corresponding indexing node

offs
    offset of the corresponding indexing node

len
    length  of the corresponding indexing node

zbranch
    array of znode branches (@c->fanout elements)

.. _`ubifs_znode.description`:

Description
-----------

Note! The \ ``lnum``\ , \ ``offs``\ , and \ ``len``\  fields are not really needed - we have them
only for internal consistency check. They could be removed to save some RAM.

.. _`bu_info`:

struct bu_info
==============

.. c:type:: struct bu_info

    bulk-read information.

.. _`bu_info.definition`:

Definition
----------

.. code-block:: c

    struct bu_info {
        union ubifs_key key;
        struct ubifs_zbranch zbranch[UBIFS_MAX_BULK_READ];
        void *buf;
        int buf_len;
        int gc_seq;
        int cnt;
        int blk_cnt;
        int eof;
    }

.. _`bu_info.members`:

Members
-------

key
    first data node key

zbranch
    zbranches of data nodes to bulk read

buf
    buffer to read into

buf_len
    buffer length

gc_seq
    GC sequence number to detect races with GC

cnt
    number of data nodes for bulk read

blk_cnt
    number of data blocks including holes

eof
    *undescribed*

.. _`ubifs_node_range`:

struct ubifs_node_range
=======================

.. c:type:: struct ubifs_node_range

    node length range description data structure.

.. _`ubifs_node_range.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_node_range {
        union {
            int len;
            int min_len;
        } ;
        int max_len;
    }

.. _`ubifs_node_range.members`:

Members
-------

{unnamed_union}
    anonymous

len
    fixed node length

min_len
    minimum possible node length

max_len
    maximum possible node length

.. _`ubifs_node_range.description`:

Description
-----------

If \ ``max_len``\  is \ ``0``\ , the node has fixed length \ ``len``\ .

.. _`ubifs_compressor`:

struct ubifs_compressor
=======================

.. c:type:: struct ubifs_compressor

    UBIFS compressor description structure.

.. _`ubifs_compressor.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_compressor {
        int compr_type;
        struct crypto_comp *cc;
        struct mutex *comp_mutex;
        struct mutex *decomp_mutex;
        const char *name;
        const char *capi_name;
    }

.. _`ubifs_compressor.members`:

Members
-------

compr_type
    compressor type (%UBIFS_COMPR_LZO, etc)

cc
    cryptoapi compressor handle

comp_mutex
    mutex used during compression

decomp_mutex
    mutex used during decompression

name
    compressor name

capi_name
    cryptoapi compressor name

.. _`ubifs_budget_req`:

struct ubifs_budget_req
=======================

.. c:type:: struct ubifs_budget_req

    budget requirements of an operation.

.. _`ubifs_budget_req.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_budget_req {
        unsigned int fast:1;
        unsigned int recalculate:1;
    #ifndef UBIFS_DEBUG
        unsigned int new_page:1;
        unsigned int dirtied_page:1;
        unsigned int new_dent:1;
        unsigned int mod_dent:1;
        unsigned int new_ino:1;
        unsigned int new_ino_d:13;
        unsigned int dirtied_ino:4;
        unsigned int dirtied_ino_d:15;
    #else
        unsigned int new_page;
        unsigned int dirtied_page;
        unsigned int new_dent;
        unsigned int mod_dent;
        unsigned int new_ino;
        unsigned int new_ino_d;
        unsigned int dirtied_ino;
        unsigned int dirtied_ino_d;
    #endif
        int idx_growth;
        int data_growth;
        int dd_growth;
    }

.. _`ubifs_budget_req.members`:

Members
-------

fast
    non-zero if the budgeting should try to acquire budget quickly and
    should not try to call write-back

recalculate
    non-zero if \ ``idx_growth``\ , \ ``data_growth``\ , and \ ``dd_growth``\  fields
    have to be re-calculated

new_page
    non-zero if the operation adds a new page

dirtied_page
    non-zero if the operation makes a page dirty

new_dent
    non-zero if the operation adds a new directory entry

mod_dent
    non-zero if the operation removes or modifies an existing
    directory entry

new_ino
    non-zero if the operation adds a new inode

new_ino_d
    how much data newly created inode contains

dirtied_ino
    how many inodes the operation makes dirty

dirtied_ino_d
    how much data dirtied inode contains

new_page
    non-zero if the operation adds a new page

dirtied_page
    non-zero if the operation makes a page dirty

new_dent
    non-zero if the operation adds a new directory entry

mod_dent
    non-zero if the operation removes or modifies an existing
    directory entry

new_ino
    non-zero if the operation adds a new inode

new_ino_d
    how much data newly created inode contains

dirtied_ino
    how many inodes the operation makes dirty

dirtied_ino_d
    how much data dirtied inode contains

idx_growth
    how much the index will supposedly grow

data_growth
    how much new data the operation will supposedly add

dd_growth
    how much data that makes other data dirty the operation will
    supposedly add

.. _`ubifs_budget_req.description`:

Description
-----------

\ ``idx_growth``\ , \ ``data_growth``\  and \ ``dd_growth``\  are not used in budget request. The
budgeting subsystem caches index and data growth values there to avoid
re-calculating them when the budget is released. However, if \ ``idx_growth``\  is
\ ``-1``\ , it is calculated by the release function using other fields.

An inode may contain 4KiB of data at max., thus the widths of \ ``new_ino_d``\ 
is 13 bits, and \ ``dirtied_ino_d``\  - 15, because up to 4 inodes may be made
dirty by the re-name operation.

Note, UBIFS aligns node lengths to 8-bytes boundary, so the requester has to
make sure the amount of inode data which contribute to \ ``new_ino_d``\  and
\ ``dirtied_ino_d``\  fields are aligned.

.. _`ubifs_orphan`:

struct ubifs_orphan
===================

.. c:type:: struct ubifs_orphan

    stores the inode number of an orphan.

.. _`ubifs_orphan.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_orphan {
        struct rb_node rb;
        struct list_head list;
        struct list_head new_list;
        struct ubifs_orphan *cnext;
        struct ubifs_orphan *dnext;
        ino_t inum;
        unsigned new:1;
        unsigned cmt:1;
        unsigned del:1;
    }

.. _`ubifs_orphan.members`:

Members
-------

rb
    rb-tree node of rb-tree of orphans sorted by inode number

list
    list head of list of orphans in order added

new_list
    list head of list of orphans added since the last commit

cnext
    next orphan to commit

dnext
    next orphan to delete

inum
    inode number

new
    \ ``1``\  => added since the last commit, otherwise \ ``0``\ 

cmt
    \ ``1``\  => commit pending, otherwise \ ``0``\ 

del
    \ ``1``\  => delete pending, otherwise \ ``0``\ 

.. _`ubifs_mount_opts`:

struct ubifs_mount_opts
=======================

.. c:type:: struct ubifs_mount_opts

    UBIFS-specific mount options information.

.. _`ubifs_mount_opts.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_mount_opts {
        unsigned int unmount_mode:2;
        unsigned int bulk_read:2;
        unsigned int chk_data_crc:2;
        unsigned int override_compr:1;
        unsigned int compr_type:2;
    }

.. _`ubifs_mount_opts.members`:

Members
-------

unmount_mode
    selected unmount mode (%0 default, \ ``1``\  normal, \ ``2``\  fast)

bulk_read
    enable/disable bulk-reads (%0 default, \ ``1``\  disable, \ ``2``\  enable)

chk_data_crc
    enable/disable CRC data checking when reading data nodes
    (%0 default, \ ``1``\  disable, \ ``2``\  enable)

override_compr
    override default compressor (%0 - do not override and use
    superblock compressor, \ ``1``\  - override and use compressor
    specified in \ ``compr_type``\ )

compr_type
    compressor type to override the superblock compressor with
    (%UBIFS_COMPR_NONE, etc)

.. _`ubifs_budg_info`:

struct ubifs_budg_info
======================

.. c:type:: struct ubifs_budg_info

    UBIFS budgeting information.

.. _`ubifs_budg_info.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_budg_info {
        long long idx_growth;
        long long data_growth;
        long long dd_growth;
        long long uncommitted_idx;
        unsigned long long old_idx_sz;
        int min_idx_lebs;
        unsigned int nospace:1;
        unsigned int nospace_rp:1;
        int page_budget;
        int inode_budget;
        int dent_budget;
    }

.. _`ubifs_budg_info.members`:

Members
-------

idx_growth
    amount of bytes budgeted for index growth

data_growth
    amount of bytes budgeted for cached data

dd_growth
    amount of bytes budgeted for cached data that will make
    other data dirty

uncommitted_idx
    amount of bytes were budgeted for growth of the index, but
    which still have to be taken into account because the index
    has not been committed so far

old_idx_sz
    size of index on flash

min_idx_lebs
    minimum number of LEBs required for the index

nospace
    non-zero if the file-system does not have flash space (used as
    optimization)

nospace_rp
    the same as \ ``nospace``\ , but additionally means that even reserved
    pool is full

page_budget
    budget for a page (constant, never changed after mount)

inode_budget
    budget for an inode (constant, never changed after mount)

dent_budget
    budget for a directory entry (constant, never changed after
    mount)

.. _`ubifs_info`:

struct ubifs_info
=================

.. c:type:: struct ubifs_info

    UBIFS file-system description data structure (per-superblock).

.. _`ubifs_info.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_info {
        struct super_block *vfs_sb;
        ino_t highest_inum;
        unsigned long long max_sqnum;
        unsigned long long cmt_no;
        spinlock_t cnt_lock;
        int fmt_version;
        int ro_compat_version;
        unsigned char uuid[16];
        int lhead_lnum;
        int lhead_offs;
        int ltail_lnum;
        struct mutex log_mutex;
        int min_log_bytes;
        long long cmt_bud_bytes;
        struct rb_root buds;
        long long bud_bytes;
        spinlock_t buds_lock;
        int jhead_cnt;
        struct ubifs_jhead *jheads;
        long long max_bud_bytes;
        long long bg_bud_bytes;
        struct list_head old_buds;
        int max_bud_cnt;
        struct rw_semaphore commit_sem;
        int cmt_state;
        spinlock_t cs_lock;
        wait_queue_head_t cmt_wq;
        unsigned int big_lpt:1;
        unsigned int space_fixup:1;
        unsigned int double_hash:1;
        unsigned int encrypted:1;
        unsigned int no_chk_data_crc:1;
        unsigned int bulk_read:1;
        unsigned int default_compr:2;
        unsigned int rw_incompat:1;
        struct mutex tnc_mutex;
        struct ubifs_zbranch zroot;
        struct ubifs_znode *cnext;
        struct ubifs_znode *enext;
        int *gap_lebs;
        void *cbuf;
        void *ileb_buf;
        int ileb_len;
        int ihead_lnum;
        int ihead_offs;
        int *ilebs;
        int ileb_cnt;
        int ileb_nxt;
        struct rb_root old_idx;
        int *bottom_up_buf;
        struct ubifs_mst_node *mst_node;
        int mst_offs;
        int max_bu_buf_len;
        struct mutex bu_mutex;
        struct bu_info bu;
        struct mutex write_reserve_mutex;
        void *write_reserve_buf;
        int log_lebs;
        long long log_bytes;
        int log_last;
        int lpt_lebs;
        int lpt_first;
        int lpt_last;
        int orph_lebs;
        int orph_first;
        int orph_last;
        int main_lebs;
        int main_first;
        long long main_bytes;
        uint8_t key_hash_type;
        uint32_t (*key_hash)(const char *str, int len);
        int key_fmt;
        int key_len;
        int fanout;
        int min_io_size;
        int min_io_shift;
        int max_write_size;
        int max_write_shift;
        int leb_size;
        int leb_start;
        int half_leb_size;
        int idx_leb_size;
        int leb_cnt;
        int max_leb_cnt;
        int old_leb_cnt;
        unsigned int ro_media:1;
        unsigned int ro_mount:1;
        unsigned int ro_error:1;
        atomic_long_t dirty_pg_cnt;
        atomic_long_t dirty_zn_cnt;
        atomic_long_t clean_zn_cnt;
        spinlock_t space_lock;
        struct ubifs_lp_stats lst;
        struct ubifs_budg_info bi;
        unsigned long long calc_idx_sz;
        int ref_node_alsz;
        int mst_node_alsz;
        int min_idx_node_sz;
        int max_idx_node_sz;
        long long max_inode_sz;
        int max_znode_sz;
        int leb_overhead;
        int dead_wm;
        int dark_wm;
        int block_cnt;
        struct ubifs_node_range ranges[UBIFS_NODE_TYPES_CNT];
        struct ubi_volume_desc *ubi;
        struct ubi_device_info di;
        struct ubi_volume_info vi;
        struct rb_root orph_tree;
        struct list_head orph_list;
        struct list_head orph_new;
        struct ubifs_orphan *orph_cnext;
        struct ubifs_orphan *orph_dnext;
        spinlock_t orphan_lock;
        void *orph_buf;
        int new_orphans;
        int cmt_orphans;
        int tot_orphans;
        int max_orphans;
        int ohead_lnum;
        int ohead_offs;
        int no_orphs;
        struct task_struct *bgt;
        char bgt_name[sizeof(BGT_NAME_PATTERN) + 9];
        int need_bgt;
        int need_wbuf_sync;
        int gc_lnum;
        void *sbuf;
        struct list_head idx_gc;
        int idx_gc_cnt;
        int gc_seq;
        int gced_lnum;
        struct list_head infos_list;
        struct mutex umount_mutex;
        unsigned int shrinker_run_no;
        int space_bits;
        int lpt_lnum_bits;
        int lpt_offs_bits;
        int lpt_spc_bits;
        int pcnt_bits;
        int lnum_bits;
        int nnode_sz;
        int pnode_sz;
        int ltab_sz;
        int lsave_sz;
        int pnode_cnt;
        int nnode_cnt;
        int lpt_hght;
        int pnodes_have;
        struct mutex lp_mutex;
        int lpt_lnum;
        int lpt_offs;
        int nhead_lnum;
        int nhead_offs;
        int lpt_drty_flgs;
        int dirty_nn_cnt;
        int dirty_pn_cnt;
        int check_lpt_free;
        long long lpt_sz;
        void *lpt_nod_buf;
        void *lpt_buf;
        struct ubifs_nnode *nroot;
        struct ubifs_cnode *lpt_cnext;
        struct ubifs_lpt_heap lpt_heap[LPROPS_HEAP_CNT];
        struct ubifs_lpt_heap dirty_idx;
        struct list_head uncat_list;
        struct list_head empty_list;
        struct list_head freeable_list;
        struct list_head frdi_idx_list;
        int freeable_cnt;
        int in_a_category_cnt;
        int ltab_lnum;
        int ltab_offs;
        struct ubifs_lpt_lprops *ltab;
        struct ubifs_lpt_lprops *ltab_cmt;
        int lsave_cnt;
        int lsave_lnum;
        int lsave_offs;
        int *lsave;
        int lscan_lnum;
        long long rp_size;
        long long report_rp_size;
        kuid_t rp_uid;
        kgid_t rp_gid;
        unsigned int empty:1;
        unsigned int need_recovery:1;
        unsigned int replaying:1;
        unsigned int mounting:1;
        unsigned int remounting_rw:1;
        unsigned int probing:1;
        struct list_head replay_list;
        struct list_head replay_buds;
        unsigned long long cs_sqnum;
        unsigned long long replay_sqnum;
        struct list_head unclean_leb_list;
        struct ubifs_mst_node *rcvrd_mst_node;
        struct rb_root size_tree;
        struct ubifs_mount_opts mount_opts;
        struct ubifs_debug_info *dbg;
    }

.. _`ubifs_info.members`:

Members
-------

vfs_sb
    VFS \ ``struct``\  super_block object

highest_inum
    highest used inode number

max_sqnum
    current global sequence number

cmt_no
    commit number of the last successfully completed commit, protected
    by \ ``commit_sem``\ 

cnt_lock
    protects \ ``highest_inum``\  and \ ``max_sqnum``\  counters

fmt_version
    UBIFS on-flash format version

ro_compat_version
    R/O compatibility version

uuid
    UUID from super block

lhead_lnum
    log head logical eraseblock number

lhead_offs
    log head offset

ltail_lnum
    log tail logical eraseblock number (offset is always 0)

log_mutex
    protects the log, \ ``lhead_lnum``\ , \ ``lhead_offs``\ , \ ``ltail_lnum``\ , and
    \ ``bud_bytes``\ 

min_log_bytes
    minimum required number of bytes in the log

cmt_bud_bytes
    used during commit to temporarily amount of bytes in
    committed buds

buds
    tree of all buds indexed by bud LEB number

bud_bytes
    how many bytes of flash is used by buds

buds_lock
    protects the \ ``buds``\  tree, \ ``bud_bytes``\ , and per-journal head bud
    lists

jhead_cnt
    count of journal heads

jheads
    journal heads (head zero is base head)

max_bud_bytes
    maximum number of bytes allowed in buds

bg_bud_bytes
    number of bud bytes when background commit is initiated

old_buds
    buds to be released after commit ends

max_bud_cnt
    maximum number of buds

commit_sem
    synchronizes committer with other processes

cmt_state
    commit state

cs_lock
    commit state lock

cmt_wq
    wait queue to sleep on if the log is full and a commit is running

big_lpt
    flag that LPT is too big to write whole during commit

space_fixup
    flag indicating that free space in LEBs needs to be cleaned up

double_hash
    flag indicating that we can do lookups by hash

encrypted
    flag indicating that this file system contains encrypted files

no_chk_data_crc
    do not check CRCs when reading data nodes (except during
    recovery)

bulk_read
    enable bulk-reads

default_compr
    default compression algorithm (%UBIFS_COMPR_LZO, etc)

rw_incompat
    the media is not R/W compatible

tnc_mutex
    protects the Tree Node Cache (TNC), \ ``zroot``\ , \ ``cnext``\ , \ ``enext``\ , and
    \ ``calc_idx_sz``\ 

zroot
    zbranch which points to the root index node and znode

cnext
    next znode to commit

enext
    next znode to commit to empty space

gap_lebs
    array of LEBs used by the in-gaps commit method

cbuf
    commit buffer

ileb_buf
    buffer for commit in-the-gaps method

ileb_len
    length of data in ileb_buf

ihead_lnum
    LEB number of index head

ihead_offs
    offset of index head

ilebs
    pre-allocated index LEBs

ileb_cnt
    number of pre-allocated index LEBs

ileb_nxt
    next pre-allocated index LEBs

old_idx
    tree of index nodes obsoleted since the last commit start

bottom_up_buf
    a buffer which is used by 'dirty_cow_bottom_up()' in tnc.c

mst_node
    master node

mst_offs
    offset of valid master node

max_bu_buf_len
    maximum bulk-read buffer length

bu_mutex
    protects the pre-allocated bulk-read buffer and \ ``c``\ ->bu

bu
    pre-allocated bulk-read information

write_reserve_mutex
    protects \ ``write_reserve_buf``\ 

write_reserve_buf
    on the write path we allocate memory, which might
    sometimes be unavailable, in which case we use this
    write reserve buffer

log_lebs
    number of logical eraseblocks in the log

log_bytes
    log size in bytes

log_last
    last LEB of the log

lpt_lebs
    number of LEBs used for lprops table

lpt_first
    first LEB of the lprops table area

lpt_last
    last LEB of the lprops table area

orph_lebs
    number of LEBs used for the orphan area

orph_first
    first LEB of the orphan area

orph_last
    last LEB of the orphan area

main_lebs
    count of LEBs in the main area

main_first
    first LEB of the main area

main_bytes
    main area size in bytes

key_hash_type
    type of the key hash

key_hash
    direntry key hash function

key_fmt
    key format

key_len
    key length

fanout
    fanout of the index tree (number of links per indexing node)

min_io_size
    minimal input/output unit size

min_io_shift
    number of bits in \ ``min_io_size``\  minus one

max_write_size
    maximum amount of bytes the underlying flash can write at a
    time (MTD write buffer size)

max_write_shift
    number of bits in \ ``max_write_size``\  minus one

leb_size
    logical eraseblock size in bytes

leb_start
    starting offset of logical eraseblocks within physical
    eraseblocks

half_leb_size
    half LEB size

idx_leb_size
    how many bytes of an LEB are effectively available when it is
    used to store indexing nodes (@leb_size - \ ``max_idx_node_sz``\ )

leb_cnt
    count of logical eraseblocks

max_leb_cnt
    maximum count of logical eraseblocks

old_leb_cnt
    count of logical eraseblocks before re-size

ro_media
    the underlying UBI volume is read-only

ro_mount
    the file-system was mounted as read-only

ro_error
    UBIFS switched to R/O mode because an error happened

dirty_pg_cnt
    number of dirty pages (not used)

dirty_zn_cnt
    number of dirty znodes

clean_zn_cnt
    number of clean znodes

space_lock
    protects \ ``bi``\  and \ ``lst``\ 

lst
    lprops statistics

bi
    budgeting information

calc_idx_sz
    temporary variable which is used to calculate new index size
    (contains accurate new index size at end of TNC commit start)

ref_node_alsz
    size of the LEB reference node aligned to the min. flash
    I/O unit

mst_node_alsz
    master node aligned size

min_idx_node_sz
    minimum indexing node aligned on 8-bytes boundary

max_idx_node_sz
    maximum indexing node aligned on 8-bytes boundary

max_inode_sz
    maximum possible inode size in bytes

max_znode_sz
    size of znode in bytes

leb_overhead
    how many bytes are wasted in an LEB when it is filled with
    data nodes of maximum size - used in free space reporting

dead_wm
    LEB dead space watermark

dark_wm
    LEB dark space watermark

block_cnt
    count of 4KiB blocks on the FS

ranges
    UBIFS node length ranges

ubi
    UBI volume descriptor

di
    UBI device information

vi
    UBI volume information

orph_tree
    rb-tree of orphan inode numbers

orph_list
    list of orphan inode numbers in order added

orph_new
    list of orphan inode numbers added since last commit

orph_cnext
    next orphan to commit

orph_dnext
    next orphan to delete

orphan_lock
    lock for orph_tree and orph_new

orph_buf
    buffer for orphan nodes

new_orphans
    number of orphans since last commit

cmt_orphans
    number of orphans being committed

tot_orphans
    number of orphans in the rb_tree

max_orphans
    maximum number of orphans allowed

ohead_lnum
    orphan head LEB number

ohead_offs
    orphan head offset

no_orphs
    non-zero if there are no orphans

bgt
    UBIFS background thread

bgt_name
    background thread name

need_bgt
    if background thread should run

need_wbuf_sync
    if write-buffers have to be synchronized

gc_lnum
    LEB number used for garbage collection

sbuf
    a buffer of LEB size used by GC and replay for scanning

idx_gc
    list of index LEBs that have been garbage collected

idx_gc_cnt
    number of elements on the idx_gc list

gc_seq
    incremented for every non-index LEB garbage collected

gced_lnum
    last non-index LEB that was garbage collected

infos_list
    links all 'ubifs_info' objects

umount_mutex
    serializes shrinker and un-mount

shrinker_run_no
    shrinker run number

space_bits
    number of bits needed to record free or dirty space

lpt_lnum_bits
    number of bits needed to record a LEB number in the LPT

lpt_offs_bits
    number of bits needed to record an offset in the LPT

lpt_spc_bits
    number of bits needed to space in the LPT

pcnt_bits
    number of bits needed to record pnode or nnode number

lnum_bits
    number of bits needed to record LEB number

nnode_sz
    size of on-flash nnode

pnode_sz
    size of on-flash pnode

ltab_sz
    size of on-flash LPT lprops table

lsave_sz
    size of on-flash LPT save table

pnode_cnt
    number of pnodes

nnode_cnt
    number of nnodes

lpt_hght
    height of the LPT

pnodes_have
    number of pnodes in memory

lp_mutex
    protects lprops table and all the other lprops-related fields

lpt_lnum
    LEB number of the root nnode of the LPT

lpt_offs
    offset of the root nnode of the LPT

nhead_lnum
    LEB number of LPT head

nhead_offs
    offset of LPT head

lpt_drty_flgs
    dirty flags for LPT special nodes e.g. ltab

dirty_nn_cnt
    number of dirty nnodes

dirty_pn_cnt
    number of dirty pnodes

check_lpt_free
    flag that indicates LPT GC may be needed

lpt_sz
    LPT size

lpt_nod_buf
    buffer for an on-flash nnode or pnode

lpt_buf
    buffer of LEB size used by LPT

nroot
    address in memory of the root nnode of the LPT

lpt_cnext
    next LPT node to commit

lpt_heap
    array of heaps of categorized lprops

dirty_idx
    a (reverse sorted) copy of the LPROPS_DIRTY_IDX heap as at
    previous commit start

uncat_list
    list of un-categorized LEBs

empty_list
    list of empty LEBs

freeable_list
    list of freeable non-index LEBs (free + dirty == \ ``leb_size``\ )

frdi_idx_list
    list of freeable index LEBs (free + dirty == \ ``leb_size``\ )

freeable_cnt
    number of freeable LEBs in \ ``freeable_list``\ 

in_a_category_cnt
    count of lprops which are in a certain category, which
    basically meants that they were loaded from the flash

ltab_lnum
    LEB number of LPT's own lprops table

ltab_offs
    offset of LPT's own lprops table

ltab
    LPT's own lprops table

ltab_cmt
    LPT's own lprops table (commit copy)

lsave_cnt
    number of LEB numbers in LPT's save table

lsave_lnum
    LEB number of LPT's save table

lsave_offs
    offset of LPT's save table

lsave
    LPT's save table

lscan_lnum
    LEB number of last LPT scan

rp_size
    size of the reserved pool in bytes

report_rp_size
    size of the reserved pool reported to user-space

rp_uid
    reserved pool user ID

rp_gid
    reserved pool group ID

empty
    \ ``1``\  if the UBI device is empty

need_recovery
    \ ``1``\  if the file-system needs recovery

replaying
    \ ``1``\  during journal replay

mounting
    \ ``1``\  while mounting

remounting_rw
    \ ``1``\  while re-mounting from R/O mode to R/W mode

probing
    \ ``1``\  while attempting to mount if SB_SILENT mount flag is set

replay_list
    temporary list used during journal replay

replay_buds
    list of buds to replay

cs_sqnum
    sequence number of first node in the log (commit start node)

replay_sqnum
    sequence number of node currently being replayed

unclean_leb_list
    LEBs to recover when re-mounting R/O mounted FS to R/W
    mode

rcvrd_mst_node
    recovered master node to write when re-mounting R/O mounted
    FS to R/W mode

size_tree
    inode size information for recovery

mount_opts
    UBIFS-specific mount options

dbg
    debugging-related information

.. This file was automatic generated / don't edit.

