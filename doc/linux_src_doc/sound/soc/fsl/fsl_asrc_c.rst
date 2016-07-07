.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/fsl/fsl_asrc.c

.. _`fsl_asrc_request_pair`:

fsl_asrc_request_pair
=====================

.. c:function:: int fsl_asrc_request_pair(int channels, struct fsl_asrc_pair *pair)

    :param int channels:
        *undescribed*

    :param struct fsl_asrc_pair \*pair:
        *undescribed*

.. _`fsl_asrc_request_pair.description`:

Description
-----------

It assigns pair by the order of A->C->B because allocation of pair B,
within range [ANCA, ANCA+ANCB-1], depends on the channels of pair A
while pair A and pair C are comparatively independent.

.. _`fsl_asrc_release_pair`:

fsl_asrc_release_pair
=====================

.. c:function:: void fsl_asrc_release_pair(struct fsl_asrc_pair *pair)

    :param struct fsl_asrc_pair \*pair:
        *undescribed*

.. _`fsl_asrc_release_pair.description`:

Description
-----------

It clears the resource from asrc_priv and releases the occupied channels.

.. _`fsl_asrc_set_watermarks`:

fsl_asrc_set_watermarks
=======================

.. c:function:: void fsl_asrc_set_watermarks(struct fsl_asrc_pair *pair, u32 in, u32 out)

    :param struct fsl_asrc_pair \*pair:
        *undescribed*

    :param u32 in:
        *undescribed*

    :param u32 out:
        *undescribed*

.. _`fsl_asrc_cal_asrck_divisor`:

fsl_asrc_cal_asrck_divisor
==========================

.. c:function:: u32 fsl_asrc_cal_asrck_divisor(struct fsl_asrc_pair *pair, u32 div)

    :param struct fsl_asrc_pair \*pair:
        *undescribed*

    :param u32 div:
        *undescribed*

.. _`fsl_asrc_cal_asrck_divisor.description`:

Description
-----------

It follows the formula clk_rate = samplerate \* (2 ^ prescaler) \* divider

.. _`fsl_asrc_set_ideal_ratio`:

fsl_asrc_set_ideal_ratio
========================

.. c:function:: int fsl_asrc_set_ideal_ratio(struct fsl_asrc_pair *pair, int inrate, int outrate)

    :param struct fsl_asrc_pair \*pair:
        *undescribed*

    :param int inrate:
        *undescribed*

    :param int outrate:
        *undescribed*

.. _`fsl_asrc_set_ideal_ratio.description`:

Description
-----------

The ratio is a 32-bit fixed point value with 26 fractional bits.

.. _`fsl_asrc_config_pair`:

fsl_asrc_config_pair
====================

.. c:function:: int fsl_asrc_config_pair(struct fsl_asrc_pair *pair)

    :param struct fsl_asrc_pair \*pair:
        *undescribed*

.. _`fsl_asrc_config_pair.description`:

Description
-----------

It configures those ASRC registers according to a configuration instance
of struct asrc_config which includes in/output sample rate, width, channel
and clock settings.

.. _`fsl_asrc_start_pair`:

fsl_asrc_start_pair
===================

.. c:function:: void fsl_asrc_start_pair(struct fsl_asrc_pair *pair)

    :param struct fsl_asrc_pair \*pair:
        *undescribed*

.. _`fsl_asrc_start_pair.description`:

Description
-----------

It enables the assigned pair and makes it stopped at the stall level.

.. _`fsl_asrc_stop_pair`:

fsl_asrc_stop_pair
==================

.. c:function:: void fsl_asrc_stop_pair(struct fsl_asrc_pair *pair)

    :param struct fsl_asrc_pair \*pair:
        *undescribed*

.. _`fsl_asrc_get_dma_channel`:

fsl_asrc_get_dma_channel
========================

.. c:function:: struct dma_chan *fsl_asrc_get_dma_channel(struct fsl_asrc_pair *pair, bool dir)

    :param struct fsl_asrc_pair \*pair:
        *undescribed*

    :param bool dir:
        *undescribed*

.. _`fsl_asrc_init`:

fsl_asrc_init
=============

.. c:function:: int fsl_asrc_init(struct fsl_asrc *asrc_priv)

    :param struct fsl_asrc \*asrc_priv:
        *undescribed*

.. _`fsl_asrc_isr`:

fsl_asrc_isr
============

.. c:function:: irqreturn_t fsl_asrc_isr(int irq, void *dev_id)

    :param int irq:
        *undescribed*

    :param void \*dev_id:
        *undescribed*

.. This file was automatic generated / don't edit.

