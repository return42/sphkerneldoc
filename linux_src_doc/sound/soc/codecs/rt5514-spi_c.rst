.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/codecs/rt5514-spi.c

.. _`rt5514_spi_burst_read`:

rt5514_spi_burst_read
=====================

.. c:function:: int rt5514_spi_burst_read(unsigned int addr, u8 *rxbuf, size_t len)

    Read data from SPI by rt5514 address.

    :param unsigned int addr:
        Start address.

    :param u8 \*rxbuf:
        Data Buffer for reading.

    :param size_t len:
        Data length, it must be a multiple of 8.

.. _`rt5514_spi_burst_read.description`:

Description
-----------


Returns true for success.

.. _`rt5514_spi_burst_write`:

rt5514_spi_burst_write
======================

.. c:function:: int rt5514_spi_burst_write(u32 addr, const u8 *txbuf, size_t len)

    Write data to SPI by rt5514 address.

    :param u32 addr:
        Start address.

    :param const u8 \*txbuf:
        Data Buffer for writng.

    :param size_t len:
        Data length, it must be a multiple of 8.

.. _`rt5514_spi_burst_write.description`:

Description
-----------


Returns true for success.

.. This file was automatic generated / don't edit.

