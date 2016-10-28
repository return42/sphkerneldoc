.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/powerplay/smumgr/polaris10_smumgr.c

.. _`polaris10_set_smc_sram_address`:

polaris10_set_smc_sram_address
==============================

.. c:function:: int polaris10_set_smc_sram_address(struct pp_smumgr *smumgr, uint32_t smc_addr, uint32_t limit)

    \ ``param``\     smumgr  the address of the powerplay hardware manager. \ ``param``\     smcAddress the address in the SMC RAM to access.

    :param struct pp_smumgr \*smumgr:
        *undescribed*

    :param uint32_t smc_addr:
        *undescribed*

    :param uint32_t limit:
        *undescribed*

.. _`polaris10_copy_bytes_from_smc`:

polaris10_copy_bytes_from_smc
=============================

.. c:function:: int polaris10_copy_bytes_from_smc(struct pp_smumgr *smumgr, uint32_t smc_start_address, uint32_t *dest, uint32_t byte_count, uint32_t limit)

    :param struct pp_smumgr \*smumgr:
        *undescribed*

    :param uint32_t smc_start_address:
        *undescribed*

    :param uint32_t \*dest:
        *undescribed*

    :param uint32_t byte_count:
        *undescribed*

    :param uint32_t limit:
        *undescribed*

.. _`polaris10_copy_bytes_from_smc.description`:

Description
-----------

\ ``param``\     smumgr  the address of the powerplay SMU manager.
\ ``param``\     smc_start_address the start address in the SMC RAM to copy bytes from
\ ``param``\     src the byte array to copy the bytes to.
\ ``param``\     byte_count the number of bytes to copy.

.. _`polaris10_copy_bytes_to_smc`:

polaris10_copy_bytes_to_smc
===========================

.. c:function:: int polaris10_copy_bytes_to_smc(struct pp_smumgr *smumgr, uint32_t smc_start_address, const uint8_t *src, uint32_t byte_count, uint32_t limit)

    :param struct pp_smumgr \*smumgr:
        *undescribed*

    :param uint32_t smc_start_address:
        *undescribed*

    :param const uint8_t \*src:
        *undescribed*

    :param uint32_t byte_count:
        *undescribed*

    :param uint32_t limit:
        *undescribed*

.. _`polaris10_copy_bytes_to_smc.description`:

Description
-----------

\ ``param``\     pSmuMgr  the address of the powerplay SMU manager.
\ ``param``\     smc_start_address the start address in the SMC RAM to copy bytes to.
\ ``param``\     src the byte array to copy the bytes from.
\ ``param``\     byte_count the number of bytes to copy.

.. _`polaris10_is_smc_ram_running`:

polaris10_is_smc_ram_running
============================

.. c:function:: bool polaris10_is_smc_ram_running(struct pp_smumgr *smumgr)

    :param struct pp_smumgr \*smumgr:
        *undescribed*

.. _`polaris10_is_smc_ram_running.description`:

Description
-----------

\ ``param``\     smumgr  the address of the powerplay hardware manager.

.. _`polaris10_send_msg_to_smc`:

polaris10_send_msg_to_smc
=========================

.. c:function:: int polaris10_send_msg_to_smc(struct pp_smumgr *smumgr, uint16_t msg)

    :param struct pp_smumgr \*smumgr:
        *undescribed*

    :param uint16_t msg:
        *undescribed*

.. _`polaris10_send_msg_to_smc.description`:

Description
-----------

\ ``param``\     smumgr  the address of the powerplay hardware manager.
\ ``param``\     msg the message to send.
\ ``return``\    The response that came from the SMC.

.. _`polaris10_send_msg_to_smc_without_waiting`:

polaris10_send_msg_to_smc_without_waiting
=========================================

.. c:function:: int polaris10_send_msg_to_smc_without_waiting(struct pp_smumgr *smumgr, uint16_t msg)

    :param struct pp_smumgr \*smumgr:
        *undescribed*

    :param uint16_t msg:
        *undescribed*

.. _`polaris10_send_msg_to_smc_without_waiting.description`:

Description
-----------

\ ``param``\     smumgr  the address of the powerplay hardware manager.
\ ``param``\     msg the message to send.
\ ``return``\    Always return 0.

.. _`polaris10_send_msg_to_smc_with_parameter`:

polaris10_send_msg_to_smc_with_parameter
========================================

.. c:function:: int polaris10_send_msg_to_smc_with_parameter(struct pp_smumgr *smumgr, uint16_t msg, uint32_t parameter)

    :param struct pp_smumgr \*smumgr:
        *undescribed*

    :param uint16_t msg:
        *undescribed*

    :param uint32_t parameter:
        *undescribed*

.. _`polaris10_send_msg_to_smc_with_parameter_without_waiting`:

polaris10_send_msg_to_smc_with_parameter_without_waiting
========================================================

.. c:function:: int polaris10_send_msg_to_smc_with_parameter_without_waiting(struct pp_smumgr *smumgr, uint16_t msg, uint32_t parameter)

    :param struct pp_smumgr \*smumgr:
        *undescribed*

    :param uint16_t msg:
        *undescribed*

    :param uint32_t parameter:
        *undescribed*

.. _`polaris10_wait_for_smc_inactive`:

polaris10_wait_for_smc_inactive
===============================

.. c:function:: int polaris10_wait_for_smc_inactive(struct pp_smumgr *smumgr)

    :param struct pp_smumgr \*smumgr:
        *undescribed*

.. _`polaris10_wait_for_smc_inactive.description`:

Description
-----------

\ ``param``\     smumgr  the address of the powerplay hardware manager.
\ ``param``\     msg the message to send.
\ ``return``\    The response that came from the SMC.

.. _`polaris10_upload_smc_firmware_data`:

polaris10_upload_smc_firmware_data
==================================

.. c:function:: int polaris10_upload_smc_firmware_data(struct pp_smumgr *smumgr, uint32_t length, uint32_t *src, uint32_t limit)

    :param struct pp_smumgr \*smumgr:
        *undescribed*

    :param uint32_t length:
        *undescribed*

    :param uint32_t \*src:
        *undescribed*

    :param uint32_t limit:
        *undescribed*

.. _`polaris10_upload_smc_firmware_data.description`:

Description
-----------

\ ``param``\     smumgr  the address of the powerplay hardware manager.
\ ``param``\     pFirmware the data structure containing the various sections of the firmware.

.. _`polaris10_read_smc_sram_dword`:

polaris10_read_smc_sram_dword
=============================

.. c:function:: int polaris10_read_smc_sram_dword(struct pp_smumgr *smumgr, uint32_t smc_addr, uint32_t *value, uint32_t limit)

    ALL PARAMETERS ARE IN HOST BYTE ORDER. \ ``param``\     smumgr  the address of the powerplay hardware manager. \ ``param``\     smcAddress the address in the SMC RAM to access. \ ``param``\     value and output parameter for the data read from the SMC SRAM.

    :param struct pp_smumgr \*smumgr:
        *undescribed*

    :param uint32_t smc_addr:
        *undescribed*

    :param uint32_t \*value:
        *undescribed*

    :param uint32_t limit:
        *undescribed*

.. _`polaris10_write_smc_sram_dword`:

polaris10_write_smc_sram_dword
==============================

.. c:function:: int polaris10_write_smc_sram_dword(struct pp_smumgr *smumgr, uint32_t smc_addr, uint32_t value, uint32_t limit)

    ALL PARAMETERS ARE IN HOST BYTE ORDER. \ ``param``\     smumgr  the address of the powerplay hardware manager. \ ``param``\     smc_addr the address in the SMC RAM to access. \ ``param``\     value to write to the SMC SRAM.

    :param struct pp_smumgr \*smumgr:
        *undescribed*

    :param uint32_t smc_addr:
        *undescribed*

    :param uint32_t value:
        *undescribed*

    :param uint32_t limit:
        *undescribed*

.. This file was automatic generated / don't edit.

