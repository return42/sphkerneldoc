.. -*- coding: utf-8; mode: rst -*-

=========
tda826x.h
=========



.. _xref_tda826x_attach:

tda826x_attach
==============

.. c:function:: struct dvb_frontend* tda826x_attach (struct dvb_frontend * fe, int addr, struct i2c_adapter * i2c, int has_loopthrough)

    

    :param struct dvb_frontend * fe:

        _undescribed_

    :param int addr:

        _undescribed_

    :param struct i2c_adapter * i2c:

        _undescribed_

    :param int has_loopthrough:

        _undescribed_



Description
-----------



**param** fe Frontend to attach to.
**param** addr i2c address of the tuner.
**param** i2c i2c adapter to use.
**param** has_loopthrough Set to 1 if the card has a loopthrough RF connector.
**return** FE pointer on success, NULL on failure.


