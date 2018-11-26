.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/msm_drv.h

.. _`msm_display_caps`:

enum msm_display_caps
=====================

.. c:type:: enum msm_display_caps

    features/capabilities supported by displays

.. _`msm_display_caps.definition`:

Definition
----------

.. code-block:: c

    enum msm_display_caps {
        MSM_DISPLAY_CAP_VID_MODE,
        MSM_DISPLAY_CAP_CMD_MODE,
        MSM_DISPLAY_CAP_HOT_PLUG,
        MSM_DISPLAY_CAP_EDID
    };

.. _`msm_display_caps.constants`:

Constants
---------

MSM_DISPLAY_CAP_VID_MODE
    Video or "active" mode supported

MSM_DISPLAY_CAP_CMD_MODE
    Command mode supported

MSM_DISPLAY_CAP_HOT_PLUG
    Hot plug detection supported

MSM_DISPLAY_CAP_EDID
    EDID supported

.. _`msm_event_wait`:

enum msm_event_wait
===================

.. c:type:: enum msm_event_wait

    type of HW events to wait for \ ``MSM_ENC_COMMIT_DONE``\  - wait for the driver to flush the registers to HW \ ``MSM_ENC_TX_COMPLETE``\  - wait for the HW to transfer the frame to panel \ ``MSM_ENC_VBLANK``\  - wait for the HW VBLANK event (for driver-internal waiters)

.. _`msm_event_wait.definition`:

Definition
----------

.. code-block:: c

    enum msm_event_wait {
        MSM_ENC_COMMIT_DONE,
        MSM_ENC_TX_COMPLETE,
        MSM_ENC_VBLANK
    };

.. _`msm_event_wait.constants`:

Constants
---------

MSM_ENC_COMMIT_DONE
    *undescribed*

MSM_ENC_TX_COMPLETE
    *undescribed*

MSM_ENC_VBLANK
    *undescribed*

.. _`msm_display_topology`:

struct msm_display_topology
===========================

.. c:type:: struct msm_display_topology

    defines a display topology pipeline

.. _`msm_display_topology.definition`:

Definition
----------

.. code-block:: c

    struct msm_display_topology {
        u32 num_lm;
        u32 num_enc;
        u32 num_intf;
    }

.. _`msm_display_topology.members`:

Members
-------

num_lm
    number of layer mixers used

num_enc
    number of compression encoder blocks used

num_intf
    number of interfaces the panel is mounted on

.. _`msm_display_info`:

struct msm_display_info
=======================

.. c:type:: struct msm_display_info

    defines display properties

.. _`msm_display_info.definition`:

Definition
----------

.. code-block:: c

    struct msm_display_info {
        int intf_type;
        uint32_t capabilities;
        uint32_t num_of_h_tiles;
        uint32_t h_tile_instance[MAX_H_TILES_PER_DISPLAY];
        bool is_te_using_watchdog_timer;
    }

.. _`msm_display_info.members`:

Members
-------

intf_type
    DRM_MODE_CONNECTOR\_ display type

capabilities
    Bitmask of display flags

num_of_h_tiles
    Number of horizontal tiles in case of split interface

h_tile_instance
    Controller instance used per tile. Number of elements is
    based on num_of_h_tiles

is_te_using_watchdog_timer
    Boolean to indicate watchdog TE is
    used instead of panel TE in cmd mode panels

.. This file was automatic generated / don't edit.

