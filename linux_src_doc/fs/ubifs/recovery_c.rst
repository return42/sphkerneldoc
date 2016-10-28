.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/recovery.c

.. _`is_empty`:

is_empty
========

.. c:function:: int is_empty(void *buf, int len)

    determine whether a buffer is empty (contains all 0xff).

    :param void \*buf:
        buffer to clean

    :param int len:
        length of buffer

.. _`is_empty.description`:

Description
-----------

This function returns \ ``1``\  if the buffer is empty (contains all 0xff) otherwise
\ ``0``\  is returned.

.. _`first_non_ff`:

first_non_ff
============

.. c:function:: int first_non_ff(void *buf, int len)

    find offset of the first non-0xff byte.

    :param void \*buf:
        buffer to search in

    :param int len:
        length of buffer

.. _`first_non_ff.description`:

Description
-----------

This function returns offset of the first non-0xff byte in \ ``buf``\  or \ ``-1``\  if
the buffer contains only 0xff bytes.

.. _`get_master_node`:

get_master_node
===============

.. c:function:: int get_master_node(const struct ubifs_info *c, int lnum, void **pbuf, struct ubifs_mst_node **mst, void **cor)

    get the last valid master node allowing for corruption.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        LEB number

    :param void \*\*pbuf:
        buffer containing the LEB read, is returned here

    :param struct ubifs_mst_node \*\*mst:
        master node, if found, is returned here

    :param void \*\*cor:
        corruption, if found, is returned here

.. _`get_master_node.description`:

Description
-----------

This function allocates a buffer, reads the LEB into it, and finds and
returns the last valid master node allowing for one area of corruption.
The corrupt area, if there is one, must be consistent with the assumption
that it is the result of an unclean unmount while the master node was being
written. Under those circumstances, it is valid to use the previously written
master node.

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`write_rcvrd_mst_node`:

write_rcvrd_mst_node
====================

.. c:function:: int write_rcvrd_mst_node(struct ubifs_info *c, struct ubifs_mst_node *mst)

    write recovered master node.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_mst_node \*mst:
        master node

.. _`write_rcvrd_mst_node.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`ubifs_recover_master_node`:

ubifs_recover_master_node
=========================

.. c:function:: int ubifs_recover_master_node(struct ubifs_info *c)

    recover the master node.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_recover_master_node.description`:

Description
-----------

This function recovers the master node from corruption that may occur due to
an unclean unmount.

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`ubifs_write_rcvrd_mst_node`:

ubifs_write_rcvrd_mst_node
==========================

.. c:function:: int ubifs_write_rcvrd_mst_node(struct ubifs_info *c)

    write the recovered master node.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_write_rcvrd_mst_node.description`:

Description
-----------

This function writes the master node that was recovered during mounting in
read-only mode and must now be written because we are remounting rw.

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`is_last_write`:

is_last_write
=============

.. c:function:: int is_last_write(const struct ubifs_info *c, void *buf, int offs)

    determine if an offset was in the last write to a LEB.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param void \*buf:
        buffer to check

    :param int offs:
        offset to check

.. _`is_last_write.description`:

Description
-----------

This function returns \ ``1``\  if \ ``offs``\  was in the last write to the LEB whose data
is in \ ``buf``\ , otherwise \ ``0``\  is returned. The determination is made by checking
for subsequent empty space starting from the next \ ``c``\ ->max_write_size
boundary.

.. _`clean_buf`:

clean_buf
=========

.. c:function:: void clean_buf(const struct ubifs_info *c, void **buf, int lnum, int *offs, int *len)

    clean the data from an LEB sitting in a buffer.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param void \*\*buf:
        buffer to clean

    :param int lnum:
        LEB number to clean

    :param int \*offs:
        offset from which to clean

    :param int \*len:
        length of buffer

.. _`clean_buf.description`:

Description
-----------

This function pads up to the next min_io_size boundary (if there is one) and
sets empty space to all 0xff. \ ``buf``\ , \ ``offs``\  and \ ``len``\  are updated to the next
\ ``c``\ ->min_io_size boundary.

.. _`no_more_nodes`:

no_more_nodes
=============

.. c:function:: int no_more_nodes(const struct ubifs_info *c, void *buf, int len, int lnum, int offs)

    determine if there are no more nodes in a buffer.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param void \*buf:
        buffer to check

    :param int len:
        length of buffer

    :param int lnum:
        LEB number of the LEB from which \ ``buf``\  was read

    :param int offs:
        offset from which \ ``buf``\  was read

.. _`no_more_nodes.description`:

Description
-----------

This function ensures that the corrupted node at \ ``offs``\  is the last thing
written to a LEB. This function returns \ ``1``\  if more data is not found and
\ ``0``\  if more data is found.

.. _`fix_unclean_leb`:

fix_unclean_leb
===============

.. c:function:: int fix_unclean_leb(struct ubifs_info *c, struct ubifs_scan_leb *sleb, int start)

    fix an unclean LEB.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_scan_leb \*sleb:
        scanned LEB information

    :param int start:
        offset where scan started

.. _`drop_last_group`:

drop_last_group
===============

.. c:function:: void drop_last_group(struct ubifs_scan_leb *sleb, int *offs)

    drop the last group of nodes.

    :param struct ubifs_scan_leb \*sleb:
        scanned LEB information

    :param int \*offs:
        offset of dropped nodes is returned here

.. _`drop_last_group.description`:

Description
-----------

This is a helper function for '\ :c:func:`ubifs_recover_leb`\ ' which drops the last
group of nodes of the scanned LEB.

.. _`drop_last_node`:

drop_last_node
==============

.. c:function:: void drop_last_node(struct ubifs_scan_leb *sleb, int *offs)

    drop the last node.

    :param struct ubifs_scan_leb \*sleb:
        scanned LEB information

    :param int \*offs:
        offset of dropped nodes is returned here

.. _`drop_last_node.description`:

Description
-----------

This is a helper function for '\ :c:func:`ubifs_recover_leb`\ ' which drops the last
node of the scanned LEB.

.. _`ubifs_recover_leb`:

ubifs_recover_leb
=================

.. c:function:: struct ubifs_scan_leb *ubifs_recover_leb(struct ubifs_info *c, int lnum, int offs, void *sbuf, int jhead)

    scan and recover a LEB.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        LEB number

    :param int offs:
        offset

    :param void \*sbuf:
        LEB-sized buffer to use

    :param int jhead:
        journal head number this LEB belongs to (\ ``-1``\  if the LEB does not
        belong to any journal head)

.. _`ubifs_recover_leb.description`:

Description
-----------

This function does a scan of a LEB, but caters for errors that might have
been caused by the unclean unmount from which we are attempting to recover.
Returns the scanned information on success and a negative error code on
failure.

.. _`get_cs_sqnum`:

get_cs_sqnum
============

.. c:function:: int get_cs_sqnum(struct ubifs_info *c, int lnum, int offs, unsigned long long *cs_sqnum)

    get commit start sequence number.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        LEB number of commit start node

    :param int offs:
        offset of commit start node

    :param unsigned long long \*cs_sqnum:
        commit start sequence number is returned here

.. _`get_cs_sqnum.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`ubifs_recover_log_leb`:

ubifs_recover_log_leb
=====================

.. c:function:: struct ubifs_scan_leb *ubifs_recover_log_leb(struct ubifs_info *c, int lnum, int offs, void *sbuf)

    scan and recover a log LEB.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        LEB number

    :param int offs:
        offset

    :param void \*sbuf:
        LEB-sized buffer to use

.. _`ubifs_recover_log_leb.description`:

Description
-----------

This function does a scan of a LEB, but caters for errors that might have
been caused by unclean reboots from which we are attempting to recover
(assume that only the last log LEB can be corrupted by an unclean reboot).

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`recover_head`:

recover_head
============

.. c:function:: int recover_head(struct ubifs_info *c, int lnum, int offs, void *sbuf)

    recover a head.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        LEB number of head to recover

    :param int offs:
        offset of head to recover

    :param void \*sbuf:
        LEB-sized buffer to use

.. _`recover_head.description`:

Description
-----------

This function ensures that there is no data on the flash at a head location.

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`ubifs_recover_inl_heads`:

ubifs_recover_inl_heads
=======================

.. c:function:: int ubifs_recover_inl_heads(struct ubifs_info *c, void *sbuf)

    recover index and LPT heads.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param void \*sbuf:
        LEB-sized buffer to use

.. _`ubifs_recover_inl_heads.description`:

Description
-----------

This function ensures that there is no data on the flash at the index and
LPT head locations.

This deals with the recovery of a half-completed journal commit. UBIFS is
careful never to overwrite the last version of the index or the LPT. Because
the index and LPT are wandering trees, data from a half-completed commit will
not be referenced anywhere in UBIFS. The data will be either in LEBs that are
assumed to be empty and will be unmapped anyway before use, or in the index
and LPT heads.

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`clean_an_unclean_leb`:

clean_an_unclean_leb
====================

.. c:function:: int clean_an_unclean_leb(struct ubifs_info *c, struct ubifs_unclean_leb *ucleb, void *sbuf)

    read and write a LEB to remove corruption.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_unclean_leb \*ucleb:
        unclean LEB information

    :param void \*sbuf:
        LEB-sized buffer to use

.. _`clean_an_unclean_leb.description`:

Description
-----------

This function reads a LEB up to a point pre-determined by the mount recovery,
checks the nodes, and writes the result back to the flash, thereby cleaning
off any following corruption, or non-fatal ECC errors.

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`ubifs_clean_lebs`:

ubifs_clean_lebs
================

.. c:function:: int ubifs_clean_lebs(struct ubifs_info *c, void *sbuf)

    clean LEBs recovered during read-only mount.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param void \*sbuf:
        LEB-sized buffer to use

.. _`ubifs_clean_lebs.description`:

Description
-----------

This function cleans a LEB identified during recovery that needs to be
written but was not because UBIFS was mounted read-only. This happens when
remounting to read-write mode.

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`grab_empty_leb`:

grab_empty_leb
==============

.. c:function:: int grab_empty_leb(struct ubifs_info *c)

    grab an empty LEB to use as GC LEB and run commit.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`grab_empty_leb.description`:

Description
-----------

This is a helper function for '\ :c:func:`ubifs_rcvry_gc_commit`\ ' which grabs an empty
LEB to be used as GC LEB (\ ``c``\ ->gc_lnum), and then runs the commit. Returns
zero in case of success and a negative error code in case of failure.

.. _`ubifs_rcvry_gc_commit`:

ubifs_rcvry_gc_commit
=====================

.. c:function:: int ubifs_rcvry_gc_commit(struct ubifs_info *c)

    recover the GC LEB number and run the commit.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_rcvry_gc_commit.description`:

Description
-----------

Out-of-place garbage collection requires always one empty LEB with which to
start garbage collection. The LEB number is recorded in c->gc_lnum and is
written to the master node on unmounting. In the case of an unclean unmount
the value of gc_lnum recorded in the master node is out of date and cannot
be used. Instead, recovery must allocate an empty LEB for this purpose.
However, there may not be enough empty space, in which case it must be
possible to GC the dirtiest LEB into the GC head LEB.

This function also runs the commit which causes the TNC updates from
size-recovery and orphans to be written to the flash. That is important to
ensure correct replay order for subsequent mounts.

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`size_entry`:

struct size_entry
=================

.. c:type:: struct size_entry

    inode size information for recovery.

.. _`size_entry.definition`:

Definition
----------

.. code-block:: c

    struct size_entry {
        struct rb_node rb;
        ino_t inum;
        loff_t i_size;
        loff_t d_size;
        int exists;
        struct inode *inode;
    }

.. _`size_entry.members`:

Members
-------

rb
    link in the RB-tree of sizes

inum
    inode number

i_size
    size on inode

d_size
    maximum size based on data nodes

exists
    indicates whether the inode exists

inode
    inode if pinned in memory awaiting rw mode to fix it

.. _`add_ino`:

add_ino
=======

.. c:function:: int add_ino(struct ubifs_info *c, ino_t inum, loff_t i_size, loff_t d_size, int exists)

    add an entry to the size tree.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param ino_t inum:
        inode number

    :param loff_t i_size:
        size on inode

    :param loff_t d_size:
        maximum size based on data nodes

    :param int exists:
        indicates whether the inode exists

.. _`find_ino`:

find_ino
========

.. c:function:: struct size_entry *find_ino(struct ubifs_info *c, ino_t inum)

    find an entry on the size tree.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param ino_t inum:
        inode number

.. _`remove_ino`:

remove_ino
==========

.. c:function:: void remove_ino(struct ubifs_info *c, ino_t inum)

    remove an entry from the size tree.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param ino_t inum:
        inode number

.. _`ubifs_destroy_size_tree`:

ubifs_destroy_size_tree
=======================

.. c:function:: void ubifs_destroy_size_tree(struct ubifs_info *c)

    free resources related to the size tree.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_recover_size_accum`:

ubifs_recover_size_accum
========================

.. c:function:: int ubifs_recover_size_accum(struct ubifs_info *c, union ubifs_key *key, int deletion, loff_t new_size)

    accumulate inode sizes for recovery.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param union ubifs_key \*key:
        node key

    :param int deletion:
        node is for a deletion

    :param loff_t new_size:
        inode size

.. _`ubifs_recover_size_accum.this-function-has-two-purposes`:

This function has two purposes
------------------------------

1) to ensure there are no data nodes that fall outside the inode size
2) to ensure there are no data nodes for inodes that do not exist
To accomplish those purposes, a rb-tree is constructed containing an entry
for each inode number in the journal that has not been deleted, and recording
the size from the inode node, the maximum size of any data node (also altered
by truncations) and a flag indicating a inode number for which no inode node
was present in the journal.

Note that there is still the possibility that there are data nodes that have
been committed that are beyond the inode size, however the only way to find
them would be to scan the entire index. Alternatively, some provision could
be made to record the size of inodes at the start of commit, which would seem
very cumbersome for a scenario that is quite unlikely and the only negative
consequence of which is wasted space.

This functions returns \ ``0``\  on success and a negative error code on failure.

.. _`fix_size_in_place`:

fix_size_in_place
=================

.. c:function:: int fix_size_in_place(struct ubifs_info *c, struct size_entry *e)

    fix inode size in place on flash.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct size_entry \*e:
        inode size information for recovery

.. _`ubifs_recover_size`:

ubifs_recover_size
==================

.. c:function:: int ubifs_recover_size(struct ubifs_info *c)

    recover inode size.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_recover_size.description`:

Description
-----------

This function attempts to fix inode size discrepancies identified by the
'\ :c:func:`ubifs_recover_size_accum`\ ' function.

This functions returns \ ``0``\  on success and a negative error code on failure.

.. This file was automatic generated / don't edit.

