.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/ufs/ufshcd.c

.. _`ufshcd_get_intr_mask`:

ufshcd_get_intr_mask
====================

.. c:function:: u32 ufshcd_get_intr_mask(struct ufs_hba *hba)

    Get the interrupt bit mask \ ``hba``\  - Pointer to adapter instance

    :param struct ufs_hba \*hba:
        *undescribed*

.. _`ufshcd_get_intr_mask.description`:

Description
-----------

Returns interrupt bit mask per version

.. _`ufshcd_get_ufs_version`:

ufshcd_get_ufs_version
======================

.. c:function:: u32 ufshcd_get_ufs_version(struct ufs_hba *hba)

    Get the UFS version supported by the HBA \ ``hba``\  - Pointer to adapter instance

    :param struct ufs_hba \*hba:
        *undescribed*

.. _`ufshcd_get_ufs_version.description`:

Description
-----------

Returns UFSHCI version supported by the controller

.. _`ufshcd_is_device_present`:

ufshcd_is_device_present
========================

.. c:function:: int ufshcd_is_device_present(struct ufs_hba *hba)

    Check if any device connected to the host controller

    :param struct ufs_hba \*hba:
        pointer to adapter instance

.. _`ufshcd_is_device_present.description`:

Description
-----------

Returns 1 if device present, 0 if no device detected

.. _`ufshcd_get_tr_ocs`:

ufshcd_get_tr_ocs
=================

.. c:function:: int ufshcd_get_tr_ocs(struct ufshcd_lrb *lrbp)

    Get the UTRD Overall Command Status

    :param struct ufshcd_lrb \*lrbp:
        *undescribed*

.. _`ufshcd_get_tr_ocs.description`:

Description
-----------

This function is used to get the OCS field from UTRD
Returns the OCS field in the UTRD

.. _`ufshcd_get_tmr_ocs`:

ufshcd_get_tmr_ocs
==================

.. c:function:: int ufshcd_get_tmr_ocs(struct utp_task_req_desc *task_req_descp)

    Get the UTMRD Overall Command Status

    :param struct utp_task_req_desc \*task_req_descp:
        pointer to utp_task_req_desc structure

.. _`ufshcd_get_tmr_ocs.description`:

Description
-----------

This function is used to get the OCS field from UTMRD
Returns the OCS field in the UTMRD

.. _`ufshcd_get_tm_free_slot`:

ufshcd_get_tm_free_slot
=======================

.. c:function:: bool ufshcd_get_tm_free_slot(struct ufs_hba *hba, int *free_slot)

    get a free slot for task management request

    :param struct ufs_hba \*hba:
        per adapter instance

    :param int \*free_slot:
        pointer to variable with available slot value

.. _`ufshcd_get_tm_free_slot.description`:

Description
-----------

Get a free tag and lock it until \ :c:func:`ufshcd_put_tm_slot`\  is called.
Returns 0 if free slot is not available, else return 1 with tag value
in \ ``free_slot``\ .

.. _`ufshcd_utrl_clear`:

ufshcd_utrl_clear
=================

.. c:function:: void ufshcd_utrl_clear(struct ufs_hba *hba, u32 pos)

    Clear a bit in UTRLCLR register

    :param struct ufs_hba \*hba:
        per adapter instance

    :param u32 pos:
        position of the bit to be cleared

.. _`ufshcd_outstanding_req_clear`:

ufshcd_outstanding_req_clear
============================

.. c:function:: void ufshcd_outstanding_req_clear(struct ufs_hba *hba, int tag)

    Clear a bit in outstanding request field

    :param struct ufs_hba \*hba:
        per adapter instance

    :param int tag:
        position of the bit to be cleared

.. _`ufshcd_get_lists_status`:

ufshcd_get_lists_status
=======================

.. c:function:: int ufshcd_get_lists_status(u32 reg)

    Check UCRDY, UTRLRDY and UTMRLRDY

    :param u32 reg:
        Register value of host controller status

.. _`ufshcd_get_lists_status.description`:

Description
-----------

Returns integer, 0 on Success and positive value if failed

.. _`ufshcd_get_uic_cmd_result`:

ufshcd_get_uic_cmd_result
=========================

.. c:function:: int ufshcd_get_uic_cmd_result(struct ufs_hba *hba)

    Get the UIC command result

    :param struct ufs_hba \*hba:
        Pointer to adapter instance

.. _`ufshcd_get_uic_cmd_result.description`:

Description
-----------

This function gets the result of UIC command completion
Returns 0 on success, non zero value on error

.. _`ufshcd_get_dme_attr_val`:

ufshcd_get_dme_attr_val
=======================

.. c:function:: u32 ufshcd_get_dme_attr_val(struct ufs_hba *hba)

    Get the value of attribute returned by UIC command

    :param struct ufs_hba \*hba:
        Pointer to adapter instance

.. _`ufshcd_get_dme_attr_val.description`:

Description
-----------

This function gets UIC command argument3
Returns 0 on success, non zero value on error

.. _`ufshcd_get_req_rsp`:

ufshcd_get_req_rsp
==================

.. c:function:: int ufshcd_get_req_rsp(struct utp_upiu_rsp *ucd_rsp_ptr)

    returns the TR response transaction type

    :param struct utp_upiu_rsp \*ucd_rsp_ptr:
        pointer to response UPIU

.. _`ufshcd_get_rsp_upiu_result`:

ufshcd_get_rsp_upiu_result
==========================

.. c:function:: int ufshcd_get_rsp_upiu_result(struct utp_upiu_rsp *ucd_rsp_ptr)

    Get the result from response UPIU

    :param struct utp_upiu_rsp \*ucd_rsp_ptr:
        pointer to response UPIU

.. _`ufshcd_get_rsp_upiu_result.description`:

Description
-----------

This function gets the response status and scsi_status from response UPIU
Returns the response result code.

.. _`ufshcd_is_exception_event`:

ufshcd_is_exception_event
=========================

.. c:function:: bool ufshcd_is_exception_event(struct utp_upiu_rsp *ucd_rsp_ptr)

    Check if the device raised an exception event

    :param struct utp_upiu_rsp \*ucd_rsp_ptr:
        pointer to response UPIU

.. _`ufshcd_is_exception_event.description`:

Description
-----------

The function checks if the device raised an exception event indicated in
the Device Information field of response UPIU.

Returns true if exception is raised, false otherwise.

.. _`ufshcd_reset_intr_aggr`:

ufshcd_reset_intr_aggr
======================

.. c:function:: void ufshcd_reset_intr_aggr(struct ufs_hba *hba)

    Reset interrupt aggregation values.

    :param struct ufs_hba \*hba:
        per adapter instance

.. _`ufshcd_config_intr_aggr`:

ufshcd_config_intr_aggr
=======================

.. c:function:: void ufshcd_config_intr_aggr(struct ufs_hba *hba, u8 cnt, u8 tmout)

    Configure interrupt aggregation values.

    :param struct ufs_hba \*hba:
        per adapter instance

    :param u8 cnt:
        Interrupt aggregation counter threshold

    :param u8 tmout:
        Interrupt aggregation timeout value

.. _`ufshcd_disable_intr_aggr`:

ufshcd_disable_intr_aggr
========================

.. c:function:: void ufshcd_disable_intr_aggr(struct ufs_hba *hba)

    Disables interrupt aggregation.

    :param struct ufs_hba \*hba:
        per adapter instance

.. _`ufshcd_enable_run_stop_reg`:

ufshcd_enable_run_stop_reg
==========================

.. c:function:: void ufshcd_enable_run_stop_reg(struct ufs_hba *hba)

    Enable run-stop registers, When run-stop registers are set to 1, it indicates the host controller that it can process the requests

    :param struct ufs_hba \*hba:
        per adapter instance

.. _`ufshcd_hba_start`:

ufshcd_hba_start
================

.. c:function:: void ufshcd_hba_start(struct ufs_hba *hba)

    Start controller initialization sequence

    :param struct ufs_hba \*hba:
        per adapter instance

.. _`ufshcd_is_hba_active`:

ufshcd_is_hba_active
====================

.. c:function:: int ufshcd_is_hba_active(struct ufs_hba *hba)

    Get controller state

    :param struct ufs_hba \*hba:
        per adapter instance

.. _`ufshcd_is_hba_active.description`:

Description
-----------

Returns zero if controller is active, 1 otherwise

.. _`ufshcd_hold`:

ufshcd_hold
===========

.. c:function:: int ufshcd_hold(struct ufs_hba *hba, bool async)

    Enable clocks that were gated earlier due to ufshcd_release. Also, exit from hibern8 mode and set the link as active.

    :param struct ufs_hba \*hba:
        per adapter instance

    :param bool async:
        This indicates whether caller should ungate clocks asynchronously.

.. _`ufshcd_send_command`:

ufshcd_send_command
===================

.. c:function:: void ufshcd_send_command(struct ufs_hba *hba, unsigned int task_tag)

    Send SCSI or device management commands

    :param struct ufs_hba \*hba:
        per adapter instance

    :param unsigned int task_tag:
        Task tag of the command

.. _`ufshcd_copy_sense_data`:

ufshcd_copy_sense_data
======================

.. c:function:: void ufshcd_copy_sense_data(struct ufshcd_lrb *lrbp)

    Copy sense data in case of check condition \ ``lrb``\  - pointer to local reference block

    :param struct ufshcd_lrb \*lrbp:
        *undescribed*

.. _`ufshcd_copy_query_response`:

ufshcd_copy_query_response
==========================

.. c:function:: int ufshcd_copy_query_response(struct ufs_hba *hba, struct ufshcd_lrb *lrbp)

    Copy the Query Response and the data descriptor

    :param struct ufs_hba \*hba:
        per adapter instance
        \ ``lrb``\  - pointer to local reference block

    :param struct ufshcd_lrb \*lrbp:
        *undescribed*

.. _`ufshcd_hba_capabilities`:

ufshcd_hba_capabilities
=======================

.. c:function:: void ufshcd_hba_capabilities(struct ufs_hba *hba)

    Read controller capabilities

    :param struct ufs_hba \*hba:
        per adapter instance

.. _`ufshcd_ready_for_uic_cmd`:

ufshcd_ready_for_uic_cmd
========================

.. c:function:: bool ufshcd_ready_for_uic_cmd(struct ufs_hba *hba)

    Check if controller is ready to accept UIC commands

    :param struct ufs_hba \*hba:
        per adapter instance
        Return true on success, else false

.. _`ufshcd_get_upmcrs`:

ufshcd_get_upmcrs
=================

.. c:function:: u8 ufshcd_get_upmcrs(struct ufs_hba *hba)

    Get the power mode change request status

    :param struct ufs_hba \*hba:
        Pointer to adapter instance

.. _`ufshcd_get_upmcrs.description`:

Description
-----------

This function gets the UPMCRS field of HCS register
Returns value of UPMCRS field

.. _`ufshcd_dispatch_uic_cmd`:

ufshcd_dispatch_uic_cmd
=======================

.. c:function:: void ufshcd_dispatch_uic_cmd(struct ufs_hba *hba, struct uic_command *uic_cmd)

    Dispatch UIC commands to unipro layers

    :param struct ufs_hba \*hba:
        per adapter instance

    :param struct uic_command \*uic_cmd:
        UIC command

.. _`ufshcd_dispatch_uic_cmd.description`:

Description
-----------

Mutex must be held.

.. _`ufshcd_wait_for_uic_cmd`:

ufshcd_wait_for_uic_cmd
=======================

.. c:function:: int ufshcd_wait_for_uic_cmd(struct ufs_hba *hba, struct uic_command *uic_cmd)

    Wait complectioin of UIC command

    :param struct ufs_hba \*hba:
        per adapter instance

    :param struct uic_command \*uic_cmd:
        *undescribed*

.. _`ufshcd_wait_for_uic_cmd.description`:

Description
-----------

Must be called with mutex held.
Returns 0 only if success.

.. _`__ufshcd_send_uic_cmd`:

__ufshcd_send_uic_cmd
=====================

.. c:function:: int __ufshcd_send_uic_cmd(struct ufs_hba *hba, struct uic_command *uic_cmd, bool completion)

    Send UIC commands and retrieve the result

    :param struct ufs_hba \*hba:
        per adapter instance

    :param struct uic_command \*uic_cmd:
        UIC command

    :param bool completion:
        initialize the completion only if this is set to true

.. _`__ufshcd_send_uic_cmd.description`:

Description
-----------

Identical to \ :c:func:`ufshcd_send_uic_cmd`\  expect mutex. Must be called
with mutex held and host_lock locked.
Returns 0 only if success.

.. _`ufshcd_send_uic_cmd`:

ufshcd_send_uic_cmd
===================

.. c:function:: int ufshcd_send_uic_cmd(struct ufs_hba *hba, struct uic_command *uic_cmd)

    Send UIC commands and retrieve the result

    :param struct ufs_hba \*hba:
        per adapter instance

    :param struct uic_command \*uic_cmd:
        UIC command

.. _`ufshcd_send_uic_cmd.description`:

Description
-----------

Returns 0 only if success.

.. _`ufshcd_map_sg`:

ufshcd_map_sg
=============

.. c:function:: int ufshcd_map_sg(struct ufshcd_lrb *lrbp)

    Map scatter-gather list to prdt \ ``lrbp``\  - pointer to local reference block

    :param struct ufshcd_lrb \*lrbp:
        *undescribed*

.. _`ufshcd_map_sg.description`:

Description
-----------

Returns 0 in case of success, non-zero value in case of failure

.. _`ufshcd_enable_intr`:

ufshcd_enable_intr
==================

.. c:function:: void ufshcd_enable_intr(struct ufs_hba *hba, u32 intrs)

    enable interrupts

    :param struct ufs_hba \*hba:
        per adapter instance

    :param u32 intrs:
        interrupt bits

.. _`ufshcd_disable_intr`:

ufshcd_disable_intr
===================

.. c:function:: void ufshcd_disable_intr(struct ufs_hba *hba, u32 intrs)

    disable interrupts

    :param struct ufs_hba \*hba:
        per adapter instance

    :param u32 intrs:
        interrupt bits

.. _`ufshcd_prepare_req_desc_hdr`:

ufshcd_prepare_req_desc_hdr
===========================

.. c:function:: void ufshcd_prepare_req_desc_hdr(struct ufshcd_lrb *lrbp, u32 *upiu_flags, enum dma_data_direction cmd_dir)

    Fills the requests header descriptor according to request

    :param struct ufshcd_lrb \*lrbp:
        pointer to local reference block

    :param u32 \*upiu_flags:
        flags required in the header

    :param enum dma_data_direction cmd_dir:
        requests data direction

.. _`ufshcd_prepare_utp_scsi_cmd_upiu`:

ufshcd_prepare_utp_scsi_cmd_upiu
================================

.. c:function:: void ufshcd_prepare_utp_scsi_cmd_upiu(struct ufshcd_lrb *lrbp, u32 upiu_flags)

    fills the utp_transfer_req_desc, for scsi commands \ ``lrbp``\  - local reference block pointer \ ``upiu_flags``\  - flags

    :param struct ufshcd_lrb \*lrbp:
        *undescribed*

    :param u32 upiu_flags:
        *undescribed*

.. _`ufshcd_prepare_utp_query_req_upiu`:

ufshcd_prepare_utp_query_req_upiu
=================================

.. c:function:: void ufshcd_prepare_utp_query_req_upiu(struct ufs_hba *hba, struct ufshcd_lrb *lrbp, u32 upiu_flags)

    fills the utp_transfer_req_desc, for query requsts

    :param struct ufs_hba \*hba:
        UFS hba

    :param struct ufshcd_lrb \*lrbp:
        local reference block pointer

    :param u32 upiu_flags:
        flags

.. _`ufshcd_compose_upiu`:

ufshcd_compose_upiu
===================

.. c:function:: int ufshcd_compose_upiu(struct ufs_hba *hba, struct ufshcd_lrb *lrbp)

    form UFS Protocol Information Unit(UPIU) \ ``hba``\  - per adapter instance \ ``lrb``\  - pointer to local reference block

    :param struct ufs_hba \*hba:
        *undescribed*

    :param struct ufshcd_lrb \*lrbp:
        *undescribed*

.. _`ufshcd_upiu_wlun_to_scsi_wlun`:

ufshcd_upiu_wlun_to_scsi_wlun
=============================

.. c:function:: u16 ufshcd_upiu_wlun_to_scsi_wlun(u8 upiu_wlun_id)

    maps UPIU W-LUN id to SCSI W-LUN ID

    :param u8 upiu_wlun_id:
        *undescribed*

.. _`ufshcd_upiu_wlun_to_scsi_wlun.description`:

Description
-----------

Returns SCSI W-LUN id

.. _`ufshcd_queuecommand`:

ufshcd_queuecommand
===================

.. c:function:: int ufshcd_queuecommand(struct Scsi_Host *host, struct scsi_cmnd *cmd)

    main entry point for SCSI requests

    :param struct Scsi_Host \*host:
        *undescribed*

    :param struct scsi_cmnd \*cmd:
        command from SCSI Midlayer

.. _`ufshcd_queuecommand.description`:

Description
-----------

Returns 0 for success, non-zero in case of failure

.. _`ufshcd_dev_cmd_completion`:

ufshcd_dev_cmd_completion
=========================

.. c:function:: int ufshcd_dev_cmd_completion(struct ufs_hba *hba, struct ufshcd_lrb *lrbp)

    handles device management command responses

    :param struct ufs_hba \*hba:
        per adapter instance

    :param struct ufshcd_lrb \*lrbp:
        pointer to local reference block

.. _`ufshcd_get_dev_cmd_tag`:

ufshcd_get_dev_cmd_tag
======================

.. c:function:: bool ufshcd_get_dev_cmd_tag(struct ufs_hba *hba, int *tag_out)

    Get device management command tag

    :param struct ufs_hba \*hba:
        per-adapter instance

    :param int \*tag_out:
        *undescribed*

.. _`ufshcd_get_dev_cmd_tag.description`:

Description
-----------

Get a free slot and lock it until device management command
completes.

Returns false if free slot is unavailable for locking, else
return true with tag value in \ ``tag``\ .

.. _`ufshcd_exec_dev_cmd`:

ufshcd_exec_dev_cmd
===================

.. c:function:: int ufshcd_exec_dev_cmd(struct ufs_hba *hba, enum dev_cmd_type cmd_type, int timeout)

    API for sending device management requests \ ``hba``\  - UFS hba \ ``cmd_type``\  - specifies the type (NOP, Query...) \ ``timeout``\  - time in seconds

    :param struct ufs_hba \*hba:
        *undescribed*

    :param enum dev_cmd_type cmd_type:
        *undescribed*

    :param int timeout:
        *undescribed*

.. _`ufshcd_exec_dev_cmd.note`:

NOTE
----

Since there is only one available tag for device management commands,
it is expected you hold the hba->dev_cmd.lock mutex.

.. _`ufshcd_init_query`:

ufshcd_init_query
=================

.. c:function:: void ufshcd_init_query(struct ufs_hba *hba, struct ufs_query_req **request, struct ufs_query_res **response, enum query_opcode opcode, u8 idn, u8 index, u8 selector)

    init the query response and request parameters

    :param struct ufs_hba \*hba:
        per-adapter instance

    :param struct ufs_query_req \*\*request:
        address of the request pointer to be initialized

    :param struct ufs_query_res \*\*response:
        address of the response pointer to be initialized

    :param enum query_opcode opcode:
        operation to perform

    :param u8 idn:
        flag idn to access

    :param u8 index:
        LU number to access

    :param u8 selector:
        query/flag/descriptor further identification

.. _`ufshcd_query_flag`:

ufshcd_query_flag
=================

.. c:function:: int ufshcd_query_flag(struct ufs_hba *hba, enum query_opcode opcode, enum flag_idn idn, bool *flag_res)

    API function for sending flag query requests

    :param struct ufs_hba \*hba:
        *undescribed*

    :param enum query_opcode opcode:
        *undescribed*

    :param enum flag_idn idn:
        *undescribed*

    :param bool \*flag_res:
        *undescribed*

.. _`ufshcd_query_flag.hba`:

hba
---

per-adapter instance

.. _`ufshcd_query_flag.query_opcode`:

query_opcode
------------

flag query to perform

.. _`ufshcd_query_flag.idn`:

idn
---

flag idn to access

.. _`ufshcd_query_flag.flag_res`:

flag_res
--------

the flag value after the query request completes

Returns 0 for success, non-zero in case of failure

.. _`ufshcd_query_attr`:

ufshcd_query_attr
=================

.. c:function:: int ufshcd_query_attr(struct ufs_hba *hba, enum query_opcode opcode, enum attr_idn idn, u8 index, u8 selector, u32 *attr_val)

    API function for sending attribute requests

    :param struct ufs_hba \*hba:
        *undescribed*

    :param enum query_opcode opcode:
        *undescribed*

    :param enum attr_idn idn:
        *undescribed*

    :param u8 index:
        *undescribed*

    :param u8 selector:
        *undescribed*

    :param u32 \*attr_val:
        *undescribed*

.. _`ufshcd_query_attr.hba`:

hba
---

per-adapter instance

.. _`ufshcd_query_attr.opcode`:

opcode
------

attribute opcode

.. _`ufshcd_query_attr.idn`:

idn
---

attribute idn to access

.. _`ufshcd_query_attr.index`:

index
-----

index field

.. _`ufshcd_query_attr.selector`:

selector
--------

selector field

.. _`ufshcd_query_attr.attr_val`:

attr_val
--------

the attribute value after the query request completes

Returns 0 for success, non-zero in case of failure

.. _`ufshcd_query_attr_retry`:

ufshcd_query_attr_retry
=======================

.. c:function:: int ufshcd_query_attr_retry(struct ufs_hba *hba, enum query_opcode opcode, enum attr_idn idn, u8 index, u8 selector, u32 *attr_val)

    API function for sending query attribute with retries

    :param struct ufs_hba \*hba:
        per-adapter instance

    :param enum query_opcode opcode:
        attribute opcode

    :param enum attr_idn idn:
        attribute idn to access

    :param u8 index:
        index field

    :param u8 selector:
        selector field

    :param u32 \*attr_val:
        the attribute value after the query request
        completes

.. _`ufshcd_query_attr_retry.description`:

Description
-----------

Returns 0 for success, non-zero in case of failure

.. _`ufshcd_query_descriptor_retry`:

ufshcd_query_descriptor_retry
=============================

.. c:function:: int ufshcd_query_descriptor_retry(struct ufs_hba *hba, enum query_opcode opcode, enum desc_idn idn, u8 index, u8 selector, u8 *desc_buf, int *buf_len)

    API function for sending descriptor requests

    :param struct ufs_hba \*hba:
        *undescribed*

    :param enum query_opcode opcode:
        *undescribed*

    :param enum desc_idn idn:
        *undescribed*

    :param u8 index:
        *undescribed*

    :param u8 selector:
        *undescribed*

    :param u8 \*desc_buf:
        *undescribed*

    :param int \*buf_len:
        *undescribed*

.. _`ufshcd_query_descriptor_retry.hba`:

hba
---

per-adapter instance

.. _`ufshcd_query_descriptor_retry.opcode`:

opcode
------

attribute opcode

.. _`ufshcd_query_descriptor_retry.idn`:

idn
---

attribute idn to access

.. _`ufshcd_query_descriptor_retry.index`:

index
-----

index field

.. _`ufshcd_query_descriptor_retry.selector`:

selector
--------

selector field

.. _`ufshcd_query_descriptor_retry.desc_buf`:

desc_buf
--------

the buffer that contains the descriptor

.. _`ufshcd_query_descriptor_retry.buf_len`:

buf_len
-------

length parameter passed to the device

Returns 0 for success, non-zero in case of failure.
The buf_len parameter will contain, on return, the length parameter
received on the response.

.. _`ufshcd_read_desc_param`:

ufshcd_read_desc_param
======================

.. c:function:: int ufshcd_read_desc_param(struct ufs_hba *hba, enum desc_idn desc_id, int desc_index, u32 param_offset, u8 *param_read_buf, u32 param_size)

    read the specified descriptor parameter

    :param struct ufs_hba \*hba:
        Pointer to adapter instance

    :param enum desc_idn desc_id:
        descriptor idn value

    :param int desc_index:
        descriptor index

    :param u32 param_offset:
        offset of the parameter to read

    :param u8 \*param_read_buf:
        pointer to buffer where parameter would be read

    :param u32 param_size:
        sizeof(param_read_buf)

.. _`ufshcd_read_desc_param.description`:

Description
-----------

Return 0 in case of success, non-zero otherwise

.. _`ufshcd_read_string_desc`:

ufshcd_read_string_desc
=======================

.. c:function:: int ufshcd_read_string_desc(struct ufs_hba *hba, int desc_index, u8 *buf, u32 size, bool ascii)

    read string descriptor

    :param struct ufs_hba \*hba:
        pointer to adapter instance

    :param int desc_index:
        descriptor index

    :param u8 \*buf:
        pointer to buffer where descriptor would be read

    :param u32 size:
        size of buf

    :param bool ascii:
        if true convert from unicode to ascii characters

.. _`ufshcd_read_string_desc.description`:

Description
-----------

Return 0 in case of success, non-zero otherwise

.. _`ufshcd_read_unit_desc_param`:

ufshcd_read_unit_desc_param
===========================

.. c:function:: int ufshcd_read_unit_desc_param(struct ufs_hba *hba, int lun, enum unit_desc_param param_offset, u8 *param_read_buf, u32 param_size)

    read the specified unit descriptor parameter

    :param struct ufs_hba \*hba:
        Pointer to adapter instance

    :param int lun:
        lun id

    :param enum unit_desc_param param_offset:
        offset of the parameter to read

    :param u8 \*param_read_buf:
        pointer to buffer where parameter would be read

    :param u32 param_size:
        sizeof(param_read_buf)

.. _`ufshcd_read_unit_desc_param.description`:

Description
-----------

Return 0 in case of success, non-zero otherwise

.. _`ufshcd_memory_alloc`:

ufshcd_memory_alloc
===================

.. c:function:: int ufshcd_memory_alloc(struct ufs_hba *hba)

    allocate memory for host memory space data structures

    :param struct ufs_hba \*hba:
        per adapter instance

.. _`ufshcd_memory_alloc.description`:

Description
-----------

1. Allocate DMA memory for Command Descriptor array
Each command descriptor consist of Command UPIU, Response UPIU and PRDT
2. Allocate DMA memory for UTP Transfer Request Descriptor List (UTRDL).
3. Allocate DMA memory for UTP Task Management Request Descriptor List
(UTMRDL)
4. Allocate memory for local reference block(lrb).

Returns 0 for success, non-zero in case of failure

.. _`ufshcd_host_memory_configure`:

ufshcd_host_memory_configure
============================

.. c:function:: void ufshcd_host_memory_configure(struct ufs_hba *hba)

    configure local reference block with memory offsets

    :param struct ufs_hba \*hba:
        per adapter instance

.. _`ufshcd_host_memory_configure.description`:

Description
-----------

Configure Host memory space
1. Update Corresponding UTRD.UCDBA and UTRD.UCDBAU with UCD DMA
address.
2. Update each UTRD with Response UPIU offset, Response UPIU length
and PRDT offset.
3. Save the corresponding addresses of UTRD, UCD.CMD, UCD.RSP and UCD.PRDT
into local reference block.

.. _`ufshcd_dme_link_startup`:

ufshcd_dme_link_startup
=======================

.. c:function:: int ufshcd_dme_link_startup(struct ufs_hba *hba)

    Notify Unipro to perform link startup

    :param struct ufs_hba \*hba:
        per adapter instance

.. _`ufshcd_dme_link_startup.description`:

Description
-----------

UIC_CMD_DME_LINK_STARTUP command must be issued to Unipro layer,
in order to initialize the Unipro link startup procedure.
Once the Unipro links are up, the device connected to the controller
is detected.

Returns 0 on success, non-zero value on failure

.. _`ufshcd_dme_set_attr`:

ufshcd_dme_set_attr
===================

.. c:function:: int ufshcd_dme_set_attr(struct ufs_hba *hba, u32 attr_sel, u8 attr_set, u32 mib_val, u8 peer)

    UIC command for DME_SET, DME_PEER_SET

    :param struct ufs_hba \*hba:
        per adapter instance

    :param u32 attr_sel:
        uic command argument1

    :param u8 attr_set:
        attribute set type as uic command argument2

    :param u32 mib_val:
        setting value as uic command argument3

    :param u8 peer:
        indicate whether peer or local

.. _`ufshcd_dme_set_attr.description`:

Description
-----------

Returns 0 on success, non-zero value on failure

.. _`ufshcd_dme_get_attr`:

ufshcd_dme_get_attr
===================

.. c:function:: int ufshcd_dme_get_attr(struct ufs_hba *hba, u32 attr_sel, u32 *mib_val, u8 peer)

    UIC command for DME_GET, DME_PEER_GET

    :param struct ufs_hba \*hba:
        per adapter instance

    :param u32 attr_sel:
        uic command argument1

    :param u32 \*mib_val:
        the value of the attribute as returned by the UIC command

    :param u8 peer:
        indicate whether peer or local

.. _`ufshcd_dme_get_attr.description`:

Description
-----------

Returns 0 on success, non-zero value on failure

.. _`ufshcd_uic_pwr_ctrl`:

ufshcd_uic_pwr_ctrl
===================

.. c:function:: int ufshcd_uic_pwr_ctrl(struct ufs_hba *hba, struct uic_command *cmd)

    executes UIC commands (which affects the link power state) and waits for it to take effect.

    :param struct ufs_hba \*hba:
        per adapter instance

    :param struct uic_command \*cmd:
        UIC command to execute

.. _`ufshcd_uic_pwr_ctrl.description`:

Description
-----------

DME operations like DME_SET(PA_PWRMODE), DME_HIBERNATE_ENTER &
DME_HIBERNATE_EXIT commands take some time to take its effect on both host
and device UniPro link and hence it's final completion would be indicated by
dedicated status bits in Interrupt Status register (UPMS, UHES, UHXS) in
addition to normal UIC command completion Status (UCCS). This function only
returns after the relevant status bits indicate the completion.

Returns 0 on success, non-zero value on failure

.. _`ufshcd_uic_change_pwr_mode`:

ufshcd_uic_change_pwr_mode
==========================

.. c:function:: int ufshcd_uic_change_pwr_mode(struct ufs_hba *hba, u8 mode)

    Perform the UIC power mode chage using DME_SET primitives.

    :param struct ufs_hba \*hba:
        per adapter instance

    :param u8 mode:
        powr mode value

.. _`ufshcd_uic_change_pwr_mode.description`:

Description
-----------

Returns 0 on success, non-zero value on failure

.. _`ufshcd_get_max_pwr_mode`:

ufshcd_get_max_pwr_mode
=======================

.. c:function:: int ufshcd_get_max_pwr_mode(struct ufs_hba *hba)

    reads the max power mode negotiated with device

    :param struct ufs_hba \*hba:
        per-adapter instance

.. _`ufshcd_config_pwr_mode`:

ufshcd_config_pwr_mode
======================

.. c:function:: int ufshcd_config_pwr_mode(struct ufs_hba *hba, struct ufs_pa_layer_attr *desired_pwr_mode)

    configure a new power mode

    :param struct ufs_hba \*hba:
        per-adapter instance

    :param struct ufs_pa_layer_attr \*desired_pwr_mode:
        desired power configuration

.. _`ufshcd_complete_dev_init`:

ufshcd_complete_dev_init
========================

.. c:function:: int ufshcd_complete_dev_init(struct ufs_hba *hba)

    checks device readiness

    :param struct ufs_hba \*hba:
        *undescribed*

.. _`ufshcd_complete_dev_init.hba`:

hba
---

per-adapter instance

Set fDeviceInit flag and poll until device toggles it.

.. _`ufshcd_make_hba_operational`:

ufshcd_make_hba_operational
===========================

.. c:function:: int ufshcd_make_hba_operational(struct ufs_hba *hba)

    Make UFS controller operational

    :param struct ufs_hba \*hba:
        per adapter instance

.. _`ufshcd_make_hba_operational.description`:

Description
-----------

To bring UFS host controller to operational state,
1. Enable required interrupts
2. Configure interrupt aggregation
3. Program UTRL and UTMRL base address
4. Configure run-stop-registers

Returns 0 on success, non-zero value on failure

.. _`ufshcd_hba_stop`:

ufshcd_hba_stop
===============

.. c:function:: void ufshcd_hba_stop(struct ufs_hba *hba, bool can_sleep)

    Send controller to reset state

    :param struct ufs_hba \*hba:
        per adapter instance

    :param bool can_sleep:
        perform sleep or just spin

.. _`ufshcd_hba_enable`:

ufshcd_hba_enable
=================

.. c:function:: int ufshcd_hba_enable(struct ufs_hba *hba)

    initialize the controller

    :param struct ufs_hba \*hba:
        per adapter instance

.. _`ufshcd_hba_enable.description`:

Description
-----------

The controller resets itself and controller firmware initialization
sequence kicks off. When controller is ready it will set
the Host Controller Enable bit to 1.

Returns 0 on success, non-zero value on failure

.. _`ufshcd_link_startup`:

ufshcd_link_startup
===================

.. c:function:: int ufshcd_link_startup(struct ufs_hba *hba)

    Initialize unipro link startup

    :param struct ufs_hba \*hba:
        per adapter instance

.. _`ufshcd_link_startup.description`:

Description
-----------

Returns 0 for success, non-zero in case of failure

.. _`ufshcd_verify_dev_init`:

ufshcd_verify_dev_init
======================

.. c:function:: int ufshcd_verify_dev_init(struct ufs_hba *hba)

    Verify device initialization

    :param struct ufs_hba \*hba:
        per-adapter instance

.. _`ufshcd_verify_dev_init.description`:

Description
-----------

Send NOP OUT UPIU and wait for NOP IN response to check whether the
device Transport Protocol (UTP) layer is ready after a reset.
If the UTP layer at the device side is not initialized, it may
not respond with NOP IN UPIU within timeout of \ ``NOP_OUT_TIMEOUT``\ 
and we retry sending NOP OUT for \ ``NOP_OUT_RETRIES``\  iterations.

.. _`ufshcd_set_queue_depth`:

ufshcd_set_queue_depth
======================

.. c:function:: void ufshcd_set_queue_depth(struct scsi_device *sdev)

    set lun queue depth

    :param struct scsi_device \*sdev:
        pointer to SCSI device

.. _`ufshcd_set_queue_depth.description`:

Description
-----------

Read bLUQueueDepth value and activate scsi tagged command
queueing. For WLUN, queue depth is set to 1. For best-effort
cases (bLUQueueDepth = 0) the queue depth is set to a maximum
value that host can queue.

.. _`ufshcd_get_lu_power_on_wp_status`:

ufshcd_get_lu_power_on_wp_status
================================

.. c:function:: void ufshcd_get_lu_power_on_wp_status(struct ufs_hba *hba, struct scsi_device *sdev)

    get LU's power on write protect status

    :param struct ufs_hba \*hba:
        per-adapter instance

    :param struct scsi_device \*sdev:
        pointer to SCSI device

.. _`ufshcd_slave_alloc`:

ufshcd_slave_alloc
==================

.. c:function:: int ufshcd_slave_alloc(struct scsi_device *sdev)

    handle initial SCSI device configurations

    :param struct scsi_device \*sdev:
        pointer to SCSI device

.. _`ufshcd_slave_alloc.description`:

Description
-----------

Returns success

.. _`ufshcd_change_queue_depth`:

ufshcd_change_queue_depth
=========================

.. c:function:: int ufshcd_change_queue_depth(struct scsi_device *sdev, int depth)

    change queue depth

    :param struct scsi_device \*sdev:
        pointer to SCSI device

    :param int depth:
        required depth to set

.. _`ufshcd_change_queue_depth.description`:

Description
-----------

Change queue depth and make sure the max. limits are not crossed.

.. _`ufshcd_slave_configure`:

ufshcd_slave_configure
======================

.. c:function:: int ufshcd_slave_configure(struct scsi_device *sdev)

    adjust SCSI device configurations

    :param struct scsi_device \*sdev:
        pointer to SCSI device

.. _`ufshcd_slave_destroy`:

ufshcd_slave_destroy
====================

.. c:function:: void ufshcd_slave_destroy(struct scsi_device *sdev)

    remove SCSI device configurations

    :param struct scsi_device \*sdev:
        pointer to SCSI device

.. _`ufshcd_task_req_compl`:

ufshcd_task_req_compl
=====================

.. c:function:: int ufshcd_task_req_compl(struct ufs_hba *hba, u32 index, u8 *resp)

    handle task management request completion

    :param struct ufs_hba \*hba:
        per adapter instance

    :param u32 index:
        index of the completed request

    :param u8 \*resp:
        task management service response

.. _`ufshcd_task_req_compl.description`:

Description
-----------

Returns non-zero value on error, zero on success

.. _`ufshcd_scsi_cmd_status`:

ufshcd_scsi_cmd_status
======================

.. c:function:: int ufshcd_scsi_cmd_status(struct ufshcd_lrb *lrbp, int scsi_status)

    Update SCSI command result based on SCSI status

    :param struct ufshcd_lrb \*lrbp:
        *undescribed*

    :param int scsi_status:
        SCSI command status

.. _`ufshcd_scsi_cmd_status.description`:

Description
-----------

Returns value base on SCSI command status

.. _`ufshcd_transfer_rsp_status`:

ufshcd_transfer_rsp_status
==========================

.. c:function:: int ufshcd_transfer_rsp_status(struct ufs_hba *hba, struct ufshcd_lrb *lrbp)

    Get overall status of the response

    :param struct ufs_hba \*hba:
        per adapter instance

    :param struct ufshcd_lrb \*lrbp:
        *undescribed*

.. _`ufshcd_transfer_rsp_status.description`:

Description
-----------

Returns result of the command to notify SCSI midlayer

.. _`ufshcd_uic_cmd_compl`:

ufshcd_uic_cmd_compl
====================

.. c:function:: void ufshcd_uic_cmd_compl(struct ufs_hba *hba, u32 intr_status)

    handle completion of uic command

    :param struct ufs_hba \*hba:
        per adapter instance

    :param u32 intr_status:
        interrupt status generated by the controller

.. _`__ufshcd_transfer_req_compl`:

__ufshcd_transfer_req_compl
===========================

.. c:function:: void __ufshcd_transfer_req_compl(struct ufs_hba *hba, unsigned long completed_reqs)

    handle SCSI and query command completion

    :param struct ufs_hba \*hba:
        per adapter instance

    :param unsigned long completed_reqs:
        requests to complete

.. _`ufshcd_transfer_req_compl`:

ufshcd_transfer_req_compl
=========================

.. c:function:: void ufshcd_transfer_req_compl(struct ufs_hba *hba)

    handle SCSI and query command completion

    :param struct ufs_hba \*hba:
        per adapter instance

.. _`ufshcd_disable_ee`:

ufshcd_disable_ee
=================

.. c:function:: int ufshcd_disable_ee(struct ufs_hba *hba, u16 mask)

    disable exception event

    :param struct ufs_hba \*hba:
        per-adapter instance

    :param u16 mask:
        exception event to disable

.. _`ufshcd_disable_ee.description`:

Description
-----------

Disables exception event in the device so that the EVENT_ALERT
bit is not set.

Returns zero on success, non-zero error value on failure.

.. _`ufshcd_enable_ee`:

ufshcd_enable_ee
================

.. c:function:: int ufshcd_enable_ee(struct ufs_hba *hba, u16 mask)

    enable exception event

    :param struct ufs_hba \*hba:
        per-adapter instance

    :param u16 mask:
        exception event to enable

.. _`ufshcd_enable_ee.description`:

Description
-----------

Enable corresponding exception event in the device to allow
device to alert host in critical scenarios.

Returns zero on success, non-zero error value on failure.

.. _`ufshcd_enable_auto_bkops`:

ufshcd_enable_auto_bkops
========================

.. c:function:: int ufshcd_enable_auto_bkops(struct ufs_hba *hba)

    Allow device managed BKOPS

    :param struct ufs_hba \*hba:
        per-adapter instance

.. _`ufshcd_enable_auto_bkops.description`:

Description
-----------

Allow device to manage background operations on its own. Enabling
this might lead to inconsistent latencies during normal data transfers
as the device is allowed to manage its own way of handling background
operations.

Returns zero on success, non-zero on failure.

.. _`ufshcd_disable_auto_bkops`:

ufshcd_disable_auto_bkops
=========================

.. c:function:: int ufshcd_disable_auto_bkops(struct ufs_hba *hba)

    block device in doing background operations

    :param struct ufs_hba \*hba:
        per-adapter instance

.. _`ufshcd_disable_auto_bkops.description`:

Description
-----------

Disabling background operations improves command response latency but
has drawback of device moving into critical state where the device is
not-operable. Make sure to call \ :c:func:`ufshcd_enable_auto_bkops`\  whenever the
host is idle so that BKOPS are managed effectively without any negative
impacts.

Returns zero on success, non-zero on failure.

.. _`ufshcd_force_reset_auto_bkops`:

ufshcd_force_reset_auto_bkops
=============================

.. c:function:: void ufshcd_force_reset_auto_bkops(struct ufs_hba *hba)

    force enable of auto bkops

    :param struct ufs_hba \*hba:
        per adapter instance

.. _`ufshcd_force_reset_auto_bkops.description`:

Description
-----------

After a device reset the device may toggle the BKOPS_EN flag
to default value. The s/w tracking variables should be updated
as well. Do this by forcing enable of auto bkops.

.. _`ufshcd_bkops_ctrl`:

ufshcd_bkops_ctrl
=================

.. c:function:: int ufshcd_bkops_ctrl(struct ufs_hba *hba, enum bkops_status status)

    control the auto bkops based on current bkops status

    :param struct ufs_hba \*hba:
        per-adapter instance

    :param enum bkops_status status:
        bkops_status value

.. _`ufshcd_bkops_ctrl.description`:

Description
-----------

Read the bkops_status from the UFS device and Enable fBackgroundOpsEn
flag in the device to permit background operations if the device
bkops_status is greater than or equal to "status" argument passed to
this function, disable otherwise.

Returns 0 for success, non-zero in case of failure.

.. _`ufshcd_bkops_ctrl.note`:

NOTE
----

Caller of this function can check the "hba->auto_bkops_enabled" flag
to know whether auto bkops is enabled or disabled after this function
returns control to it.

.. _`ufshcd_urgent_bkops`:

ufshcd_urgent_bkops
===================

.. c:function:: int ufshcd_urgent_bkops(struct ufs_hba *hba)

    handle urgent bkops exception event

    :param struct ufs_hba \*hba:
        per-adapter instance

.. _`ufshcd_urgent_bkops.description`:

Description
-----------

Enable fBackgroundOpsEn flag in the device to permit background
operations.

If BKOPs is enabled, this function returns 0, 1 if the bkops in not enabled
and negative error value for any other failure.

.. _`ufshcd_exception_event_handler`:

ufshcd_exception_event_handler
==============================

.. c:function:: void ufshcd_exception_event_handler(struct work_struct *work)

    handle exceptions raised by device

    :param struct work_struct \*work:
        pointer to work data

.. _`ufshcd_exception_event_handler.description`:

Description
-----------

Read bExceptionEventStatus attribute from the device and handle the
exception event accordingly.

.. _`ufshcd_quirk_dl_nac_errors`:

ufshcd_quirk_dl_nac_errors
==========================

.. c:function:: bool ufshcd_quirk_dl_nac_errors(struct ufs_hba *hba)

    This function checks if error handling is to recover from the DL NAC errors or not.

    :param struct ufs_hba \*hba:
        per-adapter instance

.. _`ufshcd_quirk_dl_nac_errors.description`:

Description
-----------

Returns true if error handling is required, false otherwise

.. _`ufshcd_err_handler`:

ufshcd_err_handler
==================

.. c:function:: void ufshcd_err_handler(struct work_struct *work)

    handle UFS errors that require s/w attention

    :param struct work_struct \*work:
        pointer to work structure

.. _`ufshcd_update_uic_error`:

ufshcd_update_uic_error
=======================

.. c:function:: void ufshcd_update_uic_error(struct ufs_hba *hba)

    check and set fatal UIC error flags.

    :param struct ufs_hba \*hba:
        per-adapter instance

.. _`ufshcd_check_errors`:

ufshcd_check_errors
===================

.. c:function:: void ufshcd_check_errors(struct ufs_hba *hba)

    Check for errors that need s/w attention

    :param struct ufs_hba \*hba:
        per-adapter instance

.. _`ufshcd_tmc_handler`:

ufshcd_tmc_handler
==================

.. c:function:: void ufshcd_tmc_handler(struct ufs_hba *hba)

    handle task management function completion

    :param struct ufs_hba \*hba:
        per adapter instance

.. _`ufshcd_sl_intr`:

ufshcd_sl_intr
==============

.. c:function:: void ufshcd_sl_intr(struct ufs_hba *hba, u32 intr_status)

    Interrupt service routine

    :param struct ufs_hba \*hba:
        per adapter instance

    :param u32 intr_status:
        contains interrupts generated by the controller

.. _`ufshcd_intr`:

ufshcd_intr
===========

.. c:function:: irqreturn_t ufshcd_intr(int irq, void *__hba)

    Main interrupt service routine

    :param int irq:
        irq number

    :param void \*__hba:
        pointer to adapter instance

.. _`ufshcd_intr.description`:

Description
-----------

Returns IRQ_HANDLED - If interrupt is valid
IRQ_NONE - If invalid interrupt

.. _`ufshcd_issue_tm_cmd`:

ufshcd_issue_tm_cmd
===================

.. c:function:: int ufshcd_issue_tm_cmd(struct ufs_hba *hba, int lun_id, int task_id, u8 tm_function, u8 *tm_response)

    issues task management commands to controller

    :param struct ufs_hba \*hba:
        per adapter instance

    :param int lun_id:
        LUN ID to which TM command is sent

    :param int task_id:
        task ID to which the TM command is applicable

    :param u8 tm_function:
        task management function opcode

    :param u8 \*tm_response:
        task management service response return value

.. _`ufshcd_issue_tm_cmd.description`:

Description
-----------

Returns non-zero value on error, zero on success.

.. _`ufshcd_eh_device_reset_handler`:

ufshcd_eh_device_reset_handler
==============================

.. c:function:: int ufshcd_eh_device_reset_handler(struct scsi_cmnd *cmd)

    device reset handler registered to scsi layer.

    :param struct scsi_cmnd \*cmd:
        SCSI command pointer

.. _`ufshcd_eh_device_reset_handler.description`:

Description
-----------

Returns SUCCESS/FAILED

.. _`ufshcd_abort`:

ufshcd_abort
============

.. c:function:: int ufshcd_abort(struct scsi_cmnd *cmd)

    abort a specific command

    :param struct scsi_cmnd \*cmd:
        SCSI command pointer

.. _`ufshcd_abort.description`:

Description
-----------

Abort the pending command in device by sending UFS_ABORT_TASK task management
command, and in host controller by clearing the door-bell register. There can
be race between controller sending the command to the device while abort is
issued. To avoid that, first issue UFS_QUERY_TASK to check if the command is
really issued and then try to abort it.

Returns SUCCESS/FAILED

.. _`ufshcd_host_reset_and_restore`:

ufshcd_host_reset_and_restore
=============================

.. c:function:: int ufshcd_host_reset_and_restore(struct ufs_hba *hba)

    reset and restore host controller

    :param struct ufs_hba \*hba:
        per-adapter instance

.. _`ufshcd_host_reset_and_restore.description`:

Description
-----------

Note that host controller reset may issue DME_RESET to
local and remote (device) Uni-Pro stack and the attributes
are reset to default state.

Returns zero on success, non-zero on failure

.. _`ufshcd_reset_and_restore`:

ufshcd_reset_and_restore
========================

.. c:function:: int ufshcd_reset_and_restore(struct ufs_hba *hba)

    reset and re-initialize host/device

    :param struct ufs_hba \*hba:
        per-adapter instance

.. _`ufshcd_reset_and_restore.description`:

Description
-----------

Reset and recover device, host and re-establish link. This
is helpful to recover the communication in fatal error conditions.

Returns zero on success, non-zero on failure

.. _`ufshcd_eh_host_reset_handler`:

ufshcd_eh_host_reset_handler
============================

.. c:function:: int ufshcd_eh_host_reset_handler(struct scsi_cmnd *cmd)

    host reset handler registered to scsi layer \ ``cmd``\  - SCSI command pointer

    :param struct scsi_cmnd \*cmd:
        *undescribed*

.. _`ufshcd_eh_host_reset_handler.description`:

Description
-----------

Returns SUCCESS/FAILED

.. _`ufshcd_get_max_icc_level`:

ufshcd_get_max_icc_level
========================

.. c:function:: u32 ufshcd_get_max_icc_level(int sup_curr_uA, u32 start_scan, char *buff)

    calculate the ICC level

    :param int sup_curr_uA:
        max. current supported by the regulator

    :param u32 start_scan:
        row at the desc table to start scan from

    :param char \*buff:
        power descriptor buffer

.. _`ufshcd_get_max_icc_level.description`:

Description
-----------

Returns calculated max ICC level for specific regulator

.. _`ufshcd_find_max_sup_active_icc_level`:

ufshcd_find_max_sup_active_icc_level
====================================

.. c:function:: u32 ufshcd_find_max_sup_active_icc_level(struct ufs_hba *hba, u8 *desc_buf, int len)

    calculate the max ICC level In case regulators are not initialized we'll return 0

    :param struct ufs_hba \*hba:
        per-adapter instance

    :param u8 \*desc_buf:
        power descriptor buffer to extract ICC levels from.

    :param int len:
        length of desc_buff

.. _`ufshcd_find_max_sup_active_icc_level.description`:

Description
-----------

Returns calculated ICC level

.. _`ufshcd_scsi_add_wlus`:

ufshcd_scsi_add_wlus
====================

.. c:function:: int ufshcd_scsi_add_wlus(struct ufs_hba *hba)

    Adds required W-LUs

    :param struct ufs_hba \*hba:
        per-adapter instance

.. _`ufshcd_scsi_add_wlus.description`:

Description
-----------

UFS device specification requires the UFS devices to support 4 well known

.. _`ufshcd_scsi_add_wlus.logical-units`:

logical units
-------------

"REPORT_LUNS" (address: 01h)
"UFS Device" (address: 50h)
"RPMB" (address: 44h)
"BOOT" (address: 30h)
UFS device's power management needs to be controlled by "POWER CONDITION"
field of SSU (START STOP UNIT) command. But this "power condition" field
will take effect only when its sent to "UFS device" well known logical unit
hence we require the scsi_device instance to represent this logical unit in
order for the UFS host driver to send the SSU command for power management.
We also require the scsi_device instance for "RPMB" (Replay Protected Memory
Block) LU so user space process can control this LU. User space may also
want to have access to BOOT LU.
This function adds scsi device instances for each of all well known LUs
(except "REPORT LUNS" LU).

Returns zero on success (all required W-LUs are added successfully),
non-zero error value on failure (if failed to add any of the required W-LU).

.. _`ufshcd_tune_pa_tactivate`:

ufshcd_tune_pa_tactivate
========================

.. c:function:: int ufshcd_tune_pa_tactivate(struct ufs_hba *hba)

    Tunes PA_TActivate of local UniPro

    :param struct ufs_hba \*hba:
        per-adapter instance

.. _`ufshcd_tune_pa_tactivate.description`:

Description
-----------

PA_TActivate parameter can be tuned manually if UniPro version is less than
1.61. PA_TActivate needs to be greater than or equal to peerM-PHY's
RX_MIN_ACTIVATETIME_CAPABILITY attribute. This optimal value can help reduce
the hibern8 exit latency.

Returns zero on success, non-zero error value on failure.

.. _`ufshcd_tune_pa_hibern8time`:

ufshcd_tune_pa_hibern8time
==========================

.. c:function:: int ufshcd_tune_pa_hibern8time(struct ufs_hba *hba)

    Tunes PA_Hibern8Time of local UniPro

    :param struct ufs_hba \*hba:
        per-adapter instance

.. _`ufshcd_tune_pa_hibern8time.description`:

Description
-----------

PA_Hibern8Time parameter can be tuned manually if UniPro version is less than
1.61. PA_Hibern8Time needs to be maximum of local M-PHY's
TX_HIBERN8TIME_CAPABILITY & peer M-PHY's RX_HIBERN8TIME_CAPABILITY.
This optimal value can help reduce the hibern8 exit latency.

Returns zero on success, non-zero error value on failure.

.. _`ufshcd_probe_hba`:

ufshcd_probe_hba
================

.. c:function:: int ufshcd_probe_hba(struct ufs_hba *hba)

    probe hba to detect device and initialize

    :param struct ufs_hba \*hba:
        per-adapter instance

.. _`ufshcd_probe_hba.description`:

Description
-----------

Execute link-startup and verify device initialization

.. _`ufshcd_async_scan`:

ufshcd_async_scan
=================

.. c:function:: void ufshcd_async_scan(void *data, async_cookie_t cookie)

    asynchronous execution for probing hba

    :param void \*data:
        data pointer to pass to this function

    :param async_cookie_t cookie:
        cookie data

.. _`ufshcd_set_dev_pwr_mode`:

ufshcd_set_dev_pwr_mode
=======================

.. c:function:: int ufshcd_set_dev_pwr_mode(struct ufs_hba *hba, enum ufs_dev_pwr_mode pwr_mode)

    sends START STOP UNIT command to set device power mode

    :param struct ufs_hba \*hba:
        per adapter instance

    :param enum ufs_dev_pwr_mode pwr_mode:
        device power mode to set

.. _`ufshcd_set_dev_pwr_mode.description`:

Description
-----------

Returns 0 if requested power mode is set successfully
Returns non-zero if failed to set the requested power mode

.. _`ufshcd_suspend`:

ufshcd_suspend
==============

.. c:function:: int ufshcd_suspend(struct ufs_hba *hba, enum ufs_pm_op pm_op)

    helper function for suspend operations

    :param struct ufs_hba \*hba:
        per adapter instance

    :param enum ufs_pm_op pm_op:
        desired low power operation type

.. _`ufshcd_suspend.description`:

Description
-----------

This function will try to put the UFS device and link into low power
mode based on the "rpm_lvl" (Runtime PM level) or "spm_lvl"
(System PM level).

If this function is called during shutdown, it will make sure that
both UFS device and UFS link is powered off.

.. _`ufshcd_suspend.note`:

NOTE
----

UFS device & link must be active before we enter in this function.

Returns 0 for success and non-zero for failure

.. _`ufshcd_resume`:

ufshcd_resume
=============

.. c:function:: int ufshcd_resume(struct ufs_hba *hba, enum ufs_pm_op pm_op)

    helper function for resume operations

    :param struct ufs_hba \*hba:
        per adapter instance

    :param enum ufs_pm_op pm_op:
        runtime PM or system PM

.. _`ufshcd_resume.description`:

Description
-----------

This function basically brings the UFS device, UniPro link and controller
to active state.

Returns 0 for success and non-zero for failure

.. _`ufshcd_system_suspend`:

ufshcd_system_suspend
=====================

.. c:function:: int ufshcd_system_suspend(struct ufs_hba *hba)

    system suspend routine

    :param struct ufs_hba \*hba:
        per adapter instance

.. _`ufshcd_system_suspend.description`:

Description
-----------

Check the description of \ :c:func:`ufshcd_suspend`\  function for more details.

Returns 0 for success and non-zero for failure

.. _`ufshcd_system_resume`:

ufshcd_system_resume
====================

.. c:function:: int ufshcd_system_resume(struct ufs_hba *hba)

    system resume routine

    :param struct ufs_hba \*hba:
        per adapter instance

.. _`ufshcd_system_resume.description`:

Description
-----------

Returns 0 for success and non-zero for failure

.. _`ufshcd_runtime_suspend`:

ufshcd_runtime_suspend
======================

.. c:function:: int ufshcd_runtime_suspend(struct ufs_hba *hba)

    runtime suspend routine

    :param struct ufs_hba \*hba:
        per adapter instance

.. _`ufshcd_runtime_suspend.description`:

Description
-----------

Check the description of \ :c:func:`ufshcd_suspend`\  function for more details.

Returns 0 for success and non-zero for failure

.. _`ufshcd_runtime_resume`:

ufshcd_runtime_resume
=====================

.. c:function:: int ufshcd_runtime_resume(struct ufs_hba *hba)

    runtime resume routine

    :param struct ufs_hba \*hba:
        per adapter instance

.. _`ufshcd_runtime_resume.description`:

Description
-----------

This function basically brings the UFS device, UniPro link and controller
to active state. Following operations are done in this function:

1. Turn on all the controller related clocks
2. Bring the UniPro link out of Hibernate state
3. If UFS device is in sleep state, turn ON VCC rail and bring the UFS device
to active state.
4. If auto-bkops is enabled on the device, disable it.

So following would be the possible power state after this function return

.. _`ufshcd_runtime_resume.successfully`:

successfully
------------

S1: UFS device in Active state with VCC rail ON
UniPro link in Active state
All the UFS/UniPro controller clocks are ON

Returns 0 for success and non-zero for failure

.. _`ufshcd_shutdown`:

ufshcd_shutdown
===============

.. c:function:: int ufshcd_shutdown(struct ufs_hba *hba)

    shutdown routine

    :param struct ufs_hba \*hba:
        per adapter instance

.. _`ufshcd_shutdown.description`:

Description
-----------

This function would power off both UFS device and UFS link.

Returns 0 always to allow force shutdown even in case of errors.

.. _`ufshcd_remove`:

ufshcd_remove
=============

.. c:function:: void ufshcd_remove(struct ufs_hba *hba)

    de-allocate SCSI host and host memory space data structure memory \ ``hba``\  - per adapter instance

    :param struct ufs_hba \*hba:
        *undescribed*

.. _`ufshcd_dealloc_host`:

ufshcd_dealloc_host
===================

.. c:function:: void ufshcd_dealloc_host(struct ufs_hba *hba)

    deallocate Host Bus Adapter (HBA)

    :param struct ufs_hba \*hba:
        pointer to Host Bus Adapter (HBA)

.. _`ufshcd_set_dma_mask`:

ufshcd_set_dma_mask
===================

.. c:function:: int ufshcd_set_dma_mask(struct ufs_hba *hba)

    Set dma mask based on the controller addressing capability

    :param struct ufs_hba \*hba:
        per adapter instance

.. _`ufshcd_set_dma_mask.description`:

Description
-----------

Returns 0 for success, non-zero for failure

.. _`ufshcd_alloc_host`:

ufshcd_alloc_host
=================

.. c:function:: int ufshcd_alloc_host(struct device *dev, struct ufs_hba **hba_handle)

    allocate Host Bus Adapter (HBA)

    :param struct device \*dev:
        pointer to device handle

    :param struct ufs_hba \*\*hba_handle:
        driver private handle
        Returns 0 on success, non-zero value on failure

.. _`ufshcd_init`:

ufshcd_init
===========

.. c:function:: int ufshcd_init(struct ufs_hba *hba, void __iomem *mmio_base, unsigned int irq)

    Driver initialization routine

    :param struct ufs_hba \*hba:
        per-adapter instance

    :param void __iomem \*mmio_base:
        base register address

    :param unsigned int irq:
        Interrupt line of device
        Returns 0 on success, non-zero value on failure

.. This file was automatic generated / don't edit.

