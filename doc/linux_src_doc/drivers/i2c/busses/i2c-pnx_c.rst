.. -*- coding: utf-8; mode: rst -*-

=========
i2c-pnx.c
=========


.. _`i2c_pnx_start`:

i2c_pnx_start
=============

.. c:function:: int i2c_pnx_start (unsigned char slave_addr, struct i2c_pnx_algo_data *alg_data)

    start a device

    :param unsigned char slave_addr:
        slave address

    :param struct i2c_pnx_algo_data \*alg_data:

        *undescribed*



.. _`i2c_pnx_start.description`:

Description
-----------

Generate a START signal in the desired mode.



.. _`i2c_pnx_stop`:

i2c_pnx_stop
============

.. c:function:: void i2c_pnx_stop (struct i2c_pnx_algo_data *alg_data)

    stop a device

    :param struct i2c_pnx_algo_data \*alg_data:

        *undescribed*



.. _`i2c_pnx_stop.description`:

Description
-----------

Generate a STOP signal to terminate the master transaction.



.. _`i2c_pnx_master_xmit`:

i2c_pnx_master_xmit
===================

.. c:function:: int i2c_pnx_master_xmit (struct i2c_pnx_algo_data *alg_data)

    transmit data to slave

    :param struct i2c_pnx_algo_data \*alg_data:

        *undescribed*



.. _`i2c_pnx_master_xmit.description`:

Description
-----------

Sends one byte of data to the slave



.. _`i2c_pnx_master_rcv`:

i2c_pnx_master_rcv
==================

.. c:function:: int i2c_pnx_master_rcv (struct i2c_pnx_algo_data *alg_data)

    receive data from slave

    :param struct i2c_pnx_algo_data \*alg_data:

        *undescribed*



.. _`i2c_pnx_master_rcv.description`:

Description
-----------

Reads one byte data from the slave



.. _`i2c_pnx_xfer`:

i2c_pnx_xfer
============

.. c:function:: int i2c_pnx_xfer (struct i2c_adapter *adap, struct i2c_msg *msgs, int num)

    generic transfer entry point

    :param struct i2c_adapter \*adap:
        pointer to I2C adapter structure

    :param struct i2c_msg \*msgs:
        array of messages

    :param int num:
        number of messages



.. _`i2c_pnx_xfer.description`:

Description
-----------

Initiates the transfer

