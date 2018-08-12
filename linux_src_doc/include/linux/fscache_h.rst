.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/fscache.h

.. _`fscache_register_netfs`:

fscache_register_netfs
======================

.. c:function:: int fscache_register_netfs(struct fscache_netfs *netfs)

    Register a filesystem as desiring caching services

    :param struct fscache_netfs \*netfs:
        The description of the filesystem

.. _`fscache_register_netfs.description`:

Description
-----------

Register a filesystem as desiring caching services if they're available.

See Documentation/filesystems/caching/netfs-api.txt for a complete
description.

.. _`fscache_unregister_netfs`:

fscache_unregister_netfs
========================

.. c:function:: void fscache_unregister_netfs(struct fscache_netfs *netfs)

    Indicate that a filesystem no longer desires caching services

    :param struct fscache_netfs \*netfs:
        The description of the filesystem

.. _`fscache_unregister_netfs.description`:

Description
-----------

Indicate that a filesystem no longer desires caching services for the
moment.

See Documentation/filesystems/caching/netfs-api.txt for a complete
description.

.. _`fscache_lookup_cache_tag`:

fscache_lookup_cache_tag
========================

.. c:function:: struct fscache_cache_tag *fscache_lookup_cache_tag(const char *name)

    Look up a cache tag

    :param const char \*name:
        The name of the tag to search for

.. _`fscache_lookup_cache_tag.description`:

Description
-----------

Acquire a specific cache referral tag that can be used to select a specific
cache in which to cache an index.

See Documentation/filesystems/caching/netfs-api.txt for a complete
description.

.. _`fscache_release_cache_tag`:

fscache_release_cache_tag
=========================

.. c:function:: void fscache_release_cache_tag(struct fscache_cache_tag *tag)

    Release a cache tag

    :param struct fscache_cache_tag \*tag:
        The tag to release

.. _`fscache_release_cache_tag.description`:

Description
-----------

Release a reference to a cache referral tag previously looked up.

See Documentation/filesystems/caching/netfs-api.txt for a complete
description.

.. _`fscache_acquire_cookie`:

fscache_acquire_cookie
======================

.. c:function:: struct fscache_cookie *fscache_acquire_cookie(struct fscache_cookie *parent, const struct fscache_cookie_def *def, const void *index_key, size_t index_key_len, const void *aux_data, size_t aux_data_len, void *netfs_data, loff_t object_size, bool enable)

    Acquire a cookie to represent a cache object

    :param struct fscache_cookie \*parent:
        The cookie that's to be the parent of this one

    :param const struct fscache_cookie_def \*def:
        A description of the cache object, including callback operations

    :param const void \*index_key:
        The index key for this cookie

    :param size_t index_key_len:
        Size of the index key

    :param const void \*aux_data:
        The auxiliary data for the cookie (may be NULL)

    :param size_t aux_data_len:
        Size of the auxiliary data buffer

    :param void \*netfs_data:
        An arbitrary piece of data to be kept in the cookie to
        represent the cache object to the netfs

    :param loff_t object_size:
        The initial size of object

    :param bool enable:
        Whether or not to enable a data cookie immediately

.. _`fscache_acquire_cookie.description`:

Description
-----------

This function is used to inform FS-Cache about part of an index hierarchy
that can be used to locate files.  This is done by requesting a cookie for
each index in the path to the file.

See Documentation/filesystems/caching/netfs-api.txt for a complete
description.

.. _`fscache_relinquish_cookie`:

fscache_relinquish_cookie
=========================

.. c:function:: void fscache_relinquish_cookie(struct fscache_cookie *cookie, const void *aux_data, bool retire)

    Return the cookie to the cache, maybe discarding it

    :param struct fscache_cookie \*cookie:
        The cookie being returned

    :param const void \*aux_data:
        The updated auxiliary data for the cookie (may be NULL)

    :param bool retire:
        True if the cache object the cookie represents is to be discarded

.. _`fscache_relinquish_cookie.description`:

Description
-----------

This function returns a cookie to the cache, forcibly discarding the
associated cache object if retire is set to true.  The opportunity is
provided to update the auxiliary data in the cache before the object is
disconnected.

See Documentation/filesystems/caching/netfs-api.txt for a complete
description.

.. _`fscache_check_consistency`:

fscache_check_consistency
=========================

.. c:function:: int fscache_check_consistency(struct fscache_cookie *cookie, const void *aux_data)

    Request validation of a cache's auxiliary data

    :param struct fscache_cookie \*cookie:
        The cookie representing the cache object

    :param const void \*aux_data:
        The updated auxiliary data for the cookie (may be NULL)

.. _`fscache_check_consistency.description`:

Description
-----------

Request an consistency check from fscache, which passes the request to the
backing cache.  The auxiliary data on the cookie will be updated first if
\ ``aux_data``\  is set.

Returns 0 if consistent and -ESTALE if inconsistent.  May also
return -ENOMEM and -ERESTARTSYS.

.. _`fscache_update_cookie`:

fscache_update_cookie
=====================

.. c:function:: void fscache_update_cookie(struct fscache_cookie *cookie, const void *aux_data)

    Request that a cache object be updated

    :param struct fscache_cookie \*cookie:
        The cookie representing the cache object

    :param const void \*aux_data:
        The updated auxiliary data for the cookie (may be NULL)

.. _`fscache_update_cookie.description`:

Description
-----------

Request an update of the index data for the cache object associated with the
cookie.  The auxiliary data on the cookie will be updated first if \ ``aux_data``\ 
is set.

See Documentation/filesystems/caching/netfs-api.txt for a complete
description.

.. _`fscache_pin_cookie`:

fscache_pin_cookie
==================

.. c:function:: int fscache_pin_cookie(struct fscache_cookie *cookie)

    Pin a data-storage cache object in its cache

    :param struct fscache_cookie \*cookie:
        The cookie representing the cache object

.. _`fscache_pin_cookie.description`:

Description
-----------

Permit data-storage cache objects to be pinned in the cache.

See Documentation/filesystems/caching/netfs-api.txt for a complete
description.

.. _`fscache_unpin_cookie`:

fscache_unpin_cookie
====================

.. c:function:: void fscache_unpin_cookie(struct fscache_cookie *cookie)

    Unpin a data-storage cache object in its cache

    :param struct fscache_cookie \*cookie:
        The cookie representing the cache object

.. _`fscache_unpin_cookie.description`:

Description
-----------

Permit data-storage cache objects to be unpinned from the cache.

See Documentation/filesystems/caching/netfs-api.txt for a complete
description.

.. _`fscache_attr_changed`:

fscache_attr_changed
====================

.. c:function:: int fscache_attr_changed(struct fscache_cookie *cookie)

    Notify cache that an object's attributes changed

    :param struct fscache_cookie \*cookie:
        The cookie representing the cache object

.. _`fscache_attr_changed.description`:

Description
-----------

Send a notification to the cache indicating that an object's attributes have
changed.  This includes the data size.  These attributes will be obtained
through the \ :c:func:`get_attr`\  cookie definition op.

See Documentation/filesystems/caching/netfs-api.txt for a complete
description.

.. _`fscache_invalidate`:

fscache_invalidate
==================

.. c:function:: void fscache_invalidate(struct fscache_cookie *cookie)

    Notify cache that an object needs invalidation

    :param struct fscache_cookie \*cookie:
        The cookie representing the cache object

.. _`fscache_invalidate.description`:

Description
-----------

Notify the cache that an object is needs to be invalidated and that it
should abort any retrievals or stores it is doing on the cache.  The object
is then marked non-caching until such time as the invalidation is complete.

This can be called with spinlocks held.

See Documentation/filesystems/caching/netfs-api.txt for a complete
description.

.. _`fscache_wait_on_invalidate`:

fscache_wait_on_invalidate
==========================

.. c:function:: void fscache_wait_on_invalidate(struct fscache_cookie *cookie)

    Wait for invalidation to complete

    :param struct fscache_cookie \*cookie:
        The cookie representing the cache object

.. _`fscache_wait_on_invalidate.description`:

Description
-----------

Wait for the invalidation of an object to complete.

See Documentation/filesystems/caching/netfs-api.txt for a complete
description.

.. _`fscache_reserve_space`:

fscache_reserve_space
=====================

.. c:function:: int fscache_reserve_space(struct fscache_cookie *cookie, loff_t size)

    Reserve data space for a cached object

    :param struct fscache_cookie \*cookie:
        The cookie representing the cache object

    :param loff_t size:
        *undescribed*

.. _`fscache_reserve_space.description`:

Description
-----------

Reserve an amount of space in the cache for the cache object attached to a
cookie so that a write to that object within the space can always be
honoured.

See Documentation/filesystems/caching/netfs-api.txt for a complete
description.

.. _`fscache_read_or_alloc_page`:

fscache_read_or_alloc_page
==========================

.. c:function:: int fscache_read_or_alloc_page(struct fscache_cookie *cookie, struct page *page, fscache_rw_complete_t end_io_func, void *context, gfp_t gfp)

    Read a page from the cache or allocate a block in which to store it

    :param struct fscache_cookie \*cookie:
        The cookie representing the cache object

    :param struct page \*page:
        The netfs page to fill if possible

    :param fscache_rw_complete_t end_io_func:
        The callback to invoke when and if the page is filled

    :param void \*context:
        An arbitrary piece of data to pass on to \ :c:func:`end_io_func`\ 

    :param gfp_t gfp:
        The conditions under which memory allocation should be made

.. _`fscache_read_or_alloc_page.description`:

Description
-----------

Read a page from the cache, or if that's not possible make a potential
one-block reservation in the cache into which the page may be stored once
fetched from the server.

If the page is not backed by the cache object, or if it there's some reason
it can't be, -ENOBUFS will be returned and nothing more will be done for
that page.

Else, if that page is backed by the cache, a read will be initiated directly
to the netfs's page and 0 will be returned by this function.  The
\ :c:func:`end_io_func`\  callback will be invoked when the operation terminates on a
completion or failure.  Note that the callback may be invoked before the
return.

Else, if the page is unbacked, -ENODATA is returned and a block may have
been allocated in the cache.

See Documentation/filesystems/caching/netfs-api.txt for a complete
description.

.. _`fscache_read_or_alloc_pages`:

fscache_read_or_alloc_pages
===========================

.. c:function:: int fscache_read_or_alloc_pages(struct fscache_cookie *cookie, struct address_space *mapping, struct list_head *pages, unsigned *nr_pages, fscache_rw_complete_t end_io_func, void *context, gfp_t gfp)

    Read pages from the cache and/or allocate blocks in which to store them

    :param struct fscache_cookie \*cookie:
        The cookie representing the cache object

    :param struct address_space \*mapping:
        The netfs inode mapping to which the pages will be attached

    :param struct list_head \*pages:
        A list of potential netfs pages to be filled

    :param unsigned \*nr_pages:
        Number of pages to be read and/or allocated

    :param fscache_rw_complete_t end_io_func:
        The callback to invoke when and if each page is filled

    :param void \*context:
        An arbitrary piece of data to pass on to \ :c:func:`end_io_func`\ 

    :param gfp_t gfp:
        The conditions under which memory allocation should be made

.. _`fscache_read_or_alloc_pages.description`:

Description
-----------

Read a set of pages from the cache, or if that's not possible, attempt to
make a potential one-block reservation for each page in the cache into which
that page may be stored once fetched from the server.

If some pages are not backed by the cache object, or if it there's some
reason they can't be, -ENOBUFS will be returned and nothing more will be
done for that pages.

Else, if some of the pages are backed by the cache, a read will be initiated
directly to the netfs's page and 0 will be returned by this function.  The
\ :c:func:`end_io_func`\  callback will be invoked when the operation terminates on a
completion or failure.  Note that the callback may be invoked before the
return.

Else, if a page is unbacked, -ENODATA is returned and a block may have
been allocated in the cache.

Because the function may want to return all of -ENOBUFS, -ENODATA and 0 in
regard to different pages, the return values are prioritised in that order.
Any pages submitted for reading are removed from the pages list.

See Documentation/filesystems/caching/netfs-api.txt for a complete
description.

.. _`fscache_alloc_page`:

fscache_alloc_page
==================

.. c:function:: int fscache_alloc_page(struct fscache_cookie *cookie, struct page *page, gfp_t gfp)

    Allocate a block in which to store a page

    :param struct fscache_cookie \*cookie:
        The cookie representing the cache object

    :param struct page \*page:
        The netfs page to allocate a page for

    :param gfp_t gfp:
        The conditions under which memory allocation should be made

.. _`fscache_alloc_page.description`:

Description
-----------

Request Allocation a block in the cache in which to store a netfs page
without retrieving any contents from the cache.

If the page is not backed by a file then -ENOBUFS will be returned and
nothing more will be done, and no reservation will be made.

Else, a block will be allocated if one wasn't already, and 0 will be
returned

See Documentation/filesystems/caching/netfs-api.txt for a complete
description.

.. _`fscache_readpages_cancel`:

fscache_readpages_cancel
========================

.. c:function:: void fscache_readpages_cancel(struct fscache_cookie *cookie, struct list_head *pages)

    Cancel read/alloc on pages

    :param struct fscache_cookie \*cookie:
        The cookie representing the inode's cache object.

    :param struct list_head \*pages:
        The netfs pages that we canceled write on in \ :c:func:`readpages`\ 

.. _`fscache_readpages_cancel.description`:

Description
-----------

Uncache/unreserve the pages reserved earlier in \ :c:func:`readpages`\  via
\ :c:func:`fscache_readpages_or_alloc`\  and similar.  In most successful caches in
\ :c:func:`readpages`\  this doesn't do anything.  In cases when the underlying netfs's
readahead failed we need to clean up the pagelist (unmark and uncache).

This function may sleep as it may have to clean up disk state.

.. _`fscache_write_page`:

fscache_write_page
==================

.. c:function:: int fscache_write_page(struct fscache_cookie *cookie, struct page *page, loff_t object_size, gfp_t gfp)

    Request storage of a page in the cache

    :param struct fscache_cookie \*cookie:
        The cookie representing the cache object

    :param struct page \*page:
        The netfs page to store

    :param loff_t object_size:
        Updated size of object

    :param gfp_t gfp:
        The conditions under which memory allocation should be made

.. _`fscache_write_page.description`:

Description
-----------

Request the contents of the netfs page be written into the cache.  This
request may be ignored if no cache block is currently allocated, in which
case it will return -ENOBUFS.

If a cache block was already allocated, a write will be initiated and 0 will
be returned.  The PG_fscache_write page bit is set immediately and will then
be cleared at the completion of the write to indicate the success or failure
of the operation.  Note that the completion may happen before the return.

See Documentation/filesystems/caching/netfs-api.txt for a complete
description.

.. _`fscache_uncache_page`:

fscache_uncache_page
====================

.. c:function:: void fscache_uncache_page(struct fscache_cookie *cookie, struct page *page)

    Indicate that caching is no longer required on a page

    :param struct fscache_cookie \*cookie:
        The cookie representing the cache object

    :param struct page \*page:
        The netfs page that was being cached.

.. _`fscache_uncache_page.description`:

Description
-----------

Tell the cache that we no longer want a page to be cached and that it should
remove any knowledge of the netfs page it may have.

Note that this cannot cancel any outstanding I/O operations between this
page and the cache.

See Documentation/filesystems/caching/netfs-api.txt for a complete
description.

.. _`fscache_check_page_write`:

fscache_check_page_write
========================

.. c:function:: bool fscache_check_page_write(struct fscache_cookie *cookie, struct page *page)

    Ask if a page is being writing to the cache

    :param struct fscache_cookie \*cookie:
        The cookie representing the cache object

    :param struct page \*page:
        The netfs page that is being cached.

.. _`fscache_check_page_write.description`:

Description
-----------

Ask the cache if a page is being written to the cache.

See Documentation/filesystems/caching/netfs-api.txt for a complete
description.

.. _`fscache_wait_on_page_write`:

fscache_wait_on_page_write
==========================

.. c:function:: void fscache_wait_on_page_write(struct fscache_cookie *cookie, struct page *page)

    Wait for a page to complete writing to the cache

    :param struct fscache_cookie \*cookie:
        The cookie representing the cache object

    :param struct page \*page:
        The netfs page that is being cached.

.. _`fscache_wait_on_page_write.description`:

Description
-----------

Ask the cache to wake us up when a page is no longer being written to the
cache.

See Documentation/filesystems/caching/netfs-api.txt for a complete
description.

.. _`fscache_maybe_release_page`:

fscache_maybe_release_page
==========================

.. c:function:: bool fscache_maybe_release_page(struct fscache_cookie *cookie, struct page *page, gfp_t gfp)

    Consider releasing a page, cancelling a store

    :param struct fscache_cookie \*cookie:
        The cookie representing the cache object

    :param struct page \*page:
        The netfs page that is being cached.

    :param gfp_t gfp:
        The gfp flags passed to \ :c:func:`releasepage`\ 

.. _`fscache_maybe_release_page.description`:

Description
-----------

Consider releasing a page for the vmscan algorithm, on behalf of the netfs's
\ :c:func:`releasepage`\  call.  A storage request on the page may cancelled if it is
not currently being processed.

The function returns true if the page no longer has a storage request on it,
and false if a storage request is left in place.  If true is returned, the
page will have been passed to \ :c:func:`fscache_uncache_page`\ .  If false is returned
the page cannot be freed yet.

.. _`fscache_uncache_all_inode_pages`:

fscache_uncache_all_inode_pages
===============================

.. c:function:: void fscache_uncache_all_inode_pages(struct fscache_cookie *cookie, struct inode *inode)

    Uncache all an inode's pages

    :param struct fscache_cookie \*cookie:
        The cookie representing the inode's cache object.

    :param struct inode \*inode:
        The inode to uncache pages from.

.. _`fscache_uncache_all_inode_pages.description`:

Description
-----------

Uncache all the pages in an inode that are marked PG_fscache, assuming them
to be associated with the given cookie.

This function may sleep.  It will wait for pages that are being written out
and will wait whilst the PG_fscache mark is removed by the cache.

.. _`fscache_disable_cookie`:

fscache_disable_cookie
======================

.. c:function:: void fscache_disable_cookie(struct fscache_cookie *cookie, const void *aux_data, bool invalidate)

    Disable a cookie

    :param struct fscache_cookie \*cookie:
        The cookie representing the cache object

    :param const void \*aux_data:
        The updated auxiliary data for the cookie (may be NULL)

    :param bool invalidate:
        Invalidate the backing object

.. _`fscache_disable_cookie.description`:

Description
-----------

Disable a cookie from accepting further alloc, read, write, invalidate,
update or acquire operations.  Outstanding operations can still be waited
upon and pages can still be uncached and the cookie relinquished.

This will not return until all outstanding operations have completed.

If \ ``invalidate``\  is set, then the backing object will be invalidated and
detached, otherwise it will just be detached.

If \ ``aux_data``\  is set, then auxiliary data will be updated from that.

.. _`fscache_enable_cookie`:

fscache_enable_cookie
=====================

.. c:function:: void fscache_enable_cookie(struct fscache_cookie *cookie, const void *aux_data, loff_t object_size, bool (*can_enable)(void *data), void *data)

    Reenable a cookie

    :param struct fscache_cookie \*cookie:
        The cookie representing the cache object

    :param const void \*aux_data:
        The updated auxiliary data for the cookie (may be NULL)

    :param loff_t object_size:
        Current size of object

    :param bool (\*can_enable)(void \*data):
        A function to permit enablement once lock is held

    :param void \*data:
        Data for \ :c:func:`can_enable`\ 

.. _`fscache_enable_cookie.description`:

Description
-----------

Reenable a previously disabled cookie, allowing it to accept further alloc,
read, write, invalidate, update or acquire operations.  An attempt will be
made to immediately reattach the cookie to a backing object.  If \ ``aux_data``\ 
is set, the auxiliary data attached to the cookie will be updated.

The \ :c:func:`can_enable`\  function is called (if not NULL) once the enablement lock
is held to rule on whether enablement is still permitted to go ahead.

.. This file was automatic generated / don't edit.

