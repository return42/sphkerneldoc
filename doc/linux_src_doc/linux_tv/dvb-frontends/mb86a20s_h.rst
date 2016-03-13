.. -*- coding: utf-8; mode: rst -*-

==========
mb86a20s.h
==========



.. _xref_struct_mb86a20s_config:

struct mb86a20s_config
======================

.. c:type:: struct mb86a20s_config

    Define the per-device attributes of the frontend



Definition
----------

.. code-block:: c

  struct mb86a20s_config {
    u32 fclk;
    u8 demod_address;
    bool is_serial;
  };



Members
-------

:``u32 fclk``:
    Clock frequency. If zero, assumes the default
    			(32.57142 Mhz)

:``u8 demod_address``:
    the demodulator's i2c address

:``bool is_serial``:
    if true, TS is serial. Otherwise, TS is parallel



