.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/codecs/rt5514-spi.c

.. _`rt5514_spi_burst_read`:

rt5514_spi_burst_read
=====================

.. c:function:: int rt5514_spi_burst_read(unsigned int addr, u8 *rxbuf, size_t len)

    Read data from SPI by rt5514 address.

    :param addr:
        Start address.
    :type addr: unsigned int

    :param rxbuf:
        Data Buffer for reading.
    :type rxbuf: u8 \*

    :param len:
        Data length, it must be a multiple of 8.
    :type len: size_t

.. _`rt5514_spi_burst_read.description`:

Description
-----------


Returns true for success.

.. _`rt5514_spi_burst_write`:

rt5514_spi_burst_write
======================

.. c:function:: int rt5514_spi_burst_write(u32 addr, const u8 *txbuf, size_t len)

    Write data to SPI by rt5514 address.

    :param addr:
        Start address.
    :type addr: u32

    :param txbuf:
        Data Buffer for writng.
    :type txbuf: const u8 \*

    :param len:
        Data length, it must be a multiple of 8.
    :type len: size_t

.. _`rt5514_spi_burst_write.description`:

Description
-----------


Returns true for success.

.. This file was automatic generated / don't edit.

