.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/megaraid/megaraid_sas_fusion.c

.. _`megasas_check_same_4gb_region`:

megasas_check_same_4gb_region
=============================

.. c:function:: bool megasas_check_same_4gb_region(struct megasas_instance *instance, dma_addr_t start_addr, size_t size)

    check if allocation crosses same 4GB boundary or not \ ``instance``\  -                          adapter's soft instance start_addr -                 start address of DMA allocation size -                               size of allocation in bytes return -                             true : allocation does not cross same 4GB boundary false: allocation crosses same 4GB boundary

    :param instance:
        *undescribed*
    :type instance: struct megasas_instance \*

    :param start_addr:
        *undescribed*
    :type start_addr: dma_addr_t

    :param size:
        *undescribed*
    :type size: size_t

.. _`megasas_enable_intr_fusion`:

megasas_enable_intr_fusion
==========================

.. c:function:: void megasas_enable_intr_fusion(struct megasas_instance *instance)

    Enables interrupts

    :param instance:
        *undescribed*
    :type instance: struct megasas_instance \*

.. _`megasas_disable_intr_fusion`:

megasas_disable_intr_fusion
===========================

.. c:function:: void megasas_disable_intr_fusion(struct megasas_instance *instance)

    Disables interrupt

    :param instance:
        *undescribed*
    :type instance: struct megasas_instance \*

.. _`megasas_get_cmd_fusion`:

megasas_get_cmd_fusion
======================

.. c:function:: struct megasas_cmd_fusion *megasas_get_cmd_fusion(struct megasas_instance *instance, u32 blk_tag)

    Get a command from the free pool

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

    :param blk_tag:
        *undescribed*
    :type blk_tag: u32

.. _`megasas_get_cmd_fusion.description`:

Description
-----------

Returns a blk_tag indexed mpt frame

.. _`megasas_return_cmd_fusion`:

megasas_return_cmd_fusion
=========================

.. c:function:: void megasas_return_cmd_fusion(struct megasas_instance *instance, struct megasas_cmd_fusion *cmd)

    Return a cmd to free command pool

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

    :param cmd:
        Command packet to be returned to free command pool
    :type cmd: struct megasas_cmd_fusion \*

.. _`megasas_fire_cmd_fusion`:

megasas_fire_cmd_fusion
=======================

.. c:function:: void megasas_fire_cmd_fusion(struct megasas_instance *instance, union MEGASAS_REQUEST_DESCRIPTOR_UNION *req_desc)

    Sends command to the FW

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

    :param req_desc:
        64bit Request descriptor
    :type req_desc: union MEGASAS_REQUEST_DESCRIPTOR_UNION \*

.. _`megasas_fire_cmd_fusion.description`:

Description
-----------

Perform PCI Write.

.. _`megasas_fusion_update_can_queue`:

megasas_fusion_update_can_queue
===============================

.. c:function:: void megasas_fusion_update_can_queue(struct megasas_instance *instance, int fw_boot_context)

    Do all Adapter Queue depth related calculations here

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

    :param fw_boot_context:
        *undescribed*
    :type fw_boot_context: int

.. _`megasas_fusion_update_can_queue.fw_boot_context`:

fw_boot_context
---------------

Whether this function called during probe or after OCR

This function is only for fusion controllers.
Update host can queue, if firmware downgrade max supported firmware commands.
Firmware upgrade case will be skiped because underlying firmware has
more resource than exposed to the OS.

.. _`megasas_free_cmds_fusion`:

megasas_free_cmds_fusion
========================

.. c:function:: void megasas_free_cmds_fusion(struct megasas_instance *instance)

    Free all the cmds in the free cmd pool

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

.. _`megasas_create_sg_sense_fusion`:

megasas_create_sg_sense_fusion
==============================

.. c:function:: int megasas_create_sg_sense_fusion(struct megasas_instance *instance)

    Creates DMA pool for cmd frames

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

.. _`megasas_alloc_cmds_fusion`:

megasas_alloc_cmds_fusion
=========================

.. c:function:: int megasas_alloc_cmds_fusion(struct megasas_instance *instance)

    Allocates the command packets

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

.. _`megasas_alloc_cmds_fusion.description`:

Description
-----------


Each frame has a 32-bit field called context. This context is used to get
back the megasas_cmd_fusion from the frame when a frame gets completed
In this driver, the 32 bit values are the indices into an array cmd_list.
This array is used only to look up the megasas_cmd_fusion given the context.
The free commands themselves are maintained in a linked list called cmd_pool.

cmds are formed in the io_request and sg_frame members of the
megasas_cmd_fusion. The context field is used to get a request descriptor
and is used as SMID of the cmd.
SMID value range is from 1 to max_fw_cmds.

.. _`wait_and_poll`:

wait_and_poll
=============

.. c:function:: int wait_and_poll(struct megasas_instance *instance, struct megasas_cmd *cmd, int seconds)

    Issues a polling command

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

    :param cmd:
        Command packet to be issued
    :type cmd: struct megasas_cmd \*

    :param seconds:
        *undescribed*
    :type seconds: int

.. _`wait_and_poll.description`:

Description
-----------

For polling, MFI requires the cmd_status to be set to 0xFF before posting.

.. _`megasas_ioc_init_fusion`:

megasas_ioc_init_fusion
=======================

.. c:function:: int megasas_ioc_init_fusion(struct megasas_instance *instance)

    Initializes the FW

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

.. _`megasas_ioc_init_fusion.description`:

Description
-----------

Issues the IOC Init cmd

.. _`megasas_sync_pd_seq_num`:

megasas_sync_pd_seq_num
=======================

.. c:function:: int megasas_sync_pd_seq_num(struct megasas_instance *instance, bool pend)

    JBOD SEQ MAP

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

    :param pend:
        set to 1, if it is pended jbod map.
    :type pend: bool

.. _`megasas_sync_pd_seq_num.description`:

Description
-----------

Issue Jbod map to the firmware. If it is pended command,
issue command and return. If it is first instance of jbod map
issue and receive command.

.. _`megasas_allocate_raid_maps`:

megasas_allocate_raid_maps
==========================

.. c:function:: int megasas_allocate_raid_maps(struct megasas_instance *instance)

    Allocate memory for RAID maps

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

.. _`megasas_allocate_raid_maps.return`:

Return
------

if success: return 0
failed:  return -ENOMEM

.. _`megasas_configure_queue_sizes`:

megasas_configure_queue_sizes
=============================

.. c:function:: void megasas_configure_queue_sizes(struct megasas_instance *instance)

    Calculate size of request desc queue, reply desc queue, IO request frame queue, set can_queue.

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

.. _`megasas_free_ioc_init_cmd`:

megasas_free_ioc_init_cmd
=========================

.. c:function:: void megasas_free_ioc_init_cmd(struct megasas_instance *instance)

    Free IOC INIT command frame

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

.. _`megasas_init_adapter_fusion`:

megasas_init_adapter_fusion
===========================

.. c:function:: u32 megasas_init_adapter_fusion(struct megasas_instance *instance)

    Initializes the FW

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

.. _`megasas_init_adapter_fusion.description`:

Description
-----------

This is the main function for initializing firmware.

.. _`map_cmd_status`:

map_cmd_status
==============

.. c:function:: void map_cmd_status(struct fusion_context *fusion, struct scsi_cmnd *scmd, u8 status, u8 ext_status, u32 data_length, u8 *sense)

    Maps FW cmd status to OS cmd status

    :param fusion:
        *undescribed*
    :type fusion: struct fusion_context \*

    :param scmd:
        *undescribed*
    :type scmd: struct scsi_cmnd \*

    :param status:
        status of cmd returned by FW
    :type status: u8

    :param ext_status:
        ext status of cmd returned by FW
    :type ext_status: u8

    :param data_length:
        *undescribed*
    :type data_length: u32

    :param sense:
        *undescribed*
    :type sense: u8 \*

.. _`megasas_is_prp_possible`:

megasas_is_prp_possible
=======================

.. c:function:: bool megasas_is_prp_possible(struct megasas_instance *instance, struct scsi_cmnd *scmd, int sge_count)

    Checks if native NVMe PRPs can be built for the IO

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

    :param scmd:
        SCSI command from the mid-layer
    :type scmd: struct scsi_cmnd \*

    :param sge_count:
        scatter gather element count.
    :type sge_count: int

.. _`megasas_is_prp_possible.return`:

Return
------

true: PRPs can be built
false: IEEE SGLs needs to be built

.. _`megasas_make_prp_nvme`:

megasas_make_prp_nvme
=====================

.. c:function:: bool megasas_make_prp_nvme(struct megasas_instance *instance, struct scsi_cmnd *scmd, struct MPI25_IEEE_SGE_CHAIN64 *sgl_ptr, struct megasas_cmd_fusion *cmd, int sge_count)

    Prepare PRPs(Physical Region Page)- SGLs specific to NVMe drives only

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

    :param scmd:
        SCSI command from the mid-layer
    :type scmd: struct scsi_cmnd \*

    :param sgl_ptr:
        SGL to be filled in
    :type sgl_ptr: struct MPI25_IEEE_SGE_CHAIN64 \*

    :param cmd:
        Fusion command frame
    :type cmd: struct megasas_cmd_fusion \*

    :param sge_count:
        scatter gather element count.
    :type sge_count: int

.. _`megasas_make_prp_nvme.return`:

Return
------

true: PRPs are built
false: IEEE SGLs needs to be built

.. _`megasas_make_sgl_fusion`:

megasas_make_sgl_fusion
=======================

.. c:function:: void megasas_make_sgl_fusion(struct megasas_instance *instance, struct scsi_cmnd *scp, struct MPI25_IEEE_SGE_CHAIN64 *sgl_ptr, struct megasas_cmd_fusion *cmd, int sge_count)

    Prepares 32-bit SGL

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

    :param scp:
        SCSI command from the mid-layer
    :type scp: struct scsi_cmnd \*

    :param sgl_ptr:
        SGL to be filled in
    :type sgl_ptr: struct MPI25_IEEE_SGE_CHAIN64 \*

    :param cmd:
        cmd we are working on
        \ ``sge_count``\            sge count
    :type cmd: struct megasas_cmd_fusion \*

    :param sge_count:
        *undescribed*
    :type sge_count: int

.. _`megasas_make_sgl`:

megasas_make_sgl
================

.. c:function:: int megasas_make_sgl(struct megasas_instance *instance, struct scsi_cmnd *scp, struct megasas_cmd_fusion *cmd)

    Build Scatter Gather List(SGLs)

    :param instance:
        Soft instance of controller
    :type instance: struct megasas_instance \*

    :param scp:
        SCSI command pointer
    :type scp: struct scsi_cmnd \*

    :param cmd:
        Fusion command pointer
    :type cmd: struct megasas_cmd_fusion \*

.. _`megasas_make_sgl.description`:

Description
-----------

This function will build sgls based on device type.
For nvme drives, there is different way of building sgls in nvme native
format- PRPs(Physical Region Page).

Returns the number of sg lists actually used, zero if the sg lists
is NULL, or -ENOMEM if the mapping failed

.. _`megasas_set_pd_lba`:

megasas_set_pd_lba
==================

.. c:function:: void megasas_set_pd_lba(struct MPI2_RAID_SCSI_IO_REQUEST *io_request, u8 cdb_len, struct IO_REQUEST_INFO *io_info, struct scsi_cmnd *scp, struct MR_DRV_RAID_MAP_ALL *local_map_ptr, u32 ref_tag)

    Sets PD LBA

    :param io_request:
        *undescribed*
    :type io_request: struct MPI2_RAID_SCSI_IO_REQUEST \*

    :param cdb_len:
        cdb length
    :type cdb_len: u8

    :param io_info:
        *undescribed*
    :type io_info: struct IO_REQUEST_INFO \*

    :param scp:
        *undescribed*
    :type scp: struct scsi_cmnd \*

    :param local_map_ptr:
        *undescribed*
    :type local_map_ptr: struct MR_DRV_RAID_MAP_ALL \*

    :param ref_tag:
        *undescribed*
    :type ref_tag: u32

.. _`megasas_set_pd_lba.description`:

Description
-----------

Used to set the PD LBA in CDB for FP IOs

.. _`megasas_stream_detect`:

megasas_stream_detect
=====================

.. c:function:: void megasas_stream_detect(struct megasas_instance *instance, struct megasas_cmd_fusion *cmd, struct IO_REQUEST_INFO *io_info)

    stream detection on read and and write IOs

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

    :param cmd:
        Command to be prepared
    :type cmd: struct megasas_cmd_fusion \*

    :param io_info:
        IO Request info
    :type io_info: struct IO_REQUEST_INFO \*

.. _`megasas_set_raidflag_cpu_affinity`:

megasas_set_raidflag_cpu_affinity
=================================

.. c:function:: void megasas_set_raidflag_cpu_affinity(union RAID_CONTEXT_UNION *praid_context, struct MR_LD_RAID *raid, bool fp_possible, u8 is_read, u32 scsi_buff_len)

    This function sets the cpu affinity (cpu of the controller) and raid_flags in the raid context based on IO type.

    :param praid_context:
        IO RAID context
    :type praid_context: union RAID_CONTEXT_UNION \*

    :param raid:
        LD raid map
    :type raid: struct MR_LD_RAID \*

    :param fp_possible:
        Is fast path possible?
    :type fp_possible: bool

    :param is_read:
        Is read IO?
    :type is_read: u8

    :param scsi_buff_len:
        *undescribed*
    :type scsi_buff_len: u32

.. _`megasas_build_ldio_fusion`:

megasas_build_ldio_fusion
=========================

.. c:function:: void megasas_build_ldio_fusion(struct megasas_instance *instance, struct scsi_cmnd *scp, struct megasas_cmd_fusion *cmd)

    Prepares IOs to devices

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

    :param scp:
        SCSI command
    :type scp: struct scsi_cmnd \*

    :param cmd:
        Command to be prepared
    :type cmd: struct megasas_cmd_fusion \*

.. _`megasas_build_ldio_fusion.description`:

Description
-----------

Prepares the io_request and chain elements (sg_frame) for IO
The IO can be for PD (Fast Path) or LD

.. _`megasas_build_ld_nonrw_fusion`:

megasas_build_ld_nonrw_fusion
=============================

.. c:function:: void megasas_build_ld_nonrw_fusion(struct megasas_instance *instance, struct scsi_cmnd *scmd, struct megasas_cmd_fusion *cmd)

    prepares non rw ios for virtual disk

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

    :param scmd:
        *undescribed*
    :type scmd: struct scsi_cmnd \*

    :param cmd:
        Command to be prepared
    :type cmd: struct megasas_cmd_fusion \*

.. _`megasas_build_ld_nonrw_fusion.description`:

Description
-----------

Prepares the io_request frame for non-rw io cmds for vd.

.. _`megasas_build_syspd_fusion`:

megasas_build_syspd_fusion
==========================

.. c:function:: void megasas_build_syspd_fusion(struct megasas_instance *instance, struct scsi_cmnd *scmd, struct megasas_cmd_fusion *cmd, bool fp_possible)

    prepares rw/non-rw ios for syspd

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

    :param scmd:
        *undescribed*
    :type scmd: struct scsi_cmnd \*

    :param cmd:
        Command to be prepared
    :type cmd: struct megasas_cmd_fusion \*

    :param fp_possible:
        parameter to detect fast path or firmware path io.
    :type fp_possible: bool

.. _`megasas_build_syspd_fusion.description`:

Description
-----------

Prepares the io_request frame for rw/non-rw io cmds for syspds

.. _`megasas_build_io_fusion`:

megasas_build_io_fusion
=======================

.. c:function:: int megasas_build_io_fusion(struct megasas_instance *instance, struct scsi_cmnd *scp, struct megasas_cmd_fusion *cmd)

    Prepares IOs to devices

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

    :param scp:
        SCSI command
    :type scp: struct scsi_cmnd \*

    :param cmd:
        Command to be prepared
    :type cmd: struct megasas_cmd_fusion \*

.. _`megasas_build_io_fusion.description`:

Description
-----------

Invokes helper functions to prepare request frames
and sets flags appropriate for IO/Non-IO cmd

.. _`megasas_build_and_issue_cmd_fusion`:

megasas_build_and_issue_cmd_fusion
==================================

.. c:function:: u32 megasas_build_and_issue_cmd_fusion(struct megasas_instance *instance, struct scsi_cmnd *scmd)

    Main routine for building and issuing non IOCTL cmd

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

    :param scmd:
        pointer to scsi cmd from OS
    :type scmd: struct scsi_cmnd \*

.. _`megasas_complete_r1_command`:

megasas_complete_r1_command
===========================

.. c:function:: void megasas_complete_r1_command(struct megasas_instance *instance, struct megasas_cmd_fusion *cmd)

    completes R1 FP write commands which has valid peer smid

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

    :param cmd:
        *undescribed*
    :type cmd: struct megasas_cmd_fusion \*

.. _`complete_cmd_fusion`:

complete_cmd_fusion
===================

.. c:function:: int complete_cmd_fusion(struct megasas_instance *instance, u32 MSIxIndex)

    Completes command

    :param instance:
        Adapter soft state
        Completes all commands that is in reply descriptor queue
    :type instance: struct megasas_instance \*

    :param MSIxIndex:
        *undescribed*
    :type MSIxIndex: u32

.. _`megasas_sync_irqs`:

megasas_sync_irqs
=================

.. c:function:: void megasas_sync_irqs(unsigned long instance_addr)

    Synchronizes all IRQs owned by adapter

    :param instance_addr:
        *undescribed*
    :type instance_addr: unsigned long

.. _`megasas_complete_cmd_dpc_fusion`:

megasas_complete_cmd_dpc_fusion
===============================

.. c:function:: void megasas_complete_cmd_dpc_fusion(unsigned long instance_addr)

    Completes command

    :param instance_addr:
        *undescribed*
    :type instance_addr: unsigned long

.. _`megasas_complete_cmd_dpc_fusion.description`:

Description
-----------

Tasklet to complete cmds

.. _`megasas_isr_fusion`:

megasas_isr_fusion
==================

.. c:function:: irqreturn_t megasas_isr_fusion(int irq, void *devp)

    isr entry point

    :param irq:
        *undescribed*
    :type irq: int

    :param devp:
        *undescribed*
    :type devp: void \*

.. _`build_mpt_mfi_pass_thru`:

build_mpt_mfi_pass_thru
=======================

.. c:function:: void build_mpt_mfi_pass_thru(struct megasas_instance *instance, struct megasas_cmd *mfi_cmd)

    builds a cmd fo MFI Pass thru

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

    :param mfi_cmd:
        *undescribed*
    :type mfi_cmd: struct megasas_cmd \*

.. _`build_mpt_mfi_pass_thru.mfi_cmd`:

mfi_cmd
-------

megasas_cmd pointer

.. _`build_mpt_cmd`:

build_mpt_cmd
=============

.. c:function:: union MEGASAS_REQUEST_DESCRIPTOR_UNION *build_mpt_cmd(struct megasas_instance *instance, struct megasas_cmd *cmd)

    Calls helper function to build a cmd MFI Pass thru cmd

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

    :param cmd:
        mfi cmd to build
    :type cmd: struct megasas_cmd \*

.. _`megasas_issue_dcmd_fusion`:

megasas_issue_dcmd_fusion
=========================

.. c:function:: void megasas_issue_dcmd_fusion(struct megasas_instance *instance, struct megasas_cmd *cmd)

    Issues a MFI Pass thru cmd

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

    :param cmd:
        mfi cmd pointer
    :type cmd: struct megasas_cmd \*

.. _`megasas_release_fusion`:

megasas_release_fusion
======================

.. c:function:: void megasas_release_fusion(struct megasas_instance *instance)

    Reverses the FW initialization

    :param instance:
        Adapter soft state
    :type instance: struct megasas_instance \*

.. _`megasas_read_fw_status_reg_fusion`:

megasas_read_fw_status_reg_fusion
=================================

.. c:function:: u32 megasas_read_fw_status_reg_fusion(struct megasas_register_set __iomem *regs)

    returns the current FW status value

    :param regs:
        MFI register set
    :type regs: struct megasas_register_set __iomem \*

.. _`megasas_alloc_host_crash_buffer`:

megasas_alloc_host_crash_buffer
===============================

.. c:function:: void megasas_alloc_host_crash_buffer(struct megasas_instance *instance)

    Host buffers for Crash dump collection from Firmware

    :param instance:
        Controller's soft instance
    :type instance: struct megasas_instance \*

.. _`megasas_alloc_host_crash_buffer.return`:

Return
------

Number of allocated host crash buffers

.. _`megasas_free_host_crash_buffer`:

megasas_free_host_crash_buffer
==============================

.. c:function:: void megasas_free_host_crash_buffer(struct megasas_instance *instance)

    Host buffers for Crash dump collection from Firmware

    :param instance:
        Controller's soft instance
    :type instance: struct megasas_instance \*

.. _`megasas_adp_reset_fusion`:

megasas_adp_reset_fusion
========================

.. c:function:: int megasas_adp_reset_fusion(struct megasas_instance *instance, struct megasas_register_set __iomem *regs)

    For controller reset

    :param instance:
        *undescribed*
    :type instance: struct megasas_instance \*

    :param regs:
        MFI register set
    :type regs: struct megasas_register_set __iomem \*

.. _`megasas_check_reset_fusion`:

megasas_check_reset_fusion
==========================

.. c:function:: int megasas_check_reset_fusion(struct megasas_instance *instance, struct megasas_register_set __iomem *regs)

    For controller reset check

    :param instance:
        *undescribed*
    :type instance: struct megasas_instance \*

    :param regs:
        MFI register set
    :type regs: struct megasas_register_set __iomem \*

.. _`megasas_tm_response_code`:

megasas_tm_response_code
========================

.. c:function:: void megasas_tm_response_code(struct megasas_instance *instance, struct MPI2_SCSI_TASK_MANAGE_REPLY *mpi_reply)

    translation of device response code

    :param instance:
        *undescribed*
    :type instance: struct megasas_instance \*

    :param mpi_reply:
        MPI reply returned by firmware
    :type mpi_reply: struct MPI2_SCSI_TASK_MANAGE_REPLY \*

.. _`megasas_tm_response_code.description`:

Description
-----------

Return nothing.

.. _`megasas_issue_tm`:

megasas_issue_tm
================

.. c:function:: int megasas_issue_tm(struct megasas_instance *instance, u16 device_handle, uint channel, uint id, u16 smid_task, u8 type, struct MR_PRIV_DEVICE *mr_device_priv_data)

    main routine for sending tm requests

    :param instance:
        per adapter struct
    :type instance: struct megasas_instance \*

    :param device_handle:
        device handle
    :type device_handle: u16

    :param channel:
        the channel assigned by the OS
    :type channel: uint

    :param id:
        the id assigned by the OS
    :type id: uint

    :param smid_task:
        smid assigned to the task
    :type smid_task: u16

    :param type:
        MPI2_SCSITASKMGMT_TASKTYPE__XXX (defined in megaraid_sas_fusion.c)
    :type type: u8

    :param mr_device_priv_data:
        *undescribed*
    :type mr_device_priv_data: struct MR_PRIV_DEVICE \*

.. _`megasas_issue_tm.context`:

Context
-------

user

.. _`megasas_issue_tm.description`:

Description
-----------

MegaRaid use MPT interface for Task Magement request.
A generic API for sending task management requests to firmware.

Return SUCCESS or FAILED.

.. This file was automatic generated / don't edit.

