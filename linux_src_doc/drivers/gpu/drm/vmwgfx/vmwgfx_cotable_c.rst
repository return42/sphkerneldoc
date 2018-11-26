.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_cotable.c

.. _`vmw_cotable`:

struct vmw_cotable
==================

.. c:type:: struct vmw_cotable

    Context Object Table resource

.. _`vmw_cotable.definition`:

Definition
----------

.. code-block:: c

    struct vmw_cotable {
        struct vmw_resource res;
        struct vmw_resource *ctx;
        size_t size_read_back;
        int seen_entries;
        u32 type;
        bool scrubbed;
        struct list_head resource_list;
    }

.. _`vmw_cotable.members`:

Members
-------

res
    struct vmw_resource we are deriving from.

ctx
    non-refcounted pointer to the owning context.

size_read_back
    Size of data read back during eviction.

seen_entries
    Seen entries in command stream for this cotable.

type
    The cotable type.

scrubbed
    Whether the cotable has been scrubbed.

resource_list
    List of resources in the cotable.

.. _`vmw_cotable_info`:

struct vmw_cotable_info
=======================

.. c:type:: struct vmw_cotable_info

    Static info about cotable types

.. _`vmw_cotable_info.definition`:

Definition
----------

.. code-block:: c

    struct vmw_cotable_info {
        u32 min_initial_entries;
        u32 size;
        void (*unbind_func)(struct vmw_private *, struct list_head *, bool);
    }

.. _`vmw_cotable_info.members`:

Members
-------

min_initial_entries
    Min number of initial intries at cotable allocation
    for this cotable type.

size
    Size of each entry.

unbind_func
    *undescribed*

.. _`vmw_cotable`:

vmw_cotable
===========

.. c:function:: struct vmw_cotable *vmw_cotable(struct vmw_resource *res)

    Convert a struct vmw_resource pointer to a struct vmw_cotable pointer

    :param res:
        Pointer to the resource.
    :type res: struct vmw_resource \*

.. _`vmw_cotable_destroy`:

vmw_cotable_destroy
===================

.. c:function:: int vmw_cotable_destroy(struct vmw_resource *res)

    Cotable resource destroy callback

    :param res:
        Pointer to the cotable resource.
    :type res: struct vmw_resource \*

.. _`vmw_cotable_destroy.description`:

Description
-----------

There is no device cotable destroy command, so this function only
makes sure that the resource id is set to invalid.

.. _`vmw_cotable_unscrub`:

vmw_cotable_unscrub
===================

.. c:function:: int vmw_cotable_unscrub(struct vmw_resource *res)

    Undo a cotable unscrub operation

    :param res:
        Pointer to the cotable resource
    :type res: struct vmw_resource \*

.. _`vmw_cotable_unscrub.description`:

Description
-----------

This function issues commands to (re)bind the cotable to
its backing mob, which needs to be validated and reserved at this point.
This is identical to \ :c:func:`bind`\  except the function interface looks different.

.. _`vmw_cotable_bind`:

vmw_cotable_bind
================

.. c:function:: int vmw_cotable_bind(struct vmw_resource *res, struct ttm_validate_buffer *val_buf)

    Undo a cotable unscrub operation

    :param res:
        Pointer to the cotable resource
    :type res: struct vmw_resource \*

    :param val_buf:
        Pointer to a struct ttm_validate_buffer prepared by the caller
        for convenience / fencing.
    :type val_buf: struct ttm_validate_buffer \*

.. _`vmw_cotable_bind.description`:

Description
-----------

This function issues commands to (re)bind the cotable to
its backing mob, which needs to be validated and reserved at this point.

.. _`vmw_cotable_scrub`:

vmw_cotable_scrub
=================

.. c:function:: int vmw_cotable_scrub(struct vmw_resource *res, bool readback)

    Scrub the cotable from the device.

    :param res:
        Pointer to the cotable resource.
    :type res: struct vmw_resource \*

    :param readback:
        Whether initiate a readback of the cotable data to the backup
        buffer.
    :type readback: bool

.. _`vmw_cotable_scrub.description`:

Description
-----------

In some situations (context swapouts) it might be desirable to make the
device forget about the cotable without performing a full unbind. A full
unbind requires reserved backup buffers and it might not be possible to
reserve them due to locking order violation issues. The vmw_cotable_scrub
function implements a partial \ :c:func:`unbind`\  without that requirement but with the
following restrictions.
1) Before the cotable is again used by the GPU, \ :c:func:`vmw_cotable_unscrub`\  must
be called.
2) Before the cotable backing buffer is used by the CPU, or during the
resource destruction, \ :c:func:`vmw_cotable_unbind`\  must be called.

.. _`vmw_cotable_unbind`:

vmw_cotable_unbind
==================

.. c:function:: int vmw_cotable_unbind(struct vmw_resource *res, bool readback, struct ttm_validate_buffer *val_buf)

    Cotable resource unbind callback

    :param res:
        Pointer to the cotable resource.
    :type res: struct vmw_resource \*

    :param readback:
        Whether to read back cotable data to the backup buffer.
    :type readback: bool

    :param val_buf:
        *undescribed*
    :type val_buf: struct ttm_validate_buffer \*

.. _`vmw_cotable_unbind.val_buf`:

val_buf
-------

Pointer to a struct ttm_validate_buffer prepared by the caller
for convenience / fencing.

Unbinds the cotable from the device and fences the backup buffer.

.. _`vmw_cotable_readback`:

vmw_cotable_readback
====================

.. c:function:: int vmw_cotable_readback(struct vmw_resource *res)

    Read back a cotable without unbinding.

    :param res:
        The cotable resource.
    :type res: struct vmw_resource \*

.. _`vmw_cotable_readback.description`:

Description
-----------

Reads back a cotable to its backing mob without scrubbing the MOB from
the cotable. The MOB is fenced for subsequent CPU access.

.. _`vmw_cotable_resize`:

vmw_cotable_resize
==================

.. c:function:: int vmw_cotable_resize(struct vmw_resource *res, size_t new_size)

    Resize a cotable.

    :param res:
        The cotable resource.
    :type res: struct vmw_resource \*

    :param new_size:
        The new size.
    :type new_size: size_t

.. _`vmw_cotable_resize.description`:

Description
-----------

Resizes a cotable and binds the new backup buffer.
On failure the cotable is left intact.
Important! This function may not fail once the MOB switch has been
committed to hardware. That would put the device context in an
invalid state which we can't currently recover from.

.. _`vmw_cotable_create`:

vmw_cotable_create
==================

.. c:function:: int vmw_cotable_create(struct vmw_resource *res)

    Cotable resource create callback

    :param res:
        Pointer to a cotable resource.
    :type res: struct vmw_resource \*

.. _`vmw_cotable_create.description`:

Description
-----------

There is no separate create command for cotables, so this callback, which
is called before \ :c:func:`bind`\  in the validation sequence is instead used for two
things.
1) Unscrub the cotable if it is scrubbed and still attached to a backup
buffer, that is, if \ ``res->mob_head``\  is non-empty.
2) Resize the cotable if needed.

.. _`vmw_hw_cotable_destroy`:

vmw_hw_cotable_destroy
======================

.. c:function:: void vmw_hw_cotable_destroy(struct vmw_resource *res)

    Cotable hw_destroy callback

    :param res:
        Pointer to a cotable resource.
    :type res: struct vmw_resource \*

.. _`vmw_hw_cotable_destroy.description`:

Description
-----------

The final (part of resource destruction) destroy callback.

.. _`vmw_cotable_free`:

vmw_cotable_free
================

.. c:function:: void vmw_cotable_free(struct vmw_resource *res)

    Cotable resource destructor

    :param res:
        Pointer to a cotable resource.
    :type res: struct vmw_resource \*

.. _`vmw_cotable_alloc`:

vmw_cotable_alloc
=================

.. c:function:: struct vmw_resource *vmw_cotable_alloc(struct vmw_private *dev_priv, struct vmw_resource *ctx, u32 type)

    Create a cotable resource

    :param dev_priv:
        Pointer to a device private struct.
    :type dev_priv: struct vmw_private \*

    :param ctx:
        Pointer to the context resource.
        The cotable resource will not add a refcount.
    :type ctx: struct vmw_resource \*

    :param type:
        The cotable type.
    :type type: u32

.. _`vmw_cotable_notify`:

vmw_cotable_notify
==================

.. c:function:: int vmw_cotable_notify(struct vmw_resource *res, int id)

    Notify the cotable about an item creation

    :param res:
        Pointer to a cotable resource.
    :type res: struct vmw_resource \*

    :param id:
        Item id.
    :type id: int

.. _`vmw_cotable_add_resource`:

vmw_cotable_add_resource
========================

.. c:function:: void vmw_cotable_add_resource(struct vmw_resource *res, struct list_head *head)

    add a view to the cotable's list of active views.

    :param res:
        pointer struct vmw_resource representing the cotable.
    :type res: struct vmw_resource \*

    :param head:
        pointer to the struct list_head member of the resource, dedicated
        to the cotable active resource list.
    :type head: struct list_head \*

.. This file was automatic generated / don't edit.

