.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_va.c

.. _`vmw_stream`:

struct vmw_stream
=================

.. c:type:: struct vmw_stream

    Overlay stream simple resource.

.. _`vmw_stream.definition`:

Definition
----------

.. code-block:: c

    struct vmw_stream {
        struct vmw_simple_resource sres;
        u32 stream_id;
    }

.. _`vmw_stream.members`:

Members
-------

sres
    The simple resource we derive from.

stream_id
    The overlay stream id.

.. _`vmw_stream`:

vmw_stream
==========

.. c:function:: struct vmw_stream *vmw_stream(struct vmw_resource *res)

    Typecast a struct vmw_resource to a struct vmw_stream.

    :param struct vmw_resource \*res:
        Pointer to the struct vmw_resource.

.. _`vmw_stream.return`:

Return
------

Returns a pointer to the struct vmw_stream.

.. _`vmw_stream_unref_ioctl`:

vmw_stream_unref_ioctl
======================

.. c:function:: int vmw_stream_unref_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    Ioctl to unreference a user-space handle to a struct vmw_stream.

    :param struct drm_device \*dev:
        Pointer to the drm device.

    :param void \*data:
        The ioctl argument

    :param struct drm_file \*file_priv:
        Pointer to a struct drm_file identifying the caller.

.. _`vmw_stream_unref_ioctl.return`:

Return
------

0 if successful.
Negative error value on failure.

.. _`vmw_stream_claim_ioctl`:

vmw_stream_claim_ioctl
======================

.. c:function:: int vmw_stream_claim_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    Ioctl to claim a struct vmw_stream overlay.

    :param struct drm_device \*dev:
        Pointer to the drm device.

    :param void \*data:
        The ioctl argument

    :param struct drm_file \*file_priv:
        Pointer to a struct drm_file identifying the caller.

.. _`vmw_stream_claim_ioctl.return`:

Return
------

0 if successful.
Negative error value on failure.

.. _`vmw_user_stream_lookup`:

vmw_user_stream_lookup
======================

.. c:function:: int vmw_user_stream_lookup(struct vmw_private *dev_priv, struct ttm_object_file *tfile, uint32_t *inout_id, struct vmw_resource **out)

    Look up a struct vmw_user_stream from a handle.

    :param struct vmw_private \*dev_priv:
        Pointer to a struct vmw_private.

    :param struct ttm_object_file \*tfile:
        struct ttm_object_file identifying the caller.

    :param uint32_t \*inout_id:
        In: The user-space handle. Out: The stream id.

    :param struct vmw_resource \*\*out:
        On output contains a refcounted pointer to the embedded
        struct vmw_resource.

.. _`vmw_user_stream_lookup.return`:

Return
------

0 if successful.
Negative error value on failure.

.. This file was automatic generated / don't edit.

