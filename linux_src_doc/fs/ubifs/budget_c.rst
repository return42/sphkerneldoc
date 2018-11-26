.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/budget.c

.. _`shrink_liability`:

shrink_liability
================

.. c:function:: void shrink_liability(struct ubifs_info *c, int nr_to_write)

    write-back some dirty pages/inodes.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param nr_to_write:
        how many dirty pages to write-back
    :type nr_to_write: int

.. _`shrink_liability.description`:

Description
-----------

This function shrinks UBIFS liability by means of writing back some amount
of dirty inodes and their pages.

Note, this function synchronizes even VFS inodes which are locked
(@i_mutex) by the caller of the budgeting function, because write-back does
not touch \ ``i_mutex``\ .

.. _`run_gc`:

run_gc
======

.. c:function:: int run_gc(struct ubifs_info *c)

    run garbage collector.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`run_gc.description`:

Description
-----------

This function runs garbage collector to make some more free space. Returns
zero if a free LEB has been produced, \ ``-EAGAIN``\  if commit is required, and a
negative error code in case of failure.

.. _`get_liability`:

get_liability
=============

.. c:function:: long long get_liability(struct ubifs_info *c)

    calculate current liability.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`get_liability.description`:

Description
-----------

This function calculates and returns current UBIFS liability, i.e. the
amount of bytes UBIFS has "promised" to write to the media.

.. _`make_free_space`:

make_free_space
===============

.. c:function:: int make_free_space(struct ubifs_info *c)

    make more free space on the file-system.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`make_free_space.description`:

Description
-----------

This function is called when an operation cannot be budgeted because there
is supposedly no free space. But in most cases there is some free space:
o budgeting is pessimistic, so it always budgets more than it is actually
needed, so shrinking the liability is one way to make free space - the
cached data will take less space then it was budgeted for;
o GC may turn some dark space into free space (budgeting treats dark space
as not available);
o commit may free some LEB, i.e., turn freeable LEBs into free LEBs.

So this function tries to do the above. Returns \ ``-EAGAIN``\  if some free space
was presumably made and the caller has to re-try budgeting the operation.
Returns \ ``-ENOSPC``\  if it couldn't do more free space, and other negative error
codes on failures.

.. _`ubifs_calc_min_idx_lebs`:

ubifs_calc_min_idx_lebs
=======================

.. c:function:: int ubifs_calc_min_idx_lebs(struct ubifs_info *c)

    calculate amount of LEBs for the index.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`ubifs_calc_min_idx_lebs.description`:

Description
-----------

This function calculates and returns the number of LEBs which should be kept
for index usage.

.. _`ubifs_calc_available`:

ubifs_calc_available
====================

.. c:function:: long long ubifs_calc_available(const struct ubifs_info *c, int min_idx_lebs)

    calculate available FS space.

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param min_idx_lebs:
        minimum number of LEBs reserved for the index
    :type min_idx_lebs: int

.. _`ubifs_calc_available.description`:

Description
-----------

This function calculates and returns amount of FS space available for use.

.. _`can_use_rp`:

can_use_rp
==========

.. c:function:: int can_use_rp(struct ubifs_info *c)

    check whether the user is allowed to use reserved pool.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`can_use_rp.description`:

Description
-----------

UBIFS has so-called "reserved pool" which is flash space reserved
for the superuser and for uses whose UID/GID is recorded in UBIFS superblock.
This function checks whether current user is allowed to use reserved pool.
Returns \ ``1``\   current user is allowed to use reserved pool and \ ``0``\  otherwise.

.. _`do_budget_space`:

do_budget_space
===============

.. c:function:: int do_budget_space(struct ubifs_info *c)

    reserve flash space for index and data growth.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`do_budget_space.description`:

Description
-----------

This function makes sure UBIFS has enough free LEBs for index growth and
data.

When budgeting index space, UBIFS reserves thrice as many LEBs as the index
would take if it was consolidated and written to the flash. This guarantees
that the "in-the-gaps" commit method always succeeds and UBIFS will always
be able to commit dirty index. So this function basically adds amount of
budgeted index space to the size of the current index, multiplies this by 3,
and makes sure this does not exceed the amount of free LEBs.

Notes about \ ``c->bi.min_idx_lebs``\  and \ ``c->lst.idx_lebs``\  variables:
o \ ``c->lst.idx_lebs``\  is the number of LEBs the index currently uses. It might
be large, because UBIFS does not do any index consolidation as long as
there is free space. IOW, the index may take a lot of LEBs, but the LEBs
will contain a lot of dirt.
o \ ``c->bi.min_idx_lebs``\  is the number of LEBS the index presumably takes. IOW,
the index may be consolidated to take up to \ ``c->bi.min_idx_lebs``\  LEBs.

This function returns zero in case of success, and \ ``-ENOSPC``\  in case of
failure.

.. _`calc_idx_growth`:

calc_idx_growth
===============

.. c:function:: int calc_idx_growth(const struct ubifs_info *c, const struct ubifs_budget_req *req)

    calculate approximate index growth from budgeting request.

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param req:
        budgeting request
    :type req: const struct ubifs_budget_req \*

.. _`calc_idx_growth.description`:

Description
-----------

For now we assume each new node adds one znode. But this is rather poor
approximation, though.

.. _`calc_data_growth`:

calc_data_growth
================

.. c:function:: int calc_data_growth(const struct ubifs_info *c, const struct ubifs_budget_req *req)

    calculate approximate amount of new data from budgeting request.

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param req:
        budgeting request
    :type req: const struct ubifs_budget_req \*

.. _`calc_dd_growth`:

calc_dd_growth
==============

.. c:function:: int calc_dd_growth(const struct ubifs_info *c, const struct ubifs_budget_req *req)

    calculate approximate amount of data which makes other data dirty from budgeting request.

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param req:
        budgeting request
    :type req: const struct ubifs_budget_req \*

.. _`ubifs_budget_space`:

ubifs_budget_space
==================

.. c:function:: int ubifs_budget_space(struct ubifs_info *c, struct ubifs_budget_req *req)

    ensure there is enough space to complete an operation.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param req:
        budget request
    :type req: struct ubifs_budget_req \*

.. _`ubifs_budget_space.description`:

Description
-----------

This function allocates budget for an operation. It uses pessimistic
approximation of how much flash space the operation needs. The goal of this
function is to make sure UBIFS always has flash space to flush all dirty
pages, dirty inodes, and dirty znodes (liability). This function may force
commit, garbage-collection or write-back. Returns zero in case of success,
\ ``-ENOSPC``\  if there is no free space and other negative error codes in case of
failures.

.. _`ubifs_release_budget`:

ubifs_release_budget
====================

.. c:function:: void ubifs_release_budget(struct ubifs_info *c, struct ubifs_budget_req *req)

    release budgeted free space.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param req:
        budget request
    :type req: struct ubifs_budget_req \*

.. _`ubifs_release_budget.description`:

Description
-----------

This function releases the space budgeted by 'ubifs_budget_space()'. Note,
since the index changes (which were budgeted for in \ ``req->idx_growth``\ ) will
only be written to the media on commit, this function moves the index budget
from \ ``c->bi.idx_growth``\  to \ ``c->bi.uncommitted_idx``\ . The latter will be zeroed
by the commit operation.

.. _`ubifs_convert_page_budget`:

ubifs_convert_page_budget
=========================

.. c:function:: void ubifs_convert_page_budget(struct ubifs_info *c)

    convert budget of a new page.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`ubifs_convert_page_budget.description`:

Description
-----------

This function converts budget which was allocated for a new page of data to
the budget of changing an existing page of data. The latter is smaller than
the former, so this function only does simple re-calculation and does not
involve any write-back.

.. _`ubifs_release_dirty_inode_budget`:

ubifs_release_dirty_inode_budget
================================

.. c:function:: void ubifs_release_dirty_inode_budget(struct ubifs_info *c, struct ubifs_inode *ui)

    release dirty inode budget.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param ui:
        UBIFS inode to release the budget for
    :type ui: struct ubifs_inode \*

.. _`ubifs_release_dirty_inode_budget.description`:

Description
-----------

This function releases budget corresponding to a dirty inode. It is usually
called when after the inode has been written to the media and marked as
clean. It also causes the "no space" flags to be cleared.

.. _`ubifs_reported_space`:

ubifs_reported_space
====================

.. c:function:: long long ubifs_reported_space(const struct ubifs_info *c, long long free)

    calculate reported free space.

    :param c:
        the UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param free:
        amount of free space
    :type free: long long

.. _`ubifs_reported_space.description`:

Description
-----------

This function calculates amount of free space which will be reported to
user-space. User-space application tend to expect that if the file-system
(e.g., via the 'statfs()' call) reports that it has N bytes available, they
are able to write a file of size N. UBIFS attaches node headers to each data
node and it has to write indexing nodes as well. This introduces additional
overhead, and UBIFS has to report slightly less free space to meet the above
expectations.

This function assumes free space is made up of uncompressed data nodes and
full index nodes (one per data node, tripled because we always allow enough
space to write the index thrice).

Note, the calculation is pessimistic, which means that most of the time
UBIFS reports less space than it actually has.

.. _`ubifs_get_free_space_nolock`:

ubifs_get_free_space_nolock
===========================

.. c:function:: long long ubifs_get_free_space_nolock(struct ubifs_info *c)

    return amount of free space.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`ubifs_get_free_space_nolock.description`:

Description
-----------

This function calculates amount of free space to report to user-space.

Because UBIFS may introduce substantial overhead (the index, node headers,
alignment, wastage at the end of LEBs, etc), it cannot report real amount of
free flash space it has (well, because not all dirty space is reclaimable,
UBIFS does not actually know the real amount). If UBIFS did so, it would
bread user expectations about what free space is. Users seem to accustomed
to assume that if the file-system reports N bytes of free space, they would
be able to fit a file of N bytes to the FS. This almost works for
traditional file-systems, because they have way less overhead than UBIFS.
So, to keep users happy, UBIFS tries to take the overhead into account.

.. _`ubifs_get_free_space`:

ubifs_get_free_space
====================

.. c:function:: long long ubifs_get_free_space(struct ubifs_info *c)

    return amount of free space.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`ubifs_get_free_space.description`:

Description
-----------

This function calculates and returns amount of free space to report to
user-space.

.. This file was automatic generated / don't edit.

