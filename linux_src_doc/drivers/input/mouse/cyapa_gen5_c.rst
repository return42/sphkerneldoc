.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/mouse/cyapa_gen5.c

.. _`cyapa_i2c_pip_write`:

cyapa_i2c_pip_write
===================

.. c:function:: ssize_t cyapa_i2c_pip_write(struct cyapa *cyapa, u8 *buf, size_t size)

    :param struct cyapa \*cyapa:
        *undescribed*

    :param u8 \*buf:
        *undescribed*

    :param size_t size:
        *undescribed*

.. _`cyapa_empty_pip_output_data`:

cyapa_empty_pip_output_data
===========================

.. c:function:: int cyapa_empty_pip_output_data(struct cyapa *cyapa, u8 *buf, int *len, cb_sort func)

    before send any command, otherwise, the interrupt line will be blocked.

    :param struct cyapa \*cyapa:
        *undescribed*

    :param u8 \*buf:
        *undescribed*

    :param int \*len:
        *undescribed*

    :param cb_sort func:
        *undescribed*

.. This file was automatic generated / don't edit.

