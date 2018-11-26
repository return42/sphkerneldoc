.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/tnc_commit.c

.. _`make_idx_node`:

make_idx_node
=============

.. c:function:: int make_idx_node(struct ubifs_info *c, struct ubifs_idx_node *idx, struct ubifs_znode *znode, int lnum, int offs, int len)

    make an index node for fill-the-gaps method of TNC commit.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param idx:
        buffer in which to place new index node
    :type idx: struct ubifs_idx_node \*

    :param znode:
        znode from which to make new index node
    :type znode: struct ubifs_znode \*

    :param lnum:
        LEB number where new index node will be written
    :type lnum: int

    :param offs:
        offset where new index node will be written
    :type offs: int

    :param len:
        length of new index node
    :type len: int

.. _`fill_gap`:

fill_gap
========

.. c:function:: int fill_gap(struct ubifs_info *c, int lnum, int gap_start, int gap_end, int *dirt)

    make index nodes in gaps in dirty index LEBs.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param lnum:
        LEB number that gap appears in
    :type lnum: int

    :param gap_start:
        offset of start of gap
    :type gap_start: int

    :param gap_end:
        offset of end of gap
    :type gap_end: int

    :param dirt:
        adds dirty space to this
    :type dirt: int \*

.. _`fill_gap.description`:

Description
-----------

This function returns the number of index nodes written into the gap.

.. _`find_old_idx`:

find_old_idx
============

.. c:function:: int find_old_idx(struct ubifs_info *c, int lnum, int offs)

    find an index node obsoleted since the last commit start.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param lnum:
        LEB number of obsoleted index node
    :type lnum: int

    :param offs:
        offset of obsoleted index node
    :type offs: int

.. _`find_old_idx.description`:

Description
-----------

Returns \ ``1``\  if found and \ ``0``\  otherwise.

.. _`is_idx_node_in_use`:

is_idx_node_in_use
==================

.. c:function:: int is_idx_node_in_use(struct ubifs_info *c, union ubifs_key *key, int level, int lnum, int offs)

    determine if an index node can be overwritten.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param key:
        key of index node
    :type key: union ubifs_key \*

    :param level:
        index node level
    :type level: int

    :param lnum:
        LEB number of index node
    :type lnum: int

    :param offs:
        offset of index node
    :type offs: int

.. _`is_idx_node_in_use.description`:

Description
-----------

If \ ``key``\  / \ ``lnum``\  / \ ``offs``\  identify an index node that was not part of the old
index, then this function returns \ ``0``\  (obsolete).  Else if the index node was
part of the old index but is now dirty \ ``1``\  is returned, else if it is clean \ ``2``\ 
is returned. A negative error code is returned on failure.

.. _`layout_leb_in_gaps`:

layout_leb_in_gaps
==================

.. c:function:: int layout_leb_in_gaps(struct ubifs_info *c, int *p)

    layout index nodes using in-the-gaps method.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param p:
        return LEB number here
    :type p: int \*

.. _`layout_leb_in_gaps.description`:

Description
-----------

This function lays out new index nodes for dirty znodes using in-the-gaps
method of TNC commit.
This function merely puts the next znode into the next gap, making no attempt
to try to maximise the number of znodes that fit.
This function returns the number of index nodes written into the gaps, or a
negative error code on failure.

.. _`get_leb_cnt`:

get_leb_cnt
===========

.. c:function:: int get_leb_cnt(struct ubifs_info *c, int cnt)

    calculate the number of empty LEBs needed to commit.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param cnt:
        number of znodes to commit
    :type cnt: int

.. _`get_leb_cnt.description`:

Description
-----------

This function returns the number of empty LEBs needed to commit \ ``cnt``\  znodes
to the current index head.  The number is not exact and may be more than
needed.

.. _`layout_in_gaps`:

layout_in_gaps
==============

.. c:function:: int layout_in_gaps(struct ubifs_info *c, int cnt)

    in-the-gaps method of committing TNC.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param cnt:
        number of dirty znodes to commit.
    :type cnt: int

.. _`layout_in_gaps.description`:

Description
-----------

This function lays out new index nodes for dirty znodes using in-the-gaps
method of TNC commit.

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`layout_in_empty_space`:

layout_in_empty_space
=====================

.. c:function:: int layout_in_empty_space(struct ubifs_info *c)

    layout index nodes in empty space.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`layout_in_empty_space.description`:

Description
-----------

This function lays out new index nodes for dirty znodes using empty LEBs.

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`layout_commit`:

layout_commit
=============

.. c:function:: int layout_commit(struct ubifs_info *c, int no_space, int cnt)

    determine positions of index nodes to commit.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param no_space:
        indicates that insufficient empty LEBs were allocated
    :type no_space: int

    :param cnt:
        number of znodes to commit
    :type cnt: int

.. _`layout_commit.description`:

Description
-----------

Calculate and update the positions of index nodes to commit.  If there were
an insufficient number of empty LEBs allocated, then index nodes are placed
into the gaps created by obsolete index nodes in non-empty index LEBs.  For
this purpose, an obsolete index node is one that was not in the index as at
the end of the last commit.  To write "in-the-gaps" requires that those index
LEBs are updated atomically in-place.

.. _`find_first_dirty`:

find_first_dirty
================

.. c:function:: struct ubifs_znode *find_first_dirty(struct ubifs_znode *znode)

    find first dirty znode.

    :param znode:
        znode to begin searching from
    :type znode: struct ubifs_znode \*

.. _`find_next_dirty`:

find_next_dirty
===============

.. c:function:: struct ubifs_znode *find_next_dirty(struct ubifs_znode *znode)

    find next dirty znode.

    :param znode:
        znode to begin searching from
    :type znode: struct ubifs_znode \*

.. _`get_znodes_to_commit`:

get_znodes_to_commit
====================

.. c:function:: int get_znodes_to_commit(struct ubifs_info *c)

    create list of dirty znodes to commit.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`get_znodes_to_commit.description`:

Description
-----------

This function returns the number of znodes to commit.

.. _`alloc_idx_lebs`:

alloc_idx_lebs
==============

.. c:function:: int alloc_idx_lebs(struct ubifs_info *c, int cnt)

    allocate empty LEBs to be used to commit.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param cnt:
        number of znodes to commit
    :type cnt: int

.. _`alloc_idx_lebs.description`:

Description
-----------

This function returns \ ``-ENOSPC``\  if it cannot allocate a sufficient number of
empty LEBs.  \ ``0``\  is returned on success, otherwise a negative error code
is returned.

.. _`free_unused_idx_lebs`:

free_unused_idx_lebs
====================

.. c:function:: int free_unused_idx_lebs(struct ubifs_info *c)

    free unused LEBs that were allocated for the commit.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`free_unused_idx_lebs.description`:

Description
-----------

It is possible that we allocate more empty LEBs for the commit than we need.
This functions frees the surplus.

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`free_idx_lebs`:

free_idx_lebs
=============

.. c:function:: int free_idx_lebs(struct ubifs_info *c)

    free unused LEBs after commit end.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`free_idx_lebs.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`ubifs_tnc_start_commit`:

ubifs_tnc_start_commit
======================

.. c:function:: int ubifs_tnc_start_commit(struct ubifs_info *c, struct ubifs_zbranch *zroot)

    start TNC commit.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param zroot:
        new index root position is returned here
    :type zroot: struct ubifs_zbranch \*

.. _`ubifs_tnc_start_commit.description`:

Description
-----------

This function prepares the list of indexing nodes to commit and lays out
their positions on flash. If there is not enough free space it uses the
in-gap commit method. Returns zero in case of success and a negative error
code in case of failure.

.. _`write_index`:

write_index
===========

.. c:function:: int write_index(struct ubifs_info *c)

    write index nodes.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`write_index.description`:

Description
-----------

This function writes the index nodes whose positions were laid out in the
layout_in_empty_space function.

.. _`free_obsolete_znodes`:

free_obsolete_znodes
====================

.. c:function:: void free_obsolete_znodes(struct ubifs_info *c)

    free obsolete znodes.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`free_obsolete_znodes.description`:

Description
-----------

At the end of commit end, obsolete znodes are freed.

.. _`return_gap_lebs`:

return_gap_lebs
===============

.. c:function:: int return_gap_lebs(struct ubifs_info *c)

    return LEBs used by the in-gap commit method.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`return_gap_lebs.description`:

Description
-----------

This function clears the "taken" flag for the LEBs which were used by the
"commit in-the-gaps" method.

.. _`ubifs_tnc_end_commit`:

ubifs_tnc_end_commit
====================

.. c:function:: int ubifs_tnc_end_commit(struct ubifs_info *c)

    update the TNC for commit end.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`ubifs_tnc_end_commit.description`:

Description
-----------

Write the dirty znodes.

.. This file was automatic generated / don't edit.

