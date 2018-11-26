.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdkfd/kfd_events.c

.. _`lookup_signaled_event_by_partial_id`:

lookup_signaled_event_by_partial_id
===================================

.. c:function:: struct kfd_event *lookup_signaled_event_by_partial_id(struct kfd_process *p, uint32_t id, uint32_t bits)

    Lookup signaled event from partial ID

    :param p:
        Pointer to struct kfd_process
    :type p: struct kfd_process \*

    :param id:
        ID to look up
    :type id: uint32_t

    :param bits:
        Number of valid bits in \ ``id``\ 
    :type bits: uint32_t

.. _`lookup_signaled_event_by_partial_id.description`:

Description
-----------

Finds the first signaled event with a matching partial ID. If no
matching signaled event is found, returns NULL. In that case the
caller should assume that the partial ID is invalid and do an
exhaustive search of all siglaned events.

If multiple events with the same partial ID signal at the same
time, they will be found one interrupt at a time, not necessarily
in the same order the interrupts occurred. As long as the number of
interrupts is correct, all signaled events will be seen by the
driver.

.. This file was automatic generated / don't edit.

