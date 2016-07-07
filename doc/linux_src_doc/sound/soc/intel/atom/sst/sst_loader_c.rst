.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/intel/atom/sst/sst_loader.c

.. _`intel_sst_reset_dsp_mrfld`:

intel_sst_reset_dsp_mrfld
=========================

.. c:function:: int intel_sst_reset_dsp_mrfld(struct intel_sst_drv *sst_drv_ctx)

    Resetting SST DSP

    :param struct intel_sst_drv \*sst_drv_ctx:
        *undescribed*

.. _`intel_sst_reset_dsp_mrfld.description`:

Description
-----------

This resets DSP in case of MRFLD platfroms

.. _`sst_start_mrfld`:

sst_start_mrfld
===============

.. c:function:: int sst_start_mrfld(struct intel_sst_drv *sst_drv_ctx)

    Start the SST DSP processor

    :param struct intel_sst_drv \*sst_drv_ctx:
        *undescribed*

.. _`sst_start_mrfld.description`:

Description
-----------

This starts the DSP in MERRIFIELD platfroms

.. _`sst_parse_module_memcpy`:

sst_parse_module_memcpy
=======================

.. c:function:: int sst_parse_module_memcpy(struct intel_sst_drv *sst_drv_ctx, struct fw_module_header *module, struct list_head *memcpy_list)

    Parse audio FW modules and populate the memcpy list

    :param struct intel_sst_drv \*sst_drv_ctx:
        driver context

    :param struct fw_module_header \*module:
        FW module header

    :param struct list_head \*memcpy_list:
        Pointer to the list to be populated
        Create the memcpy list as the number of block to be copied
        returns error or 0 if module sizes are proper

.. _`sst_parse_fw_memcpy`:

sst_parse_fw_memcpy
===================

.. c:function:: int sst_parse_fw_memcpy(struct intel_sst_drv *ctx, unsigned long size, struct list_head *fw_list)

    parse the firmware image & populate the list for memcpy

    :param struct intel_sst_drv \*ctx:
        pointer to drv context

    :param unsigned long size:
        size of the firmware

    :param struct list_head \*fw_list:
        pointer to list_head to be populated
        This function parses the FW image and saves the parsed image in the list
        for memcpy

.. _`sst_do_memcpy`:

sst_do_memcpy
=============

.. c:function:: void sst_do_memcpy(struct list_head *memcpy_list)

    function initiates the memcpy

    :param struct list_head \*memcpy_list:
        Pter to memcpy list on which the memcpy needs to be initiated

.. _`sst_do_memcpy.description`:

Description
-----------

Triggers the memcpy

.. _`sst_load_fw`:

sst_load_fw
===========

.. c:function:: int sst_load_fw(struct intel_sst_drv *sst_drv_ctx)

    function to load FW into DSP Transfers the FW to DSP using dma/memcpy

    :param struct intel_sst_drv \*sst_drv_ctx:
        *undescribed*

.. This file was automatic generated / don't edit.

