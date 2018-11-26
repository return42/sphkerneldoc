.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/display/dc/dce/dce_opp.c

.. _`set_truncation`:

set_truncation
==============

.. c:function:: void set_truncation(struct dce110_opp *opp110, const struct bit_depth_reduction_params *params)

    1) set truncation depth: 0 for 18 bpp or 1 for 24 bpp 2) enable truncation 3) HW remove 12bit FMT support for DCE11 power saving reason.

    :param opp110:
        *undescribed*
    :type opp110: struct dce110_opp \*

    :param params:
        *undescribed*
    :type params: const struct bit_depth_reduction_params \*

.. _`set_spatial_dither`:

set_spatial_dither
==================

.. c:function:: void set_spatial_dither(struct dce110_opp *opp110, const struct bit_depth_reduction_params *params)

    1) set spatial dithering mode: pattern of seed 2) set spatial dithering depth: 0 for 18bpp or 1 for 24bpp 3) set random seed 4) set random mode lfsr is reset every frame or not reset RGB dithering method 0: RGB data are all dithered with x^28+x^3+1 1: R data is dithered with x^28+x^3+1 G data is dithered with x^28+X^9+1 B data is dithered with x^28+x^13+1 enable high pass filter or not 5) enable spatical dithering

    :param opp110:
        *undescribed*
    :type opp110: struct dce110_opp \*

    :param params:
        *undescribed*
    :type params: const struct bit_depth_reduction_params \*

.. _`set_temporal_dither`:

set_temporal_dither
===================

.. c:function:: void set_temporal_dither(struct dce110_opp *opp110, const struct bit_depth_reduction_params *params)

    1) set temporal dither depth 2) select pattern: from hard-coded pattern or programmable pattern 3) select optimized strips for BGR or RGB LCD sub-pixel 4) set s matrix 5) set t matrix 6) set grey level for 0.25, 0.5, 0.75 7) enable temporal dithering

    :param opp110:
        *undescribed*
    :type opp110: struct dce110_opp \*

    :param params:
        *undescribed*
    :type params: const struct bit_depth_reduction_params \*

.. _`dce110_opp_set_clamping`:

dce110_opp_set_clamping
=======================

.. c:function:: void dce110_opp_set_clamping(struct dce110_opp *opp110, const struct clamping_and_pixel_encoding_params *params)

    1) Set clamping format based on bpc - 0 for 6bpc (No clamping) 1 for 8 bpc 2 for 10 bpc 3 for 12 bpc 7 for programable 2) Enable clamp if Limited range requested

    :param opp110:
        *undescribed*
    :type opp110: struct dce110_opp \*

    :param params:
        *undescribed*
    :type params: const struct clamping_and_pixel_encoding_params \*

.. _`set_pixel_encoding`:

set_pixel_encoding
==================

.. c:function:: void set_pixel_encoding(struct dce110_opp *opp110, const struct clamping_and_pixel_encoding_params *params)

    :param opp110:
        *undescribed*
    :type opp110: struct dce110_opp \*

    :param params:
        *undescribed*
    :type params: const struct clamping_and_pixel_encoding_params \*

.. _`set_pixel_encoding.description`:

Description
-----------

Set Pixel Encoding
0: RGB 4:4:4 or YCbCr 4:4:4 or YOnly
1: YCbCr 4:2:2

.. This file was automatic generated / don't edit.

