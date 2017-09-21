.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/cgroup/cpuset.c

.. _`cpuset_for_each_child`:

cpuset_for_each_child
=====================

.. c:function::  cpuset_for_each_child( child_cs,  pos_css,  parent_cs)

    traverse online children of a cpuset

    :param  child_cs:
        loop cursor pointing to the current child

    :param  pos_css:
        used for iteration

    :param  parent_cs:
        target cpuset to walk children of

.. _`cpuset_for_each_child.description`:

Description
-----------

Walk \ ``child_cs``\  through the online children of \ ``parent_cs``\ .  Must be used
with RCU read locked.

.. _`cpuset_for_each_descendant_pre`:

cpuset_for_each_descendant_pre
==============================

.. c:function::  cpuset_for_each_descendant_pre( des_cs,  pos_css,  root_cs)

    pre-order walk of a cpuset's descendants

    :param  des_cs:
        loop cursor pointing to the current descendant

    :param  pos_css:
        used for iteration

    :param  root_cs:
        target cpuset to walk ancestor of

.. _`cpuset_for_each_descendant_pre.description`:

Description
-----------

Walk \ ``des_cs``\  through the online descendants of \ ``root_cs``\ .  Must be used
with RCU read locked.  The caller may modify \ ``pos_css``\  by calling
\ :c:func:`css_rightmost_descendant`\  to skip subtree.  \ ``root_cs``\  is included in the
iteration and the first node to be visited.

.. _`alloc_trial_cpuset`:

alloc_trial_cpuset
==================

.. c:function:: struct cpuset *alloc_trial_cpuset(struct cpuset *cs)

    allocate a trial cpuset

    :param struct cpuset \*cs:
        the cpuset that the trial cpuset duplicates

.. _`free_trial_cpuset`:

free_trial_cpuset
=================

.. c:function:: void free_trial_cpuset(struct cpuset *trial)

    free the trial cpuset

    :param struct cpuset \*trial:
        the trial cpuset to be freed

.. _`update_tasks_cpumask`:

update_tasks_cpumask
====================

.. c:function:: void update_tasks_cpumask(struct cpuset *cs)

    Update the cpumasks of tasks in the cpuset.

    :param struct cpuset \*cs:
        the cpuset in which each task's cpus_allowed mask needs to be changed

.. _`update_tasks_cpumask.description`:

Description
-----------

Iterate through each task of \ ``cs``\  updating its cpus_allowed to the
effective cpuset's.  As this function is called with cpuset_mutex held,
cpuset membership stays stable.

.. _`update_cpumask`:

update_cpumask
==============

.. c:function:: int update_cpumask(struct cpuset *cs, struct cpuset *trialcs, const char *buf)

    update the cpus_allowed mask of a cpuset and all tasks in it

    :param struct cpuset \*cs:
        the cpuset to consider

    :param struct cpuset \*trialcs:
        trial cpuset

    :param const char \*buf:
        buffer of cpu numbers written to this cpuset

.. _`update_tasks_nodemask`:

update_tasks_nodemask
=====================

.. c:function:: void update_tasks_nodemask(struct cpuset *cs)

    Update the nodemasks of tasks in the cpuset.

    :param struct cpuset \*cs:
        the cpuset in which each task's mems_allowed mask needs to be changed

.. _`update_tasks_nodemask.description`:

Description
-----------

Iterate through each task of \ ``cs``\  updating its mems_allowed to the
effective cpuset's.  As this function is called with cpuset_mutex held,
cpuset membership stays stable.

.. _`update_tasks_flags`:

update_tasks_flags
==================

.. c:function:: void update_tasks_flags(struct cpuset *cs)

    update the spread flags of tasks in the cpuset.

    :param struct cpuset \*cs:
        the cpuset in which each task's spread flags needs to be changed

.. _`update_tasks_flags.description`:

Description
-----------

Iterate through each task of \ ``cs``\  updating its spread flags.  As this
function is called with cpuset_mutex held, cpuset membership stays
stable.

.. _`cpuset_init`:

cpuset_init
===========

.. c:function:: int cpuset_init( void)

    initialize cpusets at system boot

    :param  void:
        no arguments

.. _`cpuset_init.description`:

Description
-----------

Initialize top_cpuset and the cpuset internal file system,

.. _`cpuset_hotplug_update_tasks`:

cpuset_hotplug_update_tasks
===========================

.. c:function:: void cpuset_hotplug_update_tasks(struct cpuset *cs)

    update tasks in a cpuset for hotunplug

    :param struct cpuset \*cs:
        cpuset in interest

.. _`cpuset_hotplug_update_tasks.description`:

Description
-----------

Compare \ ``cs``\ 's cpu and mem masks against top_cpuset and if some have gone
offline, update \ ``cs``\  accordingly.  If \ ``cs``\  ends up with no CPU or memory,
all its tasks are moved to the nearest ancestor with both resources.

.. _`cpuset_hotplug_workfn`:

cpuset_hotplug_workfn
=====================

.. c:function:: void cpuset_hotplug_workfn(struct work_struct *work)

    handle CPU/memory hotunplug for a cpuset

    :param struct work_struct \*work:
        *undescribed*

.. _`cpuset_hotplug_workfn.description`:

Description
-----------

This function is called after either CPU or memory configuration has
changed and updates cpuset accordingly.  The top_cpuset is always
synchronized to cpu_active_mask and N_MEMORY, which is necessary in
order to make cpusets transparent (of no affect) on systems that are
actively using CPU hotplug but making no active use of cpusets.

Non-root cpusets are only affected by offlining.  If any CPUs or memory
nodes have been taken down, \ :c:func:`cpuset_hotplug_update_tasks`\  is invoked on
all descendants.

Note that CPU offlining during suspend is ignored.  We don't modify
cpusets across suspend/resume cycles at all.

.. _`cpuset_init_smp`:

cpuset_init_smp
===============

.. c:function:: void cpuset_init_smp( void)

    initialize cpus_allowed

    :param  void:
        no arguments

.. _`cpuset_init_smp.description`:

Description
-----------

Finish top cpuset after cpu, node maps are initialized

.. _`cpuset_cpus_allowed`:

cpuset_cpus_allowed
===================

.. c:function:: void cpuset_cpus_allowed(struct task_struct *tsk, struct cpumask *pmask)

    return cpus_allowed mask from a tasks cpuset.

    :param struct task_struct \*tsk:
        pointer to task_struct from which to obtain cpuset->cpus_allowed.

    :param struct cpumask \*pmask:
        pointer to struct cpumask variable to receive cpus_allowed set.

.. _`cpuset_cpus_allowed.description`:

Description
-----------

Returns the cpumask_var_t cpus_allowed of the cpuset
attached to the specified \ ``tsk``\ .  Guaranteed to return some non-empty
subset of cpu_online_mask, even if this means going outside the
tasks cpuset.

.. _`cpuset_mems_allowed`:

cpuset_mems_allowed
===================

.. c:function:: nodemask_t cpuset_mems_allowed(struct task_struct *tsk)

    return mems_allowed mask from a tasks cpuset.

    :param struct task_struct \*tsk:
        pointer to task_struct from which to obtain cpuset->mems_allowed.

.. _`cpuset_mems_allowed.description`:

Description
-----------

Returns the nodemask_t mems_allowed of the cpuset
attached to the specified \ ``tsk``\ .  Guaranteed to return some non-empty
subset of node_states[N_MEMORY], even if this means going outside the
tasks cpuset.

.. _`cpuset_nodemask_valid_mems_allowed`:

cpuset_nodemask_valid_mems_allowed
==================================

.. c:function:: int cpuset_nodemask_valid_mems_allowed(nodemask_t *nodemask)

    check nodemask vs. curremt mems_allowed

    :param nodemask_t \*nodemask:
        the nodemask to be checked

.. _`cpuset_nodemask_valid_mems_allowed.description`:

Description
-----------

Are any of the nodes in the nodemask allowed in current->mems_allowed?

.. _`__cpuset_node_allowed`:

__cpuset_node_allowed
=====================

.. c:function:: bool __cpuset_node_allowed(int node, gfp_t gfp_mask)

    Can we allocate on a memory node?

    :param int node:
        is this an allowed node?

    :param gfp_t gfp_mask:
        memory allocation flags

.. _`__cpuset_node_allowed.description`:

Description
-----------

If we're in interrupt, yes, we can always allocate.  If \ ``node``\  is set in
current's mems_allowed, yes.  If it's not a \__GFP_HARDWALL request and this
node is set in the nearest hardwalled cpuset ancestor to current's cpuset,
yes.  If current has access to memory reserves as an oom victim, yes.
Otherwise, no.

GFP_USER allocations are marked with the \__GFP_HARDWALL bit,
and do not allow allocations outside the current tasks cpuset
unless the task has been OOM killed.
GFP_KERNEL allocations are not so marked, so can escape to the
nearest enclosing hardwalled ancestor cpuset.

Scanning up parent cpusets requires callback_lock.  The
\__alloc_pages() routine only calls here with \__GFP_HARDWALL bit
\_not\_ set if it's a GFP_KERNEL allocation, and all nodes in the
current tasks mems_allowed came up empty on the first pass over
the zonelist.  So only GFP_KERNEL allocations, if all nodes in the
cpuset are short of memory, might require taking the callback_lock.

The first call here from mm/page_alloc:get_page_from_freelist()
has \__GFP_HARDWALL set in gfp_mask, enforcing hardwall cpusets,
so no allocation on a node outside the cpuset is allowed (unless
in interrupt, of course).

The second pass through \ :c:func:`get_page_from_freelist`\  doesn't even call
here for GFP_ATOMIC calls.  For those calls, the \__alloc_pages()
variable 'wait' is not set, and the bit ALLOC_CPUSET is not set
in alloc_flags.  That logic and the checks below have the combined

.. _`__cpuset_node_allowed.affect-that`:

affect that
-----------

in_interrupt - any node ok (current task context irrelevant)
GFP_ATOMIC   - any node ok
tsk_is_oom_victim   - any node ok
GFP_KERNEL   - any node in enclosing hardwalled cpuset ok
GFP_USER     - only nodes in current tasks mems allowed ok.

.. _`cpuset_spread_node`:

cpuset_spread_node
==================

.. c:function:: int cpuset_spread_node(int *rotor)

    On which node to begin search for a file page \ :c:func:`cpuset_slab_spread_node`\  - On which node to begin search for a slab page

    :param int \*rotor:
        *undescribed*

.. _`cpuset_spread_node.description`:

Description
-----------

If a task is marked PF_SPREAD_PAGE or PF_SPREAD_SLAB (as for
tasks in a cpuset with is_spread_page or is_spread_slab set),
and if the memory allocation used \ :c:func:`cpuset_mem_spread_node`\ 
to determine on which node to start looking, as it will for
certain page cache or slab cache pages such as used for file
system buffers and inode caches, then instead of starting on the
local node to look for a free page, rather spread the starting
node around the tasks mems_allowed nodes.

We don't have to worry about the returned node being offline
because "it can't happen", and even if it did, it would be ok.

The routines calling \ :c:func:`guarantee_online_mems`\  are careful to
only set nodes in task->mems_allowed that are online.  So it
should not be possible for the following code to return an
offline node.  But if it did, that would be ok, as this routine
is not returning the node where the allocation must be, only
the node where the search should start.  The zonelist passed to
\__alloc_pages() will include all nodes.  If the slab allocator
is passed an offline node, it will fall back to the local node.
See \ :c:func:`kmem_cache_alloc_node`\ .

.. _`cpuset_mems_allowed_intersects`:

cpuset_mems_allowed_intersects
==============================

.. c:function:: int cpuset_mems_allowed_intersects(const struct task_struct *tsk1, const struct task_struct *tsk2)

    Does \ ``tsk1``\ 's mems_allowed intersect \ ``tsk2``\ 's?

    :param const struct task_struct \*tsk1:
        pointer to task_struct of some task.

    :param const struct task_struct \*tsk2:
        pointer to task_struct of some other task.

.. _`cpuset_mems_allowed_intersects.description`:

Description
-----------

Return true if \ ``tsk1``\ 's mems_allowed intersects the
mems_allowed of \ ``tsk2``\ .  Used by the OOM killer to determine if
one of the task's memory usage might impact the memory available
to the other.

.. _`cpuset_print_current_mems_allowed`:

cpuset_print_current_mems_allowed
=================================

.. c:function:: void cpuset_print_current_mems_allowed( void)

    prints current's cpuset and mems_allowed

    :param  void:
        no arguments

.. _`cpuset_print_current_mems_allowed.description`:

Description
-----------

Prints current's name, cpuset name, and cached copy of its
mems_allowed to the kernel log.

.. _`__cpuset_memory_pressure_bump`:

__cpuset_memory_pressure_bump
=============================

.. c:function:: void __cpuset_memory_pressure_bump( void)

    keep stats of per-cpuset reclaims.

    :param  void:
        no arguments

.. _`__cpuset_memory_pressure_bump.description`:

Description
-----------

Keep a running average of the rate of synchronous (direct)
page reclaim efforts initiated by tasks in each cpuset.

This represents the rate at which some task in the cpuset
ran low on memory on all nodes it was allowed to use, and
had to enter the kernels page reclaim code in an effort to
create more free memory by tossing clean pages or swapping
or writing dirty pages.

Display to user space in the per-cpuset read-only file
"memory_pressure".  Value displayed is an integer
representing the recent rate of entry into the synchronous
(direct) page reclaim by any task attached to the cpuset.

.. This file was automatic generated / don't edit.

