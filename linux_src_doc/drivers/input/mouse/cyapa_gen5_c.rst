.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/mouse/cyapa_gen5.c

.. _`cyapa_i2c_pip_write`:

cyapa_i2c_pip_write
===================

.. c:function:: ssize_t cyapa_i2c_pip_write(struct cyapa *cyapa, u8 *buf, size_t size)

    :param cyapa:
        *undescribed*
    :type cyapa: struct cyapa \*

    :param buf:
        *undescribed*
    :type buf: u8 \*

    :param size:
        *undescribed*
    :type size: size_t

.. _`cyapa_empty_pip_output_data`:

cyapa_empty_pip_output_data
===========================

.. c:function:: int cyapa_empty_pip_output_data(struct cyapa *cyapa, u8 *buf, int *len, cb_sort func)

    before send any command, otherwise, the interrupt line will be blocked.

    :param cyapa:
        *undescribed*
    :type cyapa: struct cyapa \*

    :param buf:
        *undescribed*
    :type buf: u8 \*

    :param len:
        *undescribed*
    :type len: int \*

    :param func:
        *undescribed*
    :type func: cb_sort

.. This file was automatic generated / don't edit.

