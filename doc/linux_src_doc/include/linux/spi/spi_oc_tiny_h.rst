.. -*- coding: utf-8; mode: rst -*-

=============
spi_oc_tiny.h
=============


.. _`tiny_spi_platform_data`:

struct tiny_spi_platform_data
=============================

.. c:type:: tiny_spi_platform_data

    platform data of the OpenCores tiny SPI


.. _`tiny_spi_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct tiny_spi_platform_data {
    unsigned int freq;
    unsigned int baudwidth;
    unsigned int gpio_cs_count;
    int * gpio_cs;
  };


.. _`tiny_spi_platform_data.members`:

Members
-------

:``freq``:
    input clock freq to the core.

:``baudwidth``:
    baud rate divider width of the core.

:``gpio_cs_count``:
    number of gpio pins used for chipselect.

:``gpio_cs``:
    array of gpio pins used for chipselect.




.. _`tiny_spi_platform_data.description`:

Description
-----------

freq and baudwidth are used only if the divider is programmable.

