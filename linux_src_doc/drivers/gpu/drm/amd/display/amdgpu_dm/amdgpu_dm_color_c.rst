.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/display/amdgpu_dm/amdgpu_dm_color.c

.. _`__drm_lut_to_dc_gamma`:

\__drm_lut_to_dc_gamma
======================

.. c:function:: void __drm_lut_to_dc_gamma(struct drm_color_lut *lut, struct dc_gamma *gamma, bool is_legacy)

    of the lut - whether or not it's legacy.

    :param struct drm_color_lut \*lut:
        *undescribed*

    :param struct dc_gamma \*gamma:
        *undescribed*

    :param bool is_legacy:
        *undescribed*

.. _`amdgpu_dm_set_regamma_lut`:

amdgpu_dm_set_regamma_lut
=========================

.. c:function:: int amdgpu_dm_set_regamma_lut(struct dm_crtc_state *crtc)

    Set regamma lut for the given CRTC.

    :param struct dm_crtc_state \*crtc:
        amdgpu_dm crtc state

.. _`amdgpu_dm_set_regamma_lut.description`:

Description
-----------

Update the underlying dc_stream_state's output transfer function (OTF) in
preparation for hardware commit. If no lut is specified by user, we default
to SRGB.

.. _`amdgpu_dm_set_regamma_lut.return`:

Return
------

0 on success, -ENOMEM if memory cannot be allocated to calculate the OTF.

.. _`amdgpu_dm_set_ctm`:

amdgpu_dm_set_ctm
=================

.. c:function:: void amdgpu_dm_set_ctm(struct dm_crtc_state *crtc)

    Set the color transform matrix for the given CRTC.

    :param struct dm_crtc_state \*crtc:
        amdgpu_dm crtc state

.. _`amdgpu_dm_set_ctm.description`:

Description
-----------

Update the underlying dc_stream_state's gamut remap matrix in preparation
for hardware commit. If no matrix is specified by user, gamut remap will be
disabled.

.. _`amdgpu_dm_set_degamma_lut`:

amdgpu_dm_set_degamma_lut
=========================

.. c:function:: int amdgpu_dm_set_degamma_lut(struct drm_crtc_state *crtc_state, struct dc_plane_state *dc_plane_state)

    Set degamma lut for the given CRTC.

    :param struct drm_crtc_state \*crtc_state:
        *undescribed*

    :param struct dc_plane_state \*dc_plane_state:
        *undescribed*

.. _`amdgpu_dm_set_degamma_lut.description`:

Description
-----------

Update the underlying dc_stream_state's input transfer function (ITF) in
preparation for hardware commit. If no lut is specified by user, we default
to SRGB degamma.

Currently, we only support degamma bypass, or preprogrammed SRGB degamma.
Programmable degamma is not supported, and an attempt to do so will return
-EINVAL.

.. _`amdgpu_dm_set_degamma_lut.return`:

Return
------

0 on success, -EINVAL if custom degamma curve is given.

.. This file was automatic generated / don't edit.

