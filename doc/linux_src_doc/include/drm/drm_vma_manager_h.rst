.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_vma_manager.h

.. _`drm_vma_offset_exact_lookup_locked`:

drm_vma_offset_exact_lookup_locked
==================================

.. c:function:: struct drm_vma_offset_node *drm_vma_offset_exact_lookup_locked(struct drm_vma_offset_manager *mgr, unsigned long start, unsigned long pages)

    Look up node by exact address

    :param struct drm_vma_offset_manager \*mgr:
        Manager object

    :param unsigned long start:
        Start address (page-based, not byte-based)

    :param unsigned long pages:
        Size of object (page-based)

.. _`drm_vma_offset_exact_lookup_locked.description`:

Description
-----------

Same as \ :c:func:`drm_vma_offset_lookup_locked`\  but does not allow any offset into the node.
It only returns the exact object with the given start address.

.. _`drm_vma_offset_exact_lookup_locked.return`:

Return
------

Node at exact start address \ ``start``\ .

.. _`drm_vma_offset_lock_lookup`:

drm_vma_offset_lock_lookup
==========================

.. c:function:: void drm_vma_offset_lock_lookup(struct drm_vma_offset_manager *mgr)

    Lock lookup for extended private use

    :param struct drm_vma_offset_manager \*mgr:
        Manager object

.. _`drm_vma_offset_lock_lookup.description`:

Description
-----------

Lock VMA manager for extended lookups. Only locked VMA function calls
are allowed while holding this lock. All other contexts are blocked from VMA
until the lock is released via \ :c:func:`drm_vma_offset_unlock_lookup`\ .

Use this if you need to take a reference to the objects returned by
\ :c:func:`drm_vma_offset_lookup_locked`\  before releasing this lock again.

This lock must not be used for anything else than extended lookups. You must
not call any other VMA helpers while holding this lock.

.. _`drm_vma_offset_lock_lookup.note`:

Note
----

You're in atomic-context while holding this lock!

.. _`drm_vma_offset_unlock_lookup`:

drm_vma_offset_unlock_lookup
============================

.. c:function:: void drm_vma_offset_unlock_lookup(struct drm_vma_offset_manager *mgr)

    Unlock lookup for extended private use

    :param struct drm_vma_offset_manager \*mgr:
        Manager object

.. _`drm_vma_offset_unlock_lookup.description`:

Description
-----------

Release lookup-lock. See \ :c:func:`drm_vma_offset_lock_lookup`\  for more information.

.. _`drm_vma_node_reset`:

drm_vma_node_reset
==================

.. c:function:: void drm_vma_node_reset(struct drm_vma_offset_node *node)

    Initialize or reset node object

    :param struct drm_vma_offset_node \*node:
        Node to initialize or reset

.. _`drm_vma_node_reset.description`:

Description
-----------

Reset a node to its initial state. This must be called before using it with
any VMA offset manager.

This must not be called on an already allocated node, or you will leak
memory.

.. _`drm_vma_node_start`:

drm_vma_node_start
==================

.. c:function:: unsigned long drm_vma_node_start(struct drm_vma_offset_node *node)

    Return start address for page-based addressing

    :param struct drm_vma_offset_node \*node:
        Node to inspect

.. _`drm_vma_node_start.description`:

Description
-----------

Return the start address of the given node. This can be used as offset into
the linear VM space that is provided by the VMA offset manager. Note that
this can only be used for page-based addressing. If you need a proper offset
for user-space mappings, you must apply "<< PAGE_SHIFT" or use the
\ :c:func:`drm_vma_node_offset_addr`\  helper instead.

.. _`drm_vma_node_start.return`:

Return
------

Start address of \ ``node``\  for page-based addressing. 0 if the node does not
have an offset allocated.

.. _`drm_vma_node_size`:

drm_vma_node_size
=================

.. c:function:: unsigned long drm_vma_node_size(struct drm_vma_offset_node *node)

    Return size (page-based)

    :param struct drm_vma_offset_node \*node:
        Node to inspect

.. _`drm_vma_node_size.description`:

Description
-----------

Return the size as number of pages for the given node. This is the same size
that was passed to \ :c:func:`drm_vma_offset_add`\ . If no offset is allocated for the
node, this is 0.

.. _`drm_vma_node_size.return`:

Return
------

Size of \ ``node``\  as number of pages. 0 if the node does not have an offset
allocated.

.. _`drm_vma_node_offset_addr`:

drm_vma_node_offset_addr
========================

.. c:function:: __u64 drm_vma_node_offset_addr(struct drm_vma_offset_node *node)

    Return sanitized offset for user-space mmaps

    :param struct drm_vma_offset_node \*node:
        Linked offset node

.. _`drm_vma_node_offset_addr.description`:

Description
-----------

Same as \ :c:func:`drm_vma_node_start`\  but returns the address as a valid offset that
can be used for user-space mappings during \ :c:func:`mmap`\ .
This must not be called on unlinked nodes.

.. _`drm_vma_node_offset_addr.return`:

Return
------

Offset of \ ``node``\  for byte-based addressing. 0 if the node does not have an
object allocated.

.. _`drm_vma_node_unmap`:

drm_vma_node_unmap
==================

.. c:function:: void drm_vma_node_unmap(struct drm_vma_offset_node *node, struct address_space *file_mapping)

    Unmap offset node

    :param struct drm_vma_offset_node \*node:
        Offset node

    :param struct address_space \*file_mapping:
        Address space to unmap \ ``node``\  from

.. _`drm_vma_node_unmap.description`:

Description
-----------

Unmap all userspace mappings for a given offset node. The mappings must be
associated with the \ ``file_mapping``\  address-space. If no offset exists
nothing is done.

This call is unlocked. The caller must guarantee that \ :c:func:`drm_vma_offset_remove`\ 
is not called on this node concurrently.

.. _`drm_vma_node_verify_access`:

drm_vma_node_verify_access
==========================

.. c:function:: int drm_vma_node_verify_access(struct drm_vma_offset_node *node, struct file *filp)

    Access verification helper for TTM

    :param struct drm_vma_offset_node \*node:
        Offset node

    :param struct file \*filp:
        Open-file

.. _`drm_vma_node_verify_access.description`:

Description
-----------

This checks whether \ ``filp``\  is granted access to \ ``node``\ . It is the same as
\ :c:func:`drm_vma_node_is_allowed`\  but suitable as drop-in helper for TTM
\ :c:func:`verify_access`\  callbacks.

.. _`drm_vma_node_verify_access.return`:

Return
------

0 if access is granted, -EACCES otherwise.

.. This file was automatic generated / don't edit.

