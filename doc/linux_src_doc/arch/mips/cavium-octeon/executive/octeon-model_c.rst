.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/cavium-octeon/executive/octeon-model.c

.. _`cvmx_fuse_read_byte`:

cvmx_fuse_read_byte
===================

.. c:function:: uint8_t cvmx_fuse_read_byte(int byte_addr)

    :param int byte_addr:
        address to read

.. _`cvmx_fuse_read_byte.returns-fuse-value`:

Returns fuse value
------------------

0 or 1

.. _`octeon_model_get_string`:

octeon_model_get_string
=======================

.. c:function:: const char *octeon_model_get_string(uint32_t chip_id)

    string representing the chip model number. The string is of the form CNXXXXpX.X-FREQ-SUFFIX. - XXXX = The chip model number - X.X = Chip pass number - FREQ = Current frequency in Mhz - SUFFIX = NSP, EXP, SCP, SSP, or CP

    :param uint32_t chip_id:
        Chip ID

.. _`octeon_model_get_string.description`:

Description
-----------

Returns Model string

.. This file was automatic generated / don't edit.

