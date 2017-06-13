.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/intel-spi.h

.. _`intel_spi_boardinfo`:

struct intel_spi_boardinfo
==========================

.. c:type:: struct intel_spi_boardinfo

    Board specific data for Intel SPI driver

.. _`intel_spi_boardinfo.definition`:

Definition
----------

.. code-block:: c

    struct intel_spi_boardinfo {
        enum intel_spi_type type;
        bool writeable;
    }

.. _`intel_spi_boardinfo.members`:

Members
-------

type
    Type which this controller is compatible with

writeable
    The chip is writeable

.. This file was automatic generated / don't edit.

