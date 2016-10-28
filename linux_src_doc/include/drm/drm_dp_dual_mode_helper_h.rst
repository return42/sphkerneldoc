.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_dp_dual_mode_helper.h

.. _`drm_dp_dual_mode_type`:

enum drm_dp_dual_mode_type
==========================

.. c:type:: enum drm_dp_dual_mode_type

    Type of the DP dual mode adaptor

.. _`drm_dp_dual_mode_type.definition`:

Definition
----------

.. code-block:: c

    enum drm_dp_dual_mode_type {
        DRM_DP_DUAL_MODE_NONE,
        DRM_DP_DUAL_MODE_UNKNOWN,
        DRM_DP_DUAL_MODE_TYPE1_DVI,
        DRM_DP_DUAL_MODE_TYPE1_HDMI,
        DRM_DP_DUAL_MODE_TYPE2_DVI,
        DRM_DP_DUAL_MODE_TYPE2_HDMI
    };

.. _`drm_dp_dual_mode_type.constants`:

Constants
---------

DRM_DP_DUAL_MODE_NONE
    No DP dual mode adaptor

DRM_DP_DUAL_MODE_UNKNOWN
    Could be either none or type 1 DVI adaptor

DRM_DP_DUAL_MODE_TYPE1_DVI
    Type 1 DVI adaptor

DRM_DP_DUAL_MODE_TYPE1_HDMI
    Type 1 HDMI adaptor

DRM_DP_DUAL_MODE_TYPE2_DVI
    Type 2 DVI adaptor

DRM_DP_DUAL_MODE_TYPE2_HDMI
    Type 2 HDMI adaptor

.. This file was automatic generated / don't edit.

