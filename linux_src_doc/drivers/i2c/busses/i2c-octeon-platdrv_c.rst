.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-octeon-platdrv.c

.. _`octeon_i2c_int_enable`:

octeon_i2c_int_enable
=====================

.. c:function:: void octeon_i2c_int_enable(struct octeon_i2c *i2c)

    enable the CORE interrupt

    :param struct octeon_i2c \*i2c:
        The struct octeon_i2c

.. _`octeon_i2c_int_enable.description`:

Description
-----------

The interrupt will be asserted when there is non-STAT_IDLE state in
the SW_TWSI_EOP_TWSI_STAT register.

.. _`octeon_i2c_int_enable78`:

octeon_i2c_int_enable78
=======================

.. c:function:: void octeon_i2c_int_enable78(struct octeon_i2c *i2c)

    enable the CORE interrupt

    :param struct octeon_i2c \*i2c:
        The struct octeon_i2c

.. _`octeon_i2c_int_enable78.description`:

Description
-----------

The interrupt will be asserted when there is non-STAT_IDLE state in the
SW_TWSI_EOP_TWSI_STAT register.

.. _`octeon_i2c_hlc_int_enable78`:

octeon_i2c_hlc_int_enable78
===========================

.. c:function:: void octeon_i2c_hlc_int_enable78(struct octeon_i2c *i2c)

    enable the ST interrupt

    :param struct octeon_i2c \*i2c:
        The struct octeon_i2c

.. _`octeon_i2c_hlc_int_enable78.description`:

Description
-----------

The interrupt will be asserted when there is non-STAT_IDLE state in
the SW_TWSI_EOP_TWSI_STAT register.

.. This file was automatic generated / don't edit.

