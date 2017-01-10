.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/soc/tegra/pmc.h

.. _`tegra_io_pad`:

enum tegra_io_pad
=================

.. c:type:: enum tegra_io_pad

    I/O pad group identifier

.. _`tegra_io_pad.definition`:

Definition
----------

.. code-block:: c

    enum tegra_io_pad {
        TEGRA_IO_PAD_AUDIO,
        TEGRA_IO_PAD_AUDIO_HV,
        TEGRA_IO_PAD_BB,
        TEGRA_IO_PAD_CAM,
        TEGRA_IO_PAD_COMP,
        TEGRA_IO_PAD_CSIA,
        TEGRA_IO_PAD_CSIB,
        TEGRA_IO_PAD_CSIC,
        TEGRA_IO_PAD_CSID,
        TEGRA_IO_PAD_CSIE,
        TEGRA_IO_PAD_CSIF,
        TEGRA_IO_PAD_DBG,
        TEGRA_IO_PAD_DEBUG_NONAO,
        TEGRA_IO_PAD_DMIC,
        TEGRA_IO_PAD_DP,
        TEGRA_IO_PAD_DSI,
        TEGRA_IO_PAD_DSIB,
        TEGRA_IO_PAD_DSIC,
        TEGRA_IO_PAD_DSID,
        TEGRA_IO_PAD_EMMC,
        TEGRA_IO_PAD_EMMC2,
        TEGRA_IO_PAD_GPIO,
        TEGRA_IO_PAD_HDMI,
        TEGRA_IO_PAD_HSIC,
        TEGRA_IO_PAD_HV,
        TEGRA_IO_PAD_LVDS,
        TEGRA_IO_PAD_MIPI_BIAS,
        TEGRA_IO_PAD_NAND,
        TEGRA_IO_PAD_PEX_BIAS,
        TEGRA_IO_PAD_PEX_CLK1,
        TEGRA_IO_PAD_PEX_CLK2,
        TEGRA_IO_PAD_PEX_CNTRL,
        TEGRA_IO_PAD_SDMMC1,
        TEGRA_IO_PAD_SDMMC3,
        TEGRA_IO_PAD_SDMMC4,
        TEGRA_IO_PAD_SPI,
        TEGRA_IO_PAD_SPI_HV,
        TEGRA_IO_PAD_SYS_DDC,
        TEGRA_IO_PAD_UART,
        TEGRA_IO_PAD_USB0,
        TEGRA_IO_PAD_USB1,
        TEGRA_IO_PAD_USB2,
        TEGRA_IO_PAD_USB3,
        TEGRA_IO_PAD_USB_BIAS
    };

.. _`tegra_io_pad.constants`:

Constants
---------

TEGRA_IO_PAD_AUDIO
    *undescribed*

TEGRA_IO_PAD_AUDIO_HV
    *undescribed*

TEGRA_IO_PAD_BB
    *undescribed*

TEGRA_IO_PAD_CAM
    *undescribed*

TEGRA_IO_PAD_COMP
    *undescribed*

TEGRA_IO_PAD_CSIA
    *undescribed*

TEGRA_IO_PAD_CSIB
    *undescribed*

TEGRA_IO_PAD_CSIC
    *undescribed*

TEGRA_IO_PAD_CSID
    *undescribed*

TEGRA_IO_PAD_CSIE
    *undescribed*

TEGRA_IO_PAD_CSIF
    *undescribed*

TEGRA_IO_PAD_DBG
    *undescribed*

TEGRA_IO_PAD_DEBUG_NONAO
    *undescribed*

TEGRA_IO_PAD_DMIC
    *undescribed*

TEGRA_IO_PAD_DP
    *undescribed*

TEGRA_IO_PAD_DSI
    *undescribed*

TEGRA_IO_PAD_DSIB
    *undescribed*

TEGRA_IO_PAD_DSIC
    *undescribed*

TEGRA_IO_PAD_DSID
    *undescribed*

TEGRA_IO_PAD_EMMC
    *undescribed*

TEGRA_IO_PAD_EMMC2
    *undescribed*

TEGRA_IO_PAD_GPIO
    *undescribed*

TEGRA_IO_PAD_HDMI
    *undescribed*

TEGRA_IO_PAD_HSIC
    *undescribed*

TEGRA_IO_PAD_HV
    *undescribed*

TEGRA_IO_PAD_LVDS
    *undescribed*

TEGRA_IO_PAD_MIPI_BIAS
    *undescribed*

TEGRA_IO_PAD_NAND
    *undescribed*

TEGRA_IO_PAD_PEX_BIAS
    *undescribed*

TEGRA_IO_PAD_PEX_CLK1
    *undescribed*

TEGRA_IO_PAD_PEX_CLK2
    *undescribed*

TEGRA_IO_PAD_PEX_CNTRL
    *undescribed*

TEGRA_IO_PAD_SDMMC1
    *undescribed*

TEGRA_IO_PAD_SDMMC3
    *undescribed*

TEGRA_IO_PAD_SDMMC4
    *undescribed*

TEGRA_IO_PAD_SPI
    *undescribed*

TEGRA_IO_PAD_SPI_HV
    *undescribed*

TEGRA_IO_PAD_SYS_DDC
    *undescribed*

TEGRA_IO_PAD_UART
    *undescribed*

TEGRA_IO_PAD_USB0
    *undescribed*

TEGRA_IO_PAD_USB1
    *undescribed*

TEGRA_IO_PAD_USB2
    *undescribed*

TEGRA_IO_PAD_USB3
    *undescribed*

TEGRA_IO_PAD_USB_BIAS
    *undescribed*

.. _`tegra_io_pad.description`:

Description
-----------

I/O pins on Tegra SoCs are grouped into so-called I/O pads. Each such pad
can be used to control the common voltage signal level and power state of
the pins of the given pad.

.. _`tegra_io_pad_voltage`:

enum tegra_io_pad_voltage
=========================

.. c:type:: enum tegra_io_pad_voltage

    voltage level of the I/O pad's source rail

.. _`tegra_io_pad_voltage.definition`:

Definition
----------

.. code-block:: c

    enum tegra_io_pad_voltage {
        TEGRA_IO_PAD_1800000UV,
        TEGRA_IO_PAD_3300000UV
    };

.. _`tegra_io_pad_voltage.constants`:

Constants
---------

TEGRA_IO_PAD_1800000UV
    1.8 V

TEGRA_IO_PAD_3300000UV
    3.3 V

.. This file was automatic generated / don't edit.

