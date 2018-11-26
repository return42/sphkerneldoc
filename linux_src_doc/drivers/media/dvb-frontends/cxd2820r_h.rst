.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/dvb-frontends/cxd2820r.h

.. _`cxd2820r_platform_data`:

struct cxd2820r_platform_data
=============================

.. c:type:: struct cxd2820r_platform_data

    Platform data for the cxd2820r driver

.. _`cxd2820r_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct cxd2820r_platform_data {
        u8 ts_mode;
        bool ts_clk_inv;
        bool if_agc_polarity;
        bool spec_inv;
        int **gpio_chip_base;
        struct dvb_frontend* (*get_dvb_frontend)(struct i2c_client *);
    }

.. _`cxd2820r_platform_data.members`:

Members
-------

ts_mode
    TS mode.

ts_clk_inv
    TS clock inverted.

if_agc_polarity
    IF AGC polarity.

spec_inv
    Input spectrum inverted.

gpio_chip_base
    GPIO.

get_dvb_frontend
    Get DVB frontend.

.. _`cxd2820r_config`:

struct cxd2820r_config
======================

.. c:type:: struct cxd2820r_config

    configuration for cxd2020r demod

.. _`cxd2820r_config.definition`:

Definition
----------

.. code-block:: c

    struct cxd2820r_config {
        u8 i2c_address;
        u8 ts_mode;
        bool ts_clock_inv;
        bool if_agc_polarity;
        bool spec_inv;
    }

.. _`cxd2820r_config.members`:

Members
-------

i2c_address
    Demodulator I2C address. Driver determines DVB-C slave I2C
    address automatically from master address.
    Default: none, must set. Values: 0x6c, 0x6d.

ts_mode
    TS output mode. Default: none, must set. Values: FIXME?

ts_clock_inv
    TS clock inverted. Default: 0. Values: 0, 1.

if_agc_polarity
    Default: 0. Values: 0, 1

spec_inv
    Spectrum inversion. Default: 0. Values: 0, 1.

.. _`cxd2820r_attach`:

cxd2820r_attach
===============

.. c:function:: struct dvb_frontend *cxd2820r_attach(const struct cxd2820r_config *config, struct i2c_adapter *i2c, int *gpio_chip_base)

    :param config:
        pointer to \ :c:type:`struct cxd2820r_config <cxd2820r_config>`\  with demod configuration.
    :type config: const struct cxd2820r_config \*

    :param i2c:
        i2c adapter to use.
    :type i2c: struct i2c_adapter \*

    :param gpio_chip_base:
        if zero, disables GPIO setting. Otherwise, if
        CONFIG_GPIOLIB is set dynamically allocate
        gpio base; if is not set, use its value to
        setup the GPIO pins.
    :type gpio_chip_base: int \*

.. _`cxd2820r_attach.return`:

Return
------

FE pointer on success, NULL on failure.

.. This file was automatic generated / don't edit.

