.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/iio/accel/lis3l02dq_ring.c

.. _`combine_8_to_16`:

combine_8_to_16
===============

.. c:function:: u16 combine_8_to_16(u8 lower, u8 upper)

    :param u8 lower:
        *undescribed*

    :param u8 upper:
        *undescribed*

.. _`lis3l02dq_data_rdy_trig_poll`:

lis3l02dq_data_rdy_trig_poll
============================

.. c:function:: irqreturn_t lis3l02dq_data_rdy_trig_poll(int irq, void *private)

    :param int irq:
        *undescribed*

    :param void \*private:
        *undescribed*

.. _`lis3l02dq_read_all`:

lis3l02dq_read_all
==================

.. c:function:: int lis3l02dq_read_all(struct iio_dev *indio_dev, u8 *rx_array)

    :param struct iio_dev \*indio_dev:
        IIO device state

    :param u8 \*rx_array:
        (dma capable) receive array, must be at least
        4\*number of channels

.. _`lis3l02dq_data_rdy_trigger_set_state`:

lis3l02dq_data_rdy_trigger_set_state
====================================

.. c:function:: int lis3l02dq_data_rdy_trigger_set_state(struct iio_trigger *trig, bool state)

    :param struct iio_trigger \*trig:
        *undescribed*

    :param bool state:
        *undescribed*

.. _`lis3l02dq_data_rdy_trigger_set_state.description`:

Description
-----------

If disabling the interrupt also does a final read to ensure it is clear.
This is only important in some cases where the scan enable elements are
switched before the buffer is reenabled.

.. _`lis3l02dq_trig_try_reen`:

lis3l02dq_trig_try_reen
=======================

.. c:function:: int lis3l02dq_trig_try_reen(struct iio_trigger *trig)

    :param struct iio_trigger \*trig:
        the datardy trigger

.. This file was automatic generated / don't edit.

