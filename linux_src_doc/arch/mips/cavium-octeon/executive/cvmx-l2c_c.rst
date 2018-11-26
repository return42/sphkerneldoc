.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/cavium-octeon/executive/cvmx-l2c.c

.. _`cvmx_l2c_get_set_bits`:

cvmx_l2c_get_set_bits
=====================

.. c:function:: int cvmx_l2c_get_set_bits( void)

    Returns

    :param void:
        no arguments
    :type void: 

.. _`cvmx_l2c_flush_line`:

cvmx_l2c_flush_line
===================

.. c:function:: void cvmx_l2c_flush_line(uint32_t assoc, uint32_t index)

    This should only be called from one core at a time, as this routine sets the core to the 'debug' core in order to flush the line.

    :param assoc:
        Association (or way) to flush
    :type assoc: uint32_t

    :param index:
        Index to flush
    :type index: uint32_t

.. This file was automatic generated / don't edit.

