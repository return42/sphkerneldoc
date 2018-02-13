.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/octeon/cvmx-pow.h

.. _`cvmx_pow_wait_t`:

typedef cvmx_pow_wait_t
=======================

.. c:type:: typedef cvmx_pow_wait_t


.. _`cvmx_pow_tag_op_t`:

typedef cvmx_pow_tag_op_t
=========================

.. c:type:: typedef cvmx_pow_tag_op_t


.. _`cvmx_pow_tag_req_t`:

typedef cvmx_pow_tag_req_t
==========================

.. c:type:: typedef cvmx_pow_tag_req_t


.. _`cvmx_pow_load_addr_t`:

typedef cvmx_pow_load_addr_t
============================

.. c:type:: typedef cvmx_pow_load_addr_t


.. _`cvmx_pow_tag_load_resp_t`:

typedef cvmx_pow_tag_load_resp_t
================================

.. c:type:: typedef cvmx_pow_tag_load_resp_t

    (except CSR reads)

.. _`cvmx_pow_tag_store_addr_t`:

typedef cvmx_pow_tag_store_addr_t
=================================

.. c:type:: typedef cvmx_pow_tag_store_addr_t

    The store address is meaningful on stores to the POW.  The hardware assumes that an aligned 64-bit store was used for all these stores.  Note the assumption that the work queue entry is aligned on an 8-byte boundary (since the low-order 3 address bits must be zero).  Note that not all fields are used by all operations.

.. _`cvmx_pow_tag_store_addr_t.note`:

NOTE
----

The following is the behavior of the pending switch bit at the PP
for POW stores (i.e. when did<7:3> == 0xc)
- did<2:0> == 0      => pending switch bit is set
- did<2:0> == 1      => no affect on the pending switch bit
- did<2:0> == 3      => pending switch bit is cleared
- did<2:0> == 7      => no affect on the pending switch bit
- did<2:0> == others => must not be used
- No other loads/stores have an affect on the pending switch bit
- The switch bus from POW can clear the pending switch bit

NOTE: did<2:0> == 2 is used by the HW for a special single-cycle
ADDWQ command that only contains the pointer). SW must never use
did<2:0> == 2.

.. _`cvmx_pow_iobdma_store_t`:

typedef cvmx_pow_iobdma_store_t
===============================

.. c:type:: typedef cvmx_pow_iobdma_store_t


.. _`cvmx_pow_get_current_tag`:

cvmx_pow_get_current_tag
========================

.. c:function:: cvmx_pow_tag_req_t cvmx_pow_get_current_tag( void)

    tag type, tag, group, and POW entry index associated with this core. Index is only valid if the tag type isn't NULL_NULL. If a tag switch is pending this routine returns the tag before the tag switch, not after.

    :param  void:
        no arguments

.. _`cvmx_pow_get_current_tag.description`:

Description
-----------

Returns Current tag

.. _`cvmx_pow_get_current_wqp`:

cvmx_pow_get_current_wqp
========================

.. c:function:: cvmx_wqe_t *cvmx_pow_get_current_wqp( void)

    entry currently associated with this core.

    :param  void:
        no arguments

.. _`cvmx_pow_get_current_wqp.description`:

Description
-----------

Returns WQE pointer

.. _`__cvmx_pow_warn_if_pending_switch`:

\__cvmx_pow_warn_if_pending_switch
==================================

.. c:function:: void __cvmx_pow_warn_if_pending_switch(const char *function)

    :param const char \*function:
        Function name checking for a pending tag switch

.. _`cvmx_pow_tag_sw_wait`:

cvmx_pow_tag_sw_wait
====================

.. c:function:: void cvmx_pow_tag_sw_wait( void)

    Note that switches to NULL complete immediately and do not need to be waited for.

    :param  void:
        no arguments

.. _`cvmx_pow_work_request_sync_nocheck`:

cvmx_pow_work_request_sync_nocheck
==================================

.. c:function:: cvmx_wqe_t *cvmx_pow_work_request_sync_nocheck(cvmx_pow_wait_t wait)

    This function does NOT wait for previous tag switches to complete, so the caller must ensure that there is not a pending tag switch.

    :param cvmx_pow_wait_t wait:
        When set, call stalls until work becomes avaiable, or times out.
        If not set, returns immediately.

.. _`cvmx_pow_work_request_sync_nocheck.description`:

Description
-----------

Returns Returns the WQE pointer from POW. Returns NULL if no work
was available.

.. _`cvmx_pow_work_request_sync`:

cvmx_pow_work_request_sync
==========================

.. c:function:: cvmx_wqe_t *cvmx_pow_work_request_sync(cvmx_pow_wait_t wait)

    This function waits for any previous tag switch to complete before requesting the new work.

    :param cvmx_pow_wait_t wait:
        When set, call stalls until work becomes avaiable, or times out.
        If not set, returns immediately.

.. _`cvmx_pow_work_request_sync.description`:

Description
-----------

Returns Returns the WQE pointer from POW. Returns NULL if no work
was available.

.. _`cvmx_pow_work_request_null_rd`:

cvmx_pow_work_request_null_rd
=============================

.. c:function:: enum cvmx_pow_tag_type cvmx_pow_work_request_null_rd( void)

    This function waits for any previous tag switch to complete before requesting the null_rd.

    :param  void:
        no arguments

.. _`cvmx_pow_work_request_null_rd.description`:

Description
-----------

Returns Returns the POW state of type cvmx_pow_tag_type_t.

.. _`cvmx_pow_work_request_async_nocheck`:

cvmx_pow_work_request_async_nocheck
===================================

.. c:function:: void cvmx_pow_work_request_async_nocheck(int scr_addr, cvmx_pow_wait_t wait)

    and should later be checked with function cvmx_pow_work_response_async.  This function does NOT wait for previous tag switches to complete, so the caller must ensure that there is not a pending tag switch.

    :param int scr_addr:
        Scratch memory address that response will be returned
        to, which is either a valid WQE, or a response with the
        invalid bit set.  Byte address, must be 8 byte aligned.

    :param cvmx_pow_wait_t wait:
        1 to cause response to wait for work to become available (or
        timeout), 0 to cause response to return immediately

.. _`cvmx_pow_work_request_async`:

cvmx_pow_work_request_async
===========================

.. c:function:: void cvmx_pow_work_request_async(int scr_addr, cvmx_pow_wait_t wait)

    and should later be checked with function cvmx_pow_work_response_async.  This function waits for any previous tag switch to complete before requesting the new work.

    :param int scr_addr:
        Scratch memory address that response will be returned
        to, which is either a valid WQE, or a response with the
        invalid bit set.  Byte address, must be 8 byte aligned.

    :param cvmx_pow_wait_t wait:
        1 to cause response to wait for work to become available (or
        timeout), 0 to cause response to return immediately

.. _`cvmx_pow_work_response_async`:

cvmx_pow_work_response_async
============================

.. c:function:: cvmx_wqe_t *cvmx_pow_work_response_async(int scr_addr)

    to wait for the response.

    :param int scr_addr:
        Scratch memory address to get result from Byte address,
        must be 8 byte aligned.

.. _`cvmx_pow_work_response_async.description`:

Description
-----------

Returns Returns the WQE from the scratch register, or NULL if no
work was available.

.. _`cvmx_pow_work_invalid`:

cvmx_pow_work_invalid
=====================

.. c:function:: uint64_t cvmx_pow_work_invalid(cvmx_wqe_t *wqe_ptr)

    request is valid.  It may be invalid due to no work being available or due to a timeout.

    :param cvmx_wqe_t \*wqe_ptr:
        pointer to a work queue entry returned by the POW

.. _`cvmx_pow_work_invalid.description`:

Description
-----------

Returns 0 if pointer is valid
1 if invalid (no work was returned)

.. _`cvmx_pow_tag_sw_nocheck`:

cvmx_pow_tag_sw_nocheck
=======================

.. c:function:: void cvmx_pow_tag_sw_nocheck(uint32_t tag, enum cvmx_pow_tag_type tag_type)

    Completion for the tag switch must be checked for separately.  This function does NOT update the work queue entry in dram to match tag value and type, so the application must keep track of these if they are important to the application.  This tag switch command must not be used for switches to NULL, as the tag switch pending bit will be set by the switch request, but never cleared by the hardware.

    :param uint32_t tag:
        new tag value

    :param enum cvmx_pow_tag_type tag_type:
        new tag type (ordered or atomic)

.. _`cvmx_pow_tag_sw_nocheck.note`:

NOTE
----

This should not be used when switching from a NULL tag.  Use
\ :c:func:`cvmx_pow_tag_sw_full`\  instead.

This function does no checks, so the caller must ensure that any
previous tag switch has completed.

.. _`cvmx_pow_tag_sw`:

cvmx_pow_tag_sw
===============

.. c:function:: void cvmx_pow_tag_sw(uint32_t tag, enum cvmx_pow_tag_type tag_type)

    Completion for the tag switch must be checked for separately.  This function does NOT update the work queue entry in dram to match tag value and type, so the application must keep track of these if they are important to the application.  This tag switch command must not be used for switches to NULL, as the tag switch pending bit will be set by the switch request, but never cleared by the hardware.

    :param uint32_t tag:
        new tag value

    :param enum cvmx_pow_tag_type tag_type:
        new tag type (ordered or atomic)

.. _`cvmx_pow_tag_sw.note`:

NOTE
----

This should not be used when switching from a NULL tag.  Use
\ :c:func:`cvmx_pow_tag_sw_full`\  instead.

This function waits for any previous tag switch to complete, and also
displays an error on tag switches to NULL.

.. _`cvmx_pow_tag_sw_full_nocheck`:

cvmx_pow_tag_sw_full_nocheck
============================

.. c:function:: void cvmx_pow_tag_sw_full_nocheck(cvmx_wqe_t *wqp, uint32_t tag, enum cvmx_pow_tag_type tag_type, uint64_t group)

    Completion for the tag switch must be checked for separately.  This function does NOT update the work queue entry in dram to match tag value and type, so the application must keep track of these if they are important to the application.  This tag switch command must not be used for switches to NULL, as the tag switch pending bit will be set by the switch request, but never cleared by the hardware.

    :param cvmx_wqe_t \*wqp:
        pointer to work queue entry to submit.  This entry is
        updated to match the other parameters

    :param uint32_t tag:
        tag value to be assigned to work queue entry

    :param enum cvmx_pow_tag_type tag_type:
        type of tag

    :param uint64_t group:
        group value for the work queue entry.

.. _`cvmx_pow_tag_sw_full_nocheck.description`:

Description
-----------

This function must be used for tag switches from NULL.

This function does no checks, so the caller must ensure that any
previous tag switch has completed.

.. _`cvmx_pow_tag_sw_full`:

cvmx_pow_tag_sw_full
====================

.. c:function:: void cvmx_pow_tag_sw_full(cvmx_wqe_t *wqp, uint32_t tag, enum cvmx_pow_tag_type tag_type, uint64_t group)

    Completion for the tag switch must be checked for separately.  This function does NOT update the work queue entry in dram to match tag value and type, so the application must keep track of these if they are important to the application.  This tag switch command must not be used for switches to NULL, as the tag switch pending bit will be set by the switch request, but never cleared by the hardware.

    :param cvmx_wqe_t \*wqp:
        pointer to work queue entry to submit.  This entry is updated
        to match the other parameters

    :param uint32_t tag:
        tag value to be assigned to work queue entry

    :param enum cvmx_pow_tag_type tag_type:
        type of tag

    :param uint64_t group:
        group value for the work queue entry.

.. _`cvmx_pow_tag_sw_full.description`:

Description
-----------

This function must be used for tag switches from NULL.

This function waits for any pending tag switches to complete
before requesting the tag switch.

.. _`cvmx_pow_tag_sw_null_nocheck`:

cvmx_pow_tag_sw_null_nocheck
============================

.. c:function:: void cvmx_pow_tag_sw_null_nocheck( void)

    synchronization provided by the POW for the current work queue entry.  This operation completes immediately, so completion should not be waited for. This function does NOT wait for previous tag switches to complete, so the caller must ensure that any previous tag switches have completed.

    :param  void:
        no arguments

.. _`cvmx_pow_tag_sw_null`:

cvmx_pow_tag_sw_null
====================

.. c:function:: void cvmx_pow_tag_sw_null( void)

    synchronization provided by the POW for the current work queue entry.  This operation completes immediately, so completion should not be waited for. This function waits for any pending tag switches to complete before requesting the switch to NULL.

    :param  void:
        no arguments

.. _`cvmx_pow_work_submit`:

cvmx_pow_work_submit
====================

.. c:function:: void cvmx_pow_work_submit(cvmx_wqe_t *wqp, uint32_t tag, enum cvmx_pow_tag_type tag_type, uint64_t qos, uint64_t grp)

    queue entry in DRAM to match the arguments given.  Note that the tag provided is for the work queue entry submitted, and is unrelated to the tag that the core currently holds.

    :param cvmx_wqe_t \*wqp:
        pointer to work queue entry to submit.  This entry is
        updated to match the other parameters

    :param uint32_t tag:
        tag value to be assigned to work queue entry

    :param enum cvmx_pow_tag_type tag_type:
        type of tag

    :param uint64_t qos:
        Input queue to add to.

    :param uint64_t grp:
        group value for the work queue entry.

.. _`cvmx_pow_set_group_mask`:

cvmx_pow_set_group_mask
=======================

.. c:function:: void cvmx_pow_set_group_mask(uint64_t core_num, uint64_t mask)

    indicates which groups each core will accept work from. There are 16 groups.

    :param uint64_t core_num:
        core to apply mask to

    :param uint64_t mask:
        Group mask. There are 16 groups, so only bits 0-15 are valid,
        representing groups 0-15.
        Each 1 bit in the mask enables the core to accept work from
        the corresponding group.

.. _`cvmx_pow_set_priority`:

cvmx_pow_set_priority
=====================

.. c:function:: void cvmx_pow_set_priority(uint64_t core_num, const uint8_t priority)

    an associated priority value.

    :param uint64_t core_num:
        core to apply priorities to

    :param const uint8_t priority:
        Vector of 8 priorities, one per POW Input Queue (0-7).
        Highest priority is 0 and lowest is 7. A priority value
        of 0xF instructs POW to skip the Input Queue when
        scheduling to this specific core.
        NOTE: priorities should not have gaps in values, meaning
        {0,1,1,1,1,1,1,1} is a valid configuration while
        {0,2,2,2,2,2,2,2} is not.

.. _`cvmx_pow_tag_sw_desched_nocheck`:

cvmx_pow_tag_sw_desched_nocheck
===============================

.. c:function:: void cvmx_pow_tag_sw_desched_nocheck(uint32_t tag, enum cvmx_pow_tag_type tag_type, uint64_t group, uint64_t no_sched)

    immediately, so completion must not be waited for.  This function does NOT update the wqe in DRAM to match arguments.

    :param uint32_t tag:
        New tag value

    :param enum cvmx_pow_tag_type tag_type:
        New tag type

    :param uint64_t group:
        New group value

    :param uint64_t no_sched:
        Control whether this work queue entry will be rescheduled.
        - 1 : don't schedule this work
        - 0 : allow this work to be scheduled.

.. _`cvmx_pow_tag_sw_desched_nocheck.description`:

Description
-----------

This function does NOT wait for any prior tag switches to complete, so the
calling code must do this.

Note the following CAVEAT of the Octeon HW behavior when
re-scheduling DE-SCHEDULEd items whose (next) state is

.. _`cvmx_pow_tag_sw_desched_nocheck.ordered`:

ORDERED
-------

- If there are no switches pending at the time that the
HW executes the de-schedule, the HW will only re-schedule
the head of the FIFO associated with the given tag. This
means that in many respects, the HW treats this ORDERED
tag as an ATOMIC tag. Note that in the SWTAG_DESCH
case (to an ORDERED tag), the HW will do the switch
before the deschedule whenever it is possible to do
the switch immediately, so it may often look like
this case.
- If there is a pending switch to ORDERED at the time
the HW executes the de-schedule, the HW will perform
the switch at the time it re-schedules, and will be
able to reschedule any/all of the entries with the
same tag.
Due to this behavior, the RECOMMENDATION to software is
that they have a (next) state of ATOMIC when they
DE-SCHEDULE. If an ORDERED tag is what was really desired,
SW can choose to immediately switch to an ORDERED tag
after the work (that has an ATOMIC tag) is re-scheduled.
Note that since there are never any tag switches pending
when the HW re-schedules, this switch can be IMMEDIATE upon
the reception of the pointer during the re-schedule.

.. _`cvmx_pow_tag_sw_desched`:

cvmx_pow_tag_sw_desched
=======================

.. c:function:: void cvmx_pow_tag_sw_desched(uint32_t tag, enum cvmx_pow_tag_type tag_type, uint64_t group, uint64_t no_sched)

    immediately, so completion must not be waited for.  This function does NOT update the wqe in DRAM to match arguments.

    :param uint32_t tag:
        New tag value

    :param enum cvmx_pow_tag_type tag_type:
        New tag type

    :param uint64_t group:
        New group value

    :param uint64_t no_sched:
        Control whether this work queue entry will be rescheduled.
        - 1 : don't schedule this work
        - 0 : allow this work to be scheduled.

.. _`cvmx_pow_tag_sw_desched.description`:

Description
-----------

This function waits for any prior tag switches to complete, so the
calling code may call this function with a pending tag switch.

Note the following CAVEAT of the Octeon HW behavior when
re-scheduling DE-SCHEDULEd items whose (next) state is

.. _`cvmx_pow_tag_sw_desched.ordered`:

ORDERED
-------

- If there are no switches pending at the time that the
HW executes the de-schedule, the HW will only re-schedule
the head of the FIFO associated with the given tag. This
means that in many respects, the HW treats this ORDERED
tag as an ATOMIC tag. Note that in the SWTAG_DESCH
case (to an ORDERED tag), the HW will do the switch
before the deschedule whenever it is possible to do
the switch immediately, so it may often look like
this case.
- If there is a pending switch to ORDERED at the time
the HW executes the de-schedule, the HW will perform
the switch at the time it re-schedules, and will be
able to reschedule any/all of the entries with the
same tag.
Due to this behavior, the RECOMMENDATION to software is
that they have a (next) state of ATOMIC when they
DE-SCHEDULE. If an ORDERED tag is what was really desired,
SW can choose to immediately switch to an ORDERED tag
after the work (that has an ATOMIC tag) is re-scheduled.
Note that since there are never any tag switches pending
when the HW re-schedules, this switch can be IMMEDIATE upon
the reception of the pointer during the re-schedule.

.. _`cvmx_pow_desched`:

cvmx_pow_desched
================

.. c:function:: void cvmx_pow_desched(uint64_t no_sched)

    :param uint64_t no_sched:
        no schedule flag value to be set on the work queue
        entry.  If this is set the entry will not be
        rescheduled.

.. _`cvmx_pow_tag_compose`:

cvmx_pow_tag_compose
====================

.. c:function:: uint32_t cvmx_pow_tag_compose(uint64_t sw_bits, uint64_t hw_bits)

    :param uint64_t sw_bits:
        The upper bits (number depends on configuration) are set
        to this value.  The remainder of bits are set by the
        hw_bits parameter.

    :param uint64_t hw_bits:
        The lower bits (number depends on configuration) are set
        to this value.  The remainder of bits are set by the
        sw_bits parameter.

.. _`cvmx_pow_tag_compose.description`:

Description
-----------

Returns 32 bit value of the combined hw and sw bits.

.. _`cvmx_pow_tag_get_sw_bits`:

cvmx_pow_tag_get_sw_bits
========================

.. c:function:: uint32_t cvmx_pow_tag_get_sw_bits(uint64_t tag)

    :param uint64_t tag:
        32 bit tag value

.. _`cvmx_pow_tag_get_sw_bits.description`:

Description
-----------

Returns N bit software tag value, where N is configurable with the
CVMX_TAG_SW_BITS define

.. _`cvmx_pow_capture`:

cvmx_pow_capture
================

.. c:function:: int cvmx_pow_capture(void *buffer, int buffer_size)

    buffer. It is recommended that you pass a buffer of at least 128KB. The format of the capture may change based on SDK version and Octeon chip.

    :param void \*buffer:
        Buffer to store capture into

    :param int buffer_size:
        The size of the supplied buffer

.. _`cvmx_pow_capture.description`:

Description
-----------

Returns Zero on success, negative on failure

.. _`cvmx_pow_display`:

cvmx_pow_display
================

.. c:function:: void cvmx_pow_display(void *buffer, int buffer_size)

    :param void \*buffer:
        POW capture from \ :c:func:`cvmx_pow_capture`\ 

    :param int buffer_size:
        Size of the buffer

.. _`cvmx_pow_get_num_entries`:

cvmx_pow_get_num_entries
========================

.. c:function:: int cvmx_pow_get_num_entries( void)

    :param  void:
        no arguments

.. _`cvmx_pow_get_num_entries.description`:

Description
-----------

Returns Number of POW entries

.. This file was automatic generated / don't edit.

