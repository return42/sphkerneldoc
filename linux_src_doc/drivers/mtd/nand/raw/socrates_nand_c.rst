.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/raw/socrates_nand.c

.. _`socrates_nand_write_buf`:

socrates_nand_write_buf
=======================

.. c:function:: void socrates_nand_write_buf(struct nand_chip *this, const uint8_t *buf, int len)

    write buffer to chip

    :param this:
        NAND chip object
    :type this: struct nand_chip \*

    :param buf:
        data buffer
    :type buf: const uint8_t \*

    :param len:
        number of bytes to write
    :type len: int

.. _`socrates_nand_read_buf`:

socrates_nand_read_buf
======================

.. c:function:: void socrates_nand_read_buf(struct nand_chip *this, uint8_t *buf, int len)

    read chip data into buffer

    :param this:
        NAND chip object
    :type this: struct nand_chip \*

    :param buf:
        buffer to store date
    :type buf: uint8_t \*

    :param len:
        number of bytes to read
    :type len: int

.. _`socrates_nand_read_byte`:

socrates_nand_read_byte
=======================

.. c:function:: uint8_t socrates_nand_read_byte(struct nand_chip *this)

    read one byte from the chip

    :param this:
        *undescribed*
    :type this: struct nand_chip \*

.. This file was automatic generated / don't edit.

