.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_dp_dual_mode_helper.h

.. _`drm_lspcon_mode`:

enum drm_lspcon_mode
====================

.. c:type:: enum drm_lspcon_mode


.. _`drm_lspcon_mode.definition`:

Definition
----------

.. code-block:: c

    enum drm_lspcon_mode {
        DRM_LSPCON_MODE_INVALID,
        DRM_LSPCON_MODE_LS,
        DRM_LSPCON_MODE_PCON
    };

.. _`drm_lspcon_mode.constants`:

Constants
---------

DRM_LSPCON_MODE_INVALID
    No LSPCON.

DRM_LSPCON_MODE_LS
    Level shifter mode of LSPCON
    which drives DP++ to HDMI 1.4 conversion.

DRM_LSPCON_MODE_PCON
    Protocol converter mode of LSPCON
    which drives DP++ to HDMI 2.0 active conversion.

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
        DRM_DP_DUAL_MODE_TYPE2_HDMI,
        DRM_DP_DUAL_MODE_LSPCON
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

DRM_DP_DUAL_MODE_LSPCON
    Level shifter / protocol converter

.. This file was automatic generated / don't edit.

