.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/raw/nand_bch.c

.. _`nand_bch_control`:

struct nand_bch_control
=======================

.. c:type:: struct nand_bch_control

    private NAND BCH control structure

.. _`nand_bch_control.definition`:

Definition
----------

.. code-block:: c

    struct nand_bch_control {
        struct bch_control *bch;
        unsigned int *errloc;
        unsigned char *eccmask;
    }

.. _`nand_bch_control.members`:

Members
-------

bch
    BCH control structure

errloc
    error location array

eccmask
    XOR ecc mask, allows erased pages to be decoded as valid

.. _`nand_bch_calculate_ecc`:

nand_bch_calculate_ecc
======================

.. c:function:: int nand_bch_calculate_ecc(struct mtd_info *mtd, const unsigned char *buf, unsigned char *code)

    [NAND Interface] Calculate ECC for data block

    :param struct mtd_info \*mtd:
        MTD block structure

    :param const unsigned char \*buf:
        input buffer with raw data

    :param unsigned char \*code:
        output buffer with ECC

.. _`nand_bch_correct_data`:

nand_bch_correct_data
=====================

.. c:function:: int nand_bch_correct_data(struct mtd_info *mtd, unsigned char *buf, unsigned char *read_ecc, unsigned char *calc_ecc)

    [NAND Interface] Detect and correct bit error(s)

    :param struct mtd_info \*mtd:
        MTD block structure

    :param unsigned char \*buf:
        raw data read from the chip

    :param unsigned char \*read_ecc:
        ECC from the chip

    :param unsigned char \*calc_ecc:
        the ECC calculated from raw data

.. _`nand_bch_correct_data.description`:

Description
-----------

Detect and correct bit errors for a data byte block

.. _`nand_bch_init`:

nand_bch_init
=============

.. c:function:: struct nand_bch_control *nand_bch_init(struct mtd_info *mtd)

    [NAND Interface] Initialize NAND BCH error correction

    :param struct mtd_info \*mtd:
        MTD block structure

.. _`nand_bch_init.return`:

Return
------

a pointer to a new NAND BCH control structure, or NULL upon failure

Initialize NAND BCH error correction. Parameters \ ``eccsize``\  and \ ``eccbytes``\ 
are used to compute BCH parameters m (Galois field order) and t (error
correction capability). \ ``eccbytes``\  should be equal to the number of bytes
required to store m\*t bits, where m is such that 2^m-1 > \ ``eccsize``\ \*8.

.. _`nand_bch_init.example`:

Example
-------

.. code-block:: c

    to configure 4 bit correction per 512 bytes, you should pass
    @eccsize = 512  (thus, m=13 is the smallest integer such that 2^m-1 > 512*8)
    @eccbytes = 7   (7 bytes are required to store m*t = 13*4 = 52 bits)


.. _`nand_bch_free`:

nand_bch_free
=============

.. c:function:: void nand_bch_free(struct nand_bch_control *nbc)

    [NAND Interface] Release NAND BCH ECC resources

    :param struct nand_bch_control \*nbc:
        NAND BCH control structure

.. This file was automatic generated / don't edit.

