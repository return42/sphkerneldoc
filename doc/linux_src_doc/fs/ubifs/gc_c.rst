.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/gc.c

.. _`switch_gc_head`:

switch_gc_head
==============

.. c:function:: int switch_gc_head(struct ubifs_info *c)

    switch the garbage collection journal head.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`switch_gc_head.description`:

Description
-----------

This function switch the GC head to the next LEB which is reserved in
\ ``c``\ ->gc_lnum. Returns \ ``0``\  in case of success, \ ``-EAGAIN``\  if commit is required,
and other negative error code in case of failures.

.. _`data_nodes_cmp`:

data_nodes_cmp
==============

.. c:function:: int data_nodes_cmp(void *priv, struct list_head *a, struct list_head *b)

    compare 2 data nodes.

    :param void \*priv:
        UBIFS file-system description object

    :param struct list_head \*a:
        second data node

    :param struct list_head \*b:
        *undescribed*

.. _`data_nodes_cmp.description`:

Description
-----------

This function compares data nodes \ ``a``\  and \ ``b``\ . Returns \ ``1``\  if \ ``a``\  has greater
inode or block number, and \ ``-1``\  otherwise.

.. _`sort_nodes`:

sort_nodes
==========

.. c:function:: int sort_nodes(struct ubifs_info *c, struct ubifs_scan_leb *sleb, struct list_head *nondata, int *min)

    sort nodes for GC.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_scan_leb \*sleb:
        describes nodes to sort and contains the result on exit

    :param struct list_head \*nondata:
        contains non-data nodes on exit

    :param int \*min:
        minimum node size is returned here

.. _`sort_nodes.description`:

Description
-----------

This function sorts the list of inodes to garbage collect. First of all, it
kills obsolete nodes and separates data and non-data nodes to the
\ ``sleb``\ ->nodes and \ ``nondata``\  lists correspondingly.

Data nodes are then sorted in block number order - this is important for
bulk-read; data nodes with lower inode number go before data nodes with
higher inode number, and data nodes with lower block number go before data
nodes with higher block number;

Non-data nodes are sorted as follows.
o First go inode nodes - they are sorted in descending length order.
o Then go directory entry nodes - they are sorted in hash order, which
should supposedly optimize '\ :c:func:`readdir`\ '. Direntry nodes with lower parent
inode number go before direntry nodes with higher parent inode number,
and direntry nodes with lower name hash values go before direntry nodes
with higher name hash values.

This function returns zero in case of success and a negative error code in
case of failure.

.. _`move_node`:

move_node
=========

.. c:function:: int move_node(struct ubifs_info *c, struct ubifs_scan_leb *sleb, struct ubifs_scan_node *snod, struct ubifs_wbuf *wbuf)

    move a node.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_scan_leb \*sleb:
        describes the LEB to move nodes from

    :param struct ubifs_scan_node \*snod:
        the mode to move

    :param struct ubifs_wbuf \*wbuf:
        write-buffer to move node to

.. _`move_node.description`:

Description
-----------

This function moves node \ ``snod``\  to \ ``wbuf``\ , changes TNC correspondingly, and
destroys \ ``snod``\ . Returns zero in case of success and a negative error code in
case of failure.

.. _`move_nodes`:

move_nodes
==========

.. c:function:: int move_nodes(struct ubifs_info *c, struct ubifs_scan_leb *sleb)

    move nodes.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_scan_leb \*sleb:
        describes the LEB to move nodes from

.. _`move_nodes.description`:

Description
-----------

This function moves valid nodes from data LEB described by \ ``sleb``\  to the GC
journal head. This function returns zero in case of success, \ ``-EAGAIN``\  if
commit is required, and other negative error codes in case of other
failures.

.. _`gc_sync_wbufs`:

gc_sync_wbufs
=============

.. c:function:: int gc_sync_wbufs(struct ubifs_info *c)

    sync write-buffers for GC.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`gc_sync_wbufs.description`:

Description
-----------

We must guarantee that obsoleting nodes are on flash. Unfortunately they may
be in a write-buffer instead. That is, a node could be written to a
write-buffer, obsoleting another node in a LEB that is GC'd. If that LEB is
erased before the write-buffer is sync'd and then there is an unclean
unmount, then an existing node is lost. To avoid this, we sync all
write-buffers.

This function returns \ ``0``\  on success or a negative error code on failure.

.. _`ubifs_garbage_collect_leb`:

ubifs_garbage_collect_leb
=========================

.. c:function:: int ubifs_garbage_collect_leb(struct ubifs_info *c, struct ubifs_lprops *lp)

    garbage-collect a logical eraseblock.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_lprops \*lp:
        describes the LEB to garbage collect

.. _`ubifs_garbage_collect_leb.description`:

Description
-----------

This function garbage-collects an LEB and returns one of the \ ``LEB_FREED``\ ,
\ ``LEB_RETAINED``\ , etc positive codes in case of success, \ ``-EAGAIN``\  if commit is
required, and other negative error codes in case of failures.

.. _`ubifs_garbage_collect`:

ubifs_garbage_collect
=====================

.. c:function:: int ubifs_garbage_collect(struct ubifs_info *c, int anyway)

    UBIFS garbage collector.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int anyway:
        do GC even if there are free LEBs

.. _`ubifs_garbage_collect.description`:

Description
-----------

This function does out-of-place garbage collection. The return codes are:
o positive LEB number if the LEB has been freed and may be used;
o \ ``-EAGAIN``\  if the caller has to run commit;
o \ ``-ENOSPC``\  if GC failed to make any progress;
o other negative error codes in case of other errors.

Garbage collector writes data to the journal when GC'ing data LEBs, and just
marking indexing nodes dirty when GC'ing indexing LEBs. Thus, at some point
commit may be required. But commit cannot be run from inside GC, because the
caller might be holding the commit lock, so \ ``-EAGAIN``\  is returned instead;
And this error code means that the caller has to run commit, and re-run GC
if there is still no free space.

There are many reasons why this function may return \ ``-EAGAIN``\ :
o the log is full and there is no space to write an LEB reference for
\ ``c``\ ->gc_lnum;
o the journal is too large and exceeds size limitations;
o GC moved indexing LEBs, but they can be used only after the commit;
o the shrinker fails to find clean znodes to free and requests the commit;
o etc.

Note, if the file-system is close to be full, this function may return
\ ``-EAGAIN``\  infinitely, so the caller has to limit amount of re-invocations of
the function. E.g., this happens if the limits on the journal size are too
tough and GC writes too much to the journal before an LEB is freed. This
might also mean that the journal is too large, and the TNC becomes to big,
so that the shrinker is constantly called, finds not clean znodes to free,
and requests commit. Well, this may also happen if the journal is all right,
but another kernel process consumes too much memory. Anyway, infinite
\ ``-EAGAIN``\  may happen, but in some extreme/misconfiguration cases.

.. _`ubifs_gc_start_commit`:

ubifs_gc_start_commit
=====================

.. c:function:: int ubifs_gc_start_commit(struct ubifs_info *c)

    garbage collection at start of commit.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_gc_start_commit.description`:

Description
-----------

If a LEB has only dirty and free space, then we may safely unmap it and make
it free.  Note, we cannot do this with indexing LEBs because dirty space may
correspond index nodes that are required for recovery.  In that case, the
LEB cannot be unmapped until after the next commit.

This function returns \ ``0``\  upon success and a negative error code upon failure.

.. _`ubifs_gc_end_commit`:

ubifs_gc_end_commit
===================

.. c:function:: int ubifs_gc_end_commit(struct ubifs_info *c)

    garbage collection at end of commit.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_gc_end_commit.description`:

Description
-----------

This function completes out-of-place garbage collection of index LEBs.

.. _`ubifs_destroy_idx_gc`:

ubifs_destroy_idx_gc
====================

.. c:function:: void ubifs_destroy_idx_gc(struct ubifs_info *c)

    destroy idx_gc list.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_destroy_idx_gc.description`:

Description
-----------

This function destroys the \ ``c``\ ->idx_gc list. It is called when unmounting
so locks are not needed. Returns zero in case of success and a negative
error code in case of failure.

.. _`ubifs_get_idx_gc_leb`:

ubifs_get_idx_gc_leb
====================

.. c:function:: int ubifs_get_idx_gc_leb(struct ubifs_info *c)

    get a LEB from GC'd index LEB list.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_get_idx_gc_leb.description`:

Description
-----------

Called during start commit so locks are not needed.

.. This file was automatic generated / don't edit.

