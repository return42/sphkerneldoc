.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/rockchip/rockchip_drm_psr.c

.. _`rockchip_drm_psr_inhibit_put`:

rockchip_drm_psr_inhibit_put
============================

.. c:function:: int rockchip_drm_psr_inhibit_put(struct drm_encoder *encoder)

    release PSR inhibit on given encoder

    :param encoder:
        encoder to obtain the PSR encoder
    :type encoder: struct drm_encoder \*

.. _`rockchip_drm_psr_inhibit_put.description`:

Description
-----------

Decrements PSR inhibit count on given encoder. Should be called only
for a PSR inhibit count increment done before. If PSR inhibit counter
reaches zero, PSR flush work is scheduled to make the hardware enter
PSR mode in PSR_FLUSH_TIMEOUT_MS.

.. _`rockchip_drm_psr_inhibit_put.return`:

Return
------

Zero on success, negative errno on failure.

.. _`rockchip_drm_psr_inhibit_get`:

rockchip_drm_psr_inhibit_get
============================

.. c:function:: int rockchip_drm_psr_inhibit_get(struct drm_encoder *encoder)

    acquire PSR inhibit on given encoder

    :param encoder:
        encoder to obtain the PSR encoder
    :type encoder: struct drm_encoder \*

.. _`rockchip_drm_psr_inhibit_get.description`:

Description
-----------

Increments PSR inhibit count on given encoder. This function guarantees
that after it returns PSR is turned off on given encoder and no PSR-related
hardware state change occurs at least until a matching call to
\ :c:func:`rockchip_drm_psr_inhibit_put`\  is done.

.. _`rockchip_drm_psr_inhibit_get.return`:

Return
------

Zero on success, negative errno on failure.

.. _`rockchip_drm_psr_flush_all`:

rockchip_drm_psr_flush_all
==========================

.. c:function:: void rockchip_drm_psr_flush_all(struct drm_device *dev)

    force to flush all registered PSR encoders

    :param dev:
        drm device
    :type dev: struct drm_device \*

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

.. c:function:: int rockchip_drm_psr_register(struct drm_encoder *encoder, int (*psr_set)(struct drm_encoder *, bool enable))

    register encoder to psr driver

    :param encoder:
        encoder that obtain the PSR function
    :type encoder: struct drm_encoder \*

    :param int (\*psr_set)(struct drm_encoder \*, bool enable):
        call back to set PSR state

.. _`rockchip_drm_psr_register.description`:

Description
-----------

The function returns with PSR inhibit counter initialized with one
and the caller (typically encoder driver) needs to call
\ :c:func:`rockchip_drm_psr_inhibit_put`\  when it becomes ready to accept PSR
enable request.

.. _`rockchip_drm_psr_register.return`:

Return
------

Zero on success, negative errno on failure.

.. _`rockchip_drm_psr_unregister`:

rockchip_drm_psr_unregister
===========================

.. c:function:: void rockchip_drm_psr_unregister(struct drm_encoder *encoder)

    unregister encoder to psr driver

    :param encoder:
        encoder that obtain the PSR function
    :type encoder: struct drm_encoder \*

.. _`rockchip_drm_psr_unregister.description`:

Description
-----------

It is expected that the PSR inhibit counter is 1 when this function is
called, which corresponds to a state when related encoder has been
disconnected from any CRTCs and its driver called
\ :c:func:`rockchip_drm_psr_inhibit_get`\  to stop the PSR logic.

.. _`rockchip_drm_psr_unregister.return`:

Return
------

Zero on success, negative errno on failure.

.. This file was automatic generated / don't edit.

