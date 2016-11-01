.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-octeon-core.h

.. _`octeon_i2c_reg_write`:

octeon_i2c_reg_write
====================

.. c:function:: void octeon_i2c_reg_write(struct octeon_i2c *i2c, u64 eop_reg, u8 data)

    write an I2C core register

    :param struct octeon_i2c \*i2c:
        The struct octeon_i2c

    :param u64 eop_reg:
        Register selector

    :param u8 data:
        Value to be written

.. _`octeon_i2c_reg_write.description`:

Description
-----------

The I2C core registers are accessed indirectly via the SW_TWSI CSR.

.. _`octeon_i2c_reg_read`:

octeon_i2c_reg_read
===================

.. c:function:: int octeon_i2c_reg_read(struct octeon_i2c *i2c, u64 eop_reg, int *error)

    read lower bits of an I2C core register

    :param struct octeon_i2c \*i2c:
        The struct octeon_i2c

    :param u64 eop_reg:
        Register selector

    :param int \*error:
        *undescribed*

.. _`octeon_i2c_reg_read.description`:

Description
-----------

Returns the data.

The I2C core registers are accessed indirectly via the SW_TWSI CSR.

.. _`octeon_i2c_read_int`:

octeon_i2c_read_int
===================

.. c:function:: u64 octeon_i2c_read_int(struct octeon_i2c *i2c)

    read the TWSI_INT register

    :param struct octeon_i2c \*i2c:
        The struct octeon_i2c

.. _`octeon_i2c_read_int.description`:

Description
-----------

Returns the value of the register.

.. _`octeon_i2c_write_int`:

octeon_i2c_write_int
====================

.. c:function:: void octeon_i2c_write_int(struct octeon_i2c *i2c, u64 data)

    write the TWSI_INT register

    :param struct octeon_i2c \*i2c:
        The struct octeon_i2c

    :param u64 data:
        Value to be written

.. This file was automatic generated / don't edit.

