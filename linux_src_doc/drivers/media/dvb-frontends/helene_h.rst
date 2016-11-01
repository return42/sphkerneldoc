.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/dvb-frontends/helene.h

.. _`helene_config`:

struct helene_config
====================

.. c:type:: struct helene_config

    the configuration of 'Helene' tuner driver

.. _`helene_config.definition`:

Definition
----------

.. code-block:: c

    struct helene_config {
        u8 i2c_address;
        u8 xtal_freq_mhz;
        void *set_tuner_priv;
        int (*set_tuner_callback)(void *, int);
        enum helene_xtal xtal;
    }

.. _`helene_config.members`:

Members
-------

i2c_address
    I2C address of the tuner

xtal_freq_mhz
    Oscillator frequency, MHz

set_tuner_priv
    Callback function private context

set_tuner_callback
    Callback function that notifies the parent driver
    which tuner is active now

xtal
    *undescribed*

.. This file was automatic generated / don't edit.

