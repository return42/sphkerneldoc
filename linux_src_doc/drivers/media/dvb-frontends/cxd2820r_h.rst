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
        bool attach_in_use;
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

attach_in_use
    *undescribed*

.. This file was automatic generated / don't edit.

