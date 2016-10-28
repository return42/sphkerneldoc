.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/resource.c

.. _`request_resource_conflict`:

request_resource_conflict
=========================

.. c:function:: struct resource *request_resource_conflict(struct resource *root, struct resource *new)

    request and reserve an I/O or memory resource

    :param struct resource \*root:
        root resource descriptor

    :param struct resource \*new:
        resource descriptor desired by caller

.. _`request_resource_conflict.description`:

Description
-----------

Returns 0 for success, conflict resource on error.

.. _`request_resource`:

request_resource
================

.. c:function:: int request_resource(struct resource *root, struct resource *new)

    request and reserve an I/O or memory resource

    :param struct resource \*root:
        root resource descriptor

    :param struct resource \*new:
        resource descriptor desired by caller

.. _`request_resource.description`:

Description
-----------

Returns 0 for success, negative error code on error.

.. _`release_resource`:

release_resource
================

.. c:function:: int release_resource(struct resource *old)

    release a previously reserved resource

    :param struct resource \*old:
        resource pointer

.. _`region_intersects`:

region_intersects
=================

.. c:function:: int region_intersects(resource_size_t start, size_t size, unsigned long flags, unsigned long desc)

    determine intersection of region with known resources

    :param resource_size_t start:
        region start address

    :param size_t size:
        size of region

    :param unsigned long flags:
        flags of resource (in iomem_resource)

    :param unsigned long desc:
        descriptor of resource (in iomem_resource) or IORES_DESC_NONE

.. _`region_intersects.description`:

Description
-----------

Check if the specified region partially overlaps or fully eclipses a
resource identified by \ ``flags``\  and \ ``desc``\  (optional with IORES_DESC_NONE).
Return REGION_DISJOINT if the region does not overlap \ ``flags``\ /\ ``desc``\ ,
return REGION_MIXED if the region overlaps \ ``flags``\ /\ ``desc``\  and another
resource, and return REGION_INTERSECTS if the region overlaps \ ``flags``\ /\ ``desc``\ 
and no other defined resource. Note that REGION_INTERSECTS is also
returned in the case when the specified region overlaps RAM and undefined
memory holes.

\ :c:func:`region_intersect`\  is used by memory remapping functions to ensure
the user is not remapping RAM and is a vast speed up over walking
through the resource table page by page.

.. _`reallocate_resource`:

reallocate_resource
===================

.. c:function:: int reallocate_resource(struct resource *root, struct resource *old, resource_size_t newsize, struct resource_constraint *constraint)

    allocate a slot in the resource tree given range & alignment. The resource will be relocated if the new size cannot be reallocated in the current location.

    :param struct resource \*root:
        root resource descriptor

    :param struct resource \*old:
        resource descriptor desired by caller

    :param resource_size_t newsize:
        new size of the resource descriptor

    :param struct resource_constraint \*constraint:
        the size and alignment constraints to be met.

.. _`allocate_resource`:

allocate_resource
=================

.. c:function:: int allocate_resource(struct resource *root, struct resource *new, resource_size_t size, resource_size_t min, resource_size_t max, resource_size_t align, resource_size_t (*alignf)(void *, const struct resource *, resource_size_t, resource_size_t), void *alignf_data)

    allocate empty slot in the resource tree given range & alignment. The resource will be reallocated with a new size if it was already allocated

    :param struct resource \*root:
        root resource descriptor

    :param struct resource \*new:
        resource descriptor desired by caller

    :param resource_size_t size:
        requested resource region size

    :param resource_size_t min:
        minimum boundary to allocate

    :param resource_size_t max:
        maximum boundary to allocate

    :param resource_size_t align:
        alignment requested, in bytes

    :param resource_size_t (\*alignf)(void \*, const struct resource \*, resource_size_t, resource_size_t):
        alignment function, optional, called if not NULL

    :param void \*alignf_data:
        arbitrary data to pass to the \ ``alignf``\  function

.. _`lookup_resource`:

lookup_resource
===============

.. c:function:: struct resource *lookup_resource(struct resource *root, resource_size_t start)

    find an existing resource by a resource start address

    :param struct resource \*root:
        root resource descriptor

    :param resource_size_t start:
        resource start address

.. _`lookup_resource.description`:

Description
-----------

Returns a pointer to the resource if found, NULL otherwise

.. _`insert_resource_conflict`:

insert_resource_conflict
========================

.. c:function:: struct resource *insert_resource_conflict(struct resource *parent, struct resource *new)

    Inserts resource in the resource tree

    :param struct resource \*parent:
        parent of the new resource

    :param struct resource \*new:
        new resource to insert

.. _`insert_resource_conflict.description`:

Description
-----------

Returns 0 on success, conflict resource if the resource can't be inserted.

This function is equivalent to request_resource_conflict when no conflict
happens. If a conflict happens, and the conflicting resources
entirely fit within the range of the new resource, then the new
resource is inserted and the conflicting resources become children of
the new resource.

This function is intended for producers of resources, such as FW modules
and bus drivers.

.. _`insert_resource`:

insert_resource
===============

.. c:function:: int insert_resource(struct resource *parent, struct resource *new)

    Inserts a resource in the resource tree

    :param struct resource \*parent:
        parent of the new resource

    :param struct resource \*new:
        new resource to insert

.. _`insert_resource.description`:

Description
-----------

Returns 0 on success, -EBUSY if the resource can't be inserted.

This function is intended for producers of resources, such as FW modules
and bus drivers.

.. _`insert_resource_expand_to_fit`:

insert_resource_expand_to_fit
=============================

.. c:function:: void insert_resource_expand_to_fit(struct resource *root, struct resource *new)

    Insert a resource into the resource tree

    :param struct resource \*root:
        root resource descriptor

    :param struct resource \*new:
        new resource to insert

.. _`insert_resource_expand_to_fit.description`:

Description
-----------

Insert a resource into the resource tree, possibly expanding it in order
to make it encompass any conflicting resources.

.. _`remove_resource`:

remove_resource
===============

.. c:function:: int remove_resource(struct resource *old)

    Remove a resource in the resource tree

    :param struct resource \*old:
        resource to remove

.. _`remove_resource.description`:

Description
-----------

Returns 0 on success, -EINVAL if the resource is not valid.

This function removes a resource previously inserted by \ :c:func:`insert_resource`\ 
or \ :c:func:`insert_resource_conflict`\ , and moves the children (if any) up to
where they were before.  \ :c:func:`insert_resource`\  and \ :c:func:`insert_resource_conflict`\ 
insert a new resource, and move any conflicting resources down to the
children of the new resource.

\ :c:func:`insert_resource`\ , \ :c:func:`insert_resource_conflict`\  and \ :c:func:`remove_resource`\  are
intended for producers of resources, such as FW modules and bus drivers.

.. _`adjust_resource`:

adjust_resource
===============

.. c:function:: int adjust_resource(struct resource *res, resource_size_t start, resource_size_t size)

    modify a resource's start and size

    :param struct resource \*res:
        resource to modify

    :param resource_size_t start:
        new start value

    :param resource_size_t size:
        new size

.. _`adjust_resource.description`:

Description
-----------

Given an existing resource, change its start and size to match the
arguments.  Returns 0 on success, -EBUSY if it can't fit.
Existing children of the resource are assumed to be immutable.

.. _`resource_alignment`:

resource_alignment
==================

.. c:function:: resource_size_t resource_alignment(struct resource *res)

    calculate resource's alignment

    :param struct resource \*res:
        resource pointer

.. _`resource_alignment.description`:

Description
-----------

Returns alignment on success, 0 (invalid alignment) on failure.

.. _`__request_region`:

__request_region
================

.. c:function:: struct resource *__request_region(struct resource *parent, resource_size_t start, resource_size_t n, const char *name, int flags)

    create a new busy resource region

    :param struct resource \*parent:
        parent resource descriptor

    :param resource_size_t start:
        resource start address

    :param resource_size_t n:
        resource region size

    :param const char \*name:
        reserving caller's ID string

    :param int flags:
        IO resource flags

.. _`__release_region`:

__release_region
================

.. c:function:: void __release_region(struct resource *parent, resource_size_t start, resource_size_t n)

    release a previously reserved resource region

    :param struct resource \*parent:
        parent resource descriptor

    :param resource_size_t start:
        resource start address

    :param resource_size_t n:
        resource region size

.. _`__release_region.description`:

Description
-----------

The described resource region must match a currently busy region.

.. _`release_mem_region_adjustable`:

release_mem_region_adjustable
=============================

.. c:function:: int release_mem_region_adjustable(struct resource *parent, resource_size_t start, resource_size_t size)

    release a previously reserved memory region

    :param struct resource \*parent:
        parent resource descriptor

    :param resource_size_t start:
        resource start address

    :param resource_size_t size:
        resource region size

.. _`release_mem_region_adjustable.description`:

Description
-----------

This interface is intended for memory hot-delete.  The requested region
is released from a currently busy memory resource.  The requested region
must either match exactly or fit into a single busy resource entry.  In
the latter case, the remaining resource is adjusted accordingly.
Existing children of the busy memory resource must be immutable in the
request.

.. _`release_mem_region_adjustable.note`:

Note
----

- Additional release conditions, such as overlapping region, can be
supported after they are confirmed as valid cases.
- When a busy memory resource gets split into two entries, the code
assumes that all children remain in the lower address entry for
simplicity.  Enhance this logic when necessary.

.. _`devm_request_resource`:

devm_request_resource
=====================

.. c:function:: int devm_request_resource(struct device *dev, struct resource *root, struct resource *new)

    request and reserve an I/O or memory resource

    :param struct device \*dev:
        device for which to request the resource

    :param struct resource \*root:
        root of the resource tree from which to request the resource

    :param struct resource \*new:
        descriptor of the resource to request

.. _`devm_request_resource.description`:

Description
-----------

This is a device-managed version of \ :c:func:`request_resource`\ . There is usually
no need to release resources requested by this function explicitly since
that will be taken care of when the device is unbound from its driver.
If for some reason the resource needs to be released explicitly, because
of ordering issues for example, drivers must call \ :c:func:`devm_release_resource`\ 
rather than the regular \ :c:func:`release_resource`\ .

When a conflict is detected between any existing resources and the newly
requested resource, an error message will be printed.

Returns 0 on success or a negative error code on failure.

.. _`devm_release_resource`:

devm_release_resource
=====================

.. c:function:: void devm_release_resource(struct device *dev, struct resource *new)

    release a previously requested resource

    :param struct device \*dev:
        device for which to release the resource

    :param struct resource \*new:
        descriptor of the resource to release

.. _`devm_release_resource.description`:

Description
-----------

Releases a resource previously requested using \ :c:func:`devm_request_resource`\ .

.. This file was automatic generated / don't edit.

