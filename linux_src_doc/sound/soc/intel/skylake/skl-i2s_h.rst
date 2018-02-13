.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/intel/skylake/skl-i2s.h

.. _`skl_i2s_config_blob_legacy`:

struct skl_i2s_config_blob_legacy
=================================

.. c:type:: struct skl_i2s_config_blob_legacy

    Structure defines I2S Gateway configuration legacy blob

.. _`skl_i2s_config_blob_legacy.definition`:

Definition
----------

.. code-block:: c

    struct skl_i2s_config_blob_legacy {
        u32 gtw_attr;
        u32 tdm_ts_group[SKL_I2S_MAX_TIME_SLOTS];
        struct skl_i2s_config i2s_cfg;
        struct skl_i2s_config_mclk mclk;
    }

.. _`skl_i2s_config_blob_legacy.members`:

Members
-------

gtw_attr
    Gateway attribute for the I2S Gateway

tdm_ts_group
    TDM slot mapping against channels in the Gateway.

i2s_cfg
    I2S HW registers

mclk
    MCLK clock source and divider values

.. This file was automatic generated / don't edit.

