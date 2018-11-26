.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_validation.h

.. _`vmw_validation_context`:

struct vmw_validation_context
=============================

.. c:type:: struct vmw_validation_context

    Per command submission validation context

.. _`vmw_validation_context.definition`:

Definition
----------

.. code-block:: c

    struct vmw_validation_context {
        struct drm_open_hash *ht;
        struct list_head resource_list;
        struct list_head resource_ctx_list;
        struct list_head bo_list;
        struct list_head page_list;
        struct ww_acquire_ctx ticket;
        struct mutex *res_mutex;
        unsigned int merge_dups;
        unsigned int mem_size_left;
        u8 *page_address;
    }

.. _`vmw_validation_context.members`:

Members
-------

ht
    Hash table used to find resource- or buffer object duplicates

resource_list
    List head for resource validation metadata

resource_ctx_list
    List head for resource validation metadata for
    resources that need to be validated before those in \ ``resource_list``\ 

bo_list
    List head for buffer objects

page_list
    List of pages used by the memory allocator

ticket
    Ticked used for ww mutex locking

res_mutex
    Pointer to mutex used for resource reserving

merge_dups
    Whether to merge metadata for duplicate resources or
    buffer objects

mem_size_left
    Free memory left in the last page in \ ``page_list``\ 

page_address
    Kernel virtual address of the last page in \ ``page_list``\ 

.. _`declare_val_context`:

DECLARE_VAL_CONTEXT
===================

.. c:function::  DECLARE_VAL_CONTEXT( _name,  _ht,  _merge_dups)

    Declare a validation context with initialization

    :param _name:
        The name of the variable
    :type _name: 

    :param _ht:
        The hash table used to find dups or NULL if none
    :type _ht: 

    :param _merge_dups:
        Whether to merge duplicate buffer object- or resource
        entries. If set to true, ideally a hash table pointer should be supplied
        as well unless the number of resources and buffer objects per validation
        is known to be very small
    :type _merge_dups: 

.. _`vmw_validation_has_bos`:

vmw_validation_has_bos
======================

.. c:function:: bool vmw_validation_has_bos(struct vmw_validation_context *ctx)

    return whether the validation context has any buffer objects registered.

    :param ctx:
        The validation context
    :type ctx: struct vmw_validation_context \*

.. _`vmw_validation_has_bos.return`:

Return
------

Whether any buffer objects are registered

.. _`vmw_validation_set_ht`:

vmw_validation_set_ht
=====================

.. c:function:: void vmw_validation_set_ht(struct vmw_validation_context *ctx, struct drm_open_hash *ht)

    Register a hash table for duplicate finding

    :param ctx:
        The validation context
    :type ctx: struct vmw_validation_context \*

    :param ht:
        Pointer to a hash table to use for duplicate finding
        This function is intended to be used if the hash table wasn't
        available at validation context declaration time
    :type ht: struct drm_open_hash \*

.. _`vmw_validation_bo_reserve`:

vmw_validation_bo_reserve
=========================

.. c:function:: int vmw_validation_bo_reserve(struct vmw_validation_context *ctx, bool intr)

    Reserve buffer objects registered with a validation context

    :param ctx:
        The validation context
    :type ctx: struct vmw_validation_context \*

    :param intr:
        Perform waits interruptible
    :type intr: bool

.. _`vmw_validation_bo_reserve.return`:

Return
------

Zero on success, -ERESTARTSYS when interrupted, negative error
code on failure

.. _`vmw_validation_bo_backoff`:

vmw_validation_bo_backoff
=========================

.. c:function:: void vmw_validation_bo_backoff(struct vmw_validation_context *ctx)

    Unreserve buffer objects registered with a validation context

    :param ctx:
        The validation context
    :type ctx: struct vmw_validation_context \*

.. _`vmw_validation_bo_backoff.description`:

Description
-----------

This function unreserves the buffer objects previously reserved using
vmw_validation_bo_reserve. It's typically used as part of an error path

.. _`vmw_validation_bo_fence`:

vmw_validation_bo_fence
=======================

.. c:function:: void vmw_validation_bo_fence(struct vmw_validation_context *ctx, struct vmw_fence_obj *fence)

    Unreserve and fence buffer objects registered with a validation context

    :param ctx:
        The validation context
    :type ctx: struct vmw_validation_context \*

    :param fence:
        *undescribed*
    :type fence: struct vmw_fence_obj \*

.. _`vmw_validation_bo_fence.description`:

Description
-----------

This function unreserves the buffer objects previously reserved using
vmw_validation_bo_reserve, and fences them with a fence object.

.. _`vmw_validation_context_init`:

vmw_validation_context_init
===========================

.. c:function:: void vmw_validation_context_init(struct vmw_validation_context *ctx)

    Initialize a validation context

    :param ctx:
        Pointer to the validation context to initialize
    :type ctx: struct vmw_validation_context \*

.. _`vmw_validation_context_init.description`:

Description
-----------

This function initializes a validation context with \ ``merge_dups``\  set
to false

.. _`vmw_validation_align`:

vmw_validation_align
====================

.. c:function:: unsigned int vmw_validation_align(unsigned int val)

    Align a validation memory allocation

    :param val:
        The size to be aligned
    :type val: unsigned int

.. _`vmw_validation_align.return`:

Return
------

\ ``val``\  aligned to the granularity used by the validation memory
allocator.

.. This file was automatic generated / don't edit.

