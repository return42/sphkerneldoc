.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_mode_config.c

.. _`drm_mode_getresources`:

drm_mode_getresources
=====================

.. c:function:: int drm_mode_getresources(struct drm_device *dev, void *data, struct drm_file *file_priv)

    get graphics configuration

    :param dev:
        drm device for the ioctl
    :type dev: struct drm_device \*

    :param data:
        data pointer for the ioctl
    :type data: void \*

    :param file_priv:
        drm file for the ioctl call
    :type file_priv: struct drm_file \*

.. _`drm_mode_getresources.description`:

Description
-----------

Construct a set of configuration description structures and return
them to the user, including CRTC, connector and framebuffer configuration.

Called by the user via ioctl.

.. _`drm_mode_getresources.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_config_reset`:

drm_mode_config_reset
=====================

.. c:function:: void drm_mode_config_reset(struct drm_device *dev)

    call ->reset callbacks

    :param dev:
        drm device
    :type dev: struct drm_device \*

.. _`drm_mode_config_reset.description`:

Description
-----------

This functions calls all the crtc's, encoder's and connector's ->reset
callback. Drivers can use this in e.g. their driver load or resume code to
reset hardware and software state.

.. _`drm_mode_config_init`:

drm_mode_config_init
====================

.. c:function:: void drm_mode_config_init(struct drm_device *dev)

    initialize DRM mode_configuration structure

    :param dev:
        DRM device
    :type dev: struct drm_device \*

.. _`drm_mode_config_init.description`:

Description
-----------

Initialize \ ``dev``\ 's mode_config structure, used for tracking the graphics
configuration of \ ``dev``\ .

Since this initializes the modeset locks, no locking is possible. Which is no
problem, since this should happen single threaded at init time. It is the
driver's problem to ensure this guarantee.

.. _`drm_mode_config_cleanup`:

drm_mode_config_cleanup
=======================

.. c:function:: void drm_mode_config_cleanup(struct drm_device *dev)

    free up DRM mode_config info

    :param dev:
        DRM device
    :type dev: struct drm_device \*

.. _`drm_mode_config_cleanup.description`:

Description
-----------

Free up all the connectors and CRTCs associated with this DRM device, then
free up the framebuffers and associated buffer objects.

Note that since this /should/ happen single-threaded at driver/device
teardown time, no locking is required. It's the driver's job to ensure that
this guarantee actually holds true.

FIXME: cleanup any dangling user buffer objects too

.. This file was automatic generated / don't edit.

