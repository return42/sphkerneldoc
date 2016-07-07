.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_dmabuf.c

.. _`vmw_dmabuf_pin_in_placement`:

vmw_dmabuf_pin_in_placement
===========================

.. c:function:: int vmw_dmabuf_pin_in_placement(struct vmw_private *dev_priv, struct vmw_dma_buffer *buf, struct ttm_placement *placement, bool interruptible)

    Validate a buffer to placement.

    :param struct vmw_private \*dev_priv:
        Driver private.

    :param struct vmw_dma_buffer \*buf:
        DMA buffer to move.

    :param struct ttm_placement \*placement:
        The placement to pin it.

    :param bool interruptible:
        Use interruptible wait.

.. _`vmw_dmabuf_pin_in_placement.description`:

Description
-----------

Returns
-ERESTARTSYS if interrupted by a signal.

.. _`vmw_dmabuf_pin_in_vram_or_gmr`:

vmw_dmabuf_pin_in_vram_or_gmr
=============================

.. c:function:: int vmw_dmabuf_pin_in_vram_or_gmr(struct vmw_private *dev_priv, struct vmw_dma_buffer *buf, bool interruptible)

    Move a buffer to vram or gmr.

    :param struct vmw_private \*dev_priv:
        Driver private.

    :param struct vmw_dma_buffer \*buf:
        DMA buffer to move.

    :param bool interruptible:
        Use interruptible wait.

.. _`vmw_dmabuf_pin_in_vram_or_gmr.description`:

Description
-----------

This function takes the reservation_sem in write mode.
Flushes and unpins the query bo to avoid failures.

Returns
-ERESTARTSYS if interrupted by a signal.

.. _`vmw_dmabuf_pin_in_vram`:

vmw_dmabuf_pin_in_vram
======================

.. c:function:: int vmw_dmabuf_pin_in_vram(struct vmw_private *dev_priv, struct vmw_dma_buffer *buf, bool interruptible)

    Move a buffer to vram.

    :param struct vmw_private \*dev_priv:
        Driver private.

    :param struct vmw_dma_buffer \*buf:
        DMA buffer to move.

    :param bool interruptible:
        Use interruptible wait.

.. _`vmw_dmabuf_pin_in_vram.description`:

Description
-----------

This function takes the reservation_sem in write mode.
Flushes and unpins the query bo to avoid failures.

Returns
-ERESTARTSYS if interrupted by a signal.

.. _`vmw_dmabuf_pin_in_start_of_vram`:

vmw_dmabuf_pin_in_start_of_vram
===============================

.. c:function:: int vmw_dmabuf_pin_in_start_of_vram(struct vmw_private *dev_priv, struct vmw_dma_buffer *buf, bool interruptible)

    Move a buffer to start of vram.

    :param struct vmw_private \*dev_priv:
        Driver private.

    :param struct vmw_dma_buffer \*buf:
        DMA buffer to pin.

    :param bool interruptible:
        Use interruptible wait.

.. _`vmw_dmabuf_pin_in_start_of_vram.description`:

Description
-----------

This function takes the reservation_sem in write mode.
Flushes and unpins the query bo to avoid failures.

Returns
-ERESTARTSYS if interrupted by a signal.

.. _`vmw_dmabuf_unpin`:

vmw_dmabuf_unpin
================

.. c:function:: int vmw_dmabuf_unpin(struct vmw_private *dev_priv, struct vmw_dma_buffer *buf, bool interruptible)

    Unpin the buffer given buffer, does not move the buffer.

    :param struct vmw_private \*dev_priv:
        Driver private.

    :param struct vmw_dma_buffer \*buf:
        DMA buffer to unpin.

    :param bool interruptible:
        Use interruptible wait.

.. _`vmw_dmabuf_unpin.description`:

Description
-----------

This function takes the reservation_sem in write mode.

Returns
-ERESTARTSYS if interrupted by a signal.

.. _`vmw_bo_get_guest_ptr`:

vmw_bo_get_guest_ptr
====================

.. c:function:: void vmw_bo_get_guest_ptr(const struct ttm_buffer_object *bo, SVGAGuestPtr *ptr)

    Get the guest ptr representing the current placement of a buffer.

    :param const struct ttm_buffer_object \*bo:
        Pointer to a struct ttm_buffer_object. Must be pinned or reserved.

    :param SVGAGuestPtr \*ptr:
        SVGAGuestPtr returning the result.

.. _`vmw_bo_pin_reserved`:

vmw_bo_pin_reserved
===================

.. c:function:: void vmw_bo_pin_reserved(struct vmw_dma_buffer *vbo, bool pin)

    Pin or unpin a buffer object without moving it.

    :param struct vmw_dma_buffer \*vbo:
        The buffer object. Must be reserved.

    :param bool pin:
        Whether to pin or unpin.

.. This file was automatic generated / don't edit.

