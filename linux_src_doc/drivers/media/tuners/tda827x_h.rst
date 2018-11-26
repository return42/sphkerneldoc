.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/tuners/tda827x.h

.. _`tda827x_attach`:

tda827x_attach
==============

.. c:function:: struct dvb_frontend* tda827x_attach(struct dvb_frontend *fe, int addr, struct i2c_adapter *i2c, struct tda827x_config *cfg)

    :param fe:
        *undescribed*
    :type fe: struct dvb_frontend \*

    :param addr:
        *undescribed*
    :type addr: int

    :param i2c:
        *undescribed*
    :type i2c: struct i2c_adapter \*

    :param cfg:
        *undescribed*
    :type cfg: struct tda827x_config \*

.. _`tda827x_attach.description`:

Description
-----------

\ ``param``\  fe Frontend to attach to.
\ ``param``\  addr i2c address of the tuner.
\ ``param``\  i2c i2c adapter to use.
\ ``param``\  cfg optional callback function pointers.
\ ``return``\  FE pointer on success, NULL on failure.

.. This file was automatic generated / don't edit.

