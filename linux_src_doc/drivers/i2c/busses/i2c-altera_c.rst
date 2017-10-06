.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-altera.c

.. _`altr_i2c_transfer`:

altr_i2c_transfer
=================

.. c:function:: void altr_i2c_transfer(struct altr_i2c_dev *idev, u32 data)

    On the last byte to be transmitted, send a Stop bit on the last byte.

    :param struct altr_i2c_dev \*idev:
        *undescribed*

    :param u32 data:
        *undescribed*

.. _`altr_i2c_empty_rx_fifo`:

altr_i2c_empty_rx_fifo
======================

.. c:function:: void altr_i2c_empty_rx_fifo(struct altr_i2c_dev *idev)

    Fetch data from RX FIFO until end of transfer. Send a Stop bit on the last byte.

    :param struct altr_i2c_dev \*idev:
        *undescribed*

.. _`altr_i2c_fill_tx_fifo`:

altr_i2c_fill_tx_fifo
=====================

.. c:function:: int altr_i2c_fill_tx_fifo(struct altr_i2c_dev *idev)

    Fill TX FIFO from current message buffer.

    :param struct altr_i2c_dev \*idev:
        *undescribed*

.. This file was automatic generated / don't edit.

