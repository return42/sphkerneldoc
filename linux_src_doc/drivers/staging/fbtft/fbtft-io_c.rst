.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fbtft/fbtft-io.c

.. _`fbtft_write_spi_emulate_9`:

fbtft_write_spi_emulate_9
=========================

.. c:function:: int fbtft_write_spi_emulate_9(struct fbtft_par *par, void *buf, size_t len)

    write SPI emulating 9-bit

    :param par:
        Driver data
    :type par: struct fbtft_par \*

    :param buf:
        Buffer to write
    :type buf: void \*

    :param len:
        Length of buffer (must be divisible by 8)
    :type len: size_t

.. _`fbtft_write_spi_emulate_9.description`:

Description
-----------

When 9-bit SPI is not available, this function can be used to emulate that.
par->extra must hold a transformation buffer used for transfer.

.. This file was automatic generated / don't edit.

