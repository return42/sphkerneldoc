.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/i2c/sil164.h

.. _`sil164_encoder_params`:

struct sil164_encoder_params
============================

.. c:type:: struct sil164_encoder_params


.. _`sil164_encoder_params.definition`:

Definition
----------

.. code-block:: c

    struct sil164_encoder_params {
        enum {
            SIL164_INPUT_EDGE_FALLING = 0,
            SIL164_INPUT_EDGE_RISING } input_edge;,
            enum {,
                SIL164_INPUT_WIDTH_12BIT = 0,
                SIL164_INPUT_WIDTH_24BIT } input_width;,
                enum {,
                    SIL164_INPUT_SINGLE_EDGE = 0,
                    SIL164_INPUT_DUAL_EDGE } input_dual;,
                    enum {,
                        SIL164_PLL_FILTER_ON = 0,
                        SIL164_PLL_FILTER_OFF,
                    } pll_filter;
                    int input_skew;,
                    int duallink_skew;,
    }

.. _`sil164_encoder_params.members`:

Members
-------

input_edge
    *undescribed*

input_width
    *undescribed*

input_dual
    *undescribed*

pll_filter
    *undescribed*

input_skew
    *undescribed*

duallink_skew
    *undescribed*

.. _`sil164_encoder_params.description`:

Description
-----------

Describes how the sil164 is connected to the GPU. It should be used
as the \ ``params``\  parameter of its \ ``set_config``\  method.

See "http://www.siliconimage.com/docs/SiI-DS-0021-E-164.pdf".

.. This file was automatic generated / don't edit.

