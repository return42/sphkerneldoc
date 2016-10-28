.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/socrates_nand.c

.. _`socrates_nand_write_buf`:

socrates_nand_write_buf
=======================

.. c:function:: void socrates_nand_write_buf(struct mtd_info *mtd, const uint8_t *buf, int len)

    write buffer to chip

    :param struct mtd_info \*mtd:
        MTD device structure

    :param const uint8_t \*buf:
        data buffer

    :param int len:
        number of bytes to write

.. _`socrates_nand_read_buf`:

socrates_nand_read_buf
======================

.. c:function:: void socrates_nand_read_buf(struct mtd_info *mtd, uint8_t *buf, int len)

    read chip data into buffer

    :param struct mtd_info \*mtd:
        MTD device structure

    :param uint8_t \*buf:
        buffer to store date

    :param int len:
        number of bytes to read

.. _`socrates_nand_read_byte`:

socrates_nand_read_byte
=======================

.. c:function:: uint8_t socrates_nand_read_byte(struct mtd_info *mtd)

    read one byte from the chip

    :param struct mtd_info \*mtd:
        MTD device structure

.. _`socrates_nand_read_word`:

socrates_nand_read_word
=======================

.. c:function:: uint16_t socrates_nand_read_word(struct mtd_info *mtd)

    read one word from the chip

    :param struct mtd_info \*mtd:
        MTD device structure

.. This file was automatic generated / don't edit.

