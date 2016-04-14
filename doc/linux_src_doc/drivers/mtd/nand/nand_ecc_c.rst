.. -*- coding: utf-8; mode: rst -*-

==========
nand_ecc.c
==========

.. _`__nand_calculate_ecc`:

__nand_calculate_ecc
====================

.. c:function:: void __nand_calculate_ecc (const unsigned char *buf, unsigned int eccsize, unsigned char *code)

    [NAND Interface] Calculate 3-byte ECC for 256/512-byte block

    :param const unsigned char \*buf:
        input buffer with raw data

    :param unsigned int eccsize:
        data bytes per ECC step (256 or 512)

    :param unsigned char \*code:
        output buffer with ECC


.. _`nand_calculate_ecc`:

nand_calculate_ecc
==================

.. c:function:: int nand_calculate_ecc (struct mtd_info *mtd, const unsigned char *buf, unsigned char *code)

    [NAND Interface] Calculate 3-byte ECC for 256/512-byte block

    :param struct mtd_info \*mtd:
        MTD block structure

    :param const unsigned char \*buf:
        input buffer with raw data

    :param unsigned char \*code:
        output buffer with ECC


.. _`__nand_correct_data`:

__nand_correct_data
===================

.. c:function:: int __nand_correct_data (unsigned char *buf, unsigned char *read_ecc, unsigned char *calc_ecc, unsigned int eccsize)

    [NAND Interface] Detect and correct bit error(s)

    :param unsigned char \*buf:
        raw data read from the chip

    :param unsigned char \*read_ecc:
        ECC from the chip

    :param unsigned char \*calc_ecc:
        the ECC calculated from raw data

    :param unsigned int eccsize:
        data bytes per ECC step (256 or 512)


.. _`__nand_correct_data.description`:

Description
-----------

Detect and correct a 1 bit error for eccsize byte block


.. _`nand_correct_data`:

nand_correct_data
=================

.. c:function:: int nand_correct_data (struct mtd_info *mtd, unsigned char *buf, unsigned char *read_ecc, unsigned char *calc_ecc)

    [NAND Interface] Detect and correct bit error(s)

    :param struct mtd_info \*mtd:
        MTD block structure

    :param unsigned char \*buf:
        raw data read from the chip

    :param unsigned char \*read_ecc:
        ECC from the chip

    :param unsigned char \*calc_ecc:
        the ECC calculated from raw data


.. _`nand_correct_data.description`:

Description
-----------

Detect and correct a 1 bit error for 256/512 byte block

