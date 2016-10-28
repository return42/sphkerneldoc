.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/srcu.h

.. _`call_srcu`:

call_srcu
=========

.. c:function:: void call_srcu(struct srcu_struct *sp, struct rcu_head *head, void (*func)(struct rcu_head *head))

    Queue a callback for invocation after an SRCU grace period

    :param struct srcu_struct \*sp:
        srcu_struct in queue the callback

    :param struct rcu_head \*head:
        structure to be used for queueing the SRCU callback.

    :param void (\*func)(struct rcu_head \*head):
        function to be invoked after the SRCU grace period

.. _`call_srcu.description`:

Description
-----------

The callback function will be invoked some time after a full SRCU
grace period elapses, in other words after all pre-existing SRCU
read-side critical sections have completed.  However, the callback
function might well execute concurrently with other SRCU read-side
critical sections that started after \ :c:func:`call_srcu`\  was invoked.  SRCU
read-side critical sections are delimited by \ :c:func:`srcu_read_lock`\  and
\ :c:func:`srcu_read_unlock`\ , and may be nested.

The callback will be invoked from process context, but must nevertheless
be fast and must not block.

.. _`srcu_read_lock_held`:

srcu_read_lock_held
===================

.. c:function:: int srcu_read_lock_held(struct srcu_struct *sp)

    might we be in SRCU read-side critical section?

    :param struct srcu_struct \*sp:
        *undescribed*

.. _`srcu_read_lock_held.description`:

Description
-----------

If CONFIG_DEBUG_LOCK_ALLOC is selected, returns nonzero iff in an SRCU
read-side critical section.  In absence of CONFIG_DEBUG_LOCK_ALLOC,
this assumes we are in an SRCU read-side critical section unless it can
prove otherwise.

Checks \ :c:func:`debug_lockdep_rcu_enabled`\  to prevent false positives during boot
and while lockdep is disabled.

Note that SRCU is based on its own statemachine and it doesn't
relies on normal RCU, it can be called from the CPU which
is in the idle loop from an RCU point of view or offline.

.. _`srcu_dereference_check`:

srcu_dereference_check
======================

.. c:function::  srcu_dereference_check( p,  sp,  c)

    fetch SRCU-protected pointer for later dereferencing

    :param  p:
        the pointer to fetch and protect for later dereferencing

    :param  sp:
        pointer to the srcu_struct, which is used to check that we
        really are in an SRCU read-side critical section.

    :param  c:
        condition to check for update-side use

.. _`srcu_dereference_check.description`:

Description
-----------

If PROVE_RCU is enabled, invoking this outside of an RCU read-side
critical section will result in an RCU-lockdep splat, unless \ ``c``\  evaluates
to 1.  The \ ``c``\  argument will normally be a logical expression containing
\ :c:func:`lockdep_is_held`\  calls.

.. _`srcu_dereference`:

srcu_dereference
================

.. c:function::  srcu_dereference( p,  sp)

    fetch SRCU-protected pointer for later dereferencing

    :param  p:
        the pointer to fetch and protect for later dereferencing

    :param  sp:
        pointer to the srcu_struct, which is used to check that we
        really are in an SRCU read-side critical section.

.. _`srcu_dereference.description`:

Description
-----------

Makes \ :c:func:`rcu_dereference_check`\  do the dirty work.  If PROVE_RCU
is enabled, invoking this outside of an RCU read-side critical
section will result in an RCU-lockdep splat.

.. _`srcu_read_lock`:

srcu_read_lock
==============

.. c:function:: int srcu_read_lock(struct srcu_struct *sp)

    register a new reader for an SRCU-protected structure.

    :param struct srcu_struct \*sp:
        srcu_struct in which to register the new reader.

.. _`srcu_read_lock.description`:

Description
-----------

Enter an SRCU read-side critical section.  Note that SRCU read-side
critical sections may be nested.  However, it is illegal to
call anything that waits on an SRCU grace period for the same
srcu_struct, whether directly or indirectly.  Please note that
one way to indirectly wait on an SRCU grace period is to acquire
a mutex that is held elsewhere while calling \ :c:func:`synchronize_srcu`\  or
\ :c:func:`synchronize_srcu_expedited`\ .

Note that \ :c:func:`srcu_read_lock`\  and the matching \ :c:func:`srcu_read_unlock`\  must
occur in the same context, for example, it is illegal to invoke
\ :c:func:`srcu_read_unlock`\  in an irq handler if the matching \ :c:func:`srcu_read_lock`\ 
was invoked in process context.

.. _`srcu_read_unlock`:

srcu_read_unlock
================

.. c:function:: void srcu_read_unlock(struct srcu_struct *sp, int idx)

    unregister a old reader from an SRCU-protected structure.

    :param struct srcu_struct \*sp:
        srcu_struct in which to unregister the old reader.

    :param int idx:
        return value from corresponding \ :c:func:`srcu_read_lock`\ .

.. _`srcu_read_unlock.description`:

Description
-----------

Exit an SRCU read-side critical section.

.. _`smp_mb__after_srcu_read_unlock`:

smp_mb__after_srcu_read_unlock
==============================

.. c:function:: void smp_mb__after_srcu_read_unlock( void)

    ensure full ordering after srcu_read_unlock

    :param  void:
        no arguments

.. _`smp_mb__after_srcu_read_unlock.description`:

Description
-----------

Converts the preceding srcu_read_unlock into a two-way memory barrier.

Call this after srcu_read_unlock, to guarantee that all memory operations
that occur after smp_mb__after_srcu_read_unlock will appear to happen after
the preceding srcu_read_unlock.

.. This file was automatic generated / don't edit.

