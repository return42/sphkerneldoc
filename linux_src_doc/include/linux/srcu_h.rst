.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/srcu.h

.. _`cleanup_srcu_struct`:

cleanup_srcu_struct
===================

.. c:function:: void cleanup_srcu_struct(struct srcu_struct *sp)

    deconstruct a sleep-RCU structure

    :param struct srcu_struct \*sp:
        structure to clean up.

.. _`cleanup_srcu_struct.description`:

Description
-----------

Must invoke this after you are finished using a given srcu_struct that
was initialized via \ :c:func:`init_srcu_struct`\ , else you leak memory.

.. _`cleanup_srcu_struct_quiesced`:

cleanup_srcu_struct_quiesced
============================

.. c:function:: void cleanup_srcu_struct_quiesced(struct srcu_struct *sp)

    deconstruct a quiesced sleep-RCU structure

    :param struct srcu_struct \*sp:
        structure to clean up.

.. _`cleanup_srcu_struct_quiesced.description`:

Description
-----------

Must invoke this after you are finished using a given srcu_struct that
was initialized via \ :c:func:`init_srcu_struct`\ , else you leak memory.  Also,
all grace-period processing must have completed.

"Completed" means that the last \ :c:func:`synchronize_srcu`\  and
\ :c:func:`synchronize_srcu_expedited`\  calls must have returned before the call
to \ :c:func:`cleanup_srcu_struct_quiesced`\ .  It also means that the callback
from the last \ :c:func:`call_srcu`\  must have been invoked before the call to
\ :c:func:`cleanup_srcu_struct_quiesced`\ , but you can use \ :c:func:`srcu_barrier`\  to help
with this last.  Violating these rules will get you a \ :c:func:`WARN_ON`\  splat
(with high probability, anyway), and will also cause the srcu_struct
to be leaked.

.. _`srcu_read_lock_held`:

srcu_read_lock_held
===================

.. c:function:: int srcu_read_lock_held(const struct srcu_struct *sp)

    might we be in SRCU read-side critical section?

    :param const struct srcu_struct \*sp:
        The srcu_struct structure to check

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

