.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_color_mgmt.h

.. _`drm_color_lut_extract`:

drm_color_lut_extract
=====================

.. c:function:: uint32_t drm_color_lut_extract(uint32_t user_input, uint32_t bit_precision)

    clamp&round LUT entries

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

.. This file was automatic generated / don't edit.

