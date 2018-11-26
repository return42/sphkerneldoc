.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_dma.c

.. _`drm_legacy_dma_setup`:

drm_legacy_dma_setup
====================

.. c:function:: int drm_legacy_dma_setup(struct drm_device *dev)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

.. _`drm_legacy_dma_setup.description`:

Description
-----------

\param dev DRM device.
\return zero on success or a negative value on failure.

Allocate and initialize a drm_device_dma structure.

.. _`drm_legacy_dma_takedown`:

drm_legacy_dma_takedown
=======================

.. c:function:: void drm_legacy_dma_takedown(struct drm_device *dev)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

.. _`drm_legacy_dma_takedown.description`:

Description
-----------

\param dev DRM device.

Free all pages associated with DMA buffers, the buffers and pages lists, and
finally the drm_device::dma structure itself.

.. _`drm_legacy_free_buffer`:

drm_legacy_free_buffer
======================

.. c:function:: void drm_legacy_free_buffer(struct drm_device *dev, struct drm_buf *buf)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param buf:
        *undescribed*
    :type buf: struct drm_buf \*

.. _`drm_legacy_free_buffer.description`:

Description
-----------

\param dev DRM device.
\param buf buffer to free.

Resets the fields of \p buf.

.. _`drm_legacy_reclaim_buffers`:

drm_legacy_reclaim_buffers
==========================

.. c:function:: void drm_legacy_reclaim_buffers(struct drm_device *dev, struct drm_file *file_priv)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param file_priv:
        *undescribed*
    :type file_priv: struct drm_file \*

.. _`drm_legacy_reclaim_buffers.description`:

Description
-----------

\param file_priv DRM file private.

Frees each buffer associated with \p file_priv not already on the hardware.

.. This file was automatic generated / don't edit.

