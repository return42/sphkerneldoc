.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/mtk-vpu/mtk_vpu.h

.. _`ipi_handler_t`:

ipi_handler_t
=============

.. c:function:: void ipi_handler_t(void *data, unsigned int len, void *priv)

    related to video codec, scaling and color format converting. VPU interfaces with other blocks by share memory and interrupt.

    :param void \*data:
        *undescribed*

    :param unsigned int len:
        *undescribed*

    :param void \*priv:
        *undescribed*

.. _`ipi_id`:

enum ipi_id
===========

.. c:type:: enum ipi_id

    the id of inter-processor interrupt

.. _`ipi_id.definition`:

Definition
----------

.. code-block:: c

    enum ipi_id {
        IPI_VPU_INIT,
        IPI_VENC_H264,
        IPI_VENC_VP8,
        IPI_MAX
    };

.. _`ipi_id.constants`:

Constants
---------

IPI_VPU_INIT
    The interrupt from vpu is to notfiy kernel

IPI_VENC_H264
    The interrupt from vpu is to notify kernel to

IPI_VENC_VP8
    The interrupt fro vpu is to notify kernel to

IPI_MAX
    The maximum IPI number

.. _`rst_id`:

enum rst_id
===========

.. c:type:: enum rst_id

    reset id to register reset function for VPU watchdog timeout

.. _`rst_id.definition`:

Definition
----------

.. code-block:: c

    enum rst_id {
        VPU_RST_ENC,
        VPU_RST_MAX
    };

.. _`rst_id.constants`:

Constants
---------

VPU_RST_ENC
    encoder reset id

VPU_RST_MAX
    maximum reset id

.. _`vpu_ipi_register`:

vpu_ipi_register
================

.. c:function:: int vpu_ipi_register(struct platform_device *pdev, enum ipi_id id, ipi_handler_t handler, const char *name, void *priv)

    register an ipi function

    :param struct platform_device \*pdev:
        VPU platform device

    :param enum ipi_id id:
        IPI ID

    :param ipi_handler_t handler:
        IPI handler

    :param const char \*name:
        IPI name

    :param void \*priv:
        private data for IPI handler

.. _`vpu_ipi_register.description`:

Description
-----------

Register an ipi function to receive ipi interrupt from VPU.

.. _`vpu_ipi_register.return`:

Return
------

Return 0 if ipi registers successfully, otherwise it is failed.

.. _`vpu_ipi_send`:

vpu_ipi_send
============

.. c:function:: int vpu_ipi_send(struct platform_device *pdev, enum ipi_id id, void *buf, unsigned int len)

    send data from AP to vpu.

    :param struct platform_device \*pdev:
        VPU platform device

    :param enum ipi_id id:
        IPI ID

    :param void \*buf:
        the data buffer

    :param unsigned int len:
        the data buffer length

.. _`vpu_ipi_send.description`:

Description
-----------

This function is thread-safe. When this function returns,
VPU has received the data and starts the processing.
When the processing completes, IPI handler registered
by vpu_ipi_register will be called in interrupt context.

.. _`vpu_ipi_send.return`:

Return
------

Return 0 if sending data successfully, otherwise it is failed.

.. _`vpu_get_plat_device`:

vpu_get_plat_device
===================

.. c:function:: struct platform_device *vpu_get_plat_device(struct platform_device *pdev)

    get VPU's platform device

    :param struct platform_device \*pdev:
        the platform device of the module requesting VPU platform
        device for using VPU API.

.. _`vpu_get_plat_device.return`:

Return
------

Return NULL if it is failed.
otherwise it is VPU's platform device

.. _`vpu_wdt_reg_handler`:

vpu_wdt_reg_handler
===================

.. c:function:: int vpu_wdt_reg_handler(struct platform_device *pdev, void vpu_wdt_reset_func(void *), void *priv, enum rst_id id)

    register a VPU watchdog handler

    :param struct platform_device \*pdev:
        VPU platform device

    :param void vpu_wdt_reset_func(void \*):
        *undescribed*

    :param void \*priv:
        *undescribed*

    :param enum rst_id id:
        *undescribed*

.. _`vpu_wdt_reg_handler.description`:

Description
-----------

Register a handler performing own tasks when vpu reset by watchdog

.. _`vpu_wdt_reg_handler.return`:

Return
------

Return 0 if the handler is added successfully,
otherwise it is failed.

.. _`vpu_get_venc_hw_capa`:

vpu_get_venc_hw_capa
====================

.. c:function:: unsigned int vpu_get_venc_hw_capa(struct platform_device *pdev)

    get video encoder hardware capability

    :param struct platform_device \*pdev:
        VPU platform device

.. _`vpu_get_venc_hw_capa.return`:

Return
------

video encoder hardware capability

.. _`vpu_load_firmware`:

vpu_load_firmware
=================

.. c:function:: int vpu_load_firmware(struct platform_device *pdev)

    download VPU firmware and boot it

    :param struct platform_device \*pdev:
        VPU platform device

.. _`vpu_load_firmware.return`:

Return
------

Return 0 if downloading firmware successfully,
otherwise it is failed

.. _`vpu_mapping_dm_addr`:

vpu_mapping_dm_addr
===================

.. c:function:: void *vpu_mapping_dm_addr(struct platform_device *pdev, u32 dtcm_dmem_addr)

    Mapping DTCM/DMEM to kernel virtual address

    :param struct platform_device \*pdev:
        VPU platform device

    :param u32 dtcm_dmem_addr:
        *undescribed*

.. _`vpu_mapping_dm_addr.description`:

Description
-----------

Mapping the VPU's DTCM (Data Tightly-Coupled Memory) /
DMEM (Data Extended Memory) memory address to
kernel virtual address.

.. _`vpu_mapping_dm_addr.return`:

Return
------

Return ERR_PTR(-EINVAL) if mapping failed,
otherwise the mapped kernel virtual address

.. This file was automatic generated / don't edit.

