.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/cpu/intel_rdt_rdtgroup.c

.. _`closid_allocated`:

closid_allocated
================

.. c:function:: bool closid_allocated(unsigned int closid)

    test if provided closid is in use

    :param closid:
        closid to be tested
    :type closid: unsigned int

.. _`closid_allocated.return`:

Return
------

true if \ ``closid``\  is currently associated with a resource group,
false if \ ``closid``\  is free

.. _`rdtgroup_mode_by_closid`:

rdtgroup_mode_by_closid
=======================

.. c:function:: enum rdtgrp_mode rdtgroup_mode_by_closid(int closid)

    Return mode of resource group with closid

    :param closid:
        closid if the resource group
    :type closid: int

.. _`rdtgroup_mode_by_closid.description`:

Description
-----------

Each resource group is associated with a \ ``closid``\ . Here the mode
of a resource group can be queried by searching for it using its closid.

.. _`rdtgroup_mode_by_closid.return`:

Return
------

mode as \ :c:type:`enum rdtgrp_mode <rdtgrp_mode>`\  of resource group with closid \ ``closid``\ 

.. _`rdtgroup_mode_str`:

rdtgroup_mode_str
=================

.. c:function:: const char *rdtgroup_mode_str(enum rdtgrp_mode mode)

    Return the string representation of mode

    :param mode:
        the resource group mode as \ :c:type:`enum rdtgroup_mode <rdtgroup_mode>`\ 
    :type mode: enum rdtgrp_mode

.. _`rdtgroup_mode_str.return`:

Return
------

string representation of valid mode, "unknown" otherwise

.. _`rdtgroup_tasks_assigned`:

rdtgroup_tasks_assigned
=======================

.. c:function:: int rdtgroup_tasks_assigned(struct rdtgroup *r)

    Test if tasks have been assigned to resource group

    :param r:
        Resource group
    :type r: struct rdtgroup \*

.. _`rdtgroup_tasks_assigned.return`:

Return
------

1 if tasks have been assigned to \ ``r``\ , 0 otherwise

.. _`rdt_bit_usage_show`:

rdt_bit_usage_show
==================

.. c:function:: int rdt_bit_usage_show(struct kernfs_open_file *of, struct seq_file *seq, void *v)

    Display current usage of resources

    :param of:
        *undescribed*
    :type of: struct kernfs_open_file \*

    :param seq:
        *undescribed*
    :type seq: struct seq_file \*

    :param v:
        *undescribed*
    :type v: void \*

.. _`rdt_bit_usage_show.description`:

Description
-----------

A domain is a shared resource that can now be allocated differently. Here
we display the current regions of the domain as an annotated bitmask.
For each domain of this resource its allocation bitmask

.. _`rdt_bit_usage_show.is-annotated-as-below-to-indicate-the-current-usage-of-the-corresponding-bit`:

is annotated as below to indicate the current usage of the corresponding bit
----------------------------------------------------------------------------

0 - currently unused
X - currently available for sharing and used by software and hardware
H - currently used by hardware only but available for software use
S - currently used and shareable by software only
E - currently used exclusively by one resource group
P - currently pseudo-locked by one resource group

.. _`rdt_cdp_peer_get`:

rdt_cdp_peer_get
================

.. c:function:: int rdt_cdp_peer_get(struct rdt_resource *r, struct rdt_domain *d, struct rdt_resource **r_cdp, struct rdt_domain **d_cdp)

    Retrieve CDP peer if it exists

    :param r:
        RDT resource to which RDT domain \ ``d``\  belongs
    :type r: struct rdt_resource \*

    :param d:
        Cache instance for which a CDP peer is requested
    :type d: struct rdt_domain \*

    :param r_cdp:
        RDT resource that shares hardware with \ ``r``\  (RDT resource peer)
        Used to return the result.
    :type r_cdp: struct rdt_resource \*\*

    :param d_cdp:
        RDT domain that shares hardware with \ ``d``\  (RDT domain peer)
        Used to return the result.
    :type d_cdp: struct rdt_domain \*\*

.. _`rdt_cdp_peer_get.description`:

Description
-----------

RDT resources are managed independently and by extension the RDT domains
(RDT resource instances) are managed independently also. The Code and
Data Prioritization (CDP) RDT resources, while managed independently,
could refer to the same underlying hardware. For example,
RDT_RESOURCE_L2CODE and RDT_RESOURCE_L2DATA both refer to the L2 cache.

When provided with an RDT resource \ ``r``\  and an instance of that RDT
resource \ ``d``\  \ :c:func:`rdt_cdp_peer_get`\  will return if there is a peer RDT
resource and the exact instance that shares the same hardware.

.. _`rdt_cdp_peer_get.return`:

Return
------

0 if a CDP peer was found, <0 on error or if no CDP peer exists.
If a CDP peer was found, \ ``r_cdp``\  will point to the peer RDT resource
and \ ``d_cdp``\  will point to the peer RDT domain.

.. _`__rdtgroup_cbm_overlaps`:

\__rdtgroup_cbm_overlaps
========================

.. c:function:: bool __rdtgroup_cbm_overlaps(struct rdt_resource *r, struct rdt_domain *d, unsigned long cbm, int closid, bool exclusive)

    Does CBM for intended closid overlap with other

    :param r:
        Resource to which domain instance \ ``d``\  belongs.
    :type r: struct rdt_resource \*

    :param d:
        The domain instance for which \ ``closid``\  is being tested.
    :type d: struct rdt_domain \*

    :param cbm:
        Capacity bitmask being tested.
    :type cbm: unsigned long

    :param closid:
        Intended closid for \ ``cbm``\ .
    :type closid: int

    :param exclusive:
        Only check if overlaps with exclusive resource groups
    :type exclusive: bool

.. _`__rdtgroup_cbm_overlaps.description`:

Description
-----------

Checks if provided \ ``cbm``\  intended to be used for \ ``closid``\  on domain
\ ``d``\  overlaps with any other closids or other hardware usage associated
with this domain. If \ ``exclusive``\  is true then only overlaps with
resource groups in exclusive mode will be considered. If \ ``exclusive``\ 
is false then overlaps with any resource group or hardware entities
will be considered.

\ ``cbm``\  is unsigned long, even if only 32 bits are used, to make the
bitmap functions work correctly.

.. _`__rdtgroup_cbm_overlaps.return`:

Return
------

false if CBM does not overlap, true if it does.

.. _`rdtgroup_cbm_overlaps`:

rdtgroup_cbm_overlaps
=====================

.. c:function:: bool rdtgroup_cbm_overlaps(struct rdt_resource *r, struct rdt_domain *d, unsigned long cbm, int closid, bool exclusive)

    Does CBM overlap with other use of hardware

    :param r:
        Resource to which domain instance \ ``d``\  belongs.
    :type r: struct rdt_resource \*

    :param d:
        The domain instance for which \ ``closid``\  is being tested.
    :type d: struct rdt_domain \*

    :param cbm:
        Capacity bitmask being tested.
    :type cbm: unsigned long

    :param closid:
        Intended closid for \ ``cbm``\ .
    :type closid: int

    :param exclusive:
        Only check if overlaps with exclusive resource groups
    :type exclusive: bool

.. _`rdtgroup_cbm_overlaps.description`:

Description
-----------

Resources that can be allocated using a CBM can use the CBM to control
the overlap of these allocations. \ :c:func:`rdtgroup_cmb_overlaps`\  is the test
for overlap. Overlap test is not limited to the specific resource for
which the CBM is intended though - when dealing with CDP resources that
share the underlying hardware the overlap check should be performed on
the CDP resource sharing the hardware also.

Refer to description of \__rdtgroup_cbm_overlaps() for the details of the
overlap test.

.. _`rdtgroup_cbm_overlaps.return`:

Return
------

true if CBM overlap detected, false if there is no overlap

.. _`rdtgroup_mode_test_exclusive`:

rdtgroup_mode_test_exclusive
============================

.. c:function:: bool rdtgroup_mode_test_exclusive(struct rdtgroup *rdtgrp)

    Test if this resource group can be exclusive

    :param rdtgrp:
        *undescribed*
    :type rdtgrp: struct rdtgroup \*

.. _`rdtgroup_mode_test_exclusive.description`:

Description
-----------

An exclusive resource group implies that there should be no sharing of
its allocated resources. At the time this group is considered to be
exclusive this test can determine if its current schemata supports this
setting by testing for overlap with all other resource groups.

.. _`rdtgroup_mode_test_exclusive.return`:

Return
------

true if resource group can be exclusive, false if there is overlap
with allocations of other resource groups and thus this resource group
cannot be exclusive.

.. _`rdtgroup_mode_write`:

rdtgroup_mode_write
===================

.. c:function:: ssize_t rdtgroup_mode_write(struct kernfs_open_file *of, char *buf, size_t nbytes, loff_t off)

    Modify the resource group's mode

    :param of:
        *undescribed*
    :type of: struct kernfs_open_file \*

    :param buf:
        *undescribed*
    :type buf: char \*

    :param nbytes:
        *undescribed*
    :type nbytes: size_t

    :param off:
        *undescribed*
    :type off: loff_t

.. _`rdtgroup_cbm_to_size`:

rdtgroup_cbm_to_size
====================

.. c:function:: unsigned int rdtgroup_cbm_to_size(struct rdt_resource *r, struct rdt_domain *d, unsigned long cbm)

    Translate CBM to size in bytes

    :param r:
        RDT resource to which \ ``d``\  belongs.
    :type r: struct rdt_resource \*

    :param d:
        RDT domain instance.
    :type d: struct rdt_domain \*

    :param cbm:
        bitmask for which the size should be computed.
    :type cbm: unsigned long

.. _`rdtgroup_cbm_to_size.description`:

Description
-----------

The bitmask provided associated with the RDT domain instance \ ``d``\  will be
translated into how many bytes it represents. The size in bytes is
computed by first dividing the total cache size by the CBM length to
determine how many bytes each bit in the bitmask represents. The result
is multiplied with the number of bits set in the bitmask.

\ ``cbm``\  is unsigned long, even if only 32 bits are used to make the
bitmap functions work correctly.

.. _`rdtgroup_size_show`:

rdtgroup_size_show
==================

.. c:function:: int rdtgroup_size_show(struct kernfs_open_file *of, struct seq_file *s, void *v)

    Display size in bytes of allocated regions

    :param of:
        *undescribed*
    :type of: struct kernfs_open_file \*

    :param s:
        *undescribed*
    :type s: struct seq_file \*

    :param v:
        *undescribed*
    :type v: void \*

.. _`rdtgroup_size_show.description`:

Description
-----------

The "size" file mirrors the layout of the "schemata" file, printing the
size in bytes of each region instead of the capacity bitmask.

.. _`rdtgroup_kn_mode_restrict`:

rdtgroup_kn_mode_restrict
=========================

.. c:function:: int rdtgroup_kn_mode_restrict(struct rdtgroup *r, const char *name)

    Restrict user access to named resctrl file

    :param r:
        The resource group with which the file is associated.
    :type r: struct rdtgroup \*

    :param name:
        Name of the file
    :type name: const char \*

.. _`rdtgroup_kn_mode_restrict.description`:

Description
-----------

The permissions of named resctrl file, directory, or link are modified
to not allow read, write, or execute by any user.

.. _`rdtgroup_kn_mode_restrict.warning`:

WARNING
-------

This function is intended to communicate to the user that the
resctrl file has been locked down - that it is not relevant to the
particular state the system finds itself in. It should not be relied
on to protect from user access because after the file's permissions
are restricted the user can still change the permissions using chmod
from the command line.

.. _`rdtgroup_kn_mode_restrict.return`:

Return
------

0 on success, <0 on failure.

.. _`rdtgroup_kn_mode_restore`:

rdtgroup_kn_mode_restore
========================

.. c:function:: int rdtgroup_kn_mode_restore(struct rdtgroup *r, const char *name, umode_t mask)

    Restore user access to named resctrl file

    :param r:
        The resource group with which the file is associated.
    :type r: struct rdtgroup \*

    :param name:
        Name of the file
    :type name: const char \*

    :param mask:
        Mask of permissions that should be restored
    :type mask: umode_t

.. _`rdtgroup_kn_mode_restore.description`:

Description
-----------

Restore the permissions of the named file. If \ ``name``\  is a directory the
permissions of its parent will be used.

.. _`rdtgroup_kn_mode_restore.return`:

Return
------

0 on success, <0 on failure.

.. _`cbm_ensure_valid`:

cbm_ensure_valid
================

.. c:function:: void cbm_ensure_valid(u32 *_val, struct rdt_resource *r)

    Enforce validity on provided CBM

    :param _val:
        Candidate CBM
    :type _val: u32 \*

    :param r:
        RDT resource to which the CBM belongs
    :type r: struct rdt_resource \*

.. _`cbm_ensure_valid.description`:

Description
-----------

The provided CBM represents all cache portions available for use. This
may be represented by a bitmap that does not consist of contiguous ones
and thus be an invalid CBM.
Here the provided CBM is forced to be a valid CBM by only considering
the first set of contiguous bits as valid and clearing all bits.
The intention here is to provide a valid default CBM with which a new
resource group is initialized. The user can follow this with a
modification to the CBM if the default does not satisfy the
requirements.

.. _`rdtgroup_init_alloc`:

rdtgroup_init_alloc
===================

.. c:function:: int rdtgroup_init_alloc(struct rdtgroup *rdtgrp)

    Initialize the new RDT group's allocations

    :param rdtgrp:
        *undescribed*
    :type rdtgrp: struct rdtgroup \*

.. _`rdtgroup_init_alloc.description`:

Description
-----------

A new RDT group is being created on an allocation capable (CAT)
supporting system. Set this group up to start off with all usable
allocations. That is, all shareable and unused bits.

All-zero CBM is invalid. If there are no more shareable bits available
on any domain then the entire allocation will fail.

.. This file was automatic generated / don't edit.

