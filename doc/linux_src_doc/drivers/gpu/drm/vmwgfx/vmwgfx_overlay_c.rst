.. -*- coding: utf-8; mode: rst -*-

================
vmwgfx_overlay.c
================


.. _`vmw_overlay_send_put`:

vmw_overlay_send_put
====================

.. c:function:: int vmw_overlay_send_put (struct vmw_private *dev_priv, struct vmw_dma_buffer *buf, struct drm_vmw_control_stream_arg *arg, bool interruptible)

    :param struct vmw_private \*dev_priv:

        *undescribed*

    :param struct vmw_dma_buffer \*buf:

        *undescribed*

    :param struct drm_vmw_control_stream_arg \*arg:

        *undescribed*

    :param bool interruptible:

        *undescribed*



.. _`vmw_overlay_send_put.description`:

Description
-----------


Returns
-ERESTARTSYS if interrupted by a signal.



.. _`vmw_overlay_send_stop`:

vmw_overlay_send_stop
=====================

.. c:function:: int vmw_overlay_send_stop (struct vmw_private *dev_priv, uint32_t stream_id, bool interruptible)

    :param struct vmw_private \*dev_priv:

        *undescribed*

    :param uint32_t stream_id:

        *undescribed*

    :param bool interruptible:

        *undescribed*



.. _`vmw_overlay_send_stop.description`:

Description
-----------


Returns
-ERESTARTSYS if interrupted by a signal.



.. _`vmw_overlay_move_buffer`:

vmw_overlay_move_buffer
=======================

.. c:function:: int vmw_overlay_move_buffer (struct vmw_private *dev_priv, struct vmw_dma_buffer *buf, bool pin, bool inter)

    :param struct vmw_private \*dev_priv:

        *undescribed*

    :param struct vmw_dma_buffer \*buf:

        *undescribed*

    :param bool pin:

        *undescribed*

    :param bool inter:

        *undescribed*



.. _`vmw_overlay_move_buffer.description`:

Description
-----------


With the introduction of screen objects buffers could now be
used with GMRs instead of being locked to vram.



.. _`vmw_overlay_stop`:

vmw_overlay_stop
================

.. c:function:: int vmw_overlay_stop (struct vmw_private *dev_priv, uint32_t stream_id, bool pause, bool interruptible)

    :param struct vmw_private \*dev_priv:

        *undescribed*

    :param uint32_t stream_id:

        *undescribed*

    :param bool pause:

        *undescribed*

    :param bool interruptible:

        *undescribed*



.. _`vmw_overlay_stop.description`:

Description
-----------


If the stream is paused the no evict flag is removed from the buffer
but left in vram. This allows for instance mode_set to evict it
should it need to.

The caller must hold the overlay lock.

``stream_id`` which stream to stop/pause.
``pause`` true to pause, false to stop completely.



.. _`vmw_overlay_update_stream`:

vmw_overlay_update_stream
=========================

.. c:function:: int vmw_overlay_update_stream (struct vmw_private *dev_priv, struct vmw_dma_buffer *buf, struct drm_vmw_control_stream_arg *arg, bool interruptible)

    :param struct vmw_private \*dev_priv:

        *undescribed*

    :param struct vmw_dma_buffer \*buf:

        *undescribed*

    :param struct drm_vmw_control_stream_arg \*arg:

        *undescribed*

    :param bool interruptible:

        *undescribed*



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

.. c:function:: int vmw_overlay_stop_all (struct vmw_private *dev_priv)

    :param struct vmw_private \*dev_priv:

        *undescribed*



.. _`vmw_overlay_stop_all.description`:

Description
-----------


Used by the fb code when starting.

Takes the overlay lock.



.. _`vmw_overlay_resume_all`:

vmw_overlay_resume_all
======================

.. c:function:: int vmw_overlay_resume_all (struct vmw_private *dev_priv)

    :param struct vmw_private \*dev_priv:

        *undescribed*



.. _`vmw_overlay_resume_all.description`:

Description
-----------


Used by the kms code after moving a new scanout buffer to vram.

Takes the overlay lock.



.. _`vmw_overlay_pause_all`:

vmw_overlay_pause_all
=====================

.. c:function:: int vmw_overlay_pause_all (struct vmw_private *dev_priv)

    :param struct vmw_private \*dev_priv:

        *undescribed*



.. _`vmw_overlay_pause_all.description`:

Description
-----------


Used by the kms code when moving a new scanout buffer to vram.

Takes the overlay lock.

