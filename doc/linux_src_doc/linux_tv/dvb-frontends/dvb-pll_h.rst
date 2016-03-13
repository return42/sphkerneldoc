.. -*- coding: utf-8; mode: rst -*-

=========
dvb-pll.h
=========



.. _xref_dvb_pll_attach:

dvb_pll_attach
==============

.. c:function:: struct dvb_frontend * dvb_pll_attach (struct dvb_frontend * fe, int pll_addr, struct i2c_adapter * i2c, unsigned int pll_desc_id)

    pll to the supplied frontend structure.

    :param struct dvb_frontend * fe:

        _undescribed_

    :param int pll_addr:

        _undescribed_

    :param struct i2c_adapter * i2c:

        _undescribed_

    :param unsigned int pll_desc_id:

        _undescribed_



Description
-----------



**param** fe Frontend to attach to.
**param** pll_addr i2c address of the PLL (if used).
**param** i2c i2c adapter to use (set to NULL if not used).
**param** pll_desc_id dvb_pll_desc to use.
**return** Frontend pointer on success, NULL on failure


