.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/osc/osc_cache.c

.. _`osc_extent_is_overlapped`:

osc_extent_is_overlapped
========================

.. c:function:: int osc_extent_is_overlapped(struct osc_object *obj, struct osc_extent *ext)

    to make sure there is no overlapped extent in the tree.

    :param struct osc_object \*obj:
        *undescribed*

    :param struct osc_extent \*ext:
        *undescribed*

.. _`osc_extent_put_trust`:

osc_extent_put_trust
====================

.. c:function:: void osc_extent_put_trust(struct osc_extent *ext)

    it's known that the caller is not the last user. This is to address the problem of lacking of lu_env ;-).

    :param struct osc_extent \*ext:
        *undescribed*

.. _`osc_extent_search`:

osc_extent_search
=================

.. c:function:: struct osc_extent *osc_extent_search(struct osc_object *obj, pgoff_t index)

    previous extent in the tree.

    :param struct osc_object \*obj:
        *undescribed*

    :param pgoff_t index:
        *undescribed*

.. _`osc_extent_merge`:

osc_extent_merge
================

.. c:function:: int osc_extent_merge(const struct lu_env *env, struct osc_extent *cur, struct osc_extent *victim)

    if \ ``cur``\  and \ ``victim``\  are contiguous at chunk level.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct osc_extent \*cur:
        *undescribed*

    :param struct osc_extent \*victim:
        *undescribed*

.. _`osc_extent_release`:

osc_extent_release
==================

.. c:function:: void osc_extent_release(const struct lu_env *env, struct osc_extent *ext)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct osc_extent \*ext:
        *undescribed*

.. _`osc_extent_find`:

osc_extent_find
===============

.. c:function:: struct osc_extent *osc_extent_find(const struct lu_env *env, struct osc_object *obj, pgoff_t index, int *grants)

    extent tree.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct osc_object \*obj:
        *undescribed*

    :param pgoff_t index:
        *undescribed*

    :param int \*grants:
        *undescribed*

.. _`osc_extent_finish`:

osc_extent_finish
=================

.. c:function:: int osc_extent_finish(const struct lu_env *env, struct osc_extent *ext, int sent, int rc)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct osc_extent \*ext:
        *undescribed*

    :param int sent:
        *undescribed*

    :param int rc:
        *undescribed*

.. _`osc_extent_wait`:

osc_extent_wait
===============

.. c:function:: int osc_extent_wait(const struct lu_env *env, struct osc_extent *ext, int state)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct osc_extent \*ext:
        *undescribed*

    :param int state:
        *undescribed*

.. _`osc_extent_truncate`:

osc_extent_truncate
===================

.. c:function:: int osc_extent_truncate(struct osc_extent *ext, pgoff_t trunc_index, bool partial)

    \ ``size``\ , then partial truncate happens.

    :param struct osc_extent \*ext:
        *undescribed*

    :param pgoff_t trunc_index:
        *undescribed*

    :param bool partial:
        *undescribed*

.. _`osc_extent_make_ready`:

osc_extent_make_ready
=====================

.. c:function:: int osc_extent_make_ready(const struct lu_env *env, struct osc_extent *ext)

    A race with flushing page - \ :c:func:`ll_writepage`\  has to be handled cautiously.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct osc_extent \*ext:
        *undescribed*

.. _`osc_extent_expand`:

osc_extent_expand
=================

.. c:function:: int osc_extent_expand(struct osc_extent *ext, pgoff_t index, int *grants)

    called to expand the extent for the same IO. To expand the extent, the page index must be in the same or next chunk of ext->oe_end.

    :param struct osc_extent \*ext:
        *undescribed*

    :param pgoff_t index:
        *undescribed*

    :param int \*grants:
        *undescribed*

.. _`osc_reserve_grant`:

osc_reserve_grant
=================

.. c:function:: int osc_reserve_grant(struct client_obd *cli, unsigned int bytes)

    grants before entering into critical section.

    :param struct client_obd \*cli:
        *undescribed*

    :param unsigned int bytes:
        *undescribed*

.. _`osc_reserve_grant.description`:

Description
-----------

spin_lock held by caller

.. _`osc_free_grant`:

osc_free_grant
==============

.. c:function:: void osc_free_grant(struct client_obd *cli, unsigned int nr_pages, unsigned int lost_grant)

    :param struct client_obd \*cli:
        *undescribed*

    :param unsigned int nr_pages:
        *undescribed*

    :param unsigned int lost_grant:
        *undescribed*

.. _`osc_free_grant.description`:

Description
-----------

\ ``lost_grant``\  is used to remember how many grants we have allocated but not
used, we should return these grants to OST. There're two cases where grants

.. _`osc_free_grant.can-be-lost`:

can be lost
-----------

1. truncate;
2. blocksize at OST is less than PAGE_SIZE and a partial page was
written. In this case OST may use less chunks to serve this partial
write. OSTs don't actually know the page size on the client side. so
clients have to calculate lost grant by the blocksize on the OST.
See \ :c:func:`filter_grant_check`\  for details.

.. _`osc_exit_cache`:

osc_exit_cache
==============

.. c:function:: void osc_exit_cache(struct client_obd *cli, struct osc_async_page *oap)

    the dirty accounting due to error.

    :param struct client_obd \*cli:
        *undescribed*

    :param struct osc_async_page \*oap:
        *undescribed*

.. _`osc_enter_cache_try`:

osc_enter_cache_try
===================

.. c:function:: int osc_enter_cache_try(struct client_obd *cli, struct osc_async_page *oap, int bytes, int transient)

    blocking version of \ :c:func:`osc_enter_cache`\  that consumes grant only when it is available.

    :param struct client_obd \*cli:
        *undescribed*

    :param struct osc_async_page \*oap:
        *undescribed*

    :param int bytes:
        *undescribed*

    :param int transient:
        *undescribed*

.. _`osc_enter_cache`:

osc_enter_cache
===============

.. c:function:: int osc_enter_cache(const struct lu_env *env, struct client_obd *cli, struct osc_async_page *oap, int bytes)

    in this function will be freed in bulk in \ :c:func:`osc_free_grant`\  unless it fails to add osc cache, in that case, it will be freed in \ :c:func:`osc_exit_cache`\ .

    :param const struct lu_env \*env:
        *undescribed*

    :param struct client_obd \*cli:
        *undescribed*

    :param struct osc_async_page \*oap:
        *undescribed*

    :param int bytes:
        *undescribed*

.. _`osc_enter_cache.description`:

Description
-----------

The process will be put into sleep if it's already run out of grant.

.. _`osc_dec_unstable_pages`:

osc_dec_unstable_pages
======================

.. c:function:: void osc_dec_unstable_pages(struct ptlrpc_request *req)

    increment operations performed in osc_inc_unstable_pages. It is registered as the RPC request callback, and is executed when the bulk RPC is committed on the server. Thus at this point, the pages involved in the bulk transfer are no longer considered unstable.

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`try_to_add_extent_for_io`:

try_to_add_extent_for_io
========================

.. c:function:: int try_to_add_extent_for_io(struct client_obd *cli, struct osc_extent *ext, struct list_head *rpclist, int *pc, unsigned int *max_pages)

    - # of pages must not be over max_pages_per_rpc - extent must be compatible with previous ones

    :param struct client_obd \*cli:
        *undescribed*

    :param struct osc_extent \*ext:
        *undescribed*

    :param struct list_head \*rpclist:
        *undescribed*

    :param int \*pc:
        *undescribed*

    :param unsigned int \*max_pages:
        *undescribed*

.. _`get_write_extents`:

get_write_extents
=================

.. c:function:: int get_write_extents(struct osc_object *obj, struct list_head *rpclist)

    \ :c:func:`get_write_extent`\  takes all appropriate extents in atomic.

    :param struct osc_object \*obj:
        *undescribed*

    :param struct list_head \*rpclist:
        *undescribed*

.. _`get_write_extents.the-following-policy-is-used-to-collect-extents-for-io`:

The following policy is used to collect extents for IO
------------------------------------------------------

1. Add as many HP extents as possible;
2. Add the first urgent extent in urgent extent list and take it out of
urgent list;
3. Add subsequent extents of this urgent extent;
4. If urgent list is not empty, goto 2;
5. Traverse the extent tree from the 1st extent;
6. Above steps exit if there is no space in this RPC.

.. _`osc_send_read_rpc`:

osc_send_read_rpc
=================

.. c:function:: int osc_send_read_rpc(const struct lu_env *env, struct client_obd *cli, struct osc_object *osc)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct client_obd \*cli:
        *undescribed*

    :param struct osc_object \*osc:
        *undescribed*

.. _`osc_send_read_rpc.description`:

Description
-----------

\param cmd OBD_BRW\_\* macroses
\param lop pending pages

\return zero if no page added to send queue.
\return 1 if pages successfully added to send queue.
\return negative on errors.

.. _`osc_flush_async_page`:

osc_flush_async_page
====================

.. c:function:: int osc_flush_async_page(const struct lu_env *env, struct cl_io *io, struct osc_page *ops)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct osc_page \*ops:
        *undescribed*

.. _`osc_flush_async_page.description`:

Description
-----------

We should find out the corresponding extent and add the whole extent
into urgent list. The extent may be being truncated or used, handle it
carefully.

.. _`osc_cancel_async_page`:

osc_cancel_async_page
=====================

.. c:function:: int osc_cancel_async_page(const struct lu_env *env, struct osc_page *ops)

    get the caller woken as soon as possible.  If its page hasn't been put in an rpc yet it can dequeue immediately.  Otherwise it has to mark the rpc as desiring interruption which will forcefully complete the rpc once the rpc has timed out.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct osc_page \*ops:
        *undescribed*

.. _`osc_cache_truncate_start`:

osc_cache_truncate_start
========================

.. c:function:: int osc_cache_truncate_start(const struct lu_env *env, struct osc_io *oio, struct osc_object *obj, __u64 size)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct osc_io \*oio:
        *undescribed*

    :param struct osc_object \*obj:
        *undescribed*

    :param __u64 size:
        *undescribed*

.. _`osc_cache_truncate_end`:

osc_cache_truncate_end
======================

.. c:function:: void osc_cache_truncate_end(const struct lu_env *env, struct osc_io *oio, struct osc_object *obj)

    >oi_trunc back to cache.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct osc_io \*oio:
        *undescribed*

    :param struct osc_object \*obj:
        *undescribed*

.. _`osc_cache_wait_range`:

osc_cache_wait_range
====================

.. c:function:: int osc_cache_wait_range(const struct lu_env *env, struct osc_object *obj, pgoff_t start, pgoff_t end)

    The caller must have called \ :c:func:`osc_cache_writeback_range`\  to issue IO otherwise it will take a long time for this function to finish.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct osc_object \*obj:
        *undescribed*

    :param pgoff_t start:
        *undescribed*

    :param pgoff_t end:
        *undescribed*

.. _`osc_cache_wait_range.description`:

Description
-----------

Caller must hold inode_mutex , or cancel exclusive dlm lock so that
nobody else can dirty this range of file while we're waiting for
extents to be written.

.. _`osc_cache_writeback_range`:

osc_cache_writeback_range
=========================

.. c:function:: int osc_cache_writeback_range(const struct lu_env *env, struct osc_object *obj, pgoff_t start, pgoff_t end, int hp, int discard)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct osc_object \*obj:
        *undescribed*

    :param pgoff_t start:
        *undescribed*

    :param pgoff_t end:
        *undescribed*

    :param int hp:
        should be set this is caused by lock cancel;

    :param int discard:
        is set if dirty pages should be dropped - file will be deleted or
        truncated, this implies there is no partially discarding extents.

.. _`osc_cache_writeback_range.description`:

Description
-----------

Return how many pages will be issued, or error code if error occurred.

.. _`osc_page_gang_lookup`:

osc_page_gang_lookup
====================

.. c:function:: int osc_page_gang_lookup(const struct lu_env *env, struct cl_io *io, struct osc_object *osc, pgoff_t start, pgoff_t end, osc_page_gang_cbt cb, void *cbdata)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct osc_object \*osc:
        *undescribed*

    :param pgoff_t start:
        *undescribed*

    :param pgoff_t end:
        *undescribed*

    :param osc_page_gang_cbt cb:
        *undescribed*

    :param void \*cbdata:
        *undescribed*

.. _`osc_page_gang_lookup.description`:

Description
-----------

\param resched If not NULL, then we give up before hogging CPU for too
long and set \*resched = 1, in that case caller should implement a retry
logic.

Gang tree lookup (\ :c:func:`radix_tree_gang_lookup`\ ) optimization is absolutely
crucial in the face of [offset, EOF] locks.

Return at least one page in \ ``queue``\  unless there is no covered page.

.. _`check_and_discard_cb`:

check_and_discard_cb
====================

.. c:function:: int check_and_discard_cb(const struct lu_env *env, struct cl_io *io, struct osc_page *ops, void *cbdata)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct osc_page \*ops:
        *undescribed*

    :param void \*cbdata:
        *undescribed*

.. _`osc_lock_discard_pages`:

osc_lock_discard_pages
======================

.. c:function:: int osc_lock_discard_pages(const struct lu_env *env, struct osc_object *osc, pgoff_t start, pgoff_t end, enum cl_lock_mode mode)

    tree to find all covering pages and discard them. If a page is being covered by other locks, it should remain in cache.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct osc_object \*osc:
        *undescribed*

    :param pgoff_t start:
        *undescribed*

    :param pgoff_t end:
        *undescribed*

    :param enum cl_lock_mode mode:
        *undescribed*

.. _`osc_lock_discard_pages.description`:

Description
-----------

If error happens on any step, the process continues anyway (the reasoning
behind this being that lock cancellation cannot be delayed indefinitely).

.. This file was automatic generated / don't edit.

