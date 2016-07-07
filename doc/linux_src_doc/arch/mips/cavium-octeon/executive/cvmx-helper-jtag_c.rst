.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/cavium-octeon/executive/cvmx-helper-jtag.c

.. _`cvmx_helper_qlm_jtag_init`:

cvmx_helper_qlm_jtag_init
=========================

.. c:function:: void cvmx_helper_qlm_jtag_init( void)

    of the JTAG chain by the cvmx_helper_qlm_jtag\_\*() functions. These functions should only be used at the direction of Cavium Networks. Programming incorrect values into the JTAG chain can cause chip damage.

    :param  void:
        no arguments

.. _`cvmx_helper_qlm_jtag_shift`:

cvmx_helper_qlm_jtag_shift
==========================

.. c:function:: uint32_t cvmx_helper_qlm_jtag_shift(int qlm, int bits, uint32_t data)

    into the MSB and out the LSB, so you should shift in the low order bits followed by the high order bits. The JTAG chain is 4 \* 268 bits long, or 1072.

    :param int qlm:
        QLM to shift value into

    :param int bits:
        Number of bits to shift in (1-32).

    :param uint32_t data:
        Data to shift in. Bit 0 enters the chain first, followed by
        bit 1, etc.

.. _`cvmx_helper_qlm_jtag_shift.description`:

Description
-----------

Returns The low order bits of the JTAG chain that shifted out of the
circle.

.. _`cvmx_helper_qlm_jtag_shift_zeros`:

cvmx_helper_qlm_jtag_shift_zeros
================================

.. c:function:: void cvmx_helper_qlm_jtag_shift_zeros(int qlm, int bits)

    common to need to shift more than 32 bits of zeros into the chain. This function is a convience wrapper around \ :c:func:`cvmx_helper_qlm_jtag_shift`\  to shift more than 32 bits of zeros at a time.

    :param int qlm:
        QLM to shift zeros into

    :param int bits:
        *undescribed*

.. _`cvmx_helper_qlm_jtag_update`:

cvmx_helper_qlm_jtag_update
===========================

.. c:function:: void cvmx_helper_qlm_jtag_update(int qlm)

    have already shifted in 268\*4, or 1072 bits into the JTAG chain. Updating invalid values can possibly cause chip damage.

    :param int qlm:
        QLM to program

.. This file was automatic generated / don't edit.

