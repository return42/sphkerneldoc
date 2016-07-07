.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/spi/spi-meson-spifc.c

.. _`meson_spifc`:

struct meson_spifc
==================

.. c:type:: struct meson_spifc


.. _`meson_spifc.definition`:

Definition
----------

.. code-block:: c

    struct meson_spifc {
        struct spi_master *master;
        struct regmap *regmap;
        struct clk *clk;
        struct device *dev;
    }

.. _`meson_spifc.members`:

Members
-------

master
    the SPI master

regmap
    regmap for device registers

clk
    input clock of the built-in baud rate generator

dev
    *undescribed*

.. _`meson_spifc_wait_ready`:

meson_spifc_wait_ready
======================

.. c:function:: int meson_spifc_wait_ready(struct meson_spifc *spifc)

    wait for the current operation to terminate

    :param struct meson_spifc \*spifc:
        the Meson SPI device

.. _`meson_spifc_wait_ready.return`:

Return
------

0 on success, a negative value on error

.. _`meson_spifc_drain_buffer`:

meson_spifc_drain_buffer
========================

.. c:function:: void meson_spifc_drain_buffer(struct meson_spifc *spifc, u8 *buf, int len)

    copy data from device buffer to memory

    :param struct meson_spifc \*spifc:
        the Meson SPI device

    :param u8 \*buf:
        the destination buffer

    :param int len:
        number of bytes to copy

.. _`meson_spifc_fill_buffer`:

meson_spifc_fill_buffer
=======================

.. c:function:: void meson_spifc_fill_buffer(struct meson_spifc *spifc, const u8 *buf, int len)

    copy data from memory to device buffer

    :param struct meson_spifc \*spifc:
        the Meson SPI device

    :param const u8 \*buf:
        the source buffer

    :param int len:
        number of bytes to copy

.. _`meson_spifc_setup_speed`:

meson_spifc_setup_speed
=======================

.. c:function:: void meson_spifc_setup_speed(struct meson_spifc *spifc, u32 speed)

    program the clock divider

    :param struct meson_spifc \*spifc:
        the Meson SPI device

    :param u32 speed:
        desired speed in Hz

.. _`meson_spifc_txrx`:

meson_spifc_txrx
================

.. c:function:: int meson_spifc_txrx(struct meson_spifc *spifc, struct spi_transfer *xfer, int offset, int len, bool last_xfer, bool last_chunk)

    transfer a chunk of data

    :param struct meson_spifc \*spifc:
        the Meson SPI device

    :param struct spi_transfer \*xfer:
        the current SPI transfer

    :param int offset:
        offset of the data to transfer

    :param int len:
        length of the data to transfer

    :param bool last_xfer:
        whether this is the last transfer of the message

    :param bool last_chunk:
        whether this is the last chunk of the transfer

.. _`meson_spifc_txrx.return`:

Return
------

0 on success, a negative value on error

.. _`meson_spifc_transfer_one`:

meson_spifc_transfer_one
========================

.. c:function:: int meson_spifc_transfer_one(struct spi_master *master, struct spi_device *spi, struct spi_transfer *xfer)

    perform a single transfer

    :param struct spi_master \*master:
        the SPI master

    :param struct spi_device \*spi:
        the SPI device

    :param struct spi_transfer \*xfer:
        the current SPI transfer

.. _`meson_spifc_transfer_one.return`:

Return
------

0 on success, a negative value on error

.. _`meson_spifc_hw_init`:

meson_spifc_hw_init
===================

.. c:function:: void meson_spifc_hw_init(struct meson_spifc *spifc)

    reset and initialize the SPI controller

    :param struct meson_spifc \*spifc:
        the Meson SPI device

.. This file was automatic generated / don't edit.

