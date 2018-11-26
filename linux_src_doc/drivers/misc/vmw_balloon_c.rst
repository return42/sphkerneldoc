.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/vmw_balloon.c

.. _`vmballoon_cmd_type`:

enum vmballoon_cmd_type
=======================

.. c:type:: enum vmballoon_cmd_type

    backdoor commands.

.. _`vmballoon_cmd_type.definition`:

Definition
----------

.. code-block:: c

    enum vmballoon_cmd_type {
        VMW_BALLOON_CMD_START,
        VMW_BALLOON_CMD_GET_TARGET,
        VMW_BALLOON_CMD_LOCK,
        VMW_BALLOON_CMD_UNLOCK,
        VMW_BALLOON_CMD_GUEST_ID,
        VMW_BALLOON_CMD_BATCHED_LOCK,
        VMW_BALLOON_CMD_BATCHED_UNLOCK,
        VMW_BALLOON_CMD_BATCHED_2M_LOCK,
        VMW_BALLOON_CMD_BATCHED_2M_UNLOCK,
        VMW_BALLOON_CMD_VMCI_DOORBELL_SET,
        VMW_BALLOON_CMD_LAST
    };

.. _`vmballoon_cmd_type.constants`:

Constants
---------

VMW_BALLOON_CMD_START
    Communicating supported version with the hypervisor.

VMW_BALLOON_CMD_GET_TARGET
    Gets the balloon target size.

VMW_BALLOON_CMD_LOCK
    Informs the hypervisor about a ballooned page.

VMW_BALLOON_CMD_UNLOCK
    Informs the hypervisor about a page that is about
    to be deflated from the balloon.

VMW_BALLOON_CMD_GUEST_ID
    Informs the hypervisor about the type of OS that
    runs in the VM.

VMW_BALLOON_CMD_BATCHED_LOCK
    Inform the hypervisor about a batch of
    ballooned pages (up to 512).

VMW_BALLOON_CMD_BATCHED_UNLOCK
    Inform the hypervisor about a batch of
    pages that are about to be deflated from the
    balloon (up to 512).

VMW_BALLOON_CMD_BATCHED_2M_LOCK
    Similar to \ ``VMW_BALLOON_CMD_BATCHED_LOCK``\ 
    for 2MB pages.

VMW_BALLOON_CMD_BATCHED_2M_UNLOCK
    Similar to
    \ ``VMW_BALLOON_CMD_BATCHED_UNLOCK``\  for 2MB
    pages.

VMW_BALLOON_CMD_VMCI_DOORBELL_SET
    A command to set doorbell notification
    that would be invoked when the balloon
    size changes.

VMW_BALLOON_CMD_LAST
    Value of the last command.

.. _`vmballoon_cmd_type.availability-of-the-commands-is-as-followed`:

Availability of the commands is as followed
-------------------------------------------


\ ``VMW_BALLOON_CMD_START``\ , \ ``VMW_BALLOON_CMD_GET_TARGET``\  and
\ ``VMW_BALLOON_CMD_GUEST_ID``\  are always available.

If the host reports \ ``VMW_BALLOON_BASIC_CMDS``\  are supported then
\ ``VMW_BALLOON_CMD_LOCK``\  and \ ``VMW_BALLOON_CMD_UNLOCK``\  commands are available.

If the host reports \ ``VMW_BALLOON_BATCHED_CMDS``\  are supported then
\ ``VMW_BALLOON_CMD_BATCHED_LOCK``\  and VMW_BALLOON_CMD_BATCHED_UNLOCK commands
are available.

If the host reports \ ``VMW_BALLOON_BATCHED_2M_CMDS``\  are supported then
\ ``VMW_BALLOON_CMD_BATCHED_2M_LOCK``\  and \ ``VMW_BALLOON_CMD_BATCHED_2M_UNLOCK``\ 
are supported.

If the host reports  VMW_BALLOON_SIGNALLED_WAKEUP_CMD is supported then
VMW_BALLOON_CMD_VMCI_DOORBELL_SET command is supported.

.. _`vmballoon_batch_entry`:

struct vmballoon_batch_entry
============================

.. c:type:: struct vmballoon_batch_entry

    a batch entry for lock or unlock.

.. _`vmballoon_batch_entry.definition`:

Definition
----------

.. code-block:: c

    struct vmballoon_batch_entry {
        u64 status : 5;
        u64 reserved : PAGE_SHIFT - 5;
        u64 pfn : 52;
    }

.. _`vmballoon_batch_entry.members`:

Members
-------

status
    the status of the operation, which is written by the hypervisor.

5
    *undescribed*

pfn
    the physical frame number of the page to be locked or unlocked.

.. _`vmballoon_send_guest_id`:

vmballoon_send_guest_id
=======================

.. c:function:: int vmballoon_send_guest_id(struct vmballoon *b)

    communicate guest type to the host.

    :param b:
        pointer to the balloon.
    :type b: struct vmballoon \*

.. _`vmballoon_send_guest_id.description`:

Description
-----------

Communicate guest type to the host so that it can adjust ballooning
algorithm to the one most appropriate for the guest. This command
is normally issued after sending "start" command and is part of
standard reset sequence.

.. _`vmballoon_send_guest_id.return`:

Return
------

zero on success or appropriate error code.

.. _`vmballoon_page_order`:

vmballoon_page_order
====================

.. c:function:: unsigned int vmballoon_page_order(enum vmballoon_page_size_type page_size)

    return the order of the page

    :param page_size:
        the size of the page.
    :type page_size: enum vmballoon_page_size_type

.. _`vmballoon_page_order.return`:

Return
------

the allocation order.

.. _`vmballoon_page_in_frames`:

vmballoon_page_in_frames
========================

.. c:function:: unsigned int vmballoon_page_in_frames(enum vmballoon_page_size_type page_size)

    returns the number of frames in a page.

    :param page_size:
        the size of the page.
    :type page_size: enum vmballoon_page_size_type

.. _`vmballoon_page_in_frames.return`:

Return
------

the number of 4k frames.

.. _`vmballoon_send_get_target`:

vmballoon_send_get_target
=========================

.. c:function:: int vmballoon_send_get_target(struct vmballoon *b)

    Retrieve desired balloon size from the host.

    :param b:
        pointer to the balloon.
    :type b: struct vmballoon \*

.. _`vmballoon_send_get_target.return`:

Return
------

zero on success, EINVAL if limit does not fit in 32-bit, as required
by the host-guest protocol and EIO if an error occurred in communicating with
the host.

.. _`vmballoon_alloc_page_list`:

vmballoon_alloc_page_list
=========================

.. c:function:: int vmballoon_alloc_page_list(struct vmballoon *b, struct vmballoon_ctl *ctl, unsigned int req_n_pages)

    allocates a list of pages.

    :param b:
        pointer to the balloon.
    :type b: struct vmballoon \*

    :param ctl:
        pointer for the \ ``struct``\  vmballoon_ctl, which defines the operation.
    :type ctl: struct vmballoon_ctl \*

    :param req_n_pages:
        the number of requested pages.
    :type req_n_pages: unsigned int

.. _`vmballoon_alloc_page_list.description`:

Description
-----------

Tries to allocate \ ``req_n_pages``\ . Add them to the list of balloon pages in
\ ``ctl.pages``\  and updates \ ``ctl.n_pages``\  to reflect the number of pages.

.. _`vmballoon_alloc_page_list.return`:

Return
------

zero on success or error code otherwise.

.. _`vmballoon_handle_one_result`:

vmballoon_handle_one_result
===========================

.. c:function:: int vmballoon_handle_one_result(struct vmballoon *b, struct page *page, enum vmballoon_page_size_type page_size, unsigned long status)

    Handle lock/unlock result for a single page.

    :param b:
        pointer for \ ``struct``\  vmballoon.
    :type b: struct vmballoon \*

    :param page:
        pointer for the page whose result should be handled.
    :type page: struct page \*

    :param page_size:
        size of the page.
    :type page_size: enum vmballoon_page_size_type

    :param status:
        status of the operation as provided by the hypervisor.
    :type status: unsigned long

.. _`vmballoon_status_page`:

vmballoon_status_page
=====================

.. c:function:: unsigned long vmballoon_status_page(struct vmballoon *b, int idx, struct page **p)

    returns the status of (un)lock operation

    :param b:
        pointer to the balloon.
    :type b: struct vmballoon \*

    :param idx:
        index for the page for which the operation is performed.
    :type idx: int

    :param p:
        pointer to where the page struct is returned.
    :type p: struct page \*\*

.. _`vmballoon_status_page.description`:

Description
-----------

Following a lock or unlock operation, returns the status of the operation for
an individual page. Provides the page that the operation was performed on on
the \ ``page``\  argument.

.. _`vmballoon_status_page.return`:

Return
------

The status of a lock or unlock operation for an individual page.

.. _`vmballoon_lock_op`:

vmballoon_lock_op
=================

.. c:function:: unsigned long vmballoon_lock_op(struct vmballoon *b, unsigned int num_pages, enum vmballoon_page_size_type page_size, enum vmballoon_op op)

    notifies the host about inflated/deflated pages.

    :param b:
        pointer to the balloon.
    :type b: struct vmballoon \*

    :param num_pages:
        number of inflated/deflated pages.
    :type num_pages: unsigned int

    :param page_size:
        size of the page.
    :type page_size: enum vmballoon_page_size_type

    :param op:
        the type of operation (lock or unlock).
    :type op: enum vmballoon_op

.. _`vmballoon_lock_op.description`:

Description
-----------

Notify the host about page(s) that were ballooned (or removed from the
balloon) so that host can use it without fear that guest will need it (or
stop using them since the VM does). Host may reject some pages, we need to
check the return value and maybe submit a different page. The pages that are
inflated/deflated are pointed by \ ``b->page``\ .

.. _`vmballoon_lock_op.return`:

Return
------

result as provided by the hypervisor.

.. _`vmballoon_add_page`:

vmballoon_add_page
==================

.. c:function:: void vmballoon_add_page(struct vmballoon *b, unsigned int idx, struct page *p)

    adds a page towards lock/unlock operation.

    :param b:
        pointer to the balloon.
    :type b: struct vmballoon \*

    :param idx:
        index of the page to be ballooned in this batch.
    :type idx: unsigned int

    :param p:
        pointer to the page that is about to be ballooned.
    :type p: struct page \*

.. _`vmballoon_add_page.description`:

Description
-----------

Adds the page to be ballooned. Must be called while holding \ ``comm_lock``\ .

.. _`vmballoon_lock`:

vmballoon_lock
==============

.. c:function:: int vmballoon_lock(struct vmballoon *b, struct vmballoon_ctl *ctl)

    lock or unlock a batch of pages.

    :param b:
        pointer to the balloon.
    :type b: struct vmballoon \*

    :param ctl:
        pointer for the \ ``struct``\  vmballoon_ctl, which defines the operation.
    :type ctl: struct vmballoon_ctl \*

.. _`vmballoon_lock.description`:

Description
-----------

Notifies the host of about ballooned pages (after inflation or deflation,
according to \ ``ctl``\ ). If the host rejects the page put it on the
\ ``ctl``\  refuse list. These refused page are then released when moving to the
next size of pages.

Note that we neither free any \ ``page``\  here nor put them back on the ballooned
pages list. Instead we queue it for later processing. We do that for several
reasons. First, we do not want to free the page under the lock. Second, it
allows us to unify the handling of lock and unlock. In the inflate case, the
caller will check if there are too many refused pages and release them.
Although it is not identical to the past behavior, it should not affect
performance.

.. _`vmballoon_release_page_list`:

vmballoon_release_page_list
===========================

.. c:function:: void vmballoon_release_page_list(struct list_head *page_list, int *n_pages, enum vmballoon_page_size_type page_size)

    Releases a page list

    :param page_list:
        list of pages to release.
    :type page_list: struct list_head \*

    :param n_pages:
        pointer to the number of pages.
    :type n_pages: int \*

    :param page_size:
        whether the pages in the list are 2MB (or else 4KB).
    :type page_size: enum vmballoon_page_size_type

.. _`vmballoon_release_page_list.description`:

Description
-----------

Releases the list of pages and zeros the number of pages.

.. _`vmballoon_change`:

vmballoon_change
================

.. c:function:: int64_t vmballoon_change(struct vmballoon *b)

    retrieve the required balloon change

    :param b:
        pointer for the balloon.
    :type b: struct vmballoon \*

.. _`vmballoon_change.return`:

Return
------

the required change for the balloon size. A positive number
indicates inflation, a negative number indicates a deflation.

.. _`vmballoon_enqueue_page_list`:

vmballoon_enqueue_page_list
===========================

.. c:function:: void vmballoon_enqueue_page_list(struct vmballoon *b, struct list_head *pages, unsigned int *n_pages, enum vmballoon_page_size_type page_size)

    Enqueues list of pages after inflation.

    :param b:
        pointer to balloon.
    :type b: struct vmballoon \*

    :param pages:
        list of pages to enqueue.
    :type pages: struct list_head \*

    :param n_pages:
        pointer to number of pages in list. The value is zeroed.
    :type n_pages: unsigned int \*

    :param page_size:
        whether the pages are 2MB or 4KB pages.
    :type page_size: enum vmballoon_page_size_type

.. _`vmballoon_enqueue_page_list.description`:

Description
-----------

Enqueues the provides list of pages in the ballooned page list, clears the
list and zeroes the number of pages that was provided.

.. _`vmballoon_dequeue_page_list`:

vmballoon_dequeue_page_list
===========================

.. c:function:: void vmballoon_dequeue_page_list(struct vmballoon *b, struct list_head *pages, unsigned int *n_pages, enum vmballoon_page_size_type page_size, unsigned int n_req_pages)

    Dequeues page lists for deflation.

    :param b:
        pointer to balloon.
    :type b: struct vmballoon \*

    :param pages:
        list of pages to enqueue.
    :type pages: struct list_head \*

    :param n_pages:
        pointer to number of pages in list. The value is zeroed.
    :type n_pages: unsigned int \*

    :param page_size:
        whether the pages are 2MB or 4KB pages.
    :type page_size: enum vmballoon_page_size_type

    :param n_req_pages:
        the number of requested pages.
    :type n_req_pages: unsigned int

.. _`vmballoon_dequeue_page_list.description`:

Description
-----------

Dequeues the number of requested pages from the balloon for deflation. The
number of dequeued pages may be lower, if not enough pages in the requested
size are available.

.. _`vmballoon_inflate`:

vmballoon_inflate
=================

.. c:function:: void vmballoon_inflate(struct vmballoon *b)

    Inflate the balloon towards its target size.

    :param b:
        pointer to the balloon.
    :type b: struct vmballoon \*

.. _`vmballoon_deflate`:

vmballoon_deflate
=================

.. c:function:: unsigned long vmballoon_deflate(struct vmballoon *b, uint64_t n_frames, bool coordinated)

    Decrease the size of the balloon.

    :param b:
        pointer to the balloon
    :type b: struct vmballoon \*

    :param n_frames:
        the number of frames to deflate. If zero, automatically
        calculated according to the target size.
    :type n_frames: uint64_t

    :param coordinated:
        whether to coordinate with the host
    :type coordinated: bool

.. _`vmballoon_deflate.description`:

Description
-----------

Decrease the size of the balloon allowing guest to use more memory.

.. _`vmballoon_deflate.return`:

Return
------

The number of deflated frames (i.e., basic page size units)

.. _`vmballoon_deinit_batching`:

vmballoon_deinit_batching
=========================

.. c:function:: void vmballoon_deinit_batching(struct vmballoon *b)

    disables batching mode.

    :param b:
        pointer to \ :c:type:`struct vmballoon <vmballoon>`\ .
    :type b: struct vmballoon \*

.. _`vmballoon_deinit_batching.description`:

Description
-----------

Disables batching, by deallocating the page for communication with the
hypervisor and disabling the static key to indicate that batching is off.

.. _`vmballoon_init_batching`:

vmballoon_init_batching
=======================

.. c:function:: int vmballoon_init_batching(struct vmballoon *b)

    enable batching mode.

    :param b:
        pointer to \ :c:type:`struct vmballoon <vmballoon>`\ .
    :type b: struct vmballoon \*

.. _`vmballoon_init_batching.description`:

Description
-----------

Enables batching, by allocating a page for communication with the hypervisor
and enabling the static_key to use batching.

.. _`vmballoon_init_batching.return`:

Return
------

zero on success or an appropriate error-code.

.. _`vmballoon_vmci_init`:

vmballoon_vmci_init
===================

.. c:function:: int vmballoon_vmci_init(struct vmballoon *b)

    Initialize vmci doorbell.

    :param b:
        pointer to the balloon.
    :type b: struct vmballoon \*

.. _`vmballoon_vmci_init.return`:

Return
------

zero on success or when wakeup command not supported. Error-code
otherwise.

Initialize vmci doorbell, to get notified as soon as balloon changes.

.. _`vmballoon_pop`:

vmballoon_pop
=============

.. c:function:: void vmballoon_pop(struct vmballoon *b)

    Quickly release all pages allocate for the balloon.

    :param b:
        pointer to the balloon.
    :type b: struct vmballoon \*

.. _`vmballoon_pop.description`:

Description
-----------

This function is called when host decides to "reset" balloon for one reason
or another. Unlike normal "deflate" we do not (shall not) notify host of the
pages being released.

.. _`vmballoon_work`:

vmballoon_work
==============

.. c:function:: void vmballoon_work(struct work_struct *work)

    periodic balloon worker for reset, inflation and deflation.

    :param work:
        pointer to the \ :c:type:`struct work_struct <work_struct>`\  which is provided by the workqueue.
    :type work: struct work_struct \*

.. _`vmballoon_work.description`:

Description
-----------

Resets the protocol if needed, gets the new size and adjusts balloon as
needed. Repeat in 1 sec.

.. _`vmballoon_debug_show`:

vmballoon_debug_show
====================

.. c:function:: int vmballoon_debug_show(struct seq_file *f, void *offset)

    shows statistics of balloon operations.

    :param f:
        pointer to the \ :c:type:`struct seq_file <seq_file>`\ .
    :type f: struct seq_file \*

    :param offset:
        ignored.
    :type offset: void \*

.. _`vmballoon_debug_show.description`:

Description
-----------

Provides the statistics that can be accessed in vmmemctl in the debugfs.
To avoid the overhead - mainly that of memory - of collecting the statistics,
we only collect statistics after the first time the counters are read.

.. _`vmballoon_debug_show.return`:

Return
------

zero on success or an error code.

.. This file was automatic generated / don't edit.

