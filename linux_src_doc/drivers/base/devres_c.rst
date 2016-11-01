.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/devres.c

.. _`devres_alloc_node`:

devres_alloc_node
=================

.. c:function:: void *devres_alloc_node(dr_release_t release, size_t size, gfp_t gfp, int nid)

    Allocate device resource data

    :param dr_release_t release:
        Release function devres will be associated with

    :param size_t size:
        Allocation size

    :param gfp_t gfp:
        Allocation flags

    :param int nid:
        NUMA node

.. _`devres_alloc_node.description`:

Description
-----------

Allocate devres of \ ``size``\  bytes.  The allocated area is zeroed, then
associated with \ ``release``\ .  The returned pointer can be passed to
other devres_*() functions.

.. _`devres_alloc_node.return`:

Return
------

Pointer to allocated devres on success, NULL on failure.

.. _`devres_for_each_res`:

devres_for_each_res
===================

.. c:function:: void devres_for_each_res(struct device *dev, dr_release_t release, dr_match_t match, void *match_data, void (*fn)(struct device *, void *, void *), void *data)

    Resource iterator

    :param struct device \*dev:
        Device to iterate resource from

    :param dr_release_t release:
        Look for resources associated with this release function

    :param dr_match_t match:
        Match function (optional)

    :param void \*match_data:
        Data for the match function

    :param void (\*fn)(struct device \*, void \*, void \*):
        Function to be called for each matched resource.

    :param void \*data:
        Data for \ ``fn``\ , the 3rd parameter of \ ``fn``\ 

.. _`devres_for_each_res.description`:

Description
-----------

Call \ ``fn``\  for each devres of \ ``dev``\  which is associated with \ ``release``\ 
and for which \ ``match``\  returns 1.

.. _`devres_for_each_res.return`:

Return
------

     void

.. _`devres_free`:

devres_free
===========

.. c:function:: void devres_free(void *res)

    Free device resource data

    :param void \*res:
        Pointer to devres data to free

.. _`devres_free.description`:

Description
-----------

Free devres created with \ :c:func:`devres_alloc`\ .

.. _`devres_add`:

devres_add
==========

.. c:function:: void devres_add(struct device *dev, void *res)

    Register device resource

    :param struct device \*dev:
        Device to add resource to

    :param void \*res:
        Resource to register

.. _`devres_add.description`:

Description
-----------

Register devres \ ``res``\  to \ ``dev``\ .  \ ``res``\  should have been allocated
using \ :c:func:`devres_alloc`\ .  On driver detach, the associated release
function will be invoked and devres will be freed automatically.

.. _`devres_find`:

devres_find
===========

.. c:function:: void *devres_find(struct device *dev, dr_release_t release, dr_match_t match, void *match_data)

    Find device resource

    :param struct device \*dev:
        Device to lookup resource from

    :param dr_release_t release:
        Look for resources associated with this release function

    :param dr_match_t match:
        Match function (optional)

    :param void \*match_data:
        Data for the match function

.. _`devres_find.description`:

Description
-----------

Find the latest devres of \ ``dev``\  which is associated with \ ``release``\ 
and for which \ ``match``\  returns 1.  If \ ``match``\  is NULL, it's considered
to match all.

.. _`devres_find.return`:

Return
------

Pointer to found devres, NULL if not found.

.. _`devres_get`:

devres_get
==========

.. c:function:: void *devres_get(struct device *dev, void *new_res, dr_match_t match, void *match_data)

    Find devres, if non-existent, add one atomically

    :param struct device \*dev:
        Device to lookup or add devres for

    :param void \*new_res:
        Pointer to new initialized devres to add if not found

    :param dr_match_t match:
        Match function (optional)

    :param void \*match_data:
        Data for the match function

.. _`devres_get.description`:

Description
-----------

Find the latest devres of \ ``dev``\  which has the same release function
as \ ``new_res``\  and for which \ ``match``\  return 1.  If found, \ ``new_res``\  is
freed; otherwise, \ ``new_res``\  is added atomically.

.. _`devres_get.return`:

Return
------

Pointer to found or added devres.

.. _`devres_remove`:

devres_remove
=============

.. c:function:: void *devres_remove(struct device *dev, dr_release_t release, dr_match_t match, void *match_data)

    Find a device resource and remove it

    :param struct device \*dev:
        Device to find resource from

    :param dr_release_t release:
        Look for resources associated with this release function

    :param dr_match_t match:
        Match function (optional)

    :param void \*match_data:
        Data for the match function

.. _`devres_remove.description`:

Description
-----------

Find the latest devres of \ ``dev``\  associated with \ ``release``\  and for
which \ ``match``\  returns 1.  If \ ``match``\  is NULL, it's considered to
match all.  If found, the resource is removed atomically and
returned.

.. _`devres_remove.return`:

Return
------

Pointer to removed devres on success, NULL if not found.

.. _`devres_destroy`:

devres_destroy
==============

.. c:function:: int devres_destroy(struct device *dev, dr_release_t release, dr_match_t match, void *match_data)

    Find a device resource and destroy it

    :param struct device \*dev:
        Device to find resource from

    :param dr_release_t release:
        Look for resources associated with this release function

    :param dr_match_t match:
        Match function (optional)

    :param void \*match_data:
        Data for the match function

.. _`devres_destroy.description`:

Description
-----------

Find the latest devres of \ ``dev``\  associated with \ ``release``\  and for
which \ ``match``\  returns 1.  If \ ``match``\  is NULL, it's considered to
match all.  If found, the resource is removed atomically and freed.

Note that the release function for the resource will not be called,
only the devres-allocated data will be freed.  The caller becomes
responsible for freeing any other data.

.. _`devres_destroy.return`:

Return
------

0 if devres is found and freed, -ENOENT if not found.

.. _`devres_release`:

devres_release
==============

.. c:function:: int devres_release(struct device *dev, dr_release_t release, dr_match_t match, void *match_data)

    Find a device resource and destroy it, calling release

    :param struct device \*dev:
        Device to find resource from

    :param dr_release_t release:
        Look for resources associated with this release function

    :param dr_match_t match:
        Match function (optional)

    :param void \*match_data:
        Data for the match function

.. _`devres_release.description`:

Description
-----------

Find the latest devres of \ ``dev``\  associated with \ ``release``\  and for
which \ ``match``\  returns 1.  If \ ``match``\  is NULL, it's considered to
match all.  If found, the resource is removed atomically, the
release function called and the resource freed.

.. _`devres_release.return`:

Return
------

0 if devres is found and freed, -ENOENT if not found.

.. _`devres_release_all`:

devres_release_all
==================

.. c:function:: int devres_release_all(struct device *dev)

    Release all managed resources

    :param struct device \*dev:
        Device to release resources for

.. _`devres_release_all.description`:

Description
-----------

Release all resources associated with \ ``dev``\ .  This function is
called on driver detach.

.. _`devres_open_group`:

devres_open_group
=================

.. c:function:: void *devres_open_group(struct device *dev, void *id, gfp_t gfp)

    Open a new devres group

    :param struct device \*dev:
        Device to open devres group for

    :param void \*id:
        Separator ID

    :param gfp_t gfp:
        Allocation flags

.. _`devres_open_group.description`:

Description
-----------

Open a new devres group for \ ``dev``\  with \ ``id``\ .  For \ ``id``\ , using a
pointer to an object which won't be used for another group is
recommended.  If \ ``id``\  is NULL, address-wise unique ID is created.

.. _`devres_open_group.return`:

Return
------

ID of the new group, NULL on failure.

.. _`devres_close_group`:

devres_close_group
==================

.. c:function:: void devres_close_group(struct device *dev, void *id)

    Close a devres group

    :param struct device \*dev:
        Device to close devres group for

    :param void \*id:
        ID of target group, can be NULL

.. _`devres_close_group.description`:

Description
-----------

Close the group identified by \ ``id``\ .  If \ ``id``\  is NULL, the latest open
group is selected.

.. _`devres_remove_group`:

devres_remove_group
===================

.. c:function:: void devres_remove_group(struct device *dev, void *id)

    Remove a devres group

    :param struct device \*dev:
        Device to remove group for

    :param void \*id:
        ID of target group, can be NULL

.. _`devres_remove_group.description`:

Description
-----------

Remove the group identified by \ ``id``\ .  If \ ``id``\  is NULL, the latest
open group is selected.  Note that removing a group doesn't affect
any other resources.

.. _`devres_release_group`:

devres_release_group
====================

.. c:function:: int devres_release_group(struct device *dev, void *id)

    Release resources in a devres group

    :param struct device \*dev:
        Device to release group for

    :param void \*id:
        ID of target group, can be NULL

.. _`devres_release_group.description`:

Description
-----------

Release all resources in the group identified by \ ``id``\ .  If \ ``id``\  is
NULL, the latest open group is selected.  The selected group and
groups properly nested inside the selected group are removed.

.. _`devres_release_group.return`:

Return
------

The number of released non-group resources.

.. _`devm_add_action`:

devm_add_action
===============

.. c:function:: int devm_add_action(struct device *dev, void (*action)(void *), void *data)

    add a custom action to list of managed resources

    :param struct device \*dev:
        Device that owns the action

    :param void (\*action)(void \*):
        Function that should be called

    :param void \*data:
        Pointer to data passed to \ ``action``\  implementation

.. _`devm_add_action.description`:

Description
-----------

This adds a custom action to the list of managed resources so that
it gets executed as part of standard resource unwinding.

.. _`devm_remove_action`:

devm_remove_action
==================

.. c:function:: void devm_remove_action(struct device *dev, void (*action)(void *), void *data)

    removes previously added custom action

    :param struct device \*dev:
        Device that owns the action

    :param void (\*action)(void \*):
        Function implementing the action

    :param void \*data:
        Pointer to data passed to \ ``action``\  implementation

.. _`devm_remove_action.description`:

Description
-----------

Removes instance of \ ``action``\  previously added by \ :c:func:`devm_add_action`\ .
Both action and data should match one of the existing entries.

.. _`devm_kmalloc`:

devm_kmalloc
============

.. c:function:: void *devm_kmalloc(struct device *dev, size_t size, gfp_t gfp)

    Resource-managed kmalloc

    :param struct device \*dev:
        Device to allocate memory for

    :param size_t size:
        Allocation size

    :param gfp_t gfp:
        Allocation gfp flags

.. _`devm_kmalloc.description`:

Description
-----------

Managed kmalloc.  Memory allocated with this function is
automatically freed on driver detach.  Like all other devres
resources, guaranteed alignment is unsigned long long.

.. _`devm_kmalloc.return`:

Return
------

Pointer to allocated memory on success, NULL on failure.

.. _`devm_kstrdup`:

devm_kstrdup
============

.. c:function:: char *devm_kstrdup(struct device *dev, const char *s, gfp_t gfp)

    Allocate resource managed space and copy an existing string into that.

    :param struct device \*dev:
        Device to allocate memory for

    :param const char \*s:
        the string to duplicate

    :param gfp_t gfp:
        the GFP mask used in the \ :c:func:`devm_kmalloc`\  call when
        allocating memory

.. _`devm_kstrdup.return`:

Return
------

Pointer to allocated string on success, NULL on failure.

.. _`devm_kvasprintf`:

devm_kvasprintf
===============

.. c:function:: char *devm_kvasprintf(struct device *dev, gfp_t gfp, const char *fmt, va_list ap)

    Allocate resource managed space and format a string into that.

    :param struct device \*dev:
        Device to allocate memory for

    :param gfp_t gfp:
        the GFP mask used in the \ :c:func:`devm_kmalloc`\  call when
        allocating memory

    :param const char \*fmt:
        The \ :c:func:`printf`\ -style format string

    :param va_list ap:
        Arguments for the format string

.. _`devm_kvasprintf.return`:

Return
------

Pointer to allocated string on success, NULL on failure.

.. _`devm_kasprintf`:

devm_kasprintf
==============

.. c:function:: char *devm_kasprintf(struct device *dev, gfp_t gfp, const char *fmt,  ...)

    Allocate resource managed space and format a string into that.

    :param struct device \*dev:
        Device to allocate memory for

    :param gfp_t gfp:
        the GFP mask used in the \ :c:func:`devm_kmalloc`\  call when
        allocating memory

    :param const char \*fmt:
        The \ :c:func:`printf`\ -style format string

    :param ... :
        Arguments for the format string

.. _`devm_kasprintf.return`:

Return
------

Pointer to allocated string on success, NULL on failure.

.. _`devm_kfree`:

devm_kfree
==========

.. c:function:: void devm_kfree(struct device *dev, void *p)

    Resource-managed kfree

    :param struct device \*dev:
        Device this memory belongs to

    :param void \*p:
        Memory to free

.. _`devm_kfree.description`:

Description
-----------

Free memory allocated with \ :c:func:`devm_kmalloc`\ .

.. _`devm_kmemdup`:

devm_kmemdup
============

.. c:function:: void *devm_kmemdup(struct device *dev, const void *src, size_t len, gfp_t gfp)

    Resource-managed kmemdup

    :param struct device \*dev:
        Device this memory belongs to

    :param const void \*src:
        Memory region to duplicate

    :param size_t len:
        Memory region length

    :param gfp_t gfp:
        GFP mask to use

.. _`devm_kmemdup.description`:

Description
-----------

Duplicate region of a memory using resource managed kmalloc

.. _`devm_get_free_pages`:

devm_get_free_pages
===================

.. c:function:: unsigned long devm_get_free_pages(struct device *dev, gfp_t gfp_mask, unsigned int order)

    Resource-managed __get_free_pages

    :param struct device \*dev:
        Device to allocate memory for

    :param gfp_t gfp_mask:
        Allocation gfp flags

    :param unsigned int order:
        Allocation size is (1 << order) pages

.. _`devm_get_free_pages.description`:

Description
-----------

Managed get_free_pages.  Memory allocated with this function is
automatically freed on driver detach.

.. _`devm_get_free_pages.return`:

Return
------

Address of allocated memory on success, 0 on failure.

.. _`devm_free_pages`:

devm_free_pages
===============

.. c:function:: void devm_free_pages(struct device *dev, unsigned long addr)

    Resource-managed free_pages

    :param struct device \*dev:
        Device this memory belongs to

    :param unsigned long addr:
        Memory to free

.. _`devm_free_pages.description`:

Description
-----------

Free memory allocated with \ :c:func:`devm_get_free_pages`\ . Unlike free_pages,
there is no need to supply the \ ``order``\ .

.. This file was automatic generated / don't edit.

