.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/dvb-frontends/ascot2e.h

.. _`ascot2e_config`:

struct ascot2e_config
=====================

.. c:type:: struct ascot2e_config

    the configuration of Ascot2E tuner driver

.. _`ascot2e_config.definition`:

Definition
----------

.. code-block:: c

    struct ascot2e_config {
        u8 i2c_address;
        u8 xtal_freq_mhz;
        void *set_tuner_priv;
        int (*set_tuner_callback)(void *, int);
    }

.. _`ascot2e_config.members`:

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

.. _`ascot2e_attach`:

ascot2e_attach
==============

.. c:function:: struct dvb_frontend *ascot2e_attach(struct dvb_frontend *fe, const struct ascot2e_config *config, struct i2c_adapter *i2c)

    :param fe:
        frontend to be attached
    :type fe: struct dvb_frontend \*

    :param config:
        pointer to \ :c:type:`struct ascot2e_config <ascot2e_config>`\  with tuner configuration.
    :type config: const struct ascot2e_config \*

    :param i2c:
        i2c adapter to use.
    :type i2c: struct i2c_adapter \*

.. _`ascot2e_attach.return`:

Return
------

FE pointer on success, NULL on failure.

.. This file was automatic generated / don't edit.

