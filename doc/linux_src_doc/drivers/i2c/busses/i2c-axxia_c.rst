.. -*- coding: utf-8; mode: rst -*-

===========
i2c-axxia.c
===========


.. _`ns_to_clk`:

ns_to_clk
=========

.. c:function:: u32 ns_to_clk (u64 ns, u32 clk_mhz)

    Convert time (ns) to clock cycles for the given clock frequency.

    :param u64 ns:

        *undescribed*

    :param u32 clk_mhz:

        *undescribed*



.. _`axxia_i2c_empty_rx_fifo`:

axxia_i2c_empty_rx_fifo
=======================

.. c:function:: int axxia_i2c_empty_rx_fifo (struct axxia_i2c_dev *idev)

    Fetch data from RX FIFO and update SMBus block transfer length if this is the first byte of such a transfer.

    :param struct axxia_i2c_dev \*idev:

        *undescribed*



.. _`axxia_i2c_fill_tx_fifo`:

axxia_i2c_fill_tx_fifo
======================

.. c:function:: int axxia_i2c_fill_tx_fifo (struct axxia_i2c_dev *idev)

    Fill TX FIFO from current message buffer.

    :param struct axxia_i2c_dev \*idev:

        *undescribed*

