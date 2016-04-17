.. -*- coding: utf-8; mode: rst -*-

=========
ascot2e.h
=========


.. _`ascot2e_config`:

struct ascot2e_config
=====================

.. c:type:: ascot2e_config

    the configuration of Ascot2E tuner driver


.. _`ascot2e_config.definition`:

Definition
----------

.. code-block:: c

  struct ascot2e_config {
    u8 i2c_address;
    u8 xtal_freq_mhz;
    void * set_tuner_priv;
    int (* set_tuner_callback) (void *, int);
  };


.. _`ascot2e_config.members`:

Members
-------

:``i2c_address``:
    I2C address of the tuner

:``xtal_freq_mhz``:
    Oscillator frequency, MHz

:``set_tuner_priv``:
    Callback function private context

:``set_tuner_callback``:
    Callback function that notifies the parent driver
    which tuner is active now


