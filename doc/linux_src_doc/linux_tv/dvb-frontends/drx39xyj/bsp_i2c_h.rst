.. -*- coding: utf-8; mode: rst -*-

=========
bsp_i2c.h
=========



.. _xref_drxbsp_i2c_write_read:

drxbsp_i2c_write_read
=====================

.. c:function:: drx_status_t drxbsp_i2c_write_read (struct i2c_device_addr * w_dev_addr, u16 w_count, u8 * w_data, struct i2c_device_addr * r_dev_addr, u16 r_count, u8 * r_data)

    

    :param struct i2c_device_addr * w_dev_addr:

        _undescribed_

    :param u16 w_count:

        _undescribed_

    :param u8 * w_data:

        _undescribed_

    :param struct i2c_device_addr * r_dev_addr:

        _undescribed_

    :param u16 r_count:

        _undescribed_

    :param u8 * r_data:

        _undescribed_



Description
-----------

                                      u16 w_count,
                                      u8 *wData,
                                      struct i2c_device_addr *r_dev_addr,
                                      u16 r_count,
                                      u8 *r_data)
\brief Read and/or write count bytes from I2C bus, store them in data[].
\param w_dev_addr The device i2c address and the device ID to write to
\param w_count   The number of bytes to write
\param wData    The array to write the data to
\param r_dev_addr The device i2c address and the device ID to read from
\param r_count   The number of bytes to read
\param r_data    The array to read the data from
\return drx_status_t Return status.
\retval 0 Succes.
\retval -EIO Failure.
\retval -EINVAL Parameter 'wcount' is not zero but parameter
                                      'wdata' contains NULL.
                                      Idem for 'rcount' and 'rdata'.
                                      Both w_dev_addr and r_dev_addr are NULL.


This function must implement an atomic write and/or read action on the I2C bus
No other process may use the I2C bus when this function is executing.
The critical section of this function runs from and including the I2C
write, up to and including the I2C read action.


The device ID can be useful if several devices share an I2C address.
It can be used to control a "switch" on the I2C bus to the correct device.


