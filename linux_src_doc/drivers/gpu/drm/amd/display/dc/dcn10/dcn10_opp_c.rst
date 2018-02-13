.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/display/dc/dcn10/dcn10_opp.c

.. _`opp1_set_truncation`:

opp1_set_truncation
===================

.. c:function:: void opp1_set_truncation(struct dcn10_opp *oppn10, const struct bit_depth_reduction_params *params)

    1) set truncation depth: 0 for 18 bpp or 1 for 24 bpp 2) enable truncation 3) HW remove 12bit FMT support for DCE11 power saving reason.

    :param struct dcn10_opp \*oppn10:
        *undescribed*

    :param const struct bit_depth_reduction_params \*params:
        *undescribed*

.. _`opp1_set_pixel_encoding`:

opp1_set_pixel_encoding
=======================

.. c:function:: void opp1_set_pixel_encoding(struct dcn10_opp *oppn10, const struct clamping_and_pixel_encoding_params *params)

    :param struct dcn10_opp \*oppn10:
        *undescribed*

    :param const struct clamping_and_pixel_encoding_params \*params:
        *undescribed*

.. _`opp1_set_pixel_encoding.description`:

Description
-----------

Set Pixel Encoding
0: RGB 4:4:4 or YCbCr 4:4:4 or YOnly
1: YCbCr 4:2:2

.. _`opp1_set_clamping`:

opp1_set_clamping
=================

.. c:function:: void opp1_set_clamping(struct dcn10_opp *oppn10, const struct clamping_and_pixel_encoding_params *params)

    1) Set clamping format based on bpc - 0 for 6bpc (No clamping) 1 for 8 bpc 2 for 10 bpc 3 for 12 bpc 7 for programable 2) Enable clamp if Limited range requested

    :param struct dcn10_opp \*oppn10:
        *undescribed*

    :param const struct clamping_and_pixel_encoding_params \*params:
        *undescribed*

.. This file was automatic generated / don't edit.

