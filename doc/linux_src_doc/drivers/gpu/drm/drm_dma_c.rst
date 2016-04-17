.. -*- coding: utf-8; mode: rst -*-

=========
drm_dma.c
=========


.. _`drm_legacy_dma_setup`:

drm_legacy_dma_setup
====================

.. c:function:: int drm_legacy_dma_setup (struct drm_device *dev)

    :param struct drm_device \*dev:

        *undescribed*



.. _`drm_legacy_dma_setup.description`:

Description
-----------


\param dev DRM device.
\return zero on success or a negative value on failure.

Allocate and initialize a drm_device_dma structure.



.. _`drm_legacy_dma_takedown`:

drm_legacy_dma_takedown
=======================

.. c:function:: void drm_legacy_dma_takedown (struct drm_device *dev)

    :param struct drm_device \*dev:

        *undescribed*



.. _`drm_legacy_dma_takedown.description`:

Description
-----------


\param dev DRM device.

Free all pages associated with DMA buffers, the buffers and pages lists, and



.. _`drm_legacy_dma_takedown.finally-the-drm_device`:

finally the drm_device
----------------------

:dma structure itself.



.. _`drm_legacy_free_buffer`:

drm_legacy_free_buffer
======================

.. c:function:: void drm_legacy_free_buffer (struct drm_device *dev, struct drm_buf *buf)

    :param struct drm_device \*dev:

        *undescribed*

    :param struct drm_buf \*buf:

        *undescribed*



.. _`drm_legacy_free_buffer.description`:

Description
-----------


\param dev DRM device.
\param buf buffer to free.

Resets the fields of \p buf.



.. _`drm_legacy_reclaim_buffers`:

drm_legacy_reclaim_buffers
==========================

.. c:function:: void drm_legacy_reclaim_buffers (struct drm_device *dev, struct drm_file *file_priv)

    :param struct drm_device \*dev:

        *undescribed*

    :param struct drm_file \*file_priv:

        *undescribed*



.. _`drm_legacy_reclaim_buffers.description`:

Description
-----------


\param file_priv DRM file private.

Frees each buffer associated with \p file_priv not already on the hardware.

