.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ti/wlcore/spi.c

.. _`wl12xx_spi_set_power`:

wl12xx_spi_set_power
====================

.. c:function:: int wl12xx_spi_set_power(struct device *child, bool enable)

    power on/off the wl12xx unit

    :param child:
        wl12xx device handle.
    :type child: struct device \*

    :param enable:
        true/false to power on/off the unit.
    :type enable: bool

.. _`wl12xx_spi_set_power.description`:

Description
-----------

use the WiFi enable regulator to enable/disable the WiFi unit.

.. _`wl12xx_spi_set_block_size`:

wl12xx_spi_set_block_size
=========================

.. c:function:: void wl12xx_spi_set_block_size(struct device *child, unsigned int blksz)

    :param child:
        *undescribed*
    :type child: struct device \*

    :param blksz:
        *undescribed*
    :type blksz: unsigned int

.. _`wl12xx_spi_set_block_size.description`:

Description
-----------

This function is not needed for spi mode, but need to be present.
Without it defined the wlcore fallback to use the wrong packet
allignment on tx.

.. _`wlcore_probe_of`:

wlcore_probe_of
===============

.. c:function:: int wlcore_probe_of(struct spi_device *spi, struct wl12xx_spi_glue *glue, struct wlcore_platdev_data *pdev_data)

    DT node parsing.

    :param spi:
        SPI slave device parameters.
    :type spi: struct spi_device \*

    :param glue:
        wl12xx SPI bus to slave device glue parameters.
    :type glue: struct wl12xx_spi_glue \*

    :param pdev_data:
        wlcore device parameters
    :type pdev_data: struct wlcore_platdev_data \*

.. This file was automatic generated / don't edit.

