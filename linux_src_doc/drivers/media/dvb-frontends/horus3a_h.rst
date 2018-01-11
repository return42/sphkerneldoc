.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/dvb-frontends/horus3a.h

.. _`horus3a_config`:

struct horus3a_config
=====================

.. c:type:: struct horus3a_config

    the configuration of Horus3A tuner driver

.. _`horus3a_config.definition`:

Definition
----------

.. code-block:: c

    struct horus3a_config {
        u8 i2c_address;
        u8 xtal_freq_mhz;
        void *set_tuner_priv;
        int (*set_tuner_callback)(void *, int);
    }

.. _`horus3a_config.members`:

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

.. _`horus3a_attach`:

horus3a_attach
==============

.. c:function:: struct dvb_frontend *horus3a_attach(struct dvb_frontend *fe, const struct horus3a_config *config, struct i2c_adapter *i2c)

    :param struct dvb_frontend \*fe:
        frontend to be attached

    :param const struct horus3a_config \*config:
        pointer to \ :c:type:`struct helene_config <helene_config>`\  with tuner configuration.

    :param struct i2c_adapter \*i2c:
        i2c adapter to use.

.. _`horus3a_attach.return`:

Return
------

FE pointer on success, NULL on failure.

.. This file was automatic generated / don't edit.

