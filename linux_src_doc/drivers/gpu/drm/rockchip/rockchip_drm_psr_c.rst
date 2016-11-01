.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/rockchip/rockchip_drm_psr.c

.. _`rockchip_drm_psr_activate`:

rockchip_drm_psr_activate
=========================

.. c:function:: int rockchip_drm_psr_activate(struct drm_crtc *crtc)

    activate PSR on the given pipe

    :param struct drm_crtc \*crtc:
        CRTC to obtain the PSR encoder

.. _`rockchip_drm_psr_activate.return`:

Return
------

Zero on success, negative errno on failure.

.. _`rockchip_drm_psr_deactivate`:

rockchip_drm_psr_deactivate
===========================

.. c:function:: int rockchip_drm_psr_deactivate(struct drm_crtc *crtc)

    deactivate PSR on the given pipe

    :param struct drm_crtc \*crtc:
        CRTC to obtain the PSR encoder

.. _`rockchip_drm_psr_deactivate.return`:

Return
------

Zero on success, negative errno on failure.

.. _`rockchip_drm_psr_flush`:

rockchip_drm_psr_flush
======================

.. c:function:: int rockchip_drm_psr_flush(struct drm_crtc *crtc)

    flush a single pipe

    :param struct drm_crtc \*crtc:
        CRTC of the pipe to flush

.. _`rockchip_drm_psr_flush.return`:

Return
------

0 on success, -errno on fail

.. _`rockchip_drm_psr_flush_all`:

rockchip_drm_psr_flush_all
==========================

.. c:function:: void rockchip_drm_psr_flush_all(struct drm_device *dev)

    force to flush all registered PSR encoders

    :param struct drm_device \*dev:
        drm device

.. _`rockchip_drm_psr_flush_all.description`:

Description
-----------

Disable the PSR function for all registered encoders, and then enable the
PSR function back after PSR_FLUSH_TIMEOUT. If encoder PSR state have been
changed during flush time, then keep the state no change after flush
timeout.

.. _`rockchip_drm_psr_flush_all.return`:

Return
------

Zero on success, negative errno on failure.

.. _`rockchip_drm_psr_register`:

rockchip_drm_psr_register
=========================

.. c:function:: int rockchip_drm_psr_register(struct drm_encoder *encoder, void (*psr_set)(struct drm_encoder *, bool enable))

    register encoder to psr driver

    :param struct drm_encoder \*encoder:
        encoder that obtain the PSR function

    :param void (\*psr_set)(struct drm_encoder \*, bool enable):
        call back to set PSR state

.. _`rockchip_drm_psr_register.return`:

Return
------

Zero on success, negative errno on failure.

.. _`rockchip_drm_psr_unregister`:

rockchip_drm_psr_unregister
===========================

.. c:function:: void rockchip_drm_psr_unregister(struct drm_encoder *encoder)

    unregister encoder to psr driver

    :param struct drm_encoder \*encoder:
        encoder that obtain the PSR function

.. _`rockchip_drm_psr_unregister.return`:

Return
------

Zero on success, negative errno on failure.

.. This file was automatic generated / don't edit.

