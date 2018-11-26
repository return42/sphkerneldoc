.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/mouse/cyapa.c

.. _`cyapa_i2c_write`:

cyapa_i2c_write
===============

.. c:function:: int cyapa_i2c_write(struct cyapa *cyapa, u8 reg, size_t len, const void *values)

    Execute i2c block data write operation

    :param cyapa:
        Handle to this driver
    :type cyapa: struct cyapa \*

    :param reg:
        *undescribed*
    :type reg: u8

    :param len:
        number of bytes to write
    :type len: size_t

    :param values:
        Data to be written
    :type values: const void \*

.. _`cyapa_i2c_write.description`:

Description
-----------

Return negative errno code on error; return zero when success.

.. This file was automatic generated / don't edit.

