.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/soc/fsl/qman.h

.. _`qman_p_irqsource_add`:

qman_p_irqsource_add
====================

.. c:function:: void qman_p_irqsource_add(struct qman_portal *p, u32 bits)

    add processing sources to be interrupt-driven

    :param struct qman_portal \*p:
        *undescribed*

    :param u32 bits:
        bitmask of QM_PIRQ\_\*\*I processing sources

.. _`qman_p_irqsource_add.description`:

Description
-----------

Adds processing sources that should be interrupt-driven (rather than
processed via qman_poll\_\*\*\*() functions).

.. _`qman_p_irqsource_remove`:

qman_p_irqsource_remove
=======================

.. c:function:: void qman_p_irqsource_remove(struct qman_portal *p, u32 bits)

    remove processing sources from being int-driven

    :param struct qman_portal \*p:
        *undescribed*

    :param u32 bits:
        bitmask of QM_PIRQ\_\*\*I processing sources

.. _`qman_p_irqsource_remove.description`:

Description
-----------

Removes processing sources from being interrupt-driven, so that they will
instead be processed via qman_poll\_\*\*\*() functions.

.. _`qman_affine_cpus`:

qman_affine_cpus
================

.. c:function:: const cpumask_t *qman_affine_cpus( void)

    return a mask of cpus that have affine portals

    :param  void:
        no arguments

.. _`qman_affine_channel`:

qman_affine_channel
===================

.. c:function:: u16 qman_affine_channel(int cpu)

    return the channel ID of an portal

    :param int cpu:
        the cpu whose affine portal is the subject of the query

.. _`qman_affine_channel.description`:

Description
-----------

If \ ``cpu``\  is -1, the affine portal for the current CPU will be used. It is a
bug to call this function for any value of \ ``cpu``\  (other than -1) that is not a
member of the mask returned from \ :c:func:`qman_affine_cpus`\ .

.. _`qman_get_affine_portal`:

qman_get_affine_portal
======================

.. c:function:: struct qman_portal *qman_get_affine_portal(int cpu)

    return the portal pointer affine to cpu

    :param int cpu:
        the cpu whose affine portal is the subject of the query

.. _`qman_p_poll_dqrr`:

qman_p_poll_dqrr
================

.. c:function:: int qman_p_poll_dqrr(struct qman_portal *p, unsigned int limit)

    process DQRR (fast-path) entries

    :param struct qman_portal \*p:
        *undescribed*

    :param unsigned int limit:
        the maximum number of DQRR entries to process

.. _`qman_p_poll_dqrr.description`:

Description
-----------

Use of this function requires that DQRR processing not be interrupt-driven.
The return value represents the number of DQRR entries processed.

.. _`qman_p_static_dequeue_add`:

qman_p_static_dequeue_add
=========================

.. c:function:: void qman_p_static_dequeue_add(struct qman_portal *p, u32 pools)

    Add pool channels to the portal SDQCR

    :param struct qman_portal \*p:
        *undescribed*

    :param u32 pools:
        bit-mask of pool channels, using QM_SDQCR_CHANNELS_POOL(n)

.. _`qman_p_static_dequeue_add.description`:

Description
-----------

Adds a set of pool channels to the portal's static dequeue command register
(SDQCR). The requested pools are limited to those the portal has dequeue
access to.

.. _`qman_create_fq`:

qman_create_fq
==============

.. c:function:: int qman_create_fq(u32 fqid, u32 flags, struct qman_fq *fq)

    Allocates a FQ

    :param u32 fqid:
        the index of the FQD to encapsulate, must be "Out of Service"

    :param u32 flags:
        bit-mask of QMAN_FQ_FLAG\_\*\*\* options

    :param struct qman_fq \*fq:
        memory for storing the 'fq', with callbacks filled in

.. _`qman_create_fq.description`:

Description
-----------

Creates a frame queue object for the given \ ``fqid``\ , unless the
QMAN_FQ_FLAG_DYNAMIC_FQID flag is set in \ ``flags``\ , in which case a FQID is
dynamically allocated (or the function fails if none are available). Once
created, the caller should not touch the memory at 'fq' except as extended to
adjacent memory for user-defined fields (see the definition of "struct
qman_fq" for more info). NO_MODIFY is only intended for enqueuing to
pre-existing frame-queues that aren't to be otherwise interfered with, it
prevents all other modifications to the frame queue. The TO_DCPORTAL flag
causes the driver to honour any context_b modifications requested in the
\ :c:func:`qm_init_fq`\  API, as this indicates the frame queue will be consumed by a
direct-connect portal (PME, CAAM, or Fman). When frame queues are consumed by
software portals, the context_b field is controlled by the driver and can't
be modified by the caller.

.. _`qman_destroy_fq`:

qman_destroy_fq
===============

.. c:function:: void qman_destroy_fq(struct qman_fq *fq)

    Deallocates a FQ

    :param struct qman_fq \*fq:
        the frame queue object to release

.. _`qman_destroy_fq.description`:

Description
-----------

The memory for this frame queue object ('fq' provided in \ :c:func:`qman_create_fq`\ ) is
not deallocated but the caller regains ownership, to do with as desired. The
FQ must be in the 'out-of-service' or in the 'parked' state.

.. _`qman_fq_fqid`:

qman_fq_fqid
============

.. c:function:: u32 qman_fq_fqid(struct qman_fq *fq)

    Queries the frame queue ID of a FQ object

    :param struct qman_fq \*fq:
        the frame queue object to query

.. _`qman_init_fq`:

qman_init_fq
============

.. c:function:: int qman_init_fq(struct qman_fq *fq, u32 flags, struct qm_mcc_initfq *opts)

    Initialises FQ fields, leaves the FQ "parked" or "scheduled"

    :param struct qman_fq \*fq:
        the frame queue object to modify, must be 'parked' or new.

    :param u32 flags:
        bit-mask of QMAN_INITFQ_FLAG\_\*\*\* options

    :param struct qm_mcc_initfq \*opts:
        the FQ-modification settings, as defined in the low-level API

.. _`qman_init_fq.description`:

Description
-----------

The \ ``opts``\  parameter comes from the low-level portal API. Select
QMAN_INITFQ_FLAG_SCHED in \ ``flags``\  to cause the frame queue to be scheduled
rather than parked. NB, \ ``opts``\  can be NULL.

Note that some fields and options within \ ``opts``\  may be ignored or overwritten
by the driver;
1. the 'count' and 'fqid' fields are always ignored (this operation only

.. _`qman_init_fq.affects-one-frame-queue`:

affects one frame queue
-----------------------

@fq).
2. the QM_INITFQ_WE_CONTEXTB option of the 'we_mask' field and the associated
'fqd' structure's 'context_b' field are sometimes overwritten;
- if \ ``fq``\  was not created with QMAN_FQ_FLAG_TO_DCPORTAL, then context_b is
initialised to a value used by the driver for demux.
- if context_b is initialised for demux, so is context_a in case stashing
is requested (see item 4).
(So caller control of context_b is only possible for TO_DCPORTAL frame queue
objects.)
3. if \ ``flags``\  contains QMAN_INITFQ_FLAG_LOCAL, the 'fqd' structure's
'dest::channel' field will be overwritten to match the portal used to issue
the command. If the WE_DESTWQ write-enable bit had already been set by the
caller, the channel workqueue will be left as-is, otherwise the write-enable
bit is set and the workqueue is set to a default of 4. If the "LOCAL" flag
isn't set, the destination channel/workqueue fields and the write-enable bit
are left as-is.
4. if the driver overwrites context_a/b for demux, then if
QM_INITFQ_WE_CONTEXTA is set, the driver will only overwrite
context_a.address fields and will leave the stashing fields provided by the
user alone, otherwise it will zero out the context_a.stashing fields.

.. _`qman_schedule_fq`:

qman_schedule_fq
================

.. c:function:: int qman_schedule_fq(struct qman_fq *fq)

    Schedules a FQ

    :param struct qman_fq \*fq:
        the frame queue object to schedule, must be 'parked'

.. _`qman_schedule_fq.description`:

Description
-----------

Schedules the frame queue, which must be Parked, which takes it to
Tentatively-Scheduled or Truly-Scheduled depending on its fill-level.

.. _`qman_retire_fq`:

qman_retire_fq
==============

.. c:function:: int qman_retire_fq(struct qman_fq *fq, u32 *flags)

    Retires a FQ

    :param struct qman_fq \*fq:
        the frame queue object to retire

    :param u32 \*flags:
        FQ flags (QMAN_FQ_STATE\*) if retirement completes immediately

.. _`qman_retire_fq.description`:

Description
-----------

Retires the frame queue. This returns zero if it succeeds immediately, +1 if
the retirement was started asynchronously, otherwise it returns negative for
failure. When this function returns zero, \ ``flags``\  is set to indicate whether
the retired FQ is empty and/or whether it has any ORL fragments (to show up
as ERNs). Otherwise the corresponding flags will be known when a subsequent
FQRN message shows up on the portal's message ring.

NB, if the retirement is asynchronous (the FQ was in the Truly Scheduled or
Active state), the completion will be via the message ring as a FQRN - but
the corresponding callback may occur before this function returns!! Ie. the
caller should be prepared to accept the callback as the function is called,
not only once it has returned.

.. _`qman_oos_fq`:

qman_oos_fq
===========

.. c:function:: int qman_oos_fq(struct qman_fq *fq)

    Puts a FQ "out of service"

    :param struct qman_fq \*fq:
        the frame queue object to be put out-of-service, must be 'retired'

.. _`qman_oos_fq.description`:

Description
-----------

The frame queue must be retired and empty, and if any order restoration list
was released as ERNs at the time of retirement, they must all be consumed.

.. _`qman_enqueue`:

qman_enqueue
============

.. c:function:: int qman_enqueue(struct qman_fq *fq, const struct qm_fd *fd)

    Enqueue a frame to a frame queue

    :param struct qman_fq \*fq:
        the frame queue object to enqueue to

    :param const struct qm_fd \*fd:
        a descriptor of the frame to be enqueued

.. _`qman_enqueue.description`:

Description
-----------

Fills an entry in the EQCR of portal \ ``qm``\  to enqueue the frame described by
\ ``fd``\ . The descriptor details are copied from \ ``fd``\  to the EQCR entry, the 'pid'
field is ignored. The return value is non-zero on error, such as ring full.

.. _`qman_alloc_fqid_range`:

qman_alloc_fqid_range
=====================

.. c:function:: int qman_alloc_fqid_range(u32 *result, u32 count)

    Allocate a contiguous range of FQIDs

    :param u32 \*result:
        is set by the API to the base FQID of the allocated range

    :param u32 count:
        the number of FQIDs required

.. _`qman_alloc_fqid_range.description`:

Description
-----------

Returns 0 on success, or a negative error code.

.. _`qman_release_fqid`:

qman_release_fqid
=================

.. c:function:: int qman_release_fqid(u32 fqid)

    Release the specified frame queue ID

    :param u32 fqid:
        the FQID to be released back to the resource pool

.. _`qman_release_fqid.description`:

Description
-----------

This function can also be used to seed the allocator with
FQID ranges that it can subsequently allocate from.
Returns 0 on success, or a negative error code.

.. _`qman_alloc_pool_range`:

qman_alloc_pool_range
=====================

.. c:function:: int qman_alloc_pool_range(u32 *result, u32 count)

    Allocate a contiguous range of pool-channel IDs

    :param u32 \*result:
        is set by the API to the base pool-channel ID of the allocated range

    :param u32 count:
        the number of pool-channel IDs required

.. _`qman_alloc_pool_range.description`:

Description
-----------

Returns 0 on success, or a negative error code.

.. _`qman_release_pool`:

qman_release_pool
=================

.. c:function:: int qman_release_pool(u32 id)

    Release the specified pool-channel ID

    :param u32 id:
        the pool-chan ID to be released back to the resource pool

.. _`qman_release_pool.description`:

Description
-----------

This function can also be used to seed the allocator with
pool-channel ID ranges that it can subsequently allocate from.
Returns 0 on success, or a negative error code.

.. _`qman_create_cgr`:

qman_create_cgr
===============

.. c:function:: int qman_create_cgr(struct qman_cgr *cgr, u32 flags, struct qm_mcc_initcgr *opts)

    Register a congestion group object

    :param struct qman_cgr \*cgr:
        the 'cgr' object, with fields filled in

    :param u32 flags:
        QMAN_CGR_FLAG\_\* values

    :param struct qm_mcc_initcgr \*opts:
        optional state of CGR settings

.. _`qman_create_cgr.description`:

Description
-----------

Registers this object to receiving congestion entry/exit callbacks on the
portal affine to the cpu portal on which this API is executed. If opts is
NULL then only the callback (cgr->cb) function is registered. If \ ``flags``\ 
contains QMAN_CGR_FLAG_USE_INIT, then an init hw command (which will reset
any unspecified parameters) will be used rather than a modify hw hardware
(which only modifies the specified parameters).

.. _`qman_delete_cgr`:

qman_delete_cgr
===============

.. c:function:: int qman_delete_cgr(struct qman_cgr *cgr)

    Deregisters a congestion group object

    :param struct qman_cgr \*cgr:
        the 'cgr' object to deregister

.. _`qman_delete_cgr.description`:

Description
-----------

"Unplugs" this CGR object from the portal affine to the cpu on which this API
is executed. This must be excuted on the same affine portal on which it was
created.

.. _`qman_delete_cgr_safe`:

qman_delete_cgr_safe
====================

.. c:function:: void qman_delete_cgr_safe(struct qman_cgr *cgr)

    Deregisters a congestion group object from any CPU

    :param struct qman_cgr \*cgr:
        the 'cgr' object to deregister

.. _`qman_delete_cgr_safe.description`:

Description
-----------

This will select the proper CPU and run there \ :c:func:`qman_delete_cgr`\ .

.. _`qman_query_cgr_congested`:

qman_query_cgr_congested
========================

.. c:function:: int qman_query_cgr_congested(struct qman_cgr *cgr, bool *result)

    Queries CGR's congestion status

    :param struct qman_cgr \*cgr:
        the 'cgr' object to query

    :param bool \*result:
        returns 'cgr's congestion status, 1 (true) if congested

.. _`qman_alloc_cgrid_range`:

qman_alloc_cgrid_range
======================

.. c:function:: int qman_alloc_cgrid_range(u32 *result, u32 count)

    Allocate a contiguous range of CGR IDs

    :param u32 \*result:
        is set by the API to the base CGR ID of the allocated range

    :param u32 count:
        the number of CGR IDs required

.. _`qman_alloc_cgrid_range.description`:

Description
-----------

Returns 0 on success, or a negative error code.

.. _`qman_release_cgrid`:

qman_release_cgrid
==================

.. c:function:: int qman_release_cgrid(u32 id)

    Release the specified CGR ID

    :param u32 id:
        the CGR ID to be released back to the resource pool

.. _`qman_release_cgrid.description`:

Description
-----------

This function can also be used to seed the allocator with
CGR ID ranges that it can subsequently allocate from.
Returns 0 on success, or a negative error code.

.. This file was automatic generated / don't edit.

