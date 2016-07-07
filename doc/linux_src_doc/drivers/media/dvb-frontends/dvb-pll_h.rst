.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/dvb-frontends/dvb-pll.h

.. _`dvb_pll_attach`:

dvb_pll_attach
==============

.. c:function:: struct dvb_frontend *dvb_pll_attach(struct dvb_frontend *fe, int pll_addr, struct i2c_adapter *i2c, unsigned int pll_desc_id)

    pll to the supplied frontend structure.

    :param struct dvb_frontend \*fe:
        *undescribed*

    :param int pll_addr:
        *undescribed*

    :param struct i2c_adapter \*i2c:
        *undescribed*

    :param unsigned int pll_desc_id:
        *undescribed*

.. _`dvb_pll_attach.description`:

Description
-----------

\ ``param``\  fe Frontend to attach to.
\ ``param``\  pll_addr i2c address of the PLL (if used).
\ ``param``\  i2c i2c adapter to use (set to NULL if not used).
\ ``param``\  pll_desc_id dvb_pll_desc to use.
\ ``return``\  Frontend pointer on success, NULL on failure

.. This file was automatic generated / don't edit.

