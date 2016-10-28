.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/powerplay/smumgr/tonga_smumgr.c

.. _`tonga_set_smc_sram_address`:

tonga_set_smc_sram_address
==========================

.. c:function:: int tonga_set_smc_sram_address(struct pp_smumgr *smumgr, uint32_t smcAddress, uint32_t limit)

    \ ``param``\     smumgr  the address of the powerplay hardware manager. \ ``param``\     smcAddress the address in the SMC RAM to access.

    :param struct pp_smumgr \*smumgr:
        *undescribed*

    :param uint32_t smcAddress:
        *undescribed*

    :param uint32_t limit:
        *undescribed*

.. _`tonga_copy_bytes_to_smc`:

tonga_copy_bytes_to_smc
=======================

.. c:function:: int tonga_copy_bytes_to_smc(struct pp_smumgr *smumgr, uint32_t smcStartAddress, const uint8_t *src, uint32_t byteCount, uint32_t limit)

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

.. _`tonga_copy_bytes_to_smc.description`:

Description
-----------

\ ``param``\     smumgr  the address of the powerplay SMU manager.
\ ``param``\     smcStartAddress the start address in the SMC RAM to copy bytes to.
\ ``param``\     src the byte array to copy the bytes from.
\ ``param``\     byteCount the number of bytes to copy.

.. _`tonga_is_smc_ram_running`:

tonga_is_smc_ram_running
========================

.. c:function:: int tonga_is_smc_ram_running(struct pp_smumgr *smumgr)

    :param struct pp_smumgr \*smumgr:
        *undescribed*

.. _`tonga_is_smc_ram_running.description`:

Description
-----------

\ ``param``\     smumgr  the address of the powerplay hardware manager.

.. _`tonga_send_msg_to_smc`:

tonga_send_msg_to_smc
=====================

.. c:function:: int tonga_send_msg_to_smc(struct pp_smumgr *smumgr, uint16_t msg)

    :param struct pp_smumgr \*smumgr:
        *undescribed*

    :param uint16_t msg:
        *undescribed*

.. _`tonga_send_msg_to_smc.description`:

Description
-----------

\ ``param``\     smumgr  the address of the powerplay hardware manager.
\ ``param``\     msg the message to send.
\ ``return``\    The response that came from the SMC.

.. _`tonga_get_mask_for_firmware_type`:

tonga_get_mask_for_firmware_type
================================

.. c:function:: uint16_t tonga_get_mask_for_firmware_type(uint16_t firmwareType)

    For MEC, we need to check all MEC related type

    :param uint16_t firmwareType:
        *undescribed*

.. _`tonga_check_fw_load_finish`:

tonga_check_fw_load_finish
==========================

.. c:function:: int tonga_check_fw_load_finish(struct pp_smumgr *smumgr, uint32_t fwType)

    SMU will not return if loading has not finished.

    :param struct pp_smumgr \*smumgr:
        *undescribed*

    :param uint32_t fwType:
        *undescribed*

.. _`tonga_smu_upload_firmware_image`:

tonga_smu_upload_firmware_image
===============================

.. c:function:: int tonga_smu_upload_firmware_image(struct pp_smumgr *smumgr)

    :param struct pp_smumgr \*smumgr:
        *undescribed*

.. _`tonga_smu_upload_firmware_image.description`:

Description
-----------

\ ``param``\     smumgr  the address of the powerplay hardware manager.
\ ``param``\     pFirmware the data structure containing the various sections of the firmware.

.. _`tonga_smu_init`:

tonga_smu_init
==============

.. c:function:: int tonga_smu_init(struct pp_smumgr *smumgr)

    ALL PARAMETERS ARE IN HOST BYTE ORDER. \ ``param``\     smumgr  the address of the powerplay hardware manager. \ ``param``\     smcAddress the address in the SMC RAM to access. \ ``param``\     value to write to the SMC SRAM.

    :param struct pp_smumgr \*smumgr:
        *undescribed*

.. This file was automatic generated / don't edit.

