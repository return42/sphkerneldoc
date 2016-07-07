.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qla2xxx/qla_sup.c

.. _`qla2x00_lock_nvram_access`:

qla2x00_lock_nvram_access
=========================

.. c:function:: void qla2x00_lock_nvram_access(struct qla_hw_data *ha)

    :param struct qla_hw_data \*ha:
        HA context

.. _`qla2x00_unlock_nvram_access`:

qla2x00_unlock_nvram_access
===========================

.. c:function:: void qla2x00_unlock_nvram_access(struct qla_hw_data *ha)

    :param struct qla_hw_data \*ha:
        HA context

.. _`qla2x00_nv_write`:

qla2x00_nv_write
================

.. c:function:: void qla2x00_nv_write(struct qla_hw_data *ha, uint16_t data)

    Prepare for NVRAM read/write operation.

    :param struct qla_hw_data \*ha:
        HA context

    :param uint16_t data:
        Serial interface selector

.. _`qla2x00_nvram_request`:

qla2x00_nvram_request
=====================

.. c:function:: uint16_t qla2x00_nvram_request(struct qla_hw_data *ha, uint32_t nv_cmd)

    Sends read command to NVRAM and gets data from NVRAM.

    :param struct qla_hw_data \*ha:
        HA context

    :param uint32_t nv_cmd:
        NVRAM command

.. _`qla2x00_nvram_request.bit-definitions-for-nvram-command`:

Bit definitions for NVRAM command
---------------------------------


Bit 26     = start bit
Bit 25, 24 = opcode
Bit 23-16  = address
Bit 15-0   = write data

Returns the word read from nvram \ ``addr``\ .

.. _`qla2x00_get_nvram_word`:

qla2x00_get_nvram_word
======================

.. c:function:: uint16_t qla2x00_get_nvram_word(struct qla_hw_data *ha, uint32_t addr)

    Calculates word position in NVRAM and calls the request routine to get the word from NVRAM.

    :param struct qla_hw_data \*ha:
        HA context

    :param uint32_t addr:
        Address in NVRAM to read

.. _`qla2x00_get_nvram_word.description`:

Description
-----------

Returns the word read from nvram \ ``addr``\ .

.. _`qla2x00_nv_deselect`:

qla2x00_nv_deselect
===================

.. c:function:: void qla2x00_nv_deselect(struct qla_hw_data *ha)

    Deselect NVRAM operations.

    :param struct qla_hw_data \*ha:
        HA context

.. _`qla2x00_write_nvram_word`:

qla2x00_write_nvram_word
========================

.. c:function:: void qla2x00_write_nvram_word(struct qla_hw_data *ha, uint32_t addr, uint16_t data)

    Write NVRAM data.

    :param struct qla_hw_data \*ha:
        HA context

    :param uint32_t addr:
        Address in NVRAM to write

    :param uint16_t data:
        word to program

.. _`qla2x00_clear_nvram_protection`:

qla2x00_clear_nvram_protection
==============================

.. c:function:: int qla2x00_clear_nvram_protection(struct qla_hw_data *ha)

    :param struct qla_hw_data \*ha:
        HA context

.. _`qla2x00_flash_enable`:

qla2x00_flash_enable
====================

.. c:function:: void qla2x00_flash_enable(struct qla_hw_data *ha)

    Setup flash for reading and writing.

    :param struct qla_hw_data \*ha:
        HA context

.. _`qla2x00_flash_disable`:

qla2x00_flash_disable
=====================

.. c:function:: void qla2x00_flash_disable(struct qla_hw_data *ha)

    Disable flash and allow RISC to run.

    :param struct qla_hw_data \*ha:
        HA context

.. _`qla2x00_read_flash_byte`:

qla2x00_read_flash_byte
=======================

.. c:function:: uint8_t qla2x00_read_flash_byte(struct qla_hw_data *ha, uint32_t addr)

    Reads a byte from flash

    :param struct qla_hw_data \*ha:
        HA context

    :param uint32_t addr:
        Address in flash to read

.. _`qla2x00_read_flash_byte.description`:

Description
-----------

A word is read from the chip, but, only the lower byte is valid.

Returns the byte read from flash \ ``addr``\ .

.. _`qla2x00_write_flash_byte`:

qla2x00_write_flash_byte
========================

.. c:function:: void qla2x00_write_flash_byte(struct qla_hw_data *ha, uint32_t addr, uint8_t data)

    Write a byte to flash

    :param struct qla_hw_data \*ha:
        HA context

    :param uint32_t addr:
        Address in flash to write

    :param uint8_t data:
        Data to write

.. _`qla2x00_poll_flash`:

qla2x00_poll_flash
==================

.. c:function:: int qla2x00_poll_flash(struct qla_hw_data *ha, uint32_t addr, uint8_t poll_data, uint8_t man_id, uint8_t flash_id)

    Polls flash for completion.

    :param struct qla_hw_data \*ha:
        HA context

    :param uint32_t addr:
        Address in flash to poll

    :param uint8_t poll_data:
        Data to be polled

    :param uint8_t man_id:
        Flash manufacturer ID

    :param uint8_t flash_id:
        Flash ID

.. _`qla2x00_poll_flash.description`:

Description
-----------

This function polls the device until bit 7 of what is read matches data
bit 7 or until data bit 5 becomes a 1.  If that hapens, the flash ROM timed
out (a fatal error).  The flash book recommeds reading bit 7 again after
reading bit 5 as a 1.

Returns 0 on success, else non-zero.

.. _`qla2x00_program_flash_address`:

qla2x00_program_flash_address
=============================

.. c:function:: int qla2x00_program_flash_address(struct qla_hw_data *ha, uint32_t addr, uint8_t data, uint8_t man_id, uint8_t flash_id)

    Programs a flash address

    :param struct qla_hw_data \*ha:
        HA context

    :param uint32_t addr:
        Address in flash to program

    :param uint8_t data:
        Data to be written in flash

    :param uint8_t man_id:
        Flash manufacturer ID

    :param uint8_t flash_id:
        Flash ID

.. _`qla2x00_program_flash_address.description`:

Description
-----------

Returns 0 on success, else non-zero.

.. _`qla2x00_erase_flash`:

qla2x00_erase_flash
===================

.. c:function:: int qla2x00_erase_flash(struct qla_hw_data *ha, uint8_t man_id, uint8_t flash_id)

    Erase the flash.

    :param struct qla_hw_data \*ha:
        HA context

    :param uint8_t man_id:
        Flash manufacturer ID

    :param uint8_t flash_id:
        Flash ID

.. _`qla2x00_erase_flash.description`:

Description
-----------

Returns 0 on success, else non-zero.

.. _`qla2x00_erase_flash_sector`:

qla2x00_erase_flash_sector
==========================

.. c:function:: int qla2x00_erase_flash_sector(struct qla_hw_data *ha, uint32_t addr, uint32_t sec_mask, uint8_t man_id, uint8_t flash_id)

    Erase a flash sector.

    :param struct qla_hw_data \*ha:
        HA context

    :param uint32_t addr:
        Flash sector to erase

    :param uint32_t sec_mask:
        Sector address mask

    :param uint8_t man_id:
        Flash manufacturer ID

    :param uint8_t flash_id:
        Flash ID

.. _`qla2x00_erase_flash_sector.description`:

Description
-----------

Returns 0 on success, else non-zero.

.. _`qla2x00_get_flash_manufacturer`:

qla2x00_get_flash_manufacturer
==============================

.. c:function:: void qla2x00_get_flash_manufacturer(struct qla_hw_data *ha, uint8_t *man_id, uint8_t *flash_id)

    Read manufacturer ID from flash chip.

    :param struct qla_hw_data \*ha:
        *undescribed*

    :param uint8_t \*man_id:
        Flash manufacturer ID

    :param uint8_t \*flash_id:
        Flash ID

.. _`qla2x00_get_fcode_version`:

qla2x00_get_fcode_version
=========================

.. c:function:: void qla2x00_get_fcode_version(struct qla_hw_data *ha, uint32_t pcids)

    Determine an FCODE image's version.

    :param struct qla_hw_data \*ha:
        HA context

    :param uint32_t pcids:
        Pointer to the FCODE PCI data structure

.. _`qla2x00_get_fcode_version.description`:

Description
-----------

The process of retrieving the FCODE version information is at best
described as interesting.

Within the first 100h bytes of the image an ASCII string is present
which contains several pieces of information including the FCODE
version.  Unfortunately it seems the only reliable way to retrieve
the version is by scanning for another sentinel within the string,

.. _`qla2x00_get_fcode_version.the-fcode-build-date`:

the FCODE build date
--------------------


... 2.00.02 10/17/02 ...

Returns QLA_SUCCESS on successful retrieval of version.

.. This file was automatic generated / don't edit.

