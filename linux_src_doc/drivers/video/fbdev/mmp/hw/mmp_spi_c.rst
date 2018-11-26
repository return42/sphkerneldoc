.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/mmp/hw/mmp_spi.c

.. _`lcd_spi_write`:

lcd_spi_write
=============

.. c:function:: int lcd_spi_write(struct spi_device *spi, u32 data)

    write command to the SPI port

    :param spi:
        *undescribed*
    :type spi: struct spi_device \*

    :param data:
        can be 8/16/32-bit, MSB justified data to write.
    :type data: u32

.. _`lcd_spi_write.description`:

Description
-----------

Wait bus transfer complete IRQ.
The caller is expected to perform the necessary locking.

.. _`lcd_spi_write.return`:

Return
------

\ ``-ETIMEDOUT``\         timeout occurred
0                  success

.. This file was automatic generated / don't edit.

