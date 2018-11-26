.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/cpu/intel_rdt_pseudo_lock.c

.. _`get_prefetch_disable_bits`:

get_prefetch_disable_bits
=========================

.. c:function:: u64 get_prefetch_disable_bits( void)

    prefetch disable bits of supported platforms

    :param void:
        no arguments
    :type void: 

.. _`get_prefetch_disable_bits.description`:

Description
-----------

Capture the list of platforms that have been validated to support
pseudo-locking. This includes testing to ensure pseudo-locked regions
with low cache miss rates can be created under variety of load conditions
as well as that these pseudo-locked regions can maintain their low cache
miss rates under variety of load conditions for significant lengths of time.

After a platform has been validated to support pseudo-locking its
hardware prefetch disable bits are included here as they are documented
in the SDM.

When adding a platform here also add support for its cache events to
\ :c:func:`measure_cycles_perf_fn`\ 

.. _`get_prefetch_disable_bits.return`:

Return
------

If platform is supported, the bits to disable hardware prefetchers, 0
if platform is not supported.

.. _`pseudo_lock_minor_get`:

pseudo_lock_minor_get
=====================

.. c:function:: int pseudo_lock_minor_get(unsigned int *minor)

    Obtain available minor number

    :param minor:
        Pointer to where new minor number will be stored
    :type minor: unsigned int \*

.. _`pseudo_lock_minor_get.description`:

Description
-----------

A bitmask is used to track available minor numbers. Here the next free
minor number is marked as unavailable and returned.

.. _`pseudo_lock_minor_get.return`:

Return
------

0 on success, <0 on failure.

.. _`pseudo_lock_minor_release`:

pseudo_lock_minor_release
=========================

.. c:function:: void pseudo_lock_minor_release(unsigned int minor)

    Return minor number to available

    :param minor:
        The minor number made available
    :type minor: unsigned int

.. _`region_find_by_minor`:

region_find_by_minor
====================

.. c:function:: struct rdtgroup *region_find_by_minor(unsigned int minor)

    Locate a pseudo-lock region by inode minor number

    :param minor:
        The minor number of the device representing pseudo-locked region
    :type minor: unsigned int

.. _`region_find_by_minor.description`:

Description
-----------

When the character device is accessed we need to determine which
pseudo-locked region it belongs to. This is done by matching the minor
number of the device to the pseudo-locked region it belongs.

Minor numbers are assigned at the time a pseudo-locked region is associated
with a cache instance.

.. _`region_find_by_minor.return`:

Return
------

On success return pointer to resource group owning the pseudo-locked
region, NULL on failure.

.. _`pseudo_lock_cstates_constrain`:

pseudo_lock_cstates_constrain
=============================

.. c:function:: int pseudo_lock_cstates_constrain(struct pseudo_lock_region *plr)

    Restrict cores from entering C6

    :param plr:
        *undescribed*
    :type plr: struct pseudo_lock_region \*

.. _`pseudo_lock_cstates_constrain.description`:

Description
-----------

To prevent the cache from being affected by power management entering
C6 has to be avoided. This is accomplished by requesting a latency
requirement lower than lowest C6 exit latency of all supported
platforms as found in the cpuidle state tables in the intel_idle driver.
At this time it is possible to do so with a single latency requirement
for all supported platforms.

Since Goldmont is supported, which is affected by X86_BUG_MONITOR,
the ACPI latencies need to be considered while keeping in mind that C2
may be set to map to deeper sleep states. In this case the latency
requirement needs to prevent entering C2 also.

.. _`pseudo_lock_region_clear`:

pseudo_lock_region_clear
========================

.. c:function:: void pseudo_lock_region_clear(struct pseudo_lock_region *plr)

    Reset pseudo-lock region data

    :param plr:
        pseudo-lock region
    :type plr: struct pseudo_lock_region \*

.. _`pseudo_lock_region_clear.description`:

Description
-----------

All content of the pseudo-locked region is reset - any memory allocated
freed.

.. _`pseudo_lock_region_clear.return`:

Return
------

void

.. _`pseudo_lock_region_init`:

pseudo_lock_region_init
=======================

.. c:function:: int pseudo_lock_region_init(struct pseudo_lock_region *plr)

    Initialize pseudo-lock region information

    :param plr:
        pseudo-lock region
    :type plr: struct pseudo_lock_region \*

.. _`pseudo_lock_region_init.description`:

Description
-----------

Called after user provided a schemata to be pseudo-locked. From the
schemata the \ :c:type:`struct pseudo_lock_region <pseudo_lock_region>`\  is on entry already initialized
with the resource, domain, and capacity bitmask. Here the information
required for pseudo-locking is deduced from this data and \ :c:type:`struct struct <struct>`\ 
pseudo_lock_region initialized further. This information includes:
- size in bytes of the region to be pseudo-locked
- cache line size to know the stride with which data needs to be accessed
to be pseudo-locked
- a cpu associated with the cache instance on which the pseudo-locking
flow can be executed

.. _`pseudo_lock_region_init.return`:

Return
------

0 on success, <0 on failure. Descriptive error will be written
to last_cmd_status buffer.

.. _`pseudo_lock_init`:

pseudo_lock_init
================

.. c:function:: int pseudo_lock_init(struct rdtgroup *rdtgrp)

    Initialize a pseudo-lock region

    :param rdtgrp:
        resource group to which new pseudo-locked region will belong
    :type rdtgrp: struct rdtgroup \*

.. _`pseudo_lock_init.description`:

Description
-----------

A pseudo-locked region is associated with a resource group. When this
association is created the pseudo-locked region is initialized. The
details of the pseudo-locked region are not known at this time so only
allocation is done and association established.

.. _`pseudo_lock_init.return`:

Return
------

0 on success, <0 on failure

.. _`pseudo_lock_region_alloc`:

pseudo_lock_region_alloc
========================

.. c:function:: int pseudo_lock_region_alloc(struct pseudo_lock_region *plr)

    Allocate kernel memory that will be pseudo-locked

    :param plr:
        pseudo-lock region
    :type plr: struct pseudo_lock_region \*

.. _`pseudo_lock_region_alloc.description`:

Description
-----------

Initialize the details required to set up the pseudo-locked region and
allocate the contiguous memory that will be pseudo-locked to the cache.

.. _`pseudo_lock_region_alloc.return`:

Return
------

0 on success, <0 on failure.  Descriptive error will be written
to last_cmd_status buffer.

.. _`pseudo_lock_free`:

pseudo_lock_free
================

.. c:function:: void pseudo_lock_free(struct rdtgroup *rdtgrp)

    Free a pseudo-locked region

    :param rdtgrp:
        resource group to which pseudo-locked region belonged
    :type rdtgrp: struct rdtgroup \*

.. _`pseudo_lock_free.description`:

Description
-----------

The pseudo-locked region's resources have already been released, or not
yet created at this point. Now it can be freed and disassociated from the
resource group.

.. _`pseudo_lock_free.return`:

Return
------

void

.. _`pseudo_lock_fn`:

pseudo_lock_fn
==============

.. c:function:: int pseudo_lock_fn(void *_rdtgrp)

    Load kernel memory into cache

    :param _rdtgrp:
        resource group to which pseudo-lock region belongs
    :type _rdtgrp: void \*

.. _`pseudo_lock_fn.description`:

Description
-----------

This is the core pseudo-locking flow.

First we ensure that the kernel memory cannot be found in the cache.
Then, while taking care that there will be as little interference as
possible, the memory to be loaded is accessed while core is running
with class of service set to the bitmask of the pseudo-locked region.
After this is complete no future CAT allocations will be allowed to
overlap with this bitmask.

Local register variables are utilized to ensure that the memory region
to be locked is the only memory access made during the critical locking
loop.

.. _`pseudo_lock_fn.return`:

Return
------

0. Waiter on waitqueue will be woken on completion.

.. _`rdtgroup_monitor_in_progress`:

rdtgroup_monitor_in_progress
============================

.. c:function:: int rdtgroup_monitor_in_progress(struct rdtgroup *rdtgrp)

    Test if monitoring in progress

    :param rdtgrp:
        *undescribed*
    :type rdtgrp: struct rdtgroup \*

.. _`rdtgroup_monitor_in_progress.return`:

Return
------

1 if monitor groups have been created for this resource
group, 0 otherwise.

.. _`rdtgroup_locksetup_user_restrict`:

rdtgroup_locksetup_user_restrict
================================

.. c:function:: int rdtgroup_locksetup_user_restrict(struct rdtgroup *rdtgrp)

    Restrict user access to group

    :param rdtgrp:
        resource group needing access restricted
    :type rdtgrp: struct rdtgroup \*

.. _`rdtgroup_locksetup_user_restrict.description`:

Description
-----------

A resource group used for cache pseudo-locking cannot have cpus or tasks
assigned to it. This is communicated to the user by restricting access
to all the files that can be used to make such changes.

Permissions restored with \ :c:func:`rdtgroup_locksetup_user_restore`\ 

.. _`rdtgroup_locksetup_user_restrict.return`:

Return
------

0 on success, <0 on failure. If a failure occurs during the
restriction of access an attempt will be made to restore permissions but
the state of the mode of these files will be uncertain when a failure
occurs.

.. _`rdtgroup_locksetup_user_restore`:

rdtgroup_locksetup_user_restore
===============================

.. c:function:: int rdtgroup_locksetup_user_restore(struct rdtgroup *rdtgrp)

    Restore user access to group

    :param rdtgrp:
        resource group needing access restored
    :type rdtgrp: struct rdtgroup \*

.. _`rdtgroup_locksetup_user_restore.description`:

Description
-----------

Restore all file access previously removed using
\ :c:func:`rdtgroup_locksetup_user_restrict`\ 

.. _`rdtgroup_locksetup_user_restore.return`:

Return
------

0 on success, <0 on failure.  If a failure occurs during the
restoration of access an attempt will be made to restrict permissions
again but the state of the mode of these files will be uncertain when
a failure occurs.

.. _`rdtgroup_locksetup_enter`:

rdtgroup_locksetup_enter
========================

.. c:function:: int rdtgroup_locksetup_enter(struct rdtgroup *rdtgrp)

    Resource group enters locksetup mode

    :param rdtgrp:
        resource group requested to enter locksetup mode
    :type rdtgrp: struct rdtgroup \*

.. _`rdtgroup_locksetup_enter.description`:

Description
-----------

A resource group enters locksetup mode to reflect that it would be used
to represent a pseudo-locked region and is in the process of being set
up to do so. A resource group used for a pseudo-locked region would
lose the closid associated with it so we cannot allow it to have any
tasks or cpus assigned nor permit tasks or cpus to be assigned in the
future. Monitoring of a pseudo-locked region is not allowed either.

The above and more restrictions on a pseudo-locked region are checked
for and enforced before the resource group enters the locksetup mode.

.. _`rdtgroup_locksetup_enter.return`:

Return
------

0 if the resource group successfully entered locksetup mode, <0
on failure. On failure the last_cmd_status buffer is updated with text to
communicate details of failure to the user.

.. _`rdtgroup_locksetup_exit`:

rdtgroup_locksetup_exit
=======================

.. c:function:: int rdtgroup_locksetup_exit(struct rdtgroup *rdtgrp)

    resource group exist locksetup mode

    :param rdtgrp:
        resource group
    :type rdtgrp: struct rdtgroup \*

.. _`rdtgroup_locksetup_exit.description`:

Description
-----------

When a resource group exits locksetup mode the earlier restrictions are
lifted.

.. _`rdtgroup_locksetup_exit.return`:

Return
------

0 on success, <0 on failure

.. _`rdtgroup_cbm_overlaps_pseudo_locked`:

rdtgroup_cbm_overlaps_pseudo_locked
===================================

.. c:function:: bool rdtgroup_cbm_overlaps_pseudo_locked(struct rdt_domain *d, unsigned long cbm)

    Test if CBM or portion is pseudo-locked

    :param d:
        RDT domain
    :type d: struct rdt_domain \*

    :param cbm:
        CBM to test
    :type cbm: unsigned long

.. _`rdtgroup_cbm_overlaps_pseudo_locked.description`:

Description
-----------

\ ``d``\  represents a cache instance and \ ``cbm``\  a capacity bitmask that is
considered for it. Determine if \ ``cbm``\  overlaps with any existing
pseudo-locked region on \ ``d``\ .

\ ``cbm``\  is unsigned long, even if only 32 bits are used, to make the
bitmap functions work correctly.

.. _`rdtgroup_cbm_overlaps_pseudo_locked.return`:

Return
------

true if \ ``cbm``\  overlaps with pseudo-locked region on \ ``d``\ , false
otherwise.

.. _`rdtgroup_pseudo_locked_in_hierarchy`:

rdtgroup_pseudo_locked_in_hierarchy
===================================

.. c:function:: bool rdtgroup_pseudo_locked_in_hierarchy(struct rdt_domain *d)

    Pseudo-locked region in cache hierarchy

    :param d:
        RDT domain under test
    :type d: struct rdt_domain \*

.. _`rdtgroup_pseudo_locked_in_hierarchy.description`:

Description
-----------

The setup of a pseudo-locked region affects all cache instances within
the hierarchy of the region. It is thus essential to know if any
pseudo-locked regions exist within a cache hierarchy to prevent any
attempts to create new pseudo-locked regions in the same hierarchy.

.. _`rdtgroup_pseudo_locked_in_hierarchy.return`:

Return
------

true if a pseudo-locked region exists in the hierarchy of \ ``d``\  or
if it is not possible to test due to memory allocation issue,
false otherwise.

.. _`measure_cycles_lat_fn`:

measure_cycles_lat_fn
=====================

.. c:function:: int measure_cycles_lat_fn(void *_plr)

    Measure cycle latency to read pseudo-locked memory

    :param _plr:
        pseudo-lock region to measure
    :type _plr: void \*

.. _`measure_cycles_lat_fn.description`:

Description
-----------

There is no deterministic way to test if a memory region is cached. One
way is to measure how long it takes to read the memory, the speed of
access is a good way to learn how close to the cpu the data was. Even
more, if the prefetcher is disabled and the memory is read at a stride
of half the cache line, then a cache miss will be easy to spot since the
read of the first half would be significantly slower than the read of
the second half.

.. _`measure_cycles_lat_fn.return`:

Return
------

0. Waiter on waitqueue will be woken on completion.

.. _`pseudo_lock_measure_cycles`:

pseudo_lock_measure_cycles
==========================

.. c:function:: int pseudo_lock_measure_cycles(struct rdtgroup *rdtgrp, int sel)

    Trigger latency measure to pseudo-locked region

    :param rdtgrp:
        *undescribed*
    :type rdtgrp: struct rdtgroup \*

    :param sel:
        *undescribed*
    :type sel: int

.. _`pseudo_lock_measure_cycles.description`:

Description
-----------

The measurement of latency to access a pseudo-locked region should be
done from a cpu that is associated with that pseudo-locked region.
Determine which cpu is associated with this region and start a thread on
that cpu to perform the measurement, wait for that thread to complete.

.. _`pseudo_lock_measure_cycles.return`:

Return
------

0 on success, <0 on failure

.. _`rdtgroup_pseudo_lock_create`:

rdtgroup_pseudo_lock_create
===========================

.. c:function:: int rdtgroup_pseudo_lock_create(struct rdtgroup *rdtgrp)

    Create a pseudo-locked region

    :param rdtgrp:
        resource group to which pseudo-lock region belongs
    :type rdtgrp: struct rdtgroup \*

.. _`rdtgroup_pseudo_lock_create.description`:

Description
-----------

Called when a resource group in the pseudo-locksetup mode receives a
valid schemata that should be pseudo-locked. Since the resource group is
in pseudo-locksetup mode the \ :c:type:`struct pseudo_lock_region <pseudo_lock_region>`\  has already been
allocated and initialized with the essential information. If a failure
occurs the resource group remains in the pseudo-locksetup mode with the
\ :c:type:`struct pseudo_lock_region <pseudo_lock_region>`\  associated with it, but cleared from all
information and ready for the user to re-attempt pseudo-locking by
writing the schemata again.

.. _`rdtgroup_pseudo_lock_create.return`:

Return
------

0 if the pseudo-locked region was successfully pseudo-locked, <0
on failure. Descriptive error will be written to last_cmd_status buffer.

.. _`rdtgroup_pseudo_lock_remove`:

rdtgroup_pseudo_lock_remove
===========================

.. c:function:: void rdtgroup_pseudo_lock_remove(struct rdtgroup *rdtgrp)

    Remove a pseudo-locked region

    :param rdtgrp:
        resource group to which the pseudo-locked region belongs
    :type rdtgrp: struct rdtgroup \*

.. _`rdtgroup_pseudo_lock_remove.description`:

Description
-----------

The removal of a pseudo-locked region can be initiated when the resource
group is removed from user space via a "rmdir" from userspace or the
unmount of the resctrl filesystem. On removal the resource group does
not go back to pseudo-locksetup mode before it is removed, instead it is
removed directly. There is thus assymmetry with the creation where the
\ :c:type:`struct pseudo_lock_region <pseudo_lock_region>`\  is removed here while it was not created in
\ :c:func:`rdtgroup_pseudo_lock_create`\ .

.. _`rdtgroup_pseudo_lock_remove.return`:

Return
------

void

.. This file was automatic generated / don't edit.

