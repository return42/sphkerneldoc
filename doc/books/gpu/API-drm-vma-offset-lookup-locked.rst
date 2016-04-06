
.. _API-drm-vma-offset-lookup-locked:

============================
drm_vma_offset_lookup_locked
============================

*man drm_vma_offset_lookup_locked(9)*

*4.6.0-rc1*

Find node in offset space


Synopsis
========

.. c:function:: struct drm_vma_offset_node ⋆ drm_vma_offset_lookup_locked( struct drm_vma_offset_manager * mgr, unsigned long start, unsigned long pages )

Arguments
=========

``mgr``
    Manager object

``start``
    Start address for object (page-based)

``pages``
    Size of object (page-based)


Description
===========

Find a node given a start address and object size. This returns the _best_ match for the given node. That is, ``start`` may point somewhere into a valid region and the given node
will be returned, as long as the node spans the whole requested area (given the size in number of pages as ``pages``).

Note that before lookup the vma offset manager lookup lock must be acquired with ``drm_vma_offset_lock_lookup``. See there for an example. This can then be used to implement weakly
referenced lookups using ``kref_get_unless_zero``.


Example
=======


.. code-block:: c

           drm_vma_offset_lock_lookup(mgr);
           node = drm_vma_offset_lookup_locked(mgr);
           if (node)
               kref_get_unless_zero(container_of(node, sth, entr));
           drm_vma_offset_unlock_lookup(mgr);


RETURNS
=======

Returns NULL if no suitable node can be found. Otherwise, the best match is returned. It's the caller's responsibility to make sure the node doesn't get destroyed before the caller
can access it.
