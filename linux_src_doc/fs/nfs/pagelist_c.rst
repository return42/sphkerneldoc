.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/pagelist.c

.. _`nfs_iocounter_wait`:

nfs_iocounter_wait
==================

.. c:function:: int nfs_iocounter_wait(struct nfs_lock_context *l_ctx)

    wait for i/o to complete

    :param l_ctx:
        nfs_lock_context with io_counter to use
    :type l_ctx: struct nfs_lock_context \*

.. _`nfs_iocounter_wait.description`:

Description
-----------

returns -ERESTARTSYS if interrupted by a fatal signal.
Otherwise returns 0 once the io_count hits 0.

.. _`nfs_async_iocounter_wait`:

nfs_async_iocounter_wait
========================

.. c:function:: bool nfs_async_iocounter_wait(struct rpc_task *task, struct nfs_lock_context *l_ctx)

    wait on a rpc_waitqueue for I/O to complete

    :param task:
        the rpc_task that should wait
    :type task: struct rpc_task \*

    :param l_ctx:
        nfs_lock_context with io_counter to check
    :type l_ctx: struct nfs_lock_context \*

.. _`nfs_async_iocounter_wait.description`:

Description
-----------

Returns true if there is outstanding I/O to wait on and the
task has been put to sleep.

.. _`nfs_create_request`:

nfs_create_request
==================

.. c:function:: struct nfs_page *nfs_create_request(struct nfs_open_context *ctx, struct page *page, struct nfs_page *last, unsigned int offset, unsigned int count)

    Create an NFS read/write request.

    :param ctx:
        open context to use
    :type ctx: struct nfs_open_context \*

    :param page:
        page to write
    :type page: struct page \*

    :param last:
        last nfs request created for this page group or NULL if head
    :type last: struct nfs_page \*

    :param offset:
        starting offset within the page for the write
    :type offset: unsigned int

    :param count:
        number of bytes to read/write
    :type count: unsigned int

.. _`nfs_create_request.description`:

Description
-----------

The page must be locked by the caller. This makes sure we never
create two different requests for the same page.
User should ensure it is safe to sleep in this function.

.. _`nfs_unlock_request`:

nfs_unlock_request
==================

.. c:function:: void nfs_unlock_request(struct nfs_page *req)

    Unlock request and wake up sleepers.

    :param req:
        *undescribed*
    :type req: struct nfs_page \*

.. _`nfs_unlock_and_release_request`:

nfs_unlock_and_release_request
==============================

.. c:function:: void nfs_unlock_and_release_request(struct nfs_page *req)

    Unlock request and release the nfs_page

    :param req:
        *undescribed*
    :type req: struct nfs_page \*

.. _`nfs_free_request`:

nfs_free_request
================

.. c:function:: void nfs_free_request(struct nfs_page *req)

    Release the count on an NFS read/write request

    :param req:
        request to release
    :type req: struct nfs_page \*

.. _`nfs_free_request.note`:

Note
----

Should never be called with the spinlock held!

.. _`nfs_wait_on_request`:

nfs_wait_on_request
===================

.. c:function:: int nfs_wait_on_request(struct nfs_page *req)

    Wait for a request to complete.

    :param req:
        request to wait upon.
    :type req: struct nfs_page \*

.. _`nfs_wait_on_request.description`:

Description
-----------

Interruptible by fatal signals only.
The user is responsible for holding a count on the request.

.. _`nfs_pgio_data_destroy`:

nfs_pgio_data_destroy
=====================

.. c:function:: void nfs_pgio_data_destroy(struct nfs_pgio_header *hdr)

    make \ ``hdr``\  suitable for reuse

    :param hdr:
        A header that has had nfs_generic_pgio called
    :type hdr: struct nfs_pgio_header \*

.. _`nfs_pgio_data_destroy.description`:

Description
-----------

Frees memory and releases refs from nfs_generic_pgio, so that it may
be called again.

.. _`nfs_pgio_rpcsetup`:

nfs_pgio_rpcsetup
=================

.. c:function:: void nfs_pgio_rpcsetup(struct nfs_pgio_header *hdr, unsigned int count, int how, struct nfs_commit_info *cinfo)

    Set up arguments for a pageio call

    :param hdr:
        The pageio hdr
    :type hdr: struct nfs_pgio_header \*

    :param count:
        Number of bytes to read
    :type count: unsigned int

    :param how:
        How to commit data (writes only)
    :type how: int

    :param cinfo:
        Commit information for the call (writes only)
    :type cinfo: struct nfs_commit_info \*

.. _`nfs_pgio_prepare`:

nfs_pgio_prepare
================

.. c:function:: void nfs_pgio_prepare(struct rpc_task *task, void *calldata)

    Prepare pageio hdr to go over the wire

    :param task:
        The current task
    :type task: struct rpc_task \*

    :param calldata:
        pageio header to prepare
    :type calldata: void \*

.. _`nfs_pgio_error`:

nfs_pgio_error
==============

.. c:function:: void nfs_pgio_error(struct nfs_pgio_header *hdr)

    Clean up from a pageio error

    :param hdr:
        pageio header
    :type hdr: struct nfs_pgio_header \*

.. _`nfs_pgio_release`:

nfs_pgio_release
================

.. c:function:: void nfs_pgio_release(void *calldata)

    Release pageio data

    :param calldata:
        The pageio header to release
    :type calldata: void \*

.. _`nfs_pageio_init`:

nfs_pageio_init
===============

.. c:function:: void nfs_pageio_init(struct nfs_pageio_descriptor *desc, struct inode *inode, const struct nfs_pageio_ops *pg_ops, const struct nfs_pgio_completion_ops *compl_ops, const struct nfs_rw_ops *rw_ops, size_t bsize, int io_flags)

    initialise a page io descriptor

    :param desc:
        pointer to descriptor
    :type desc: struct nfs_pageio_descriptor \*

    :param inode:
        pointer to inode
    :type inode: struct inode \*

    :param pg_ops:
        pointer to pageio operations
    :type pg_ops: const struct nfs_pageio_ops \*

    :param compl_ops:
        pointer to pageio completion operations
    :type compl_ops: const struct nfs_pgio_completion_ops \*

    :param rw_ops:
        pointer to nfs read/write operations
    :type rw_ops: const struct nfs_rw_ops \*

    :param bsize:
        io block size
    :type bsize: size_t

    :param io_flags:
        extra parameters for the io function
    :type io_flags: int

.. _`nfs_pgio_result`:

nfs_pgio_result
===============

.. c:function:: void nfs_pgio_result(struct rpc_task *task, void *calldata)

    Basic pageio error handling

    :param task:
        The task that ran
    :type task: struct rpc_task \*

    :param calldata:
        Pageio header to check
    :type calldata: void \*

.. _`nfs_can_coalesce_requests`:

nfs_can_coalesce_requests
=========================

.. c:function:: bool nfs_can_coalesce_requests(struct nfs_page *prev, struct nfs_page *req, struct nfs_pageio_descriptor *pgio)

    test two requests for compatibility

    :param prev:
        pointer to nfs_page
    :type prev: struct nfs_page \*

    :param req:
        pointer to nfs_page
    :type req: struct nfs_page \*

    :param pgio:
        *undescribed*
    :type pgio: struct nfs_pageio_descriptor \*

.. _`nfs_can_coalesce_requests.description`:

Description
-----------

The nfs_page structures 'prev' and 'req' are compared to ensure that the
page data area they describe is contiguous, and that their RPC
credentials, NFSv4 open state, and lockowners are the same.

Return 'true' if this is the case, else return 'false'.

.. _`nfs_pageio_do_add_request`:

nfs_pageio_do_add_request
=========================

.. c:function:: int nfs_pageio_do_add_request(struct nfs_pageio_descriptor *desc, struct nfs_page *req)

    Attempt to coalesce a request into a page list.

    :param desc:
        destination io descriptor
    :type desc: struct nfs_pageio_descriptor \*

    :param req:
        request
    :type req: struct nfs_page \*

.. _`nfs_pageio_do_add_request.description`:

Description
-----------

Returns true if the request 'req' was successfully coalesced into the
existing list of pages 'desc'.

.. _`__nfs_pageio_add_request`:

\__nfs_pageio_add_request
=========================

.. c:function:: int __nfs_pageio_add_request(struct nfs_pageio_descriptor *desc, struct nfs_page *req)

    Attempt to coalesce a request into a page list.

    :param desc:
        destination io descriptor
    :type desc: struct nfs_pageio_descriptor \*

    :param req:
        request
    :type req: struct nfs_page \*

.. _`__nfs_pageio_add_request.description`:

Description
-----------

This may split a request into subrequests which are all part of the
same page group.

Returns true if the request 'req' was successfully coalesced into the
existing list of pages 'desc'.

.. _`nfs_pageio_complete`:

nfs_pageio_complete
===================

.. c:function:: void nfs_pageio_complete(struct nfs_pageio_descriptor *desc)

    Complete I/O then cleanup an nfs_pageio_descriptor

    :param desc:
        pointer to io descriptor
    :type desc: struct nfs_pageio_descriptor \*

.. _`nfs_pageio_cond_complete`:

nfs_pageio_cond_complete
========================

.. c:function:: void nfs_pageio_cond_complete(struct nfs_pageio_descriptor *desc, pgoff_t index)

    Conditional I/O completion

    :param desc:
        pointer to io descriptor
    :type desc: struct nfs_pageio_descriptor \*

    :param index:
        page index
    :type index: pgoff_t

.. _`nfs_pageio_cond_complete.description`:

Description
-----------

It is important to ensure that processes don't try to take locks
on non-contiguous ranges of pages as that might deadlock. This
function should be called before attempting to wait on a locked
nfs_page. It will complete the I/O if the page index 'index'
is not contiguous with the existing list of pages in 'desc'.

.. This file was automatic generated / don't edit.

