.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_encoder.c

.. _`overview`:

overview
========

Encoders represent the connecting element between the CRTC (as the overall
pixel pipeline, represented by \ :c:type:`struct drm_crtc <drm_crtc>`\ ) and the connectors (as the
generic sink entity, represented by \ :c:type:`struct drm_connector <drm_connector>`\ ). An encoder takes
pixel data from a CRTC and converts it to a format suitable for any attached
connector. Encoders are objects exposed to userspace, originally to allow
userspace to infer cloning and connector/CRTC restrictions. Unfortunately
almost all drivers get this wrong, making the uabi pretty much useless. On
top of that the exposed restrictions are too simple for today's hardware, and
the recommended way to infer restrictions is by using the
DRM_MODE_ATOMIC_TEST_ONLY flag for the atomic IOCTL.

Otherwise encoders aren't used in the uapi at all (any modeset request from
userspace directly connects a connector with a CRTC), drivers are therefore
free to use them however they wish. Modeset helper libraries make strong use
of encoders to facilitate code sharing. But for more complex settings it is
usually better to move shared code into a separate \ :c:type:`struct drm_bridge <drm_bridge>`\ . Compared to
encoders, bridges also have the benefit of being purely an internal
abstraction since they are not exposed to userspace at all.

Encoders are initialized with \ :c:func:`drm_encoder_init`\  and cleaned up using
\ :c:func:`drm_encoder_cleanup`\ .

.. _`drm_encoder_init`:

drm_encoder_init
================

.. c:function:: int drm_encoder_init(struct drm_device *dev, struct drm_encoder *encoder, const struct drm_encoder_funcs *funcs, int encoder_type, const char *name,  ...)

    Init a preallocated encoder

    :param struct drm_device \*dev:
        drm device

    :param struct drm_encoder \*encoder:
        the encoder to init

    :param const struct drm_encoder_funcs \*funcs:
        callbacks for this encoder

    :param int encoder_type:
        user visible type of the encoder

    :param const char \*name:
        printf style format string for the encoder name, or NULL for default name

    :param ... :
        variable arguments

.. _`drm_encoder_init.description`:

Description
-----------

Initialises a preallocated encoder. Encoder should be subclassed as part of
driver encoder objects. At driver unload time \ :c:func:`drm_encoder_cleanup`\  should be
called from the driver's \ :c:type:`drm_encoder_funcs.destroy <drm_encoder_funcs>`\  hook.

.. _`drm_encoder_init.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_encoder_cleanup`:

drm_encoder_cleanup
===================

.. c:function:: void drm_encoder_cleanup(struct drm_encoder *encoder)

    cleans up an initialised encoder

    :param struct drm_encoder \*encoder:
        encoder to cleanup

.. _`drm_encoder_cleanup.description`:

Description
-----------

Cleans up the encoder but doesn't free the object.

.. This file was automatic generated / don't edit.

