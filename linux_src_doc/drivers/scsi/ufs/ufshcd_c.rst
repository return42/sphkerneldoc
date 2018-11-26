.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/ufs/ufshcd.c

.. _`ufshcd_print_pwr_info`:

ufshcd_print_pwr_info
=====================

.. c:function:: void ufshcd_print_pwr_info(struct ufs_hba *hba)

    print power params as saved in hba power info

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_get_intr_mask`:

ufshcd_get_intr_mask
====================

.. c:function:: u32 ufshcd_get_intr_mask(struct ufs_hba *hba)

    Get the interrupt bit mask

    :param hba:
        Pointer to adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_get_intr_mask.description`:

Description
-----------

Returns interrupt bit mask per version

.. _`ufshcd_get_ufs_version`:

ufshcd_get_ufs_version
======================

.. c:function:: u32 ufshcd_get_ufs_version(struct ufs_hba *hba)

    Get the UFS version supported by the HBA

    :param hba:
        Pointer to adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_get_ufs_version.description`:

Description
-----------

Returns UFSHCI version supported by the controller

.. _`ufshcd_is_device_present`:

ufshcd_is_device_present
========================

.. c:function:: bool ufshcd_is_device_present(struct ufs_hba *hba)

    Check if any device connected to the host controller

    :param hba:
        pointer to adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_is_device_present.description`:

Description
-----------

Returns true if device present, false if no device detected

.. _`ufshcd_get_tr_ocs`:

ufshcd_get_tr_ocs
=================

.. c:function:: int ufshcd_get_tr_ocs(struct ufshcd_lrb *lrbp)

    Get the UTRD Overall Command Status

    :param lrbp:
        pointer to local command reference block
    :type lrbp: struct ufshcd_lrb \*

.. _`ufshcd_get_tr_ocs.description`:

Description
-----------

This function is used to get the OCS field from UTRD
Returns the OCS field in the UTRD

.. _`ufshcd_get_tm_free_slot`:

ufshcd_get_tm_free_slot
=======================

.. c:function:: bool ufshcd_get_tm_free_slot(struct ufs_hba *hba, int *free_slot)

    get a free slot for task management request

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param free_slot:
        pointer to variable with available slot value
    :type free_slot: int \*

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

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param pos:
        position of the bit to be cleared
    :type pos: u32

.. _`ufshcd_utmrl_clear`:

ufshcd_utmrl_clear
==================

.. c:function:: void ufshcd_utmrl_clear(struct ufs_hba *hba, u32 pos)

    Clear a bit in UTRMLCLR register

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param pos:
        position of the bit to be cleared
    :type pos: u32

.. _`ufshcd_outstanding_req_clear`:

ufshcd_outstanding_req_clear
============================

.. c:function:: void ufshcd_outstanding_req_clear(struct ufs_hba *hba, int tag)

    Clear a bit in outstanding request field

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param tag:
        position of the bit to be cleared
    :type tag: int

.. _`ufshcd_get_lists_status`:

ufshcd_get_lists_status
=======================

.. c:function:: int ufshcd_get_lists_status(u32 reg)

    Check UCRDY, UTRLRDY and UTMRLRDY

    :param reg:
        Register value of host controller status
    :type reg: u32

.. _`ufshcd_get_lists_status.description`:

Description
-----------

Returns integer, 0 on Success and positive value if failed

.. _`ufshcd_get_uic_cmd_result`:

ufshcd_get_uic_cmd_result
=========================

.. c:function:: int ufshcd_get_uic_cmd_result(struct ufs_hba *hba)

    Get the UIC command result

    :param hba:
        Pointer to adapter instance
    :type hba: struct ufs_hba \*

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

    :param hba:
        Pointer to adapter instance
    :type hba: struct ufs_hba \*

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

    :param ucd_rsp_ptr:
        pointer to response UPIU
    :type ucd_rsp_ptr: struct utp_upiu_rsp \*

.. _`ufshcd_get_rsp_upiu_result`:

ufshcd_get_rsp_upiu_result
==========================

.. c:function:: int ufshcd_get_rsp_upiu_result(struct utp_upiu_rsp *ucd_rsp_ptr)

    Get the result from response UPIU

    :param ucd_rsp_ptr:
        pointer to response UPIU
    :type ucd_rsp_ptr: struct utp_upiu_rsp \*

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

    :param ucd_rsp_ptr:
        pointer to response UPIU
    :type ucd_rsp_ptr: struct utp_upiu_rsp \*

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

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_config_intr_aggr`:

ufshcd_config_intr_aggr
=======================

.. c:function:: void ufshcd_config_intr_aggr(struct ufs_hba *hba, u8 cnt, u8 tmout)

    Configure interrupt aggregation values.

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param cnt:
        Interrupt aggregation counter threshold
    :type cnt: u8

    :param tmout:
        Interrupt aggregation timeout value
    :type tmout: u8

.. _`ufshcd_disable_intr_aggr`:

ufshcd_disable_intr_aggr
========================

.. c:function:: void ufshcd_disable_intr_aggr(struct ufs_hba *hba)

    Disables interrupt aggregation.

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_enable_run_stop_reg`:

ufshcd_enable_run_stop_reg
==========================

.. c:function:: void ufshcd_enable_run_stop_reg(struct ufs_hba *hba)

    Enable run-stop registers, When run-stop registers are set to 1, it indicates the host controller that it can process the requests

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_hba_start`:

ufshcd_hba_start
================

.. c:function:: void ufshcd_hba_start(struct ufs_hba *hba)

    Start controller initialization sequence

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_is_hba_active`:

ufshcd_is_hba_active
====================

.. c:function:: bool ufshcd_is_hba_active(struct ufs_hba *hba)

    Get controller state

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_is_hba_active.description`:

Description
-----------

Returns false if controller is active, true otherwise

.. _`ufshcd_is_devfreq_scaling_required`:

ufshcd_is_devfreq_scaling_required
==================================

.. c:function:: bool ufshcd_is_devfreq_scaling_required(struct ufs_hba *hba, bool scale_up)

    check if scaling is required or not

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param scale_up:
        True if scaling up and false if scaling down
    :type scale_up: bool

.. _`ufshcd_is_devfreq_scaling_required.description`:

Description
-----------

Returns true if scaling is required, false otherwise.

.. _`ufshcd_scale_gear`:

ufshcd_scale_gear
=================

.. c:function:: int ufshcd_scale_gear(struct ufs_hba *hba, bool scale_up)

    scale up/down UFS gear

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param scale_up:
        True for scaling up gear and false for scaling down
    :type scale_up: bool

.. _`ufshcd_scale_gear.description`:

Description
-----------

Returns 0 for success,
Returns -EBUSY if scaling can't happen at this time
Returns non-zero for any other errors

.. _`ufshcd_devfreq_scale`:

ufshcd_devfreq_scale
====================

.. c:function:: int ufshcd_devfreq_scale(struct ufs_hba *hba, bool scale_up)

    scale up/down UFS clocks and gear

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param scale_up:
        True for scaling up and false for scalin down
    :type scale_up: bool

.. _`ufshcd_devfreq_scale.description`:

Description
-----------

Returns 0 for success,
Returns -EBUSY if scaling can't happen at this time
Returns non-zero for any other errors

.. _`ufshcd_hold`:

ufshcd_hold
===========

.. c:function:: int ufshcd_hold(struct ufs_hba *hba, bool async)

    Enable clocks that were gated earlier due to ufshcd_release. Also, exit from hibern8 mode and set the link as active.

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param async:
        This indicates whether caller should ungate clocks asynchronously.
    :type async: bool

.. _`ufshcd_send_command`:

ufshcd_send_command
===================

.. c:function:: void ufshcd_send_command(struct ufs_hba *hba, unsigned int task_tag)

    Send SCSI or device management commands

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param task_tag:
        Task tag of the command
    :type task_tag: unsigned int

.. _`ufshcd_copy_sense_data`:

ufshcd_copy_sense_data
======================

.. c:function:: void ufshcd_copy_sense_data(struct ufshcd_lrb *lrbp)

    Copy sense data in case of check condition

    :param lrbp:
        pointer to local reference block
    :type lrbp: struct ufshcd_lrb \*

.. _`ufshcd_copy_query_response`:

ufshcd_copy_query_response
==========================

.. c:function:: int ufshcd_copy_query_response(struct ufs_hba *hba, struct ufshcd_lrb *lrbp)

    Copy the Query Response and the data descriptor

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param lrbp:
        pointer to local reference block
    :type lrbp: struct ufshcd_lrb \*

.. _`ufshcd_hba_capabilities`:

ufshcd_hba_capabilities
=======================

.. c:function:: void ufshcd_hba_capabilities(struct ufs_hba *hba)

    Read controller capabilities

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_ready_for_uic_cmd`:

ufshcd_ready_for_uic_cmd
========================

.. c:function:: bool ufshcd_ready_for_uic_cmd(struct ufs_hba *hba)

    Check if controller is ready to accept UIC commands

    :param hba:
        per adapter instance
        Return true on success, else false
    :type hba: struct ufs_hba \*

.. _`ufshcd_get_upmcrs`:

ufshcd_get_upmcrs
=================

.. c:function:: u8 ufshcd_get_upmcrs(struct ufs_hba *hba)

    Get the power mode change request status

    :param hba:
        Pointer to adapter instance
    :type hba: struct ufs_hba \*

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

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param uic_cmd:
        UIC command
    :type uic_cmd: struct uic_command \*

.. _`ufshcd_dispatch_uic_cmd.description`:

Description
-----------

Mutex must be held.

.. _`ufshcd_wait_for_uic_cmd`:

ufshcd_wait_for_uic_cmd
=======================

.. c:function:: int ufshcd_wait_for_uic_cmd(struct ufs_hba *hba, struct uic_command *uic_cmd)

    Wait complectioin of UIC command

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param uic_cmd:
        UIC command
    :type uic_cmd: struct uic_command \*

.. _`ufshcd_wait_for_uic_cmd.description`:

Description
-----------

Must be called with mutex held.
Returns 0 only if success.

.. _`__ufshcd_send_uic_cmd`:

\__ufshcd_send_uic_cmd
======================

.. c:function:: int __ufshcd_send_uic_cmd(struct ufs_hba *hba, struct uic_command *uic_cmd, bool completion)

    Send UIC commands and retrieve the result

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param uic_cmd:
        UIC command
    :type uic_cmd: struct uic_command \*

    :param completion:
        initialize the completion only if this is set to true
    :type completion: bool

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

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param uic_cmd:
        UIC command
    :type uic_cmd: struct uic_command \*

.. _`ufshcd_send_uic_cmd.description`:

Description
-----------

Returns 0 only if success.

.. _`ufshcd_map_sg`:

ufshcd_map_sg
=============

.. c:function:: int ufshcd_map_sg(struct ufs_hba *hba, struct ufshcd_lrb *lrbp)

    Map scatter-gather list to prdt

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param lrbp:
        pointer to local reference block
    :type lrbp: struct ufshcd_lrb \*

.. _`ufshcd_map_sg.description`:

Description
-----------

Returns 0 in case of success, non-zero value in case of failure

.. _`ufshcd_enable_intr`:

ufshcd_enable_intr
==================

.. c:function:: void ufshcd_enable_intr(struct ufs_hba *hba, u32 intrs)

    enable interrupts

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param intrs:
        interrupt bits
    :type intrs: u32

.. _`ufshcd_disable_intr`:

ufshcd_disable_intr
===================

.. c:function:: void ufshcd_disable_intr(struct ufs_hba *hba, u32 intrs)

    disable interrupts

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param intrs:
        interrupt bits
    :type intrs: u32

.. _`ufshcd_prepare_req_desc_hdr`:

ufshcd_prepare_req_desc_hdr
===========================

.. c:function:: void ufshcd_prepare_req_desc_hdr(struct ufshcd_lrb *lrbp, u32 *upiu_flags, enum dma_data_direction cmd_dir)

    Fills the requests header descriptor according to request

    :param lrbp:
        pointer to local reference block
    :type lrbp: struct ufshcd_lrb \*

    :param upiu_flags:
        flags required in the header
    :type upiu_flags: u32 \*

    :param cmd_dir:
        requests data direction
    :type cmd_dir: enum dma_data_direction

.. _`ufshcd_prepare_utp_scsi_cmd_upiu`:

ufshcd_prepare_utp_scsi_cmd_upiu
================================

.. c:function:: void ufshcd_prepare_utp_scsi_cmd_upiu(struct ufshcd_lrb *lrbp, u32 upiu_flags)

    fills the utp_transfer_req_desc, for scsi commands

    :param lrbp:
        local reference block pointer
    :type lrbp: struct ufshcd_lrb \*

    :param upiu_flags:
        flags
    :type upiu_flags: u32

.. _`ufshcd_prepare_utp_query_req_upiu`:

ufshcd_prepare_utp_query_req_upiu
=================================

.. c:function:: void ufshcd_prepare_utp_query_req_upiu(struct ufs_hba *hba, struct ufshcd_lrb *lrbp, u32 upiu_flags)

    fills the utp_transfer_req_desc, for query requsts

    :param hba:
        UFS hba
    :type hba: struct ufs_hba \*

    :param lrbp:
        local reference block pointer
    :type lrbp: struct ufshcd_lrb \*

    :param upiu_flags:
        flags
    :type upiu_flags: u32

.. _`ufshcd_comp_devman_upiu`:

ufshcd_comp_devman_upiu
=======================

.. c:function:: int ufshcd_comp_devman_upiu(struct ufs_hba *hba, struct ufshcd_lrb *lrbp)

    UFS Protocol Information Unit(UPIU) for Device Management Purposes

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param lrbp:
        pointer to local reference block
    :type lrbp: struct ufshcd_lrb \*

.. _`ufshcd_comp_scsi_upiu`:

ufshcd_comp_scsi_upiu
=====================

.. c:function:: int ufshcd_comp_scsi_upiu(struct ufs_hba *hba, struct ufshcd_lrb *lrbp)

    UFS Protocol Information Unit(UPIU) for SCSI Purposes

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param lrbp:
        pointer to local reference block
    :type lrbp: struct ufshcd_lrb \*

.. _`ufshcd_upiu_wlun_to_scsi_wlun`:

ufshcd_upiu_wlun_to_scsi_wlun
=============================

.. c:function:: u16 ufshcd_upiu_wlun_to_scsi_wlun(u8 upiu_wlun_id)

    maps UPIU W-LUN id to SCSI W-LUN ID

    :param upiu_wlun_id:
        UPIU W-LUN id
    :type upiu_wlun_id: u8

.. _`ufshcd_upiu_wlun_to_scsi_wlun.description`:

Description
-----------

Returns SCSI W-LUN id

.. _`ufshcd_queuecommand`:

ufshcd_queuecommand
===================

.. c:function:: int ufshcd_queuecommand(struct Scsi_Host *host, struct scsi_cmnd *cmd)

    main entry point for SCSI requests

    :param host:
        SCSI host pointer
    :type host: struct Scsi_Host \*

    :param cmd:
        command from SCSI Midlayer
    :type cmd: struct scsi_cmnd \*

.. _`ufshcd_queuecommand.description`:

Description
-----------

Returns 0 for success, non-zero in case of failure

.. _`ufshcd_dev_cmd_completion`:

ufshcd_dev_cmd_completion
=========================

.. c:function:: int ufshcd_dev_cmd_completion(struct ufs_hba *hba, struct ufshcd_lrb *lrbp)

    handles device management command responses

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param lrbp:
        pointer to local reference block
    :type lrbp: struct ufshcd_lrb \*

.. _`ufshcd_get_dev_cmd_tag`:

ufshcd_get_dev_cmd_tag
======================

.. c:function:: bool ufshcd_get_dev_cmd_tag(struct ufs_hba *hba, int *tag_out)

    Get device management command tag

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

    :param tag_out:
        pointer to variable with available slot value
    :type tag_out: int \*

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

    API for sending device management requests

    :param hba:
        UFS hba
    :type hba: struct ufs_hba \*

    :param cmd_type:
        specifies the type (NOP, Query...)
    :type cmd_type: enum dev_cmd_type

    :param timeout:
        time in seconds
    :type timeout: int

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

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

    :param request:
        address of the request pointer to be initialized
    :type request: struct ufs_query_req \*\*

    :param response:
        address of the response pointer to be initialized
    :type response: struct ufs_query_res \*\*

    :param opcode:
        operation to perform
    :type opcode: enum query_opcode

    :param idn:
        flag idn to access
    :type idn: u8

    :param index:
        LU number to access
    :type index: u8

    :param selector:
        query/flag/descriptor further identification
    :type selector: u8

.. _`ufshcd_query_flag`:

ufshcd_query_flag
=================

.. c:function:: int ufshcd_query_flag(struct ufs_hba *hba, enum query_opcode opcode, enum flag_idn idn, bool *flag_res)

    API function for sending flag query requests

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

    :param opcode:
        flag query to perform
    :type opcode: enum query_opcode

    :param idn:
        flag idn to access
    :type idn: enum flag_idn

    :param flag_res:
        the flag value after the query request completes
    :type flag_res: bool \*

.. _`ufshcd_query_flag.description`:

Description
-----------

Returns 0 for success, non-zero in case of failure

.. _`ufshcd_query_attr`:

ufshcd_query_attr
=================

.. c:function:: int ufshcd_query_attr(struct ufs_hba *hba, enum query_opcode opcode, enum attr_idn idn, u8 index, u8 selector, u32 *attr_val)

    API function for sending attribute requests

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

    :param opcode:
        attribute opcode
    :type opcode: enum query_opcode

    :param idn:
        attribute idn to access
    :type idn: enum attr_idn

    :param index:
        index field
    :type index: u8

    :param selector:
        selector field
    :type selector: u8

    :param attr_val:
        the attribute value after the query request completes
    :type attr_val: u32 \*

.. _`ufshcd_query_attr.description`:

Description
-----------

Returns 0 for success, non-zero in case of failure

.. _`ufshcd_query_attr_retry`:

ufshcd_query_attr_retry
=======================

.. c:function:: int ufshcd_query_attr_retry(struct ufs_hba *hba, enum query_opcode opcode, enum attr_idn idn, u8 index, u8 selector, u32 *attr_val)

    API function for sending query attribute with retries

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

    :param opcode:
        attribute opcode
    :type opcode: enum query_opcode

    :param idn:
        attribute idn to access
    :type idn: enum attr_idn

    :param index:
        index field
    :type index: u8

    :param selector:
        selector field
    :type selector: u8

    :param attr_val:
        the attribute value after the query request
        completes
    :type attr_val: u32 \*

.. _`ufshcd_query_attr_retry.description`:

Description
-----------

Returns 0 for success, non-zero in case of failure

.. _`ufshcd_query_descriptor_retry`:

ufshcd_query_descriptor_retry
=============================

.. c:function:: int ufshcd_query_descriptor_retry(struct ufs_hba *hba, enum query_opcode opcode, enum desc_idn idn, u8 index, u8 selector, u8 *desc_buf, int *buf_len)

    API function for sending descriptor requests

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

    :param opcode:
        attribute opcode
    :type opcode: enum query_opcode

    :param idn:
        attribute idn to access
    :type idn: enum desc_idn

    :param index:
        index field
    :type index: u8

    :param selector:
        selector field
    :type selector: u8

    :param desc_buf:
        the buffer that contains the descriptor
    :type desc_buf: u8 \*

    :param buf_len:
        length parameter passed to the device
    :type buf_len: int \*

.. _`ufshcd_query_descriptor_retry.description`:

Description
-----------

Returns 0 for success, non-zero in case of failure.
The buf_len parameter will contain, on return, the length parameter
received on the response.

.. _`ufshcd_read_desc_length`:

ufshcd_read_desc_length
=======================

.. c:function:: int ufshcd_read_desc_length(struct ufs_hba *hba, enum desc_idn desc_id, int desc_index, int *desc_length)

    read the specified descriptor length from header

    :param hba:
        Pointer to adapter instance
    :type hba: struct ufs_hba \*

    :param desc_id:
        descriptor idn value
    :type desc_id: enum desc_idn

    :param desc_index:
        descriptor index
    :type desc_index: int

    :param desc_length:
        pointer to variable to read the length of descriptor
    :type desc_length: int \*

.. _`ufshcd_read_desc_length.description`:

Description
-----------

Return 0 in case of success, non-zero otherwise

.. _`ufshcd_map_desc_id_to_length`:

ufshcd_map_desc_id_to_length
============================

.. c:function:: int ufshcd_map_desc_id_to_length(struct ufs_hba *hba, enum desc_idn desc_id, int *desc_len)

    map descriptor IDN to its length

    :param hba:
        Pointer to adapter instance
    :type hba: struct ufs_hba \*

    :param desc_id:
        descriptor idn value
    :type desc_id: enum desc_idn

    :param desc_len:
        mapped desc length (out)
    :type desc_len: int \*

.. _`ufshcd_map_desc_id_to_length.description`:

Description
-----------

Return 0 in case of success, non-zero otherwise

.. _`ufshcd_read_desc_param`:

ufshcd_read_desc_param
======================

.. c:function:: int ufshcd_read_desc_param(struct ufs_hba *hba, enum desc_idn desc_id, int desc_index, u8 param_offset, u8 *param_read_buf, u8 param_size)

    read the specified descriptor parameter

    :param hba:
        Pointer to adapter instance
    :type hba: struct ufs_hba \*

    :param desc_id:
        descriptor idn value
    :type desc_id: enum desc_idn

    :param desc_index:
        descriptor index
    :type desc_index: int

    :param param_offset:
        offset of the parameter to read
    :type param_offset: u8

    :param param_read_buf:
        pointer to buffer where parameter would be read
    :type param_read_buf: u8 \*

    :param param_size:
        sizeof(param_read_buf)
    :type param_size: u8

.. _`ufshcd_read_desc_param.description`:

Description
-----------

Return 0 in case of success, non-zero otherwise

.. _`ufshcd_read_string_desc`:

ufshcd_read_string_desc
=======================

.. c:function:: int ufshcd_read_string_desc(struct ufs_hba *hba, int desc_index, u8 *buf, u32 size, bool ascii)

    read string descriptor

    :param hba:
        pointer to adapter instance
    :type hba: struct ufs_hba \*

    :param desc_index:
        descriptor index
    :type desc_index: int

    :param buf:
        pointer to buffer where descriptor would be read
    :type buf: u8 \*

    :param size:
        size of buf
    :type size: u32

    :param ascii:
        if true convert from unicode to ascii characters
    :type ascii: bool

.. _`ufshcd_read_string_desc.description`:

Description
-----------

Return 0 in case of success, non-zero otherwise

.. _`ufshcd_read_unit_desc_param`:

ufshcd_read_unit_desc_param
===========================

.. c:function:: int ufshcd_read_unit_desc_param(struct ufs_hba *hba, int lun, enum unit_desc_param param_offset, u8 *param_read_buf, u32 param_size)

    read the specified unit descriptor parameter

    :param hba:
        Pointer to adapter instance
    :type hba: struct ufs_hba \*

    :param lun:
        lun id
    :type lun: int

    :param param_offset:
        offset of the parameter to read
    :type param_offset: enum unit_desc_param

    :param param_read_buf:
        pointer to buffer where parameter would be read
    :type param_read_buf: u8 \*

    :param param_size:
        sizeof(param_read_buf)
    :type param_size: u32

.. _`ufshcd_read_unit_desc_param.description`:

Description
-----------

Return 0 in case of success, non-zero otherwise

.. _`ufshcd_memory_alloc`:

ufshcd_memory_alloc
===================

.. c:function:: int ufshcd_memory_alloc(struct ufs_hba *hba)

    allocate memory for host memory space data structures

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

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

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

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

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_dme_link_startup.description`:

Description
-----------

UIC_CMD_DME_LINK_STARTUP command must be issued to Unipro layer,
in order to initialize the Unipro link startup procedure.
Once the Unipro links are up, the device connected to the controller
is detected.

Returns 0 on success, non-zero value on failure

.. _`ufshcd_dme_reset`:

ufshcd_dme_reset
================

.. c:function:: int ufshcd_dme_reset(struct ufs_hba *hba)

    UIC command for DME_RESET

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_dme_reset.description`:

Description
-----------

DME_RESET command is issued in order to reset UniPro stack.
This function now deal with cold reset.

Returns 0 on success, non-zero value on failure

.. _`ufshcd_dme_enable`:

ufshcd_dme_enable
=================

.. c:function:: int ufshcd_dme_enable(struct ufs_hba *hba)

    UIC command for DME_ENABLE

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_dme_enable.description`:

Description
-----------

DME_ENABLE command is issued in order to enable UniPro stack.

Returns 0 on success, non-zero value on failure

.. _`ufshcd_dme_set_attr`:

ufshcd_dme_set_attr
===================

.. c:function:: int ufshcd_dme_set_attr(struct ufs_hba *hba, u32 attr_sel, u8 attr_set, u32 mib_val, u8 peer)

    UIC command for DME_SET, DME_PEER_SET

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param attr_sel:
        uic command argument1
    :type attr_sel: u32

    :param attr_set:
        attribute set type as uic command argument2
    :type attr_set: u8

    :param mib_val:
        setting value as uic command argument3
    :type mib_val: u32

    :param peer:
        indicate whether peer or local
    :type peer: u8

.. _`ufshcd_dme_set_attr.description`:

Description
-----------

Returns 0 on success, non-zero value on failure

.. _`ufshcd_dme_get_attr`:

ufshcd_dme_get_attr
===================

.. c:function:: int ufshcd_dme_get_attr(struct ufs_hba *hba, u32 attr_sel, u32 *mib_val, u8 peer)

    UIC command for DME_GET, DME_PEER_GET

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param attr_sel:
        uic command argument1
    :type attr_sel: u32

    :param mib_val:
        the value of the attribute as returned by the UIC command
    :type mib_val: u32 \*

    :param peer:
        indicate whether peer or local
    :type peer: u8

.. _`ufshcd_dme_get_attr.description`:

Description
-----------

Returns 0 on success, non-zero value on failure

.. _`ufshcd_uic_pwr_ctrl`:

ufshcd_uic_pwr_ctrl
===================

.. c:function:: int ufshcd_uic_pwr_ctrl(struct ufs_hba *hba, struct uic_command *cmd)

    executes UIC commands (which affects the link power state) and waits for it to take effect.

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param cmd:
        UIC command to execute
    :type cmd: struct uic_command \*

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

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param mode:
        powr mode value
    :type mode: u8

.. _`ufshcd_uic_change_pwr_mode.description`:

Description
-----------

Returns 0 on success, non-zero value on failure

.. _`ufshcd_get_max_pwr_mode`:

ufshcd_get_max_pwr_mode
=======================

.. c:function:: int ufshcd_get_max_pwr_mode(struct ufs_hba *hba)

    reads the max power mode negotiated with device

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_config_pwr_mode`:

ufshcd_config_pwr_mode
======================

.. c:function:: int ufshcd_config_pwr_mode(struct ufs_hba *hba, struct ufs_pa_layer_attr *desired_pwr_mode)

    configure a new power mode

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

    :param desired_pwr_mode:
        desired power configuration
    :type desired_pwr_mode: struct ufs_pa_layer_attr \*

.. _`ufshcd_complete_dev_init`:

ufshcd_complete_dev_init
========================

.. c:function:: int ufshcd_complete_dev_init(struct ufs_hba *hba)

    checks device readiness

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_complete_dev_init.description`:

Description
-----------

Set fDeviceInit flag and poll until device toggles it.

.. _`ufshcd_make_hba_operational`:

ufshcd_make_hba_operational
===========================

.. c:function:: int ufshcd_make_hba_operational(struct ufs_hba *hba)

    Make UFS controller operational

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

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

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param can_sleep:
        perform sleep or just spin
    :type can_sleep: bool

.. _`ufshcd_hba_execute_hce`:

ufshcd_hba_execute_hce
======================

.. c:function:: int ufshcd_hba_execute_hce(struct ufs_hba *hba)

    initialize the controller

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_hba_execute_hce.description`:

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

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_link_startup.description`:

Description
-----------

Returns 0 for success, non-zero in case of failure

.. _`ufshcd_verify_dev_init`:

ufshcd_verify_dev_init
======================

.. c:function:: int ufshcd_verify_dev_init(struct ufs_hba *hba)

    Verify device initialization

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

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

    :param sdev:
        pointer to SCSI device
    :type sdev: struct scsi_device \*

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

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

    :param sdev:
        pointer to SCSI device
    :type sdev: struct scsi_device \*

.. _`ufshcd_slave_alloc`:

ufshcd_slave_alloc
==================

.. c:function:: int ufshcd_slave_alloc(struct scsi_device *sdev)

    handle initial SCSI device configurations

    :param sdev:
        pointer to SCSI device
    :type sdev: struct scsi_device \*

.. _`ufshcd_slave_alloc.description`:

Description
-----------

Returns success

.. _`ufshcd_change_queue_depth`:

ufshcd_change_queue_depth
=========================

.. c:function:: int ufshcd_change_queue_depth(struct scsi_device *sdev, int depth)

    change queue depth

    :param sdev:
        pointer to SCSI device
    :type sdev: struct scsi_device \*

    :param depth:
        required depth to set
    :type depth: int

.. _`ufshcd_change_queue_depth.description`:

Description
-----------

Change queue depth and make sure the max. limits are not crossed.

.. _`ufshcd_slave_configure`:

ufshcd_slave_configure
======================

.. c:function:: int ufshcd_slave_configure(struct scsi_device *sdev)

    adjust SCSI device configurations

    :param sdev:
        pointer to SCSI device
    :type sdev: struct scsi_device \*

.. _`ufshcd_slave_destroy`:

ufshcd_slave_destroy
====================

.. c:function:: void ufshcd_slave_destroy(struct scsi_device *sdev)

    remove SCSI device configurations

    :param sdev:
        pointer to SCSI device
    :type sdev: struct scsi_device \*

.. _`ufshcd_scsi_cmd_status`:

ufshcd_scsi_cmd_status
======================

.. c:function:: int ufshcd_scsi_cmd_status(struct ufshcd_lrb *lrbp, int scsi_status)

    Update SCSI command result based on SCSI status

    :param lrbp:
        pointer to local reference block of completed command
    :type lrbp: struct ufshcd_lrb \*

    :param scsi_status:
        SCSI command status
    :type scsi_status: int

.. _`ufshcd_scsi_cmd_status.description`:

Description
-----------

Returns value base on SCSI command status

.. _`ufshcd_transfer_rsp_status`:

ufshcd_transfer_rsp_status
==========================

.. c:function:: int ufshcd_transfer_rsp_status(struct ufs_hba *hba, struct ufshcd_lrb *lrbp)

    Get overall status of the response

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param lrbp:
        pointer to local reference block of completed command
    :type lrbp: struct ufshcd_lrb \*

.. _`ufshcd_transfer_rsp_status.description`:

Description
-----------

Returns result of the command to notify SCSI midlayer

.. _`ufshcd_uic_cmd_compl`:

ufshcd_uic_cmd_compl
====================

.. c:function:: void ufshcd_uic_cmd_compl(struct ufs_hba *hba, u32 intr_status)

    handle completion of uic command

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param intr_status:
        interrupt status generated by the controller
    :type intr_status: u32

.. _`__ufshcd_transfer_req_compl`:

\__ufshcd_transfer_req_compl
============================

.. c:function:: void __ufshcd_transfer_req_compl(struct ufs_hba *hba, unsigned long completed_reqs)

    handle SCSI and query command completion

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param completed_reqs:
        requests to complete
    :type completed_reqs: unsigned long

.. _`ufshcd_transfer_req_compl`:

ufshcd_transfer_req_compl
=========================

.. c:function:: void ufshcd_transfer_req_compl(struct ufs_hba *hba)

    handle SCSI and query command completion

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_disable_ee`:

ufshcd_disable_ee
=================

.. c:function:: int ufshcd_disable_ee(struct ufs_hba *hba, u16 mask)

    disable exception event

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

    :param mask:
        exception event to disable
    :type mask: u16

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

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

    :param mask:
        exception event to enable
    :type mask: u16

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

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

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

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

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

    force reset auto bkops state

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_force_reset_auto_bkops.description`:

Description
-----------

After a device reset the device may toggle the BKOPS_EN flag
to default value. The s/w tracking variables should be updated
as well. This function would change the auto-bkops state based on
UFSHCD_CAP_KEEP_AUTO_BKOPS_ENABLED_EXCEPT_SUSPEND.

.. _`ufshcd_bkops_ctrl`:

ufshcd_bkops_ctrl
=================

.. c:function:: int ufshcd_bkops_ctrl(struct ufs_hba *hba, enum bkops_status status)

    control the auto bkops based on current bkops status

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

    :param status:
        bkops_status value
    :type status: enum bkops_status

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

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

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

    :param work:
        pointer to work data
    :type work: struct work_struct \*

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

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_quirk_dl_nac_errors.description`:

Description
-----------

Returns true if error handling is required, false otherwise

.. _`ufshcd_err_handler`:

ufshcd_err_handler
==================

.. c:function:: void ufshcd_err_handler(struct work_struct *work)

    handle UFS errors that require s/w attention

    :param work:
        pointer to work structure
    :type work: struct work_struct \*

.. _`ufshcd_update_uic_error`:

ufshcd_update_uic_error
=======================

.. c:function:: void ufshcd_update_uic_error(struct ufs_hba *hba)

    check and set fatal UIC error flags.

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_check_errors`:

ufshcd_check_errors
===================

.. c:function:: void ufshcd_check_errors(struct ufs_hba *hba)

    Check for errors that need s/w attention

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_tmc_handler`:

ufshcd_tmc_handler
==================

.. c:function:: void ufshcd_tmc_handler(struct ufs_hba *hba)

    handle task management function completion

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_sl_intr`:

ufshcd_sl_intr
==============

.. c:function:: void ufshcd_sl_intr(struct ufs_hba *hba, u32 intr_status)

    Interrupt service routine

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param intr_status:
        contains interrupts generated by the controller
    :type intr_status: u32

.. _`ufshcd_intr`:

ufshcd_intr
===========

.. c:function:: irqreturn_t ufshcd_intr(int irq, void *__hba)

    Main interrupt service routine

    :param irq:
        irq number
    :type irq: int

    :param __hba:
        pointer to adapter instance
    :type __hba: void \*

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

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param lun_id:
        LUN ID to which TM command is sent
    :type lun_id: int

    :param task_id:
        task ID to which the TM command is applicable
    :type task_id: int

    :param tm_function:
        task management function opcode
    :type tm_function: u8

    :param tm_response:
        task management service response return value
    :type tm_response: u8 \*

.. _`ufshcd_issue_tm_cmd.description`:

Description
-----------

Returns non-zero value on error, zero on success.

.. _`ufshcd_issue_devman_upiu_cmd`:

ufshcd_issue_devman_upiu_cmd
============================

.. c:function:: int ufshcd_issue_devman_upiu_cmd(struct ufs_hba *hba, struct utp_upiu_req *req_upiu, struct utp_upiu_req *rsp_upiu, u8 *desc_buff, int *buff_len, int cmd_type, enum query_opcode desc_op)

    API for sending "utrd" type requests

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

    :param req_upiu:
        upiu request
    :type req_upiu: struct utp_upiu_req \*

    :param rsp_upiu:
        upiu reply
    :type rsp_upiu: struct utp_upiu_req \*

    :param desc_buff:
        pointer to descriptor buffer, NULL if NA
    :type desc_buff: u8 \*

    :param buff_len:
        descriptor size, 0 if NA
    :type buff_len: int \*

    :param cmd_type:
        *undescribed*
    :type cmd_type: int

    :param desc_op:
        descriptor operation
    :type desc_op: enum query_opcode

.. _`ufshcd_issue_devman_upiu_cmd.description`:

Description
-----------

Those type of requests uses UTP Transfer Request Descriptor - utrd.
Therefore, it "rides" the device management infrastructure: uses its tag and
tasks work queues.

Since there is only one available tag for device management commands,
the caller is expected to hold the hba->dev_cmd.lock mutex.

.. _`ufshcd_exec_raw_upiu_cmd`:

ufshcd_exec_raw_upiu_cmd
========================

.. c:function:: int ufshcd_exec_raw_upiu_cmd(struct ufs_hba *hba, struct utp_upiu_req *req_upiu, struct utp_upiu_req *rsp_upiu, int msgcode, u8 *desc_buff, int *buff_len, enum query_opcode desc_op)

    API function for sending raw upiu commands

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

    :param req_upiu:
        upiu request
    :type req_upiu: struct utp_upiu_req \*

    :param rsp_upiu:
        upiu reply - only 8 DW as we do not support scsi commands
    :type rsp_upiu: struct utp_upiu_req \*

    :param msgcode:
        message code, one of UPIU Transaction Codes Initiator to Target
    :type msgcode: int

    :param desc_buff:
        pointer to descriptor buffer, NULL if NA
    :type desc_buff: u8 \*

    :param buff_len:
        descriptor size, 0 if NA
    :type buff_len: int \*

    :param desc_op:
        descriptor operation
    :type desc_op: enum query_opcode

.. _`ufshcd_exec_raw_upiu_cmd.description`:

Description
-----------

Supports UTP Transfer requests (nop and query), and UTP Task
Management requests.
It is up to the caller to fill the upiu conent properly, as it will
be copied without any further input validations.

.. _`ufshcd_eh_device_reset_handler`:

ufshcd_eh_device_reset_handler
==============================

.. c:function:: int ufshcd_eh_device_reset_handler(struct scsi_cmnd *cmd)

    device reset handler registered to scsi layer.

    :param cmd:
        SCSI command pointer
    :type cmd: struct scsi_cmnd \*

.. _`ufshcd_eh_device_reset_handler.description`:

Description
-----------

Returns SUCCESS/FAILED

.. _`ufshcd_abort`:

ufshcd_abort
============

.. c:function:: int ufshcd_abort(struct scsi_cmnd *cmd)

    abort a specific command

    :param cmd:
        SCSI command pointer
    :type cmd: struct scsi_cmnd \*

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

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

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

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

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

    host reset handler registered to scsi layer

    :param cmd:
        SCSI command pointer
    :type cmd: struct scsi_cmnd \*

.. _`ufshcd_eh_host_reset_handler.description`:

Description
-----------

Returns SUCCESS/FAILED

.. _`ufshcd_get_max_icc_level`:

ufshcd_get_max_icc_level
========================

.. c:function:: u32 ufshcd_get_max_icc_level(int sup_curr_uA, u32 start_scan, char *buff)

    calculate the ICC level

    :param sup_curr_uA:
        max. current supported by the regulator
    :type sup_curr_uA: int

    :param start_scan:
        row at the desc table to start scan from
    :type start_scan: u32

    :param buff:
        power descriptor buffer
    :type buff: char \*

.. _`ufshcd_get_max_icc_level.description`:

Description
-----------

Returns calculated max ICC level for specific regulator

.. _`ufshcd_find_max_sup_active_icc_level`:

ufshcd_find_max_sup_active_icc_level
====================================

.. c:function:: u32 ufshcd_find_max_sup_active_icc_level(struct ufs_hba *hba, u8 *desc_buf, int len)

    calculate the max ICC level In case regulators are not initialized we'll return 0

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

    :param desc_buf:
        power descriptor buffer to extract ICC levels from.
    :type desc_buf: u8 \*

    :param len:
        length of desc_buff
    :type len: int

.. _`ufshcd_find_max_sup_active_icc_level.description`:

Description
-----------

Returns calculated ICC level

.. _`ufshcd_scsi_add_wlus`:

ufshcd_scsi_add_wlus
====================

.. c:function:: int ufshcd_scsi_add_wlus(struct ufs_hba *hba)

    Adds required W-LUs

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

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

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

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

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_tune_pa_hibern8time.description`:

Description
-----------

PA_Hibern8Time parameter can be tuned manually if UniPro version is less than
1.61. PA_Hibern8Time needs to be maximum of local M-PHY's
TX_HIBERN8TIME_CAPABILITY & peer M-PHY's RX_HIBERN8TIME_CAPABILITY.
This optimal value can help reduce the hibern8 exit latency.

Returns zero on success, non-zero error value on failure.

.. _`ufshcd_quirk_tune_host_pa_tactivate`:

ufshcd_quirk_tune_host_pa_tactivate
===================================

.. c:function:: int ufshcd_quirk_tune_host_pa_tactivate(struct ufs_hba *hba)

    Ensures that host PA_TACTIVATE is less than device PA_TACTIVATE time.

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_quirk_tune_host_pa_tactivate.description`:

Description
-----------

Some UFS devices require host PA_TACTIVATE to be lower than device
PA_TACTIVATE, we need to enable UFS_DEVICE_QUIRK_HOST_PA_TACTIVATE quirk
for such devices.

Returns zero on success, non-zero error value on failure.

.. _`ufshcd_probe_hba`:

ufshcd_probe_hba
================

.. c:function:: int ufshcd_probe_hba(struct ufs_hba *hba)

    probe hba to detect device and initialize

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_probe_hba.description`:

Description
-----------

Execute link-startup and verify device initialization

.. _`ufshcd_async_scan`:

ufshcd_async_scan
=================

.. c:function:: void ufshcd_async_scan(void *data, async_cookie_t cookie)

    asynchronous execution for probing hba

    :param data:
        data pointer to pass to this function
    :type data: void \*

    :param cookie:
        cookie data
    :type cookie: async_cookie_t

.. _`ufshcd_set_dev_pwr_mode`:

ufshcd_set_dev_pwr_mode
=======================

.. c:function:: int ufshcd_set_dev_pwr_mode(struct ufs_hba *hba, enum ufs_dev_pwr_mode pwr_mode)

    sends START STOP UNIT command to set device power mode

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param pwr_mode:
        device power mode to set
    :type pwr_mode: enum ufs_dev_pwr_mode

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

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param pm_op:
        desired low power operation type
    :type pm_op: enum ufs_pm_op

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

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

    :param pm_op:
        runtime PM or system PM
    :type pm_op: enum ufs_pm_op

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

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

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

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_system_resume.description`:

Description
-----------

Returns 0 for success and non-zero for failure

.. _`ufshcd_runtime_suspend`:

ufshcd_runtime_suspend
======================

.. c:function:: int ufshcd_runtime_suspend(struct ufs_hba *hba)

    runtime suspend routine

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

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

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

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

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_shutdown.description`:

Description
-----------

This function would power off both UFS device and UFS link.

Returns 0 always to allow force shutdown even in case of errors.

.. _`ufshcd_remove`:

ufshcd_remove
=============

.. c:function:: void ufshcd_remove(struct ufs_hba *hba)

    de-allocate SCSI host and host memory space data structure memory

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_dealloc_host`:

ufshcd_dealloc_host
===================

.. c:function:: void ufshcd_dealloc_host(struct ufs_hba *hba)

    deallocate Host Bus Adapter (HBA)

    :param hba:
        pointer to Host Bus Adapter (HBA)
    :type hba: struct ufs_hba \*

.. _`ufshcd_set_dma_mask`:

ufshcd_set_dma_mask
===================

.. c:function:: int ufshcd_set_dma_mask(struct ufs_hba *hba)

    Set dma mask based on the controller addressing capability

    :param hba:
        per adapter instance
    :type hba: struct ufs_hba \*

.. _`ufshcd_set_dma_mask.description`:

Description
-----------

Returns 0 for success, non-zero for failure

.. _`ufshcd_alloc_host`:

ufshcd_alloc_host
=================

.. c:function:: int ufshcd_alloc_host(struct device *dev, struct ufs_hba **hba_handle)

    allocate Host Bus Adapter (HBA)

    :param dev:
        pointer to device handle
    :type dev: struct device \*

    :param hba_handle:
        driver private handle
        Returns 0 on success, non-zero value on failure
    :type hba_handle: struct ufs_hba \*\*

.. _`ufshcd_init`:

ufshcd_init
===========

.. c:function:: int ufshcd_init(struct ufs_hba *hba, void __iomem *mmio_base, unsigned int irq)

    Driver initialization routine

    :param hba:
        per-adapter instance
    :type hba: struct ufs_hba \*

    :param mmio_base:
        base register address
    :type mmio_base: void __iomem \*

    :param irq:
        Interrupt line of device
        Returns 0 on success, non-zero value on failure
    :type irq: unsigned int

.. This file was automatic generated / don't edit.

