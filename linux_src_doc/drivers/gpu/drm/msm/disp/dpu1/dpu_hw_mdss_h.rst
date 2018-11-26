.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_hw_mdss.h

.. _`dpu_plane_type`:

enum dpu_plane_type
===================

.. c:type:: enum dpu_plane_type

    defines how the color component pixel packing

.. _`dpu_plane_type.definition`:

Definition
----------

.. code-block:: c

    enum dpu_plane_type {
        DPU_PLANE_INTERLEAVED,
        DPU_PLANE_PLANAR,
        DPU_PLANE_PSEUDO_PLANAR
    };

.. _`dpu_plane_type.constants`:

Constants
---------

DPU_PLANE_INTERLEAVED
    Color components in single plane

DPU_PLANE_PLANAR
    Color component in separate planes

DPU_PLANE_PSEUDO_PLANAR
    Chroma components interleaved in separate plane

.. _`dpu_chroma_samp_type`:

enum dpu_chroma_samp_type
=========================

.. c:type:: enum dpu_chroma_samp_type

    chroma sub-samplng type

.. _`dpu_chroma_samp_type.definition`:

Definition
----------

.. code-block:: c

    enum dpu_chroma_samp_type {
        DPU_CHROMA_RGB,
        DPU_CHROMA_H2V1,
        DPU_CHROMA_H1V2,
        DPU_CHROMA_420
    };

.. _`dpu_chroma_samp_type.constants`:

Constants
---------

DPU_CHROMA_RGB
    No chroma subsampling

DPU_CHROMA_H2V1
    Chroma pixels are horizontally subsampled

DPU_CHROMA_H1V2
    Chroma pixels are vertically subsampled

DPU_CHROMA_420
    420 subsampling

.. _`dpu_3d_blend_mode`:

enum dpu_3d_blend_mode
======================

.. c:type:: enum dpu_3d_blend_mode

    Desribes how the 3d data is blended

.. _`dpu_3d_blend_mode.definition`:

Definition
----------

.. code-block:: c

    enum dpu_3d_blend_mode {
        BLEND_3D_NONE,
        BLEND_3D_FRAME_INT,
        BLEND_3D_H_ROW_INT,
        BLEND_3D_V_ROW_INT,
        BLEND_3D_COL_INT,
        BLEND_3D_MAX
    };

.. _`dpu_3d_blend_mode.constants`:

Constants
---------

BLEND_3D_NONE
    3d blending not enabled

BLEND_3D_FRAME_INT
    Frame interleaving

BLEND_3D_H_ROW_INT
    Horizontal row interleaving

BLEND_3D_V_ROW_INT
    vertical row interleaving

BLEND_3D_COL_INT
    column interleaving

BLEND_3D_MAX
    *undescribed*

.. _`dpu_hw_fmt_layout`:

struct dpu_hw_fmt_layout
========================

.. c:type:: struct dpu_hw_fmt_layout

    format information of the source pixel data

.. _`dpu_hw_fmt_layout.definition`:

Definition
----------

.. code-block:: c

    struct dpu_hw_fmt_layout {
        const struct dpu_format *format;
        uint32_t num_planes;
        uint32_t width;
        uint32_t height;
        uint32_t total_size;
        uint32_t plane_addr[DPU_MAX_PLANES];
        uint32_t plane_size[DPU_MAX_PLANES];
        uint32_t plane_pitch[DPU_MAX_PLANES];
    }

.. _`dpu_hw_fmt_layout.members`:

Members
-------

format
    pixel format parameters

num_planes
    number of planes (including meta data planes)

width
    image width

height
    image height

total_size
    total size in bytes

plane_addr
    address of each plane

plane_size
    length of each plane

plane_pitch
    pitch of each plane

.. _`dpu_mdss_color`:

struct dpu_mdss_color
=====================

.. c:type:: struct dpu_mdss_color

    mdss color description color 0 : green color 1 : blue color 2 : red color 3 : alpha

.. _`dpu_mdss_color.definition`:

Definition
----------

.. code-block:: c

    struct dpu_mdss_color {
        u32 color_0;
        u32 color_1;
        u32 color_2;
        u32 color_3;
    }

.. _`dpu_mdss_color.members`:

Members
-------

color_0
    *undescribed*

color_1
    *undescribed*

color_2
    *undescribed*

color_3
    *undescribed*

.. This file was automatic generated / don't edit.

