.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/ia64/kernel/mca_drv.c

.. _`mca_page_isolate`:

mca_page_isolate
================

.. c:function:: isolate_status_t mca_page_isolate(unsigned long paddr)

    isolate a poisoned page in order not to use it later

    :param unsigned long paddr:
        poisoned memory location

.. _`mca_page_isolate.return-value`:

Return value
------------

one of isolate_status_t, ISOLATE_OK/NG/NONE.

.. _`mca_handler_bh`:

mca_handler_bh
==============

.. c:function:: void mca_handler_bh(unsigned long paddr, void *iip, unsigned long ipsr)

    Kill the process which occurred memory read error

    :param unsigned long paddr:
        poisoned address received from MCA Handler

    :param void \*iip:
        *undescribed*

    :param unsigned long ipsr:
        *undescribed*

.. _`mca_make_peidx`:

mca_make_peidx
==============

.. c:function:: void mca_make_peidx(sal_log_processor_info_t *slpi, peidx_table_t *peidx)

    Make index of processor error section

    :param sal_log_processor_info_t \*slpi:
        pointer to record of processor error section

    :param peidx_table_t \*peidx:
        pointer to index of processor error section

.. _`log_index_add_sect_ptr`:

LOG_INDEX_ADD_SECT_PTR
======================

.. c:function::  LOG_INDEX_ADD_SECT_PTR( sect,  ptr)

    Make index of SAL error record

    :param  sect:
        *undescribed*

    :param  ptr:
        *undescribed*

.. _`log_index_add_sect_ptr.return-value`:

Return value
------------

1 if record has platform error / 0 if not

.. _`init_record_index_pools`:

init_record_index_pools
=======================

.. c:function:: int init_record_index_pools( void)

    Initialize pool of lists for SAL record index

    :param  void:
        no arguments

.. _`init_record_index_pools.return-value`:

Return value
------------

0 on Success / -ENOMEM on Failure

.. _`is_mca_global`:

is_mca_global
=============

.. c:function:: mca_type_t is_mca_global(peidx_table_t *peidx, pal_bus_check_info_t *pbci, struct ia64_sal_os_state *sos)

    Check whether this MCA is global or not

    :param peidx_table_t \*peidx:
        pointer of index of processor error section

    :param pal_bus_check_info_t \*pbci:
        pointer to pal_bus_check_info_t

    :param struct ia64_sal_os_state \*sos:
        pointer to hand off struct between SAL and OS

.. _`is_mca_global.return-value`:

Return value
------------

MCA_IS_LOCAL / MCA_IS_GLOBAL

.. _`get_target_identifier`:

get_target_identifier
=====================

.. c:function:: u64 get_target_identifier(peidx_table_t *peidx)

    Get the valid Cache or Bus check target identifier.

    :param peidx_table_t \*peidx:
        pointer of index of processor error section

.. _`get_target_identifier.return-value`:

Return value
------------

target address on Success / 0 on Failure

.. _`recover_from_read_error`:

recover_from_read_error
=======================

.. c:function:: int recover_from_read_error(slidx_table_t *slidx, peidx_table_t *peidx, pal_bus_check_info_t *pbci, struct ia64_sal_os_state *sos)

    Try to recover the errors which type are "read"s.

    :param slidx_table_t \*slidx:
        pointer of index of SAL error record

    :param peidx_table_t \*peidx:
        pointer of index of processor error section

    :param pal_bus_check_info_t \*pbci:
        pointer of pal_bus_check_info

    :param struct ia64_sal_os_state \*sos:
        pointer to hand off struct between SAL and OS

.. _`recover_from_read_error.return-value`:

Return value
------------

1 on Success / 0 on Failure

.. _`recover_from_platform_error`:

recover_from_platform_error
===========================

.. c:function:: int recover_from_platform_error(slidx_table_t *slidx, peidx_table_t *peidx, pal_bus_check_info_t *pbci, struct ia64_sal_os_state *sos)

    Recover from platform error.

    :param slidx_table_t \*slidx:
        pointer of index of SAL error record

    :param peidx_table_t \*peidx:
        pointer of index of processor error section

    :param pal_bus_check_info_t \*pbci:
        pointer of pal_bus_check_info

    :param struct ia64_sal_os_state \*sos:
        pointer to hand off struct between SAL and OS

.. _`recover_from_platform_error.return-value`:

Return value
------------

1 on Success / 0 on Failure

.. _`recover_from_processor_error`:

recover_from_processor_error
============================

.. c:function:: int recover_from_processor_error(int platform, slidx_table_t *slidx, peidx_table_t *peidx, pal_bus_check_info_t *pbci, struct ia64_sal_os_state *sos)

    :param int platform:
        whether there are some platform error section or not

    :param slidx_table_t \*slidx:
        pointer of index of SAL error record

    :param peidx_table_t \*peidx:
        pointer of index of processor error section

    :param pal_bus_check_info_t \*pbci:
        pointer of pal_bus_check_info

    :param struct ia64_sal_os_state \*sos:
        pointer to hand off struct between SAL and OS

.. _`recover_from_processor_error.return-value`:

Return value
------------

1 on Success / 0 on Failure

.. _`mca_try_to_recover`:

mca_try_to_recover
==================

.. c:function:: int mca_try_to_recover(void *rec, struct ia64_sal_os_state *sos)

    Try to recover from MCA

    :param void \*rec:
        pointer to a SAL error record

    :param struct ia64_sal_os_state \*sos:
        pointer to hand off struct between SAL and OS

.. _`mca_try_to_recover.return-value`:

Return value
------------

1 on Success / 0 on Failure

.. This file was automatic generated / don't edit.

