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
        enum pll_filter;
        int input_skew;
        int duallink_skew;
    }

.. _`sil164_encoder_params.members`:

Members
-------

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

