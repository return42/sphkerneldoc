.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/avr32/mach-at32ap/hmatrix.c

.. _`hmatrix_write_reg`:

hmatrix_write_reg
=================

.. c:function:: void hmatrix_write_reg(unsigned long offset, u32 value)

    write HMATRIX configuration register

    :param unsigned long offset:
        register offset

    :param u32 value:
        value to be written to the register at \ ``offset``\ 

.. _`hmatrix_read_reg`:

hmatrix_read_reg
================

.. c:function:: u32 hmatrix_read_reg(unsigned long offset)

    read HMATRIX configuration register

    :param unsigned long offset:
        register offset

.. _`hmatrix_read_reg.description`:

Description
-----------

Returns the value of the register at \ ``offset``\ .

.. _`hmatrix_sfr_set_bits`:

hmatrix_sfr_set_bits
====================

.. c:function:: void hmatrix_sfr_set_bits(unsigned int slave_id, u32 mask)

    set bits in a slave's Special Function Register

    :param unsigned int slave_id:
        operate on the SFR belonging to this slave

    :param u32 mask:
        mask of bits to be set in the SFR

.. _`hmatrix_sfr_clear_bits`:

hmatrix_sfr_clear_bits
======================

.. c:function:: void hmatrix_sfr_clear_bits(unsigned int slave_id, u32 mask)

    clear bits in a slave's Special Function Register

    :param unsigned int slave_id:
        operate on the SFR belonging to this slave

    :param u32 mask:
        mask of bits to be cleared in the SFR

.. This file was automatic generated / don't edit.

