.. -*- coding: utf-8; mode: rst -*-

==========
i915_drv.h
==========


.. _`intel_context`:

struct intel_context
====================

.. c:type:: intel_context

    as the name implies, represents a context.


.. _`intel_context.definition`:

Definition
----------

.. code-block:: c

  struct intel_context {
    struct kref ref;
    int user_handle;
    uint8_t remap_slice;
    int flags;
    struct drm_i915_file_private * file_priv;
    struct i915_ctx_hang_stats hang_stats;
    struct i915_hw_ppgtt * ppgtt;
    struct list_head link;
  };


.. _`intel_context.members`:

Members
-------

:``ref``:
    reference count.

:``user_handle``:
    userspace tracking identity for this context.

:``remap_slice``:
    l3 row remapping information.

:``flags``:
    context specific flags:

:``file_priv``:
    filp associated with this context (NULL for global default
    context).

:``hang_stats``:
    information about the role of this context in possible GPU
    hangs.

:``ppgtt``:
    virtual memory space used by this context.

:``link``:
    link in the global list of contexts.




.. _`intel_context.context_no_zeromap`:

CONTEXT_NO_ZEROMAP
------------------

do not allow mapping things to page 0.



.. _`intel_context.description`:

Description
-----------

Contexts are memory images used by the hardware to store copies of their
internal state.



.. _`i915_seqno_passed`:

i915_seqno_passed
=================

.. c:function:: bool i915_seqno_passed (uint32_t seq1, uint32_t seq2)

    :param uint32_t seq1:

        *undescribed*

    :param uint32_t seq2:

        *undescribed*

