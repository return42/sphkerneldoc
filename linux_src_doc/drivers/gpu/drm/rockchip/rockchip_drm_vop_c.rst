.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/rockchip/rockchip_drm_vop.c

.. _`rockchip_drm_wait_vact_end`:

rockchip_drm_wait_vact_end
==========================

.. c:function:: int rockchip_drm_wait_vact_end(struct drm_crtc *crtc, unsigned int mstimeout)

    :param crtc:
        CRTC to enable line flag
    :type crtc: struct drm_crtc \*

    :param mstimeout:
        millisecond for timeout
    :type mstimeout: unsigned int

.. _`rockchip_drm_wait_vact_end.description`:

Description
-----------

Wait for vact_end line flag irq or timeout.

.. _`rockchip_drm_wait_vact_end.return`:

Return
------

Zero on success, negative errno on failure.

.. This file was automatic generated / don't edit.

