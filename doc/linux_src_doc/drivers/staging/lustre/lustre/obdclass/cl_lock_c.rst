.. -*- coding: utf-8; mode: rst -*-

=========
cl_lock.c
=========


.. _`cl_lock_invariant_trusted`:

cl_lock_invariant_trusted
=========================

.. c:function:: int cl_lock_invariant_trusted (const struct lu_env *env, const struct cl_lock *lock)

    :param const struct lu_env \*env:

        *undescribed*

    :param const struct cl_lock \*lock:

        *undescribed*



.. _`cl_lock_invariant_trusted.description`:

Description
-----------

reference to \a lock, or somehow assures that \a lock cannot be freed.

\see :c:func:`cl_lock_invariant`



.. _`cl_lock_invariant`:

cl_lock_invariant
=================

.. c:function:: int cl_lock_invariant (const struct lu_env *env, const struct cl_lock *lock)

    :param const struct lu_env \*env:

        *undescribed*

    :param const struct cl_lock \*lock:

        *undescribed*



.. _`cl_lock_invariant.description`:

Description
-----------


\see :c:func:`cl_lock_invariant_trusted`



.. _`cl_lock_nesting`:

cl_lock_nesting
===============

.. c:function:: enum clt_nesting_level cl_lock_nesting (const struct cl_lock *lock)

    lock and 1 for a sub-lock.

    :param const struct cl_lock \*lock:

        *undescribed*



.. _`cl_lock_counters`:

cl_lock_counters
================

.. c:function:: struct cl_thread_counters *cl_lock_counters (const struct lu_env *env, const struct cl_lock *lock)

    :param const struct lu_env \*env:

        *undescribed*

    :param const struct cl_lock \*lock:

        *undescribed*



.. _`cl_lock_slice_add`:

cl_lock_slice_add
=================

.. c:function:: void cl_lock_slice_add (struct cl_lock *lock, struct cl_lock_slice *slice, struct cl_object *obj, const struct cl_lock_operations *ops)

    :param struct cl_lock \*lock:

        *undescribed*

    :param struct cl_lock_slice \*slice:

        *undescribed*

    :param struct cl_object \*obj:

        *undescribed*

    :param const struct cl_lock_operations \*ops:

        *undescribed*



.. _`cl_lock_slice_add.this-is-called-by-cl_object_operations`:

This is called by cl_object_operations
--------------------------------------

::c:func:`coo_lock_init` methods to add a
per-layer state to the lock. New state is added at the end of



.. _`cl_lock_slice_add.cl_lock`:

cl_lock
-------

:cll_layers list, that is, it is at the bottom of the stack.

\see :c:func:`cl_req_slice_add`, :c:func:`cl_page_slice_add`, :c:func:`cl_io_slice_add`



.. _`cl_lock_mode_match`:

cl_lock_mode_match
==================

.. c:function:: int cl_lock_mode_match (enum cl_lock_mode has, enum cl_lock_mode need)

    :param enum cl_lock_mode has:

        *undescribed*

    :param enum cl_lock_mode need:

        *undescribed*



.. _`cl_lock_mode_match.description`:

Description
-----------

guarantees as a lock with the mode \a need.



.. _`cl_lock_ext_match`:

cl_lock_ext_match
=================

.. c:function:: int cl_lock_ext_match (const struct cl_lock_descr *has, const struct cl_lock_descr *need)

    :param const struct cl_lock_descr \*has:

        *undescribed*

    :param const struct cl_lock_descr \*need:

        *undescribed*



.. _`cl_lock_descr_match`:

cl_lock_descr_match
===================

.. c:function:: int cl_lock_descr_match (const struct cl_lock_descr *has, const struct cl_lock_descr *need)

    :param const struct cl_lock_descr \*has:

        *undescribed*

    :param const struct cl_lock_descr \*need:

        *undescribed*



.. _`cl_lock_descr_match.description`:

Description
-----------

same guarantees as a lock with the description \a need.



.. _`cl_lock_put`:

cl_lock_put
===========

.. c:function:: void cl_lock_put (const struct lu_env *env, struct cl_lock *lock)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*



.. _`cl_lock_put.description`:

Description
-----------


When last reference is released, lock is returned to the cache, unless it



.. _`cl_lock_put.is-in-cl_lock_state`:

is in cl_lock_state
-------------------

:CLS_FREEING state, in which case it is destroyed
immediately.

\see :c:func:`cl_object_put`, :c:func:`cl_page_put`



.. _`cl_lock_get`:

cl_lock_get
===========

.. c:function:: void cl_lock_get (struct cl_lock *lock)

    :param struct cl_lock \*lock:

        *undescribed*



.. _`cl_lock_get.description`:

Description
-----------


This can be called only by caller already possessing a reference to \a
lock.

\see :c:func:`cl_object_get`, :c:func:`cl_page_get`



.. _`cl_lock_get_trust`:

cl_lock_get_trust
=================

.. c:function:: void cl_lock_get_trust (struct cl_lock *lock)

    :param struct cl_lock \*lock:

        *undescribed*



.. _`cl_lock_get_trust.description`:

Description
-----------


This is much like :c:func:`cl_lock_get`, except that this function can be used to
acquire initial reference to the cached lock. Caller has to deal with all
possible races. Use with care!

\see :c:func:`cl_page_get_trust`



.. _`cl_lock_finish`:

cl_lock_finish
==============

.. c:function:: void cl_lock_finish (const struct lu_env *env, struct cl_lock *lock)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*



.. _`cl_lock_finish.description`:

Description
-----------


Other threads can acquire references to the top-lock through its
sub-locks. Hence, it cannot be :c:func:`cl_lock_free`-ed immediately.



.. _`cl_lock_intransit`:

cl_lock_intransit
=================

.. c:function:: enum cl_lock_state cl_lock_intransit (const struct lu_env *env, struct cl_lock *lock)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*



.. _`cl_lock_intransit.description`:

Description
-----------


\pre  state: CLS_CACHED, CLS_HELD or CLS_ENQUEUED
\post state: CLS_INTRANSIT
\see CLS_INTRANSIT



.. _`cl_lock_extransit`:

cl_lock_extransit
=================

.. c:function:: void cl_lock_extransit (const struct lu_env *env, struct cl_lock *lock, enum cl_lock_state state)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*

    :param enum cl_lock_state state:

        *undescribed*



.. _`cl_lock_is_intransit`:

cl_lock_is_intransit
====================

.. c:function:: int cl_lock_is_intransit (struct cl_lock *lock)

    :param struct cl_lock \*lock:

        *undescribed*



.. _`cl_lock_fits_into`:

cl_lock_fits_into
=================

.. c:function:: int cl_lock_fits_into (const struct lu_env *env, const struct cl_lock *lock, const struct cl_lock_descr *need, const struct cl_io *io)

    :param const struct lu_env \*env:

        *undescribed*

    :param const struct cl_lock \*lock:

        *undescribed*

    :param const struct cl_lock_descr \*need:

        *undescribed*

    :param const struct cl_io \*io:

        *undescribed*



.. _`cl_lock_fits_into.description`:

Description
-----------

truncate and O_APPEND cannot be reused for read/non-append-write, as they
cover multiple stripes and can trigger cascading timeouts.



.. _`cl_lock_find`:

cl_lock_find
============

.. c:function:: struct cl_lock *cl_lock_find (const struct lu_env *env, const struct cl_io *io, const struct cl_lock_descr *need)

    :param const struct lu_env \*env:

        *undescribed*

    :param const struct cl_io \*io:

        *undescribed*

    :param const struct cl_lock_descr \*need:

        *undescribed*



.. _`cl_lock_find.description`:

Description
-----------


This is the main entry point into the cl_lock caching interface. First, a
cache (implemented as a per-object linked list) is consulted. If lock is
found there, it is returned immediately. Otherwise new lock is allocated
and returned. In any case, additional reference to lock is acquired.

\see :c:func:`cl_object_find`, :c:func:`cl_page_find`



.. _`cl_lock_peek`:

cl_lock_peek
============

.. c:function:: struct cl_lock *cl_lock_peek (const struct lu_env *env, const struct cl_io *io, const struct cl_lock_descr *need, const char *scope, const void *source)

    :param const struct lu_env \*env:

        *undescribed*

    :param const struct cl_io \*io:

        *undescribed*

    :param const struct cl_lock_descr \*need:

        *undescribed*

    :param const char \*scope:

        *undescribed*

    :param const void \*source:

        *undescribed*



.. _`cl_lock_peek.description`:

Description
-----------

:c:func:`cl_lock_find` except that no new lock is created, and returned lock is



.. _`cl_lock_peek.guaranteed-to-be-in-enum-cl_lock_state`:

guaranteed to be in enum cl_lock_state
--------------------------------------

:CLS_HELD state.



.. _`cl_lock_at`:

cl_lock_at
==========

.. c:function:: const struct cl_lock_slice *cl_lock_at (const struct cl_lock *lock, const struct lu_device_type *dtype)

    :param const struct cl_lock \*lock:

        *undescribed*

    :param const struct lu_device_type \*dtype:

        *undescribed*



.. _`cl_lock_at.description`:

Description
-----------

device stack.

\see :c:func:`cl_page_at`



.. _`cl_lock_mutex_get`:

cl_lock_mutex_get
=================

.. c:function:: void cl_lock_mutex_get (const struct lu_env *env, struct cl_lock *lock)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*



.. _`cl_lock_mutex_get.description`:

Description
-----------


This is used to manipulate cl_lock fields, and to serialize state
transitions in the lock state machine.

\post cl_lock_is_mutexed(lock)

\see :c:func:`cl_lock_mutex_put`



.. _`cl_lock_mutex_try`:

cl_lock_mutex_try
=================

.. c:function:: int cl_lock_mutex_try (const struct lu_env *env, struct cl_lock *lock)

    locks cl_lock object.

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*



.. _`cl_lock_mutex_try.description`:

Description
-----------


\retval 0 \a lock was successfully locked

\retval -EBUSY \a lock cannot be locked right now

\post ergo(result == 0, cl_lock_is_mutexed(lock))

\see :c:func:`cl_lock_mutex_get`



.. _`cl_lock_mutex_put`:

cl_lock_mutex_put
=================

.. c:function:: void cl_lock_mutex_put (const struct lu_env *env, struct cl_lock *lock)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*



.. _`cl_lock_mutex_put.description`:

Description
-----------


\pre cl_lock_is_mutexed(lock)

\see :c:func:`cl_lock_mutex_get`



.. _`cl_lock_is_mutexed`:

cl_lock_is_mutexed
==================

.. c:function:: int cl_lock_is_mutexed (struct cl_lock *lock)

    :param struct cl_lock \*lock:

        *undescribed*



.. _`cl_lock_nr_mutexed`:

cl_lock_nr_mutexed
==================

.. c:function:: int cl_lock_nr_mutexed (const struct lu_env *env)

    :param const struct lu_env \*env:

        *undescribed*



.. _`cl_lock_hold_mod`:

cl_lock_hold_mod
================

.. c:function:: void cl_lock_hold_mod (const struct lu_env *env, struct cl_lock *lock, int delta)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*

    :param int delta:

        *undescribed*



.. _`cl_lock_hold_mod.description`:

Description
-----------

top-lock (nesting == 0) accounts for this modification in the per-thread
debugging counters. Sub-lock holds can be released by a thread different
from one that acquired it.



.. _`cl_lock_used_mod`:

cl_lock_used_mod
================

.. c:function:: void cl_lock_used_mod (const struct lu_env *env, struct cl_lock *lock, int delta)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*

    :param int delta:

        *undescribed*



.. _`cl_lock_used_mod.description`:

Description
-----------

:c:func:`cl_lock_hold_mod` for the explanation of the debugging code.



.. _`cl_lock_state_wait`:

cl_lock_state_wait
==================

.. c:function:: int cl_lock_state_wait (const struct lu_env *env, struct cl_lock *lock)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*



.. _`cl_lock_state_wait.description`:

Description
-----------


This function is called with cl_lock mutex locked, atomically releases
mutex and goes to sleep, waiting for a lock state change (signaled by
:c:func:`cl_lock_signal`), and re-acquires the mutex before return.

This function is used to wait until lock state machine makes some progress
and to emulate synchronous operations on top of asynchronous lock
interface.

\retval -EINTR wait was interrupted

\retval 0 wait wasn't interrupted

\pre cl_lock_is_mutexed(lock)

\see :c:func:`cl_lock_signal`



.. _`cl_lock_signal`:

cl_lock_signal
==============

.. c:function:: void cl_lock_signal (const struct lu_env *env, struct cl_lock *lock)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*



.. _`cl_lock_signal.description`:

Description
-----------


Wakes up all waiters sleeping in :c:func:`cl_lock_state_wait`, also notifies all



.. _`cl_lock_signal.layers-about-state-change-by-calling-cl_lock_operations`:

layers about state change by calling cl_lock_operations
-------------------------------------------------------

::c:func:`clo_state`
top-to-bottom.



.. _`cl_lock_state_set`:

cl_lock_state_set
=================

.. c:function:: void cl_lock_state_set (const struct lu_env *env, struct cl_lock *lock, enum cl_lock_state state)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*

    :param enum cl_lock_state state:

        *undescribed*



.. _`cl_lock_state_set.description`:

Description
-----------


This function is invoked to notify layers that lock state changed, possible
as a result of an asynchronous event such as call-back reception.

\post lock->cll_state == state

\see cl_lock_operations:::c:func:`clo_state`



.. _`cl_use_try`:

cl_use_try
==========

.. c:function:: int cl_use_try (const struct lu_env *env, struct cl_lock *lock, int atomic)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*

    :param int atomic:

        *undescribed*



.. _`cl_use_try.cl_lock_operations`:

cl_lock_operations
------------------

::c:func:`clo_use` top-to-bottom to notify layers.
``atomic`` = 1, it must unuse the lock to recovery the lock to keep the
use process atomic



.. _`cl_enqueue_kick`:

cl_enqueue_kick
===============

.. c:function:: int cl_enqueue_kick (const struct lu_env *env, struct cl_lock *lock, struct cl_io *io, __u32 flags)

    >clo_enqueue() across all layers top-to-bottom.

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*

    :param struct cl_io \*io:

        *undescribed*

    :param __u32 flags:

        *undescribed*



.. _`cl_enqueue_try`:

cl_enqueue_try
==============

.. c:function:: int cl_enqueue_try (const struct lu_env *env, struct cl_lock *lock, struct cl_io *io, __u32 flags)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*

    :param struct cl_io \*io:

        *undescribed*

    :param __u32 flags:

        *undescribed*



.. _`cl_enqueue_try.description`:

Description
-----------


This function is called repeatedly by :c:func:`cl_enqueue` until either lock is
enqueued, or error occurs. This function does not block waiting for
networking communication to complete.

\post ergo(result == 0, lock->cll_state == CLS_ENQUEUED ||
lock->cll_state == CLS_HELD)

\see :c:func:`cl_enqueue` cl_lock_operations:::c:func:`clo_enqueue`
\see cl_lock_state::CLS_ENQUEUED



.. _`cl_lock_enqueue_wait`:

cl_lock_enqueue_wait
====================

.. c:function:: int cl_lock_enqueue_wait (const struct lu_env *env, struct cl_lock *lock, int keep_mutex)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*

    :param int keep_mutex:

        *undescribed*



.. _`cl_lock_enqueue_wait.description`:

Description
-----------


\retval 0 conflicting lock has been canceled.
\retval -ve error code.



.. _`cl_unuse_try`:

cl_unuse_try
============

.. c:function:: int cl_unuse_try (const struct lu_env *env, struct cl_lock *lock)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*



.. _`cl_unuse_try.this-function-is-called-to-release-underlying-resource`:

This function is called to release underlying resource
------------------------------------------------------

1. for top lock, the resource is sublocks it held;
2. for sublock, the resource is the reference to dlmlock.

cl_unuse_try is a one-shot operation, so it must NOT return CLO_WAIT.

\see :c:func:`cl_unuse` cl_lock_operations:::c:func:`clo_unuse`
\see cl_lock_state::CLS_CACHED



.. _`cl_unuse`:

cl_unuse
========

.. c:function:: void cl_unuse (const struct lu_env *env, struct cl_lock *lock)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*



.. _`cl_wait_try`:

cl_wait_try
===========

.. c:function:: int cl_wait_try (const struct lu_env *env, struct cl_lock *lock)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*



.. _`cl_wait_try.description`:

Description
-----------


This function is called repeatedly by :c:func:`cl_wait` until either lock is
granted, or error occurs. This function does not block waiting for network
communication to complete.

\see :c:func:`cl_wait` cl_lock_operations:::c:func:`clo_wait`
\see cl_lock_state::CLS_HELD



.. _`cl_wait`:

cl_wait
=======

.. c:function:: int cl_wait (const struct lu_env *env, struct cl_lock *lock)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*



.. _`cl_wait.description`:

Description
-----------


\pre current thread or io owns a hold on the lock
\pre ergo(result == 0, lock->cll_state == CLS_ENQUEUED ||
lock->cll_state == CLS_HELD)

\post ergo(result == 0, lock->cll_state == CLS_HELD)



.. _`cl_lock_weigh`:

cl_lock_weigh
=============

.. c:function:: unsigned long cl_lock_weigh (const struct lu_env *env, struct cl_lock *lock)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*



.. _`cl_lock_weigh.description`:

Description
-----------

value.



.. _`cl_lock_modify`:

cl_lock_modify
==============

.. c:function:: int cl_lock_modify (const struct lu_env *env, struct cl_lock *lock, const struct cl_lock_descr *desc)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*

    :param const struct cl_lock_descr \*desc:

        *undescribed*



.. _`cl_lock_modify.description`:

Description
-----------


The server can grant client a lock different from one that was requested
(e.g., larger in extent). This method is called when actually granted lock
description becomes known to let layers to accommodate for changed lock
description.

\see cl_lock_operations:::c:func:`clo_modify`



.. _`cl_lock_closure_init`:

cl_lock_closure_init
====================

.. c:function:: void cl_lock_closure_init (const struct lu_env *env, struct cl_lock_closure *closure, struct cl_lock *origin, int wait)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock_closure \*closure:

        *undescribed*

    :param struct cl_lock \*origin:

        *undescribed*

    :param int wait:

        *undescribed*



.. _`cl_lock_closure_init.description`:

Description
-----------


\see cl_lock_closure



.. _`cl_lock_closure_build`:

cl_lock_closure_build
=====================

.. c:function:: int cl_lock_closure_build (const struct lu_env *env, struct cl_lock *lock, struct cl_lock_closure *closure)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*

    :param struct cl_lock_closure \*closure:

        *undescribed*



.. _`cl_lock_closure_build.description`:

Description
-----------


Building of a closure consists of adding initial lock (\a lock) into it,



.. _`cl_lock_closure_build.and-calling-cl_lock_operations`:

and calling cl_lock_operations
------------------------------

::c:func:`clo_closure` methods of \a lock. These
methods might call :c:func:`cl_lock_closure_build` recursively again, adding more
locks to the closure, etc.

\see cl_lock_closure



.. _`cl_lock_enclosure`:

cl_lock_enclosure
=================

.. c:function:: int cl_lock_enclosure (const struct lu_env *env, struct cl_lock *lock, struct cl_lock_closure *closure)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*

    :param struct cl_lock_closure \*closure:

        *undescribed*



.. _`cl_lock_enclosure.description`:

Description
-----------


Try-locks \a lock and if succeeded, adds it to the closure (never more than
once). If try-lock failed, returns CLO_REPEAT, after optionally waiting
until next try-lock is likely to succeed.



.. _`cl_lock_delete`:

cl_lock_delete
==============

.. c:function:: void cl_lock_delete (const struct lu_env *env, struct cl_lock *lock)

    to-top) that lock is being destroyed, then destroy the lock. If there are holds on the lock, postpone destruction until all holds are released. This is called when a decision is made to destroy the lock in the future. E.g., when a blocking AST is received on it, or fatal communication error happens.

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*



.. _`cl_lock_delete.description`:

Description
-----------


Caller must have a reference on this lock to prevent a situation, when
deleted lock lingers in memory for indefinite time, because nobody calls
:c:func:`cl_lock_put` to finish it.

\pre atomic_read(:c:type:`struct lock <lock>`->cll_ref) > 0
\pre ergo(cl_lock_nesting(lock) == CNL_TOP,
cl_lock_nr_mutexed(env) == 1)
[i.e., if a top-lock is deleted, mutices of no other locks can be
held, as deletion of sub-locks might require releasing a top-lock
mutex]

\see cl_lock_operations:::c:func:`clo_delete`
\see cl_lock::cll_holds



.. _`cl_lock_error`:

cl_lock_error
=============

.. c:function:: void cl_lock_error (const struct lu_env *env, struct cl_lock *lock, int error)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*

    :param int error:

        *undescribed*



.. _`cl_lock_error.description`:

Description
-----------

happens when, e.g., server fails to grant a lock to us, or networking
time-out happens.

\pre atomic_read(:c:type:`struct lock <lock>`->cll_ref) > 0

\see :c:func:`clo_lock_delete`
\see cl_lock::cll_holds



.. _`cl_lock_cancel`:

cl_lock_cancel
==============

.. c:function:: void cl_lock_cancel (const struct lu_env *env, struct cl_lock *lock)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*



.. _`cl_lock_cancel.description`:

Description
-----------

(bottom-to-top) that lock is being cancelled, then destroy the lock. If
there are holds on the lock, postpone cancellation until
all holds are released.

Cancellation notification is delivered to layers at most once.

\see cl_lock_operations:::c:func:`clo_cancel`
\see cl_lock::cll_holds



.. _`cl_lock_at_pgoff`:

cl_lock_at_pgoff
================

.. c:function:: struct cl_lock *cl_lock_at_pgoff (const struct lu_env *env, struct cl_object *obj, pgoff_t index, struct cl_lock *except, int pending, int canceld)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_object \*obj:

        *undescribed*

    :param pgoff_t index:

        *undescribed*

    :param struct cl_lock \*except:

        *undescribed*

    :param int pending:

        *undescribed*

    :param int canceld:

        *undescribed*



.. _`cl_lock_at_pgoff.description`:

Description
-----------

given \a except lock.



.. _`pgoff_at_lock`:

pgoff_at_lock
=============

.. c:function:: pgoff_t pgoff_at_lock (struct cl_page *page, struct cl_lock *lock)

    :param struct cl_page \*page:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*



.. _`pgoff_at_lock.description`:

Description
-----------

At the time of this writing, ``page`` is top page and ``lock`` is sub lock.



.. _`check_and_discard_cb`:

check_and_discard_cb
====================

.. c:function:: int check_and_discard_cb (const struct lu_env *env, struct cl_io *io, struct cl_page *page, void *cbdata)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_io \*io:

        *undescribed*

    :param struct cl_page \*page:

        *undescribed*

    :param void \*cbdata:

        *undescribed*



.. _`cl_lock_discard_pages`:

cl_lock_discard_pages
=====================

.. c:function:: int cl_lock_discard_pages (const struct lu_env *env, struct cl_lock *lock)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*



.. _`cl_lock_discard_pages.description`:

Description
-----------

tree to find all covering pages and discard them. If a page is being covered
by other locks, it should remain in cache.

If error happens on any step, the process continues anyway (the reasoning
behind this being that lock cancellation cannot be delayed indefinitely).



.. _`cl_locks_prune`:

cl_locks_prune
==============

.. c:function:: void cl_locks_prune (const struct lu_env *env, struct cl_object *obj, int cancel)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_object \*obj:

        *undescribed*

    :param int cancel:

        *undescribed*



.. _`cl_locks_prune.description`:

Description
-----------


Caller has to guarantee that no lock is in active use.

\param cancel when this is set, :c:func:`cl_locks_prune` cancels locks before
destroying.



.. _`cl_lock_hold`:

cl_lock_hold
============

.. c:function:: struct cl_lock *cl_lock_hold (const struct lu_env *env, const struct cl_io *io, const struct cl_lock_descr *need, const char *scope, const void *source)

    :param const struct lu_env \*env:

        *undescribed*

    :param const struct cl_io \*io:

        *undescribed*

    :param const struct cl_lock_descr \*need:

        *undescribed*

    :param const char \*scope:

        *undescribed*

    :param const void \*source:

        *undescribed*



.. _`cl_lock_hold.description`:

Description
-----------

it.

This is much like :c:func:`cl_lock_find`, except that :c:func:`cl_lock_hold` additionally
guarantees that lock is not in the CLS_FREEING state on return.



.. _`cl_lock_request`:

cl_lock_request
===============

.. c:function:: struct cl_lock *cl_lock_request (const struct lu_env *env, struct cl_io *io, const struct cl_lock_descr *need, const char *scope, const void *source)

    level entry point of cl_lock interface that finds existing or enqueues new lock matching given description.

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_io \*io:

        *undescribed*

    :param const struct cl_lock_descr \*need:

        *undescribed*

    :param const char \*scope:

        *undescribed*

    :param const void \*source:

        *undescribed*



.. _`cl_lock_hold_add`:

cl_lock_hold_add
================

.. c:function:: void cl_lock_hold_add (const struct lu_env *env, struct cl_lock *lock, const char *scope, const void *source)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*

    :param const char \*scope:

        *undescribed*

    :param const void \*source:

        *undescribed*



.. _`cl_lock_unhold`:

cl_lock_unhold
==============

.. c:function:: void cl_lock_unhold (const struct lu_env *env, struct cl_lock *lock, const char *scope, const void *source)

     mutex.

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*

    :param const char \*scope:

        *undescribed*

    :param const void \*source:

        *undescribed*



.. _`cl_lock_release`:

cl_lock_release
===============

.. c:function:: void cl_lock_release (const struct lu_env *env, struct cl_lock *lock, const char *scope, const void *source)

    :param const struct lu_env \*env:

        *undescribed*

    :param struct cl_lock \*lock:

        *undescribed*

    :param const char \*scope:

        *undescribed*

    :param const void \*source:

        *undescribed*



.. _`cl_lock_descr_print`:

cl_lock_descr_print
===================

.. c:function:: void cl_lock_descr_print (const struct lu_env *env, void *cookie, lu_printer_t printer, const struct cl_lock_descr *descr)

    :param const struct lu_env \*env:

        *undescribed*

    :param void \*cookie:

        *undescribed*

    :param lu_printer_t printer:

        *undescribed*

    :param const struct cl_lock_descr \*descr:

        *undescribed*



.. _`cl_lock_print`:

cl_lock_print
=============

.. c:function:: void cl_lock_print (const struct lu_env *env, void *cookie, lu_printer_t printer, const struct cl_lock *lock)

    :param const struct lu_env \*env:

        *undescribed*

    :param void \*cookie:

        *undescribed*

    :param lu_printer_t printer:

        *undescribed*

    :param const struct cl_lock \*lock:

        *undescribed*

