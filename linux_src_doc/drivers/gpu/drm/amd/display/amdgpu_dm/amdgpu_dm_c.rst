.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/display/amdgpu_dm/amdgpu_dm.c

.. _`dm_bandwidth_update`:

dm_bandwidth_update
===================

.. c:function:: void dm_bandwidth_update(struct amdgpu_device *adev)

    program display watermarks

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`dm_bandwidth_update.description`:

Description
-----------

Calculate and program the display watermarks and line buffer allocation.

.. _`amdgpu_dm_crtc_copy_transient_flags`:

amdgpu_dm_crtc_copy_transient_flags
===================================

.. c:function:: void amdgpu_dm_crtc_copy_transient_flags(struct drm_crtc_state *crtc_state, struct dc_stream_state *stream_state)

    copy mirrored flags from DRM to DC

    :param struct drm_crtc_state \*crtc_state:
        the DRM CRTC state

    :param struct dc_stream_state \*stream_state:
        the DC stream state.

.. _`amdgpu_dm_crtc_copy_transient_flags.description`:

Description
-----------

Copy the mirrored transient state flags from DRM, to DC. It is used to bring
a dc_stream_state's flags in sync with a drm_crtc_state's flags.

.. This file was automatic generated / don't edit.

