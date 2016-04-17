.. -*- coding: utf-8; mode: rst -*-

=========
tda826x.h
=========


.. _`tda826x_attach`:

tda826x_attach
==============

.. c:function:: struct dvb_frontend*tda826x_attach (struct dvb_frontend *fe, int addr, struct i2c_adapter *i2c, int has_loopthrough)

    :param struct dvb_frontend \*fe:

        *undescribed*

    :param int addr:

        *undescribed*

    :param struct i2c_adapter \*i2c:

        *undescribed*

    :param int has_loopthrough:

        *undescribed*



.. _`tda826x_attach.description`:

Description
-----------


``param`` fe Frontend to attach to.
``param`` addr i2c address of the tuner.
``param`` i2c i2c adapter to use.
``param`` has_loopthrough Set to 1 if the card has a loopthrough RF connector.
``return`` FE pointer on success, NULL on failure.

