.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/percpu-refcount.c

.. _`percpu_ref_init`:

percpu_ref_init
===============

.. c:function:: int percpu_ref_init(struct percpu_ref *ref, percpu_ref_func_t *release, unsigned int flags, gfp_t gfp)

    initialize a percpu refcount

    :param struct percpu_ref \*ref:
        percpu_ref to initialize

    :param percpu_ref_func_t \*release:
        function which will be called when refcount hits 0

    :param unsigned int flags:
        PERCPU_REF_INIT\_\* flags

    :param gfp_t gfp:
        allocation mask to use

.. _`percpu_ref_init.description`:

Description
-----------

Initializes \ ``ref``\ .  If \ ``flags``\  is zero, \ ``ref``\  starts in percpu mode with a
refcount of 1; analagous to atomic_long_set(ref, 1).  See the
definitions of PERCPU_REF_INIT\_\* flags for flag behaviors.

Note that \ ``release``\  must not sleep - it may potentially be called from RCU
callback context by \ :c:func:`percpu_ref_kill`\ .

.. _`percpu_ref_exit`:

percpu_ref_exit
===============

.. c:function:: void percpu_ref_exit(struct percpu_ref *ref)

    undo \ :c:func:`percpu_ref_init`\ 

    :param struct percpu_ref \*ref:
        percpu_ref to exit

.. _`percpu_ref_exit.description`:

Description
-----------

This function exits \ ``ref``\ .  The caller is responsible for ensuring that
\ ``ref``\  is no longer in active use.  The usual places to invoke this
function from are the \ ``ref``\ ->\ :c:func:`release`\  callback or in init failure path
where \ :c:func:`percpu_ref_init`\  succeeded but other parts of the initialization
of the embedding object failed.

.. _`percpu_ref_switch_to_atomic`:

percpu_ref_switch_to_atomic
===========================

.. c:function:: void percpu_ref_switch_to_atomic(struct percpu_ref *ref, percpu_ref_func_t *confirm_switch)

    switch a percpu_ref to atomic mode

    :param struct percpu_ref \*ref:
        percpu_ref to switch to atomic mode

    :param percpu_ref_func_t \*confirm_switch:
        optional confirmation callback

.. _`percpu_ref_switch_to_atomic.description`:

Description
-----------

There's no reason to use this function for the usual reference counting.
Use percpu_ref_kill[_and_confirm]().

Schedule switching of \ ``ref``\  to atomic mode.  All its percpu counts will
be collected to the main atomic counter.  On completion, when all CPUs
are guaraneed to be in atomic mode, \ ``confirm_switch``\ , which may not
block, is invoked.  This function may be invoked concurrently with all
the get/put operations and can safely be mixed with kill and reinit
operations.  Note that \ ``ref``\  will stay in atomic mode across kill/reinit
cycles until \ :c:func:`percpu_ref_switch_to_percpu`\  is called.

This function normally doesn't block and can be called from any context
but it may block if \ ``confirm_kill``\  is specified and \ ``ref``\  is already in
the process of switching to atomic mode.  In such cases, \ ``confirm_switch``\ 
will be invoked after the switching is complete.

Due to the way percpu_ref is implemented, \ ``confirm_switch``\  will be called
after at least one full sched RCU grace period has passed but this is an
implementation detail and must not be depended upon.

.. _`percpu_ref_switch_to_percpu`:

percpu_ref_switch_to_percpu
===========================

.. c:function:: void percpu_ref_switch_to_percpu(struct percpu_ref *ref)

    switch a percpu_ref to percpu mode

    :param struct percpu_ref \*ref:
        percpu_ref to switch to percpu mode

.. _`percpu_ref_switch_to_percpu.description`:

Description
-----------

There's no reason to use this function for the usual reference counting.
To re-use an expired ref, use \ :c:func:`percpu_ref_reinit`\ .

Switch \ ``ref``\  to percpu mode.  This function may be invoked concurrently
with all the get/put operations and can safely be mixed with kill and
reinit operations.  This function reverses the sticky atomic state set
by PERCPU_REF_INIT_ATOMIC or \ :c:func:`percpu_ref_switch_to_atomic`\ .  If \ ``ref``\  is
dying or dead, the actual switching takes place on the following
\ :c:func:`percpu_ref_reinit`\ .

This function normally doesn't block and can be called from any context
but it may block if \ ``ref``\  is in the process of switching to atomic mode
by \ :c:func:`percpu_ref_switch_atomic`\ .

.. _`percpu_ref_kill_and_confirm`:

percpu_ref_kill_and_confirm
===========================

.. c:function:: void percpu_ref_kill_and_confirm(struct percpu_ref *ref, percpu_ref_func_t *confirm_kill)

    drop the initial ref and schedule confirmation

    :param struct percpu_ref \*ref:
        percpu_ref to kill

    :param percpu_ref_func_t \*confirm_kill:
        optional confirmation callback

.. _`percpu_ref_kill_and_confirm.description`:

Description
-----------

Equivalent to \ :c:func:`percpu_ref_kill`\  but also schedules kill confirmation if
\ ``confirm_kill``\  is not NULL.  \ ``confirm_kill``\ , which may not block, will be
called after \ ``ref``\  is seen as dead from all CPUs at which point all
further invocations of \ :c:func:`percpu_ref_tryget_live`\  will fail.  See
\ :c:func:`percpu_ref_tryget_live`\  for details.

This function normally doesn't block and can be called from any context
but it may block if \ ``confirm_kill``\  is specified and \ ``ref``\  is in the
process of switching to atomic mode by \ :c:func:`percpu_ref_switch_atomic`\ .

Due to the way percpu_ref is implemented, \ ``confirm_switch``\  will be called
after at least one full sched RCU grace period has passed but this is an
implementation detail and must not be depended upon.

.. _`percpu_ref_reinit`:

percpu_ref_reinit
=================

.. c:function:: void percpu_ref_reinit(struct percpu_ref *ref)

    re-initialize a percpu refcount

    :param struct percpu_ref \*ref:
        perpcu_ref to re-initialize

.. _`percpu_ref_reinit.description`:

Description
-----------

Re-initialize \ ``ref``\  so that it's in the same state as when it finished
\ :c:func:`percpu_ref_init`\  ignoring \ ``PERCPU_REF_INIT_DEAD``\ .  \ ``ref``\  must have been
initialized successfully and reached 0 but not exited.

Note that percpu_ref_tryget[_live]() are safe to perform on \ ``ref``\  while
this function is in progress.

.. This file was automatic generated / don't edit.

