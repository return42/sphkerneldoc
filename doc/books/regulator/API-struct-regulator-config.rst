.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-regulator-config:

=======================
struct regulator_config
=======================

*man struct regulator_config(9)*

*4.6.0-rc5*

Dynamic regulator descriptor


Synopsis
========

.. code-block:: c

    struct regulator_config {
      struct device * dev;
      const struct regulator_init_data * init_data;
      void * driver_data;
      struct device_node * of_node;
      struct regmap * regmap;
      bool ena_gpio_initialized;
      int ena_gpio;
      unsigned int ena_gpio_invert:1;
      unsigned int ena_gpio_flags;
    };


Members
=======

dev
    struct device for the regulator

init_data
    platform provided init data, passed through by driver

driver_data
    private regulator data

of_node
    OpenFirmware node to parse for device tree bindings (may be NULL).

regmap
    regmap to use for core regmap helpers if ``dev_get_regmap`` is
    insufficient.

ena_gpio_initialized
    GPIO controlling regulator enable was properly initialized, meaning
    that >= 0 is a valid gpio identifier and < 0 is a non existent gpio.

ena_gpio
    GPIO controlling regulator enable.

ena_gpio_invert
    Sense for GPIO enable control.

ena_gpio_flags
    Flags to use when calling ``gpio_request_one``


Description
===========

Each regulator registered with the core is described with a structure of
this type and a struct regulator_desc. This structure contains the
runtime variable parts of the regulator description.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
