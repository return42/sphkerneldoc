.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/mouse/cyapa.c

.. _`cyapa_i2c_write`:

cyapa_i2c_write
===============

.. c:function:: int cyapa_i2c_write(struct cyapa *cyapa, u8 reg, size_t len, const void *values)

    Execute i2c block data write operation

    :param struct cyapa \*cyapa:
        Handle to this driver

    :param u8 reg:
        *undescribed*

    :param size_t len:
        number of bytes to write

    :param const void \*values:
        Data to be written

.. _`cyapa_i2c_write.description`:

Description
-----------

Return negative errno code on error; return zero when success.

.. This file was automatic generated / don't edit.

