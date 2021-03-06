.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/rcupdate.h

.. _`rcu_nonidle`:

RCU_NONIDLE
===========

.. c:function::  RCU_NONIDLE( a)

    Indicate idle-loop code that needs RCU readers

    :param a:
        Code that RCU needs to pay attention to.
    :type a: 

.. _`rcu_nonidle.description`:

Description
-----------

RCU read-side critical sections are forbidden in the inner idle loop,
that is, between the \ :c:func:`rcu_idle_enter`\  and the \ :c:func:`rcu_idle_exit`\  -- RCU
will happily ignore any such read-side critical sections.  However,
things like powertop need tracepoints in the inner idle loop.

This macro provides the way out:  RCU_NONIDLE(do_something_with_RCU())
will tell RCU that it needs to pay attention, invoke its argument
(in this example, calling the \ :c:func:`do_something_with_RCU`\  function),
and then tell RCU to go back to ignoring this CPU.  It is permissible
to nest \ :c:func:`RCU_NONIDLE`\  wrappers, but not indefinitely (but the limit is
on the order of a million or so, even on 32-bit systems).  It is
not legal to block within \ :c:func:`RCU_NONIDLE`\ , nor is it permissible to
transfer control either into or out of \ :c:func:`RCU_NONIDLE`\ 's statement.

.. _`cond_resched_tasks_rcu_qs`:

cond_resched_tasks_rcu_qs
=========================

.. c:function::  cond_resched_tasks_rcu_qs( void)

    Report potential quiescent states to RCU

    :param void:
        no arguments
    :type void: 

.. _`cond_resched_tasks_rcu_qs.description`:

Description
-----------

This macro resembles \ :c:func:`cond_resched`\ , except that it is defined to
report potential quiescent states to RCU-tasks even if the \ :c:func:`cond_resched`\ 
machinery were to be shut off, as some advocate for PREEMPT kernels.

.. _`rcu_lockdep_warn`:

RCU_LOCKDEP_WARN
================

.. c:function::  RCU_LOCKDEP_WARN( c,  s)

    emit lockdep splat if specified condition is met

    :param c:
        condition to check
    :type c: 

    :param s:
        informative message
    :type s: 

.. _`rcu_initializer`:

RCU_INITIALIZER
===============

.. c:function::  RCU_INITIALIZER( v)

    statically initialize an RCU-protected global variable

    :param v:
        The value to statically initialize with.
    :type v: 

.. _`rcu_assign_pointer`:

rcu_assign_pointer
==================

.. c:function::  rcu_assign_pointer( p,  v)

    assign to RCU-protected pointer

    :param p:
        pointer to assign to
    :type p: 

    :param v:
        value to assign (publish)
    :type v: 

.. _`rcu_assign_pointer.description`:

Description
-----------

Assigns the specified value to the specified RCU-protected
pointer, ensuring that any concurrent RCU readers will see
any prior initialization.

Inserts memory barriers on architectures that require them
(which is most of them), and also prevents the compiler from
reordering the code that initializes the structure after the pointer
assignment.  More importantly, this call documents which pointers
will be dereferenced by RCU read-side code.

In some special cases, you may use \ :c:func:`RCU_INIT_POINTER`\  instead
of \ :c:func:`rcu_assign_pointer`\ .  \ :c:func:`RCU_INIT_POINTER`\  is a bit faster due
to the fact that it does not constrain either the CPU or the compiler.
That said, using \ :c:func:`RCU_INIT_POINTER`\  when you should have used
\ :c:func:`rcu_assign_pointer`\  is a very bad thing that results in
impossible-to-diagnose memory corruption.  So please be careful.
See the \ :c:func:`RCU_INIT_POINTER`\  comment header for details.

Note that \ :c:func:`rcu_assign_pointer`\  evaluates each of its arguments only
once, appearances notwithstanding.  One of the "extra" evaluations
is in \ :c:func:`typeof`\  and the other visible only to sparse (__CHECKER__),
neither of which actually execute the argument.  As with most cpp
macros, this execute-arguments-only-once property is important, so
please be careful when making changes to \ :c:func:`rcu_assign_pointer`\  and the
other macros that it invokes.

.. _`rcu_swap_protected`:

rcu_swap_protected
==================

.. c:function::  rcu_swap_protected( rcu_ptr,  ptr,  c)

    swap an RCU and a regular pointer

    :param rcu_ptr:
        RCU pointer
    :type rcu_ptr: 

    :param ptr:
        regular pointer
    :type ptr: 

    :param c:
        the conditions under which the dereference will take place
    :type c: 

.. _`rcu_swap_protected.description`:

Description
-----------

Perform swap(@rcu_ptr, \ ``ptr``\ ) where \ ``rcu_ptr``\  is an RCU-annotated pointer and
\ ``c``\  is the argument that is passed to the \ :c:func:`rcu_dereference_protected`\  call
used to read that pointer.

.. _`rcu_access_pointer`:

rcu_access_pointer
==================

.. c:function::  rcu_access_pointer( p)

    fetch RCU pointer with no dereferencing

    :param p:
        The pointer to read
    :type p: 

.. _`rcu_access_pointer.description`:

Description
-----------

Return the value of the specified RCU-protected pointer, but omit the
lockdep checks for being in an RCU read-side critical section.  This is
useful when the value of this pointer is accessed, but the pointer is
not dereferenced, for example, when testing an RCU-protected pointer
against NULL.  Although \ :c:func:`rcu_access_pointer`\  may also be used in cases
where update-side locks prevent the value of the pointer from changing,
you should instead use \ :c:func:`rcu_dereference_protected`\  for this use case.

It is also permissible to use \ :c:func:`rcu_access_pointer`\  when read-side
access to the pointer was removed at least one grace period ago, as
is the case in the context of the RCU callback that is freeing up
the data, or after a \ :c:func:`synchronize_rcu`\  returns.  This can be useful
when tearing down multi-linked structures after a grace period
has elapsed.

.. _`rcu_dereference_check`:

rcu_dereference_check
=====================

.. c:function::  rcu_dereference_check( p,  c)

    rcu_dereference with debug checking

    :param p:
        The pointer to read, prior to dereferencing
    :type p: 

    :param c:
        The conditions under which the dereference will take place
    :type c: 

.. _`rcu_dereference_check.description`:

Description
-----------

Do an \ :c:func:`rcu_dereference`\ , but check that the conditions under which the
dereference will take place are correct.  Typically the conditions
indicate the various locking conditions that should be held at that
point.  The check should return true if the conditions are satisfied.
An implicit check for being in an RCU read-side critical section
(rcu_read_lock()) is included.

.. _`rcu_dereference_check.for-example`:

For example
-----------


     bar = rcu_dereference_check(foo->bar, lockdep_is_held(&foo->lock));

could be used to indicate to lockdep that foo->bar may only be dereferenced
if either \ :c:func:`rcu_read_lock`\  is held, or that the lock required to replace
the bar struct at foo->bar is held.

Note that the list of conditions may also include indications of when a lock
need not be held, for example during initialisation or destruction of the

.. _`rcu_dereference_check.target-struct`:

target struct
-------------


     bar = rcu_dereference_check(foo->bar, lockdep_is_held(&foo->lock) ||
                                           atomic_read(&foo->usage) == 0);

Inserts memory barriers on architectures that require them
(currently only the Alpha), prevents the compiler from refetching
(and from merging fetches), and, more importantly, documents exactly
which pointers are protected by RCU and checks that the pointer is
annotated as __rcu.

.. _`rcu_dereference_bh_check`:

rcu_dereference_bh_check
========================

.. c:function::  rcu_dereference_bh_check( p,  c)

    rcu_dereference_bh with debug checking

    :param p:
        The pointer to read, prior to dereferencing
    :type p: 

    :param c:
        The conditions under which the dereference will take place
    :type c: 

.. _`rcu_dereference_bh_check.description`:

Description
-----------

This is the RCU-bh counterpart to \ :c:func:`rcu_dereference_check`\ .

.. _`rcu_dereference_sched_check`:

rcu_dereference_sched_check
===========================

.. c:function::  rcu_dereference_sched_check( p,  c)

    rcu_dereference_sched with debug checking

    :param p:
        The pointer to read, prior to dereferencing
    :type p: 

    :param c:
        The conditions under which the dereference will take place
    :type c: 

.. _`rcu_dereference_sched_check.description`:

Description
-----------

This is the RCU-sched counterpart to \ :c:func:`rcu_dereference_check`\ .

.. _`rcu_dereference_protected`:

rcu_dereference_protected
=========================

.. c:function::  rcu_dereference_protected( p,  c)

    fetch RCU pointer when updates prevented

    :param p:
        The pointer to read, prior to dereferencing
    :type p: 

    :param c:
        The conditions under which the dereference will take place
    :type c: 

.. _`rcu_dereference_protected.description`:

Description
-----------

Return the value of the specified RCU-protected pointer, but omit
the \ :c:func:`READ_ONCE`\ .  This is useful in cases where update-side locks
prevent the value of the pointer from changing.  Please note that this
primitive does *not* prevent the compiler from repeating this reference
or combining it with other references, so it should not be used without
protection of appropriate locks.

This function is only for update-side use.  Using this function
when protected only by \ :c:func:`rcu_read_lock`\  will result in infrequent
but very ugly failures.

.. _`rcu_dereference`:

rcu_dereference
===============

.. c:function::  rcu_dereference( p)

    fetch RCU-protected pointer for dereferencing

    :param p:
        The pointer to read, prior to dereferencing
    :type p: 

.. _`rcu_dereference.description`:

Description
-----------

This is a simple wrapper around \ :c:func:`rcu_dereference_check`\ .

.. _`rcu_dereference_bh`:

rcu_dereference_bh
==================

.. c:function::  rcu_dereference_bh( p)

    fetch an RCU-bh-protected pointer for dereferencing

    :param p:
        The pointer to read, prior to dereferencing
    :type p: 

.. _`rcu_dereference_bh.description`:

Description
-----------

Makes \ :c:func:`rcu_dereference_check`\  do the dirty work.

.. _`rcu_dereference_sched`:

rcu_dereference_sched
=====================

.. c:function::  rcu_dereference_sched( p)

    fetch RCU-sched-protected pointer for dereferencing

    :param p:
        The pointer to read, prior to dereferencing
    :type p: 

.. _`rcu_dereference_sched.description`:

Description
-----------

Makes \ :c:func:`rcu_dereference_check`\  do the dirty work.

.. _`rcu_pointer_handoff`:

rcu_pointer_handoff
===================

.. c:function::  rcu_pointer_handoff( p)

    Hand off a pointer from RCU to other mechanism

    :param p:
        The pointer to hand off
    :type p: 

.. _`rcu_pointer_handoff.description`:

Description
-----------

This is simply an identity function, but it documents where a pointer
is handed off from RCU to some other synchronization mechanism, for
example, reference counting or locking.  In C11, it would map to
\ :c:func:`kill_dependency`\ .  It could be used as follows::

     rcu_read_lock();
     p = rcu_dereference(gp);
     long_lived = is_long_lived(p);
     if (long_lived) {
             if (!atomic_inc_not_zero(p->refcnt))
                     long_lived = false;
             else
                     p = rcu_pointer_handoff(p);
     }
     rcu_read_unlock();

.. _`rcu_read_lock`:

rcu_read_lock
=============

.. c:function:: void rcu_read_lock( void)

    mark the beginning of an RCU read-side critical section

    :param void:
        no arguments
    :type void: 

.. _`rcu_read_lock.description`:

Description
-----------

When \ :c:func:`synchronize_rcu`\  is invoked on one CPU while other CPUs
are within RCU read-side critical sections, then the
\ :c:func:`synchronize_rcu`\  is guaranteed to block until after all the other
CPUs exit their critical sections.  Similarly, if \ :c:func:`call_rcu`\  is invoked
on one CPU while other CPUs are within RCU read-side critical
sections, invocation of the corresponding RCU callback is deferred
until after the all the other CPUs exit their critical sections.

Note, however, that RCU callbacks are permitted to run concurrently
with new RCU read-side critical sections.  One way that this can happen
is via the following sequence of events: (1) CPU 0 enters an RCU
read-side critical section, (2) CPU 1 invokes \ :c:func:`call_rcu`\  to register
an RCU callback, (3) CPU 0 exits the RCU read-side critical section,
(4) CPU 2 enters a RCU read-side critical section, (5) the RCU
callback is invoked.  This is legal, because the RCU read-side critical
section that was running concurrently with the \ :c:func:`call_rcu`\  (and which
therefore might be referencing something that the corresponding RCU
callback would free up) has completed before the corresponding
RCU callback is invoked.

RCU read-side critical sections may be nested.  Any deferred actions
will be deferred until the outermost RCU read-side critical section
completes.

You can avoid reading and understanding the next paragraph by
following this rule: don't put anything in an \ :c:func:`rcu_read_lock`\  RCU
read-side critical section that would block in a !PREEMPT kernel.
But if you want the full story, read on!

In non-preemptible RCU implementations (TREE_RCU and TINY_RCU),
it is illegal to block while in an RCU read-side critical section.
In preemptible RCU implementations (PREEMPT_RCU) in CONFIG_PREEMPT
kernel builds, RCU read-side critical sections may be preempted,
but explicit blocking is illegal.  Finally, in preemptible RCU
implementations in real-time (with -rt patchset) kernel builds, RCU
read-side critical sections may be preempted and they may also block, but
only when acquiring spinlocks that are subject to priority inheritance.

.. _`rcu_read_unlock`:

rcu_read_unlock
===============

.. c:function:: void rcu_read_unlock( void)

    marks the end of an RCU read-side critical section.

    :param void:
        no arguments
    :type void: 

.. _`rcu_read_unlock.description`:

Description
-----------

In most situations, \ :c:func:`rcu_read_unlock`\  is immune from deadlock.
However, in kernels built with CONFIG_RCU_BOOST, \ :c:func:`rcu_read_unlock`\ 
is responsible for deboosting, which it does via \ :c:func:`rt_mutex_unlock`\ .
Unfortunately, this function acquires the scheduler's runqueue and
priority-inheritance spinlocks.  This means that deadlock could result
if the caller of \ :c:func:`rcu_read_unlock`\  already holds one of these locks or
any lock that is ever acquired while holding them.

That said, RCU readers are never priority boosted unless they were
preempted.  Therefore, one way to avoid deadlock is to make sure
that preemption never happens within any RCU read-side critical
section whose outermost \ :c:func:`rcu_read_unlock`\  is called with one of
\ :c:func:`rt_mutex_unlock`\ 's locks held.  Such preemption can be avoided in
a number of ways, for example, by invoking \ :c:func:`preempt_disable`\  before
critical section's outermost \ :c:func:`rcu_read_lock`\ .

Given that the set of locks acquired by \ :c:func:`rt_mutex_unlock`\  might change
at any time, a somewhat more future-proofed approach is to make sure
that that preemption never happens within any RCU read-side critical
section whose outermost \ :c:func:`rcu_read_unlock`\  is called with irqs disabled.
This approach relies on the fact that \ :c:func:`rt_mutex_unlock`\  currently only
acquires irq-disabled locks.

The second of these two approaches is best in most situations,
however, the first approach can also be useful, at least to those
developers willing to keep abreast of the set of locks acquired by
\ :c:func:`rt_mutex_unlock`\ .

See \ :c:func:`rcu_read_lock`\  for more information.

.. _`rcu_read_lock_bh`:

rcu_read_lock_bh
================

.. c:function:: void rcu_read_lock_bh( void)

    mark the beginning of an RCU-bh critical section

    :param void:
        no arguments
    :type void: 

.. _`rcu_read_lock_bh.description`:

Description
-----------

This is equivalent of \ :c:func:`rcu_read_lock`\ , but also disables softirqs.
Note that anything else that disables softirqs can also serve as
an RCU read-side critical section.

Note that \ :c:func:`rcu_read_lock_bh`\  and the matching \ :c:func:`rcu_read_unlock_bh`\ 
must occur in the same context, for example, it is illegal to invoke
\ :c:func:`rcu_read_unlock_bh`\  from one task if the matching \ :c:func:`rcu_read_lock_bh`\ 
was invoked from some other task.

.. _`rcu_read_lock_sched`:

rcu_read_lock_sched
===================

.. c:function:: void rcu_read_lock_sched( void)

    mark the beginning of a RCU-sched critical section

    :param void:
        no arguments
    :type void: 

.. _`rcu_read_lock_sched.description`:

Description
-----------

This is equivalent of \ :c:func:`rcu_read_lock`\ , but disables preemption.
Read-side critical sections can also be introduced by anything else
that disables preemption, including \ :c:func:`local_irq_disable`\  and friends.

Note that \ :c:func:`rcu_read_lock_sched`\  and the matching \ :c:func:`rcu_read_unlock_sched`\ 
must occur in the same context, for example, it is illegal to invoke
\ :c:func:`rcu_read_unlock_sched`\  from process context if the matching
\ :c:func:`rcu_read_lock_sched`\  was invoked from an NMI handler.

.. _`rcu_init_pointer`:

RCU_INIT_POINTER
================

.. c:function::  RCU_INIT_POINTER( p,  v)

    initialize an RCU protected pointer

    :param p:
        The pointer to be initialized.
    :type p: 

    :param v:
        The value to initialized the pointer to.
    :type v: 

.. _`rcu_init_pointer.description`:

Description
-----------

Initialize an RCU-protected pointer in special cases where readers
do not need ordering constraints on the CPU or the compiler.  These

.. _`rcu_init_pointer.special-cases-are`:

special cases are
-----------------


1.   This use of \ :c:func:`RCU_INIT_POINTER`\  is NULLing out the pointer *or*
2.   The caller has taken whatever steps are required to prevent
     RCU readers from concurrently accessing this pointer *or*
3.   The referenced data structure has already been exposed to
     readers either at compile time or via \ :c:func:`rcu_assign_pointer`\  *and*

     a.      You have not made *any* reader-visible changes to
             this structure since then *or*
     b.      It is OK for readers accessing this structure from its
             new location to see the old state of the structure.  (For
             example, the changes were to statistical counters or to
             other state where exact synchronization is not required.)

Failure to follow these rules governing use of \ :c:func:`RCU_INIT_POINTER`\  will
result in impossible-to-diagnose memory corruption.  As in the structures
will look OK in crash dumps, but any concurrent RCU readers might
see pre-initialized values of the referenced data structure.  So
please be very careful how you use \ :c:func:`RCU_INIT_POINTER`\ !!!

If you are creating an RCU-protected linked structure that is accessed
by a single external-to-structure RCU-protected pointer, then you may
use \ :c:func:`RCU_INIT_POINTER`\  to initialize the internal RCU-protected
pointers, but you must use \ :c:func:`rcu_assign_pointer`\  to initialize the
external-to-structure pointer *after* you have completely initialized
the reader-accessible portions of the linked structure.

Note that unlike \ :c:func:`rcu_assign_pointer`\ , \ :c:func:`RCU_INIT_POINTER`\  provides no
ordering guarantees for either the CPU or the compiler.

.. _`rcu_pointer_initializer`:

RCU_POINTER_INITIALIZER
=======================

.. c:function::  RCU_POINTER_INITIALIZER( p,  v)

    statically initialize an RCU protected pointer

    :param p:
        The pointer to be initialized.
    :type p: 

    :param v:
        The value to initialized the pointer to.
    :type v: 

.. _`rcu_pointer_initializer.description`:

Description
-----------

GCC-style initialization for an RCU-protected pointer in a structure field.

.. _`kfree_rcu`:

kfree_rcu
=========

.. c:function::  kfree_rcu( ptr,  rcu_head)

    kfree an object after a grace period.

    :param ptr:
        pointer to kfree
    :type ptr: 

    :param rcu_head:
        the name of the struct rcu_head within the type of \ ``ptr``\ .
    :type rcu_head: 

.. _`kfree_rcu.description`:

Description
-----------

Many rcu callbacks functions just call \ :c:func:`kfree`\  on the base structure.
These functions are trivial, but their size adds up, and furthermore
when they are used in a kernel module, that module must invoke the
high-latency \ :c:func:`rcu_barrier`\  function at module-unload time.

The \ :c:func:`kfree_rcu`\  function handles this issue.  Rather than encoding a
function address in the embedded rcu_head structure, \ :c:func:`kfree_rcu`\  instead
encodes the offset of the rcu_head structure within the base structure.
Because the functions are not allowed in the low-order 4096 bytes of
kernel virtual memory, offsets up to 4095 bytes can be accommodated.
If the offset is larger than 4095 bytes, a compile-time error will
be generated in \ :c:func:`__kfree_rcu`\ .  If this error is triggered, you can
either fall back to use of \ :c:func:`call_rcu`\  or rearrange the structure to
position the rcu_head structure into the first 4096 bytes.

Note that the allowable offset might decrease in the future, for example,
to allow something like \ :c:func:`kmem_cache_free_rcu`\ .

The BUILD_BUG_ON check must not involve any function calls, hence the
checks are done in macros here.

.. This file was automatic generated / don't edit.

