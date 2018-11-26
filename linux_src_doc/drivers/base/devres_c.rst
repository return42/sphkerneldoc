.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/devres.c

.. _`devres_alloc_node`:

devres_alloc_node
=================

.. c:function:: void *devres_alloc_node(dr_release_t release, size_t size, gfp_t gfp, int nid)

    Allocate device resource data

    :param release:
        Release function devres will be associated with
    :type release: dr_release_t

    :param size:
        Allocation size
    :type size: size_t

    :param gfp:
        Allocation flags
    :type gfp: gfp_t

    :param nid:
        NUMA node
    :type nid: int

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

    :param dev:
        Device to iterate resource from
    :type dev: struct device \*

    :param release:
        Look for resources associated with this release function
    :type release: dr_release_t

    :param match:
        Match function (optional)
    :type match: dr_match_t

    :param match_data:
        Data for the match function
    :type match_data: void \*

    :param void (\*fn)(struct device \*, void \*, void \*):
        Function to be called for each matched resource.

    :param data:
        Data for \ ``fn``\ , the 3rd parameter of \ ``fn``\ 
    :type data: void \*

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

    :param res:
        Pointer to devres data to free
    :type res: void \*

.. _`devres_free.description`:

Description
-----------

Free devres created with \ :c:func:`devres_alloc`\ .

.. _`devres_add`:

devres_add
==========

.. c:function:: void devres_add(struct device *dev, void *res)

    Register device resource

    :param dev:
        Device to add resource to
    :type dev: struct device \*

    :param res:
        Resource to register
    :type res: void \*

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

    :param dev:
        Device to lookup resource from
    :type dev: struct device \*

    :param release:
        Look for resources associated with this release function
    :type release: dr_release_t

    :param match:
        Match function (optional)
    :type match: dr_match_t

    :param match_data:
        Data for the match function
    :type match_data: void \*

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

    :param dev:
        Device to lookup or add devres for
    :type dev: struct device \*

    :param new_res:
        Pointer to new initialized devres to add if not found
    :type new_res: void \*

    :param match:
        Match function (optional)
    :type match: dr_match_t

    :param match_data:
        Data for the match function
    :type match_data: void \*

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

    :param dev:
        Device to find resource from
    :type dev: struct device \*

    :param release:
        Look for resources associated with this release function
    :type release: dr_release_t

    :param match:
        Match function (optional)
    :type match: dr_match_t

    :param match_data:
        Data for the match function
    :type match_data: void \*

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

    :param dev:
        Device to find resource from
    :type dev: struct device \*

    :param release:
        Look for resources associated with this release function
    :type release: dr_release_t

    :param match:
        Match function (optional)
    :type match: dr_match_t

    :param match_data:
        Data for the match function
    :type match_data: void \*

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

    :param dev:
        Device to find resource from
    :type dev: struct device \*

    :param release:
        Look for resources associated with this release function
    :type release: dr_release_t

    :param match:
        Match function (optional)
    :type match: dr_match_t

    :param match_data:
        Data for the match function
    :type match_data: void \*

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

    :param dev:
        Device to release resources for
    :type dev: struct device \*

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

    :param dev:
        Device to open devres group for
    :type dev: struct device \*

    :param id:
        Separator ID
    :type id: void \*

    :param gfp:
        Allocation flags
    :type gfp: gfp_t

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

    :param dev:
        Device to close devres group for
    :type dev: struct device \*

    :param id:
        ID of target group, can be NULL
    :type id: void \*

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

    :param dev:
        Device to remove group for
    :type dev: struct device \*

    :param id:
        ID of target group, can be NULL
    :type id: void \*

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

    :param dev:
        Device to release group for
    :type dev: struct device \*

    :param id:
        ID of target group, can be NULL
    :type id: void \*

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

    :param dev:
        Device that owns the action
    :type dev: struct device \*

    :param void (\*action)(void \*):
        Function that should be called

    :param data:
        Pointer to data passed to \ ``action``\  implementation
    :type data: void \*

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

    :param dev:
        Device that owns the action
    :type dev: struct device \*

    :param void (\*action)(void \*):
        Function implementing the action

    :param data:
        Pointer to data passed to \ ``action``\  implementation
    :type data: void \*

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

    :param dev:
        Device to allocate memory for
    :type dev: struct device \*

    :param size:
        Allocation size
    :type size: size_t

    :param gfp:
        Allocation gfp flags
    :type gfp: gfp_t

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

    :param dev:
        Device to allocate memory for
    :type dev: struct device \*

    :param s:
        the string to duplicate
    :type s: const char \*

    :param gfp:
        the GFP mask used in the \ :c:func:`devm_kmalloc`\  call when
        allocating memory
    :type gfp: gfp_t

.. _`devm_kstrdup.return`:

Return
------

Pointer to allocated string on success, NULL on failure.

.. _`devm_kstrdup_const`:

devm_kstrdup_const
==================

.. c:function:: const char *devm_kstrdup_const(struct device *dev, const char *s, gfp_t gfp)

    resource managed conditional string duplication

    :param dev:
        device for which to duplicate the string
    :type dev: struct device \*

    :param s:
        the string to duplicate
    :type s: const char \*

    :param gfp:
        the GFP mask used in the \ :c:func:`kmalloc`\  call when allocating memory
    :type gfp: gfp_t

.. _`devm_kstrdup_const.description`:

Description
-----------

Strings allocated by devm_kstrdup_const will be automatically freed when
the associated device is detached.

.. _`devm_kstrdup_const.return`:

Return
------

Source string if it is in .rodata section otherwise it falls back to
devm_kstrdup.

.. _`devm_kvasprintf`:

devm_kvasprintf
===============

.. c:function:: char *devm_kvasprintf(struct device *dev, gfp_t gfp, const char *fmt, va_list ap)

    Allocate resource managed space and format a string into that.

    :param dev:
        Device to allocate memory for
    :type dev: struct device \*

    :param gfp:
        the GFP mask used in the \ :c:func:`devm_kmalloc`\  call when
        allocating memory
    :type gfp: gfp_t

    :param fmt:
        The \ :c:func:`printf`\ -style format string
    :type fmt: const char \*

    :param ap:
        Arguments for the format string
    :type ap: va_list

.. _`devm_kvasprintf.return`:

Return
------

Pointer to allocated string on success, NULL on failure.

.. _`devm_kasprintf`:

devm_kasprintf
==============

.. c:function:: char *devm_kasprintf(struct device *dev, gfp_t gfp, const char *fmt,  ...)

    Allocate resource managed space and format a string into that.

    :param dev:
        Device to allocate memory for
    :type dev: struct device \*

    :param gfp:
        the GFP mask used in the \ :c:func:`devm_kmalloc`\  call when
        allocating memory
    :type gfp: gfp_t

    :param fmt:
        The \ :c:func:`printf`\ -style format string
    :type fmt: const char \*

    :param ellipsis ellipsis:
        Arguments for the format string

.. _`devm_kasprintf.return`:

Return
------

Pointer to allocated string on success, NULL on failure.

.. _`devm_kfree`:

devm_kfree
==========

.. c:function:: void devm_kfree(struct device *dev, const void *p)

    Resource-managed kfree

    :param dev:
        Device this memory belongs to
    :type dev: struct device \*

    :param p:
        Memory to free
    :type p: const void \*

.. _`devm_kfree.description`:

Description
-----------

Free memory allocated with \ :c:func:`devm_kmalloc`\ .

.. _`devm_kmemdup`:

devm_kmemdup
============

.. c:function:: void *devm_kmemdup(struct device *dev, const void *src, size_t len, gfp_t gfp)

    Resource-managed kmemdup

    :param dev:
        Device this memory belongs to
    :type dev: struct device \*

    :param src:
        Memory region to duplicate
    :type src: const void \*

    :param len:
        Memory region length
    :type len: size_t

    :param gfp:
        GFP mask to use
    :type gfp: gfp_t

.. _`devm_kmemdup.description`:

Description
-----------

Duplicate region of a memory using resource managed kmalloc

.. _`devm_get_free_pages`:

devm_get_free_pages
===================

.. c:function:: unsigned long devm_get_free_pages(struct device *dev, gfp_t gfp_mask, unsigned int order)

    Resource-managed __get_free_pages

    :param dev:
        Device to allocate memory for
    :type dev: struct device \*

    :param gfp_mask:
        Allocation gfp flags
    :type gfp_mask: gfp_t

    :param order:
        Allocation size is (1 << order) pages
    :type order: unsigned int

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

    :param dev:
        Device this memory belongs to
    :type dev: struct device \*

    :param addr:
        Memory to free
    :type addr: unsigned long

.. _`devm_free_pages.description`:

Description
-----------

Free memory allocated with \ :c:func:`devm_get_free_pages`\ . Unlike free_pages,
there is no need to supply the \ ``order``\ .

.. _`__devm_alloc_percpu`:

__devm_alloc_percpu
===================

.. c:function:: void __percpu *__devm_alloc_percpu(struct device *dev, size_t size, size_t align)

    Resource-managed alloc_percpu

    :param dev:
        Device to allocate per-cpu memory for
    :type dev: struct device \*

    :param size:
        Size of per-cpu memory to allocate
    :type size: size_t

    :param align:
        Alignment of per-cpu memory to allocate
    :type align: size_t

.. _`__devm_alloc_percpu.description`:

Description
-----------

Managed alloc_percpu. Per-cpu memory allocated with this function is
automatically freed on driver detach.

.. _`__devm_alloc_percpu.return`:

Return
------

Pointer to allocated memory on success, NULL on failure.

.. _`devm_free_percpu`:

devm_free_percpu
================

.. c:function:: void devm_free_percpu(struct device *dev, void __percpu *pdata)

    Resource-managed free_percpu

    :param dev:
        Device this memory belongs to
    :type dev: struct device \*

    :param pdata:
        Per-cpu memory to free
    :type pdata: void __percpu \*

.. _`devm_free_percpu.description`:

Description
-----------

Free memory allocated with \ :c:func:`devm_alloc_percpu`\ .

.. This file was automatic generated / don't edit.

