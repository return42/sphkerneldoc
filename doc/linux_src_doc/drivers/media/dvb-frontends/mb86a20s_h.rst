.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/dvb-frontends/mb86a20s.h

.. _`mb86a20s_config`:

struct mb86a20s_config
======================

.. c:type:: struct mb86a20s_config

    Define the per-device attributes of the frontend

.. _`mb86a20s_config.definition`:

Definition
----------

.. code-block:: c

    struct mb86a20s_config {
        u32 fclk;
        u8 demod_address;
        bool is_serial;
    }

.. _`mb86a20s_config.members`:

Members
-------

fclk
    Clock frequency. If zero, assumes the default
    (32.57142 Mhz)

demod_address
    the demodulator's i2c address

is_serial
    if true, TS is serial. Otherwise, TS is parallel

.. This file was automatic generated / don't edit.

