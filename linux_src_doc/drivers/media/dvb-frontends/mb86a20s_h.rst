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

.. _`mb86a20s_attach`:

mb86a20s_attach
===============

.. c:function:: struct dvb_frontend *mb86a20s_attach(const struct mb86a20s_config *config, struct i2c_adapter *i2c)

    :param const struct mb86a20s_config \*config:
        pointer to \ :c:type:`struct mb86a20s_config <mb86a20s_config>`\  with demod configuration.

    :param struct i2c_adapter \*i2c:
        i2c adapter to use.

.. _`mb86a20s_attach.return`:

Return
------

FE pointer on success, NULL on failure.

.. This file was automatic generated / don't edit.

