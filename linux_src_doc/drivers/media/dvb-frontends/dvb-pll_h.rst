.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/dvb-frontends/dvb-pll.h

.. _`dvb_pll_attach`:

dvb_pll_attach
==============

.. c:function:: struct dvb_frontend *dvb_pll_attach(struct dvb_frontend *fe, int pll_addr, struct i2c_adapter *i2c, unsigned int pll_desc_id)

    pll to the supplied frontend structure.

    :param fe:
        Frontend to attach to.
    :type fe: struct dvb_frontend \*

    :param pll_addr:
        i2c address of the PLL (if used).
    :type pll_addr: int

    :param i2c:
        i2c adapter to use (set to NULL if not used).
    :type i2c: struct i2c_adapter \*

    :param pll_desc_id:
        dvb_pll_desc to use.
    :type pll_desc_id: unsigned int

.. _`dvb_pll_attach.return`:

Return
------

Frontend pointer on success, NULL on failure

.. This file was automatic generated / don't edit.

