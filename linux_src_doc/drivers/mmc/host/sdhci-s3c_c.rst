.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/host/sdhci-s3c.c

.. _`sdhci_s3c`:

struct sdhci_s3c
================

.. c:type:: struct sdhci_s3c

    S3C SDHCI instance

.. _`sdhci_s3c.definition`:

Definition
----------

.. code-block:: c

    struct sdhci_s3c {
        struct sdhci_host *host;
        struct platform_device *pdev;
        struct resource *ioarea;
        struct s3c_sdhci_platdata *pdata;
        int cur_clk;
        int ext_cd_irq;
        int ext_cd_gpio;
        struct clk *clk_io;
        struct clk  *clk_bus;
        unsigned long clk_rates;
        bool no_divider;
    }

.. _`sdhci_s3c.members`:

Members
-------

host
    The SDHCI host created

pdev
    The platform device we where created from.

ioarea
    The resource created when we claimed the IO area.

pdata
    The platform data for this controller.

cur_clk
    The index of the current bus clock.

ext_cd_irq
    *undescribed*

ext_cd_gpio
    *undescribed*

clk_io
    The clock for the internal bus interface.

clk_bus
    The clocks that are available for the SD/MMC bus clock.

clk_rates
    *undescribed*

no_divider
    *undescribed*

.. _`sdhci_s3c_drv_data`:

struct sdhci_s3c_drv_data
=========================

.. c:type:: struct sdhci_s3c_drv_data

    S3C SDHCI platform specific driver data

.. _`sdhci_s3c_drv_data.definition`:

Definition
----------

.. code-block:: c

    struct sdhci_s3c_drv_data {
        unsigned int sdhci_quirks;
        bool no_divider;
    }

.. _`sdhci_s3c_drv_data.members`:

Members
-------

sdhci_quirks
    sdhci host specific quirks.

no_divider
    *undescribed*

.. _`sdhci_s3c_drv_data.description`:

Description
-----------

Specifies platform specific configuration of sdhci controller.

.. _`sdhci_s3c_drv_data.note`:

Note
----

A structure for driver specific platform data is used for future
expansion of its usage.

.. _`sdhci_s3c_get_max_clk`:

sdhci_s3c_get_max_clk
=====================

.. c:function:: unsigned int sdhci_s3c_get_max_clk(struct sdhci_host *host)

    callback to get maximum clock frequency.

    :param struct sdhci_host \*host:
        The SDHCI host instance.

.. _`sdhci_s3c_get_max_clk.description`:

Description
-----------

Callback to return the maximum clock rate acheivable by the controller.

.. _`sdhci_s3c_consider_clock`:

sdhci_s3c_consider_clock
========================

.. c:function:: unsigned int sdhci_s3c_consider_clock(struct sdhci_s3c *ourhost, unsigned int src, unsigned int wanted)

    consider one the bus clocks for current setting

    :param struct sdhci_s3c \*ourhost:
        Our SDHCI instance.

    :param unsigned int src:
        The source clock index.

    :param unsigned int wanted:
        The clock frequency wanted.

.. _`sdhci_s3c_set_clock`:

sdhci_s3c_set_clock
===================

.. c:function:: void sdhci_s3c_set_clock(struct sdhci_host *host, unsigned int clock)

    callback on clock change

    :param struct sdhci_host \*host:
        The SDHCI host being changed

    :param unsigned int clock:
        The clock rate being requested.

.. _`sdhci_s3c_set_clock.description`:

Description
-----------

When the card's clock is going to be changed, look at the new frequency
and find the best clock source to go with it.

.. _`sdhci_s3c_get_min_clock`:

sdhci_s3c_get_min_clock
=======================

.. c:function:: unsigned int sdhci_s3c_get_min_clock(struct sdhci_host *host)

    callback to get minimal supported clock value

    :param struct sdhci_host \*host:
        The SDHCI host being queried

.. _`sdhci_s3c_get_min_clock.description`:

Description
-----------

To init mmc host properly a minimal clock value is needed. For high system
bus clock's values the standard formula gives values out of allowed range.
The clock still can be set to lower values, if clock source other then
system bus is selected.

.. _`sdhci_s3c_set_bus_width`:

sdhci_s3c_set_bus_width
=======================

.. c:function:: void sdhci_s3c_set_bus_width(struct sdhci_host *host, int width)

    support 8bit buswidth

    :param struct sdhci_host \*host:
        The SDHCI host being queried

    :param int width:
        MMC_BUS_WIDTH\_ macro for the bus width being requested

.. _`sdhci_s3c_set_bus_width.description`:

Description
-----------

We have 8-bit width support but is not a v3 controller.
So we add \ :c:func:`platform_bus_width`\  and support 8bit width.

.. This file was automatic generated / don't edit.

