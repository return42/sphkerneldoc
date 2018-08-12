.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/raw/au1550nd.c

.. _`au_read_byte`:

au_read_byte
============

.. c:function:: u_char au_read_byte(struct mtd_info *mtd)

    read one byte from the chip

    :param struct mtd_info \*mtd:
        MTD device structure

.. _`au_read_byte.description`:

Description
-----------

read function for 8bit buswidth

.. _`au_write_byte`:

au_write_byte
=============

.. c:function:: void au_write_byte(struct mtd_info *mtd, u_char byte)

    write one byte to the chip

    :param struct mtd_info \*mtd:
        MTD device structure

    :param u_char byte:
        pointer to data byte to write

.. _`au_write_byte.description`:

Description
-----------

write function for 8it buswidth

.. _`au_read_byte16`:

au_read_byte16
==============

.. c:function:: u_char au_read_byte16(struct mtd_info *mtd)

    read one byte endianness aware from the chip

    :param struct mtd_info \*mtd:
        MTD device structure

.. _`au_read_byte16.description`:

Description
-----------

read function for 16bit buswidth with endianness conversion

.. _`au_write_byte16`:

au_write_byte16
===============

.. c:function:: void au_write_byte16(struct mtd_info *mtd, u_char byte)

    write one byte endianness aware to the chip

    :param struct mtd_info \*mtd:
        MTD device structure

    :param u_char byte:
        pointer to data byte to write

.. _`au_write_byte16.description`:

Description
-----------

write function for 16bit buswidth with endianness conversion

.. _`au_read_word`:

au_read_word
============

.. c:function:: u16 au_read_word(struct mtd_info *mtd)

    read one word from the chip

    :param struct mtd_info \*mtd:
        MTD device structure

.. _`au_read_word.description`:

Description
-----------

read function for 16bit buswidth without endianness conversion

.. _`au_write_buf`:

au_write_buf
============

.. c:function:: void au_write_buf(struct mtd_info *mtd, const u_char *buf, int len)

    write buffer to chip

    :param struct mtd_info \*mtd:
        MTD device structure

    :param const u_char \*buf:
        data buffer

    :param int len:
        number of bytes to write

.. _`au_write_buf.description`:

Description
-----------

write function for 8bit buswidth

.. _`au_read_buf`:

au_read_buf
===========

.. c:function:: void au_read_buf(struct mtd_info *mtd, u_char *buf, int len)

    read chip data into buffer

    :param struct mtd_info \*mtd:
        MTD device structure

    :param u_char \*buf:
        buffer to store date

    :param int len:
        number of bytes to read

.. _`au_read_buf.description`:

Description
-----------

read function for 8bit buswidth

.. _`au_write_buf16`:

au_write_buf16
==============

.. c:function:: void au_write_buf16(struct mtd_info *mtd, const u_char *buf, int len)

    write buffer to chip

    :param struct mtd_info \*mtd:
        MTD device structure

    :param const u_char \*buf:
        data buffer

    :param int len:
        number of bytes to write

.. _`au_write_buf16.description`:

Description
-----------

write function for 16bit buswidth

.. _`au_read_buf16`:

au_read_buf16
=============

.. c:function:: void au_read_buf16(struct mtd_info *mtd, u_char *buf, int len)

    read chip data into buffer

    :param struct mtd_info \*mtd:
        MTD device structure

    :param u_char \*buf:
        buffer to store date

    :param int len:
        number of bytes to read

.. _`au_read_buf16.description`:

Description
-----------

read function for 16bit buswidth

.. _`au1550_select_chip`:

au1550_select_chip
==================

.. c:function:: void au1550_select_chip(struct mtd_info *mtd, int chip)

    control -CE line Forbid driving -CE manually permitting the NAND controller to do this. Keeping -CE asserted during the whole sector reads interferes with the NOR flash and PCMCIA drivers as it causes contention on the static bus. We only have to hold -CE low for the NAND read commands since the flash chip needs it to be asserted during chip not ready time but the NAND controller keeps it released.

    :param struct mtd_info \*mtd:
        MTD device structure

    :param int chip:
        chipnumber to select, -1 for deselect

.. _`au1550_command`:

au1550_command
==============

.. c:function:: void au1550_command(struct mtd_info *mtd, unsigned command, int column, int page_addr)

    Send command to NAND device

    :param struct mtd_info \*mtd:
        MTD device structure

    :param unsigned command:
        the command to be sent

    :param int column:
        the column address for this command, -1 if none

    :param int page_addr:
        the page address for this command, -1 if none

.. This file was automatic generated / don't edit.

