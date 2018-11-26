.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_overlay.c

.. _`vmw_overlay_send_put`:

vmw_overlay_send_put
====================

.. c:function:: int vmw_overlay_send_put(struct vmw_private *dev_priv, struct vmw_buffer_object *buf, struct drm_vmw_control_stream_arg *arg, bool interruptible)

    :param dev_priv:
        *undescribed*
    :type dev_priv: struct vmw_private \*

    :param buf:
        *undescribed*
    :type buf: struct vmw_buffer_object \*

    :param arg:
        *undescribed*
    :type arg: struct drm_vmw_control_stream_arg \*

    :param interruptible:
        *undescribed*
    :type interruptible: bool

.. _`vmw_overlay_send_put.description`:

Description
-----------

Returns
-ERESTARTSYS if interrupted by a signal.

.. _`vmw_overlay_send_stop`:

vmw_overlay_send_stop
=====================

.. c:function:: int vmw_overlay_send_stop(struct vmw_private *dev_priv, uint32_t stream_id, bool interruptible)

    :param dev_priv:
        *undescribed*
    :type dev_priv: struct vmw_private \*

    :param stream_id:
        *undescribed*
    :type stream_id: uint32_t

    :param interruptible:
        *undescribed*
    :type interruptible: bool

.. _`vmw_overlay_send_stop.description`:

Description
-----------

Returns
-ERESTARTSYS if interrupted by a signal.

.. _`vmw_overlay_move_buffer`:

vmw_overlay_move_buffer
=======================

.. c:function:: int vmw_overlay_move_buffer(struct vmw_private *dev_priv, struct vmw_buffer_object *buf, bool pin, bool inter)

    :param dev_priv:
        *undescribed*
    :type dev_priv: struct vmw_private \*

    :param buf:
        *undescribed*
    :type buf: struct vmw_buffer_object \*

    :param pin:
        *undescribed*
    :type pin: bool

    :param inter:
        *undescribed*
    :type inter: bool

.. _`vmw_overlay_move_buffer.description`:

Description
-----------

With the introduction of screen objects buffers could now be
used with GMRs instead of being locked to vram.

.. _`vmw_overlay_stop`:

vmw_overlay_stop
================

.. c:function:: int vmw_overlay_stop(struct vmw_private *dev_priv, uint32_t stream_id, bool pause, bool interruptible)

    :param dev_priv:
        *undescribed*
    :type dev_priv: struct vmw_private \*

    :param stream_id:
        *undescribed*
    :type stream_id: uint32_t

    :param pause:
        *undescribed*
    :type pause: bool

    :param interruptible:
        *undescribed*
    :type interruptible: bool

.. _`vmw_overlay_stop.description`:

Description
-----------

If the stream is paused the no evict flag is removed from the buffer
but left in vram. This allows for instance mode_set to evict it
should it need to.

The caller must hold the overlay lock.

\ ``stream_id``\  which stream to stop/pause.
\ ``pause``\  true to pause, false to stop completely.

.. _`vmw_overlay_update_stream`:

vmw_overlay_update_stream
=========================

.. c:function:: int vmw_overlay_update_stream(struct vmw_private *dev_priv, struct vmw_buffer_object *buf, struct drm_vmw_control_stream_arg *arg, bool interruptible)

    :param dev_priv:
        *undescribed*
    :type dev_priv: struct vmw_private \*

    :param buf:
        *undescribed*
    :type buf: struct vmw_buffer_object \*

    :param arg:
        *undescribed*
    :type arg: struct drm_vmw_control_stream_arg \*

    :param interruptible:
        *undescribed*
    :type interruptible: bool

.. _`vmw_overlay_update_stream.description`:

Description
-----------

The caller must hold the overlay lock.

Returns
-ENOMEM if buffer doesn't fit in vram.
-ERESTARTSYS if interrupted.

.. _`vmw_overlay_stop_all`:

vmw_overlay_stop_all
====================

.. c:function:: int vmw_overlay_stop_all(struct vmw_private *dev_priv)

    :param dev_priv:
        *undescribed*
    :type dev_priv: struct vmw_private \*

.. _`vmw_overlay_stop_all.description`:

Description
-----------

Used by the fb code when starting.

Takes the overlay lock.

.. _`vmw_overlay_resume_all`:

vmw_overlay_resume_all
======================

.. c:function:: int vmw_overlay_resume_all(struct vmw_private *dev_priv)

    :param dev_priv:
        *undescribed*
    :type dev_priv: struct vmw_private \*

.. _`vmw_overlay_resume_all.description`:

Description
-----------

Used by the kms code after moving a new scanout buffer to vram.

Takes the overlay lock.

.. _`vmw_overlay_pause_all`:

vmw_overlay_pause_all
=====================

.. c:function:: int vmw_overlay_pause_all(struct vmw_private *dev_priv)

    :param dev_priv:
        *undescribed*
    :type dev_priv: struct vmw_private \*

.. _`vmw_overlay_pause_all.description`:

Description
-----------

Used by the kms code when moving a new scanout buffer to vram.

Takes the overlay lock.

.. This file was automatic generated / don't edit.

