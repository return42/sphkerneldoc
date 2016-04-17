.. -*- coding: utf-8; mode: rst -*-

=============
fiji_smumgr.c
=============


.. _`fiji_set_smc_sram_address`:

fiji_set_smc_sram_address
=========================

.. c:function:: int fiji_set_smc_sram_address (struct pp_smumgr *smumgr, uint32_t smc_addr, uint32_t limit)

    :param struct pp_smumgr \*smumgr:

        *undescribed*

    :param uint32_t smc_addr:

        *undescribed*

    :param uint32_t limit:

        *undescribed*



.. _`fiji_set_smc_sram_address.description`:

Description
-----------

``param``    smumgr  the address of the powerplay hardware manager.
``param``    smc_addr the address in the SMC RAM to access.



.. _`fiji_copy_bytes_to_smc`:

fiji_copy_bytes_to_smc
======================

.. c:function:: int fiji_copy_bytes_to_smc (struct pp_smumgr *smumgr, uint32_t smcStartAddress, const uint8_t *src, uint32_t byteCount, uint32_t limit)

    :param struct pp_smumgr \*smumgr:

        *undescribed*

    :param uint32_t smcStartAddress:

        *undescribed*

    :param const uint8_t \*src:

        *undescribed*

    :param uint32_t byteCount:

        *undescribed*

    :param uint32_t limit:

        *undescribed*



.. _`fiji_copy_bytes_to_smc.description`:

Description
-----------


``param``    smumgr  the address of the powerplay SMU manager.
``param``    smcStartAddress the start address in the SMC RAM to copy bytes to.
``param``    src the byte array to copy the bytes from.
``param``    byteCount the number of bytes to copy.



.. _`fiji_is_smc_ram_running`:

fiji_is_smc_ram_running
=======================

.. c:function:: bool fiji_is_smc_ram_running (struct pp_smumgr *smumgr)

    :param struct pp_smumgr \*smumgr:

        *undescribed*



.. _`fiji_is_smc_ram_running.description`:

Description
-----------


``param``    smumgr  the address of the powerplay hardware manager.



.. _`fiji_send_msg_to_smc`:

fiji_send_msg_to_smc
====================

.. c:function:: int fiji_send_msg_to_smc (struct pp_smumgr *smumgr, uint16_t msg)

    :param struct pp_smumgr \*smumgr:

        *undescribed*

    :param uint16_t msg:

        *undescribed*



.. _`fiji_send_msg_to_smc.description`:

Description
-----------


``param``    smumgr  the address of the powerplay hardware manager.
``param``    msg the message to send.
``return``   The response that came from the SMC.



.. _`fiji_send_msg_to_smc_with_parameter`:

fiji_send_msg_to_smc_with_parameter
===================================

.. c:function:: int fiji_send_msg_to_smc_with_parameter (struct pp_smumgr *smumgr, uint16_t msg, uint32_t parameter)

    :param struct pp_smumgr \*smumgr:

        *undescribed*

    :param uint16_t msg:

        *undescribed*

    :param uint32_t parameter:

        *undescribed*



.. _`fiji_send_msg_to_smc_with_parameter_without_waiting`:

fiji_send_msg_to_smc_with_parameter_without_waiting
===================================================

.. c:function:: int fiji_send_msg_to_smc_with_parameter_without_waiting (struct pp_smumgr *smumgr, uint16_t msg, uint32_t parameter)

    :param struct pp_smumgr \*smumgr:

        *undescribed*

    :param uint16_t msg:

        *undescribed*

    :param uint32_t parameter:

        *undescribed*



.. _`fiji_upload_smu_firmware_image`:

fiji_upload_smu_firmware_image
==============================

.. c:function:: int fiji_upload_smu_firmware_image (struct pp_smumgr *smumgr)

    :param struct pp_smumgr \*smumgr:

        *undescribed*



.. _`fiji_upload_smu_firmware_image.description`:

Description
-----------


``param``    smumgr  the address of the powerplay SMU manager.
``return``   0 or -1.



.. _`fiji_read_smc_sram_dword`:

fiji_read_smc_sram_dword
========================

.. c:function:: int fiji_read_smc_sram_dword (struct pp_smumgr *smumgr, uint32_t smc_addr, uint32_t *value, uint32_t limit)

    :param struct pp_smumgr \*smumgr:

        *undescribed*

    :param uint32_t smc_addr:

        *undescribed*

    :param uint32_t \*value:

        *undescribed*

    :param uint32_t limit:

        *undescribed*



.. _`fiji_read_smc_sram_dword.description`:

Description
-----------

ALL PARAMETERS ARE IN HOST BYTE ORDER.
``param``    smumgr  the address of the powerplay hardware manager.
``param``    smc_addr the address in the SMC RAM to access.
``param``    value and output parameter for the data read from the SMC SRAM.



.. _`fiji_write_smc_sram_dword`:

fiji_write_smc_sram_dword
=========================

.. c:function:: int fiji_write_smc_sram_dword (struct pp_smumgr *smumgr, uint32_t smc_addr, uint32_t value, uint32_t limit)

    :param struct pp_smumgr \*smumgr:

        *undescribed*

    :param uint32_t smc_addr:

        *undescribed*

    :param uint32_t value:

        *undescribed*

    :param uint32_t limit:

        *undescribed*



.. _`fiji_write_smc_sram_dword.description`:

Description
-----------

ALL PARAMETERS ARE IN HOST BYTE ORDER.
``param``    smumgr  the address of the powerplay hardware manager.
``param``    smc_addr the address in the SMC RAM to access.
``param``    value to write to the SMC SRAM.



.. _`fiji_smu_init`:

fiji_smu_init
=============

.. c:function:: int fiji_smu_init (struct pp_smumgr *smumgr)

    :param struct pp_smumgr \*smumgr:

        *undescribed*



.. _`fiji_smu_init.description`:

Description
-----------

ALL PARAMETERS ARE IN HOST BYTE ORDER.
``param``    smumgr  the address of the powerplay hardware manager.
``param``    smc_addr the address in the SMC RAM to access.
``param``    value to write to the SMC SRAM.

