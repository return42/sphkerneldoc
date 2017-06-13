.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_encoder.c

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

