.. -*- coding: utf-8; mode: rst -*-

==============
eeprom_93cx6.c
==============


.. _`eeprom_93cx6_read`:

eeprom_93cx6_read
=================

.. c:function:: void eeprom_93cx6_read (struct eeprom_93cx6 *eeprom, const u8 word, u16 *data)

    Read a word from eeprom

    :param struct eeprom_93cx6 \*eeprom:
        Pointer to eeprom structure

    :param const u8 word:
        Word index from where we should start reading

    :param u16 \*data:
        target pointer where the information will have to be stored



.. _`eeprom_93cx6_read.description`:

Description
-----------

This function will read the eeprom data as host-endian word
into the given data pointer.



.. _`eeprom_93cx6_multiread`:

eeprom_93cx6_multiread
======================

.. c:function:: void eeprom_93cx6_multiread (struct eeprom_93cx6 *eeprom, const u8 word, __le16 *data, const u16 words)

    Read multiple words from eeprom

    :param struct eeprom_93cx6 \*eeprom:
        Pointer to eeprom structure

    :param const u8 word:
        Word index from where we should start reading

    :param __le16 \*data:
        target pointer where the information will have to be stored

    :param const u16 words:
        Number of words that should be read.



.. _`eeprom_93cx6_multiread.description`:

Description
-----------

This function will read all requested words from the eeprom,
this is done by calling :c:func:`eeprom_93cx6_read` multiple times.
But with the additional change that while the eeprom_93cx6_read
will return host ordered bytes, this method will return little
endian words.



.. _`eeprom_93cx6_readb`:

eeprom_93cx6_readb
==================

.. c:function:: void eeprom_93cx6_readb (struct eeprom_93cx6 *eeprom, const u8 byte, u8 *data)

    Read a byte from eeprom

    :param struct eeprom_93cx6 \*eeprom:
        Pointer to eeprom structure

    :param const u8 byte:

        *undescribed*

    :param u8 \*data:
        target pointer where the information will have to be stored



.. _`eeprom_93cx6_readb.description`:

Description
-----------

This function will read a byte of the eeprom data
into the given data pointer.



.. _`eeprom_93cx6_multireadb`:

eeprom_93cx6_multireadb
=======================

.. c:function:: void eeprom_93cx6_multireadb (struct eeprom_93cx6 *eeprom, const u8 byte, u8 *data, const u16 bytes)

    Read multiple bytes from eeprom

    :param struct eeprom_93cx6 \*eeprom:
        Pointer to eeprom structure

    :param const u8 byte:
        Index from where we should start reading

    :param u8 \*data:
        target pointer where the information will have to be stored

    :param const u16 bytes:

        *undescribed*



.. _`eeprom_93cx6_multireadb.description`:

Description
-----------

This function will read all requested bytes from the eeprom,
this is done by calling :c:func:`eeprom_93cx6_readb` multiple times.



.. _`eeprom_93cx6_wren`:

eeprom_93cx6_wren
=================

.. c:function:: void eeprom_93cx6_wren (struct eeprom_93cx6 *eeprom, bool enable)

    set the write enable state

    :param struct eeprom_93cx6 \*eeprom:
        Pointer to eeprom structure

    :param bool enable:
        true to enable writes, otherwise disable writes



.. _`eeprom_93cx6_wren.description`:

Description
-----------

Set the EEPROM write enable state to either allow or deny
writes depending on the ``enable`` value.



.. _`eeprom_93cx6_write`:

eeprom_93cx6_write
==================

.. c:function:: void eeprom_93cx6_write (struct eeprom_93cx6 *eeprom, u8 addr, u16 data)

    write data to the EEPROM

    :param struct eeprom_93cx6 \*eeprom:
        Pointer to eeprom structure

    :param u8 addr:
        Address to write data to.

    :param u16 data:
        The data to write to address ``addr``\ .



.. _`eeprom_93cx6_write.description`:

Description
-----------

Write the ``data`` to the specified ``addr`` in the EEPROM and
waiting for the device to finish writing.

Note, since we do not expect large number of write operations
we delay in between parts of the operation to avoid using excessive
amounts of CPU time busy waiting.

