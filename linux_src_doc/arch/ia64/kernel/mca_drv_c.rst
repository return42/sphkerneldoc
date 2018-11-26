.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/ia64/kernel/mca_drv.c

.. _`mca_page_isolate`:

mca_page_isolate
================

.. c:function:: isolate_status_t mca_page_isolate(unsigned long paddr)

    isolate a poisoned page in order not to use it later

    :param paddr:
        poisoned memory location
    :type paddr: unsigned long

.. _`mca_page_isolate.return-value`:

Return value
------------

one of isolate_status_t, ISOLATE_OK/NG/NONE.

.. _`mca_handler_bh`:

mca_handler_bh
==============

.. c:function:: void mca_handler_bh(unsigned long paddr, void *iip, unsigned long ipsr)

    Kill the process which occurred memory read error

    :param paddr:
        poisoned address received from MCA Handler
    :type paddr: unsigned long

    :param iip:
        *undescribed*
    :type iip: void \*

    :param ipsr:
        *undescribed*
    :type ipsr: unsigned long

.. _`mca_make_peidx`:

mca_make_peidx
==============

.. c:function:: void mca_make_peidx(sal_log_processor_info_t *slpi, peidx_table_t *peidx)

    Make index of processor error section

    :param slpi:
        pointer to record of processor error section
    :type slpi: sal_log_processor_info_t \*

    :param peidx:
        pointer to index of processor error section
    :type peidx: peidx_table_t \*

.. _`log_index_add_sect_ptr`:

LOG_INDEX_ADD_SECT_PTR
======================

.. c:function::  LOG_INDEX_ADD_SECT_PTR( sect,  ptr)

    Make index of SAL error record

    :param sect:
        *undescribed*
    :type sect: 

    :param ptr:
        *undescribed*
    :type ptr: 

.. _`log_index_add_sect_ptr.return-value`:

Return value
------------

1 if record has platform error / 0 if not

.. _`init_record_index_pools`:

init_record_index_pools
=======================

.. c:function:: int init_record_index_pools( void)

    Initialize pool of lists for SAL record index

    :param void:
        no arguments
    :type void: 

.. _`init_record_index_pools.return-value`:

Return value
------------

0 on Success / -ENOMEM on Failure

.. _`is_mca_global`:

is_mca_global
=============

.. c:function:: mca_type_t is_mca_global(peidx_table_t *peidx, pal_bus_check_info_t *pbci, struct ia64_sal_os_state *sos)

    Check whether this MCA is global or not

    :param peidx:
        pointer of index of processor error section
    :type peidx: peidx_table_t \*

    :param pbci:
        pointer to pal_bus_check_info_t
    :type pbci: pal_bus_check_info_t \*

    :param sos:
        pointer to hand off struct between SAL and OS
    :type sos: struct ia64_sal_os_state \*

.. _`is_mca_global.return-value`:

Return value
------------

MCA_IS_LOCAL / MCA_IS_GLOBAL

.. _`get_target_identifier`:

get_target_identifier
=====================

.. c:function:: u64 get_target_identifier(peidx_table_t *peidx)

    Get the valid Cache or Bus check target identifier.

    :param peidx:
        pointer of index of processor error section
    :type peidx: peidx_table_t \*

.. _`get_target_identifier.return-value`:

Return value
------------

target address on Success / 0 on Failure

.. _`recover_from_read_error`:

recover_from_read_error
=======================

.. c:function:: int recover_from_read_error(slidx_table_t *slidx, peidx_table_t *peidx, pal_bus_check_info_t *pbci, struct ia64_sal_os_state *sos)

    Try to recover the errors which type are "read"s.

    :param slidx:
        pointer of index of SAL error record
    :type slidx: slidx_table_t \*

    :param peidx:
        pointer of index of processor error section
    :type peidx: peidx_table_t \*

    :param pbci:
        pointer of pal_bus_check_info
    :type pbci: pal_bus_check_info_t \*

    :param sos:
        pointer to hand off struct between SAL and OS
    :type sos: struct ia64_sal_os_state \*

.. _`recover_from_read_error.return-value`:

Return value
------------

1 on Success / 0 on Failure

.. _`recover_from_platform_error`:

recover_from_platform_error
===========================

.. c:function:: int recover_from_platform_error(slidx_table_t *slidx, peidx_table_t *peidx, pal_bus_check_info_t *pbci, struct ia64_sal_os_state *sos)

    Recover from platform error.

    :param slidx:
        pointer of index of SAL error record
    :type slidx: slidx_table_t \*

    :param peidx:
        pointer of index of processor error section
    :type peidx: peidx_table_t \*

    :param pbci:
        pointer of pal_bus_check_info
    :type pbci: pal_bus_check_info_t \*

    :param sos:
        pointer to hand off struct between SAL and OS
    :type sos: struct ia64_sal_os_state \*

.. _`recover_from_platform_error.return-value`:

Return value
------------

1 on Success / 0 on Failure

.. _`recover_from_processor_error`:

recover_from_processor_error
============================

.. c:function:: int recover_from_processor_error(int platform, slidx_table_t *slidx, peidx_table_t *peidx, pal_bus_check_info_t *pbci, struct ia64_sal_os_state *sos)

    :param platform:
        whether there are some platform error section or not
    :type platform: int

    :param slidx:
        pointer of index of SAL error record
    :type slidx: slidx_table_t \*

    :param peidx:
        pointer of index of processor error section
    :type peidx: peidx_table_t \*

    :param pbci:
        pointer of pal_bus_check_info
    :type pbci: pal_bus_check_info_t \*

    :param sos:
        pointer to hand off struct between SAL and OS
    :type sos: struct ia64_sal_os_state \*

.. _`recover_from_processor_error.return-value`:

Return value
------------

1 on Success / 0 on Failure

.. _`mca_try_to_recover`:

mca_try_to_recover
==================

.. c:function:: int mca_try_to_recover(void *rec, struct ia64_sal_os_state *sos)

    Try to recover from MCA

    :param rec:
        pointer to a SAL error record
    :type rec: void \*

    :param sos:
        pointer to hand off struct between SAL and OS
    :type sos: struct ia64_sal_os_state \*

.. _`mca_try_to_recover.return-value`:

Return value
------------

1 on Success / 0 on Failure

.. This file was automatic generated / don't edit.

