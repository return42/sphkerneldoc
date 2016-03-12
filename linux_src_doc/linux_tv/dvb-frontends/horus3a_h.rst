.. -*- coding: utf-8; mode: rst -*-

=========
horus3a.h
=========



.. _xref_struct_horus3a_config:

struct horus3a_config
=====================

.. c:type:: struct horus3a_config

    the configuration of Horus3A tuner driver



Definition
----------

.. code-block:: c

  struct horus3a_config {
    u8 i2c_address;
    u8 xtal_freq_mhz;
    void * set_tuner_priv;
    int (* set_tuner_callback) (void *, int);
  };



Members
-------

:``u8 i2c_address``:
    I2C address of the tuner

:``u8 xtal_freq_mhz``:
    Oscillator frequency, MHz

:``void * set_tuner_priv``:
    Callback function private context

:``int (*)(void *, int) set_tuner_callback``:
    Callback function that notifies the parent driver
             which tuner is active now



