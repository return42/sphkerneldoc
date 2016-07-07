.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/tuners/tda827x.h

.. _`tda827x_attach`:

tda827x_attach
==============

.. c:function:: struct dvb_frontend*tda827x_attach(struct dvb_frontend *fe, int addr, struct i2c_adapter *i2c, struct tda827x_config *cfg)

    :param struct dvb_frontend \*fe:
        *undescribed*

    :param int addr:
        *undescribed*

    :param struct i2c_adapter \*i2c:
        *undescribed*

    :param struct tda827x_config \*cfg:
        *undescribed*

.. _`tda827x_attach.description`:

Description
-----------

\ ``param``\  fe Frontend to attach to.
\ ``param``\  addr i2c address of the tuner.
\ ``param``\  i2c i2c adapter to use.
\ ``param``\  cfg optional callback function pointers.
\ ``return``\  FE pointer on success, NULL on failure.

.. This file was automatic generated / don't edit.

