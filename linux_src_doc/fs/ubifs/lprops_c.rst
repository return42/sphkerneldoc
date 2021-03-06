.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/lprops.c

.. _`get_heap_comp_val`:

get_heap_comp_val
=================

.. c:function:: int get_heap_comp_val(struct ubifs_lprops *lprops, int cat)

    get the LEB properties value for heap comparisons.

    :param lprops:
        LEB properties
    :type lprops: struct ubifs_lprops \*

    :param cat:
        LEB category
    :type cat: int

.. _`move_up_lpt_heap`:

move_up_lpt_heap
================

.. c:function:: void move_up_lpt_heap(struct ubifs_info *c, struct ubifs_lpt_heap *heap, struct ubifs_lprops *lprops, int cat)

    move a new heap entry up as far as possible.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param heap:
        LEB category heap
    :type heap: struct ubifs_lpt_heap \*

    :param lprops:
        LEB properties to move
    :type lprops: struct ubifs_lprops \*

    :param cat:
        LEB category
    :type cat: int

.. _`move_up_lpt_heap.description`:

Description
-----------

New entries to a heap are added at the bottom and then moved up until the
parent's value is greater.  In the case of LPT's category heaps, the value
is either the amount of free space or the amount of dirty space, depending
on the category.

.. _`adjust_lpt_heap`:

adjust_lpt_heap
===============

.. c:function:: void adjust_lpt_heap(struct ubifs_info *c, struct ubifs_lpt_heap *heap, struct ubifs_lprops *lprops, int hpos, int cat)

    move a changed heap entry up or down the heap.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param heap:
        LEB category heap
    :type heap: struct ubifs_lpt_heap \*

    :param lprops:
        LEB properties to move
    :type lprops: struct ubifs_lprops \*

    :param hpos:
        heap position of \ ``lprops``\ 
    :type hpos: int

    :param cat:
        LEB category
    :type cat: int

.. _`adjust_lpt_heap.description`:

Description
-----------

Changed entries in a heap are moved up or down until the parent's value is
greater.  In the case of LPT's category heaps, the value is either the amount
of free space or the amount of dirty space, depending on the category.

.. _`add_to_lpt_heap`:

add_to_lpt_heap
===============

.. c:function:: int add_to_lpt_heap(struct ubifs_info *c, struct ubifs_lprops *lprops, int cat)

    add LEB properties to a LEB category heap.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param lprops:
        LEB properties to add
    :type lprops: struct ubifs_lprops \*

    :param cat:
        LEB category
    :type cat: int

.. _`add_to_lpt_heap.description`:

Description
-----------

This function returns \ ``1``\  if \ ``lprops``\  is added to the heap for LEB category
\ ``cat``\ , otherwise \ ``0``\  is returned because the heap is full.

.. _`remove_from_lpt_heap`:

remove_from_lpt_heap
====================

.. c:function:: void remove_from_lpt_heap(struct ubifs_info *c, struct ubifs_lprops *lprops, int cat)

    remove LEB properties from a LEB category heap.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param lprops:
        LEB properties to remove
    :type lprops: struct ubifs_lprops \*

    :param cat:
        LEB category
    :type cat: int

.. _`lpt_heap_replace`:

lpt_heap_replace
================

.. c:function:: void lpt_heap_replace(struct ubifs_info *c, struct ubifs_lprops *new_lprops, int cat)

    replace lprops in a category heap.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param new_lprops:
        LEB properties with which to replace
    :type new_lprops: struct ubifs_lprops \*

    :param cat:
        LEB category
    :type cat: int

.. _`lpt_heap_replace.description`:

Description
-----------

During commit it is sometimes necessary to copy a pnode (see dirty_cow_pnode)
and the lprops that the pnode contains.  When that happens, references in
the category heaps to those lprops must be updated to point to the new
lprops.  This function does that.

.. _`ubifs_add_to_cat`:

ubifs_add_to_cat
================

.. c:function:: void ubifs_add_to_cat(struct ubifs_info *c, struct ubifs_lprops *lprops, int cat)

    add LEB properties to a category list or heap.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param lprops:
        LEB properties to add
    :type lprops: struct ubifs_lprops \*

    :param cat:
        LEB category to which to add
    :type cat: int

.. _`ubifs_add_to_cat.description`:

Description
-----------

LEB properties are categorized to enable fast find operations.

.. _`ubifs_remove_from_cat`:

ubifs_remove_from_cat
=====================

.. c:function:: void ubifs_remove_from_cat(struct ubifs_info *c, struct ubifs_lprops *lprops, int cat)

    remove LEB properties from a category list or heap.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param lprops:
        LEB properties to remove
    :type lprops: struct ubifs_lprops \*

    :param cat:
        LEB category from which to remove
    :type cat: int

.. _`ubifs_remove_from_cat.description`:

Description
-----------

LEB properties are categorized to enable fast find operations.

.. _`ubifs_replace_cat`:

ubifs_replace_cat
=================

.. c:function:: void ubifs_replace_cat(struct ubifs_info *c, struct ubifs_lprops *old_lprops, struct ubifs_lprops *new_lprops)

    replace lprops in a category list or heap.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param old_lprops:
        LEB properties to replace
    :type old_lprops: struct ubifs_lprops \*

    :param new_lprops:
        LEB properties with which to replace
    :type new_lprops: struct ubifs_lprops \*

.. _`ubifs_replace_cat.description`:

Description
-----------

During commit it is sometimes necessary to copy a pnode (see dirty_cow_pnode)
and the lprops that the pnode contains. When that happens, references in
category lists and heaps must be replaced. This function does that.

.. _`ubifs_ensure_cat`:

ubifs_ensure_cat
================

.. c:function:: void ubifs_ensure_cat(struct ubifs_info *c, struct ubifs_lprops *lprops)

    ensure LEB properties are categorized.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param lprops:
        LEB properties
    :type lprops: struct ubifs_lprops \*

.. _`ubifs_ensure_cat.description`:

Description
-----------

A LEB may have fallen off of the bottom of a heap, and ended up as
un-categorized even though it has enough space for us now. If that is the
case this function will put the LEB back onto a heap.

.. _`ubifs_categorize_lprops`:

ubifs_categorize_lprops
=======================

.. c:function:: int ubifs_categorize_lprops(const struct ubifs_info *c, const struct ubifs_lprops *lprops)

    categorize LEB properties.

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param lprops:
        LEB properties to categorize
    :type lprops: const struct ubifs_lprops \*

.. _`ubifs_categorize_lprops.description`:

Description
-----------

LEB properties are categorized to enable fast find operations. This function
returns the LEB category to which the LEB properties belong. Note however
that if the LEB category is stored as a heap and the heap is full, the
LEB properties may have their category changed to \ ``LPROPS_UNCAT``\ .

.. _`change_category`:

change_category
===============

.. c:function:: void change_category(struct ubifs_info *c, struct ubifs_lprops *lprops)

    change LEB properties category.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param lprops:
        LEB properties to re-categorize
    :type lprops: struct ubifs_lprops \*

.. _`change_category.description`:

Description
-----------

LEB properties are categorized to enable fast find operations. When the LEB
properties change they must be re-categorized.

.. _`ubifs_calc_dark`:

ubifs_calc_dark
===============

.. c:function:: int ubifs_calc_dark(const struct ubifs_info *c, int spc)

    calculate LEB dark space size.

    :param c:
        the UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param spc:
        amount of free and dirty space in the LEB
    :type spc: int

.. _`ubifs_calc_dark.description`:

Description
-----------

This function calculates and returns amount of dark space in an LEB which
has \ ``spc``\  bytes of free and dirty space.

UBIFS is trying to account the space which might not be usable, and this
space is called "dark space". For example, if an LEB has only \ ``512``\  free
bytes, it is dark space, because it cannot fit a large data node.

.. _`is_lprops_dirty`:

is_lprops_dirty
===============

.. c:function:: int is_lprops_dirty(struct ubifs_info *c, struct ubifs_lprops *lprops)

    determine if LEB properties are dirty.

    :param c:
        the UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param lprops:
        LEB properties to test
    :type lprops: struct ubifs_lprops \*

.. _`ubifs_change_lp`:

ubifs_change_lp
===============

.. c:function:: const struct ubifs_lprops *ubifs_change_lp(struct ubifs_info *c, const struct ubifs_lprops *lp, int free, int dirty, int flags, int idx_gc_cnt)

    change LEB properties.

    :param c:
        the UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param lp:
        LEB properties to change
    :type lp: const struct ubifs_lprops \*

    :param free:
        new free space amount
    :type free: int

    :param dirty:
        new dirty space amount
    :type dirty: int

    :param flags:
        new flags
    :type flags: int

    :param idx_gc_cnt:
        change to the count of \ ``idx_gc``\  list
    :type idx_gc_cnt: int

.. _`ubifs_change_lp.description`:

Description
-----------

This function changes LEB properties (@free, \ ``dirty``\  or \ ``flag``\ ). However, the
property which has the \ ``LPROPS_NC``\  value is not changed. Returns a pointer to
the updated LEB properties on success and a negative error code on failure.

Note, the LEB properties may have had to be copied (due to COW) and
consequently the pointer returned may not be the same as the pointer
passed.

.. _`ubifs_get_lp_stats`:

ubifs_get_lp_stats
==================

.. c:function:: void ubifs_get_lp_stats(struct ubifs_info *c, struct ubifs_lp_stats *lst)

    get lprops statistics.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param lst:
        return statistics
    :type lst: struct ubifs_lp_stats \*

.. _`ubifs_change_one_lp`:

ubifs_change_one_lp
===================

.. c:function:: int ubifs_change_one_lp(struct ubifs_info *c, int lnum, int free, int dirty, int flags_set, int flags_clean, int idx_gc_cnt)

    change LEB properties.

    :param c:
        the UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param lnum:
        LEB to change properties for
    :type lnum: int

    :param free:
        amount of free space
    :type free: int

    :param dirty:
        amount of dirty space
    :type dirty: int

    :param flags_set:
        flags to set
    :type flags_set: int

    :param flags_clean:
        flags to clean
    :type flags_clean: int

    :param idx_gc_cnt:
        change to the count of idx_gc list
    :type idx_gc_cnt: int

.. _`ubifs_change_one_lp.description`:

Description
-----------

This function changes properties of LEB \ ``lnum``\ . It is a helper wrapper over
'ubifs_change_lp()' which hides lprops get/release. The arguments are the
same as in case of 'ubifs_change_lp()'. Returns zero in case of success and
a negative error code in case of failure.

.. _`ubifs_update_one_lp`:

ubifs_update_one_lp
===================

.. c:function:: int ubifs_update_one_lp(struct ubifs_info *c, int lnum, int free, int dirty, int flags_set, int flags_clean)

    update LEB properties.

    :param c:
        the UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param lnum:
        LEB to change properties for
    :type lnum: int

    :param free:
        amount of free space
    :type free: int

    :param dirty:
        amount of dirty space to add
    :type dirty: int

    :param flags_set:
        flags to set
    :type flags_set: int

    :param flags_clean:
        flags to clean
    :type flags_clean: int

.. _`ubifs_update_one_lp.description`:

Description
-----------

This function is the same as 'ubifs_change_one_lp()' but \ ``dirty``\  is added to
current dirty space, not substitutes it.

.. _`ubifs_read_one_lp`:

ubifs_read_one_lp
=================

.. c:function:: int ubifs_read_one_lp(struct ubifs_info *c, int lnum, struct ubifs_lprops *lp)

    read LEB properties.

    :param c:
        the UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param lnum:
        LEB to read properties for
    :type lnum: int

    :param lp:
        where to store read properties
    :type lp: struct ubifs_lprops \*

.. _`ubifs_read_one_lp.description`:

Description
-----------

This helper function reads properties of a LEB \ ``lnum``\  and stores them in \ ``lp``\ .
Returns zero in case of success and a negative error code in case of
failure.

.. _`ubifs_fast_find_free`:

ubifs_fast_find_free
====================

.. c:function:: const struct ubifs_lprops *ubifs_fast_find_free(struct ubifs_info *c)

    try to find a LEB with free space quickly.

    :param c:
        the UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`ubifs_fast_find_free.description`:

Description
-----------

This function returns LEB properties for a LEB with free space or \ ``NULL``\  if
the function is unable to find a LEB quickly.

.. _`ubifs_fast_find_empty`:

ubifs_fast_find_empty
=====================

.. c:function:: const struct ubifs_lprops *ubifs_fast_find_empty(struct ubifs_info *c)

    try to find an empty LEB quickly.

    :param c:
        the UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`ubifs_fast_find_empty.description`:

Description
-----------

This function returns LEB properties for an empty LEB or \ ``NULL``\  if the
function is unable to find an empty LEB quickly.

.. _`ubifs_fast_find_freeable`:

ubifs_fast_find_freeable
========================

.. c:function:: const struct ubifs_lprops *ubifs_fast_find_freeable(struct ubifs_info *c)

    try to find a freeable LEB quickly.

    :param c:
        the UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`ubifs_fast_find_freeable.description`:

Description
-----------

This function returns LEB properties for a freeable LEB or \ ``NULL``\  if the
function is unable to find a freeable LEB quickly.

.. _`ubifs_fast_find_frdi_idx`:

ubifs_fast_find_frdi_idx
========================

.. c:function:: const struct ubifs_lprops *ubifs_fast_find_frdi_idx(struct ubifs_info *c)

    try to find a freeable index LEB quickly.

    :param c:
        the UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`ubifs_fast_find_frdi_idx.description`:

Description
-----------

This function returns LEB properties for a freeable index LEB or \ ``NULL``\  if the
function is unable to find a freeable index LEB quickly.

.. _`dbg_check_cats`:

dbg_check_cats
==============

.. c:function:: int dbg_check_cats(struct ubifs_info *c)

    check category heaps and lists.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`dbg_check_cats.description`:

Description
-----------

This function returns \ ``0``\  on success and a negative error code on failure.

.. _`scan_check_cb`:

scan_check_cb
=============

.. c:function:: int scan_check_cb(struct ubifs_info *c, const struct ubifs_lprops *lp, int in_tree, struct ubifs_lp_stats *lst)

    scan callback.

    :param c:
        the UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param lp:
        LEB properties to scan
    :type lp: const struct ubifs_lprops \*

    :param in_tree:
        whether the LEB properties are in main memory
    :type in_tree: int

    :param lst:
        lprops statistics to update
    :type lst: struct ubifs_lp_stats \*

.. _`scan_check_cb.description`:

Description
-----------

This function returns a code that indicates whether the scan should continue
(%LPT_SCAN_CONTINUE), whether the LEB properties should be added to the tree
in main memory (%LPT_SCAN_ADD), or whether the scan should stop
(%LPT_SCAN_STOP).

.. _`dbg_check_lprops`:

dbg_check_lprops
================

.. c:function:: int dbg_check_lprops(struct ubifs_info *c)

    check all LEB properties.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`dbg_check_lprops.description`:

Description
-----------

This function checks all LEB properties and makes sure they are all correct.
It returns zero if everything is fine, \ ``-EINVAL``\  if there is an inconsistency
and other negative error codes in case of other errors. This function is
called while the file system is locked (because of commit start), so no
additional locking is required. Note that locking the LPT mutex would cause
a circular lock dependency with the TNC mutex.

.. This file was automatic generated / don't edit.

