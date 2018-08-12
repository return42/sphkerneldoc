.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/lpt_commit.c

.. _`first_dirty_cnode`:

first_dirty_cnode
=================

.. c:function:: struct ubifs_cnode *first_dirty_cnode(struct ubifs_nnode *nnode)

    find first dirty cnode.

    :param struct ubifs_nnode \*nnode:
        nnode at which to start

.. _`first_dirty_cnode.description`:

Description
-----------

This function returns the first dirty cnode or \ ``NULL``\  if there is not one.

.. _`next_dirty_cnode`:

next_dirty_cnode
================

.. c:function:: struct ubifs_cnode *next_dirty_cnode(struct ubifs_cnode *cnode)

    find next dirty cnode.

    :param struct ubifs_cnode \*cnode:
        cnode from which to begin searching

.. _`next_dirty_cnode.description`:

Description
-----------

This function returns the next dirty cnode or \ ``NULL``\  if there is not one.

.. _`get_cnodes_to_commit`:

get_cnodes_to_commit
====================

.. c:function:: int get_cnodes_to_commit(struct ubifs_info *c)

    create list of dirty cnodes to commit.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`get_cnodes_to_commit.description`:

Description
-----------

This function returns the number of cnodes to commit.

.. _`upd_ltab`:

upd_ltab
========

.. c:function:: void upd_ltab(struct ubifs_info *c, int lnum, int free, int dirty)

    update LPT LEB properties.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        LEB number

    :param int free:
        amount of free space

    :param int dirty:
        amount of dirty space to add

.. _`alloc_lpt_leb`:

alloc_lpt_leb
=============

.. c:function:: int alloc_lpt_leb(struct ubifs_info *c, int *lnum)

    allocate an LPT LEB that is empty.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int \*lnum:
        LEB number is passed and returned here

.. _`alloc_lpt_leb.description`:

Description
-----------

This function finds the next empty LEB in the ltab starting from \ ``lnum``\ . If a
an empty LEB is found it is returned in \ ``lnum``\  and the function returns \ ``0``\ .
Otherwise the function returns -ENOSPC.  Note however, that LPT is designed
never to run out of space.

.. _`layout_cnodes`:

layout_cnodes
=============

.. c:function:: int layout_cnodes(struct ubifs_info *c)

    layout cnodes for commit.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`layout_cnodes.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`realloc_lpt_leb`:

realloc_lpt_leb
===============

.. c:function:: int realloc_lpt_leb(struct ubifs_info *c, int *lnum)

    allocate an LPT LEB that is empty.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int \*lnum:
        LEB number is passed and returned here

.. _`realloc_lpt_leb.description`:

Description
-----------

This function duplicates exactly the results of the function alloc_lpt_leb.
It is used during end commit to reallocate the same LEB numbers that were
allocated by alloc_lpt_leb during start commit.

This function finds the next LEB that was allocated by the alloc_lpt_leb
function starting from \ ``lnum``\ . If a LEB is found it is returned in \ ``lnum``\  and
the function returns \ ``0``\ . Otherwise the function returns -ENOSPC.
Note however, that LPT is designed never to run out of space.

.. _`write_cnodes`:

write_cnodes
============

.. c:function:: int write_cnodes(struct ubifs_info *c)

    write cnodes for commit.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`write_cnodes.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`next_pnode_to_dirty`:

next_pnode_to_dirty
===================

.. c:function:: struct ubifs_pnode *next_pnode_to_dirty(struct ubifs_info *c, struct ubifs_pnode *pnode)

    find next pnode to dirty.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_pnode \*pnode:
        pnode

.. _`next_pnode_to_dirty.description`:

Description
-----------

This function returns the next pnode to dirty or \ ``NULL``\  if there are no more
pnodes.  Note that pnodes that have never been written (lnum == 0) are
skipped.

.. _`pnode_lookup`:

pnode_lookup
============

.. c:function:: struct ubifs_pnode *pnode_lookup(struct ubifs_info *c, int i)

    lookup a pnode in the LPT.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int i:
        pnode number (0 to (main_lebs - 1) / UBIFS_LPT_FANOUT))

.. _`pnode_lookup.description`:

Description
-----------

This function returns a pointer to the pnode on success or a negative
error code on failure.

.. _`add_pnode_dirt`:

add_pnode_dirt
==============

.. c:function:: void add_pnode_dirt(struct ubifs_info *c, struct ubifs_pnode *pnode)

    add dirty space to LPT LEB properties.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_pnode \*pnode:
        pnode for which to add dirt

.. _`do_make_pnode_dirty`:

do_make_pnode_dirty
===================

.. c:function:: void do_make_pnode_dirty(struct ubifs_info *c, struct ubifs_pnode *pnode)

    mark a pnode dirty.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_pnode \*pnode:
        pnode to mark dirty

.. _`make_tree_dirty`:

make_tree_dirty
===============

.. c:function:: int make_tree_dirty(struct ubifs_info *c)

    mark the entire LEB properties tree dirty.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`make_tree_dirty.description`:

Description
-----------

This function is used by the "small" LPT model to cause the entire LEB
properties tree to be written.  The "small" LPT model does not use LPT
garbage collection because it is more efficient to write the entire tree
(because it is small).

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`need_write_all`:

need_write_all
==============

.. c:function:: int need_write_all(struct ubifs_info *c)

    determine if the LPT area is running out of free space.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`need_write_all.description`:

Description
-----------

This function returns \ ``1``\  if the LPT area is running out of free space and \ ``0``\ 
if it is not.

.. _`lpt_tgc_start`:

lpt_tgc_start
=============

.. c:function:: void lpt_tgc_start(struct ubifs_info *c)

    start trivial garbage collection of LPT LEBs.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`lpt_tgc_start.description`:

Description
-----------

LPT trivial garbage collection is where a LPT LEB contains only dirty and
free space and so may be reused as soon as the next commit is completed.
This function is called during start commit to mark LPT LEBs for trivial GC.

.. _`lpt_tgc_end`:

lpt_tgc_end
===========

.. c:function:: int lpt_tgc_end(struct ubifs_info *c)

    end trivial garbage collection of LPT LEBs.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`lpt_tgc_end.description`:

Description
-----------

LPT trivial garbage collection is where a LPT LEB contains only dirty and
free space and so may be reused as soon as the next commit is completed.
This function is called after the commit is completed (master node has been
written) and un-maps LPT LEBs that were marked for trivial GC.

.. _`populate_lsave`:

populate_lsave
==============

.. c:function:: void populate_lsave(struct ubifs_info *c)

    fill the lsave array with important LEB numbers.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

.. _`populate_lsave.description`:

Description
-----------

This function is only called for the "big" model. It records a small number
of LEB numbers of important LEBs.  Important LEBs are ones that are (from
most important to least important): empty, freeable, freeable index, dirty
index, dirty or free. Upon mount, we read this list of LEB numbers and bring
their pnodes into memory.  That will stop us from having to scan the LPT
straight away. For the "small" model we assume that scanning the LPT is no
big deal.

.. _`nnode_lookup`:

nnode_lookup
============

.. c:function:: struct ubifs_nnode *nnode_lookup(struct ubifs_info *c, int i)

    lookup a nnode in the LPT.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int i:
        nnode number

.. _`nnode_lookup.description`:

Description
-----------

This function returns a pointer to the nnode on success or a negative
error code on failure.

.. _`make_nnode_dirty`:

make_nnode_dirty
================

.. c:function:: int make_nnode_dirty(struct ubifs_info *c, int node_num, int lnum, int offs)

    find a nnode and, if found, make it dirty.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int node_num:
        nnode number of nnode to make dirty

    :param int lnum:
        LEB number where nnode was written

    :param int offs:
        offset where nnode was written

.. _`make_nnode_dirty.description`:

Description
-----------

This function is used by LPT garbage collection.  LPT garbage collection is
used only for the "big" LPT model (c->big_lpt == 1).  Garbage collection
simply involves marking all the nodes in the LEB being garbage-collected as
dirty.  The dirty nodes are written next commit, after which the LEB is free
to be reused.

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`make_pnode_dirty`:

make_pnode_dirty
================

.. c:function:: int make_pnode_dirty(struct ubifs_info *c, int node_num, int lnum, int offs)

    find a pnode and, if found, make it dirty.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int node_num:
        pnode number of pnode to make dirty

    :param int lnum:
        LEB number where pnode was written

    :param int offs:
        offset where pnode was written

.. _`make_pnode_dirty.description`:

Description
-----------

This function is used by LPT garbage collection.  LPT garbage collection is
used only for the "big" LPT model (c->big_lpt == 1).  Garbage collection
simply involves marking all the nodes in the LEB being garbage-collected as
dirty.  The dirty nodes are written next commit, after which the LEB is free
to be reused.

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`make_ltab_dirty`:

make_ltab_dirty
===============

.. c:function:: int make_ltab_dirty(struct ubifs_info *c, int lnum, int offs)

    make ltab node dirty.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        LEB number where ltab was written

    :param int offs:
        offset where ltab was written

.. _`make_ltab_dirty.description`:

Description
-----------

This function is used by LPT garbage collection.  LPT garbage collection is
used only for the "big" LPT model (c->big_lpt == 1).  Garbage collection
simply involves marking all the nodes in the LEB being garbage-collected as
dirty.  The dirty nodes are written next commit, after which the LEB is free
to be reused.

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`make_lsave_dirty`:

make_lsave_dirty
================

.. c:function:: int make_lsave_dirty(struct ubifs_info *c, int lnum, int offs)

    make lsave node dirty.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        LEB number where lsave was written

    :param int offs:
        offset where lsave was written

.. _`make_lsave_dirty.description`:

Description
-----------

This function is used by LPT garbage collection.  LPT garbage collection is
used only for the "big" LPT model (c->big_lpt == 1).  Garbage collection
simply involves marking all the nodes in the LEB being garbage-collected as
dirty.  The dirty nodes are written next commit, after which the LEB is free
to be reused.

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`make_node_dirty`:

make_node_dirty
===============

.. c:function:: int make_node_dirty(struct ubifs_info *c, int node_type, int node_num, int lnum, int offs)

    make node dirty.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int node_type:
        LPT node type

    :param int node_num:
        node number

    :param int lnum:
        LEB number where node was written

    :param int offs:
        offset where node was written

.. _`make_node_dirty.description`:

Description
-----------

This function is used by LPT garbage collection.  LPT garbage collection is
used only for the "big" LPT model (c->big_lpt == 1).  Garbage collection
simply involves marking all the nodes in the LEB being garbage-collected as
dirty.  The dirty nodes are written next commit, after which the LEB is free
to be reused.

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`get_lpt_node_len`:

get_lpt_node_len
================

.. c:function:: int get_lpt_node_len(const struct ubifs_info *c, int node_type)

    return the length of a node based on its type.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param int node_type:
        LPT node type

.. _`get_pad_len`:

get_pad_len
===========

.. c:function:: int get_pad_len(const struct ubifs_info *c, uint8_t *buf, int len)

    return the length of padding in a buffer.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param uint8_t \*buf:
        buffer

    :param int len:
        length of buffer

.. _`get_lpt_node_type`:

get_lpt_node_type
=================

.. c:function:: int get_lpt_node_type(const struct ubifs_info *c, uint8_t *buf, int *node_num)

    return type (and node number) of a node in a buffer.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param uint8_t \*buf:
        buffer

    :param int \*node_num:
        node number is returned here

.. _`is_a_node`:

is_a_node
=========

.. c:function:: int is_a_node(const struct ubifs_info *c, uint8_t *buf, int len)

    determine if a buffer contains a node.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param uint8_t \*buf:
        buffer

    :param int len:
        length of buffer

.. _`is_a_node.description`:

Description
-----------

This function returns \ ``1``\  if the buffer contains a node or \ ``0``\  if it does not.

.. _`lpt_gc_lnum`:

lpt_gc_lnum
===========

.. c:function:: int lpt_gc_lnum(struct ubifs_info *c, int lnum)

    garbage collect a LPT LEB.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        LEB number to garbage collect

.. _`lpt_gc_lnum.description`:

Description
-----------

LPT garbage collection is used only for the "big" LPT model
(c->big_lpt == 1).  Garbage collection simply involves marking all the nodes
in the LEB being garbage-collected as dirty.  The dirty nodes are written
next commit, after which the LEB is free to be reused.

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`lpt_gc`:

lpt_gc
======

.. c:function:: int lpt_gc(struct ubifs_info *c)

    LPT garbage collection.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`lpt_gc.description`:

Description
-----------

Select a LPT LEB for LPT garbage collection and call 'lpt_gc_lnum()'.
Returns \ ``0``\  on success and a negative error code on failure.

.. _`ubifs_lpt_start_commit`:

ubifs_lpt_start_commit
======================

.. c:function:: int ubifs_lpt_start_commit(struct ubifs_info *c)

    UBIFS commit starts.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

.. _`ubifs_lpt_start_commit.description`:

Description
-----------

This function has to be called when UBIFS starts the commit operation.
This function "freezes" all currently dirty LEB properties and does not
change them anymore. Further changes are saved and tracked separately
because they are not part of this commit. This function returns zero in case
of success and a negative error code in case of failure.

.. _`free_obsolete_cnodes`:

free_obsolete_cnodes
====================

.. c:function:: void free_obsolete_cnodes(struct ubifs_info *c)

    free obsolete cnodes for commit end.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_lpt_end_commit`:

ubifs_lpt_end_commit
====================

.. c:function:: int ubifs_lpt_end_commit(struct ubifs_info *c)

    finish the commit operation.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

.. _`ubifs_lpt_end_commit.description`:

Description
-----------

This function has to be called when the commit operation finishes. It
flushes the changes which were "frozen" by 'ubifs_lprops_start_commit()' to
the media. Returns zero in case of success and a negative error code in case
of failure.

.. _`ubifs_lpt_post_commit`:

ubifs_lpt_post_commit
=====================

.. c:function:: int ubifs_lpt_post_commit(struct ubifs_info *c)

    post commit LPT trivial GC and LPT GC.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_lpt_post_commit.description`:

Description
-----------

LPT trivial GC is completed after a commit. Also LPT GC is done after a
commit for the "big" LPT model.

.. _`first_nnode`:

first_nnode
===========

.. c:function:: struct ubifs_nnode *first_nnode(struct ubifs_info *c, int *hght)

    find the first nnode in memory.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int \*hght:
        height of tree where nnode found is returned here

.. _`first_nnode.description`:

Description
-----------

This function returns a pointer to the nnode found or \ ``NULL``\  if no nnode is
found. This function is a helper to 'ubifs_lpt_free()'.

.. _`next_nnode`:

next_nnode
==========

.. c:function:: struct ubifs_nnode *next_nnode(struct ubifs_info *c, struct ubifs_nnode *nnode, int *hght)

    find the next nnode in memory.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param struct ubifs_nnode \*nnode:
        nnode from which to start.

    :param int \*hght:
        height of tree where nnode is, is passed and returned here

.. _`next_nnode.description`:

Description
-----------

This function returns a pointer to the nnode found or \ ``NULL``\  if no nnode is
found. This function is a helper to 'ubifs_lpt_free()'.

.. _`ubifs_lpt_free`:

ubifs_lpt_free
==============

.. c:function:: void ubifs_lpt_free(struct ubifs_info *c, int wr_only)

    free resources owned by the LPT.

    :param struct ubifs_info \*c:
        UBIFS file-system description object

    :param int wr_only:
        free only resources used for writing

.. _`dbg_is_all_ff`:

dbg_is_all_ff
=============

.. c:function:: int dbg_is_all_ff(uint8_t *buf, int len)

    determine if a buffer contains only 0xFF bytes.

    :param uint8_t \*buf:
        buffer

    :param int len:
        buffer length

.. _`dbg_is_nnode_dirty`:

dbg_is_nnode_dirty
==================

.. c:function:: int dbg_is_nnode_dirty(struct ubifs_info *c, int lnum, int offs)

    determine if a nnode is dirty.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

    :param int lnum:
        LEB number where nnode was written

    :param int offs:
        offset where nnode was written

.. _`dbg_is_pnode_dirty`:

dbg_is_pnode_dirty
==================

.. c:function:: int dbg_is_pnode_dirty(struct ubifs_info *c, int lnum, int offs)

    determine if a pnode is dirty.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

    :param int lnum:
        LEB number where pnode was written

    :param int offs:
        offset where pnode was written

.. _`dbg_is_ltab_dirty`:

dbg_is_ltab_dirty
=================

.. c:function:: int dbg_is_ltab_dirty(struct ubifs_info *c, int lnum, int offs)

    determine if a ltab node is dirty.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

    :param int lnum:
        LEB number where ltab node was written

    :param int offs:
        offset where ltab node was written

.. _`dbg_is_lsave_dirty`:

dbg_is_lsave_dirty
==================

.. c:function:: int dbg_is_lsave_dirty(struct ubifs_info *c, int lnum, int offs)

    determine if a lsave node is dirty.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

    :param int lnum:
        LEB number where lsave node was written

    :param int offs:
        offset where lsave node was written

.. _`dbg_is_node_dirty`:

dbg_is_node_dirty
=================

.. c:function:: int dbg_is_node_dirty(struct ubifs_info *c, int node_type, int lnum, int offs)

    determine if a node is dirty.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

    :param int node_type:
        node type

    :param int lnum:
        LEB number where node was written

    :param int offs:
        offset where node was written

.. _`dbg_check_ltab_lnum`:

dbg_check_ltab_lnum
===================

.. c:function:: int dbg_check_ltab_lnum(struct ubifs_info *c, int lnum)

    check the ltab for a LPT LEB number.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

    :param int lnum:
        LEB number where node was written

.. _`dbg_check_ltab_lnum.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`dbg_check_ltab`:

dbg_check_ltab
==============

.. c:function:: int dbg_check_ltab(struct ubifs_info *c)

    check the free and dirty space in the ltab.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

.. _`dbg_check_ltab.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`dbg_chk_lpt_free_spc`:

dbg_chk_lpt_free_spc
====================

.. c:function:: int dbg_chk_lpt_free_spc(struct ubifs_info *c)

    check LPT free space is enough to write entire LPT.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

.. _`dbg_chk_lpt_free_spc.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`dbg_chk_lpt_sz`:

dbg_chk_lpt_sz
==============

.. c:function:: int dbg_chk_lpt_sz(struct ubifs_info *c, int action, int len)

    check LPT does not write more than LPT size.

    :param struct ubifs_info \*c:
        the UBIFS file-system description object

    :param int action:
        what to do

    :param int len:
        length written

.. _`dbg_chk_lpt_sz.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.
The \ ``action``\  argument may be one of:
o \ ``0``\  - LPT debugging checking starts, initialize debugging variables;
o \ ``1``\  - wrote an LPT node, increase LPT size by \ ``len``\  bytes;
o \ ``2``\  - switched to a different LEB and wasted \ ``len``\  bytes;
o \ ``3``\  - check that we've written the right number of bytes.
o \ ``4``\  - wasted \ ``len``\  bytes;

.. _`dump_lpt_leb`:

dump_lpt_leb
============

.. c:function:: void dump_lpt_leb(const struct ubifs_info *c, int lnum)

    dump an LPT LEB.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

    :param int lnum:
        LEB number to dump

.. _`dump_lpt_leb.description`:

Description
-----------

This function dumps an LEB from LPT area. Nodes in this area are very
different to nodes in the main area (e.g., they do not have common headers,
they do not have 8-byte alignments, etc), so we have a separate function to
dump LPT area LEBs. Note, LPT has to be locked by the caller.

.. _`ubifs_dump_lpt_lebs`:

ubifs_dump_lpt_lebs
===================

.. c:function:: void ubifs_dump_lpt_lebs(const struct ubifs_info *c)

    dump LPT lebs.

    :param const struct ubifs_info \*c:
        UBIFS file-system description object

.. _`ubifs_dump_lpt_lebs.description`:

Description
-----------

This function dumps all LPT LEBs. The caller has to make sure the LPT is
locked.

.. _`dbg_populate_lsave`:

dbg_populate_lsave
==================

.. c:function:: int dbg_populate_lsave(struct ubifs_info *c)

    debugging version of 'populate_lsave()'

    :param struct ubifs_info \*c:
        UBIFS file-system description object

.. _`dbg_populate_lsave.description`:

Description
-----------

This is a debugging version for 'populate_lsave()' which populates lsave
with random LEBs instead of useful LEBs, which is good for test coverage.
Returns zero if lsave has not been populated (this debugging feature is
disabled) an non-zero if lsave has been populated.

.. This file was automatic generated / don't edit.

