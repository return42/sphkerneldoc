.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/vmpressure.c

.. _`vmpressure`:

vmpressure
==========

.. c:function:: void vmpressure(gfp_t gfp, struct mem_cgroup *memcg, bool tree, unsigned long scanned, unsigned long reclaimed)

    Account memory pressure through scanned/reclaimed ratio

    :param gfp:
        reclaimer's gfp mask
    :type gfp: gfp_t

    :param memcg:
        cgroup memory controller handle
    :type memcg: struct mem_cgroup \*

    :param tree:
        legacy subtree mode
    :type tree: bool

    :param scanned:
        number of pages scanned
    :type scanned: unsigned long

    :param reclaimed:
        number of pages reclaimed
    :type reclaimed: unsigned long

.. _`vmpressure.description`:

Description
-----------

This function should be called from the vmscan reclaim path to account
"instantaneous" memory pressure (scanned/reclaimed ratio). The raw
pressure index is then further refined and averaged over time.

If \ ``tree``\  is set, vmpressure is in traditional userspace reporting

.. _`vmpressure.mode`:

mode
----

\ ``memcg``\  is considered the pressure root and userspace is
notified of the entire subtree's reclaim efficiency.

If \ ``tree``\  is not set, reclaim efficiency is recorded for \ ``memcg``\ , and
only in-kernel users are notified.

This function does not return any value.

.. _`vmpressure_prio`:

vmpressure_prio
===============

.. c:function:: void vmpressure_prio(gfp_t gfp, struct mem_cgroup *memcg, int prio)

    Account memory pressure through reclaimer priority level

    :param gfp:
        reclaimer's gfp mask
    :type gfp: gfp_t

    :param memcg:
        cgroup memory controller handle
    :type memcg: struct mem_cgroup \*

    :param prio:
        reclaimer's priority
    :type prio: int

.. _`vmpressure_prio.description`:

Description
-----------

This function should be called from the reclaim path every time when
the vmscan's reclaiming priority (scanning depth) changes.

This function does not return any value.

.. _`vmpressure_register_event`:

vmpressure_register_event
=========================

.. c:function:: int vmpressure_register_event(struct mem_cgroup *memcg, struct eventfd_ctx *eventfd, const char *args)

    Bind vmpressure notifications to an eventfd

    :param memcg:
        memcg that is interested in vmpressure notifications
    :type memcg: struct mem_cgroup \*

    :param eventfd:
        eventfd context to link notifications with
    :type eventfd: struct eventfd_ctx \*

    :param args:
        event arguments (pressure level threshold, optional mode)
    :type args: const char \*

.. _`vmpressure_register_event.description`:

Description
-----------

This function associates eventfd context with the vmpressure
infrastructure, so that the notifications will be delivered to the
\ ``eventfd``\ . The \ ``args``\  parameter is a comma-delimited string that denotes a
pressure level threshold (one of vmpressure_str_levels, i.e. "low", "medium",
or "critical") and an optional mode (one of vmpressure_str_modes, i.e.
"hierarchy" or "local").

To be used as memcg event method.

.. _`vmpressure_unregister_event`:

vmpressure_unregister_event
===========================

.. c:function:: void vmpressure_unregister_event(struct mem_cgroup *memcg, struct eventfd_ctx *eventfd)

    Unbind eventfd from vmpressure

    :param memcg:
        memcg handle
    :type memcg: struct mem_cgroup \*

    :param eventfd:
        eventfd context that was used to link vmpressure with the \ ``cg``\ 
    :type eventfd: struct eventfd_ctx \*

.. _`vmpressure_unregister_event.description`:

Description
-----------

This function does internal manipulations to detach the \ ``eventfd``\  from
the vmpressure notifications, and then frees internal resources
associated with the \ ``eventfd``\  (but the \ ``eventfd``\  itself is not freed).

To be used as memcg event method.

.. _`vmpressure_init`:

vmpressure_init
===============

.. c:function:: void vmpressure_init(struct vmpressure *vmpr)

    Initialize vmpressure control structure

    :param vmpr:
        Structure to be initialized
    :type vmpr: struct vmpressure \*

.. _`vmpressure_init.description`:

Description
-----------

This function should be called on every allocated vmpressure structure
before any usage.

.. _`vmpressure_cleanup`:

vmpressure_cleanup
==================

.. c:function:: void vmpressure_cleanup(struct vmpressure *vmpr)

    shuts down vmpressure control structure

    :param vmpr:
        Structure to be cleaned up
    :type vmpr: struct vmpressure \*

.. _`vmpressure_cleanup.description`:

Description
-----------

This function should be called before the structure in which it is
embedded is cleaned up.

.. This file was automatic generated / don't edit.

