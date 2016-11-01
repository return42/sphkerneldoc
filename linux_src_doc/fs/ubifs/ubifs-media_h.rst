.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/ubifs-media.h

.. _`ubifs_ch`:

struct ubifs_ch
===============

.. c:type:: struct ubifs_ch

    common header node.

.. _`ubifs_ch.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_ch {
        __le32 magic;
        __le32 crc;
        __le64 sqnum;
        __le32 len;
        __u8 node_type;
        __u8 group_type;
        __u8 padding[2];
    }

.. _`ubifs_ch.members`:

Members
-------

magic
    UBIFS node magic number (%UBIFS_NODE_MAGIC)

crc
    CRC-32 checksum of the node header

sqnum
    sequence number

len
    full node length

node_type
    node type

group_type
    node group type

padding
    reserved for future, zeroes

.. _`ubifs_ch.description`:

Description
-----------

Every UBIFS node starts with this common part. If the node has a key, the
key always goes next.

.. _`ubifs_dev_desc`:

union ubifs_dev_desc
====================

.. c:type:: struct ubifs_dev_desc

    device node descriptor.

.. _`ubifs_dev_desc.definition`:

Definition
----------

.. code-block:: c

    union ubifs_dev_desc {
        __le32 new;
        __le64 huge;
    }

.. _`ubifs_dev_desc.members`:

Members
-------

new
    new type device descriptor

huge
    huge type device descriptor

.. _`ubifs_dev_desc.description`:

Description
-----------

This data structure describes major/minor numbers of a device node. In an
inode is a device node then its data contains an object of this type. UBIFS
uses standard Linux "new" and "huge" device node encodings.

.. _`ubifs_ino_node`:

struct ubifs_ino_node
=====================

.. c:type:: struct ubifs_ino_node

    inode node.

.. _`ubifs_ino_node.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_ino_node {
        struct ubifs_ch ch;
        __u8 key[UBIFS_MAX_KEY_LEN];
        __le64 creat_sqnum;
        __le64 size;
        __le64 atime_sec;
        __le64 ctime_sec;
        __le64 mtime_sec;
        __le32 atime_nsec;
        __le32 ctime_nsec;
        __le32 mtime_nsec;
        __le32 nlink;
        __le32 uid;
        __le32 gid;
        __le32 mode;
        __le32 flags;
        __le32 data_len;
        __le32 xattr_cnt;
        __le32 xattr_size;
        __u8 padding1[4];
        __le32 xattr_names;
        __le16 compr_type;
        __u8 padding2[26];
        __u8 data[];
    }

.. _`ubifs_ino_node.members`:

Members
-------

ch
    common header

key
    node key

creat_sqnum
    sequence number at time of creation

size
    inode size in bytes (amount of uncompressed data)

atime_sec
    access time seconds

ctime_sec
    creation time seconds

mtime_sec
    modification time seconds

atime_nsec
    access time nanoseconds

ctime_nsec
    creation time nanoseconds

mtime_nsec
    modification time nanoseconds

nlink
    number of hard links

uid
    owner ID

gid
    group ID

mode
    access flags

flags
    per-inode flags (%UBIFS_COMPR_FL, \ ``UBIFS_SYNC_FL``\ , etc)

data_len
    inode data length

xattr_cnt
    count of extended attributes this inode has

xattr_size
    summarized size of all extended attributes in bytes

padding1
    reserved for future, zeroes

xattr_names
    sum of lengths of all extended attribute names belonging to
    this inode

compr_type
    compression type used for this inode

padding2
    reserved for future, zeroes

data
    data attached to the inode

.. _`ubifs_ino_node.description`:

Description
-----------

Note, even though inode compression type is defined by \ ``compr_type``\ , some
nodes of this inode may be compressed with different compressor - this
happens if compression type is changed while the inode already has data
nodes. But \ ``compr_type``\  will be use for further writes to the inode.

Note, do not forget to amend 'zero_ino_node_unused()' function when changing
the padding fields.

.. _`ubifs_dent_node`:

struct ubifs_dent_node
======================

.. c:type:: struct ubifs_dent_node

    directory entry node.

.. _`ubifs_dent_node.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_dent_node {
        struct ubifs_ch ch;
        __u8 key[UBIFS_MAX_KEY_LEN];
        __le64 inum;
        __u8 padding1;
        __u8 type;
        __le16 nlen;
        __u8 padding2[4];
        __u8 name[];
    }

.. _`ubifs_dent_node.members`:

Members
-------

ch
    common header

key
    node key

inum
    target inode number

padding1
    reserved for future, zeroes

type
    type of the target inode (%UBIFS_ITYPE_REG, \ ``UBIFS_ITYPE_DIR``\ , etc)

nlen
    name length

padding2
    reserved for future, zeroes

name
    zero-terminated name

.. _`ubifs_dent_node.description`:

Description
-----------

Note, do not forget to amend 'zero_dent_node_unused()' function when
changing the padding fields.

.. _`ubifs_data_node`:

struct ubifs_data_node
======================

.. c:type:: struct ubifs_data_node

    data node.

.. _`ubifs_data_node.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_data_node {
        struct ubifs_ch ch;
        __u8 key[UBIFS_MAX_KEY_LEN];
        __le32 size;
        __le16 compr_type;
        __u8 padding[2];
        __u8 data[];
    }

.. _`ubifs_data_node.members`:

Members
-------

ch
    common header

key
    node key

size
    uncompressed data size in bytes

compr_type
    compression type (%UBIFS_COMPR_NONE, \ ``UBIFS_COMPR_LZO``\ , etc)

padding
    reserved for future, zeroes

data
    data

.. _`ubifs_data_node.description`:

Description
-----------

Note, do not forget to amend 'zero_data_node_unused()' function when
changing the padding fields.

.. _`ubifs_trun_node`:

struct ubifs_trun_node
======================

.. c:type:: struct ubifs_trun_node

    truncation node.

.. _`ubifs_trun_node.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_trun_node {
        struct ubifs_ch ch;
        __le32 inum;
        __u8 padding[12];
        __le64 old_size;
        __le64 new_size;
    }

.. _`ubifs_trun_node.members`:

Members
-------

ch
    common header

inum
    truncated inode number

padding
    reserved for future, zeroes

old_size
    size before truncation

new_size
    size after truncation

.. _`ubifs_trun_node.description`:

Description
-----------

This node exists only in the journal and never goes to the main area. Note,
do not forget to amend 'zero_trun_node_unused()' function when changing the
padding fields.

.. _`ubifs_pad_node`:

struct ubifs_pad_node
=====================

.. c:type:: struct ubifs_pad_node

    padding node.

.. _`ubifs_pad_node.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_pad_node {
        struct ubifs_ch ch;
        __le32 pad_len;
    }

.. _`ubifs_pad_node.members`:

Members
-------

ch
    common header

pad_len
    how many bytes after this node are unused (because padded)

.. _`ubifs_sb_node`:

struct ubifs_sb_node
====================

.. c:type:: struct ubifs_sb_node

    superblock node.

.. _`ubifs_sb_node.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_sb_node {
        struct ubifs_ch ch;
        __u8 padding[2];
        __u8 key_hash;
        __u8 key_fmt;
        __le32 flags;
        __le32 min_io_size;
        __le32 leb_size;
        __le32 leb_cnt;
        __le32 max_leb_cnt;
        __le64 max_bud_bytes;
        __le32 log_lebs;
        __le32 lpt_lebs;
        __le32 orph_lebs;
        __le32 jhead_cnt;
        __le32 fanout;
        __le32 lsave_cnt;
        __le32 fmt_version;
        __le16 default_compr;
        __u8 padding1[2];
        __le32 rp_uid;
        __le32 rp_gid;
        __le64 rp_size;
        __le32 time_gran;
        __u8 uuid[16];
        __le32 ro_compat_version;
        __u8 padding2[3968];
    }

.. _`ubifs_sb_node.members`:

Members
-------

ch
    common header

padding
    reserved for future, zeroes

key_hash
    type of hash function used in keys

key_fmt
    format of the key

flags
    file-system flags (%UBIFS_FLG_BIGLPT, etc)

min_io_size
    minimal input/output unit size

leb_size
    logical eraseblock size in bytes

leb_cnt
    count of LEBs used by file-system

max_leb_cnt
    maximum count of LEBs used by file-system

max_bud_bytes
    maximum amount of data stored in buds

log_lebs
    log size in logical eraseblocks

lpt_lebs
    number of LEBs used for lprops table

orph_lebs
    number of LEBs used for recording orphans

jhead_cnt
    count of journal heads

fanout
    tree fanout (max. number of links per indexing node)

lsave_cnt
    number of LEB numbers in LPT's save table

fmt_version
    UBIFS on-flash format version

default_compr
    default compression algorithm (%UBIFS_COMPR_LZO, etc)

padding1
    reserved for future, zeroes

rp_uid
    reserve pool UID

rp_gid
    reserve pool GID

rp_size
    size of the reserved pool in bytes

time_gran
    time granularity in nanoseconds

uuid
    UUID generated when the file system image was created

ro_compat_version
    UBIFS R/O compatibility version

padding2
    reserved for future, zeroes

.. _`ubifs_mst_node`:

struct ubifs_mst_node
=====================

.. c:type:: struct ubifs_mst_node

    master node.

.. _`ubifs_mst_node.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_mst_node {
        struct ubifs_ch ch;
        __le64 highest_inum;
        __le64 cmt_no;
        __le32 flags;
        __le32 log_lnum;
        __le32 root_lnum;
        __le32 root_offs;
        __le32 root_len;
        __le32 gc_lnum;
        __le32 ihead_lnum;
        __le32 ihead_offs;
        __le64 index_size;
        __le64 total_free;
        __le64 total_dirty;
        __le64 total_used;
        __le64 total_dead;
        __le64 total_dark;
        __le32 lpt_lnum;
        __le32 lpt_offs;
        __le32 nhead_lnum;
        __le32 nhead_offs;
        __le32 ltab_lnum;
        __le32 ltab_offs;
        __le32 lsave_lnum;
        __le32 lsave_offs;
        __le32 lscan_lnum;
        __le32 empty_lebs;
        __le32 idx_lebs;
        __le32 leb_cnt;
        __u8 padding[344];
    }

.. _`ubifs_mst_node.members`:

Members
-------

ch
    common header

highest_inum
    highest inode number in the committed index

cmt_no
    commit number

flags
    various flags (%UBIFS_MST_DIRTY, etc)

log_lnum
    start of the log

root_lnum
    LEB number of the root indexing node

root_offs
    offset within \ ``root_lnum``\ 

root_len
    root indexing node length

gc_lnum
    LEB reserved for garbage collection (%-1 value means the LEB was
    not reserved and should be reserved on mount)

ihead_lnum
    LEB number of index head

ihead_offs
    offset of index head

index_size
    size of index on flash

total_free
    total free space in bytes

total_dirty
    total dirty space in bytes

total_used
    total used space in bytes (includes only data LEBs)

total_dead
    total dead space in bytes (includes only data LEBs)

total_dark
    total dark space in bytes (includes only data LEBs)

lpt_lnum
    LEB number of LPT root nnode

lpt_offs
    offset of LPT root nnode

nhead_lnum
    LEB number of LPT head

nhead_offs
    offset of LPT head

ltab_lnum
    LEB number of LPT's own lprops table

ltab_offs
    offset of LPT's own lprops table

lsave_lnum
    LEB number of LPT's save table (big model only)

lsave_offs
    offset of LPT's save table (big model only)

lscan_lnum
    LEB number of last LPT scan

empty_lebs
    number of empty logical eraseblocks

idx_lebs
    number of indexing logical eraseblocks

leb_cnt
    count of LEBs used by file-system

padding
    reserved for future, zeroes

.. _`ubifs_ref_node`:

struct ubifs_ref_node
=====================

.. c:type:: struct ubifs_ref_node

    logical eraseblock reference node.

.. _`ubifs_ref_node.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_ref_node {
        struct ubifs_ch ch;
        __le32 lnum;
        __le32 offs;
        __le32 jhead;
        __u8 padding[28];
    }

.. _`ubifs_ref_node.members`:

Members
-------

ch
    common header

lnum
    the referred logical eraseblock number

offs
    start offset in the referred LEB

jhead
    journal head number

padding
    reserved for future, zeroes

.. _`ubifs_branch`:

struct ubifs_branch
===================

.. c:type:: struct ubifs_branch

    key/reference/length branch

.. _`ubifs_branch.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_branch {
        __le32 lnum;
        __le32 offs;
        __le32 len;
        __u8 key[];
    }

.. _`ubifs_branch.members`:

Members
-------

lnum
    LEB number of the target node

offs
    offset within \ ``lnum``\ 

len
    target node length

key
    key

.. _`ubifs_idx_node`:

struct ubifs_idx_node
=====================

.. c:type:: struct ubifs_idx_node

    indexing node.

.. _`ubifs_idx_node.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_idx_node {
        struct ubifs_ch ch;
        __le16 child_cnt;
        __le16 level;
        __u8 branches[];
    }

.. _`ubifs_idx_node.members`:

Members
-------

ch
    common header

child_cnt
    number of child index nodes

level
    tree level

branches
    LEB number / offset / length / key branches

.. _`ubifs_cs_node`:

struct ubifs_cs_node
====================

.. c:type:: struct ubifs_cs_node

    commit start node.

.. _`ubifs_cs_node.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_cs_node {
        struct ubifs_ch ch;
        __le64 cmt_no;
    }

.. _`ubifs_cs_node.members`:

Members
-------

ch
    common header

cmt_no
    commit number

.. _`ubifs_orph_node`:

struct ubifs_orph_node
======================

.. c:type:: struct ubifs_orph_node

    orphan node.

.. _`ubifs_orph_node.definition`:

Definition
----------

.. code-block:: c

    struct ubifs_orph_node {
        struct ubifs_ch ch;
        __le64 cmt_no;
        __le64 inos[];
    }

.. _`ubifs_orph_node.members`:

Members
-------

ch
    common header

cmt_no
    commit number (also top bit is set on the last node of the commit)

inos
    inode numbers of orphans

.. This file was automatic generated / don't edit.

