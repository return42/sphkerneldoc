.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpuidle/coupled.c

.. _`coupled-cpuidle-states`:

Coupled cpuidle states
======================

On some ARM SMP SoCs (OMAP4460, Tegra 2, and probably more), the
cpus cannot be independently powered down, either due to
sequencing restrictions (on Tegra 2, cpu 0 must be the last to
power down), or due to HW bugs (on OMAP4460, a cpu powering up
will corrupt the gic state unless the other cpu runs a work
around).  Each cpu has a power state that it can enter without
coordinating with the other cpu (usually Wait For Interrupt, or
WFI), and one or more "coupled" power states that affect blocks
shared between the cpus (L2 cache, interrupt controller, and
sometimes the whole SoC).  Entering a coupled power state must
be tightly controlled on both cpus.

This file implements a solution, where each cpu will wait in the
WFI state until all cpus are ready to enter a coupled state, at
which point the coupled state function will be called on all
cpus at approximately the same time.

Once all cpus are ready to enter idle, they are woken by an smp
cross call.  At this point, there is a chance that one of the
cpus will find work to do, and choose not to enter idle.  A
final pass is needed to guarantee that all cpus will call the
power state enter function at the same time.  During this pass,
each cpu will increment the ready counter, and continue once the
ready counter matches the number of online coupled cpus.  If any
cpu exits idle, the other cpus will decrement their counter and
retry.

requested_state stores the deepest coupled idle state each cpu
is ready for.  It is assumed that the states are indexed from
shallowest (highest power, lowest exit latency) to deepest
(lowest power, highest exit latency).  The requested_state
variable is not locked.  It is only written from the cpu that
it stores (or by the on/offlining cpu if that cpu is offline),
and only read after all the cpus are ready for the coupled idle
state are are no longer updating it.

Three atomic counters are used.  alive_count tracks the number
of cpus in the coupled set that are currently or soon will be
online.  waiting_count tracks the number of cpus that are in
the waiting loop, in the ready loop, or in the coupled idle state.
ready_count tracks the number of cpus that are in the ready loop
or in the coupled idle state.

To use coupled cpuidle states, a cpuidle driver must:

Set struct cpuidle_device.coupled_cpus to the mask of all
coupled cpus, usually the same as cpu_possible_mask if all cpus
are part of the same cluster.  The coupled_cpus mask must be
set in the struct cpuidle_device for each cpu.

Set struct cpuidle_device.safe_state to a state that is not a
coupled state.  This is usually WFI.

Set CPUIDLE_FLAG_COUPLED in struct cpuidle_state.flags for each
state that affects multiple cpus.

Provide a struct cpuidle_state.enter function for each state
that affects multiple cpus.  This function is guaranteed to be
called on all cpus at approximately the same time.  The driver
should ensure that the cpus all abort together if any cpu tries
to abort once the function is called.  The function should return
with interrupts still disabled.

.. _`cpuidle_coupled`:

struct cpuidle_coupled
======================

.. c:type:: struct cpuidle_coupled

    data for set of cpus that share a coupled idle state

.. _`cpuidle_coupled.definition`:

Definition
----------

.. code-block:: c

    struct cpuidle_coupled {
        cpumask_t coupled_cpus;
        int requested_state;
        atomic_t ready_waiting_counts;
        atomic_t abort_barrier;
        int online_count;
        int refcnt;
        int prevent;
    }

.. _`cpuidle_coupled.members`:

Members
-------

coupled_cpus
    mask of cpus that are part of the coupled set

requested_state
    array of requested states for cpus in the coupled set

ready_waiting_counts
    combined count of cpus  in ready or waiting loops

abort_barrier
    *undescribed*

online_count
    count of cpus that are online

refcnt
    reference count of cpuidle devices that are using this struct

prevent
    flag to prevent coupled idle while a cpu is hotplugging

.. _`cpuidle_coupled_parallel_barrier`:

cpuidle_coupled_parallel_barrier
================================

.. c:function:: void cpuidle_coupled_parallel_barrier(struct cpuidle_device *dev, atomic_t *a)

    synchronize all online coupled cpus

    :param struct cpuidle_device \*dev:
        cpuidle_device of the calling cpu

    :param atomic_t \*a:
        atomic variable to hold the barrier

.. _`cpuidle_coupled_parallel_barrier.description`:

Description
-----------

No caller to this function will return from this function until all online
cpus in the same coupled group have called this function.  Once any caller
has returned from this function, the barrier is immediately available for
reuse.

The atomic variable must be initialized to 0 before any cpu calls
this function, will be reset to 0 before any cpu returns from this function.

Must only be called from within a coupled idle state handler
(state.enter when state.flags has CPUIDLE_FLAG_COUPLED set).

Provides full smp barrier semantics before and after calling.

.. _`cpuidle_state_is_coupled`:

cpuidle_state_is_coupled
========================

.. c:function:: bool cpuidle_state_is_coupled(struct cpuidle_driver *drv, int state)

    check if a state is part of a coupled set

    :param struct cpuidle_driver \*drv:
        struct cpuidle_driver for the platform

    :param int state:
        index of the target state in drv->states

.. _`cpuidle_state_is_coupled.description`:

Description
-----------

Returns true if the target state is coupled with cpus besides this one

.. _`cpuidle_coupled_state_verify`:

cpuidle_coupled_state_verify
============================

.. c:function:: int cpuidle_coupled_state_verify(struct cpuidle_driver *drv)

    check if the coupled states are correctly set.

    :param struct cpuidle_driver \*drv:
        struct cpuidle_driver for the platform

.. _`cpuidle_coupled_state_verify.description`:

Description
-----------

Returns 0 for valid state values, a negative error code otherwise:
\* -EINVAL if any coupled state(safe_state_index) is wrongly set.

.. _`cpuidle_coupled_set_ready`:

cpuidle_coupled_set_ready
=========================

.. c:function:: void cpuidle_coupled_set_ready(struct cpuidle_coupled *coupled)

    mark a cpu as ready

    :param struct cpuidle_coupled \*coupled:
        the struct coupled that contains the current cpu

.. _`cpuidle_coupled_set_not_ready`:

cpuidle_coupled_set_not_ready
=============================

.. c:function:: int cpuidle_coupled_set_not_ready(struct cpuidle_coupled *coupled)

    mark a cpu as not ready

    :param struct cpuidle_coupled \*coupled:
        the struct coupled that contains the current cpu

.. _`cpuidle_coupled_set_not_ready.description`:

Description
-----------

Decrements the ready counter, unless the ready (and thus the waiting) counter
is equal to the number of online cpus.  Prevents a race where one cpu
decrements the waiting counter and then re-increments it just before another
cpu has decremented its ready counter, leading to the ready counter going
down from the number of online cpus without going through the coupled idle
state.

Returns 0 if the counter was decremented successfully, -EINVAL if the ready
counter was equal to the number of online cpus.

.. _`cpuidle_coupled_no_cpus_ready`:

cpuidle_coupled_no_cpus_ready
=============================

.. c:function:: int cpuidle_coupled_no_cpus_ready(struct cpuidle_coupled *coupled)

    check if no cpus in a coupled set are ready

    :param struct cpuidle_coupled \*coupled:
        the struct coupled that contains the current cpu

.. _`cpuidle_coupled_no_cpus_ready.description`:

Description
-----------

Returns true if all of the cpus in a coupled set are out of the ready loop.

.. _`cpuidle_coupled_cpus_ready`:

cpuidle_coupled_cpus_ready
==========================

.. c:function:: bool cpuidle_coupled_cpus_ready(struct cpuidle_coupled *coupled)

    check if all cpus in a coupled set are ready

    :param struct cpuidle_coupled \*coupled:
        the struct coupled that contains the current cpu

.. _`cpuidle_coupled_cpus_ready.description`:

Description
-----------

Returns true if all cpus coupled to this target state are in the ready loop

.. _`cpuidle_coupled_cpus_waiting`:

cpuidle_coupled_cpus_waiting
============================

.. c:function:: bool cpuidle_coupled_cpus_waiting(struct cpuidle_coupled *coupled)

    check if all cpus in a coupled set are waiting

    :param struct cpuidle_coupled \*coupled:
        the struct coupled that contains the current cpu

.. _`cpuidle_coupled_cpus_waiting.description`:

Description
-----------

Returns true if all cpus coupled to this target state are in the wait loop

.. _`cpuidle_coupled_no_cpus_waiting`:

cpuidle_coupled_no_cpus_waiting
===============================

.. c:function:: int cpuidle_coupled_no_cpus_waiting(struct cpuidle_coupled *coupled)

    check if no cpus in coupled set are waiting

    :param struct cpuidle_coupled \*coupled:
        the struct coupled that contains the current cpu

.. _`cpuidle_coupled_no_cpus_waiting.description`:

Description
-----------

Returns true if all of the cpus in a coupled set are out of the waiting loop.

.. _`cpuidle_coupled_get_state`:

cpuidle_coupled_get_state
=========================

.. c:function:: int cpuidle_coupled_get_state(struct cpuidle_device *dev, struct cpuidle_coupled *coupled)

    determine the deepest idle state

    :param struct cpuidle_device \*dev:
        struct cpuidle_device for this cpu

    :param struct cpuidle_coupled \*coupled:
        the struct coupled that contains the current cpu

.. _`cpuidle_coupled_get_state.description`:

Description
-----------

Returns the deepest idle state that all coupled cpus can enter

.. _`cpuidle_coupled_poke`:

cpuidle_coupled_poke
====================

.. c:function:: void cpuidle_coupled_poke(int cpu)

    wake up a cpu that may be waiting

    :param int cpu:
        target cpu

.. _`cpuidle_coupled_poke.description`:

Description
-----------

Ensures that the target cpu exits it's waiting idle state (if it is in it)
and will see updates to waiting_count before it re-enters it's waiting idle
state.

If cpuidle_coupled_poked_mask is already set for the target cpu, that cpu
either has or will soon have a pending IPI that will wake it out of idle,
or it is currently processing the IPI and is not in idle.

.. _`cpuidle_coupled_poke_others`:

cpuidle_coupled_poke_others
===========================

.. c:function:: void cpuidle_coupled_poke_others(int this_cpu, struct cpuidle_coupled *coupled)

    wake up all other cpus that may be waiting

    :param int this_cpu:
        *undescribed*

    :param struct cpuidle_coupled \*coupled:
        the struct coupled that contains the current cpu

.. _`cpuidle_coupled_poke_others.description`:

Description
-----------

Calls cpuidle_coupled_poke on all other online cpus.

.. _`cpuidle_coupled_set_waiting`:

cpuidle_coupled_set_waiting
===========================

.. c:function:: int cpuidle_coupled_set_waiting(int cpu, struct cpuidle_coupled *coupled, int next_state)

    mark this cpu as in the wait loop

    :param int cpu:
        *undescribed*

    :param struct cpuidle_coupled \*coupled:
        the struct coupled that contains the current cpu

    :param int next_state:
        the index in drv->states of the requested state for this cpu

.. _`cpuidle_coupled_set_waiting.description`:

Description
-----------

Updates the requested idle state for the specified cpuidle device.
Returns the number of waiting cpus.

.. _`cpuidle_coupled_set_not_waiting`:

cpuidle_coupled_set_not_waiting
===============================

.. c:function:: void cpuidle_coupled_set_not_waiting(int cpu, struct cpuidle_coupled *coupled)

    mark this cpu as leaving the wait loop

    :param int cpu:
        *undescribed*

    :param struct cpuidle_coupled \*coupled:
        the struct coupled that contains the current cpu

.. _`cpuidle_coupled_set_not_waiting.description`:

Description
-----------

Removes the requested idle state for the specified cpuidle device.

.. _`cpuidle_coupled_set_done`:

cpuidle_coupled_set_done
========================

.. c:function:: void cpuidle_coupled_set_done(int cpu, struct cpuidle_coupled *coupled)

    mark this cpu as leaving the ready loop

    :param int cpu:
        the current cpu

    :param struct cpuidle_coupled \*coupled:
        the struct coupled that contains the current cpu

.. _`cpuidle_coupled_set_done.description`:

Description
-----------

Marks this cpu as no longer in the ready and waiting loops.  Decrements
the waiting count first to prevent another cpu looping back in and seeing
this cpu as waiting just before it exits idle.

.. _`cpuidle_coupled_clear_pokes`:

cpuidle_coupled_clear_pokes
===========================

.. c:function:: int cpuidle_coupled_clear_pokes(int cpu)

    spin until the poke interrupt is processed \ ``cpu``\  - this cpu

    :param int cpu:
        *undescribed*

.. _`cpuidle_coupled_clear_pokes.description`:

Description
-----------

Turns on interrupts and spins until any outstanding poke interrupts have
been processed and the poke bit has been cleared.

Other interrupts may also be processed while interrupts are enabled, so
\ :c:func:`need_resched`\  must be tested after this function returns to make sure
the interrupt didn't schedule work that should take the cpu out of idle.

Returns 0 if no poke was pending, 1 if a poke was cleared.

.. _`cpuidle_enter_state_coupled`:

cpuidle_enter_state_coupled
===========================

.. c:function:: int cpuidle_enter_state_coupled(struct cpuidle_device *dev, struct cpuidle_driver *drv, int next_state)

    attempt to enter a state with coupled cpus

    :param struct cpuidle_device \*dev:
        struct cpuidle_device for the current cpu

    :param struct cpuidle_driver \*drv:
        struct cpuidle_driver for the platform

    :param int next_state:
        index of the requested state in drv->states

.. _`cpuidle_enter_state_coupled.description`:

Description
-----------

Coordinate with coupled cpus to enter the target state.  This is a two
stage process.  In the first stage, the cpus are operating independently,
and may call into cpuidle_enter_state_coupled at completely different times.
To save as much power as possible, the first cpus to call this function will
go to an intermediate state (the cpuidle_device's safe state), and wait for
all the other cpus to call this function.  Once all coupled cpus are idle,
the second stage will start.  Each coupled cpu will spin until all cpus have
guaranteed that they will call the target_state.

This function must be called with interrupts disabled.  It may enable
interrupts while preparing for idle, and it will always return with
interrupts enabled.

.. _`cpuidle_coupled_register_device`:

cpuidle_coupled_register_device
===============================

.. c:function:: int cpuidle_coupled_register_device(struct cpuidle_device *dev)

    register a coupled cpuidle device

    :param struct cpuidle_device \*dev:
        struct cpuidle_device for the current cpu

.. _`cpuidle_coupled_register_device.description`:

Description
-----------

Called from cpuidle_register_device to handle coupled idle init.  Finds the
cpuidle_coupled struct for this set of coupled cpus, or creates one if none
exists yet.

.. _`cpuidle_coupled_unregister_device`:

cpuidle_coupled_unregister_device
=================================

.. c:function:: void cpuidle_coupled_unregister_device(struct cpuidle_device *dev)

    unregister a coupled cpuidle device

    :param struct cpuidle_device \*dev:
        struct cpuidle_device for the current cpu

.. _`cpuidle_coupled_unregister_device.description`:

Description
-----------

Called from cpuidle_unregister_device to tear down coupled idle.  Removes the
cpu from the coupled idle set, and frees the cpuidle_coupled_info struct if
this was the last cpu in the set.

.. _`cpuidle_coupled_prevent_idle`:

cpuidle_coupled_prevent_idle
============================

.. c:function:: void cpuidle_coupled_prevent_idle(struct cpuidle_coupled *coupled)

    prevent cpus from entering a coupled state

    :param struct cpuidle_coupled \*coupled:
        the struct coupled that contains the cpu that is changing state

.. _`cpuidle_coupled_prevent_idle.description`:

Description
-----------

Disables coupled cpuidle on a coupled set of cpus.  Used to ensure that
cpu_online_mask doesn't change while cpus are coordinating coupled idle.

.. _`cpuidle_coupled_allow_idle`:

cpuidle_coupled_allow_idle
==========================

.. c:function:: void cpuidle_coupled_allow_idle(struct cpuidle_coupled *coupled)

    allows cpus to enter a coupled state

    :param struct cpuidle_coupled \*coupled:
        the struct coupled that contains the cpu that is changing state

.. _`cpuidle_coupled_allow_idle.description`:

Description
-----------

Enables coupled cpuidle on a coupled set of cpus.  Used to ensure that
cpu_online_mask doesn't change while cpus are coordinating coupled idle.

.. This file was automatic generated / don't edit.

