.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_hw_util.h

.. _`dpu_hw_scaler3_de_cfg`:

struct dpu_hw_scaler3_de_cfg
============================

.. c:type:: struct dpu_hw_scaler3_de_cfg

    QSEEDv3 detail enhancer configuration

.. _`dpu_hw_scaler3_de_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpu_hw_scaler3_de_cfg {
        u32 enable;
        int16_t sharpen_level1;
        int16_t sharpen_level2;
        uint16_t clip;
        uint16_t limit;
        uint16_t thr_quiet;
        uint16_t thr_dieout;
        uint16_t thr_low;
        uint16_t thr_high;
        uint16_t prec_shift;
        int16_t adjust_a[DPU_MAX_DE_CURVES];
        int16_t adjust_b[DPU_MAX_DE_CURVES];
        int16_t adjust_c[DPU_MAX_DE_CURVES];
    }

.. _`dpu_hw_scaler3_de_cfg.members`:

Members
-------

enable
    detail enhancer enable/disable

sharpen_level1
    sharpening strength for noise

sharpen_level2
    sharpening strength for signal
    \ ````\  clip:          clip shift
    \ ````\  limit:         limit value
    \ ````\  thr_quiet:     quiet threshold
    \ ````\  thr_dieout:    dieout threshold
    \ ````\  thr_high:      low threshold
    \ ````\  thr_high:      high threshold
    \ ````\  prec_shift:    precision shift
    \ ````\  adjust_a:      A-coefficients for mapping curve
    \ ````\  adjust_b:      B-coefficients for mapping curve
    \ ````\  adjust_c:      C-coefficients for mapping curve

clip
    *undescribed*

limit
    *undescribed*

thr_quiet
    *undescribed*

thr_dieout
    *undescribed*

thr_low
    *undescribed*

thr_high
    *undescribed*

prec_shift
    *undescribed*

adjust_a
    *undescribed*

adjust_b
    *undescribed*

adjust_c
    *undescribed*

.. _`dpu_hw_scaler3_cfg`:

struct dpu_hw_scaler3_cfg
=========================

.. c:type:: struct dpu_hw_scaler3_cfg

    QSEEDv3 configuration

.. _`dpu_hw_scaler3_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpu_hw_scaler3_cfg {
        u32 enable;
        u32 dir_en;
        int32_t init_phase_x[DPU_MAX_PLANES];
        int32_t phase_step_x[DPU_MAX_PLANES];
        int32_t init_phase_y[DPU_MAX_PLANES];
        int32_t phase_step_y[DPU_MAX_PLANES];
        u32 preload_x[DPU_MAX_PLANES];
        u32 preload_y[DPU_MAX_PLANES];
        u32 src_width[DPU_MAX_PLANES];
        u32 src_height[DPU_MAX_PLANES];
        u32 dst_width;
        u32 dst_height;
        u32 y_rgb_filter_cfg;
        u32 uv_filter_cfg;
        u32 alpha_filter_cfg;
        u32 blend_cfg;
        u32 lut_flag;
        u32 dir_lut_idx;
        u32 y_rgb_cir_lut_idx;
        u32 uv_cir_lut_idx;
        u32 y_rgb_sep_lut_idx;
        u32 uv_sep_lut_idx;
        u32 *dir_lut;
        size_t dir_len;
        u32 *cir_lut;
        size_t cir_len;
        u32 *sep_lut;
        size_t sep_len;
        struct dpu_hw_scaler3_de_cfg de;
    }

.. _`dpu_hw_scaler3_cfg.members`:

Members
-------

enable
    scaler enable

dir_en
    direction detection block enable
    \ ````\  init_phase_x: horizontal initial phase
    \ ````\  phase_step_x: horizontal phase step
    \ ````\  init_phase_y: vertical initial phase
    \ ````\  phase_step_y: vertical phase step
    \ ````\  preload_x:    horizontal preload value
    \ ````\  preload_y:    vertical preload value
    \ ````\  src_width:    source width
    \ ````\  src_height:   source height
    \ ````\  dst_width:    destination width
    \ ````\  dst_height:   destination height
    \ ````\  y_rgb_filter_cfg: y/rgb plane filter configuration
    \ ````\  uv_filter_cfg: uv plane filter configuration
    \ ````\  alpha_filter_cfg: alpha filter configuration
    \ ````\  blend_cfg:    blend coefficients configuration
    \ ````\  lut_flag:     scaler LUT update flags
    0x1 swap LUT bank
    0x2 update 2D filter LUT
    0x4 update y circular filter LUT
    0x8 update uv circular filter LUT
    0x10 update y separable filter LUT
    0x20 update uv separable filter LUT
    \ ````\  dir_lut_idx:  2D filter LUT index
    \ ````\  y_rgb_cir_lut_idx: y circular filter LUT index
    \ ````\  uv_cir_lut_idx: uv circular filter LUT index
    \ ````\  y_rgb_sep_lut_idx: y circular filter LUT index
    \ ````\  uv_sep_lut_idx: uv separable filter LUT index
    \ ````\  dir_lut:      pointer to 2D LUT
    \ ````\  cir_lut:      pointer to circular filter LUT
    \ ````\  sep_lut:      pointer to separable filter LUT
    \ ````\  de: detail enhancer configuration

init_phase_x
    *undescribed*

phase_step_x
    *undescribed*

init_phase_y
    *undescribed*

phase_step_y
    *undescribed*

preload_x
    *undescribed*

preload_y
    *undescribed*

src_width
    *undescribed*

src_height
    *undescribed*

dst_width
    *undescribed*

dst_height
    *undescribed*

y_rgb_filter_cfg
    *undescribed*

uv_filter_cfg
    *undescribed*

alpha_filter_cfg
    *undescribed*

blend_cfg
    *undescribed*

lut_flag
    *undescribed*

dir_lut_idx
    *undescribed*

y_rgb_cir_lut_idx
    *undescribed*

uv_cir_lut_idx
    *undescribed*

y_rgb_sep_lut_idx
    *undescribed*

uv_sep_lut_idx
    *undescribed*

dir_lut
    *undescribed*

dir_len
    *undescribed*

cir_lut
    *undescribed*

cir_len
    *undescribed*

sep_lut
    *undescribed*

sep_len
    *undescribed*

de
    *undescribed*

.. _`dpu_drm_pix_ext_v1`:

struct dpu_drm_pix_ext_v1
=========================

.. c:type:: struct dpu_drm_pix_ext_v1

    version 1 of pixel ext structure

.. _`dpu_drm_pix_ext_v1.definition`:

Definition
----------

.. code-block:: c

    struct dpu_drm_pix_ext_v1 {
        int32_t num_ext_pxls_lr[DPU_MAX_PLANES];
        int32_t num_ext_pxls_tb[DPU_MAX_PLANES];
        int32_t left_ftch[DPU_MAX_PLANES];
        int32_t right_ftch[DPU_MAX_PLANES];
        int32_t top_ftch[DPU_MAX_PLANES];
        int32_t btm_ftch[DPU_MAX_PLANES];
        int32_t left_rpt[DPU_MAX_PLANES];
        int32_t right_rpt[DPU_MAX_PLANES];
        int32_t top_rpt[DPU_MAX_PLANES];
        int32_t btm_rpt[DPU_MAX_PLANES];
    }

.. _`dpu_drm_pix_ext_v1.members`:

Members
-------

num_ext_pxls_lr
    Number of total horizontal pixels

num_ext_pxls_tb
    Number of total vertical lines

left_ftch
    Number of extra pixels to overfetch from left

right_ftch
    Number of extra pixels to overfetch from right

top_ftch
    Number of extra lines to overfetch from top

btm_ftch
    Number of extra lines to overfetch from bottom

left_rpt
    Number of extra pixels to repeat from left

right_rpt
    Number of extra pixels to repeat from right

top_rpt
    Number of extra lines to repeat from top

btm_rpt
    Number of extra lines to repeat from bottom

.. _`dpu_drm_de_v1`:

struct dpu_drm_de_v1
====================

.. c:type:: struct dpu_drm_de_v1

    version 1 of detail enhancer structure

.. _`dpu_drm_de_v1.definition`:

Definition
----------

.. code-block:: c

    struct dpu_drm_de_v1 {
        uint32_t enable;
        int16_t sharpen_level1;
        int16_t sharpen_level2;
        uint16_t clip;
        uint16_t limit;
        uint16_t thr_quiet;
        uint16_t thr_dieout;
        uint16_t thr_low;
        uint16_t thr_high;
        uint16_t prec_shift;
        int16_t adjust_a[DPU_MAX_DE_CURVES];
        int16_t adjust_b[DPU_MAX_DE_CURVES];
        int16_t adjust_c[DPU_MAX_DE_CURVES];
    }

.. _`dpu_drm_de_v1.members`:

Members
-------

enable
    Enables/disables detail enhancer

sharpen_level1
    Sharpening strength for noise

sharpen_level2
    Sharpening strength for context

clip
    Clip coefficient

limit
    Detail enhancer limit factor

thr_quiet
    Quite zone threshold

thr_dieout
    Die-out zone threshold

thr_low
    Linear zone left threshold

thr_high
    Linear zone right threshold

prec_shift
    Detail enhancer precision

adjust_a
    Mapping curves A coefficients

adjust_b
    Mapping curves B coefficients

adjust_c
    Mapping curves C coefficients

.. _`dpu_drm_scaler_v2`:

struct dpu_drm_scaler_v2
========================

.. c:type:: struct dpu_drm_scaler_v2

    version 2 of struct dpu_drm_scaler

.. _`dpu_drm_scaler_v2.definition`:

Definition
----------

.. code-block:: c

    struct dpu_drm_scaler_v2 {
        uint32_t enable;
        uint32_t dir_en;
        struct dpu_drm_pix_ext_v1 pe;
        uint32_t horz_decimate;
        uint32_t vert_decimate;
        int32_t init_phase_x[DPU_MAX_PLANES];
        int32_t phase_step_x[DPU_MAX_PLANES];
        int32_t init_phase_y[DPU_MAX_PLANES];
        int32_t phase_step_y[DPU_MAX_PLANES];
        uint32_t preload_x[DPU_MAX_PLANES];
        uint32_t preload_y[DPU_MAX_PLANES];
        uint32_t src_width[DPU_MAX_PLANES];
        uint32_t src_height[DPU_MAX_PLANES];
        uint32_t dst_width;
        uint32_t dst_height;
        uint32_t y_rgb_filter_cfg;
        uint32_t uv_filter_cfg;
        uint32_t alpha_filter_cfg;
        uint32_t blend_cfg;
        uint32_t lut_flag;
        uint32_t dir_lut_idx;
        uint32_t y_rgb_cir_lut_idx;
        uint32_t uv_cir_lut_idx;
        uint32_t y_rgb_sep_lut_idx;
        uint32_t uv_sep_lut_idx;
        struct dpu_drm_de_v1 de;
    }

.. _`dpu_drm_scaler_v2.members`:

Members
-------

enable
    Scaler enable

dir_en
    Detail enhancer enable

pe
    Pixel extension settings

horz_decimate
    Horizontal decimation factor

vert_decimate
    Vertical decimation factor

init_phase_x
    Initial scaler phase values for x

phase_step_x
    Phase step values for x

init_phase_y
    Initial scaler phase values for y

phase_step_y
    Phase step values for y

preload_x
    Horizontal preload value

preload_y
    Vertical preload value

src_width
    Source width

src_height
    Source height

dst_width
    Destination width

dst_height
    Destination height

y_rgb_filter_cfg
    Y/RGB plane filter configuration

uv_filter_cfg
    UV plane filter configuration

alpha_filter_cfg
    Alpha filter configuration

blend_cfg
    Selection of blend coefficients

lut_flag
    LUT configuration flags

dir_lut_idx
    2d 4x4 LUT index

y_rgb_cir_lut_idx
    Y/RGB circular LUT index

uv_cir_lut_idx
    UV circular LUT index

y_rgb_sep_lut_idx
    Y/RGB separable LUT index

uv_sep_lut_idx
    UV separable LUT index

de
    Detail enhancer settings

.. This file was automatic generated / don't edit.

