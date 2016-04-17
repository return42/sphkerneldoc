.. -*- coding: utf-8; mode: rst -*-

==========
fbtft-io.c
==========


.. _`fbtft_write_spi_emulate_9`:

fbtft_write_spi_emulate_9
=========================

.. c:function:: int fbtft_write_spi_emulate_9 (struct fbtft_par *par, void *buf, size_t len)

    write SPI emulating 9-bit

    :param struct fbtft_par \*par:
        Driver data

    :param void \*buf:
        Buffer to write

    :param size_t len:
        Length of buffer (must be divisible by 8)



.. _`fbtft_write_spi_emulate_9.description`:

Description
-----------

When 9-bit SPI is not available, this function can be used to emulate that.
par->extra must hold a transformation buffer used for transfer.

