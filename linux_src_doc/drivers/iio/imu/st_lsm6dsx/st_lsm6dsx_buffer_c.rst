.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/imu/st_lsm6dsx/st_lsm6dsx_buffer.c

.. _`st_lsm6dsx_read_fifo`:

st_lsm6dsx_read_fifo
====================

.. c:function:: int st_lsm6dsx_read_fifo(struct st_lsm6dsx_hw *hw)

    LSM6DS3-LSM6DS3H-LSM6DSL-LSM6DSM read FIFO routine

    :param struct st_lsm6dsx_hw \*hw:
        Pointer to instance of struct st_lsm6dsx_hw.

.. _`st_lsm6dsx_read_fifo.description`:

Description
-----------

Read samples from the hw FIFO and push them to IIO buffers.

.. _`st_lsm6dsx_read_fifo.return`:

Return
------

Number of bytes read from the FIFO

.. This file was automatic generated / don't edit.

