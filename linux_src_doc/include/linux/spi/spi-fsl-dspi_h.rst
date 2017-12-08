.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/spi/spi-fsl-dspi.h

.. _`fsl_dspi_platform_data`:

struct fsl_dspi_platform_data
=============================

.. c:type:: struct fsl_dspi_platform_data

    platform data for the Freescale DSPI driver

.. _`fsl_dspi_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct fsl_dspi_platform_data {
        u32 cs_num;
        u32 bus_num;
        u32 sck_cs_delay;
        u32 cs_sck_delay;
    }

.. _`fsl_dspi_platform_data.members`:

Members
-------

cs_num
    number of chip selects supported by this DSPI driver.

bus_num
    board specific identifier for this DSPI driver.

sck_cs_delay
    *undescribed*

cs_sck_delay
    *undescribed*

.. This file was automatic generated / don't edit.

