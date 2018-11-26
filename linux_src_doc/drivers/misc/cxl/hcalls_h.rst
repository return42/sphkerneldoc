.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/cxl/hcalls.h

.. _`cxl_h_detach_process`:

cxl_h_detach_process
====================

.. c:function:: long cxl_h_detach_process(u64 unit_address, u64 process_token)

    Detach a process element from a coherent platform function.

    :param unit_address:
        *undescribed*
    :type unit_address: u64

    :param process_token:
        *undescribed*
    :type process_token: u64

.. _`cxl_h_reset_afu`:

cxl_h_reset_afu
===============

.. c:function:: long cxl_h_reset_afu(u64 unit_address)

    Perform a reset to the coherent platform function.

    :param unit_address:
        *undescribed*
    :type unit_address: u64

.. _`cxl_h_suspend_process`:

cxl_h_suspend_process
=====================

.. c:function:: long cxl_h_suspend_process(u64 unit_address, u64 process_token)

    Suspend a process from being executed Parameter1 = process-token as returned from H_ATTACH_CA_PROCESS when process was attached.

    :param unit_address:
        *undescribed*
    :type unit_address: u64

    :param process_token:
        *undescribed*
    :type process_token: u64

.. _`cxl_h_resume_process`:

cxl_h_resume_process
====================

.. c:function:: long cxl_h_resume_process(u64 unit_address, u64 process_token)

    Resume a process to be executed Parameter1 = process-token as returned from H_ATTACH_CA_PROCESS when process was attached.

    :param unit_address:
        *undescribed*
    :type unit_address: u64

    :param process_token:
        *undescribed*
    :type process_token: u64

.. _`cxl_h_read_error_state`:

cxl_h_read_error_state
======================

.. c:function:: long cxl_h_read_error_state(u64 unit_address, u64 *state)

    Reads the error state of the coherent platform function. R4 contains the error state

    :param unit_address:
        *undescribed*
    :type unit_address: u64

    :param state:
        *undescribed*
    :type state: u64 \*

.. _`cxl_h_get_afu_err`:

cxl_h_get_afu_err
=================

.. c:function:: long cxl_h_get_afu_err(u64 unit_address, u64 offset, u64 buf_address, u64 len)

    collect the AFU error buffer Parameter1 = byte offset into error buffer to retrieve, valid values are between 0 and (ibm,error-buffer-size - 1) Parameter2 = 4K aligned real address of error buffer, to be filled in Parameter3 = length of error buffer, valid values are 4K or less

    :param unit_address:
        *undescribed*
    :type unit_address: u64

    :param offset:
        *undescribed*
    :type offset: u64

    :param buf_address:
        *undescribed*
    :type buf_address: u64

    :param len:
        *undescribed*
    :type len: u64

.. _`cxl_h_get_config`:

cxl_h_get_config
================

.. c:function:: long cxl_h_get_config(u64 unit_address, u64 cr_num, u64 offset, u64 buf_address, u64 len)

    collect configuration record for the coherent platform function Parameter1 = # of configuration record to retrieve, valid values are between 0 and (ibm,#config-records - 1) Parameter2 = byte offset into configuration record to retrieve, valid values are between 0 and (ibm,config-record-size - 1) Parameter3 = 4K aligned real address of configuration record buffer, to be filled in Parameter4 = length of configuration buffer, valid values are 4K or less

    :param unit_address:
        *undescribed*
    :type unit_address: u64

    :param cr_num:
        *undescribed*
    :type cr_num: u64

    :param offset:
        *undescribed*
    :type offset: u64

    :param buf_address:
        *undescribed*
    :type buf_address: u64

    :param len:
        *undescribed*
    :type len: u64

.. _`cxl_h_terminate_process`:

cxl_h_terminate_process
=======================

.. c:function:: long cxl_h_terminate_process(u64 unit_address, u64 process_token)

    Terminate the process before completion Parameter1 = process-token as returned from H_ATTACH_CA_PROCESS when process was attached.

    :param unit_address:
        *undescribed*
    :type unit_address: u64

    :param process_token:
        *undescribed*
    :type process_token: u64

.. _`cxl_h_collect_vpd`:

cxl_h_collect_vpd
=================

.. c:function:: long cxl_h_collect_vpd(u64 unit_address, u64 record, u64 list_address, u64 num, u64 *out)

    Collect VPD for the coherent platform function. Parameter1 = # of VPD record to retrieve, valid values are between 0 and (ibm,#config-records - 1). Parameter2 = 4K naturally aligned real buffer containing block list entries Parameter3 = number of block list entries in the block list, valid values are between 0 and 256

    :param unit_address:
        *undescribed*
    :type unit_address: u64

    :param record:
        *undescribed*
    :type record: u64

    :param list_address:
        *undescribed*
    :type list_address: u64

    :param num:
        *undescribed*
    :type num: u64

    :param out:
        *undescribed*
    :type out: u64 \*

.. _`cxl_h_get_fn_error_interrupt`:

cxl_h_get_fn_error_interrupt
============================

.. c:function:: long cxl_h_get_fn_error_interrupt(u64 unit_address, u64 *reg)

    Read the function-wide error data based on an interrupt

    :param unit_address:
        *undescribed*
    :type unit_address: u64

    :param reg:
        *undescribed*
    :type reg: u64 \*

.. _`cxl_h_ack_fn_error_interrupt`:

cxl_h_ack_fn_error_interrupt
============================

.. c:function:: long cxl_h_ack_fn_error_interrupt(u64 unit_address, u64 value)

    Acknowledge function-wide error data based on an interrupt Parameter1 = value to write to the function-wide error interrupt register

    :param unit_address:
        *undescribed*
    :type unit_address: u64

    :param value:
        *undescribed*
    :type value: u64

.. _`cxl_h_get_error_log`:

cxl_h_get_error_log
===================

.. c:function:: long cxl_h_get_error_log(u64 unit_address, u64 value)

    Retrieve the Platform Log ID (PLID) of an error log

    :param unit_address:
        *undescribed*
    :type unit_address: u64

    :param value:
        *undescribed*
    :type value: u64

.. _`cxl_h_collect_int_info`:

cxl_h_collect_int_info
======================

.. c:function:: long cxl_h_collect_int_info(u64 unit_address, u64 process_token, struct cxl_irq_info *info)

    Collect interrupt info about a coherent platform function after an interrupt occurred.

    :param unit_address:
        *undescribed*
    :type unit_address: u64

    :param process_token:
        *undescribed*
    :type process_token: u64

    :param info:
        *undescribed*
    :type info: struct cxl_irq_info \*

.. _`cxl_h_control_faults`:

cxl_h_control_faults
====================

.. c:function:: long cxl_h_control_faults(u64 unit_address, u64 process_token, u64 control_mask, u64 reset_mask)

    Control the operation of a coherent platform function after a fault occurs.

    :param unit_address:
        *undescribed*
    :type unit_address: u64

    :param process_token:
        *undescribed*
    :type process_token: u64

    :param control_mask:
        *undescribed*
    :type control_mask: u64

    :param reset_mask:
        *undescribed*
    :type reset_mask: u64

.. _`cxl_h_control_faults.description`:

Description
-----------

Parameters
control-mask: value to control the faults
looks like PSL_TFC_An shifted >> 32
reset-mask: mask to control reset of function faults
Set reset_mask = 1 to reset PSL errors

.. _`cxl_h_reset_adapter`:

cxl_h_reset_adapter
===================

.. c:function:: long cxl_h_reset_adapter(u64 unit_address)

    Perform a reset to the coherent platform facility.

    :param unit_address:
        *undescribed*
    :type unit_address: u64

.. _`cxl_h_collect_vpd_adapter`:

cxl_h_collect_vpd_adapter
=========================

.. c:function:: long cxl_h_collect_vpd_adapter(u64 unit_address, u64 list_address, u64 num, u64 *out)

    Collect VPD for the coherent platform function. Parameter1 = 4K naturally aligned real buffer containing block list entries Parameter2 = number of block list entries in the block list, valid values are between 0 and 256

    :param unit_address:
        *undescribed*
    :type unit_address: u64

    :param list_address:
        *undescribed*
    :type list_address: u64

    :param num:
        *undescribed*
    :type num: u64

    :param out:
        *undescribed*
    :type out: u64 \*

.. _`cxl_h_download_adapter_image`:

cxl_h_download_adapter_image
============================

.. c:function:: long cxl_h_download_adapter_image(u64 unit_address, u64 list_address, u64 num, u64 *out)

    Download the base image to the coherent platform facility.

    :param unit_address:
        *undescribed*
    :type unit_address: u64

    :param list_address:
        *undescribed*
    :type list_address: u64

    :param num:
        *undescribed*
    :type num: u64

    :param out:
        *undescribed*
    :type out: u64 \*

.. _`cxl_h_validate_adapter_image`:

cxl_h_validate_adapter_image
============================

.. c:function:: long cxl_h_validate_adapter_image(u64 unit_address, u64 list_address, u64 num, u64 *out)

    Validate the base image in the coherent platform facility.

    :param unit_address:
        *undescribed*
    :type unit_address: u64

    :param list_address:
        *undescribed*
    :type list_address: u64

    :param num:
        *undescribed*
    :type num: u64

    :param out:
        *undescribed*
    :type out: u64 \*

.. This file was automatic generated / don't edit.

