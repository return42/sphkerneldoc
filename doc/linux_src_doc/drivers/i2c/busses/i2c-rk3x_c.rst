.. -*- coding: utf-8; mode: rst -*-

==========
i2c-rk3x.c
==========


.. _`rk3x_i2c_start`:

rk3x_i2c_start
==============

.. c:function:: void rk3x_i2c_start (struct rk3x_i2c *i2c)

    :param struct rk3x_i2c \*i2c:

        *undescribed*



.. _`rk3x_i2c_stop`:

rk3x_i2c_stop
=============

.. c:function:: void rk3x_i2c_stop (struct rk3x_i2c *i2c, int error)

    :param struct rk3x_i2c \*i2c:

        *undescribed*

    :param int error:
        Error code to return in rk3x_i2c_xfer



.. _`rk3x_i2c_prepare_read`:

rk3x_i2c_prepare_read
=====================

.. c:function:: void rk3x_i2c_prepare_read (struct rk3x_i2c *i2c)

    >msg

    :param struct rk3x_i2c \*i2c:

        *undescribed*



.. _`rk3x_i2c_fill_transmit_buf`:

rk3x_i2c_fill_transmit_buf
==========================

.. c:function:: void rk3x_i2c_fill_transmit_buf (struct rk3x_i2c *i2c)

    >msg

    :param struct rk3x_i2c \*i2c:

        *undescribed*



.. _`rk3x_i2c_calc_divs`:

rk3x_i2c_calc_divs
==================

.. c:function:: int rk3x_i2c_calc_divs (unsigned long clk_rate, unsigned long scl_rate, unsigned long scl_rise_ns, unsigned long scl_fall_ns, unsigned long sda_fall_ns, unsigned long *div_low, unsigned long *div_high)

    :param unsigned long clk_rate:
        I2C input clock rate

    :param unsigned long scl_rate:
        Desired SCL rate

    :param unsigned long scl_rise_ns:
        How many ns it takes for SCL to rise.

    :param unsigned long scl_fall_ns:
        How many ns it takes for SCL to fall.

    :param unsigned long sda_fall_ns:
        How many ns it takes for SDA to fall.

    :param unsigned long \*div_low:
        Divider output for low

    :param unsigned long \*div_high:
        Divider output for high



.. _`rk3x_i2c_calc_divs.returns`:

Returns
-------

0 on success, -EINVAL if the goal SCL rate is too slow. In that case
a best-effort divider value is returned in divs. If the target rate is
too high, we silently use the highest possible rate.



.. _`rk3x_i2c_clk_notifier_cb`:

rk3x_i2c_clk_notifier_cb
========================

.. c:function:: int rk3x_i2c_clk_notifier_cb (struct notifier_block *nb, unsigned long event, void *data)

    Clock rate change callback

    :param struct notifier_block \*nb:
        Pointer to notifier block

    :param unsigned long event:
        Notification reason

    :param void \*data:
        Pointer to notification data object



.. _`rk3x_i2c_clk_notifier_cb.description`:

Description
-----------

The callback checks whether a valid bus frequency can be generated after the
change. If so, the change is acknowledged, otherwise the change is aborted.
New dividers are written to the HW in the pre- or post change notification
depending on the scaling direction.

Code adapted from i2c-cadence.c.



.. _`rk3x_i2c_clk_notifier_cb.return`:

Return
------

NOTIFY_STOP if the rate change should be aborted, NOTIFY_OK
to acknowedge the change, NOTIFY_DONE if the notification is
considered irrelevant.



.. _`rk3x_i2c_setup`:

rk3x_i2c_setup
==============

.. c:function:: int rk3x_i2c_setup (struct rk3x_i2c *i2c, struct i2c_msg *msgs, int num)

    :param struct rk3x_i2c \*i2c:

        *undescribed*

    :param struct i2c_msg \*msgs:
        I2C msgs to process

    :param int num:
        Number of msgs



.. _`rk3x_i2c_setup.description`:

Description
-----------


Must be called with i2c->lock held.



.. _`rk3x_i2c_setup.returns`:

returns
-------

Number of I2C msgs processed or negative in case of error

