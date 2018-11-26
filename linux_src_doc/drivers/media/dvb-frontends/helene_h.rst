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
        struct dvb_frontend *fe;
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
    Cristal frequency as described by \ :c:type:`enum helene_xtal <helene_xtal>`\ 

fe
    Frontend for which connects this tuner

.. _`helene_attach`:

helene_attach
=============

.. c:function:: struct dvb_frontend *helene_attach(struct dvb_frontend *fe, const struct helene_config *config, struct i2c_adapter *i2c)

    :param fe:
        frontend to be attached
    :type fe: struct dvb_frontend \*

    :param config:
        pointer to \ :c:type:`struct helene_config <helene_config>`\  with tuner configuration.
    :type config: const struct helene_config \*

    :param i2c:
        i2c adapter to use.
    :type i2c: struct i2c_adapter \*

.. _`helene_attach.return`:

Return
------

FE pointer on success, NULL on failure.

.. _`helene_attach_s`:

helene_attach_s
===============

.. c:function:: struct dvb_frontend *helene_attach_s(struct dvb_frontend *fe, const struct helene_config *config, struct i2c_adapter *i2c)

    :param fe:
        frontend to be attached
    :type fe: struct dvb_frontend \*

    :param config:
        pointer to \ :c:type:`struct helene_config <helene_config>`\  with tuner configuration.
    :type config: const struct helene_config \*

    :param i2c:
        i2c adapter to use.
    :type i2c: struct i2c_adapter \*

.. _`helene_attach_s.return`:

Return
------

FE pointer on success, NULL on failure.

.. This file was automatic generated / don't edit.

