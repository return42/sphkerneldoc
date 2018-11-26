.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/omapdrm/omap_irq.c

.. _`omap_irq_enable_vblank`:

omap_irq_enable_vblank
======================

.. c:function:: int omap_irq_enable_vblank(struct drm_crtc *crtc)

    enable vblank interrupt events

    :param crtc:
        *undescribed*
    :type crtc: struct drm_crtc \*

.. _`omap_irq_enable_vblank.description`:

Description
-----------

Enable vblank interrupts for \ ``crtc``\ .  If the device doesn't have
a hardware vblank counter, this routine should be a no-op, since
interrupts will have to stay on to keep the count accurate.

RETURNS
Zero on success, appropriate errno if the given \ ``crtc``\ 's vblank
interrupt cannot be enabled.

.. _`omap_irq_disable_vblank`:

omap_irq_disable_vblank
=======================

.. c:function:: void omap_irq_disable_vblank(struct drm_crtc *crtc)

    disable vblank interrupt events

    :param crtc:
        *undescribed*
    :type crtc: struct drm_crtc \*

.. _`omap_irq_disable_vblank.description`:

Description
-----------

Disable vblank interrupts for \ ``crtc``\ .  If the device doesn't have
a hardware vblank counter, this routine should be a no-op, since
interrupts will have to stay on to keep the count accurate.

.. This file was automatic generated / don't edit.

