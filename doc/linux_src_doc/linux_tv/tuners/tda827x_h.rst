.. -*- coding: utf-8; mode: rst -*-

=========
tda827x.h
=========



.. _xref_tda827x_attach:

tda827x_attach
==============

.. c:function:: struct dvb_frontend* tda827x_attach (struct dvb_frontend * fe, int addr, struct i2c_adapter * i2c, struct tda827x_config * cfg)

    

    :param struct dvb_frontend * fe:

        _undescribed_

    :param int addr:

        _undescribed_

    :param struct i2c_adapter * i2c:

        _undescribed_

    :param struct tda827x_config * cfg:

        _undescribed_



Description
-----------



**param** fe Frontend to attach to.
**param** addr i2c address of the tuner.
**param** i2c i2c adapter to use.
**param** cfg optional callback function pointers.
**return** FE pointer on success, NULL on failure.


