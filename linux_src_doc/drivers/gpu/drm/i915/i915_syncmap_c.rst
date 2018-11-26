.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_syncmap.c

.. _`i915_syncmap_init`:

i915_syncmap_init
=================

.. c:function:: void i915_syncmap_init(struct i915_syncmap **root)

    - initialise the #i915_syncmap

    :param root:
        pointer to the #i915_syncmap
    :type root: struct i915_syncmap \*\*

.. _`i915_syncmap_is_later`:

i915_syncmap_is_later
=====================

.. c:function:: bool i915_syncmap_is_later(struct i915_syncmap **root, u64 id, u32 seqno)

    - compare against the last know sync point

    :param root:
        pointer to the #i915_syncmap
    :type root: struct i915_syncmap \*\*

    :param id:
        the context id (other timeline) we are synchronising to
    :type id: u64

    :param seqno:
        the sequence number along the other timeline
    :type seqno: u32

.. _`i915_syncmap_is_later.description`:

Description
-----------

If we have already synchronised this \ ``root``\  timeline with another (@id) then
we can omit any repeated or earlier synchronisation requests. If the two
timelines are already coupled, we can also omit the dependency between the
two as that is already known via the timeline.

Returns true if the two timelines are already synchronised wrt to \ ``seqno``\ ,
false if not and the synchronisation must be emitted.

.. _`i915_syncmap_set`:

i915_syncmap_set
================

.. c:function:: int i915_syncmap_set(struct i915_syncmap **root, u64 id, u32 seqno)

    - mark the most recent syncpoint between contexts

    :param root:
        pointer to the #i915_syncmap
    :type root: struct i915_syncmap \*\*

    :param id:
        the context id (other timeline) we have synchronised to
    :type id: u64

    :param seqno:
        the sequence number along the other timeline
    :type seqno: u32

.. _`i915_syncmap_set.description`:

Description
-----------

When we synchronise this \ ``root``\  timeline with another (@id), we also know
that we have synchronized with all previous seqno along that timeline. If
we then have a request to synchronise with the same seqno or older, we can
omit it, see \ :c:func:`i915_syncmap_is_later`\ 

Returns 0 on success, or a negative error code.

.. _`i915_syncmap_free`:

i915_syncmap_free
=================

.. c:function:: void i915_syncmap_free(struct i915_syncmap **root)

    - free all memory associated with the syncmap

    :param root:
        pointer to the #i915_syncmap
    :type root: struct i915_syncmap \*\*

.. _`i915_syncmap_free.description`:

Description
-----------

Either when the timeline is to be freed and we no longer need the sync
point tracking, or when the fences are all known to be signaled and the
sync point tracking is redundant, we can free the #i915_syncmap to recover
its allocations.

Will reinitialise the \ ``root``\  pointer so that the #i915_syncmap is ready for
reuse.

.. This file was automatic generated / don't edit.

