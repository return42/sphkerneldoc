.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_vma_manager.c

.. _`drm_vma_offset_manager_init`:

drm_vma_offset_manager_init
===========================

.. c:function:: void drm_vma_offset_manager_init(struct drm_vma_offset_manager *mgr, unsigned long page_offset, unsigned long size)

    Initialize new offset-manager

    :param struct drm_vma_offset_manager \*mgr:
        Manager object

    :param unsigned long page_offset:
        Offset of available memory area (page-based)

    :param unsigned long size:
        Size of available address space range (page-based)

.. _`drm_vma_offset_manager_init.description`:

Description
-----------

Initialize a new offset-manager. The offset and area size available for the
manager are given as \ ``page_offset``\  and \ ``size``\ . Both are interpreted as
page-numbers, not bytes.

Adding/removing nodes from the manager is locked internally and protected
against concurrent access. However, node allocation and destruction is left
for the caller. While calling into the vma-manager, a given node must
always be guaranteed to be referenced.

.. _`drm_vma_offset_manager_destroy`:

drm_vma_offset_manager_destroy
==============================

.. c:function:: void drm_vma_offset_manager_destroy(struct drm_vma_offset_manager *mgr)

    Destroy offset manager

    :param struct drm_vma_offset_manager \*mgr:
        Manager object

.. _`drm_vma_offset_manager_destroy.description`:

Description
-----------

Destroy an object manager which was previously created via
\ :c:func:`drm_vma_offset_manager_init`\ . The caller must remove all allocated nodes
before destroying the manager. Otherwise, drm_mm will refuse to free the
requested resources.

The manager must not be accessed after this function is called.

.. _`drm_vma_offset_lookup_locked`:

drm_vma_offset_lookup_locked
============================

.. c:function:: struct drm_vma_offset_node *drm_vma_offset_lookup_locked(struct drm_vma_offset_manager *mgr, unsigned long start, unsigned long pages)

    Find node in offset space

    :param struct drm_vma_offset_manager \*mgr:
        Manager object

    :param unsigned long start:
        Start address for object (page-based)

    :param unsigned long pages:
        Size of object (page-based)

.. _`drm_vma_offset_lookup_locked.description`:

Description
-----------

Find a node given a start address and object size. This returns the \_best\_
match for the given node. That is, \ ``start``\  may point somewhere into a valid
region and the given node will be returned, as long as the node spans the
whole requested area (given the size in number of pages as \ ``pages``\ ).

Note that before lookup the vma offset manager lookup lock must be acquired
with \ :c:func:`drm_vma_offset_lock_lookup`\ . See there for an example. This can then be
used to implement weakly referenced lookups using \ :c:func:`kref_get_unless_zero`\ .

.. _`drm_vma_offset_lookup_locked.example`:

Example
-------

.. code-block:: c


    ::

        drm_vma_offset_lock_lookup(mgr);
        node = drm_vma_offset_lookup_locked(mgr);
        if (node)
            kref_get_unless_zero(container_of(node, sth, entr));
        drm_vma_offset_unlock_lookup(mgr);


.. _`drm_vma_offset_lookup_locked.return`:

Return
------

Returns NULL if no suitable node can be found. Otherwise, the best match
is returned. It's the caller's responsibility to make sure the node doesn't
get destroyed before the caller can access it.

.. _`drm_vma_offset_add`:

drm_vma_offset_add
==================

.. c:function:: int drm_vma_offset_add(struct drm_vma_offset_manager *mgr, struct drm_vma_offset_node *node, unsigned long pages)

    Add offset node to manager

    :param struct drm_vma_offset_manager \*mgr:
        Manager object

    :param struct drm_vma_offset_node \*node:
        Node to be added

    :param unsigned long pages:
        Allocation size visible to user-space (in number of pages)

.. _`drm_vma_offset_add.description`:

Description
-----------

Add a node to the offset-manager. If the node was already added, this does
nothing and return 0. \ ``pages``\  is the size of the object given in number of
pages.
After this call succeeds, you can access the offset of the node until it
is removed again.

If this call fails, it is safe to retry the operation or call
\ :c:func:`drm_vma_offset_remove`\ , anyway. However, no cleanup is required in that
case.

\ ``pages``\  is not required to be the same size as the underlying memory object
that you want to map. It only limits the size that user-space can map into
their address space.

.. _`drm_vma_offset_add.return`:

Return
------

0 on success, negative error code on failure.

.. _`drm_vma_offset_remove`:

drm_vma_offset_remove
=====================

.. c:function:: void drm_vma_offset_remove(struct drm_vma_offset_manager *mgr, struct drm_vma_offset_node *node)

    Remove offset node from manager

    :param struct drm_vma_offset_manager \*mgr:
        Manager object

    :param struct drm_vma_offset_node \*node:
        Node to be removed

.. _`drm_vma_offset_remove.description`:

Description
-----------

Remove a node from the offset manager. If the node wasn't added before, this
does nothing. After this call returns, the offset and size will be 0 until a
new offset is allocated via \ :c:func:`drm_vma_offset_add`\  again. Helper functions like
\ :c:func:`drm_vma_node_start`\  and \ :c:func:`drm_vma_node_offset_addr`\  will return 0 if no
offset is allocated.

.. _`drm_vma_node_allow`:

drm_vma_node_allow
==================

.. c:function:: int drm_vma_node_allow(struct drm_vma_offset_node *node, struct file *filp)

    Add open-file to list of allowed users

    :param struct drm_vma_offset_node \*node:
        Node to modify

    :param struct file \*filp:
        Open file to add

.. _`drm_vma_node_allow.description`:

Description
-----------

Add \ ``filp``\  to the list of allowed open-files for this node. If \ ``filp``\  is
already on this list, the ref-count is incremented.

The list of allowed-users is preserved across \ :c:func:`drm_vma_offset_add`\  and
\ :c:func:`drm_vma_offset_remove`\  calls. You may even call it if the node is currently
not added to any offset-manager.

You must remove all open-files the same number of times as you added them
before destroying the node. Otherwise, you will leak memory.

This is locked against concurrent access internally.

.. _`drm_vma_node_allow.return`:

Return
------

0 on success, negative error code on internal failure (out-of-mem)

.. _`drm_vma_node_revoke`:

drm_vma_node_revoke
===================

.. c:function:: void drm_vma_node_revoke(struct drm_vma_offset_node *node, struct file *filp)

    Remove open-file from list of allowed users

    :param struct drm_vma_offset_node \*node:
        Node to modify

    :param struct file \*filp:
        Open file to remove

.. _`drm_vma_node_revoke.description`:

Description
-----------

Decrement the ref-count of \ ``filp``\  in the list of allowed open-files on \ ``node``\ .
If the ref-count drops to zero, remove \ ``filp``\  from the list. You must call
this once for every \ :c:func:`drm_vma_node_allow`\  on \ ``filp``\ .

This is locked against concurrent access internally.

If \ ``filp``\  is not on the list, nothing is done.

.. _`drm_vma_node_is_allowed`:

drm_vma_node_is_allowed
=======================

.. c:function:: bool drm_vma_node_is_allowed(struct drm_vma_offset_node *node, struct file *filp)

    Check whether an open-file is granted access

    :param struct drm_vma_offset_node \*node:
        Node to check

    :param struct file \*filp:
        Open-file to check for

.. _`drm_vma_node_is_allowed.description`:

Description
-----------

Search the list in \ ``node``\  whether \ ``filp``\  is currently on the list of allowed
open-files (see \ :c:func:`drm_vma_node_allow`\ ).

This is locked against concurrent access internally.

.. _`drm_vma_node_is_allowed.return`:

Return
------

true iff \ ``filp``\  is on the list

.. This file was automatic generated / don't edit.

