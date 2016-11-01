.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/find.c

.. _`scan_data`:

struct scan_data
================

.. c:type:: struct scan_data

    data provided to scan callback functions

.. _`scan_data.definition`:

Definition
----------

.. code-block:: c

    struct scan_data {
        int min_space;
        int pick_free;
        int lnum;
        int exclude_index;
    }

.. _`scan_data.members`:

Members
-------

min_space
    minimum number of bytes for which to scan

pick_free
    whether it is OK to scan for empty LEBs

lnum
    LEB number found is returned here

exclude_index
    whether to exclude index LEBs

.. _`valuable`:

valuable
========

.. c:function:: int valuable(struct ubifs_info *c, const struct ubifs_lprops *lprops)

    determine whether LEB properties are valuable.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

    :param const struct ubifs_lprops \*lprops:
        LEB properties

.. _`valuable.description`:

Description
-----------

This function return \ ``1``\  if the LEB properties should be added to the LEB
properties tree in memory. Otherwise \ ``0``\  is returned.

.. _`scan_for_dirty_cb`:

scan_for_dirty_cb
=================

.. c:function:: int scan_for_dirty_cb(struct ubifs_info *c, const struct ubifs_lprops *lprops, int in_tree, struct scan_data *data)

    dirty space scan callback.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

    :param const struct ubifs_lprops \*lprops:
        LEB properties to scan

    :param int in_tree:
        whether the LEB properties are in main memory

    :param struct scan_data \*data:
        information passed to and from the caller of the scan

.. _`scan_for_dirty_cb.description`:

Description
-----------

This function returns a code that indicates whether the scan should continue
(%LPT_SCAN_CONTINUE), whether the LEB properties should be added to the tree
in main memory (%LPT_SCAN_ADD), or whether the scan should stop
(%LPT_SCAN_STOP).

.. _`scan_for_dirty`:

scan_for_dirty
==============

.. c:function:: const struct ubifs_lprops *scan_for_dirty(struct ubifs_info *c, int min_space, int pick_free, int exclude_index)

    find a data LEB with free space.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

    :param int min_space:
        minimum amount free plus dirty space the returned LEB has to
        have

    :param int pick_free:
        if it is OK to return a free or freeable LEB

    :param int exclude_index:
        whether to exclude index LEBs

.. _`scan_for_dirty.description`:

Description
-----------

This function returns a pointer to the LEB properties found or a negative
error code.

.. _`ubifs_find_dirty_leb`:

ubifs_find_dirty_leb
====================

.. c:function:: int ubifs_find_dirty_leb(struct ubifs_info *c, struct ubifs_lprops *ret_lp, int min_space, int pick_free)

    find a dirty LEB for the Garbage Collector.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

    :param struct ubifs_lprops \*ret_lp:
        LEB properties are returned here on exit

    :param int min_space:
        minimum amount free plus dirty space the returned LEB has to
        have

    :param int pick_free:
        controls whether it is OK to pick empty or index LEBs

.. _`ubifs_find_dirty_leb.description`:

Description
-----------

This function tries to find a dirty logical eraseblock which has at least
\ ``min_space``\  free and dirty space. It prefers to take an LEB from the dirty or
dirty index heap, and it falls-back to LPT scanning if the heaps are empty
or do not have an LEB which satisfies the \ ``min_space``\  criteria.

Note, LEBs which have less than dead watermark of free + dirty space are
never picked by this function.

The additional \ ``pick_free``\  argument controls if this function has to return a
free or freeable LEB if one is present. For example, GC must to set it to \ ``1``\ ,
when called from the journal space reservation function, because the
appearance of free space may coincide with the loss of enough dirty space
for GC to succeed anyway.

In contrast, if the Garbage Collector is called from budgeting, it should
just make free space, not return LEBs which are already free or freeable.

In addition \ ``pick_free``\  is set to \ ``2``\  by the recovery process in order to
recover gc_lnum in which case an index LEB must not be returned.

This function returns zero and the LEB properties of found dirty LEB in case
of success, \ ``-ENOSPC``\  if no dirty LEB was found and a negative error code in
case of other failures. The returned LEB is marked as "taken".

.. _`scan_for_free_cb`:

scan_for_free_cb
================

.. c:function:: int scan_for_free_cb(struct ubifs_info *c, const struct ubifs_lprops *lprops, int in_tree, struct scan_data *data)

    free space scan callback.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

    :param const struct ubifs_lprops \*lprops:
        LEB properties to scan

    :param int in_tree:
        whether the LEB properties are in main memory

    :param struct scan_data \*data:
        information passed to and from the caller of the scan

.. _`scan_for_free_cb.description`:

Description
-----------

This function returns a code that indicates whether the scan should continue
(%LPT_SCAN_CONTINUE), whether the LEB properties should be added to the tree
in main memory (%LPT_SCAN_ADD), or whether the scan should stop
(%LPT_SCAN_STOP).

.. _`do_find_free_space`:

do_find_free_space
==================

.. c:function:: const struct ubifs_lprops *do_find_free_space(struct ubifs_info *c, int min_space, int pick_free, int squeeze)

    find a data LEB with free space.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

    :param int min_space:
        minimum amount of free space required

    :param int pick_free:
        whether it is OK to scan for empty LEBs

    :param int squeeze:
        whether to try to find space in a non-empty LEB first

.. _`do_find_free_space.description`:

Description
-----------

This function returns a pointer to the LEB properties found or a negative
error code.

.. _`ubifs_find_free_space`:

ubifs_find_free_space
=====================

.. c:function:: int ubifs_find_free_space(struct ubifs_info *c, int min_space, int *offs, int squeeze)

    find a data LEB with free space.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

    :param int min_space:
        minimum amount of required free space

    :param int \*offs:
        contains offset of where free space starts on exit

    :param int squeeze:
        whether to try to find space in a non-empty LEB first

.. _`ubifs_find_free_space.description`:

Description
-----------

This function looks for an LEB with at least \ ``min_space``\  bytes of free space.
It tries to find an empty LEB if possible. If no empty LEBs are available,
this function searches for a non-empty data LEB. The returned LEB is marked
as "taken".

This function returns found LEB number in case of success, \ ``-ENOSPC``\  if it
failed to find a LEB with \ ``min_space``\  bytes of free space and other a negative
error codes in case of failure.

.. _`scan_for_idx_cb`:

scan_for_idx_cb
===============

.. c:function:: int scan_for_idx_cb(struct ubifs_info *c, const struct ubifs_lprops *lprops, int in_tree, struct scan_data *data)

    callback used by the scan for a free LEB for the index.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

    :param const struct ubifs_lprops \*lprops:
        LEB properties to scan

    :param int in_tree:
        whether the LEB properties are in main memory

    :param struct scan_data \*data:
        information passed to and from the caller of the scan

.. _`scan_for_idx_cb.description`:

Description
-----------

This function returns a code that indicates whether the scan should continue
(%LPT_SCAN_CONTINUE), whether the LEB properties should be added to the tree
in main memory (%LPT_SCAN_ADD), or whether the scan should stop
(%LPT_SCAN_STOP).

.. _`scan_for_leb_for_idx`:

scan_for_leb_for_idx
====================

.. c:function:: const struct ubifs_lprops *scan_for_leb_for_idx(struct ubifs_info *c)

    scan for a free LEB for the index.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

.. _`ubifs_find_free_leb_for_idx`:

ubifs_find_free_leb_for_idx
===========================

.. c:function:: int ubifs_find_free_leb_for_idx(struct ubifs_info *c)

    find a free LEB for the index.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

.. _`ubifs_find_free_leb_for_idx.description`:

Description
-----------

This function looks for a free LEB and returns that LEB number. The returned
LEB is marked as "taken", "index".

Only empty LEBs are allocated. This is for two reasons. First, the commit
calculates the number of LEBs to allocate based on the assumption that they
will be empty. Secondly, free space at the end of an index LEB is not
guaranteed to be empty because it may have been used by the in-the-gaps
method prior to an unclean unmount.

If no LEB is found \ ``-ENOSPC``\  is returned. For other failures another negative
error code is returned.

.. _`ubifs_save_dirty_idx_lnums`:

ubifs_save_dirty_idx_lnums
==========================

.. c:function:: int ubifs_save_dirty_idx_lnums(struct ubifs_info *c)

    save an array of the most dirty index LEB nos.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

.. _`ubifs_save_dirty_idx_lnums.description`:

Description
-----------

This function is called each commit to create an array of LEB numbers of
dirty index LEBs sorted in order of dirty and free space.  This is used by
the in-the-gaps method of TNC commit.

.. _`scan_dirty_idx_cb`:

scan_dirty_idx_cb
=================

.. c:function:: int scan_dirty_idx_cb(struct ubifs_info *c, const struct ubifs_lprops *lprops, int in_tree, struct scan_data *data)

    callback used by the scan for a dirty index LEB.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

    :param const struct ubifs_lprops \*lprops:
        LEB properties to scan

    :param int in_tree:
        whether the LEB properties are in main memory

    :param struct scan_data \*data:
        information passed to and from the caller of the scan

.. _`scan_dirty_idx_cb.description`:

Description
-----------

This function returns a code that indicates whether the scan should continue
(%LPT_SCAN_CONTINUE), whether the LEB properties should be added to the tree
in main memory (%LPT_SCAN_ADD), or whether the scan should stop
(%LPT_SCAN_STOP).

.. _`find_dirty_idx_leb`:

find_dirty_idx_leb
==================

.. c:function:: int find_dirty_idx_leb(struct ubifs_info *c)

    find a dirty index LEB.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

.. _`find_dirty_idx_leb.description`:

Description
-----------

This function returns LEB number upon success and a negative error code upon
failure.  In particular, -ENOSPC is returned if a dirty index LEB is not
found.

Note that this function scans the entire LPT but it is called very rarely.

.. _`get_idx_gc_leb`:

get_idx_gc_leb
==============

.. c:function:: int get_idx_gc_leb(struct ubifs_info *c)

    try to get a LEB number from trivial GC.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

.. _`find_dirtiest_idx_leb`:

find_dirtiest_idx_leb
=====================

.. c:function:: int find_dirtiest_idx_leb(struct ubifs_info *c)

    find dirtiest index LEB from dirtiest array.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

.. _`ubifs_find_dirty_idx_leb`:

ubifs_find_dirty_idx_leb
========================

.. c:function:: int ubifs_find_dirty_idx_leb(struct ubifs_info *c)

    try to find dirtiest index LEB as at last commit.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

.. _`ubifs_find_dirty_idx_leb.description`:

Description
-----------

This function attempts to find an untaken index LEB with the most free and
dirty space that can be used without overwriting index nodes that were in the
last index committed.

.. This file was automatic generated / don't edit.

