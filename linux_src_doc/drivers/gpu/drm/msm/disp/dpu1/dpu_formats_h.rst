.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_formats.h

.. _`dpu_get_dpu_format_ext`:

dpu_get_dpu_format_ext
======================

.. c:function:: const struct dpu_format *dpu_get_dpu_format_ext(const uint32_t format, const uint64_t modifier)

    Returns dpu format structure pointer.

    :param format:
        DRM FourCC Code
    :type format: const uint32_t

    :param modifier:
        *undescribed*
    :type modifier: const uint64_t

.. _`dpu_get_msm_format`:

dpu_get_msm_format
==================

.. c:function:: const struct msm_format *dpu_get_msm_format(struct msm_kms *kms, const uint32_t format, const uint64_t modifiers)

    get an dpu_format by its msm_format base callback function registers with the msm_kms layer

    :param kms:
        kms driver
    :type kms: struct msm_kms \*

    :param format:
        DRM FourCC Code
    :type format: const uint32_t

    :param modifiers:
        data layout modifier
    :type modifiers: const uint64_t

.. _`dpu_populate_formats`:

dpu_populate_formats
====================

.. c:function:: uint32_t dpu_populate_formats(const struct dpu_format_extended *format_list, uint32_t *pixel_formats, uint64_t *pixel_modifiers, uint32_t pixel_formats_max)

    populate the given array with fourcc codes supported

    :param format_list:
        pointer to list of possible formats
    :type format_list: const struct dpu_format_extended \*

    :param pixel_formats:
        array to populate with fourcc codes
    :type pixel_formats: uint32_t \*

    :param pixel_modifiers:
        array to populate with drm modifiers, can be NULL
    :type pixel_modifiers: uint64_t \*

    :param pixel_formats_max:
        length of pixel formats array
    :type pixel_formats_max: uint32_t

.. _`dpu_populate_formats.return`:

Return
------

number of elements populated

.. _`dpu_format_check_modified_format`:

dpu_format_check_modified_format
================================

.. c:function:: int dpu_format_check_modified_format(const struct msm_kms *kms, const struct msm_format *msm_fmt, const struct drm_mode_fb_cmd2 *cmd, struct drm_gem_object **bos)

    validate format and buffers for dpu non-standard, i.e. modified format

    :param kms:
        kms driver
    :type kms: const struct msm_kms \*

    :param msm_fmt:
        pointer to the msm_fmt base pointer of an dpu_format
    :type msm_fmt: const struct msm_format \*

    :param cmd:
        fb_cmd2 structure user request
    :type cmd: const struct drm_mode_fb_cmd2 \*

    :param bos:
        gem buffer object list
    :type bos: struct drm_gem_object \*\*

.. _`dpu_format_check_modified_format.return`:

Return
------

error code on failure, 0 on success

.. _`dpu_format_populate_layout`:

dpu_format_populate_layout
==========================

.. c:function:: int dpu_format_populate_layout(struct msm_gem_address_space *aspace, struct drm_framebuffer *fb, struct dpu_hw_fmt_layout *fmtl)

    populate the given format layout based on mmu, fb, and format found in the fb

    :param aspace:
        address space pointer
    :type aspace: struct msm_gem_address_space \*

    :param fb:
        framebuffer pointer
    :type fb: struct drm_framebuffer \*

    :param fmtl:
        format layout structure to populate
    :type fmtl: struct dpu_hw_fmt_layout \*

.. _`dpu_format_populate_layout.return`:

Return
------

error code on failure, -EAGAIN if success but the addresses
are the same as before or 0 if new addresses were populated

.. This file was automatic generated / don't edit.

