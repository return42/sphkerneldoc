.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/dvb-frontends/zd1301_demod.h

.. _`zd1301_demod_platform_data`:

struct zd1301_demod_platform_data
=================================

.. c:type:: struct zd1301_demod_platform_data

    Platform data for the zd1301_demod driver

.. _`zd1301_demod_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct zd1301_demod_platform_data {
        void *reg_priv;
        int (*reg_read)(void *, u16, u8 *);
        int (*reg_write)(void *, u16, u8);
    }

.. _`zd1301_demod_platform_data.members`:

Members
-------

reg_priv
    First argument of reg_read and reg_write callbacks.

reg_read
    Register read callback.

reg_write
    Register write callback.

.. _`zd1301_demod_get_dvb_frontend`:

zd1301_demod_get_dvb_frontend
=============================

.. c:function:: struct dvb_frontend *zd1301_demod_get_dvb_frontend(struct platform_device *pdev)

    Get pointer to DVB frontend

    :param pdev:
        Pointer to platform device
    :type pdev: struct platform_device \*

.. _`zd1301_demod_get_dvb_frontend.return`:

Return
------

Pointer to DVB frontend which given platform device owns.

.. _`zd1301_demod_get_i2c_adapter`:

zd1301_demod_get_i2c_adapter
============================

.. c:function:: struct i2c_adapter *zd1301_demod_get_i2c_adapter(struct platform_device *pdev)

    Get pointer to I2C adapter

    :param pdev:
        Pointer to platform device
    :type pdev: struct platform_device \*

.. _`zd1301_demod_get_i2c_adapter.return`:

Return
------

Pointer to I2C adapter which given platform device owns.

.. _`zd1301_demod_get_dvb_frontend`:

zd1301_demod_get_dvb_frontend
=============================

.. c:function:: struct dvb_frontend *zd1301_demod_get_dvb_frontend(struct platform_device *dev)

    Attach a zd1301 frontend

    :param dev:
        Pointer to platform device
    :type dev: struct platform_device \*

.. _`zd1301_demod_get_dvb_frontend.return`:

Return
------

Pointer to \ ``struct``\  dvb_frontend or NULL if attach fails.

.. This file was automatic generated / don't edit.

