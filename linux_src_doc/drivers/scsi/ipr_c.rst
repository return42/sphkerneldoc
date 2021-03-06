.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/ipr.c

.. _`ipr_trc_hook`:

ipr_trc_hook
============

.. c:function:: void ipr_trc_hook(struct ipr_cmnd *ipr_cmd, u8 type, u32 add_data)

    Add a trace entry to the driver trace

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

    :param type:
        trace type
    :type type: u8

    :param add_data:
        additional data
    :type add_data: u32

.. _`ipr_trc_hook.return-value`:

Return value
------------

none

.. _`ipr_lock_and_done`:

ipr_lock_and_done
=================

.. c:function:: void ipr_lock_and_done(struct ipr_cmnd *ipr_cmd)

    Acquire lock and complete command

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_lock_and_done.return-value`:

Return value
------------

none

.. _`ipr_reinit_ipr_cmnd`:

ipr_reinit_ipr_cmnd
===================

.. c:function:: void ipr_reinit_ipr_cmnd(struct ipr_cmnd *ipr_cmd)

    Re-initialize an IPR Cmnd block for reuse

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reinit_ipr_cmnd.return-value`:

Return value
------------

none

.. _`ipr_init_ipr_cmnd`:

ipr_init_ipr_cmnd
=================

.. c:function:: void ipr_init_ipr_cmnd(struct ipr_cmnd *ipr_cmd, void (*fast_done)(struct ipr_cmnd *))

    Initialize an IPR Cmnd block

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

    :param void (\*fast_done)(struct ipr_cmnd \*):
        *undescribed*

.. _`ipr_init_ipr_cmnd.return-value`:

Return value
------------

none

.. _`__ipr_get_free_ipr_cmnd`:

\__ipr_get_free_ipr_cmnd
========================

.. c:function:: struct ipr_cmnd *__ipr_get_free_ipr_cmnd(struct ipr_hrr_queue *hrrq)

    Get a free IPR Cmnd block

    :param hrrq:
        *undescribed*
    :type hrrq: struct ipr_hrr_queue \*

.. _`__ipr_get_free_ipr_cmnd.return-value`:

Return value
------------

pointer to ipr command struct

.. _`ipr_get_free_ipr_cmnd`:

ipr_get_free_ipr_cmnd
=====================

.. c:function:: struct ipr_cmnd *ipr_get_free_ipr_cmnd(struct ipr_ioa_cfg *ioa_cfg)

    Get a free IPR Cmnd block and initialize it

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

.. _`ipr_get_free_ipr_cmnd.return-value`:

Return value
------------

pointer to ipr command struct

.. _`ipr_mask_and_clear_interrupts`:

ipr_mask_and_clear_interrupts
=============================

.. c:function:: void ipr_mask_and_clear_interrupts(struct ipr_ioa_cfg *ioa_cfg, u32 clr_ints)

    Mask all and clear specified interrupts

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param clr_ints:
        interrupts to clear
    :type clr_ints: u32

.. _`ipr_mask_and_clear_interrupts.description`:

Description
-----------

This function masks all interrupts on the adapter, then clears the
interrupts specified in the mask

.. _`ipr_mask_and_clear_interrupts.return-value`:

Return value
------------

none

.. _`ipr_save_pcix_cmd_reg`:

ipr_save_pcix_cmd_reg
=====================

.. c:function:: int ipr_save_pcix_cmd_reg(struct ipr_ioa_cfg *ioa_cfg)

    Save PCI-X command register

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

.. _`ipr_save_pcix_cmd_reg.return-value`:

Return value
------------

0 on success / -EIO on failure

.. _`ipr_set_pcix_cmd_reg`:

ipr_set_pcix_cmd_reg
====================

.. c:function:: int ipr_set_pcix_cmd_reg(struct ipr_ioa_cfg *ioa_cfg)

    Setup PCI-X command register

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

.. _`ipr_set_pcix_cmd_reg.return-value`:

Return value
------------

0 on success / -EIO on failure

.. _`__ipr_sata_eh_done`:

\__ipr_sata_eh_done
===================

.. c:function:: void __ipr_sata_eh_done(struct ipr_cmnd *ipr_cmd)

    done function for aborted SATA commands

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`__ipr_sata_eh_done.description`:

Description
-----------

This function is invoked for ops generated to SATA
devices which are being aborted.

.. _`__ipr_sata_eh_done.return-value`:

Return value
------------

none

.. _`ipr_sata_eh_done`:

ipr_sata_eh_done
================

.. c:function:: void ipr_sata_eh_done(struct ipr_cmnd *ipr_cmd)

    done function for aborted SATA commands

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_sata_eh_done.description`:

Description
-----------

This function is invoked for ops generated to SATA
devices which are being aborted.

.. _`ipr_sata_eh_done.return-value`:

Return value
------------

none

.. _`__ipr_scsi_eh_done`:

\__ipr_scsi_eh_done
===================

.. c:function:: void __ipr_scsi_eh_done(struct ipr_cmnd *ipr_cmd)

    mid-layer done function for aborted ops

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`__ipr_scsi_eh_done.description`:

Description
-----------

This function is invoked by the interrupt handler for
ops generated by the SCSI mid-layer which are being aborted.

.. _`__ipr_scsi_eh_done.return-value`:

Return value
------------

none

.. _`ipr_scsi_eh_done`:

ipr_scsi_eh_done
================

.. c:function:: void ipr_scsi_eh_done(struct ipr_cmnd *ipr_cmd)

    mid-layer done function for aborted ops

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_scsi_eh_done.description`:

Description
-----------

This function is invoked by the interrupt handler for
ops generated by the SCSI mid-layer which are being aborted.

.. _`ipr_scsi_eh_done.return-value`:

Return value
------------

none

.. _`ipr_fail_all_ops`:

ipr_fail_all_ops
================

.. c:function:: void ipr_fail_all_ops(struct ipr_ioa_cfg *ioa_cfg)

    Fails all outstanding ops.

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

.. _`ipr_fail_all_ops.description`:

Description
-----------

This function fails all outstanding ops.

.. _`ipr_fail_all_ops.return-value`:

Return value
------------

none

.. _`ipr_send_command`:

ipr_send_command
================

.. c:function:: void ipr_send_command(struct ipr_cmnd *ipr_cmd)

    Send driver initiated requests.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_send_command.description`:

Description
-----------

This function sends a command to the adapter using the correct write call.
In the case of sis64, calculate the ioarcb size required. Then or in the
appropriate bits.

.. _`ipr_send_command.return-value`:

Return value
------------

none

.. _`ipr_do_req`:

ipr_do_req
==========

.. c:function:: void ipr_do_req(struct ipr_cmnd *ipr_cmd, void (*done)(struct ipr_cmnd *), void (*timeout_func)(struct timer_list *), u32 timeout)

    Send driver initiated requests.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

    :param void (\*done)(struct ipr_cmnd \*):
        done function

    :param void (\*timeout_func)(struct timer_list \*):
        timeout function

    :param timeout:
        timeout value
    :type timeout: u32

.. _`ipr_do_req.description`:

Description
-----------

This function sends the specified command to the adapter with the
timeout given. The done function is invoked on command completion.

.. _`ipr_do_req.return-value`:

Return value
------------

none

.. _`ipr_internal_cmd_done`:

ipr_internal_cmd_done
=====================

.. c:function:: void ipr_internal_cmd_done(struct ipr_cmnd *ipr_cmd)

    Op done function for an internally generated op.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_internal_cmd_done.description`:

Description
-----------

This function is the op done function for an internally generated,
blocking op. It simply wakes the sleeping thread.

.. _`ipr_internal_cmd_done.return-value`:

Return value
------------

none

.. _`ipr_init_ioadl`:

ipr_init_ioadl
==============

.. c:function:: void ipr_init_ioadl(struct ipr_cmnd *ipr_cmd, dma_addr_t dma_addr, u32 len, int flags)

    initialize the ioadl for the correct SIS type

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

    :param dma_addr:
        dma address
    :type dma_addr: dma_addr_t

    :param len:
        transfer length
    :type len: u32

    :param flags:
        ioadl flag value
    :type flags: int

.. _`ipr_init_ioadl.description`:

Description
-----------

This function initializes an ioadl in the case where there is only a single
descriptor.

.. _`ipr_init_ioadl.return-value`:

Return value
------------

nothing

.. _`ipr_send_blocking_cmd`:

ipr_send_blocking_cmd
=====================

.. c:function:: void ipr_send_blocking_cmd(struct ipr_cmnd *ipr_cmd, void (*timeout_func)(struct timer_list *), u32 timeout)

    Send command and sleep on its completion.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

    :param void (\*timeout_func)(struct timer_list \*):
        function to invoke if command times out

    :param timeout:
        timeout
    :type timeout: u32

.. _`ipr_send_blocking_cmd.return-value`:

Return value
------------

none

.. _`ipr_send_hcam`:

ipr_send_hcam
=============

.. c:function:: void ipr_send_hcam(struct ipr_ioa_cfg *ioa_cfg, u8 type, struct ipr_hostrcb *hostrcb)

    Send an HCAM to the adapter.

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param type:
        HCAM type
    :type type: u8

    :param hostrcb:
        hostrcb struct
    :type hostrcb: struct ipr_hostrcb \*

.. _`ipr_send_hcam.description`:

Description
-----------

This function will send a Host Controlled Async command to the adapter.
If HCAMs are currently not allowed to be issued to the adapter, it will
place the hostrcb on the free queue.

.. _`ipr_send_hcam.return-value`:

Return value
------------

none

.. _`ipr_update_ata_class`:

ipr_update_ata_class
====================

.. c:function:: void ipr_update_ata_class(struct ipr_resource_entry *res, unsigned int proto)

    Update the ata class in the resource entry

    :param res:
        resource entry struct
    :type res: struct ipr_resource_entry \*

    :param proto:
        cfgte device bus protocol value
    :type proto: unsigned int

.. _`ipr_update_ata_class.return-value`:

Return value
------------

none

.. _`ipr_init_res_entry`:

ipr_init_res_entry
==================

.. c:function:: void ipr_init_res_entry(struct ipr_resource_entry *res, struct ipr_config_table_entry_wrapper *cfgtew)

    Initialize a resource entry struct.

    :param res:
        resource entry struct
    :type res: struct ipr_resource_entry \*

    :param cfgtew:
        config table entry wrapper struct
    :type cfgtew: struct ipr_config_table_entry_wrapper \*

.. _`ipr_init_res_entry.return-value`:

Return value
------------

none

.. _`ipr_is_same_device`:

ipr_is_same_device
==================

.. c:function:: int ipr_is_same_device(struct ipr_resource_entry *res, struct ipr_config_table_entry_wrapper *cfgtew)

    Determine if two devices are the same.

    :param res:
        resource entry struct
    :type res: struct ipr_resource_entry \*

    :param cfgtew:
        config table entry wrapper struct
    :type cfgtew: struct ipr_config_table_entry_wrapper \*

.. _`ipr_is_same_device.return-value`:

Return value
------------

1 if the devices are the same / 0 otherwise

.. _`__ipr_format_res_path`:

\__ipr_format_res_path
======================

.. c:function:: char *__ipr_format_res_path(u8 *res_path, char *buffer, int len)

    Format the resource path for printing.

    :param res_path:
        resource path
    :type res_path: u8 \*

    :param buffer:
        *undescribed*
    :type buffer: char \*

    :param len:
        length of buffer provided
    :type len: int

.. _`__ipr_format_res_path.return-value`:

Return value
------------

pointer to buffer

.. _`ipr_format_res_path`:

ipr_format_res_path
===================

.. c:function:: char *ipr_format_res_path(struct ipr_ioa_cfg *ioa_cfg, u8 *res_path, char *buffer, int len)

    Format the resource path for printing.

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param res_path:
        resource path
    :type res_path: u8 \*

    :param buffer:
        *undescribed*
    :type buffer: char \*

    :param len:
        length of buffer provided
    :type len: int

.. _`ipr_format_res_path.return-value`:

Return value
------------

pointer to buffer

.. _`ipr_update_res_entry`:

ipr_update_res_entry
====================

.. c:function:: void ipr_update_res_entry(struct ipr_resource_entry *res, struct ipr_config_table_entry_wrapper *cfgtew)

    Update the resource entry.

    :param res:
        resource entry struct
    :type res: struct ipr_resource_entry \*

    :param cfgtew:
        config table entry wrapper struct
    :type cfgtew: struct ipr_config_table_entry_wrapper \*

.. _`ipr_update_res_entry.return-value`:

Return value
------------

none

.. _`ipr_clear_res_target`:

ipr_clear_res_target
====================

.. c:function:: void ipr_clear_res_target(struct ipr_resource_entry *res)

    Clear the bit in the bit map representing the target for the resource.

    :param res:
        resource entry struct
    :type res: struct ipr_resource_entry \*

.. _`ipr_clear_res_target.return-value`:

Return value
------------

none

.. _`ipr_handle_config_change`:

ipr_handle_config_change
========================

.. c:function:: void ipr_handle_config_change(struct ipr_ioa_cfg *ioa_cfg, struct ipr_hostrcb *hostrcb)

    Handle a config change from the adapter

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param hostrcb:
        hostrcb
    :type hostrcb: struct ipr_hostrcb \*

.. _`ipr_handle_config_change.return-value`:

Return value
------------

none

.. _`ipr_process_ccn`:

ipr_process_ccn
===============

.. c:function:: void ipr_process_ccn(struct ipr_cmnd *ipr_cmd)

    Op done function for a CCN.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_process_ccn.description`:

Description
-----------

This function is the op done function for a configuration
change notification host controlled async from the adapter.

.. _`ipr_process_ccn.return-value`:

Return value
------------

none

.. _`strip_and_pad_whitespace`:

strip_and_pad_whitespace
========================

.. c:function:: int strip_and_pad_whitespace(int i, char *buf)

    Strip and pad trailing whitespace.

    :param i:
        index into buffer
    :type i: int

    :param buf:
        string to modify
    :type buf: char \*

.. _`strip_and_pad_whitespace.description`:

Description
-----------

This function will strip all trailing whitespace, pad the end
of the string with a single space, and NULL terminate the string.

.. _`strip_and_pad_whitespace.return-value`:

Return value
------------

new length of string

.. _`ipr_log_vpd_compact`:

ipr_log_vpd_compact
===================

.. c:function:: void ipr_log_vpd_compact(char *prefix, struct ipr_hostrcb *hostrcb, struct ipr_vpd *vpd)

    Log the passed extended VPD compactly.

    :param prefix:
        string to print at start of printk
    :type prefix: char \*

    :param hostrcb:
        hostrcb pointer
    :type hostrcb: struct ipr_hostrcb \*

    :param vpd:
        vendor/product id/sn struct
    :type vpd: struct ipr_vpd \*

.. _`ipr_log_vpd_compact.return-value`:

Return value
------------

none

.. _`ipr_log_vpd`:

ipr_log_vpd
===========

.. c:function:: void ipr_log_vpd(struct ipr_vpd *vpd)

    Log the passed VPD to the error log.

    :param vpd:
        vendor/product id/sn struct
    :type vpd: struct ipr_vpd \*

.. _`ipr_log_vpd.return-value`:

Return value
------------

none

.. _`ipr_log_ext_vpd_compact`:

ipr_log_ext_vpd_compact
=======================

.. c:function:: void ipr_log_ext_vpd_compact(char *prefix, struct ipr_hostrcb *hostrcb, struct ipr_ext_vpd *vpd)

    Log the passed extended VPD compactly.

    :param prefix:
        string to print at start of printk
    :type prefix: char \*

    :param hostrcb:
        hostrcb pointer
    :type hostrcb: struct ipr_hostrcb \*

    :param vpd:
        vendor/product id/sn/wwn struct
    :type vpd: struct ipr_ext_vpd \*

.. _`ipr_log_ext_vpd_compact.return-value`:

Return value
------------

none

.. _`ipr_log_ext_vpd`:

ipr_log_ext_vpd
===============

.. c:function:: void ipr_log_ext_vpd(struct ipr_ext_vpd *vpd)

    Log the passed extended VPD to the error log.

    :param vpd:
        vendor/product id/sn/wwn struct
    :type vpd: struct ipr_ext_vpd \*

.. _`ipr_log_ext_vpd.return-value`:

Return value
------------

none

.. _`ipr_log_enhanced_cache_error`:

ipr_log_enhanced_cache_error
============================

.. c:function:: void ipr_log_enhanced_cache_error(struct ipr_ioa_cfg *ioa_cfg, struct ipr_hostrcb *hostrcb)

    Log a cache error.

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param hostrcb:
        hostrcb struct
    :type hostrcb: struct ipr_hostrcb \*

.. _`ipr_log_enhanced_cache_error.return-value`:

Return value
------------

none

.. _`ipr_log_cache_error`:

ipr_log_cache_error
===================

.. c:function:: void ipr_log_cache_error(struct ipr_ioa_cfg *ioa_cfg, struct ipr_hostrcb *hostrcb)

    Log a cache error.

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param hostrcb:
        hostrcb struct
    :type hostrcb: struct ipr_hostrcb \*

.. _`ipr_log_cache_error.return-value`:

Return value
------------

none

.. _`ipr_log_enhanced_config_error`:

ipr_log_enhanced_config_error
=============================

.. c:function:: void ipr_log_enhanced_config_error(struct ipr_ioa_cfg *ioa_cfg, struct ipr_hostrcb *hostrcb)

    Log a configuration error.

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param hostrcb:
        hostrcb struct
    :type hostrcb: struct ipr_hostrcb \*

.. _`ipr_log_enhanced_config_error.return-value`:

Return value
------------

none

.. _`ipr_log_sis64_config_error`:

ipr_log_sis64_config_error
==========================

.. c:function:: void ipr_log_sis64_config_error(struct ipr_ioa_cfg *ioa_cfg, struct ipr_hostrcb *hostrcb)

    Log a device error.

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param hostrcb:
        hostrcb struct
    :type hostrcb: struct ipr_hostrcb \*

.. _`ipr_log_sis64_config_error.return-value`:

Return value
------------

none

.. _`ipr_log_config_error`:

ipr_log_config_error
====================

.. c:function:: void ipr_log_config_error(struct ipr_ioa_cfg *ioa_cfg, struct ipr_hostrcb *hostrcb)

    Log a configuration error.

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param hostrcb:
        hostrcb struct
    :type hostrcb: struct ipr_hostrcb \*

.. _`ipr_log_config_error.return-value`:

Return value
------------

none

.. _`ipr_log_enhanced_array_error`:

ipr_log_enhanced_array_error
============================

.. c:function:: void ipr_log_enhanced_array_error(struct ipr_ioa_cfg *ioa_cfg, struct ipr_hostrcb *hostrcb)

    Log an array configuration error.

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param hostrcb:
        hostrcb struct
    :type hostrcb: struct ipr_hostrcb \*

.. _`ipr_log_enhanced_array_error.return-value`:

Return value
------------

none

.. _`ipr_log_array_error`:

ipr_log_array_error
===================

.. c:function:: void ipr_log_array_error(struct ipr_ioa_cfg *ioa_cfg, struct ipr_hostrcb *hostrcb)

    Log an array configuration error.

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param hostrcb:
        hostrcb struct
    :type hostrcb: struct ipr_hostrcb \*

.. _`ipr_log_array_error.return-value`:

Return value
------------

none

.. _`ipr_log_hex_data`:

ipr_log_hex_data
================

.. c:function:: void ipr_log_hex_data(struct ipr_ioa_cfg *ioa_cfg, __be32 *data, int len)

    Log additional hex IOA error data.

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param data:
        IOA error data
    :type data: __be32 \*

    :param len:
        data length
    :type len: int

.. _`ipr_log_hex_data.return-value`:

Return value
------------

none

.. _`ipr_log_enhanced_dual_ioa_error`:

ipr_log_enhanced_dual_ioa_error
===============================

.. c:function:: void ipr_log_enhanced_dual_ioa_error(struct ipr_ioa_cfg *ioa_cfg, struct ipr_hostrcb *hostrcb)

    Log an enhanced dual adapter error.

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param hostrcb:
        hostrcb struct
    :type hostrcb: struct ipr_hostrcb \*

.. _`ipr_log_enhanced_dual_ioa_error.return-value`:

Return value
------------

none

.. _`ipr_log_dual_ioa_error`:

ipr_log_dual_ioa_error
======================

.. c:function:: void ipr_log_dual_ioa_error(struct ipr_ioa_cfg *ioa_cfg, struct ipr_hostrcb *hostrcb)

    Log a dual adapter error.

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param hostrcb:
        hostrcb struct
    :type hostrcb: struct ipr_hostrcb \*

.. _`ipr_log_dual_ioa_error.return-value`:

Return value
------------

none

.. _`ipr_log_fabric_path`:

ipr_log_fabric_path
===================

.. c:function:: void ipr_log_fabric_path(struct ipr_hostrcb *hostrcb, struct ipr_hostrcb_fabric_desc *fabric)

    Log a fabric path error

    :param hostrcb:
        hostrcb struct
    :type hostrcb: struct ipr_hostrcb \*

    :param fabric:
        fabric descriptor
    :type fabric: struct ipr_hostrcb_fabric_desc \*

.. _`ipr_log_fabric_path.return-value`:

Return value
------------

none

.. _`ipr_log64_fabric_path`:

ipr_log64_fabric_path
=====================

.. c:function:: void ipr_log64_fabric_path(struct ipr_hostrcb *hostrcb, struct ipr_hostrcb64_fabric_desc *fabric)

    Log a fabric path error

    :param hostrcb:
        hostrcb struct
    :type hostrcb: struct ipr_hostrcb \*

    :param fabric:
        fabric descriptor
    :type fabric: struct ipr_hostrcb64_fabric_desc \*

.. _`ipr_log64_fabric_path.return-value`:

Return value
------------

none

.. _`ipr_log_path_elem`:

ipr_log_path_elem
=================

.. c:function:: void ipr_log_path_elem(struct ipr_hostrcb *hostrcb, struct ipr_hostrcb_config_element *cfg)

    Log a fabric path element.

    :param hostrcb:
        hostrcb struct
    :type hostrcb: struct ipr_hostrcb \*

    :param cfg:
        fabric path element struct
    :type cfg: struct ipr_hostrcb_config_element \*

.. _`ipr_log_path_elem.return-value`:

Return value
------------

none

.. _`ipr_log64_path_elem`:

ipr_log64_path_elem
===================

.. c:function:: void ipr_log64_path_elem(struct ipr_hostrcb *hostrcb, struct ipr_hostrcb64_config_element *cfg)

    Log a fabric path element.

    :param hostrcb:
        hostrcb struct
    :type hostrcb: struct ipr_hostrcb \*

    :param cfg:
        fabric path element struct
    :type cfg: struct ipr_hostrcb64_config_element \*

.. _`ipr_log64_path_elem.return-value`:

Return value
------------

none

.. _`ipr_log_fabric_error`:

ipr_log_fabric_error
====================

.. c:function:: void ipr_log_fabric_error(struct ipr_ioa_cfg *ioa_cfg, struct ipr_hostrcb *hostrcb)

    Log a fabric error.

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param hostrcb:
        hostrcb struct
    :type hostrcb: struct ipr_hostrcb \*

.. _`ipr_log_fabric_error.return-value`:

Return value
------------

none

.. _`ipr_log_sis64_array_error`:

ipr_log_sis64_array_error
=========================

.. c:function:: void ipr_log_sis64_array_error(struct ipr_ioa_cfg *ioa_cfg, struct ipr_hostrcb *hostrcb)

    Log a sis64 array error.

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param hostrcb:
        hostrcb struct
    :type hostrcb: struct ipr_hostrcb \*

.. _`ipr_log_sis64_array_error.return-value`:

Return value
------------

none

.. _`ipr_log_sis64_fabric_error`:

ipr_log_sis64_fabric_error
==========================

.. c:function:: void ipr_log_sis64_fabric_error(struct ipr_ioa_cfg *ioa_cfg, struct ipr_hostrcb *hostrcb)

    Log a sis64 fabric error.

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param hostrcb:
        hostrcb struct
    :type hostrcb: struct ipr_hostrcb \*

.. _`ipr_log_sis64_fabric_error.return-value`:

Return value
------------

none

.. _`ipr_log_sis64_service_required_error`:

ipr_log_sis64_service_required_error
====================================

.. c:function:: void ipr_log_sis64_service_required_error(struct ipr_ioa_cfg *ioa_cfg, struct ipr_hostrcb *hostrcb)

    Log a sis64 service required error.

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param hostrcb:
        hostrcb struct
    :type hostrcb: struct ipr_hostrcb \*

.. _`ipr_log_sis64_service_required_error.return-value`:

Return value
------------

none

.. _`ipr_log_generic_error`:

ipr_log_generic_error
=====================

.. c:function:: void ipr_log_generic_error(struct ipr_ioa_cfg *ioa_cfg, struct ipr_hostrcb *hostrcb)

    Log an adapter error.

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param hostrcb:
        hostrcb struct
    :type hostrcb: struct ipr_hostrcb \*

.. _`ipr_log_generic_error.return-value`:

Return value
------------

none

.. _`ipr_log_sis64_device_error`:

ipr_log_sis64_device_error
==========================

.. c:function:: void ipr_log_sis64_device_error(struct ipr_ioa_cfg *ioa_cfg, struct ipr_hostrcb *hostrcb)

    Log a cache error.

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param hostrcb:
        hostrcb struct
    :type hostrcb: struct ipr_hostrcb \*

.. _`ipr_log_sis64_device_error.return-value`:

Return value
------------

none

.. _`ipr_get_error`:

ipr_get_error
=============

.. c:function:: u32 ipr_get_error(u32 ioasc)

    Find the specfied IOASC in the ipr_error_table.

    :param ioasc:
        IOASC
    :type ioasc: u32

.. _`ipr_get_error.description`:

Description
-----------

This function will return the index of into the ipr_error_table
for the specified IOASC. If the IOASC is not in the table,
0 will be returned, which points to the entry used for unknown errors.

.. _`ipr_get_error.return-value`:

Return value
------------

index into the ipr_error_table

.. _`ipr_handle_log_data`:

ipr_handle_log_data
===================

.. c:function:: void ipr_handle_log_data(struct ipr_ioa_cfg *ioa_cfg, struct ipr_hostrcb *hostrcb)

    Log an adapter error.

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param hostrcb:
        hostrcb struct
    :type hostrcb: struct ipr_hostrcb \*

.. _`ipr_handle_log_data.description`:

Description
-----------

This function logs an adapter error to the system.

.. _`ipr_handle_log_data.return-value`:

Return value
------------

none

.. _`ipr_process_error`:

ipr_process_error
=================

.. c:function:: void ipr_process_error(struct ipr_cmnd *ipr_cmd)

    Op done function for an adapter error log.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_process_error.description`:

Description
-----------

This function is the op done function for an error log host
controlled async from the adapter. It will log the error and
send the HCAM back to the adapter.

.. _`ipr_process_error.return-value`:

Return value
------------

none

.. _`ipr_timeout`:

ipr_timeout
===========

.. c:function:: void ipr_timeout(struct timer_list *t)

    An internally generated op has timed out.

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`ipr_timeout.description`:

Description
-----------

This function blocks host requests and initiates an
adapter reset.

.. _`ipr_timeout.return-value`:

Return value
------------

none

.. _`ipr_oper_timeout`:

ipr_oper_timeout
================

.. c:function:: void ipr_oper_timeout(struct timer_list *t)

    Adapter timed out transitioning to operational

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`ipr_oper_timeout.description`:

Description
-----------

This function blocks host requests and initiates an
adapter reset.

.. _`ipr_oper_timeout.return-value`:

Return value
------------

none

.. _`ipr_find_ses_entry`:

ipr_find_ses_entry
==================

.. c:function:: const struct ipr_ses_table_entry *ipr_find_ses_entry(struct ipr_resource_entry *res)

    Find matching SES in SES table

    :param res:
        resource entry struct of SES
    :type res: struct ipr_resource_entry \*

.. _`ipr_find_ses_entry.return-value`:

Return value
------------

pointer to SES table entry / NULL on failure

.. _`ipr_get_max_scsi_speed`:

ipr_get_max_scsi_speed
======================

.. c:function:: u32 ipr_get_max_scsi_speed(struct ipr_ioa_cfg *ioa_cfg, u8 bus, u8 bus_width)

    Determine max SCSI speed for a given bus

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param bus:
        SCSI bus
    :type bus: u8

    :param bus_width:
        bus width
    :type bus_width: u8

.. _`ipr_get_max_scsi_speed.return-value`:

Return value
------------

SCSI bus speed in units of 100KHz, 1600 is 160 MHz
For a 2-byte wide SCSI bus, the maximum transfer speed is
twice the maximum transfer rate (e.g. for a wide enabled bus,
max 160MHz = max 320MB/sec).

.. _`ipr_wait_iodbg_ack`:

ipr_wait_iodbg_ack
==================

.. c:function:: int ipr_wait_iodbg_ack(struct ipr_ioa_cfg *ioa_cfg, int max_delay)

    Wait for an IODEBUG ACK from the IOA

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param max_delay:
        max delay in micro-seconds to wait
    :type max_delay: int

.. _`ipr_wait_iodbg_ack.description`:

Description
-----------

Waits for an IODEBUG ACK from the IOA, doing busy looping.

.. _`ipr_wait_iodbg_ack.return-value`:

Return value
------------

0 on success / other on failure

.. _`ipr_get_sis64_dump_data_section`:

ipr_get_sis64_dump_data_section
===============================

.. c:function:: int ipr_get_sis64_dump_data_section(struct ipr_ioa_cfg *ioa_cfg, u32 start_addr, __be32 *dest, u32 length_in_words)

    Dump IOA memory

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param start_addr:
        adapter address to dump
    :type start_addr: u32

    :param dest:
        destination kernel buffer
    :type dest: __be32 \*

    :param length_in_words:
        length to dump in 4 byte words
    :type length_in_words: u32

.. _`ipr_get_sis64_dump_data_section.return-value`:

Return value
------------

0 on success

.. _`ipr_get_ldump_data_section`:

ipr_get_ldump_data_section
==========================

.. c:function:: int ipr_get_ldump_data_section(struct ipr_ioa_cfg *ioa_cfg, u32 start_addr, __be32 *dest, u32 length_in_words)

    Dump IOA memory

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param start_addr:
        adapter address to dump
    :type start_addr: u32

    :param dest:
        destination kernel buffer
    :type dest: __be32 \*

    :param length_in_words:
        length to dump in 4 byte words
    :type length_in_words: u32

.. _`ipr_get_ldump_data_section.return-value`:

Return value
------------

0 on success / -EIO on failure

.. _`ipr_sdt_copy`:

ipr_sdt_copy
============

.. c:function:: int ipr_sdt_copy(struct ipr_ioa_cfg *ioa_cfg, unsigned long pci_address, u32 length)

    Copy Smart Dump Table to kernel buffer

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param pci_address:
        adapter address
    :type pci_address: unsigned long

    :param length:
        length of data to copy
    :type length: u32

.. _`ipr_sdt_copy.description`:

Description
-----------

Copy data from PCI adapter to kernel buffer.

.. _`ipr_sdt_copy.note`:

Note
----

length MUST be a 4 byte multiple

.. _`ipr_sdt_copy.return-value`:

Return value
------------

0 on success / other on failure

.. _`ipr_init_dump_entry_hdr`:

ipr_init_dump_entry_hdr
=======================

.. c:function:: void ipr_init_dump_entry_hdr(struct ipr_dump_entry_header *hdr)

    Initialize a dump entry header.

    :param hdr:
        dump entry header struct
    :type hdr: struct ipr_dump_entry_header \*

.. _`ipr_init_dump_entry_hdr.return-value`:

Return value
------------

nothing

.. _`ipr_dump_ioa_type_data`:

ipr_dump_ioa_type_data
======================

.. c:function:: void ipr_dump_ioa_type_data(struct ipr_ioa_cfg *ioa_cfg, struct ipr_driver_dump *driver_dump)

    Fill in the adapter type in the dump.

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param driver_dump:
        driver dump struct
    :type driver_dump: struct ipr_driver_dump \*

.. _`ipr_dump_ioa_type_data.return-value`:

Return value
------------

nothing

.. _`ipr_dump_version_data`:

ipr_dump_version_data
=====================

.. c:function:: void ipr_dump_version_data(struct ipr_ioa_cfg *ioa_cfg, struct ipr_driver_dump *driver_dump)

    Fill in the driver version in the dump.

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param driver_dump:
        driver dump struct
    :type driver_dump: struct ipr_driver_dump \*

.. _`ipr_dump_version_data.return-value`:

Return value
------------

nothing

.. _`ipr_dump_trace_data`:

ipr_dump_trace_data
===================

.. c:function:: void ipr_dump_trace_data(struct ipr_ioa_cfg *ioa_cfg, struct ipr_driver_dump *driver_dump)

    Fill in the IOA trace in the dump.

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param driver_dump:
        driver dump struct
    :type driver_dump: struct ipr_driver_dump \*

.. _`ipr_dump_trace_data.return-value`:

Return value
------------

nothing

.. _`ipr_dump_location_data`:

ipr_dump_location_data
======================

.. c:function:: void ipr_dump_location_data(struct ipr_ioa_cfg *ioa_cfg, struct ipr_driver_dump *driver_dump)

    Fill in the IOA location in the dump.

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param driver_dump:
        driver dump struct
    :type driver_dump: struct ipr_driver_dump \*

.. _`ipr_dump_location_data.return-value`:

Return value
------------

nothing

.. _`ipr_get_ioa_dump`:

ipr_get_ioa_dump
================

.. c:function:: void ipr_get_ioa_dump(struct ipr_ioa_cfg *ioa_cfg, struct ipr_dump *dump)

    Perform a dump of the driver and adapter.

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param dump:
        dump struct
    :type dump: struct ipr_dump \*

.. _`ipr_get_ioa_dump.return-value`:

Return value
------------

nothing

.. _`ipr_release_dump`:

ipr_release_dump
================

.. c:function:: void ipr_release_dump(struct kref *kref)

    Free adapter dump memory

    :param kref:
        kref struct
    :type kref: struct kref \*

.. _`ipr_release_dump.return-value`:

Return value
------------

nothing

.. _`ipr_worker_thread`:

ipr_worker_thread
=================

.. c:function:: void ipr_worker_thread(struct work_struct *work)

    Worker thread

    :param work:
        ioa config struct
    :type work: struct work_struct \*

.. _`ipr_worker_thread.description`:

Description
-----------

Called at task level from a work thread. This function takes care
of adding and removing device from the mid-layer as configuration
changes are detected by the adapter.

.. _`ipr_worker_thread.return-value`:

Return value
------------

nothing

.. _`ipr_read_trace`:

ipr_read_trace
==============

.. c:function:: ssize_t ipr_read_trace(struct file *filp, struct kobject *kobj, struct bin_attribute *bin_attr, char *buf, loff_t off, size_t count)

    Dump the adapter trace

    :param filp:
        open sysfs file
    :type filp: struct file \*

    :param kobj:
        kobject struct
    :type kobj: struct kobject \*

    :param bin_attr:
        bin_attribute struct
    :type bin_attr: struct bin_attribute \*

    :param buf:
        buffer
    :type buf: char \*

    :param off:
        offset
    :type off: loff_t

    :param count:
        buffer size
    :type count: size_t

.. _`ipr_read_trace.return-value`:

Return value
------------

number of bytes printed to buffer

.. _`ipr_show_fw_version`:

ipr_show_fw_version
===================

.. c:function:: ssize_t ipr_show_fw_version(struct device *dev, struct device_attribute *attr, char *buf)

    Show the firmware version

    :param dev:
        class device struct
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        buffer
    :type buf: char \*

.. _`ipr_show_fw_version.return-value`:

Return value
------------

number of bytes printed to buffer

.. _`ipr_show_log_level`:

ipr_show_log_level
==================

.. c:function:: ssize_t ipr_show_log_level(struct device *dev, struct device_attribute *attr, char *buf)

    Show the adapter's error logging level

    :param dev:
        class device struct
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        buffer
    :type buf: char \*

.. _`ipr_show_log_level.return-value`:

Return value
------------

number of bytes printed to buffer

.. _`ipr_store_log_level`:

ipr_store_log_level
===================

.. c:function:: ssize_t ipr_store_log_level(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Change the adapter's error logging level

    :param dev:
        class device struct
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        buffer
    :type buf: const char \*

    :param count:
        *undescribed*
    :type count: size_t

.. _`ipr_store_log_level.return-value`:

Return value
------------

number of bytes printed to buffer

.. _`ipr_store_diagnostics`:

ipr_store_diagnostics
=====================

.. c:function:: ssize_t ipr_store_diagnostics(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    IOA Diagnostics interface

    :param dev:
        device struct
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        buffer
    :type buf: const char \*

    :param count:
        buffer size
    :type count: size_t

.. _`ipr_store_diagnostics.description`:

Description
-----------

This function will reset the adapter and wait a reasonable
amount of time for any errors that the adapter might log.

.. _`ipr_store_diagnostics.return-value`:

Return value
------------

count on success / other on failure

.. _`ipr_show_adapter_state`:

ipr_show_adapter_state
======================

.. c:function:: ssize_t ipr_show_adapter_state(struct device *dev, struct device_attribute *attr, char *buf)

    Show the adapter's state

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        buffer
    :type buf: char \*

.. _`ipr_show_adapter_state.return-value`:

Return value
------------

number of bytes printed to buffer

.. _`ipr_store_adapter_state`:

ipr_store_adapter_state
=======================

.. c:function:: ssize_t ipr_store_adapter_state(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Change adapter state

    :param dev:
        device struct
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        buffer
    :type buf: const char \*

    :param count:
        buffer size
    :type count: size_t

.. _`ipr_store_adapter_state.description`:

Description
-----------

This function will change the adapter's state.

.. _`ipr_store_adapter_state.return-value`:

Return value
------------

count on success / other on failure

.. _`ipr_store_reset_adapter`:

ipr_store_reset_adapter
=======================

.. c:function:: ssize_t ipr_store_reset_adapter(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Reset the adapter

    :param dev:
        device struct
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        buffer
    :type buf: const char \*

    :param count:
        buffer size
    :type count: size_t

.. _`ipr_store_reset_adapter.description`:

Description
-----------

This function will reset the adapter.

.. _`ipr_store_reset_adapter.return-value`:

Return value
------------

count on success / other on failure

.. _`ipr_store_iopoll_weight`:

ipr_store_iopoll_weight
=======================

.. c:function:: ssize_t ipr_store_iopoll_weight(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Change the adapter's polling mode

    :param dev:
        class device struct
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        buffer
    :type buf: const char \*

    :param count:
        *undescribed*
    :type count: size_t

.. _`ipr_store_iopoll_weight.return-value`:

Return value
------------

number of bytes printed to buffer

.. _`ipr_alloc_ucode_buffer`:

ipr_alloc_ucode_buffer
======================

.. c:function:: struct ipr_sglist *ipr_alloc_ucode_buffer(int buf_len)

    Allocates a microcode download buffer

    :param buf_len:
        buffer length
    :type buf_len: int

.. _`ipr_alloc_ucode_buffer.description`:

Description
-----------

Allocates a DMA'able buffer in chunks and assembles a scatter/gather
list to use for microcode download

.. _`ipr_alloc_ucode_buffer.return-value`:

Return value
------------

pointer to sglist / NULL on failure

.. _`ipr_free_ucode_buffer`:

ipr_free_ucode_buffer
=====================

.. c:function:: void ipr_free_ucode_buffer(struct ipr_sglist *sglist)

    Frees a microcode download buffer

    :param sglist:
        *undescribed*
    :type sglist: struct ipr_sglist \*

.. _`ipr_free_ucode_buffer.description`:

Description
-----------

Free a DMA'able ucode download buffer previously allocated with
ipr_alloc_ucode_buffer

.. _`ipr_free_ucode_buffer.return-value`:

Return value
------------

nothing

.. _`ipr_copy_ucode_buffer`:

ipr_copy_ucode_buffer
=====================

.. c:function:: int ipr_copy_ucode_buffer(struct ipr_sglist *sglist, u8 *buffer, u32 len)

    Copy user buffer to kernel buffer

    :param sglist:
        scatter/gather list pointer
    :type sglist: struct ipr_sglist \*

    :param buffer:
        buffer pointer
    :type buffer: u8 \*

    :param len:
        buffer length
    :type len: u32

.. _`ipr_copy_ucode_buffer.description`:

Description
-----------

Copy a microcode image from a user buffer into a buffer allocated by
ipr_alloc_ucode_buffer

.. _`ipr_copy_ucode_buffer.return-value`:

Return value
------------

0 on success / other on failure

.. _`ipr_build_ucode_ioadl64`:

ipr_build_ucode_ioadl64
=======================

.. c:function:: void ipr_build_ucode_ioadl64(struct ipr_cmnd *ipr_cmd, struct ipr_sglist *sglist)

    Build a microcode download IOADL

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

    :param sglist:
        scatter/gather list
    :type sglist: struct ipr_sglist \*

.. _`ipr_build_ucode_ioadl64.description`:

Description
-----------

Builds a microcode download IOA data list (IOADL).

.. _`ipr_build_ucode_ioadl`:

ipr_build_ucode_ioadl
=====================

.. c:function:: void ipr_build_ucode_ioadl(struct ipr_cmnd *ipr_cmd, struct ipr_sglist *sglist)

    Build a microcode download IOADL

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

    :param sglist:
        scatter/gather list
    :type sglist: struct ipr_sglist \*

.. _`ipr_build_ucode_ioadl.description`:

Description
-----------

Builds a microcode download IOA data list (IOADL).

.. _`ipr_update_ioa_ucode`:

ipr_update_ioa_ucode
====================

.. c:function:: int ipr_update_ioa_ucode(struct ipr_ioa_cfg *ioa_cfg, struct ipr_sglist *sglist)

    Update IOA's microcode

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param sglist:
        scatter/gather list
    :type sglist: struct ipr_sglist \*

.. _`ipr_update_ioa_ucode.description`:

Description
-----------

Initiate an adapter reset to update the IOA's microcode

.. _`ipr_update_ioa_ucode.return-value`:

Return value
------------

0 on success / -EIO on failure

.. _`ipr_store_update_fw`:

ipr_store_update_fw
===================

.. c:function:: ssize_t ipr_store_update_fw(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Update the firmware on the adapter

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        buffer
    :type buf: const char \*

    :param count:
        buffer size
    :type count: size_t

.. _`ipr_store_update_fw.description`:

Description
-----------

This function will update the firmware on the adapter.

.. _`ipr_store_update_fw.return-value`:

Return value
------------

count on success / other on failure

.. _`ipr_show_fw_type`:

ipr_show_fw_type
================

.. c:function:: ssize_t ipr_show_fw_type(struct device *dev, struct device_attribute *attr, char *buf)

    Show the adapter's firmware type.

    :param dev:
        class device struct
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        buffer
    :type buf: char \*

.. _`ipr_show_fw_type.return-value`:

Return value
------------

number of bytes printed to buffer

.. _`ipr_read_dump`:

ipr_read_dump
=============

.. c:function:: ssize_t ipr_read_dump(struct file *filp, struct kobject *kobj, struct bin_attribute *bin_attr, char *buf, loff_t off, size_t count)

    Dump the adapter

    :param filp:
        open sysfs file
    :type filp: struct file \*

    :param kobj:
        kobject struct
    :type kobj: struct kobject \*

    :param bin_attr:
        bin_attribute struct
    :type bin_attr: struct bin_attribute \*

    :param buf:
        buffer
    :type buf: char \*

    :param off:
        offset
    :type off: loff_t

    :param count:
        buffer size
    :type count: size_t

.. _`ipr_read_dump.return-value`:

Return value
------------

number of bytes printed to buffer

.. _`ipr_alloc_dump`:

ipr_alloc_dump
==============

.. c:function:: int ipr_alloc_dump(struct ipr_ioa_cfg *ioa_cfg)

    Prepare for adapter dump

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

.. _`ipr_alloc_dump.return-value`:

Return value
------------

0 on success / other on failure

.. _`ipr_free_dump`:

ipr_free_dump
=============

.. c:function:: int ipr_free_dump(struct ipr_ioa_cfg *ioa_cfg)

    Free adapter dump memory

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

.. _`ipr_free_dump.return-value`:

Return value
------------

0 on success / other on failure

.. _`ipr_write_dump`:

ipr_write_dump
==============

.. c:function:: ssize_t ipr_write_dump(struct file *filp, struct kobject *kobj, struct bin_attribute *bin_attr, char *buf, loff_t off, size_t count)

    Setup dump state of adapter

    :param filp:
        open sysfs file
    :type filp: struct file \*

    :param kobj:
        kobject struct
    :type kobj: struct kobject \*

    :param bin_attr:
        bin_attribute struct
    :type bin_attr: struct bin_attribute \*

    :param buf:
        buffer
    :type buf: char \*

    :param off:
        offset
    :type off: loff_t

    :param count:
        buffer size
    :type count: size_t

.. _`ipr_write_dump.return-value`:

Return value
------------

number of bytes printed to buffer

.. _`ipr_change_queue_depth`:

ipr_change_queue_depth
======================

.. c:function:: int ipr_change_queue_depth(struct scsi_device *sdev, int qdepth)

    Change the device's queue depth

    :param sdev:
        scsi device struct
    :type sdev: struct scsi_device \*

    :param qdepth:
        depth to set
    :type qdepth: int

.. _`ipr_change_queue_depth.return-value`:

Return value
------------

actual depth set

.. _`ipr_show_adapter_handle`:

ipr_show_adapter_handle
=======================

.. c:function:: ssize_t ipr_show_adapter_handle(struct device *dev, struct device_attribute *attr, char *buf)

    Show the adapter's resource handle for this device

    :param dev:
        device struct
    :type dev: struct device \*

    :param attr:
        device attribute structure
    :type attr: struct device_attribute \*

    :param buf:
        buffer
    :type buf: char \*

.. _`ipr_show_adapter_handle.return-value`:

Return value
------------

number of bytes printed to buffer

.. _`ipr_show_resource_path`:

ipr_show_resource_path
======================

.. c:function:: ssize_t ipr_show_resource_path(struct device *dev, struct device_attribute *attr, char *buf)

    Show the resource path or the resource address for this device.

    :param dev:
        device struct
    :type dev: struct device \*

    :param attr:
        device attribute structure
    :type attr: struct device_attribute \*

    :param buf:
        buffer
    :type buf: char \*

.. _`ipr_show_resource_path.return-value`:

Return value
------------

number of bytes printed to buffer

.. _`ipr_show_device_id`:

ipr_show_device_id
==================

.. c:function:: ssize_t ipr_show_device_id(struct device *dev, struct device_attribute *attr, char *buf)

    Show the device_id for this device.

    :param dev:
        device struct
    :type dev: struct device \*

    :param attr:
        device attribute structure
    :type attr: struct device_attribute \*

    :param buf:
        buffer
    :type buf: char \*

.. _`ipr_show_device_id.return-value`:

Return value
------------

number of bytes printed to buffer

.. _`ipr_show_resource_type`:

ipr_show_resource_type
======================

.. c:function:: ssize_t ipr_show_resource_type(struct device *dev, struct device_attribute *attr, char *buf)

    Show the resource type for this device.

    :param dev:
        device struct
    :type dev: struct device \*

    :param attr:
        device attribute structure
    :type attr: struct device_attribute \*

    :param buf:
        buffer
    :type buf: char \*

.. _`ipr_show_resource_type.return-value`:

Return value
------------

number of bytes printed to buffer

.. _`ipr_show_raw_mode`:

ipr_show_raw_mode
=================

.. c:function:: ssize_t ipr_show_raw_mode(struct device *dev, struct device_attribute *attr, char *buf)

    Show the adapter's raw mode

    :param dev:
        class device struct
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        buffer
    :type buf: char \*

.. _`ipr_show_raw_mode.return-value`:

Return value
------------

number of bytes printed to buffer

.. _`ipr_store_raw_mode`:

ipr_store_raw_mode
==================

.. c:function:: ssize_t ipr_store_raw_mode(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Change the adapter's raw mode

    :param dev:
        class device struct
    :type dev: struct device \*

    :param attr:
        *undescribed*
    :type attr: struct device_attribute \*

    :param buf:
        buffer
    :type buf: const char \*

    :param count:
        *undescribed*
    :type count: size_t

.. _`ipr_store_raw_mode.return-value`:

Return value
------------

number of bytes printed to buffer

.. _`ipr_biosparam`:

ipr_biosparam
=============

.. c:function:: int ipr_biosparam(struct scsi_device *sdev, struct block_device *block_device, sector_t capacity, int *parm)

    Return the HSC mapping

    :param sdev:
        scsi device struct
    :type sdev: struct scsi_device \*

    :param block_device:
        block device pointer
    :type block_device: struct block_device \*

    :param capacity:
        capacity of the device
    :type capacity: sector_t

    :param parm:
        Array containing returned HSC values.
    :type parm: int \*

.. _`ipr_biosparam.description`:

Description
-----------

This function generates the HSC parms that fdisk uses.
We want to make sure we return something that places partitions
on 4k boundaries for best performance with the IOA.

.. _`ipr_biosparam.return-value`:

Return value
------------

0 on success

.. _`ipr_find_starget`:

ipr_find_starget
================

.. c:function:: struct ipr_resource_entry *ipr_find_starget(struct scsi_target *starget)

    Find target based on bus/target.

    :param starget:
        scsi target struct
    :type starget: struct scsi_target \*

.. _`ipr_find_starget.return-value`:

Return value
------------

resource entry pointer if found / NULL if not found

.. _`ipr_target_alloc`:

ipr_target_alloc
================

.. c:function:: int ipr_target_alloc(struct scsi_target *starget)

    Prepare for commands to a SCSI target

    :param starget:
        scsi target struct
    :type starget: struct scsi_target \*

.. _`ipr_target_alloc.description`:

Description
-----------

If the device is a SATA device, this function allocates an
ATA port with libata, else it does nothing.

.. _`ipr_target_alloc.return-value`:

Return value
------------

0 on success / non-0 on failure

.. _`ipr_target_destroy`:

ipr_target_destroy
==================

.. c:function:: void ipr_target_destroy(struct scsi_target *starget)

    Destroy a SCSI target

    :param starget:
        scsi target struct
    :type starget: struct scsi_target \*

.. _`ipr_target_destroy.description`:

Description
-----------

If the device was a SATA device, this function frees the libata
ATA port, else it does nothing.

.. _`ipr_find_sdev`:

ipr_find_sdev
=============

.. c:function:: struct ipr_resource_entry *ipr_find_sdev(struct scsi_device *sdev)

    Find device based on bus/target/lun.

    :param sdev:
        scsi device struct
    :type sdev: struct scsi_device \*

.. _`ipr_find_sdev.return-value`:

Return value
------------

resource entry pointer if found / NULL if not found

.. _`ipr_slave_destroy`:

ipr_slave_destroy
=================

.. c:function:: void ipr_slave_destroy(struct scsi_device *sdev)

    Unconfigure a SCSI device

    :param sdev:
        scsi device struct
    :type sdev: struct scsi_device \*

.. _`ipr_slave_destroy.return-value`:

Return value
------------

nothing

.. _`ipr_slave_configure`:

ipr_slave_configure
===================

.. c:function:: int ipr_slave_configure(struct scsi_device *sdev)

    Configure a SCSI device

    :param sdev:
        scsi device struct
    :type sdev: struct scsi_device \*

.. _`ipr_slave_configure.description`:

Description
-----------

This function configures the specified scsi device.

.. _`ipr_slave_configure.return-value`:

Return value
------------

0 on success

.. _`ipr_ata_slave_alloc`:

ipr_ata_slave_alloc
===================

.. c:function:: int ipr_ata_slave_alloc(struct scsi_device *sdev)

    Prepare for commands to a SATA device

    :param sdev:
        scsi device struct
    :type sdev: struct scsi_device \*

.. _`ipr_ata_slave_alloc.description`:

Description
-----------

This function initializes an ATA port so that future commands
sent through queuecommand will work.

.. _`ipr_ata_slave_alloc.return-value`:

Return value
------------

0 on success

.. _`ipr_slave_alloc`:

ipr_slave_alloc
===============

.. c:function:: int ipr_slave_alloc(struct scsi_device *sdev)

    Prepare for commands to a device.

    :param sdev:
        scsi device struct
    :type sdev: struct scsi_device \*

.. _`ipr_slave_alloc.description`:

Description
-----------

This function saves a pointer to the resource entry
in the scsi device struct if the device exists. We
can then use this pointer in ipr_queuecommand when
handling new commands.

.. _`ipr_slave_alloc.return-value`:

Return value
------------

0 on success / -ENXIO if device does not exist

.. _`ipr_match_lun`:

ipr_match_lun
=============

.. c:function:: int ipr_match_lun(struct ipr_cmnd *ipr_cmd, void *device)

    Match function for specified LUN

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

    :param device:
        device to match (sdev)
    :type device: void \*

.. _`ipr_match_lun.return`:

Return
------

1 if command matches sdev / 0 if command does not match sdev

.. _`ipr_cmnd_is_free`:

ipr_cmnd_is_free
================

.. c:function:: bool ipr_cmnd_is_free(struct ipr_cmnd *ipr_cmd)

    Check if a command is free or not \ ``ipr_cmd``\      ipr command struct

    :param ipr_cmd:
        *undescribed*
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_cmnd_is_free.return`:

Return
------

true / false

.. _`ipr_match_res`:

ipr_match_res
=============

.. c:function:: int ipr_match_res(struct ipr_cmnd *ipr_cmd, void *resource)

    Match function for specified resource entry

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

    :param resource:
        resource entry to match
    :type resource: void \*

.. _`ipr_match_res.return`:

Return
------

1 if command matches sdev / 0 if command does not match sdev

.. _`ipr_wait_for_ops`:

ipr_wait_for_ops
================

.. c:function:: int ipr_wait_for_ops(struct ipr_ioa_cfg *ioa_cfg, void *device, int (*match)(struct ipr_cmnd *, void *))

    Wait for matching commands to complete

    :param ioa_cfg:
        *undescribed*
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param device:
        device to match (sdev)
    :type device: void \*

    :param int (\*match)(struct ipr_cmnd \*, void \*):
        match function to use

.. _`ipr_wait_for_ops.return`:

Return
------

SUCCESS / FAILED

.. _`ipr_device_reset`:

ipr_device_reset
================

.. c:function:: int ipr_device_reset(struct ipr_ioa_cfg *ioa_cfg, struct ipr_resource_entry *res)

    Reset the device

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param res:
        resource entry struct
    :type res: struct ipr_resource_entry \*

.. _`ipr_device_reset.description`:

Description
-----------

This function issues a device reset to the affected device.
If the device is a SCSI device, a LUN reset will be sent
to the device first. If that does not work, a target reset
will be sent. If the device is a SATA device, a PHY reset will
be sent.

.. _`ipr_device_reset.return-value`:

Return value
------------

0 on success / non-zero on failure

.. _`ipr_sata_reset`:

ipr_sata_reset
==============

.. c:function:: int ipr_sata_reset(struct ata_link *link, unsigned int *classes, unsigned long deadline)

    Reset the SATA port

    :param link:
        SATA link to reset
    :type link: struct ata_link \*

    :param classes:
        class of the attached device
    :type classes: unsigned int \*

    :param deadline:
        *undescribed*
    :type deadline: unsigned long

.. _`ipr_sata_reset.description`:

Description
-----------

This function issues a SATA phy reset to the affected ATA link.

.. _`ipr_sata_reset.return-value`:

Return value
------------

0 on success / non-zero on failure

.. _`__ipr_eh_dev_reset`:

\__ipr_eh_dev_reset
===================

.. c:function:: int __ipr_eh_dev_reset(struct scsi_cmnd *scsi_cmd)

    Reset the device

    :param scsi_cmd:
        scsi command struct
    :type scsi_cmd: struct scsi_cmnd \*

.. _`__ipr_eh_dev_reset.description`:

Description
-----------

This function issues a device reset to the affected device.
A LUN reset will be sent to the device first. If that does
not work, a target reset will be sent.

.. _`__ipr_eh_dev_reset.return-value`:

Return value
------------

SUCCESS / FAILED

.. _`ipr_bus_reset_done`:

ipr_bus_reset_done
==================

.. c:function:: void ipr_bus_reset_done(struct ipr_cmnd *ipr_cmd)

    Op done function for bus reset.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_bus_reset_done.description`:

Description
-----------

This function is the op done function for a bus reset

.. _`ipr_bus_reset_done.return-value`:

Return value
------------

none

.. _`ipr_abort_timeout`:

ipr_abort_timeout
=================

.. c:function:: void ipr_abort_timeout(struct timer_list *t)

    An abort task has timed out

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`ipr_abort_timeout.description`:

Description
-----------

This function handles when an abort task times out. If this
happens we issue a bus reset since we have resources tied
up that must be freed before returning to the midlayer.

.. _`ipr_abort_timeout.return-value`:

Return value
------------

none

.. _`ipr_cancel_op`:

ipr_cancel_op
=============

.. c:function:: int ipr_cancel_op(struct scsi_cmnd *scsi_cmd)

    Cancel specified op

    :param scsi_cmd:
        scsi command struct
    :type scsi_cmd: struct scsi_cmnd \*

.. _`ipr_cancel_op.description`:

Description
-----------

This function cancels specified op.

.. _`ipr_cancel_op.return-value`:

Return value
------------

SUCCESS / FAILED

.. _`ipr_scan_finished`:

ipr_scan_finished
=================

.. c:function:: int ipr_scan_finished(struct Scsi_Host *shost, unsigned long elapsed_time)

    Abort a single op

    :param shost:
        *undescribed*
    :type shost: struct Scsi_Host \*

    :param elapsed_time:
        *undescribed*
    :type elapsed_time: unsigned long

.. _`ipr_scan_finished.return-value`:

Return value
------------

0 if scan in progress / 1 if scan is complete

.. _`ipr_eh_abort`:

ipr_eh_abort
============

.. c:function:: int ipr_eh_abort(struct scsi_cmnd *scsi_cmd)

    Reset the host adapter

    :param scsi_cmd:
        scsi command struct
    :type scsi_cmd: struct scsi_cmnd \*

.. _`ipr_eh_abort.return-value`:

Return value
------------

SUCCESS / FAILED

.. _`ipr_handle_other_interrupt`:

ipr_handle_other_interrupt
==========================

.. c:function:: irqreturn_t ipr_handle_other_interrupt(struct ipr_ioa_cfg *ioa_cfg, u32 int_reg)

    Handle "other" interrupts

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param int_reg:
        interrupt register
    :type int_reg: u32

.. _`ipr_handle_other_interrupt.return-value`:

Return value
------------

IRQ_NONE / IRQ_HANDLED

.. _`ipr_isr_eh`:

ipr_isr_eh
==========

.. c:function:: void ipr_isr_eh(struct ipr_ioa_cfg *ioa_cfg, char *msg, u16 number)

    Interrupt service routine error handler

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param msg:
        message to log
    :type msg: char \*

    :param number:
        *undescribed*
    :type number: u16

.. _`ipr_isr_eh.return-value`:

Return value
------------

none

.. _`ipr_isr`:

ipr_isr
=======

.. c:function:: irqreturn_t ipr_isr(int irq, void *devp)

    Interrupt service routine

    :param irq:
        irq number
    :type irq: int

    :param devp:
        pointer to ioa config struct
    :type devp: void \*

.. _`ipr_isr.return-value`:

Return value
------------

IRQ_NONE / IRQ_HANDLED

.. _`ipr_isr_mhrrq`:

ipr_isr_mhrrq
=============

.. c:function:: irqreturn_t ipr_isr_mhrrq(int irq, void *devp)

    Interrupt service routine

    :param irq:
        irq number
    :type irq: int

    :param devp:
        pointer to ioa config struct
    :type devp: void \*

.. _`ipr_isr_mhrrq.return-value`:

Return value
------------

IRQ_NONE / IRQ_HANDLED

.. _`ipr_build_ioadl64`:

ipr_build_ioadl64
=================

.. c:function:: int ipr_build_ioadl64(struct ipr_ioa_cfg *ioa_cfg, struct ipr_cmnd *ipr_cmd)

    Build a scatter/gather list and map the buffer

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_build_ioadl64.return-value`:

Return value
------------

0 on success / -1 on failure

.. _`ipr_build_ioadl`:

ipr_build_ioadl
===============

.. c:function:: int ipr_build_ioadl(struct ipr_ioa_cfg *ioa_cfg, struct ipr_cmnd *ipr_cmd)

    Build a scatter/gather list and map the buffer

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_build_ioadl.return-value`:

Return value
------------

0 on success / -1 on failure

.. _`__ipr_erp_done`:

\__ipr_erp_done
===============

.. c:function:: void __ipr_erp_done(struct ipr_cmnd *ipr_cmd)

    Process completion of ERP for a device

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`__ipr_erp_done.description`:

Description
-----------

This function copies the sense buffer into the scsi_cmd
struct and pushes the scsi_done function.

.. _`__ipr_erp_done.return-value`:

Return value
------------

nothing

.. _`ipr_erp_done`:

ipr_erp_done
============

.. c:function:: void ipr_erp_done(struct ipr_cmnd *ipr_cmd)

    Process completion of ERP for a device

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_erp_done.description`:

Description
-----------

This function copies the sense buffer into the scsi_cmd
struct and pushes the scsi_done function.

.. _`ipr_erp_done.return-value`:

Return value
------------

nothing

.. _`ipr_reinit_ipr_cmnd_for_erp`:

ipr_reinit_ipr_cmnd_for_erp
===========================

.. c:function:: void ipr_reinit_ipr_cmnd_for_erp(struct ipr_cmnd *ipr_cmd)

    Re-initialize a cmnd block to be used for ERP

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reinit_ipr_cmnd_for_erp.return-value`:

Return value
------------

none

.. _`__ipr_erp_request_sense`:

\__ipr_erp_request_sense
========================

.. c:function:: void __ipr_erp_request_sense(struct ipr_cmnd *ipr_cmd)

    Send request sense to a device

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`__ipr_erp_request_sense.description`:

Description
-----------

This function sends a request sense to a device as a result
of a check condition.

.. _`__ipr_erp_request_sense.return-value`:

Return value
------------

nothing

.. _`ipr_erp_request_sense`:

ipr_erp_request_sense
=====================

.. c:function:: void ipr_erp_request_sense(struct ipr_cmnd *ipr_cmd)

    Send request sense to a device

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_erp_request_sense.description`:

Description
-----------

This function sends a request sense to a device as a result
of a check condition.

.. _`ipr_erp_request_sense.return-value`:

Return value
------------

nothing

.. _`ipr_erp_cancel_all`:

ipr_erp_cancel_all
==================

.. c:function:: void ipr_erp_cancel_all(struct ipr_cmnd *ipr_cmd)

    Send cancel all to a device

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_erp_cancel_all.description`:

Description
-----------

This function sends a cancel all to a device to clear the
queue. If we are running TCQ on the device, QERR is set to 1,
which means all outstanding ops have been dropped on the floor.
Cancel all will return them to us.

.. _`ipr_erp_cancel_all.return-value`:

Return value
------------

nothing

.. _`ipr_dump_ioasa`:

ipr_dump_ioasa
==============

.. c:function:: void ipr_dump_ioasa(struct ipr_ioa_cfg *ioa_cfg, struct ipr_cmnd *ipr_cmd, struct ipr_resource_entry *res)

    Dump contents of IOASA

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

    :param res:
        resource entry struct
    :type res: struct ipr_resource_entry \*

.. _`ipr_dump_ioasa.description`:

Description
-----------

This function is invoked by the interrupt handler when ops
fail. It will log the IOASA if appropriate. Only called
for GPDD ops.

.. _`ipr_dump_ioasa.return-value`:

Return value
------------

none

.. _`ipr_gen_sense`:

ipr_gen_sense
=============

.. c:function:: void ipr_gen_sense(struct ipr_cmnd *ipr_cmd)

    Generate SCSI sense data from an IOASA

    :param ipr_cmd:
        *undescribed*
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_gen_sense.return-value`:

Return value
------------

none

.. _`ipr_get_autosense`:

ipr_get_autosense
=================

.. c:function:: int ipr_get_autosense(struct ipr_cmnd *ipr_cmd)

    Copy autosense data to sense buffer

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_get_autosense.description`:

Description
-----------

This function copies the autosense buffer to the buffer
in the scsi_cmd, if there is autosense available.

.. _`ipr_get_autosense.return-value`:

Return value
------------

1 if autosense was available / 0 if not

.. _`ipr_erp_start`:

ipr_erp_start
=============

.. c:function:: void ipr_erp_start(struct ipr_ioa_cfg *ioa_cfg, struct ipr_cmnd *ipr_cmd)

    Process an error response for a SCSI op

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_erp_start.description`:

Description
-----------

This function determines whether or not to initiate ERP
on the affected device.

.. _`ipr_erp_start.return-value`:

Return value
------------

nothing

.. _`ipr_scsi_done`:

ipr_scsi_done
=============

.. c:function:: void ipr_scsi_done(struct ipr_cmnd *ipr_cmd)

    mid-layer done function

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_scsi_done.description`:

Description
-----------

This function is invoked by the interrupt handler for
ops generated by the SCSI mid-layer

.. _`ipr_scsi_done.return-value`:

Return value
------------

none

.. _`ipr_queuecommand`:

ipr_queuecommand
================

.. c:function:: int ipr_queuecommand(struct Scsi_Host *shost, struct scsi_cmnd *scsi_cmd)

    Queue a mid-layer request

    :param shost:
        scsi host struct
    :type shost: struct Scsi_Host \*

    :param scsi_cmd:
        scsi command struct
    :type scsi_cmd: struct scsi_cmnd \*

.. _`ipr_queuecommand.description`:

Description
-----------

This function queues a request generated by the mid-layer.

.. _`ipr_queuecommand.return-value`:

Return value
------------

0 on success
SCSI_MLQUEUE_DEVICE_BUSY if device is busy
SCSI_MLQUEUE_HOST_BUSY if host is busy

.. _`ipr_ioctl`:

ipr_ioctl
=========

.. c:function:: int ipr_ioctl(struct scsi_device *sdev, int cmd, void __user *arg)

    IOCTL handler

    :param sdev:
        scsi device struct
    :type sdev: struct scsi_device \*

    :param cmd:
        IOCTL cmd
    :type cmd: int

    :param arg:
        IOCTL arg
    :type arg: void __user \*

.. _`ipr_ioctl.return-value`:

Return value
------------

0 on success / other on failure

.. _`ipr_ioa_info`:

ipr_ioa_info
============

.. c:function:: const char *ipr_ioa_info(struct Scsi_Host *host)

    Get information about the card/driver

    :param host:
        *undescribed*
    :type host: struct Scsi_Host \*

.. _`ipr_ioa_info.return-value`:

Return value
------------

pointer to buffer with description string

.. _`ipr_ata_phy_reset`:

ipr_ata_phy_reset
=================

.. c:function:: void ipr_ata_phy_reset(struct ata_port *ap)

    libata phy_reset handler

    :param ap:
        ata port to reset
    :type ap: struct ata_port \*

.. _`ipr_ata_post_internal`:

ipr_ata_post_internal
=====================

.. c:function:: void ipr_ata_post_internal(struct ata_queued_cmd *qc)

    Cleanup after an internal command

    :param qc:
        ATA queued command
    :type qc: struct ata_queued_cmd \*

.. _`ipr_ata_post_internal.return-value`:

Return value
------------

none

.. _`ipr_copy_sata_tf`:

ipr_copy_sata_tf
================

.. c:function:: void ipr_copy_sata_tf(struct ipr_ioarcb_ata_regs *regs, struct ata_taskfile *tf)

    Copy a SATA taskfile to an IOA data structure

    :param regs:
        destination
    :type regs: struct ipr_ioarcb_ata_regs \*

    :param tf:
        source ATA taskfile
    :type tf: struct ata_taskfile \*

.. _`ipr_copy_sata_tf.return-value`:

Return value
------------

none

.. _`ipr_sata_done`:

ipr_sata_done
=============

.. c:function:: void ipr_sata_done(struct ipr_cmnd *ipr_cmd)

    done function for SATA commands

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_sata_done.description`:

Description
-----------

This function is invoked by the interrupt handler for
ops generated by the SCSI mid-layer to SATA devices

.. _`ipr_sata_done.return-value`:

Return value
------------

none

.. _`ipr_build_ata_ioadl64`:

ipr_build_ata_ioadl64
=====================

.. c:function:: void ipr_build_ata_ioadl64(struct ipr_cmnd *ipr_cmd, struct ata_queued_cmd *qc)

    Build an ATA scatter/gather list

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

    :param qc:
        ATA queued command
    :type qc: struct ata_queued_cmd \*

.. _`ipr_build_ata_ioadl`:

ipr_build_ata_ioadl
===================

.. c:function:: void ipr_build_ata_ioadl(struct ipr_cmnd *ipr_cmd, struct ata_queued_cmd *qc)

    Build an ATA scatter/gather list

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

    :param qc:
        ATA queued command
    :type qc: struct ata_queued_cmd \*

.. _`ipr_qc_defer`:

ipr_qc_defer
============

.. c:function:: int ipr_qc_defer(struct ata_queued_cmd *qc)

    Get a free ipr_cmd

    :param qc:
        queued command
    :type qc: struct ata_queued_cmd \*

.. _`ipr_qc_defer.return-value`:

Return value
------------

0 if success

.. _`ipr_qc_issue`:

ipr_qc_issue
============

.. c:function:: unsigned int ipr_qc_issue(struct ata_queued_cmd *qc)

    Issue a SATA qc to a device

    :param qc:
        queued command
    :type qc: struct ata_queued_cmd \*

.. _`ipr_qc_issue.return-value`:

Return value
------------

0 if success

.. _`ipr_qc_fill_rtf`:

ipr_qc_fill_rtf
===============

.. c:function:: bool ipr_qc_fill_rtf(struct ata_queued_cmd *qc)

    Read result TF

    :param qc:
        ATA queued command
    :type qc: struct ata_queued_cmd \*

.. _`ipr_qc_fill_rtf.return-value`:

Return value
------------

true

.. _`ipr_invalid_adapter`:

ipr_invalid_adapter
===================

.. c:function:: int ipr_invalid_adapter(struct ipr_ioa_cfg *ioa_cfg)

    Determine if this adapter is supported on this hardware

    :param ioa_cfg:
        ioa cfg struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

.. _`ipr_invalid_adapter.description`:

Description
-----------

Adapters that use Gemstone revision < 3.1 do not work reliably on
certain pSeries hardware. This function determines if the given
adapter is in one of these confgurations or not.

.. _`ipr_invalid_adapter.return-value`:

Return value
------------

1 if adapter is not supported / 0 if adapter is supported

.. _`ipr_ioa_bringdown_done`:

ipr_ioa_bringdown_done
======================

.. c:function:: int ipr_ioa_bringdown_done(struct ipr_cmnd *ipr_cmd)

    IOA bring down completion.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_ioa_bringdown_done.description`:

Description
-----------

This function processes the completion of an adapter bring down.
It wakes any reset sleepers.

.. _`ipr_ioa_bringdown_done.return-value`:

Return value
------------

IPR_RC_JOB_RETURN

.. _`ipr_ioa_reset_done`:

ipr_ioa_reset_done
==================

.. c:function:: int ipr_ioa_reset_done(struct ipr_cmnd *ipr_cmd)

    IOA reset completion.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_ioa_reset_done.description`:

Description
-----------

This function processes the completion of an adapter reset.
It schedules any necessary mid-layer add/removes and
wakes any reset sleepers.

.. _`ipr_ioa_reset_done.return-value`:

Return value
------------

IPR_RC_JOB_RETURN

.. _`ipr_set_sup_dev_dflt`:

ipr_set_sup_dev_dflt
====================

.. c:function:: void ipr_set_sup_dev_dflt(struct ipr_supported_device *supported_dev, struct ipr_std_inq_vpids *vpids)

    Initialize a Set Supported Device buffer

    :param supported_dev:
        supported device struct
    :type supported_dev: struct ipr_supported_device \*

    :param vpids:
        vendor product id struct
    :type vpids: struct ipr_std_inq_vpids \*

.. _`ipr_set_sup_dev_dflt.return-value`:

Return value
------------

none

.. _`ipr_set_supported_devs`:

ipr_set_supported_devs
======================

.. c:function:: int ipr_set_supported_devs(struct ipr_cmnd *ipr_cmd)

    Send Set Supported Devices for a device

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_set_supported_devs.description`:

Description
-----------

This function sends a Set Supported Devices to the adapter

.. _`ipr_set_supported_devs.return-value`:

Return value
------------

IPR_RC_JOB_CONTINUE / IPR_RC_JOB_RETURN

.. _`ipr_get_mode_page`:

ipr_get_mode_page
=================

.. c:function:: void *ipr_get_mode_page(struct ipr_mode_pages *mode_pages, u32 page_code, u32 len)

    Locate specified mode page

    :param mode_pages:
        mode page buffer
    :type mode_pages: struct ipr_mode_pages \*

    :param page_code:
        page code to find
    :type page_code: u32

    :param len:
        minimum required length for mode page
    :type len: u32

.. _`ipr_get_mode_page.return-value`:

Return value
------------

pointer to mode page / NULL on failure

.. _`ipr_check_term_power`:

ipr_check_term_power
====================

.. c:function:: void ipr_check_term_power(struct ipr_ioa_cfg *ioa_cfg, struct ipr_mode_pages *mode_pages)

    Check for term power errors

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param mode_pages:
        IOAFP mode pages buffer
    :type mode_pages: struct ipr_mode_pages \*

.. _`ipr_check_term_power.description`:

Description
-----------

Check the IOAFP's mode page 28 for term power errors

.. _`ipr_check_term_power.return-value`:

Return value
------------

nothing

.. _`ipr_scsi_bus_speed_limit`:

ipr_scsi_bus_speed_limit
========================

.. c:function:: void ipr_scsi_bus_speed_limit(struct ipr_ioa_cfg *ioa_cfg)

    Limit the SCSI speed based on SES table

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

.. _`ipr_scsi_bus_speed_limit.description`:

Description
-----------

Looks through the config table checking for SES devices. If
the SES device is in the SES table indicating a maximum SCSI
bus speed, the speed is limited for the bus.

.. _`ipr_scsi_bus_speed_limit.return-value`:

Return value
------------

none

.. _`ipr_modify_ioafp_mode_page_28`:

ipr_modify_ioafp_mode_page_28
=============================

.. c:function:: void ipr_modify_ioafp_mode_page_28(struct ipr_ioa_cfg *ioa_cfg, struct ipr_mode_pages *mode_pages)

    Modify IOAFP Mode Page 28

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param mode_pages:
        mode page 28 buffer
    :type mode_pages: struct ipr_mode_pages \*

.. _`ipr_modify_ioafp_mode_page_28.description`:

Description
-----------

Updates mode page 28 based on driver configuration

.. _`ipr_modify_ioafp_mode_page_28.return-value`:

Return value
------------

none

.. _`ipr_build_mode_select`:

ipr_build_mode_select
=====================

.. c:function:: void ipr_build_mode_select(struct ipr_cmnd *ipr_cmd, __be32 res_handle, u8 parm, dma_addr_t dma_addr, u8 xfer_len)

    Build a mode select command

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

    :param res_handle:
        resource handle to send command to
    :type res_handle: __be32

    :param parm:
        Byte 2 of Mode Sense command
    :type parm: u8

    :param dma_addr:
        DMA buffer address
    :type dma_addr: dma_addr_t

    :param xfer_len:
        data transfer length
    :type xfer_len: u8

.. _`ipr_build_mode_select.return-value`:

Return value
------------

none

.. _`ipr_ioafp_mode_select_page28`:

ipr_ioafp_mode_select_page28
============================

.. c:function:: int ipr_ioafp_mode_select_page28(struct ipr_cmnd *ipr_cmd)

    Issue Mode Select Page 28 to IOA

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_ioafp_mode_select_page28.description`:

Description
-----------

This function sets up the SCSI bus attributes and sends
a Mode Select for Page 28 to activate them.

.. _`ipr_ioafp_mode_select_page28.return-value`:

Return value
------------

IPR_RC_JOB_RETURN

.. _`ipr_build_mode_sense`:

ipr_build_mode_sense
====================

.. c:function:: void ipr_build_mode_sense(struct ipr_cmnd *ipr_cmd, __be32 res_handle, u8 parm, dma_addr_t dma_addr, u8 xfer_len)

    Builds a mode sense command

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

    :param res_handle:
        *undescribed*
    :type res_handle: __be32

    :param parm:
        Byte 2 of mode sense command
    :type parm: u8

    :param dma_addr:
        DMA address of mode sense buffer
    :type dma_addr: dma_addr_t

    :param xfer_len:
        Size of DMA buffer
    :type xfer_len: u8

.. _`ipr_build_mode_sense.return-value`:

Return value
------------

none

.. _`ipr_reset_cmd_failed`:

ipr_reset_cmd_failed
====================

.. c:function:: int ipr_reset_cmd_failed(struct ipr_cmnd *ipr_cmd)

    Handle failure of IOA reset command

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reset_cmd_failed.description`:

Description
-----------

This function handles the failure of an IOA bringup command.

.. _`ipr_reset_cmd_failed.return-value`:

Return value
------------

IPR_RC_JOB_RETURN

.. _`ipr_reset_mode_sense_failed`:

ipr_reset_mode_sense_failed
===========================

.. c:function:: int ipr_reset_mode_sense_failed(struct ipr_cmnd *ipr_cmd)

    Handle failure of IOAFP mode sense

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reset_mode_sense_failed.description`:

Description
-----------

This function handles the failure of a Mode Sense to the IOAFP.
Some adapters do not handle all mode pages.

.. _`ipr_reset_mode_sense_failed.return-value`:

Return value
------------

IPR_RC_JOB_CONTINUE / IPR_RC_JOB_RETURN

.. _`ipr_ioafp_mode_sense_page28`:

ipr_ioafp_mode_sense_page28
===========================

.. c:function:: int ipr_ioafp_mode_sense_page28(struct ipr_cmnd *ipr_cmd)

    Issue Mode Sense Page 28 to IOA

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_ioafp_mode_sense_page28.description`:

Description
-----------

This function send a Page 28 mode sense to the IOA to
retrieve SCSI bus attributes.

.. _`ipr_ioafp_mode_sense_page28.return-value`:

Return value
------------

IPR_RC_JOB_RETURN

.. _`ipr_ioafp_mode_select_page24`:

ipr_ioafp_mode_select_page24
============================

.. c:function:: int ipr_ioafp_mode_select_page24(struct ipr_cmnd *ipr_cmd)

    Issue Mode Select to IOA

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_ioafp_mode_select_page24.description`:

Description
-----------

This function enables dual IOA RAID support if possible.

.. _`ipr_ioafp_mode_select_page24.return-value`:

Return value
------------

IPR_RC_JOB_RETURN

.. _`ipr_reset_mode_sense_page24_failed`:

ipr_reset_mode_sense_page24_failed
==================================

.. c:function:: int ipr_reset_mode_sense_page24_failed(struct ipr_cmnd *ipr_cmd)

    Handle failure of IOAFP mode sense

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reset_mode_sense_page24_failed.description`:

Description
-----------

This function handles the failure of a Mode Sense to the IOAFP.
Some adapters do not handle all mode pages.

.. _`ipr_reset_mode_sense_page24_failed.return-value`:

Return value
------------

IPR_RC_JOB_CONTINUE / IPR_RC_JOB_RETURN

.. _`ipr_ioafp_mode_sense_page24`:

ipr_ioafp_mode_sense_page24
===========================

.. c:function:: int ipr_ioafp_mode_sense_page24(struct ipr_cmnd *ipr_cmd)

    Issue Page 24 Mode Sense to IOA

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_ioafp_mode_sense_page24.description`:

Description
-----------

This function send a mode sense to the IOA to retrieve
the IOA Advanced Function Control mode page.

.. _`ipr_ioafp_mode_sense_page24.return-value`:

Return value
------------

IPR_RC_JOB_RETURN

.. _`ipr_init_res_table`:

ipr_init_res_table
==================

.. c:function:: int ipr_init_res_table(struct ipr_cmnd *ipr_cmd)

    Initialize the resource table

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_init_res_table.description`:

Description
-----------

This function looks through the existing resource table, comparing
it with the config table. This function will take care of old/new
devices and schedule adding/removing them from the mid-layer
as appropriate.

.. _`ipr_init_res_table.return-value`:

Return value
------------

IPR_RC_JOB_CONTINUE

.. _`ipr_ioafp_query_ioa_cfg`:

ipr_ioafp_query_ioa_cfg
=======================

.. c:function:: int ipr_ioafp_query_ioa_cfg(struct ipr_cmnd *ipr_cmd)

    Send a Query IOA Config to the adapter.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_ioafp_query_ioa_cfg.description`:

Description
-----------

This function sends a Query IOA Configuration command
to the adapter to retrieve the IOA configuration table.

.. _`ipr_ioafp_query_ioa_cfg.return-value`:

Return value
------------

IPR_RC_JOB_RETURN

.. _`ipr_ioafp_set_caching_parameters`:

ipr_ioafp_set_caching_parameters
================================

.. c:function:: int ipr_ioafp_set_caching_parameters(struct ipr_cmnd *ipr_cmd)

    Issue Set Cache parameters service action

    :param ipr_cmd:
        *undescribed*
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_ioafp_set_caching_parameters.return-value`:

Return value
------------

none

.. _`ipr_ioafp_inquiry`:

ipr_ioafp_inquiry
=================

.. c:function:: void ipr_ioafp_inquiry(struct ipr_cmnd *ipr_cmd, u8 flags, u8 page, dma_addr_t dma_addr, u8 xfer_len)

    Send an Inquiry to the adapter.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

    :param flags:
        *undescribed*
    :type flags: u8

    :param page:
        *undescribed*
    :type page: u8

    :param dma_addr:
        *undescribed*
    :type dma_addr: dma_addr_t

    :param xfer_len:
        *undescribed*
    :type xfer_len: u8

.. _`ipr_ioafp_inquiry.description`:

Description
-----------

This utility function sends an inquiry to the adapter.

.. _`ipr_ioafp_inquiry.return-value`:

Return value
------------

none

.. _`ipr_inquiry_page_supported`:

ipr_inquiry_page_supported
==========================

.. c:function:: int ipr_inquiry_page_supported(struct ipr_inquiry_page0 *page0, u8 page)

    Is the given inquiry page supported

    :param page0:
        inquiry page 0 buffer
    :type page0: struct ipr_inquiry_page0 \*

    :param page:
        page code.
    :type page: u8

.. _`ipr_inquiry_page_supported.description`:

Description
-----------

This function determines if the specified inquiry page is supported.

.. _`ipr_inquiry_page_supported.return-value`:

Return value
------------

1 if page is supported / 0 if not

.. _`ipr_ioafp_pagec4_inquiry`:

ipr_ioafp_pageC4_inquiry
========================

.. c:function:: int ipr_ioafp_pageC4_inquiry(struct ipr_cmnd *ipr_cmd)

    Send a Page 0xC4 Inquiry to the adapter.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_ioafp_pagec4_inquiry.description`:

Description
-----------

This function sends a Page 0xC4 inquiry to the adapter
to retrieve software VPD information.

.. _`ipr_ioafp_pagec4_inquiry.return-value`:

Return value
------------

IPR_RC_JOB_CONTINUE / IPR_RC_JOB_RETURN

.. _`ipr_ioafp_cap_inquiry`:

ipr_ioafp_cap_inquiry
=====================

.. c:function:: int ipr_ioafp_cap_inquiry(struct ipr_cmnd *ipr_cmd)

    Send a Page 0xD0 Inquiry to the adapter.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_ioafp_cap_inquiry.description`:

Description
-----------

This function sends a Page 0xD0 inquiry to the adapter
to retrieve adapter capabilities.

.. _`ipr_ioafp_cap_inquiry.return-value`:

Return value
------------

IPR_RC_JOB_CONTINUE / IPR_RC_JOB_RETURN

.. _`ipr_ioafp_page3_inquiry`:

ipr_ioafp_page3_inquiry
=======================

.. c:function:: int ipr_ioafp_page3_inquiry(struct ipr_cmnd *ipr_cmd)

    Send a Page 3 Inquiry to the adapter.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_ioafp_page3_inquiry.description`:

Description
-----------

This function sends a Page 3 inquiry to the adapter
to retrieve software VPD information.

.. _`ipr_ioafp_page3_inquiry.return-value`:

Return value
------------

IPR_RC_JOB_CONTINUE / IPR_RC_JOB_RETURN

.. _`ipr_ioafp_page0_inquiry`:

ipr_ioafp_page0_inquiry
=======================

.. c:function:: int ipr_ioafp_page0_inquiry(struct ipr_cmnd *ipr_cmd)

    Send a Page 0 Inquiry to the adapter.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_ioafp_page0_inquiry.description`:

Description
-----------

This function sends a Page 0 inquiry to the adapter
to retrieve supported inquiry pages.

.. _`ipr_ioafp_page0_inquiry.return-value`:

Return value
------------

IPR_RC_JOB_CONTINUE / IPR_RC_JOB_RETURN

.. _`ipr_ioafp_std_inquiry`:

ipr_ioafp_std_inquiry
=====================

.. c:function:: int ipr_ioafp_std_inquiry(struct ipr_cmnd *ipr_cmd)

    Send a Standard Inquiry to the adapter.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_ioafp_std_inquiry.description`:

Description
-----------

This function sends a standard inquiry to the adapter.

.. _`ipr_ioafp_std_inquiry.return-value`:

Return value
------------

IPR_RC_JOB_RETURN

.. _`ipr_ioafp_identify_hrrq`:

ipr_ioafp_identify_hrrq
=======================

.. c:function:: int ipr_ioafp_identify_hrrq(struct ipr_cmnd *ipr_cmd)

    Send Identify Host RRQ.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_ioafp_identify_hrrq.description`:

Description
-----------

This function send an Identify Host Request Response Queue
command to establish the HRRQ with the adapter.

.. _`ipr_ioafp_identify_hrrq.return-value`:

Return value
------------

IPR_RC_JOB_RETURN

.. _`ipr_reset_timer_done`:

ipr_reset_timer_done
====================

.. c:function:: void ipr_reset_timer_done(struct timer_list *t)

    Adapter reset timer function

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`ipr_reset_timer_done.description`:

Description
-----------

This function is used in adapter reset processing
for timing events. If the reset_cmd pointer in the IOA
config struct is not this adapter's we are doing nested
resets and fail_all_ops will take care of freeing the
command block.

.. _`ipr_reset_timer_done.return-value`:

Return value
------------

none

.. _`ipr_reset_start_timer`:

ipr_reset_start_timer
=====================

.. c:function:: void ipr_reset_start_timer(struct ipr_cmnd *ipr_cmd, unsigned long timeout)

    Start a timer for adapter reset job

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

    :param timeout:
        timeout value
    :type timeout: unsigned long

.. _`ipr_reset_start_timer.description`:

Description
-----------

This function is used in adapter reset processing
for timing events. If the reset_cmd pointer in the IOA
config struct is not this adapter's we are doing nested
resets and fail_all_ops will take care of freeing the
command block.

.. _`ipr_reset_start_timer.return-value`:

Return value
------------

none

.. _`ipr_init_ioa_mem`:

ipr_init_ioa_mem
================

.. c:function:: void ipr_init_ioa_mem(struct ipr_ioa_cfg *ioa_cfg)

    Initialize ioa_cfg control block

    :param ioa_cfg:
        ioa cfg struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

.. _`ipr_init_ioa_mem.return-value`:

Return value
------------

nothing

.. _`ipr_reset_next_stage`:

ipr_reset_next_stage
====================

.. c:function:: int ipr_reset_next_stage(struct ipr_cmnd *ipr_cmd)

    Process IPL stage change based on feedback register.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reset_next_stage.return-value`:

Return value
------------

IPR_RC_JOB_CONTINUE / IPR_RC_JOB_RETURN

.. _`ipr_reset_enable_ioa`:

ipr_reset_enable_ioa
====================

.. c:function:: int ipr_reset_enable_ioa(struct ipr_cmnd *ipr_cmd)

    Enable the IOA following a reset.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reset_enable_ioa.description`:

Description
-----------

This function reinitializes some control blocks and
enables destructive diagnostics on the adapter.

.. _`ipr_reset_enable_ioa.return-value`:

Return value
------------

IPR_RC_JOB_RETURN

.. _`ipr_reset_wait_for_dump`:

ipr_reset_wait_for_dump
=======================

.. c:function:: int ipr_reset_wait_for_dump(struct ipr_cmnd *ipr_cmd)

    Wait for a dump to timeout.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reset_wait_for_dump.description`:

Description
-----------

This function is invoked when an adapter dump has run out
of processing time.

.. _`ipr_reset_wait_for_dump.return-value`:

Return value
------------

IPR_RC_JOB_CONTINUE

.. _`ipr_unit_check_no_data`:

ipr_unit_check_no_data
======================

.. c:function:: void ipr_unit_check_no_data(struct ipr_ioa_cfg *ioa_cfg)

    Log a unit check/no data error log

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

.. _`ipr_unit_check_no_data.description`:

Description
-----------

Logs an error indicating the adapter unit checked, but for some
reason, we were unable to fetch the unit check buffer.

.. _`ipr_unit_check_no_data.return-value`:

Return value
------------

nothing

.. _`ipr_get_unit_check_buffer`:

ipr_get_unit_check_buffer
=========================

.. c:function:: void ipr_get_unit_check_buffer(struct ipr_ioa_cfg *ioa_cfg)

    Get the unit check buffer from the IOA

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

.. _`ipr_get_unit_check_buffer.description`:

Description
-----------

Fetches the unit check buffer from the adapter by clocking the data
through the mailbox register.

.. _`ipr_get_unit_check_buffer.return-value`:

Return value
------------

nothing

.. _`ipr_reset_get_unit_check_job`:

ipr_reset_get_unit_check_job
============================

.. c:function:: int ipr_reset_get_unit_check_job(struct ipr_cmnd *ipr_cmd)

    Call to get the unit check buffer.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reset_get_unit_check_job.description`:

Description
-----------

This function will call to get the unit check buffer.

.. _`ipr_reset_get_unit_check_job.return-value`:

Return value
------------

IPR_RC_JOB_RETURN

.. _`ipr_reset_restore_cfg_space`:

ipr_reset_restore_cfg_space
===========================

.. c:function:: int ipr_reset_restore_cfg_space(struct ipr_cmnd *ipr_cmd)

    Restore PCI config space.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reset_restore_cfg_space.description`:

Description
-----------

This function restores the saved PCI config space of
the adapter, fails all outstanding ops back to the callers, and
fetches the dump/unit check if applicable to this reset.

.. _`ipr_reset_restore_cfg_space.return-value`:

Return value
------------

IPR_RC_JOB_CONTINUE / IPR_RC_JOB_RETURN

.. _`ipr_reset_bist_done`:

ipr_reset_bist_done
===================

.. c:function:: int ipr_reset_bist_done(struct ipr_cmnd *ipr_cmd)

    BIST has completed on the adapter.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reset_bist_done.description`:

Description
-----------

Unblock config space and resume the reset process.

.. _`ipr_reset_bist_done.return-value`:

Return value
------------

IPR_RC_JOB_CONTINUE

.. _`ipr_reset_start_bist`:

ipr_reset_start_bist
====================

.. c:function:: int ipr_reset_start_bist(struct ipr_cmnd *ipr_cmd)

    Run BIST on the adapter.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reset_start_bist.description`:

Description
-----------

This function runs BIST on the adapter, then delays 2 seconds.

.. _`ipr_reset_start_bist.return-value`:

Return value
------------

IPR_RC_JOB_CONTINUE / IPR_RC_JOB_RETURN

.. _`ipr_reset_slot_reset_done`:

ipr_reset_slot_reset_done
=========================

.. c:function:: int ipr_reset_slot_reset_done(struct ipr_cmnd *ipr_cmd)

    Clear PCI reset to the adapter

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reset_slot_reset_done.description`:

Description
-----------

This clears PCI reset to the adapter and delays two seconds.

.. _`ipr_reset_slot_reset_done.return-value`:

Return value
------------

IPR_RC_JOB_RETURN

.. _`ipr_reset_reset_work`:

ipr_reset_reset_work
====================

.. c:function:: void ipr_reset_reset_work(struct work_struct *work)

    Pulse a PCIe fundamental reset

    :param work:
        work struct
    :type work: struct work_struct \*

.. _`ipr_reset_reset_work.description`:

Description
-----------

This pulses warm reset to a slot.

.. _`ipr_reset_slot_reset`:

ipr_reset_slot_reset
====================

.. c:function:: int ipr_reset_slot_reset(struct ipr_cmnd *ipr_cmd)

    Reset the PCI slot of the adapter.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reset_slot_reset.description`:

Description
-----------

This asserts PCI reset to the adapter.

.. _`ipr_reset_slot_reset.return-value`:

Return value
------------

IPR_RC_JOB_RETURN

.. _`ipr_reset_block_config_access_wait`:

ipr_reset_block_config_access_wait
==================================

.. c:function:: int ipr_reset_block_config_access_wait(struct ipr_cmnd *ipr_cmd)

    Wait for permission to block config access

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reset_block_config_access_wait.description`:

Description
-----------

This attempts to block config access to the IOA.

.. _`ipr_reset_block_config_access_wait.return-value`:

Return value
------------

IPR_RC_JOB_CONTINUE / IPR_RC_JOB_RETURN

.. _`ipr_reset_block_config_access`:

ipr_reset_block_config_access
=============================

.. c:function:: int ipr_reset_block_config_access(struct ipr_cmnd *ipr_cmd)

    Block config access to the IOA

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reset_block_config_access.description`:

Description
-----------

This attempts to block config access to the IOA

.. _`ipr_reset_block_config_access.return-value`:

Return value
------------

IPR_RC_JOB_CONTINUE

.. _`ipr_reset_allowed`:

ipr_reset_allowed
=================

.. c:function:: int ipr_reset_allowed(struct ipr_ioa_cfg *ioa_cfg)

    Query whether or not IOA can be reset

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

.. _`ipr_reset_allowed.return-value`:

Return value
------------

0 if reset not allowed / non-zero if reset is allowed

.. _`ipr_reset_wait_to_start_bist`:

ipr_reset_wait_to_start_bist
============================

.. c:function:: int ipr_reset_wait_to_start_bist(struct ipr_cmnd *ipr_cmd)

    Wait for permission to reset IOA.

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reset_wait_to_start_bist.description`:

Description
-----------

This function waits for adapter permission to run BIST,
then runs BIST. If the adapter does not give permission after a
reasonable time, we will reset the adapter anyway. The impact of
resetting the adapter without warning the adapter is the risk of
losing the persistent error log on the adapter. If the adapter is
reset while it is writing to the flash on the adapter, the flash
segment will have bad ECC and be zeroed.

.. _`ipr_reset_wait_to_start_bist.return-value`:

Return value
------------

IPR_RC_JOB_CONTINUE / IPR_RC_JOB_RETURN

.. _`ipr_reset_alert`:

ipr_reset_alert
===============

.. c:function:: int ipr_reset_alert(struct ipr_cmnd *ipr_cmd)

    Alert the adapter of a pending reset

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reset_alert.description`:

Description
-----------

This function alerts the adapter that it will be reset.
If memory space is not currently enabled, proceed directly
to running BIST on the adapter. The timer must always be started
so we guarantee we do not run BIST from ipr_isr.

.. _`ipr_reset_alert.return-value`:

Return value
------------

IPR_RC_JOB_RETURN

.. _`ipr_reset_quiesce_done`:

ipr_reset_quiesce_done
======================

.. c:function:: int ipr_reset_quiesce_done(struct ipr_cmnd *ipr_cmd)

    Complete IOA disconnect

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reset_quiesce_done.description`:

Description
-----------

Freeze the adapter to complete quiesce processing

.. _`ipr_reset_quiesce_done.return-value`:

Return value
------------

IPR_RC_JOB_CONTINUE

.. _`ipr_reset_cancel_hcam_done`:

ipr_reset_cancel_hcam_done
==========================

.. c:function:: int ipr_reset_cancel_hcam_done(struct ipr_cmnd *ipr_cmd)

    Check for outstanding commands

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reset_cancel_hcam_done.description`:

Description
-----------

Ensure nothing is outstanding to the IOA and
proceed with IOA disconnect. Otherwise reset the IOA.

.. _`ipr_reset_cancel_hcam_done.return-value`:

Return value
------------

IPR_RC_JOB_RETURN / IPR_RC_JOB_CONTINUE

.. _`ipr_reset_cancel_hcam`:

ipr_reset_cancel_hcam
=====================

.. c:function:: int ipr_reset_cancel_hcam(struct ipr_cmnd *ipr_cmd)

    Cancel outstanding HCAMs

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reset_cancel_hcam.description`:

Description
-----------

Cancel any oustanding HCAMs to the IOA.

.. _`ipr_reset_cancel_hcam.return-value`:

Return value
------------

IPR_RC_JOB_CONTINUE / IPR_RC_JOB_RETURN

.. _`ipr_reset_ucode_download_done`:

ipr_reset_ucode_download_done
=============================

.. c:function:: int ipr_reset_ucode_download_done(struct ipr_cmnd *ipr_cmd)

    Microcode download completion

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reset_ucode_download_done.description`:

Description
-----------

This function unmaps the microcode download buffer.

.. _`ipr_reset_ucode_download_done.return-value`:

Return value
------------

IPR_RC_JOB_CONTINUE

.. _`ipr_reset_ucode_download`:

ipr_reset_ucode_download
========================

.. c:function:: int ipr_reset_ucode_download(struct ipr_cmnd *ipr_cmd)

    Download microcode to the adapter

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reset_ucode_download.description`:

Description
-----------

This function checks to see if it there is microcode
to download to the adapter. If there is, a download is performed.

.. _`ipr_reset_ucode_download.return-value`:

Return value
------------

IPR_RC_JOB_CONTINUE / IPR_RC_JOB_RETURN

.. _`ipr_reset_shutdown_ioa`:

ipr_reset_shutdown_ioa
======================

.. c:function:: int ipr_reset_shutdown_ioa(struct ipr_cmnd *ipr_cmd)

    Shutdown the adapter

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reset_shutdown_ioa.description`:

Description
-----------

This function issues an adapter shutdown of the
specified type to the specified adapter as part of the
adapter reset job.

.. _`ipr_reset_shutdown_ioa.return-value`:

Return value
------------

IPR_RC_JOB_CONTINUE / IPR_RC_JOB_RETURN

.. _`ipr_reset_ioa_job`:

ipr_reset_ioa_job
=================

.. c:function:: void ipr_reset_ioa_job(struct ipr_cmnd *ipr_cmd)

    Adapter reset job

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reset_ioa_job.description`:

Description
-----------

This function is the job router for the adapter reset job.

.. _`ipr_reset_ioa_job.return-value`:

Return value
------------

none

.. _`_ipr_initiate_ioa_reset`:

\_ipr_initiate_ioa_reset
========================

.. c:function:: void _ipr_initiate_ioa_reset(struct ipr_ioa_cfg *ioa_cfg, int (*job_step)(struct ipr_cmnd *), enum ipr_shutdown_type shutdown_type)

    Initiate an adapter reset

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param int (\*job_step)(struct ipr_cmnd \*):
        first job step of reset job

    :param shutdown_type:
        shutdown type
    :type shutdown_type: enum ipr_shutdown_type

.. _`_ipr_initiate_ioa_reset.description`:

Description
-----------

This function will initiate the reset of the given adapter
starting at the selected job step.
If the caller needs to wait on the completion of the reset,
the caller must sleep on the reset_wait_q.

.. _`_ipr_initiate_ioa_reset.return-value`:

Return value
------------

none

.. _`ipr_initiate_ioa_reset`:

ipr_initiate_ioa_reset
======================

.. c:function:: void ipr_initiate_ioa_reset(struct ipr_ioa_cfg *ioa_cfg, enum ipr_shutdown_type shutdown_type)

    Initiate an adapter reset

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param shutdown_type:
        shutdown type
    :type shutdown_type: enum ipr_shutdown_type

.. _`ipr_initiate_ioa_reset.description`:

Description
-----------

This function will initiate the reset of the given adapter.
If the caller needs to wait on the completion of the reset,
the caller must sleep on the reset_wait_q.

.. _`ipr_initiate_ioa_reset.return-value`:

Return value
------------

none

.. _`ipr_reset_freeze`:

ipr_reset_freeze
================

.. c:function:: int ipr_reset_freeze(struct ipr_cmnd *ipr_cmd)

    Hold off all I/O activity

    :param ipr_cmd:
        ipr command struct
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_reset_freeze.description`:

Description
-----------

If the PCI slot is frozen, hold off all I/O
activity; then, as soon as the slot is available again,
initiate an adapter reset.

.. _`ipr_pci_mmio_enabled`:

ipr_pci_mmio_enabled
====================

.. c:function:: pci_ers_result_t ipr_pci_mmio_enabled(struct pci_dev *pdev)

    Called when MMIO has been re-enabled

    :param pdev:
        PCI device struct
    :type pdev: struct pci_dev \*

.. _`ipr_pci_mmio_enabled.description`:

Description
-----------

This routine is called to tell us that the MMIO
access to the IOA has been restored

.. _`ipr_pci_frozen`:

ipr_pci_frozen
==============

.. c:function:: void ipr_pci_frozen(struct pci_dev *pdev)

    Called when slot has experienced a PCI bus error.

    :param pdev:
        PCI device struct
    :type pdev: struct pci_dev \*

.. _`ipr_pci_frozen.description`:

Description
-----------

This routine is called to tell us that the PCI bus
is down. Can't do anything here, except put the device driver
into a holding pattern, waiting for the PCI bus to come back.

.. _`ipr_pci_slot_reset`:

ipr_pci_slot_reset
==================

.. c:function:: pci_ers_result_t ipr_pci_slot_reset(struct pci_dev *pdev)

    Called when PCI slot has been reset.

    :param pdev:
        PCI device struct
    :type pdev: struct pci_dev \*

.. _`ipr_pci_slot_reset.description`:

Description
-----------

This routine is called by the pci error recovery
code after the PCI slot has been reset, just before we
should resume normal operations.

.. _`ipr_pci_perm_failure`:

ipr_pci_perm_failure
====================

.. c:function:: void ipr_pci_perm_failure(struct pci_dev *pdev)

    Called when PCI slot is dead for good.

    :param pdev:
        PCI device struct
    :type pdev: struct pci_dev \*

.. _`ipr_pci_perm_failure.description`:

Description
-----------

This routine is called when the PCI bus has
permanently failed.

.. _`ipr_pci_error_detected`:

ipr_pci_error_detected
======================

.. c:function:: pci_ers_result_t ipr_pci_error_detected(struct pci_dev *pdev, pci_channel_state_t state)

    Called when a PCI error is detected.

    :param pdev:
        PCI device struct
    :type pdev: struct pci_dev \*

    :param state:
        PCI channel state
    :type state: pci_channel_state_t

.. _`ipr_pci_error_detected.description`:

Description
-----------

Called when a PCI error is detected.

.. _`ipr_pci_error_detected.return-value`:

Return value
------------

PCI_ERS_RESULT_NEED_RESET or PCI_ERS_RESULT_DISCONNECT

.. _`ipr_probe_ioa_part2`:

ipr_probe_ioa_part2
===================

.. c:function:: int ipr_probe_ioa_part2(struct ipr_ioa_cfg *ioa_cfg)

    Initializes IOAs found in ipr_probe_ioa(..)

    :param ioa_cfg:
        ioa cfg struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

.. _`ipr_probe_ioa_part2.description`:

Description
-----------

This is the second phase of adapter initialization
This function takes care of initilizing the adapter to the point
where it can accept new commands.

.. _`ipr_probe_ioa_part2.return-value`:

Return value
------------

0 on success / -EIO on failure

.. _`ipr_free_cmd_blks`:

ipr_free_cmd_blks
=================

.. c:function:: void ipr_free_cmd_blks(struct ipr_ioa_cfg *ioa_cfg)

    Frees command blocks allocated for an adapter

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

.. _`ipr_free_cmd_blks.return-value`:

Return value
------------

none

.. _`ipr_free_mem`:

ipr_free_mem
============

.. c:function:: void ipr_free_mem(struct ipr_ioa_cfg *ioa_cfg)

    Frees memory allocated for an adapter

    :param ioa_cfg:
        ioa cfg struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

.. _`ipr_free_mem.return-value`:

Return value
------------

nothing

.. _`ipr_free_irqs`:

ipr_free_irqs
=============

.. c:function:: void ipr_free_irqs(struct ipr_ioa_cfg *ioa_cfg)

    Free all allocated IRQs for the adapter.

    :param ioa_cfg:
        ipr cfg struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

.. _`ipr_free_irqs.description`:

Description
-----------

This function frees all allocated IRQs for the
specified adapter.

.. _`ipr_free_irqs.return-value`:

Return value
------------

none

.. _`ipr_free_all_resources`:

ipr_free_all_resources
======================

.. c:function:: void ipr_free_all_resources(struct ipr_ioa_cfg *ioa_cfg)

    Free all allocated resources for an adapter.

    :param ioa_cfg:
        *undescribed*
    :type ioa_cfg: struct ipr_ioa_cfg \*

.. _`ipr_free_all_resources.description`:

Description
-----------

This function frees all allocated resources for the
specified adapter.

.. _`ipr_free_all_resources.return-value`:

Return value
------------

none

.. _`ipr_alloc_cmd_blks`:

ipr_alloc_cmd_blks
==================

.. c:function:: int ipr_alloc_cmd_blks(struct ipr_ioa_cfg *ioa_cfg)

    Allocate command blocks for an adapter

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

.. _`ipr_alloc_cmd_blks.return-value`:

Return value
------------

0 on success / -ENOMEM on allocation failure

.. _`ipr_alloc_mem`:

ipr_alloc_mem
=============

.. c:function:: int ipr_alloc_mem(struct ipr_ioa_cfg *ioa_cfg)

    Allocate memory for an adapter

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

.. _`ipr_alloc_mem.return-value`:

Return value
------------

0 on success / non-zero for error

.. _`ipr_initialize_bus_attr`:

ipr_initialize_bus_attr
=======================

.. c:function:: void ipr_initialize_bus_attr(struct ipr_ioa_cfg *ioa_cfg)

    Initialize SCSI bus attributes to default values

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

.. _`ipr_initialize_bus_attr.return-value`:

Return value
------------

none

.. _`ipr_init_regs`:

ipr_init_regs
=============

.. c:function:: void ipr_init_regs(struct ipr_ioa_cfg *ioa_cfg)

    Initialize IOA registers

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

.. _`ipr_init_regs.return-value`:

Return value
------------

none

.. _`ipr_init_ioa_cfg`:

ipr_init_ioa_cfg
================

.. c:function:: void ipr_init_ioa_cfg(struct ipr_ioa_cfg *ioa_cfg, struct Scsi_Host *host, struct pci_dev *pdev)

    Initialize IOA config struct

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param host:
        scsi host struct
    :type host: struct Scsi_Host \*

    :param pdev:
        PCI dev struct
    :type pdev: struct pci_dev \*

.. _`ipr_init_ioa_cfg.return-value`:

Return value
------------

none

.. _`ipr_get_chip_info`:

ipr_get_chip_info
=================

.. c:function:: const struct ipr_chip_t *ipr_get_chip_info(const struct pci_device_id *dev_id)

    Find adapter chip information

    :param dev_id:
        PCI device id struct
    :type dev_id: const struct pci_device_id \*

.. _`ipr_get_chip_info.return-value`:

Return value
------------

ptr to chip information on success / NULL on failure

.. _`ipr_wait_for_pci_err_recovery`:

ipr_wait_for_pci_err_recovery
=============================

.. c:function:: void ipr_wait_for_pci_err_recovery(struct ipr_ioa_cfg *ioa_cfg)

    Wait for any PCI error recovery to complete during probe time

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

.. _`ipr_wait_for_pci_err_recovery.return-value`:

Return value
------------

None

.. _`ipr_test_intr`:

ipr_test_intr
=============

.. c:function:: irqreturn_t ipr_test_intr(int irq, void *devp)

    Handle the interrupt generated in \ :c:func:`ipr_test_msi`\ .

    :param irq:
        *undescribed*
    :type irq: int

    :param devp:
        *undescribed*
    :type devp: void \*

.. _`ipr_test_intr.description`:

Description
-----------

Simply set the msi_received flag to 1 indicating that
Message Signaled Interrupts are supported.

.. _`ipr_test_intr.return-value`:

Return value
------------

0 on success / non-zero on failure

.. _`ipr_test_msi`:

ipr_test_msi
============

.. c:function:: int ipr_test_msi(struct ipr_ioa_cfg *ioa_cfg, struct pci_dev *pdev)

    Test for Message Signaled Interrupt (MSI) support.

    :param ioa_cfg:
        *undescribed*
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param pdev:
        PCI device struct
    :type pdev: struct pci_dev \*

.. _`ipr_test_msi.description`:

Description
-----------

This routine sets up and initiates a test interrupt to determine
if the interrupt is received via the \ :c:func:`ipr_test_intr`\  service routine.
If the tests fails, the driver will fall back to LSI.

.. _`ipr_test_msi.return-value`:

Return value
------------

0 on success / non-zero on failure

.. _`ipr_initiate_ioa_bringdown`:

ipr_initiate_ioa_bringdown
==========================

.. c:function:: void ipr_initiate_ioa_bringdown(struct ipr_ioa_cfg *ioa_cfg, enum ipr_shutdown_type shutdown_type)

    Bring down an adapter

    :param ioa_cfg:
        ioa config struct
    :type ioa_cfg: struct ipr_ioa_cfg \*

    :param shutdown_type:
        shutdown type
    :type shutdown_type: enum ipr_shutdown_type

.. _`ipr_initiate_ioa_bringdown.description`:

Description
-----------

This function will initiate bringing down the adapter.
This consists of issuing an IOA shutdown to the adapter
to flush the cache, and running BIST.
If the caller needs to wait on the completion of the reset,
the caller must sleep on the reset_wait_q.

.. _`ipr_initiate_ioa_bringdown.return-value`:

Return value
------------

none

.. _`__ipr_remove`:

\__ipr_remove
=============

.. c:function:: void __ipr_remove(struct pci_dev *pdev)

    Remove a single adapter

    :param pdev:
        pci device struct
    :type pdev: struct pci_dev \*

.. _`__ipr_remove.description`:

Description
-----------

Adapter hot plug remove entry point.

.. _`__ipr_remove.return-value`:

Return value
------------

none

.. _`ipr_remove`:

ipr_remove
==========

.. c:function:: void ipr_remove(struct pci_dev *pdev)

    IOA hot plug remove entry point

    :param pdev:
        pci device struct
    :type pdev: struct pci_dev \*

.. _`ipr_remove.description`:

Description
-----------

Adapter hot plug remove entry point.

.. _`ipr_remove.return-value`:

Return value
------------

none

.. _`ipr_probe`:

ipr_probe
=========

.. c:function:: int ipr_probe(struct pci_dev *pdev, const struct pci_device_id *dev_id)

    Adapter hot plug add entry point

    :param pdev:
        *undescribed*
    :type pdev: struct pci_dev \*

    :param dev_id:
        *undescribed*
    :type dev_id: const struct pci_device_id \*

.. _`ipr_probe.return-value`:

Return value
------------

0 on success / non-zero on failure

.. _`ipr_shutdown`:

ipr_shutdown
============

.. c:function:: void ipr_shutdown(struct pci_dev *pdev)

    Shutdown handler.

    :param pdev:
        pci device struct
    :type pdev: struct pci_dev \*

.. _`ipr_shutdown.description`:

Description
-----------

This function is invoked upon system shutdown/reboot. It will issue
an adapter shutdown to the adapter to flush the write cache.

.. _`ipr_shutdown.return-value`:

Return value
------------

none

.. _`ipr_halt_done`:

ipr_halt_done
=============

.. c:function:: void ipr_halt_done(struct ipr_cmnd *ipr_cmd)

    Shutdown prepare completion

    :param ipr_cmd:
        *undescribed*
    :type ipr_cmd: struct ipr_cmnd \*

.. _`ipr_halt_done.return-value`:

Return value
------------

none

.. _`ipr_halt`:

ipr_halt
========

.. c:function:: int ipr_halt(struct notifier_block *nb, ulong event, void *buf)

    Issue shutdown prepare to all adapters

    :param nb:
        *undescribed*
    :type nb: struct notifier_block \*

    :param event:
        *undescribed*
    :type event: ulong

    :param buf:
        *undescribed*
    :type buf: void \*

.. _`ipr_halt.return-value`:

Return value
------------

NOTIFY_OK on success / NOTIFY_DONE on failure

.. _`ipr_init`:

ipr_init
========

.. c:function:: int ipr_init( void)

    Module entry point

    :param void:
        no arguments
    :type void: 

.. _`ipr_init.return-value`:

Return value
------------

0 on success / negative value on failure

.. _`ipr_exit`:

ipr_exit
========

.. c:function:: void __exit ipr_exit( void)

    Module unload

    :param void:
        no arguments
    :type void: 

.. _`ipr_exit.description`:

Description
-----------

Module unload entry point.

.. _`ipr_exit.return-value`:

Return value
------------

none

.. This file was automatic generated / don't edit.

