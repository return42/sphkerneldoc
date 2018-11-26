.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_eeprom.c

.. _`qib_eeprom_read`:

qib_eeprom_read
===============

.. c:function:: int qib_eeprom_read(struct qib_devdata *dd, u8 eeprom_offset, void *buff, int len)

    receives bytes from the eeprom via I2C

    :param dd:
        the qlogic_ib device
    :type dd: struct qib_devdata \*

    :param eeprom_offset:
        address to read from
    :type eeprom_offset: u8

    :param buff:
        *undescribed*
    :type buff: void \*

    :param len:
        number of bytes to receive
    :type len: int

.. _`qib_eeprom_write`:

qib_eeprom_write
================

.. c:function:: int qib_eeprom_write(struct qib_devdata *dd, u8 eeprom_offset, const void *buff, int len)

    writes data to the eeprom via I2C

    :param dd:
        the qlogic_ib device
    :type dd: struct qib_devdata \*

    :param eeprom_offset:
        where to place data
    :type eeprom_offset: u8

    :param buff:
        *undescribed*
    :type buff: const void \*

    :param len:
        number of bytes to write
    :type len: int

.. _`qib_get_eeprom_info`:

qib_get_eeprom_info
===================

.. c:function:: void qib_get_eeprom_info(struct qib_devdata *dd)

    get the GUID et al. from the TSWI EEPROM device

    :param dd:
        the qlogic_ib device
    :type dd: struct qib_devdata \*

.. _`qib_get_eeprom_info.description`:

Description
-----------

We have the capability to use the nguid field, and get
the guid from the first chip's flash, to use for all of them.

.. This file was automatic generated / don't edit.

