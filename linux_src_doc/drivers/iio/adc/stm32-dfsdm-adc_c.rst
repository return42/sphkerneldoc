.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/adc/stm32-dfsdm-adc.c

.. _`stm32_dfsdm_get_buff_cb`:

stm32_dfsdm_get_buff_cb
=======================

.. c:function:: int stm32_dfsdm_get_buff_cb(struct iio_dev *iio_dev, int (*cb)(const void *data, size_t size, void *private), void *private)

    register a callback that will be called when DMA transfer period is achieved.

    :param struct iio_dev \*iio_dev:
        Handle to IIO device.

    :param int (\*cb)(const void \*data, size_t size, void \*private):
        Pointer to callback function:
        - data: pointer to data buffer
        - size: size in byte of the data buffer
        - private: pointer to consumer private structure.

    :param void \*private:
        Pointer to consumer private structure.

.. _`stm32_dfsdm_release_buff_cb`:

stm32_dfsdm_release_buff_cb
===========================

.. c:function:: int stm32_dfsdm_release_buff_cb(struct iio_dev *iio_dev)

    unregister buffer callback

    :param struct iio_dev \*iio_dev:
        Handle to IIO device.

.. This file was automatic generated / don't edit.

