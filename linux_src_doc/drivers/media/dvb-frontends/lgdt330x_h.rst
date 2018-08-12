.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/dvb-frontends/lgdt330x.h

.. _`lgdt330x_config`:

struct lgdt330x_config
======================

.. c:type:: struct lgdt330x_config

    contains lgdt330x configuration

.. _`lgdt330x_config.definition`:

Definition
----------

.. code-block:: c

    struct lgdt330x_config {
        lg_chip_type demod_chip;
        int serial_mpeg;
        int (*pll_rf_set) (struct dvb_frontend* fe, int index);
        int (*set_ts_params)(struct dvb_frontend* fe, int is_punctured);
        int clock_polarity_flip;
        struct dvb_frontend* (*get_dvb_frontend)(struct i2c_client *);
    }

.. _`lgdt330x_config.members`:

Members
-------

demod_chip
    LG demodulator chip LGDT3302 or LGDT3303

serial_mpeg
    MPEG hardware interface - 0:parallel 1:serial

pll_rf_set
    Callback function to set PLL interface

set_ts_params
    Callback function to set device param for start_dma

clock_polarity_flip
    Flip the polarity of the mpeg data transfer clock using alternate
    init data.
    This option applies ONLY to LGDT3303 - 0:disabled (default) 1:enabled

get_dvb_frontend
    returns the frontend associated with this I2C client.
    Filled by the driver.

.. This file was automatic generated / don't edit.

