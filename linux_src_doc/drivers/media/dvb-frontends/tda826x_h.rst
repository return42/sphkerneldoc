.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/dvb-frontends/tda826x.h

.. _`tda826x_attach`:

tda826x_attach
==============

.. c:function:: struct dvb_frontend*tda826x_attach(struct dvb_frontend *fe, int addr, struct i2c_adapter *i2c, int has_loopthrough)

    :param struct dvb_frontend \*fe:
        Frontend to attach to.

    :param int addr:
        i2c address of the tuner.

    :param struct i2c_adapter \*i2c:
        i2c adapter to use.

    :param int has_loopthrough:
        Set to 1 if the card has a loopthrough RF connector.

.. _`tda826x_attach.return`:

Return
------

FE pointer on success, NULL on failure.

.. This file was automatic generated / don't edit.

