.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_color_mgmt.c

.. _`drm_color_lut_extract`:

drm_color_lut_extract
=====================

.. c:function:: uint32_t drm_color_lut_extract(uint32_t user_input, uint32_t bit_precision)

    clamp and round LUT entries

    :param uint32_t user_input:
        input value

    :param uint32_t bit_precision:
        number of bits the hw LUT supports

.. _`drm_color_lut_extract.description`:

Description
-----------

Extract a degamma/gamma LUT value provided by user (in the form of
\ :c:type:`struct drm_color_lut <drm_color_lut>`\  entries) and round it to the precision supported by the
hardware.

.. _`drm_crtc_enable_color_mgmt`:

drm_crtc_enable_color_mgmt
==========================

.. c:function:: void drm_crtc_enable_color_mgmt(struct drm_crtc *crtc, uint degamma_lut_size, bool has_ctm, uint gamma_lut_size)

    enable color management properties

    :param struct drm_crtc \*crtc:
        DRM CRTC

    :param uint degamma_lut_size:
        the size of the degamma lut (before CSC)

    :param bool has_ctm:
        whether to attach ctm_property for CSC matrix

    :param uint gamma_lut_size:
        the size of the gamma lut (after CSC)

.. _`drm_crtc_enable_color_mgmt.description`:

Description
-----------

This function lets the driver enable the color correction
properties on a CRTC. This includes 3 degamma, csc and gamma
properties that userspace can set and 2 size properties to inform
the userspace of the lut sizes. Each of the properties are
optional. The gamma and degamma properties are only attached if
their size is not 0 and ctm_property is only attached if has_ctm is
true.

.. _`drm_mode_crtc_set_gamma_size`:

drm_mode_crtc_set_gamma_size
============================

.. c:function:: int drm_mode_crtc_set_gamma_size(struct drm_crtc *crtc, int gamma_size)

    set the gamma table size

    :param struct drm_crtc \*crtc:
        CRTC to set the gamma table size for

    :param int gamma_size:
        size of the gamma table

.. _`drm_mode_crtc_set_gamma_size.description`:

Description
-----------

Drivers which support gamma tables should set this to the supported gamma
table size when initializing the CRTC. Currently the drm core only supports a
fixed gamma table size.

.. _`drm_mode_crtc_set_gamma_size.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_gamma_set_ioctl`:

drm_mode_gamma_set_ioctl
========================

.. c:function:: int drm_mode_gamma_set_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    set the gamma table

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        ioctl data

    :param struct drm_file \*file_priv:
        DRM file info

.. _`drm_mode_gamma_set_ioctl.description`:

Description
-----------

Set the gamma table of a CRTC to the one passed in by the user. Userspace can
inquire the required gamma table size through drm_mode_gamma_get_ioctl.

Called by the user via ioctl.

.. _`drm_mode_gamma_set_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

.. _`drm_mode_gamma_get_ioctl`:

drm_mode_gamma_get_ioctl
========================

.. c:function:: int drm_mode_gamma_get_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    get the gamma table

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        ioctl data

    :param struct drm_file \*file_priv:
        DRM file info

.. _`drm_mode_gamma_get_ioctl.description`:

Description
-----------

Copy the current gamma table into the storage provided. This also provides
the gamma table size the driver expects, which can be used to size the
allocated storage.

Called by the user via ioctl.

.. _`drm_mode_gamma_get_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

.. This file was automatic generated / don't edit.

