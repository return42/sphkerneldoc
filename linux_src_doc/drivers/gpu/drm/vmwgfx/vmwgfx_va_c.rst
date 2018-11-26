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

    :param res:
        Pointer to the struct vmw_resource.
    :type res: struct vmw_resource \*

.. _`vmw_stream.return`:

Return
------

Returns a pointer to the struct vmw_stream.

.. _`vmw_stream_unref_ioctl`:

vmw_stream_unref_ioctl
======================

.. c:function:: int vmw_stream_unref_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    Ioctl to unreference a user-space handle to a struct vmw_stream.

    :param dev:
        Pointer to the drm device.
    :type dev: struct drm_device \*

    :param data:
        The ioctl argument
    :type data: void \*

    :param file_priv:
        Pointer to a struct drm_file identifying the caller.
    :type file_priv: struct drm_file \*

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

    :param dev:
        Pointer to the drm device.
    :type dev: struct drm_device \*

    :param data:
        The ioctl argument
    :type data: void \*

    :param file_priv:
        Pointer to a struct drm_file identifying the caller.
    :type file_priv: struct drm_file \*

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

    :param dev_priv:
        Pointer to a struct vmw_private.
    :type dev_priv: struct vmw_private \*

    :param tfile:
        struct ttm_object_file identifying the caller.
    :type tfile: struct ttm_object_file \*

    :param inout_id:
        In: The user-space handle. Out: The stream id.
    :type inout_id: uint32_t \*

    :param out:
        On output contains a refcounted pointer to the embedded
        struct vmw_resource.
    :type out: struct vmw_resource \*\*

.. _`vmw_user_stream_lookup.return`:

Return
------

0 if successful.
Negative error value on failure.

.. This file was automatic generated / don't edit.

