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

_config_display_some_debug
==========================

.. c:function:: void _config_display_some_debug(struct MPT3SAS_ADAPTER *ioc, u16 smid, char *calling_function_name, MPI2DefaultReply_t *mpi_reply)

    debug routine

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

    :param char \*calling_function_name:
        string pass from calling function

    :param MPI2DefaultReply_t \*mpi_reply:
        reply message frame

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

_config_alloc_config_dma_memory
===============================

.. c:function:: int _config_alloc_config_dma_memory(struct MPT3SAS_ADAPTER *ioc, struct config_request *mem)

    obtain physical memory

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct config_request \*mem:
        struct config_request

.. _`_config_alloc_config_dma_memory.description`:

Description
-----------

A wrapper for obtaining dma-able memory for config page request.

Returns 0 for success, non-zero for failure.

.. _`_config_free_config_dma_memory`:

_config_free_config_dma_memory
==============================

.. c:function:: void _config_free_config_dma_memory(struct MPT3SAS_ADAPTER *ioc, struct config_request *mem)

    wrapper to free the memory

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param struct config_request \*mem:
        struct config_request

.. _`_config_free_config_dma_memory.description`:

Description
-----------

A wrapper to free dma-able memory when using \_config_alloc_config_dma_memory.

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_done`:

mpt3sas_config_done
===================

.. c:function:: u8 mpt3sas_config_done(struct MPT3SAS_ADAPTER *ioc, u16 smid, u8 msix_index, u32 reply)

    config page completion routine

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 smid:
        system request message index

    :param u8 msix_index:
        MSIX table index supplied by the OS

    :param u32 reply:
        reply message frame(lower 32bit addr)

.. _`mpt3sas_config_done.context`:

Context
-------

none.

.. _`mpt3sas_config_done.description`:

Description
-----------

The callback handler when using \_config_request.

Return 1 meaning mf should be freed from \_base_interrupt
0 means the mf is freed from this function.

.. _`_config_request`:

_config_request
===============

.. c:function:: int _config_request(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigRequest_t *mpi_request, Mpi2ConfigReply_t *mpi_reply, int timeout, void *config_page, u16 config_page_sz)

    main routine for sending config page requests

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigRequest_t \*mpi_request:
        request message frame

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param int timeout:
        timeout in seconds

    :param void \*config_page:
        contents of the config page

    :param u16 config_page_sz:
        size of config page

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

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_manufacturing_pg0`:

mpt3sas_config_get_manufacturing_pg0
====================================

.. c:function:: int mpt3sas_config_get_manufacturing_pg0(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2ManufacturingPage0_t *config_page)

    obtain manufacturing page 0

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param Mpi2ManufacturingPage0_t \*config_page:
        contents of the config page

.. _`mpt3sas_config_get_manufacturing_pg0.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_manufacturing_pg0.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_manufacturing_pg7`:

mpt3sas_config_get_manufacturing_pg7
====================================

.. c:function:: int mpt3sas_config_get_manufacturing_pg7(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2ManufacturingPage7_t *config_page, u16 sz)

    obtain manufacturing page 7

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param Mpi2ManufacturingPage7_t \*config_page:
        contents of the config page

    :param u16 sz:
        size of buffer passed in config_page

.. _`mpt3sas_config_get_manufacturing_pg7.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_manufacturing_pg7.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_manufacturing_pg10`:

mpt3sas_config_get_manufacturing_pg10
=====================================

.. c:function:: int mpt3sas_config_get_manufacturing_pg10(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, struct Mpi2ManufacturingPage10_t *config_page)

    obtain manufacturing page 10

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param struct Mpi2ManufacturingPage10_t \*config_page:
        contents of the config page

.. _`mpt3sas_config_get_manufacturing_pg10.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_manufacturing_pg10.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_manufacturing_pg11`:

mpt3sas_config_get_manufacturing_pg11
=====================================

.. c:function:: int mpt3sas_config_get_manufacturing_pg11(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, struct Mpi2ManufacturingPage11_t *config_page)

    obtain manufacturing page 11

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param struct Mpi2ManufacturingPage11_t \*config_page:
        contents of the config page

.. _`mpt3sas_config_get_manufacturing_pg11.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_manufacturing_pg11.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_set_manufacturing_pg11`:

mpt3sas_config_set_manufacturing_pg11
=====================================

.. c:function:: int mpt3sas_config_set_manufacturing_pg11(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, struct Mpi2ManufacturingPage11_t *config_page)

    set manufacturing page 11

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param struct Mpi2ManufacturingPage11_t \*config_page:
        contents of the config page

.. _`mpt3sas_config_set_manufacturing_pg11.context`:

Context
-------

sleep.

.. _`mpt3sas_config_set_manufacturing_pg11.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_bios_pg2`:

mpt3sas_config_get_bios_pg2
===========================

.. c:function:: int mpt3sas_config_get_bios_pg2(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2BiosPage2_t *config_page)

    obtain bios page 2

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param Mpi2BiosPage2_t \*config_page:
        contents of the config page

.. _`mpt3sas_config_get_bios_pg2.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_bios_pg2.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_bios_pg3`:

mpt3sas_config_get_bios_pg3
===========================

.. c:function:: int mpt3sas_config_get_bios_pg3(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2BiosPage3_t *config_page)

    obtain bios page 3

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param Mpi2BiosPage3_t \*config_page:
        contents of the config page

.. _`mpt3sas_config_get_bios_pg3.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_bios_pg3.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_iounit_pg0`:

mpt3sas_config_get_iounit_pg0
=============================

.. c:function:: int mpt3sas_config_get_iounit_pg0(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2IOUnitPage0_t *config_page)

    obtain iounit page 0

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param Mpi2IOUnitPage0_t \*config_page:
        contents of the config page

.. _`mpt3sas_config_get_iounit_pg0.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_iounit_pg0.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_iounit_pg1`:

mpt3sas_config_get_iounit_pg1
=============================

.. c:function:: int mpt3sas_config_get_iounit_pg1(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2IOUnitPage1_t *config_page)

    obtain iounit page 1

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param Mpi2IOUnitPage1_t \*config_page:
        contents of the config page

.. _`mpt3sas_config_get_iounit_pg1.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_iounit_pg1.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_set_iounit_pg1`:

mpt3sas_config_set_iounit_pg1
=============================

.. c:function:: int mpt3sas_config_set_iounit_pg1(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2IOUnitPage1_t *config_page)

    set iounit page 1

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param Mpi2IOUnitPage1_t \*config_page:
        contents of the config page

.. _`mpt3sas_config_set_iounit_pg1.context`:

Context
-------

sleep.

.. _`mpt3sas_config_set_iounit_pg1.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_iounit_pg3`:

mpt3sas_config_get_iounit_pg3
=============================

.. c:function:: int mpt3sas_config_get_iounit_pg3(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2IOUnitPage3_t *config_page, u16 sz)

    obtain iounit page 3

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param Mpi2IOUnitPage3_t \*config_page:
        contents of the config page

    :param u16 sz:
        size of buffer passed in config_page

.. _`mpt3sas_config_get_iounit_pg3.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_iounit_pg3.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_iounit_pg8`:

mpt3sas_config_get_iounit_pg8
=============================

.. c:function:: int mpt3sas_config_get_iounit_pg8(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2IOUnitPage8_t *config_page)

    obtain iounit page 8

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param Mpi2IOUnitPage8_t \*config_page:
        contents of the config page

.. _`mpt3sas_config_get_iounit_pg8.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_iounit_pg8.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_ioc_pg8`:

mpt3sas_config_get_ioc_pg8
==========================

.. c:function:: int mpt3sas_config_get_ioc_pg8(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2IOCPage8_t *config_page)

    obtain ioc page 8

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param Mpi2IOCPage8_t \*config_page:
        contents of the config page

.. _`mpt3sas_config_get_ioc_pg8.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_ioc_pg8.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_sas_device_pg0`:

mpt3sas_config_get_sas_device_pg0
=================================

.. c:function:: int mpt3sas_config_get_sas_device_pg0(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2SasDevicePage0_t *config_page, u32 form, u32 handle)

    obtain sas device page 0

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param Mpi2SasDevicePage0_t \*config_page:
        contents of the config page

    :param u32 form:
        GET_NEXT_HANDLE or HANDLE

    :param u32 handle:
        device handle

.. _`mpt3sas_config_get_sas_device_pg0.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_sas_device_pg0.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_sas_device_pg1`:

mpt3sas_config_get_sas_device_pg1
=================================

.. c:function:: int mpt3sas_config_get_sas_device_pg1(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2SasDevicePage1_t *config_page, u32 form, u32 handle)

    obtain sas device page 1

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param Mpi2SasDevicePage1_t \*config_page:
        contents of the config page

    :param u32 form:
        GET_NEXT_HANDLE or HANDLE

    :param u32 handle:
        device handle

.. _`mpt3sas_config_get_sas_device_pg1.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_sas_device_pg1.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_number_hba_phys`:

mpt3sas_config_get_number_hba_phys
==================================

.. c:function:: int mpt3sas_config_get_number_hba_phys(struct MPT3SAS_ADAPTER *ioc, u8 *num_phys)

    obtain number of phys on the host

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u8 \*num_phys:
        pointer returned with the number of phys

.. _`mpt3sas_config_get_number_hba_phys.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_number_hba_phys.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_sas_iounit_pg0`:

mpt3sas_config_get_sas_iounit_pg0
=================================

.. c:function:: int mpt3sas_config_get_sas_iounit_pg0(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2SasIOUnitPage0_t *config_page, u16 sz)

    obtain sas iounit page 0

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param Mpi2SasIOUnitPage0_t \*config_page:
        contents of the config page

    :param u16 sz:
        size of buffer passed in config_page

.. _`mpt3sas_config_get_sas_iounit_pg0.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_sas_iounit_pg0.description`:

Description
-----------

Calling function should call config_get_number_hba_phys prior to
this function, so enough memory is allocated for config_page.

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_sas_iounit_pg1`:

mpt3sas_config_get_sas_iounit_pg1
=================================

.. c:function:: int mpt3sas_config_get_sas_iounit_pg1(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2SasIOUnitPage1_t *config_page, u16 sz)

    obtain sas iounit page 1

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param Mpi2SasIOUnitPage1_t \*config_page:
        contents of the config page

    :param u16 sz:
        size of buffer passed in config_page

.. _`mpt3sas_config_get_sas_iounit_pg1.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_sas_iounit_pg1.description`:

Description
-----------

Calling function should call config_get_number_hba_phys prior to
this function, so enough memory is allocated for config_page.

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_set_sas_iounit_pg1`:

mpt3sas_config_set_sas_iounit_pg1
=================================

.. c:function:: int mpt3sas_config_set_sas_iounit_pg1(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2SasIOUnitPage1_t *config_page, u16 sz)

    send sas iounit page 1

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param Mpi2SasIOUnitPage1_t \*config_page:
        contents of the config page

    :param u16 sz:
        size of buffer passed in config_page

.. _`mpt3sas_config_set_sas_iounit_pg1.context`:

Context
-------

sleep.

.. _`mpt3sas_config_set_sas_iounit_pg1.description`:

Description
-----------

Calling function should call config_get_number_hba_phys prior to
this function, so enough memory is allocated for config_page.

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_expander_pg0`:

mpt3sas_config_get_expander_pg0
===============================

.. c:function:: int mpt3sas_config_get_expander_pg0(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2ExpanderPage0_t *config_page, u32 form, u32 handle)

    obtain expander page 0

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param Mpi2ExpanderPage0_t \*config_page:
        contents of the config page

    :param u32 form:
        GET_NEXT_HANDLE or HANDLE

    :param u32 handle:
        expander handle

.. _`mpt3sas_config_get_expander_pg0.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_expander_pg0.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_expander_pg1`:

mpt3sas_config_get_expander_pg1
===============================

.. c:function:: int mpt3sas_config_get_expander_pg1(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2ExpanderPage1_t *config_page, u32 phy_number, u16 handle)

    obtain expander page 1

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param Mpi2ExpanderPage1_t \*config_page:
        contents of the config page

    :param u32 phy_number:
        phy number

    :param u16 handle:
        expander handle

.. _`mpt3sas_config_get_expander_pg1.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_expander_pg1.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_enclosure_pg0`:

mpt3sas_config_get_enclosure_pg0
================================

.. c:function:: int mpt3sas_config_get_enclosure_pg0(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2SasEnclosurePage0_t *config_page, u32 form, u32 handle)

    obtain enclosure page 0

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param Mpi2SasEnclosurePage0_t \*config_page:
        contents of the config page

    :param u32 form:
        GET_NEXT_HANDLE or HANDLE

    :param u32 handle:
        expander handle

.. _`mpt3sas_config_get_enclosure_pg0.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_enclosure_pg0.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_phy_pg0`:

mpt3sas_config_get_phy_pg0
==========================

.. c:function:: int mpt3sas_config_get_phy_pg0(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2SasPhyPage0_t *config_page, u32 phy_number)

    obtain phy page 0

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param Mpi2SasPhyPage0_t \*config_page:
        contents of the config page

    :param u32 phy_number:
        phy number

.. _`mpt3sas_config_get_phy_pg0.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_phy_pg0.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_phy_pg1`:

mpt3sas_config_get_phy_pg1
==========================

.. c:function:: int mpt3sas_config_get_phy_pg1(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2SasPhyPage1_t *config_page, u32 phy_number)

    obtain phy page 1

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param Mpi2SasPhyPage1_t \*config_page:
        contents of the config page

    :param u32 phy_number:
        phy number

.. _`mpt3sas_config_get_phy_pg1.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_phy_pg1.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_raid_volume_pg1`:

mpt3sas_config_get_raid_volume_pg1
==================================

.. c:function:: int mpt3sas_config_get_raid_volume_pg1(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2RaidVolPage1_t *config_page, u32 form, u32 handle)

    obtain raid volume page 1

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param Mpi2RaidVolPage1_t \*config_page:
        contents of the config page

    :param u32 form:
        GET_NEXT_HANDLE or HANDLE

    :param u32 handle:
        volume handle

.. _`mpt3sas_config_get_raid_volume_pg1.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_raid_volume_pg1.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_number_pds`:

mpt3sas_config_get_number_pds
=============================

.. c:function:: int mpt3sas_config_get_number_pds(struct MPT3SAS_ADAPTER *ioc, u16 handle, u8 *num_pds)

    obtain number of phys disk assigned to volume

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 handle:
        volume handle

    :param u8 \*num_pds:
        returns pds count

.. _`mpt3sas_config_get_number_pds.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_number_pds.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_raid_volume_pg0`:

mpt3sas_config_get_raid_volume_pg0
==================================

.. c:function:: int mpt3sas_config_get_raid_volume_pg0(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2RaidVolPage0_t *config_page, u32 form, u32 handle, u16 sz)

    obtain raid volume page 0

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param Mpi2RaidVolPage0_t \*config_page:
        contents of the config page

    :param u32 form:
        GET_NEXT_HANDLE or HANDLE

    :param u32 handle:
        volume handle

    :param u16 sz:
        size of buffer passed in config_page

.. _`mpt3sas_config_get_raid_volume_pg0.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_raid_volume_pg0.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_phys_disk_pg0`:

mpt3sas_config_get_phys_disk_pg0
================================

.. c:function:: int mpt3sas_config_get_phys_disk_pg0(struct MPT3SAS_ADAPTER *ioc, Mpi2ConfigReply_t *mpi_reply, Mpi2RaidPhysDiskPage0_t *config_page, u32 form, u32 form_specific)

    obtain phys disk page 0

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param Mpi2ConfigReply_t \*mpi_reply:
        reply mf payload returned from firmware

    :param Mpi2RaidPhysDiskPage0_t \*config_page:
        contents of the config page

    :param u32 form:
        GET_NEXT_PHYSDISKNUM, PHYSDISKNUM, DEVHANDLE

    :param u32 form_specific:
        specific to the form

.. _`mpt3sas_config_get_phys_disk_pg0.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_phys_disk_pg0.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_volume_handle`:

mpt3sas_config_get_volume_handle
================================

.. c:function:: int mpt3sas_config_get_volume_handle(struct MPT3SAS_ADAPTER *ioc, u16 pd_handle, u16 *volume_handle)

    returns volume handle for give hidden raid components

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 pd_handle:
        phys disk handle

    :param u16 \*volume_handle:
        volume handle

.. _`mpt3sas_config_get_volume_handle.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_volume_handle.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. _`mpt3sas_config_get_volume_wwid`:

mpt3sas_config_get_volume_wwid
==============================

.. c:function:: int mpt3sas_config_get_volume_wwid(struct MPT3SAS_ADAPTER *ioc, u16 volume_handle, u64 *wwid)

    returns wwid given the volume handle

    :param struct MPT3SAS_ADAPTER \*ioc:
        per adapter object

    :param u16 volume_handle:
        volume handle

    :param u64 \*wwid:
        volume wwid

.. _`mpt3sas_config_get_volume_wwid.context`:

Context
-------

sleep.

.. _`mpt3sas_config_get_volume_wwid.description`:

Description
-----------

Returns 0 for success, non-zero for failure.

.. This file was automatic generated / don't edit.

