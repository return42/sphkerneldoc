.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/mpt3sas/mpt3sas_config.c

.. _`config_request`:

struct config_request
=====================

.. c:type:: struct config_request

    obtain dma memory via routine

.. _`config_request.definition`:

Definition
----------

.. code-block:: c

    struct config_request {
        u16 sz;
        void *page;
        dma_addr_t page_dma;
    }

.. _`config_request.members`:

Members
-------

sz
    size

page
    virt pointer

page_dma
    phys pointer

.. _`_config_display_some_debug`:

\_config_display_some_debug
===========================

.. c:function:: void _config_display_some_debug(struct MPT3SAS_ADAPTER *ioc, u16 smid, char *calling_function_name, MPI2DefaultReply_t *mpi_reply)

    debug routine

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param smid:
        system request message index
    :type smid: u16

    :param calling_function_name:
        string pass from calling function
    :type calling_function_name: char \*

    :param mpi_reply:
        reply message frame
    :type mpi_reply: MPI2DefaultReply_t \*

.. _`_config_display_some_debug.context`:

Context
-------

none.

.. _`_config_display_some_debug.description`:

Description
-----------

Function for displaying debug info helpful when debugging issues
in this module.

.. _`_config_alloc_config_dma_memory`:

\_config_alloc_config_dma_memory
================================

.. c:function:: int _config_alloc_config_dma_memory(struct MPT3SAS_ADAPTER *ioc, struct config_request *mem)

    obtain physical memory

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mem:
        struct config_request
    :type mem: struct config_request \*

.. _`_config_alloc_config_dma_memory.description`:

Description
-----------

A wrapper for obtaining dma-able memory for config page request.

.. _`_config_alloc_config_dma_memory.return`:

Return
------

0 for success, non-zero for failure.

.. _`_config_free_config_dma_memory`:

\_config_free_config_dma_memory
===============================

.. c:function:: void _config_free_config_dma_memory(struct MPT3SAS_ADAPTER *ioc, struct config_request *mem)

    wrapper to free the memory

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mem:
        struct config_request
    :type mem: struct config_request \*

.. _`_config_free_config_dma_memory.description`:

Description
-----------

A wrapper to free dma-able memory when using \_config_alloc_config_dma_memory.

.. _`_config_free_config_dma_memory.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_done`:

mpt3sas_config_done
===================

.. c:function:: u8 mpt3sas_config_done(struct MPT3SAS_ADAPTER *ioc, u16 smid, u8 msix_index, u32 reply)

    config page completion routine

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param smid:
        system request message index
    :type smid: u16

    :param msix_index:
        MSIX table index supplied by the OS
    :type msix_index: u8

    :param reply:
        reply message frame(lower 32bit addr)
    :type reply: u32

.. _`mpt3sas_config_done.context`:

Context
-------

none.

.. _`mpt3sas_config_done.description`:

Description
-----------

The callback handler when using \_config_request.

.. _`mpt3sas_config_done.return`:

Return
------

1 meaning mf should be freed from \_base_interrupt
0 means the mf is freed from this function.

.. _`_config_request`:

\_config_request
================

.. c:function:: int _config_request(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigRequest_t *mpi_request, Mpi2ConfigReply_t *mpi_reply, int timeout, void *config_page, u16 config_page_sz)

    main routine for sending config page requests

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_request:
        request message frame
    :type mpi_request: Mpi2ConfigRequest_t \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param timeout:
        timeout in seconds
    :type timeout: int

    :param config_page:
        contents of the config page
    :type config_page: void \*

    :param config_page_sz:
        size of config page
    :type config_page_sz: u16

.. _`_config_request.context`:

Context
-------

sleep

.. _`_config_request.description`:

Description
-----------

A generic API for config page requests to firmware.

The ioc->config_cmds.status flag should be MPT3_CMD_NOT_USED before calling
this API.

The callback index is set inside \`ioc->config_cb_idx.

.. _`_config_request.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_manufacturing_pg0`:

mpt3sas_config_get_manufacturing_pg0
====================================

.. c:function:: int mpt3sas_config_get_manufacturing_pg0(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2ManufacturingPage0_t *config_page)

    obtain manufacturing page 0

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: Mpi2ManufacturingPage0_t \*

.. _`mpt3sas_config_get_manufacturing_pg0.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_manufacturing_pg0.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_manufacturing_pg7`:

mpt3sas_config_get_manufacturing_pg7
====================================

.. c:function:: int mpt3sas_config_get_manufacturing_pg7(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2ManufacturingPage7_t *config_page, u16 sz)

    obtain manufacturing page 7

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: Mpi2ManufacturingPage7_t \*

    :param sz:
        size of buffer passed in config_page
    :type sz: u16

.. _`mpt3sas_config_get_manufacturing_pg7.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_manufacturing_pg7.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_manufacturing_pg10`:

mpt3sas_config_get_manufacturing_pg10
=====================================

.. c:function:: int mpt3sas_config_get_manufacturing_pg10(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, struct Mpi2ManufacturingPage10_t *config_page)

    obtain manufacturing page 10

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: struct Mpi2ManufacturingPage10_t \*

.. _`mpt3sas_config_get_manufacturing_pg10.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_manufacturing_pg10.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_manufacturing_pg11`:

mpt3sas_config_get_manufacturing_pg11
=====================================

.. c:function:: int mpt3sas_config_get_manufacturing_pg11(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, struct Mpi2ManufacturingPage11_t *config_page)

    obtain manufacturing page 11

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: struct Mpi2ManufacturingPage11_t \*

.. _`mpt3sas_config_get_manufacturing_pg11.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_manufacturing_pg11.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_set_manufacturing_pg11`:

mpt3sas_config_set_manufacturing_pg11
=====================================

.. c:function:: int mpt3sas_config_set_manufacturing_pg11(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, struct Mpi2ManufacturingPage11_t *config_page)

    set manufacturing page 11

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: struct Mpi2ManufacturingPage11_t \*

.. _`mpt3sas_config_set_manufacturing_pg11.context`:

Context
-------

sleep.

.. _`mpt3sas_config_set_manufacturing_pg11.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_bios_pg2`:

mpt3sas_config_get_bios_pg2
===========================

.. c:function:: int mpt3sas_config_get_bios_pg2(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2BiosPage2_t *config_page)

    obtain bios page 2

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: Mpi2BiosPage2_t \*

.. _`mpt3sas_config_get_bios_pg2.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_bios_pg2.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_bios_pg3`:

mpt3sas_config_get_bios_pg3
===========================

.. c:function:: int mpt3sas_config_get_bios_pg3(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2BiosPage3_t *config_page)

    obtain bios page 3

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: Mpi2BiosPage3_t \*

.. _`mpt3sas_config_get_bios_pg3.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_bios_pg3.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_iounit_pg0`:

mpt3sas_config_get_iounit_pg0
=============================

.. c:function:: int mpt3sas_config_get_iounit_pg0(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2IOUnitPage0_t *config_page)

    obtain iounit page 0

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: Mpi2IOUnitPage0_t \*

.. _`mpt3sas_config_get_iounit_pg0.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_iounit_pg0.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_iounit_pg1`:

mpt3sas_config_get_iounit_pg1
=============================

.. c:function:: int mpt3sas_config_get_iounit_pg1(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2IOUnitPage1_t *config_page)

    obtain iounit page 1

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: Mpi2IOUnitPage1_t \*

.. _`mpt3sas_config_get_iounit_pg1.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_iounit_pg1.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_set_iounit_pg1`:

mpt3sas_config_set_iounit_pg1
=============================

.. c:function:: int mpt3sas_config_set_iounit_pg1(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2IOUnitPage1_t *config_page)

    set iounit page 1

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: Mpi2IOUnitPage1_t \*

.. _`mpt3sas_config_set_iounit_pg1.context`:

Context
-------

sleep.

.. _`mpt3sas_config_set_iounit_pg1.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_iounit_pg3`:

mpt3sas_config_get_iounit_pg3
=============================

.. c:function:: int mpt3sas_config_get_iounit_pg3(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2IOUnitPage3_t *config_page, u16 sz)

    obtain iounit page 3

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: Mpi2IOUnitPage3_t \*

    :param sz:
        size of buffer passed in config_page
    :type sz: u16

.. _`mpt3sas_config_get_iounit_pg3.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_iounit_pg3.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_iounit_pg8`:

mpt3sas_config_get_iounit_pg8
=============================

.. c:function:: int mpt3sas_config_get_iounit_pg8(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2IOUnitPage8_t *config_page)

    obtain iounit page 8

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: Mpi2IOUnitPage8_t \*

.. _`mpt3sas_config_get_iounit_pg8.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_iounit_pg8.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_ioc_pg8`:

mpt3sas_config_get_ioc_pg8
==========================

.. c:function:: int mpt3sas_config_get_ioc_pg8(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2IOCPage8_t *config_page)

    obtain ioc page 8

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: Mpi2IOCPage8_t \*

.. _`mpt3sas_config_get_ioc_pg8.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_ioc_pg8.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_sas_device_pg0`:

mpt3sas_config_get_sas_device_pg0
=================================

.. c:function:: int mpt3sas_config_get_sas_device_pg0(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2SasDevicePage0_t *config_page, u32 form, u32 handle)

    obtain sas device page 0

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: Mpi2SasDevicePage0_t \*

    :param form:
        GET_NEXT_HANDLE or HANDLE
    :type form: u32

    :param handle:
        device handle
    :type handle: u32

.. _`mpt3sas_config_get_sas_device_pg0.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_sas_device_pg0.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_sas_device_pg1`:

mpt3sas_config_get_sas_device_pg1
=================================

.. c:function:: int mpt3sas_config_get_sas_device_pg1(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2SasDevicePage1_t *config_page, u32 form, u32 handle)

    obtain sas device page 1

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: Mpi2SasDevicePage1_t \*

    :param form:
        GET_NEXT_HANDLE or HANDLE
    :type form: u32

    :param handle:
        device handle
    :type handle: u32

.. _`mpt3sas_config_get_sas_device_pg1.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_sas_device_pg1.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_pcie_device_pg0`:

mpt3sas_config_get_pcie_device_pg0
==================================

.. c:function:: int mpt3sas_config_get_pcie_device_pg0(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi26PCIeDevicePage0_t *config_page, u32 form, u32 handle)

    obtain pcie device page 0

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: Mpi26PCIeDevicePage0_t \*

    :param form:
        GET_NEXT_HANDLE or HANDLE
    :type form: u32

    :param handle:
        device handle
    :type handle: u32

.. _`mpt3sas_config_get_pcie_device_pg0.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_pcie_device_pg0.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_pcie_device_pg2`:

mpt3sas_config_get_pcie_device_pg2
==================================

.. c:function:: int mpt3sas_config_get_pcie_device_pg2(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi26PCIeDevicePage2_t *config_page, u32 form, u32 handle)

    obtain pcie device page 2

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: Mpi26PCIeDevicePage2_t \*

    :param form:
        GET_NEXT_HANDLE or HANDLE
    :type form: u32

    :param handle:
        device handle
    :type handle: u32

.. _`mpt3sas_config_get_pcie_device_pg2.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_pcie_device_pg2.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_number_hba_phys`:

mpt3sas_config_get_number_hba_phys
==================================

.. c:function:: int mpt3sas_config_get_number_hba_phys(struct MPT3SAS_ADAPTER *ioc, u8 *num_phys)

    obtain number of phys on the host

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param num_phys:
        pointer returned with the number of phys
    :type num_phys: u8 \*

.. _`mpt3sas_config_get_number_hba_phys.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_number_hba_phys.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_sas_iounit_pg0`:

mpt3sas_config_get_sas_iounit_pg0
=================================

.. c:function:: int mpt3sas_config_get_sas_iounit_pg0(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2SasIOUnitPage0_t *config_page, u16 sz)

    obtain sas iounit page 0

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: Mpi2SasIOUnitPage0_t \*

    :param sz:
        size of buffer passed in config_page
    :type sz: u16

.. _`mpt3sas_config_get_sas_iounit_pg0.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_sas_iounit_pg0.description`:

Description
-----------

Calling function should call config_get_number_hba_phys prior to
this function, so enough memory is allocated for config_page.

.. _`mpt3sas_config_get_sas_iounit_pg0.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_sas_iounit_pg1`:

mpt3sas_config_get_sas_iounit_pg1
=================================

.. c:function:: int mpt3sas_config_get_sas_iounit_pg1(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2SasIOUnitPage1_t *config_page, u16 sz)

    obtain sas iounit page 1

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: Mpi2SasIOUnitPage1_t \*

    :param sz:
        size of buffer passed in config_page
    :type sz: u16

.. _`mpt3sas_config_get_sas_iounit_pg1.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_sas_iounit_pg1.description`:

Description
-----------

Calling function should call config_get_number_hba_phys prior to
this function, so enough memory is allocated for config_page.

.. _`mpt3sas_config_get_sas_iounit_pg1.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_set_sas_iounit_pg1`:

mpt3sas_config_set_sas_iounit_pg1
=================================

.. c:function:: int mpt3sas_config_set_sas_iounit_pg1(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2SasIOUnitPage1_t *config_page, u16 sz)

    send sas iounit page 1

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: Mpi2SasIOUnitPage1_t \*

    :param sz:
        size of buffer passed in config_page
    :type sz: u16

.. _`mpt3sas_config_set_sas_iounit_pg1.context`:

Context
-------

sleep.

.. _`mpt3sas_config_set_sas_iounit_pg1.description`:

Description
-----------

Calling function should call config_get_number_hba_phys prior to
this function, so enough memory is allocated for config_page.

.. _`mpt3sas_config_set_sas_iounit_pg1.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_expander_pg0`:

mpt3sas_config_get_expander_pg0
===============================

.. c:function:: int mpt3sas_config_get_expander_pg0(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2ExpanderPage0_t *config_page, u32 form, u32 handle)

    obtain expander page 0

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: Mpi2ExpanderPage0_t \*

    :param form:
        GET_NEXT_HANDLE or HANDLE
    :type form: u32

    :param handle:
        expander handle
    :type handle: u32

.. _`mpt3sas_config_get_expander_pg0.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_expander_pg0.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_expander_pg1`:

mpt3sas_config_get_expander_pg1
===============================

.. c:function:: int mpt3sas_config_get_expander_pg1(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2ExpanderPage1_t *config_page, u32 phy_number, u16 handle)

    obtain expander page 1

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: Mpi2ExpanderPage1_t \*

    :param phy_number:
        phy number
    :type phy_number: u32

    :param handle:
        expander handle
    :type handle: u16

.. _`mpt3sas_config_get_expander_pg1.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_expander_pg1.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_enclosure_pg0`:

mpt3sas_config_get_enclosure_pg0
================================

.. c:function:: int mpt3sas_config_get_enclosure_pg0(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2SasEnclosurePage0_t *config_page, u32 form, u32 handle)

    obtain enclosure page 0

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: Mpi2SasEnclosurePage0_t \*

    :param form:
        GET_NEXT_HANDLE or HANDLE
    :type form: u32

    :param handle:
        expander handle
    :type handle: u32

.. _`mpt3sas_config_get_enclosure_pg0.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_enclosure_pg0.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_phy_pg0`:

mpt3sas_config_get_phy_pg0
==========================

.. c:function:: int mpt3sas_config_get_phy_pg0(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2SasPhyPage0_t *config_page, u32 phy_number)

    obtain phy page 0

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: Mpi2SasPhyPage0_t \*

    :param phy_number:
        phy number
    :type phy_number: u32

.. _`mpt3sas_config_get_phy_pg0.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_phy_pg0.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_phy_pg1`:

mpt3sas_config_get_phy_pg1
==========================

.. c:function:: int mpt3sas_config_get_phy_pg1(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2SasPhyPage1_t *config_page, u32 phy_number)

    obtain phy page 1

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: Mpi2SasPhyPage1_t \*

    :param phy_number:
        phy number
    :type phy_number: u32

.. _`mpt3sas_config_get_phy_pg1.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_phy_pg1.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_raid_volume_pg1`:

mpt3sas_config_get_raid_volume_pg1
==================================

.. c:function:: int mpt3sas_config_get_raid_volume_pg1(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2RaidVolPage1_t *config_page, u32 form, u32 handle)

    obtain raid volume page 1

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: Mpi2RaidVolPage1_t \*

    :param form:
        GET_NEXT_HANDLE or HANDLE
    :type form: u32

    :param handle:
        volume handle
    :type handle: u32

.. _`mpt3sas_config_get_raid_volume_pg1.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_raid_volume_pg1.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_number_pds`:

mpt3sas_config_get_number_pds
=============================

.. c:function:: int mpt3sas_config_get_number_pds(struct MPT3SAS_ADAPTER *ioc, u16 handle, u8 *num_pds)

    obtain number of phys disk assigned to volume

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param handle:
        volume handle
    :type handle: u16

    :param num_pds:
        returns pds count
    :type num_pds: u8 \*

.. _`mpt3sas_config_get_number_pds.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_number_pds.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_raid_volume_pg0`:

mpt3sas_config_get_raid_volume_pg0
==================================

.. c:function:: int mpt3sas_config_get_raid_volume_pg0(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2RaidVolPage0_t *config_page, u32 form, u32 handle, u16 sz)

    obtain raid volume page 0

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: Mpi2RaidVolPage0_t \*

    :param form:
        GET_NEXT_HANDLE or HANDLE
    :type form: u32

    :param handle:
        volume handle
    :type handle: u32

    :param sz:
        size of buffer passed in config_page
    :type sz: u16

.. _`mpt3sas_config_get_raid_volume_pg0.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_raid_volume_pg0.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_phys_disk_pg0`:

mpt3sas_config_get_phys_disk_pg0
================================

.. c:function:: int mpt3sas_config_get_phys_disk_pg0(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2RaidPhysDiskPage0_t *config_page, u32 form, u32 form_specific)

    obtain phys disk page 0

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply mf payload returned from firmware
    :type mpi_reply: Mpi2ConfigReply_t \*

    :param config_page:
        contents of the config page
    :type config_page: Mpi2RaidPhysDiskPage0_t \*

    :param form:
        GET_NEXT_PHYSDISKNUM, PHYSDISKNUM, DEVHANDLE
    :type form: u32

    :param form_specific:
        specific to the form
    :type form_specific: u32

.. _`mpt3sas_config_get_phys_disk_pg0.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_phys_disk_pg0.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_volume_handle`:

mpt3sas_config_get_volume_handle
================================

.. c:function:: int mpt3sas_config_get_volume_handle(struct MPT3SAS_ADAPTER *ioc, u16 pd_handle, u16 *volume_handle)

    returns volume handle for give hidden raid components

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param pd_handle:
        phys disk handle
    :type pd_handle: u16

    :param volume_handle:
        volume handle
    :type volume_handle: u16 \*

.. _`mpt3sas_config_get_volume_handle.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_volume_handle.return`:

Return
------

0 for success, non-zero for failure.

.. _`mpt3sas_config_get_volume_wwid`:

mpt3sas_config_get_volume_wwid
==============================

.. c:function:: int mpt3sas_config_get_volume_wwid(struct MPT3SAS_ADAPTER *ioc, u16 volume_handle, u64 *wwid)

    returns wwid given the volume handle

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param volume_handle:
        volume handle
    :type volume_handle: u16

    :param wwid:
        volume wwid
    :type wwid: u64 \*

.. _`mpt3sas_config_get_volume_wwid.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_volume_wwid.return`:

Return
------

0 for success, non-zero for failure.

.. This file was automatic generated / don't edit.

