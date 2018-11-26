.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/regmap/regmap-sccb.c

.. _`sccb_is_available`:

sccb_is_available
=================

.. c:function:: bool sccb_is_available(struct i2c_adapter *adap)

    Check if the adapter supports SCCB protocol

    :param adap:
        I2C adapter
    :type adap: struct i2c_adapter \*

.. _`sccb_is_available.description`:

Description
-----------

Return true if the I2C adapter is capable of using SCCB helper functions,
false otherwise.

.. _`regmap_sccb_read`:

regmap_sccb_read
================

.. c:function:: int regmap_sccb_read(void *context, unsigned int reg, unsigned int *val)

    Read data from SCCB slave device

    :param context:
        Device that will be interacted with
    :type context: void \*

    :param reg:
        Register to be read from
    :type reg: unsigned int

    :param val:
        Pointer to store read value
    :type val: unsigned int \*

.. _`regmap_sccb_read.description`:

Description
-----------

This executes the 2-phase write transmission cycle that is followed by a
2-phase read transmission cycle, returning negative errno else zero on
success.

.. _`regmap_sccb_write`:

regmap_sccb_write
=================

.. c:function:: int regmap_sccb_write(void *context, unsigned int reg, unsigned int val)

    Write data to SCCB slave device

    :param context:
        Device that will be interacted with
    :type context: void \*

    :param reg:
        Register to write to
    :type reg: unsigned int

    :param val:
        Value to be written
    :type val: unsigned int

.. _`regmap_sccb_write.description`:

Description
-----------

This executes the SCCB 3-phase write transmission cycle, returning negative
errno else zero on success.

.. This file was automatic generated / don't edit.

