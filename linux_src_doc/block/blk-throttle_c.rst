.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-throttle.c

.. _`sq_to_tg`:

sq_to_tg
========

.. c:function:: struct throtl_grp *sq_to_tg(struct throtl_service_queue *sq)

    return the throl_grp the specified service queue belongs to

    :param struct throtl_service_queue \*sq:
        the throtl_service_queue of interest

.. _`sq_to_tg.description`:

Description
-----------

Return the throtl_grp \ ``sq``\  belongs to.  If \ ``sq``\  is the top-level one
embedded in throtl_data, \ ``NULL``\  is returned.

.. _`sq_to_td`:

sq_to_td
========

.. c:function:: struct throtl_data *sq_to_td(struct throtl_service_queue *sq)

    return throtl_data the specified service queue belongs to

    :param struct throtl_service_queue \*sq:
        the throtl_service_queue of interest

.. _`sq_to_td.description`:

Description
-----------

A service_queue can be embeded in either a throtl_grp or throtl_data.
Determine the associated throtl_data accordingly and return it.

.. _`throtl_log`:

throtl_log
==========

.. c:function::  throtl_log( sq,  fmt,  args...)

    log debug message via blktrace

    :param  sq:
        the service_queue being reported

    :param  fmt:
        printf format string

    :param  args...:
        variable arguments

.. _`throtl_log.description`:

Description
-----------

The messages are prefixed with "throtl BLKG_NAME" if \ ``sq``\  belongs to a
throtl_grp; otherwise, just "throtl".

.. _`throtl_qnode_add_bio`:

throtl_qnode_add_bio
====================

.. c:function:: void throtl_qnode_add_bio(struct bio *bio, struct throtl_qnode *qn, struct list_head *queued)

    add a bio to a throtl_qnode and activate it

    :param struct bio \*bio:
        bio being added

    :param struct throtl_qnode \*qn:
        qnode to add bio to

    :param struct list_head \*queued:
        the service_queue->queued[] list \ ``qn``\  belongs to

.. _`throtl_qnode_add_bio.description`:

Description
-----------

Add \ ``bio``\  to \ ``qn``\  and put \ ``qn``\  on \ ``queued``\  if it's not already on.
\ ``qn``\ ->tg's reference count is bumped when \ ``qn``\  is activated.  See the
comment on top of throtl_qnode definition for details.

.. _`throtl_peek_queued`:

throtl_peek_queued
==================

.. c:function:: struct bio *throtl_peek_queued(struct list_head *queued)

    peek the first bio on a qnode list

    :param struct list_head \*queued:
        the qnode list to peek

.. _`throtl_pop_queued`:

throtl_pop_queued
=================

.. c:function:: struct bio *throtl_pop_queued(struct list_head *queued, struct throtl_grp **tg_to_put)

    pop the first bio form a qnode list

    :param struct list_head \*queued:
        the qnode list to pop a bio from

    :param struct throtl_grp \*\*tg_to_put:
        optional out argument for throtl_grp to put

.. _`throtl_pop_queued.description`:

Description
-----------

Pop the first bio from the qnode list \ ``queued``\ .  After popping, the first
qnode is removed from \ ``queued``\  if empty or moved to the end of \ ``queued``\  so
that the popping order is round-robin.

When the first qnode is removed, its associated throtl_grp should be put
too.  If \ ``tg_to_put``\  is NULL, this function automatically puts it;
otherwise, \*@tg_to_put is set to the throtl_grp to put and the caller is
responsible for putting it.

.. _`throtl_schedule_next_dispatch`:

throtl_schedule_next_dispatch
=============================

.. c:function:: bool throtl_schedule_next_dispatch(struct throtl_service_queue *sq, bool force)

    schedule the next dispatch cycle

    :param struct throtl_service_queue \*sq:
        the service_queue to schedule dispatch for

    :param bool force:
        force scheduling

.. _`throtl_schedule_next_dispatch.description`:

Description
-----------

Arm \ ``sq``\ ->pending_timer so that the next dispatch cycle starts on the
dispatch time of the first pending child.  Returns \ ``true``\  if either timer
is armed or there's no pending child left.  \ ``false``\  if the current
dispatch window is still open and the caller should continue
dispatching.

If \ ``force``\  is \ ``true``\ , the dispatch timer is always scheduled and this
function is guaranteed to return \ ``true``\ .  This is to be used when the
caller can't dispatch itself and needs to invoke pending_timer
unconditionally.  Note that forced scheduling is likely to induce short
delay before dispatch starts even if \ ``sq``\ ->first_pending_disptime is not
in the future and thus shouldn't be used in hot paths.

.. _`throtl_add_bio_tg`:

throtl_add_bio_tg
=================

.. c:function:: void throtl_add_bio_tg(struct bio *bio, struct throtl_qnode *qn, struct throtl_grp *tg)

    add a bio to the specified throtl_grp

    :param struct bio \*bio:
        bio to add

    :param struct throtl_qnode \*qn:
        qnode to use

    :param struct throtl_grp \*tg:
        the target throtl_grp

.. _`throtl_add_bio_tg.description`:

Description
-----------

Add \ ``bio``\  to \ ``tg``\ 's service_queue using \ ``qn``\ .  If \ ``qn``\  is not specified,
tg->qnode_on_self[] is used.

.. _`throtl_pending_timer_fn`:

throtl_pending_timer_fn
=======================

.. c:function:: void throtl_pending_timer_fn(unsigned long arg)

    timer function for service_queue->pending_timer

    :param unsigned long arg:
        the throtl_service_queue being serviced

.. _`throtl_pending_timer_fn.description`:

Description
-----------

This timer is armed when a child throtl_grp with active bio's become
pending and queued on the service_queue's pending_tree and expires when
the first child throtl_grp should be dispatched.  This function
dispatches bio's from the children throtl_grps to the parent
service_queue.

If the parent's parent is another throtl_grp, dispatching is propagated
by either arming its pending_timer or repeating dispatch directly.  If
the top-level service_tree is reached, throtl_data->dispatch_work is
kicked so that the ready bio's are issued.

.. _`blk_throtl_dispatch_work_fn`:

blk_throtl_dispatch_work_fn
===========================

.. c:function:: void blk_throtl_dispatch_work_fn(struct work_struct *work)

    work function for throtl_data->dispatch_work

    :param struct work_struct \*work:
        work item being executed

.. _`blk_throtl_dispatch_work_fn.description`:

Description
-----------

This function is queued for execution when bio's reach the bio_lists[]
of throtl_data->service_queue.  Those bio's are ready and issued by this
function.

.. _`blk_throtl_drain`:

blk_throtl_drain
================

.. c:function:: void blk_throtl_drain(struct request_queue *q)

    drain throttled bios

    :param struct request_queue \*q:
        request_queue to drain throttled bios for

.. _`blk_throtl_drain.description`:

Description
-----------

Dispatch all currently throttled bios on \ ``q``\  through ->make_request_fn().

.. This file was automatic generated / don't edit.

