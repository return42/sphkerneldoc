.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/media/camera-mx3.h

.. _`mx3_camera_pdata`:

struct mx3_camera_pdata
=======================

.. c:type:: struct mx3_camera_pdata

    i.MX3x camera platform data

.. _`mx3_camera_pdata.definition`:

Definition
----------

.. code-block:: c

    struct mx3_camera_pdata {
        unsigned long flags;
        unsigned long mclk_10khz;
        struct device *dma_dev;
        struct v4l2_async_subdev **asd;
        int *asd_sizes;
    }

.. _`mx3_camera_pdata.members`:

Members
-------

flags
    MX3_CAMERA\_\* flags

mclk_10khz
    master clock frequency in 10kHz units

dma_dev
    IPU DMA device to match against in channel allocation

asd
    *undescribed*

asd_sizes
    *undescribed*

.. This file was automatic generated / don't edit.

