.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/raw/nand_ecc.c

.. _`__nand_calculate_ecc`:

__nand_calculate_ecc
====================

.. c:function:: void __nand_calculate_ecc(const unsigned char *buf, unsigned int eccsize, unsigned char *code, bool sm_order)

    [NAND Interface] Calculate 3-byte ECC for 256/512-byte block

    :param buf:
        input buffer with raw data
    :type buf: const unsigned char \*

    :param eccsize:
        data bytes per ECC step (256 or 512)
    :type eccsize: unsigned int

    :param code:
        output buffer with ECC
    :type code: unsigned char \*

    :param sm_order:
        Smart Media byte ordering
    :type sm_order: bool

.. _`nand_calculate_ecc`:

nand_calculate_ecc
==================

.. c:function:: int nand_calculate_ecc(struct nand_chip *chip, const unsigned char *buf, unsigned char *code)

    [NAND Interface] Calculate 3-byte ECC for 256/512-byte block

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param buf:
        input buffer with raw data
    :type buf: const unsigned char \*

    :param code:
        output buffer with ECC
    :type code: unsigned char \*

.. _`__nand_correct_data`:

__nand_correct_data
===================

.. c:function:: int __nand_correct_data(unsigned char *buf, unsigned char *read_ecc, unsigned char *calc_ecc, unsigned int eccsize, bool sm_order)

    [NAND Interface] Detect and correct bit error(s)

    :param buf:
        raw data read from the chip
    :type buf: unsigned char \*

    :param read_ecc:
        ECC from the chip
    :type read_ecc: unsigned char \*

    :param calc_ecc:
        the ECC calculated from raw data
    :type calc_ecc: unsigned char \*

    :param eccsize:
        data bytes per ECC step (256 or 512)
    :type eccsize: unsigned int

    :param sm_order:
        Smart Media byte order
    :type sm_order: bool

.. _`__nand_correct_data.description`:

Description
-----------

Detect and correct a 1 bit error for eccsize byte block

.. _`nand_correct_data`:

nand_correct_data
=================

.. c:function:: int nand_correct_data(struct nand_chip *chip, unsigned char *buf, unsigned char *read_ecc, unsigned char *calc_ecc)

    [NAND Interface] Detect and correct bit error(s)

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param buf:
        raw data read from the chip
    :type buf: unsigned char \*

    :param read_ecc:
        ECC from the chip
    :type read_ecc: unsigned char \*

    :param calc_ecc:
        the ECC calculated from raw data
    :type calc_ecc: unsigned char \*

.. _`nand_correct_data.description`:

Description
-----------

Detect and correct a 1 bit error for 256/512 byte block

.. This file was automatic generated / don't edit.

