.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/rcu/srcutree.c

.. _`init_srcu_struct`:

init_srcu_struct
================

.. c:function:: int init_srcu_struct(struct srcu_struct *sp)

    initialize a sleep-RCU structure

    :param struct srcu_struct \*sp:
        structure to initialize.

.. _`init_srcu_struct.description`:

Description
-----------

Must invoke this on a given srcu_struct before passing that srcu_struct
to any other function.  Each srcu_struct represents a separate domain
of SRCU protection.

.. _`srcu_readers_active`:

srcu_readers_active
===================

.. c:function:: bool srcu_readers_active(struct srcu_struct *sp)

    returns true if there are readers. and false otherwise

    :param struct srcu_struct \*sp:
        which srcu_struct to count active readers (holding srcu_read_lock).

.. _`srcu_readers_active.description`:

Description
-----------

Note that this is not an atomic primitive, and can therefore suffer
severe errors when invoked on an active srcu_struct.  That said, it
can be useful as an error check at cleanup time.

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

.. _`call_srcu`:

call_srcu
=========

.. c:function:: void call_srcu(struct srcu_struct *sp, struct rcu_head *rhp, rcu_callback_t func)

    Queue a callback for invocation after an SRCU grace period

    :param struct srcu_struct \*sp:
        srcu_struct in queue the callback

    :param struct rcu_head \*rhp:
        *undescribed*

    :param rcu_callback_t func:
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

.. _`synchronize_srcu_expedited`:

synchronize_srcu_expedited
==========================

.. c:function:: void synchronize_srcu_expedited(struct srcu_struct *sp)

    Brute-force SRCU grace period

    :param struct srcu_struct \*sp:
        srcu_struct with which to synchronize.

.. _`synchronize_srcu_expedited.description`:

Description
-----------

Wait for an SRCU grace period to elapse, but be more aggressive about
spinning rather than blocking when waiting.

Note that \ :c:func:`synchronize_srcu_expedited`\  has the same deadlock and
memory-ordering properties as does \ :c:func:`synchronize_srcu`\ .

.. _`synchronize_srcu`:

synchronize_srcu
================

.. c:function:: void synchronize_srcu(struct srcu_struct *sp)

    wait for prior SRCU read-side critical-section completion

    :param struct srcu_struct \*sp:
        srcu_struct with which to synchronize.

.. _`synchronize_srcu.description`:

Description
-----------

Wait for the count to drain to zero of both indexes. To avoid the
possible starvation of \ :c:func:`synchronize_srcu`\ , it waits for the count of
the index=((->srcu_idx & 1) ^ 1) to drain to zero at first,
and then flip the srcu_idx and wait for the count of the other index.

Can block; must be called from process context.

Note that it is illegal to call \ :c:func:`synchronize_srcu`\  from the corresponding
SRCU read-side critical section; doing so will result in deadlock.
However, it is perfectly legal to call \ :c:func:`synchronize_srcu`\  on one
srcu_struct from some other srcu_struct's read-side critical section,
as long as the resulting graph of srcu_structs is acyclic.

There are memory-ordering constraints implied by \ :c:func:`synchronize_srcu`\ .
On systems with more than one CPU, when \ :c:func:`synchronize_srcu`\  returns,
each CPU is guaranteed to have executed a full memory barrier since
the end of its last corresponding SRCU-sched read-side critical section
whose beginning preceded the call to \ :c:func:`synchronize_srcu`\ .  In addition,
each CPU having an SRCU read-side critical section that extends beyond
the return from \ :c:func:`synchronize_srcu`\  is guaranteed to have executed a
full memory barrier after the beginning of \ :c:func:`synchronize_srcu`\  and before
the beginning of that SRCU read-side critical section.  Note that these
guarantees include CPUs that are offline, idle, or executing in user mode,
as well as CPUs that are executing in the kernel.

Furthermore, if CPU A invoked \ :c:func:`synchronize_srcu`\ , which returned
to its caller on CPU B, then both CPU A and CPU B are guaranteed
to have executed a full memory barrier during the execution of
\ :c:func:`synchronize_srcu`\ .  This guarantee applies even if CPU A and CPU B
are the same CPU, but again only if the system has more than one CPU.

Of course, these memory-ordering guarantees apply only when
\ :c:func:`synchronize_srcu`\ , \ :c:func:`srcu_read_lock`\ , and \ :c:func:`srcu_read_unlock`\  are
passed the same srcu_struct structure.

If SRCU is likely idle, expedite the first request.  This semantic
was provided by Classic SRCU, and is relied upon by its users, so TREE
SRCU must also provide it.  Note that detecting idleness is heuristic
and subject to both false positives and negatives.

.. _`srcu_barrier`:

srcu_barrier
============

.. c:function:: void srcu_barrier(struct srcu_struct *sp)

    Wait until all in-flight \ :c:func:`call_srcu`\  callbacks complete.

    :param struct srcu_struct \*sp:
        srcu_struct on which to wait for in-flight callbacks.

.. _`srcu_batches_completed`:

srcu_batches_completed
======================

.. c:function:: unsigned long srcu_batches_completed(struct srcu_struct *sp)

    return batches completed.

    :param struct srcu_struct \*sp:
        srcu_struct on which to report batch completion.

.. _`srcu_batches_completed.description`:

Description
-----------

Report the number of batches, correlated with, but not necessarily
precisely the same as, the number of grace periods that have elapsed.

.. This file was automatic generated / don't edit.

