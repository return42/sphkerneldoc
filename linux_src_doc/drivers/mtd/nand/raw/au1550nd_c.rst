.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/raw/au1550nd.c

.. _`au_read_byte`:

au_read_byte
============

.. c:function:: u_char au_read_byte(struct nand_chip *this)

    read one byte from the chip

    :param this:
        NAND chip object
    :type this: struct nand_chip \*

.. _`au_read_byte.description`:

Description
-----------

read function for 8bit buswidth

.. _`au_write_byte`:

au_write_byte
=============

.. c:function:: void au_write_byte(struct nand_chip *this, u_char byte)

    write one byte to the chip

    :param this:
        NAND chip object
    :type this: struct nand_chip \*

    :param byte:
        pointer to data byte to write
    :type byte: u_char

.. _`au_write_byte.description`:

Description
-----------

write function for 8it buswidth

.. _`au_read_byte16`:

au_read_byte16
==============

.. c:function:: u_char au_read_byte16(struct nand_chip *this)

    read one byte endianness aware from the chip

    :param this:
        NAND chip object
    :type this: struct nand_chip \*

.. _`au_read_byte16.description`:

Description
-----------

read function for 16bit buswidth with endianness conversion

.. _`au_write_byte16`:

au_write_byte16
===============

.. c:function:: void au_write_byte16(struct nand_chip *this, u_char byte)

    write one byte endianness aware to the chip

    :param this:
        NAND chip object
    :type this: struct nand_chip \*

    :param byte:
        pointer to data byte to write
    :type byte: u_char

.. _`au_write_byte16.description`:

Description
-----------

write function for 16bit buswidth with endianness conversion

.. _`au_write_buf`:

au_write_buf
============

.. c:function:: void au_write_buf(struct nand_chip *this, const u_char *buf, int len)

    write buffer to chip

    :param this:
        NAND chip object
    :type this: struct nand_chip \*

    :param buf:
        data buffer
    :type buf: const u_char \*

    :param len:
        number of bytes to write
    :type len: int

.. _`au_write_buf.description`:

Description
-----------

write function for 8bit buswidth

.. _`au_read_buf`:

au_read_buf
===========

.. c:function:: void au_read_buf(struct nand_chip *this, u_char *buf, int len)

    read chip data into buffer

    :param this:
        NAND chip object
    :type this: struct nand_chip \*

    :param buf:
        buffer to store date
    :type buf: u_char \*

    :param len:
        number of bytes to read
    :type len: int

.. _`au_read_buf.description`:

Description
-----------

read function for 8bit buswidth

.. _`au_write_buf16`:

au_write_buf16
==============

.. c:function:: void au_write_buf16(struct nand_chip *this, const u_char *buf, int len)

    write buffer to chip

    :param this:
        NAND chip object
    :type this: struct nand_chip \*

    :param buf:
        data buffer
    :type buf: const u_char \*

    :param len:
        number of bytes to write
    :type len: int

.. _`au_write_buf16.description`:

Description
-----------

write function for 16bit buswidth

.. _`au_read_buf16`:

au_read_buf16
=============

.. c:function:: void au_read_buf16(struct mtd_info *mtd, u_char *buf, int len)

    read chip data into buffer

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param buf:
        buffer to store date
    :type buf: u_char \*

    :param len:
        number of bytes to read
    :type len: int

.. _`au_read_buf16.description`:

Description
-----------

read function for 16bit buswidth

.. _`au1550_select_chip`:

au1550_select_chip
==================

.. c:function:: void au1550_select_chip(struct nand_chip *this, int chip)

    control -CE line Forbid driving -CE manually permitting the NAND controller to do this. Keeping -CE asserted during the whole sector reads interferes with the NOR flash and PCMCIA drivers as it causes contention on the static bus. We only have to hold -CE low for the NAND read commands since the flash chip needs it to be asserted during chip not ready time but the NAND controller keeps it released.

    :param this:
        NAND chip object
    :type this: struct nand_chip \*

    :param chip:
        chipnumber to select, -1 for deselect
    :type chip: int

.. _`au1550_command`:

au1550_command
==============

.. c:function:: void au1550_command(struct nand_chip *this, unsigned command, int column, int page_addr)

    Send command to NAND device

    :param this:
        NAND chip object
    :type this: struct nand_chip \*

    :param command:
        the command to be sent
    :type command: unsigned

    :param column:
        the column address for this command, -1 if none
    :type column: int

    :param page_addr:
        the page address for this command, -1 if none
    :type page_addr: int

.. This file was automatic generated / don't edit.

