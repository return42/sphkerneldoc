.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/mpt3sas/mpt3sas_ctl.c

.. _`block_state`:

enum block_state
================

.. c:type:: enum block_state

    blocking state

.. _`block_state.definition`:

Definition
----------

.. code-block:: c

    enum block_state {
        NON_BLOCKING,
        BLOCKING
    };

.. _`block_state.constants`:

Constants
---------

NON_BLOCKING
    non blocking

BLOCKING
    blocking

.. _`block_state.description`:

Description
-----------

These states are for ioctls that need to wait for a response
from firmware, so they probably require sleep.

.. _`_ctl_display_some_debug`:

\_ctl_display_some_debug
========================

.. c:function:: void _ctl_display_some_debug(struct MPT3SAS_ADAPTER *ioc, u16 smid, char *calling_function_name, MPI2DefaultReply_t *mpi_reply)

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

.. _`_ctl_display_some_debug.context`:

Context
-------

none.

.. _`_ctl_display_some_debug.description`:

Description
-----------

Function for displaying debug info helpful when debugging issues
in this module.

.. _`mpt3sas_ctl_done`:

mpt3sas_ctl_done
================

.. c:function:: u8 mpt3sas_ctl_done(struct MPT3SAS_ADAPTER *ioc, u16 smid, u8 msix_index, u32 reply)

    ctl module completion routine

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

.. _`mpt3sas_ctl_done.context`:

Context
-------

none.

.. _`mpt3sas_ctl_done.description`:

Description
-----------

The callback handler when using ioc->ctl_cb_idx.

.. _`mpt3sas_ctl_done.return`:

Return
------

1 meaning mf should be freed from \_base_interrupt
0 means the mf is freed from this function.

.. _`_ctl_check_event_type`:

\_ctl_check_event_type
======================

.. c:function:: int _ctl_check_event_type(struct MPT3SAS_ADAPTER *ioc, u16 event)

    determines when an event needs logging

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param event:
        firmware event
    :type event: u16

.. _`_ctl_check_event_type.description`:

Description
-----------

The bitmask in ioc->event_type[] indicates which events should be
be saved in the driver event_log.  This bitmask is set by application.

.. _`_ctl_check_event_type.return`:

Return
------

1 when event should be captured, or zero means no match.

.. _`mpt3sas_ctl_add_to_event_log`:

mpt3sas_ctl_add_to_event_log
============================

.. c:function:: void mpt3sas_ctl_add_to_event_log(struct MPT3SAS_ADAPTER *ioc, Mpi2EventNotificationReply_t *mpi_reply)

    add event

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param mpi_reply:
        reply message frame
    :type mpi_reply: Mpi2EventNotificationReply_t \*

.. _`mpt3sas_ctl_event_callback`:

mpt3sas_ctl_event_callback
==========================

.. c:function:: u8 mpt3sas_ctl_event_callback(struct MPT3SAS_ADAPTER *ioc, u8 msix_index, u32 reply)

    firmware event handler (called at ISR time)

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param msix_index:
        MSIX table index supplied by the OS
    :type msix_index: u8

    :param reply:
        reply message frame(lower 32bit addr)
    :type reply: u32

.. _`mpt3sas_ctl_event_callback.context`:

Context
-------

interrupt.

.. _`mpt3sas_ctl_event_callback.description`:

Description
-----------

This function merely adds a new work task into ioc->firmware_event_thread.
The tasks are worked from \_firmware_event_work in user context.

.. _`mpt3sas_ctl_event_callback.return`:

Return
------

1 meaning mf should be freed from \_base_interrupt
0 means the mf is freed from this function.

.. _`_ctl_verify_adapter`:

\_ctl_verify_adapter
====================

.. c:function:: int _ctl_verify_adapter(int ioc_number, struct MPT3SAS_ADAPTER **iocpp, int mpi_version)

    validates ioc_number passed from application

    :param ioc_number:
        ?
    :type ioc_number: int

    :param iocpp:
        The ioc pointer is returned in this.
    :type iocpp: struct MPT3SAS_ADAPTER \*\*

    :param mpi_version:
        will be MPI2_VERSION for mpt2ctl ioctl device &
        MPI25_VERSION \| MPI26_VERSION for mpt3ctl ioctl device.
    :type mpi_version: int

.. _`_ctl_verify_adapter.return`:

Return
------

(-1) means error, else ioc_number.

.. _`mpt3sas_ctl_pre_reset_handler`:

mpt3sas_ctl_pre_reset_handler
=============================

.. c:function:: void mpt3sas_ctl_pre_reset_handler(struct MPT3SAS_ADAPTER *ioc)

    reset callback handler (for ctl)

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`mpt3sas_ctl_pre_reset_handler.description`:

Description
-----------

The handler for doing any required cleanup or initialization.

.. _`mpt3sas_ctl_after_reset_handler`:

mpt3sas_ctl_after_reset_handler
===============================

.. c:function:: void mpt3sas_ctl_after_reset_handler(struct MPT3SAS_ADAPTER *ioc)

    reset callback handler (for ctl)

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`mpt3sas_ctl_after_reset_handler.description`:

Description
-----------

The handler for doing any required cleanup or initialization.

.. _`mpt3sas_ctl_reset_done_handler`:

mpt3sas_ctl_reset_done_handler
==============================

.. c:function:: void mpt3sas_ctl_reset_done_handler(struct MPT3SAS_ADAPTER *ioc)

    reset callback handler (for ctl)

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

.. _`mpt3sas_ctl_reset_done_handler.description`:

Description
-----------

The handler for doing any required cleanup or initialization.

.. _`_ctl_fasync`:

\_ctl_fasync
============

.. c:function:: int _ctl_fasync(int fd, struct file *filep, int mode)

    :param fd:
        ?
    :type fd: int

    :param filep:
        ?
    :type filep: struct file \*

    :param mode:
        ?
    :type mode: int

.. _`_ctl_fasync.description`:

Description
-----------

Called when application request fasyn callback handler.

.. _`_ctl_poll`:

\_ctl_poll
==========

.. c:function:: __poll_t _ctl_poll(struct file *filep, poll_table *wait)

    :param filep:
        ?
    :type filep: struct file \*

    :param wait:
        ?
    :type wait: poll_table \*

.. _`_ctl_set_task_mid`:

\_ctl_set_task_mid
==================

.. c:function:: int _ctl_set_task_mid(struct MPT3SAS_ADAPTER *ioc, struct mpt3_ioctl_command *karg, Mpi2SCSITaskManagementRequest_t *tm_request)

    assign an active smid to tm request

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param karg:
        (struct mpt3_ioctl_command)
    :type karg: struct mpt3_ioctl_command \*

    :param tm_request:
        pointer to mf from user space
    :type tm_request: Mpi2SCSITaskManagementRequest_t \*

.. _`_ctl_set_task_mid.return`:

Return
------

0 when an smid if found, else fail.
during failure, the reply frame is filled.

.. _`_ctl_do_mpt_command`:

\_ctl_do_mpt_command
====================

.. c:function:: long _ctl_do_mpt_command(struct MPT3SAS_ADAPTER *ioc, struct mpt3_ioctl_command karg, void __user *mf)

    main handler for MPT3COMMAND opcode

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param karg:
        (struct mpt3_ioctl_command)
    :type karg: struct mpt3_ioctl_command

    :param mf:
        pointer to mf in user space
    :type mf: void __user \*

.. _`_ctl_getiocinfo`:

\_ctl_getiocinfo
================

.. c:function:: long _ctl_getiocinfo(struct MPT3SAS_ADAPTER *ioc, void __user *arg)

    main handler for MPT3IOCINFO opcode

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param arg:
        user space buffer containing ioctl content
    :type arg: void __user \*

.. _`_ctl_eventquery`:

\_ctl_eventquery
================

.. c:function:: long _ctl_eventquery(struct MPT3SAS_ADAPTER *ioc, void __user *arg)

    main handler for MPT3EVENTQUERY opcode

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param arg:
        user space buffer containing ioctl content
    :type arg: void __user \*

.. _`_ctl_eventenable`:

\_ctl_eventenable
=================

.. c:function:: long _ctl_eventenable(struct MPT3SAS_ADAPTER *ioc, void __user *arg)

    main handler for MPT3EVENTENABLE opcode

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param arg:
        user space buffer containing ioctl content
    :type arg: void __user \*

.. _`_ctl_eventreport`:

\_ctl_eventreport
=================

.. c:function:: long _ctl_eventreport(struct MPT3SAS_ADAPTER *ioc, void __user *arg)

    main handler for MPT3EVENTREPORT opcode

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param arg:
        user space buffer containing ioctl content
    :type arg: void __user \*

.. _`_ctl_do_reset`:

\_ctl_do_reset
==============

.. c:function:: long _ctl_do_reset(struct MPT3SAS_ADAPTER *ioc, void __user *arg)

    main handler for MPT3HARDRESET opcode

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param arg:
        user space buffer containing ioctl content
    :type arg: void __user \*

.. _`_ctl_btdh_search_sas_device`:

\_ctl_btdh_search_sas_device
============================

.. c:function:: int _ctl_btdh_search_sas_device(struct MPT3SAS_ADAPTER *ioc, struct mpt3_ioctl_btdh_mapping *btdh)

    searching for sas device

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param btdh:
        btdh ioctl payload
    :type btdh: struct mpt3_ioctl_btdh_mapping \*

.. _`_ctl_btdh_search_pcie_device`:

\_ctl_btdh_search_pcie_device
=============================

.. c:function:: int _ctl_btdh_search_pcie_device(struct MPT3SAS_ADAPTER *ioc, struct mpt3_ioctl_btdh_mapping *btdh)

    searching for pcie device

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param btdh:
        btdh ioctl payload
    :type btdh: struct mpt3_ioctl_btdh_mapping \*

.. _`_ctl_btdh_search_raid_device`:

\_ctl_btdh_search_raid_device
=============================

.. c:function:: int _ctl_btdh_search_raid_device(struct MPT3SAS_ADAPTER *ioc, struct mpt3_ioctl_btdh_mapping *btdh)

    searching for raid device

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param btdh:
        btdh ioctl payload
    :type btdh: struct mpt3_ioctl_btdh_mapping \*

.. _`_ctl_btdh_mapping`:

\_ctl_btdh_mapping
==================

.. c:function:: long _ctl_btdh_mapping(struct MPT3SAS_ADAPTER *ioc, void __user *arg)

    main handler for MPT3BTDHMAPPING opcode

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param arg:
        user space buffer containing ioctl content
    :type arg: void __user \*

.. _`_ctl_diag_capability`:

\_ctl_diag_capability
=====================

.. c:function:: u8 _ctl_diag_capability(struct MPT3SAS_ADAPTER *ioc, u8 buffer_type)

    return diag buffer capability

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param buffer_type:
        specifies either TRACE, SNAPSHOT, or EXTENDED
    :type buffer_type: u8

.. _`_ctl_diag_capability.description`:

Description
-----------

returns 1 when diag buffer support is enabled in firmware

.. _`_ctl_diag_register_2`:

\_ctl_diag_register_2
=====================

.. c:function:: long _ctl_diag_register_2(struct MPT3SAS_ADAPTER *ioc, struct mpt3_diag_register *diag_register)

    wrapper for registering diag buffer support

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param diag_register:
        the diag_register struct passed in from user space
    :type diag_register: struct mpt3_diag_register \*

.. _`mpt3sas_enable_diag_buffer`:

mpt3sas_enable_diag_buffer
==========================

.. c:function:: void mpt3sas_enable_diag_buffer(struct MPT3SAS_ADAPTER *ioc, u8 bits_to_register)

    enabling diag_buffers support driver load time

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param bits_to_register:
        bitwise field where trace is bit 0, and snapshot is bit 1
    :type bits_to_register: u8

.. _`mpt3sas_enable_diag_buffer.description`:

Description
-----------

This is called when command line option diag_buffer_enable is enabled
at driver load time.

.. _`_ctl_diag_register`:

\_ctl_diag_register
===================

.. c:function:: long _ctl_diag_register(struct MPT3SAS_ADAPTER *ioc, void __user *arg)

    application register with driver

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param arg:
        user space buffer containing ioctl content
    :type arg: void __user \*

.. _`_ctl_diag_register.description`:

Description
-----------

This will allow the driver to setup any required buffers that will be
needed by firmware to communicate with the driver.

.. _`_ctl_diag_unregister`:

\_ctl_diag_unregister
=====================

.. c:function:: long _ctl_diag_unregister(struct MPT3SAS_ADAPTER *ioc, void __user *arg)

    application unregister with driver

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param arg:
        user space buffer containing ioctl content
    :type arg: void __user \*

.. _`_ctl_diag_unregister.description`:

Description
-----------

This will allow the driver to cleanup any memory allocated for diag
messages and to free up any resources.

.. _`_ctl_diag_query`:

\_ctl_diag_query
================

.. c:function:: long _ctl_diag_query(struct MPT3SAS_ADAPTER *ioc, void __user *arg)

    query relevant info associated with diag buffers

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param arg:
        user space buffer containing ioctl content
    :type arg: void __user \*

.. _`_ctl_diag_query.description`:

Description
-----------

The application will send only buffer_type and unique_id.  Driver will
inspect unique_id first, if valid, fill in all the info.  If unique_id is
0x00, the driver will return info specified by Buffer Type.

.. _`mpt3sas_send_diag_release`:

mpt3sas_send_diag_release
=========================

.. c:function:: int mpt3sas_send_diag_release(struct MPT3SAS_ADAPTER *ioc, u8 buffer_type, u8 *issue_reset)

    Diag Release Message

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param buffer_type:
        specifies either TRACE, SNAPSHOT, or EXTENDED
    :type buffer_type: u8

    :param issue_reset:
        specifies whether host reset is required.
    :type issue_reset: u8 \*

.. _`_ctl_diag_release`:

\_ctl_diag_release
==================

.. c:function:: long _ctl_diag_release(struct MPT3SAS_ADAPTER *ioc, void __user *arg)

    request to send Diag Release Message to firmware

    :param ioc:
        ?
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param arg:
        user space buffer containing ioctl content
    :type arg: void __user \*

.. _`_ctl_diag_release.description`:

Description
-----------

This allows ownership of the specified buffer to returned to the driver,
allowing an application to read the buffer without fear that firmware is
overwriting information in the buffer.

.. _`_ctl_diag_read_buffer`:

\_ctl_diag_read_buffer
======================

.. c:function:: long _ctl_diag_read_buffer(struct MPT3SAS_ADAPTER *ioc, void __user *arg)

    request for copy of the diag buffer

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param arg:
        user space buffer containing ioctl content
    :type arg: void __user \*

.. _`_ctl_compat_mpt_command`:

\_ctl_compat_mpt_command
========================

.. c:function:: long _ctl_compat_mpt_command(struct MPT3SAS_ADAPTER *ioc, unsigned cmd, void __user *arg)

    convert 32bit pointers to 64bit.

    :param ioc:
        per adapter object
    :type ioc: struct MPT3SAS_ADAPTER \*

    :param cmd:
        ioctl opcode
    :type cmd: unsigned

    :param arg:
        (struct mpt3_ioctl_command32)
    :type arg: void __user \*

.. _`_ctl_compat_mpt_command.description`:

Description
-----------

MPT3COMMAND32 - Handle 32bit applications running on 64bit os.

.. _`_ctl_ioctl_main`:

\_ctl_ioctl_main
================

.. c:function:: long _ctl_ioctl_main(struct file *file, unsigned int cmd, void __user *arg, u8 compat, u16 mpi_version)

    main ioctl entry point

    :param file:
        (struct file)
    :type file: struct file \*

    :param cmd:
        ioctl opcode
    :type cmd: unsigned int

    :param arg:
        user space data buffer
    :type arg: void __user \*

    :param compat:
        handles 32 bit applications in 64bit os
    :type compat: u8

    :param mpi_version:
        will be MPI2_VERSION for mpt2ctl ioctl device &
        MPI25_VERSION \| MPI26_VERSION for mpt3ctl ioctl device.
    :type mpi_version: u16

.. _`_ctl_ioctl`:

\_ctl_ioctl
===========

.. c:function:: long _ctl_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    mpt3ctl main ioctl entry point (unlocked)

    :param file:
        (struct file)
    :type file: struct file \*

    :param cmd:
        ioctl opcode
    :type cmd: unsigned int

    :param arg:
        ?
    :type arg: unsigned long

.. _`_ctl_mpt2_ioctl`:

\_ctl_mpt2_ioctl
================

.. c:function:: long _ctl_mpt2_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    mpt2ctl main ioctl entry point (unlocked)

    :param file:
        (struct file)
    :type file: struct file \*

    :param cmd:
        ioctl opcode
    :type cmd: unsigned int

    :param arg:
        ?
    :type arg: unsigned long

.. _`_ctl_ioctl_compat`:

\_ctl_ioctl_compat
==================

.. c:function:: long _ctl_ioctl_compat(struct file *file, unsigned cmd, unsigned long arg)

    main ioctl entry point (compat)

    :param file:
        ?
    :type file: struct file \*

    :param cmd:
        ?
    :type cmd: unsigned

    :param arg:
        ?
    :type arg: unsigned long

.. _`_ctl_ioctl_compat.description`:

Description
-----------

This routine handles 32 bit applications in 64bit os.

.. _`_ctl_mpt2_ioctl_compat`:

\_ctl_mpt2_ioctl_compat
=======================

.. c:function:: long _ctl_mpt2_ioctl_compat(struct file *file, unsigned cmd, unsigned long arg)

    main ioctl entry point (compat)

    :param file:
        ?
    :type file: struct file \*

    :param cmd:
        ?
    :type cmd: unsigned

    :param arg:
        ?
    :type arg: unsigned long

.. _`_ctl_mpt2_ioctl_compat.description`:

Description
-----------

This routine handles 32 bit applications in 64bit os.

.. _`_ctl_version_fw_show`:

\_ctl_version_fw_show
=====================

.. c:function:: ssize_t _ctl_version_fw_show(struct device *cdev, struct device_attribute *attr, char *buf)

    firmware version

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_version_fw_show.description`:

Description
-----------

A sysfs 'read-only' shost attribute.

.. _`_ctl_version_bios_show`:

\_ctl_version_bios_show
=======================

.. c:function:: ssize_t _ctl_version_bios_show(struct device *cdev, struct device_attribute *attr, char *buf)

    bios version

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_version_bios_show.description`:

Description
-----------

A sysfs 'read-only' shost attribute.

.. _`_ctl_version_mpi_show`:

\_ctl_version_mpi_show
======================

.. c:function:: ssize_t _ctl_version_mpi_show(struct device *cdev, struct device_attribute *attr, char *buf)

    MPI (message passing interface) version

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_version_mpi_show.description`:

Description
-----------

A sysfs 'read-only' shost attribute.

.. _`_ctl_version_product_show`:

\_ctl_version_product_show
==========================

.. c:function:: ssize_t _ctl_version_product_show(struct device *cdev, struct device_attribute *attr, char *buf)

    product name

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_version_product_show.description`:

Description
-----------

A sysfs 'read-only' shost attribute.

.. _`_ctl_version_nvdata_persistent_show`:

\_ctl_version_nvdata_persistent_show
====================================

.. c:function:: ssize_t _ctl_version_nvdata_persistent_show(struct device *cdev, struct device_attribute *attr, char *buf)

    ndvata persistent version

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_version_nvdata_persistent_show.description`:

Description
-----------

A sysfs 'read-only' shost attribute.

.. _`_ctl_version_nvdata_default_show`:

\_ctl_version_nvdata_default_show
=================================

.. c:function:: ssize_t _ctl_version_nvdata_default_show(struct device *cdev, struct device_attribute *attr, char *buf)

    nvdata default version

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_version_nvdata_default_show.description`:

Description
-----------

A sysfs 'read-only' shost attribute.

.. _`_ctl_board_name_show`:

\_ctl_board_name_show
=====================

.. c:function:: ssize_t _ctl_board_name_show(struct device *cdev, struct device_attribute *attr, char *buf)

    board name

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_board_name_show.description`:

Description
-----------

A sysfs 'read-only' shost attribute.

.. _`_ctl_board_assembly_show`:

\_ctl_board_assembly_show
=========================

.. c:function:: ssize_t _ctl_board_assembly_show(struct device *cdev, struct device_attribute *attr, char *buf)

    board assembly name

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_board_assembly_show.description`:

Description
-----------

A sysfs 'read-only' shost attribute.

.. _`_ctl_board_tracer_show`:

\_ctl_board_tracer_show
=======================

.. c:function:: ssize_t _ctl_board_tracer_show(struct device *cdev, struct device_attribute *attr, char *buf)

    board tracer number

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_board_tracer_show.description`:

Description
-----------

A sysfs 'read-only' shost attribute.

.. _`_ctl_io_delay_show`:

\_ctl_io_delay_show
===================

.. c:function:: ssize_t _ctl_io_delay_show(struct device *cdev, struct device_attribute *attr, char *buf)

    io missing delay

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_io_delay_show.description`:

Description
-----------

This is for firmware implemention for deboucing device
removal events.

A sysfs 'read-only' shost attribute.

.. _`_ctl_device_delay_show`:

\_ctl_device_delay_show
=======================

.. c:function:: ssize_t _ctl_device_delay_show(struct device *cdev, struct device_attribute *attr, char *buf)

    device missing delay

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_device_delay_show.description`:

Description
-----------

This is for firmware implemention for deboucing device
removal events.

A sysfs 'read-only' shost attribute.

.. _`_ctl_fw_queue_depth_show`:

\_ctl_fw_queue_depth_show
=========================

.. c:function:: ssize_t _ctl_fw_queue_depth_show(struct device *cdev, struct device_attribute *attr, char *buf)

    global credits

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_fw_queue_depth_show.description`:

Description
-----------

This is firmware queue depth limit

A sysfs 'read-only' shost attribute.

.. _`_ctl_host_sas_address_show`:

\_ctl_host_sas_address_show
===========================

.. c:function:: ssize_t _ctl_host_sas_address_show(struct device *cdev, struct device_attribute *attr, char *buf)

    sas address

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_host_sas_address_show.description`:

Description
-----------

This is the controller sas address

A sysfs 'read-only' shost attribute.

.. _`_ctl_logging_level_show`:

\_ctl_logging_level_show
========================

.. c:function:: ssize_t _ctl_logging_level_show(struct device *cdev, struct device_attribute *attr, char *buf)

    logging level

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_logging_level_show.description`:

Description
-----------

A sysfs 'read/write' shost attribute.

.. _`_ctl_fwfault_debug_show`:

\_ctl_fwfault_debug_show
========================

.. c:function:: ssize_t _ctl_fwfault_debug_show(struct device *cdev, struct device_attribute *attr, char *buf)

    show/store fwfault_debug

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_fwfault_debug_show.description`:

Description
-----------

mpt3sas_fwfault_debug is command line option
A sysfs 'read/write' shost attribute.

.. _`_ctl_ioc_reset_count_show`:

\_ctl_ioc_reset_count_show
==========================

.. c:function:: ssize_t _ctl_ioc_reset_count_show(struct device *cdev, struct device_attribute *attr, char *buf)

    ioc reset count

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_ioc_reset_count_show.description`:

Description
-----------

This is firmware queue depth limit

A sysfs 'read-only' shost attribute.

.. _`_ctl_ioc_reply_queue_count_show`:

\_ctl_ioc_reply_queue_count_show
================================

.. c:function:: ssize_t _ctl_ioc_reply_queue_count_show(struct device *cdev, struct device_attribute *attr, char *buf)

    number of reply queues

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_ioc_reply_queue_count_show.description`:

Description
-----------

This is number of reply queues

A sysfs 'read-only' shost attribute.

.. _`_ctl_brm_status_show`:

\_ctl_BRM_status_show
=====================

.. c:function:: ssize_t _ctl_BRM_status_show(struct device *cdev, struct device_attribute *attr, char *buf)

    Backup Rail Monitor Status

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_brm_status_show.description`:

Description
-----------

This is number of reply queues

A sysfs 'read-only' shost attribute.

.. _`_ctl_host_trace_buffer_size_show`:

\_ctl_host_trace_buffer_size_show
=================================

.. c:function:: ssize_t _ctl_host_trace_buffer_size_show(struct device *cdev, struct device_attribute *attr, char *buf)

    host buffer size (trace only)

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_host_trace_buffer_size_show.description`:

Description
-----------

A sysfs 'read-only' shost attribute.

.. _`_ctl_host_trace_buffer_show`:

\_ctl_host_trace_buffer_show
============================

.. c:function:: ssize_t _ctl_host_trace_buffer_show(struct device *cdev, struct device_attribute *attr, char *buf)

    firmware ring buffer (trace only)

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_host_trace_buffer_show.description`:

Description
-----------

A sysfs 'read/write' shost attribute.

You will only be able to read 4k bytes of ring buffer at a time.
In order to read beyond 4k bytes, you will have to write out the
offset to the same attribute, it will move the pointer.

.. _`_ctl_host_trace_buffer_enable_show`:

\_ctl_host_trace_buffer_enable_show
===================================

.. c:function:: ssize_t _ctl_host_trace_buffer_enable_show(struct device *cdev, struct device_attribute *attr, char *buf)

    firmware ring buffer (trace only)

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_host_trace_buffer_enable_show.description`:

Description
-----------

A sysfs 'read/write' shost attribute.

This is a mechnism to post/release host_trace_buffers

.. _`_ctl_diag_trigger_master_show`:

\_ctl_diag_trigger_master_show
==============================

.. c:function:: ssize_t _ctl_diag_trigger_master_show(struct device *cdev, struct device_attribute *attr, char *buf)

    show the diag_trigger_master attribute

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_diag_trigger_master_show.description`:

Description
-----------

A sysfs 'read/write' shost attribute.

.. _`_ctl_diag_trigger_master_store`:

\_ctl_diag_trigger_master_store
===============================

.. c:function:: ssize_t _ctl_diag_trigger_master_store(struct device *cdev, struct device_attribute *attr, const char *buf, size_t count)

    store the diag_trigger_master attribute

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: const char \*

    :param count:
        ?
    :type count: size_t

.. _`_ctl_diag_trigger_master_store.description`:

Description
-----------

A sysfs 'read/write' shost attribute.

.. _`_ctl_diag_trigger_event_show`:

\_ctl_diag_trigger_event_show
=============================

.. c:function:: ssize_t _ctl_diag_trigger_event_show(struct device *cdev, struct device_attribute *attr, char *buf)

    show the diag_trigger_event attribute

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_diag_trigger_event_show.description`:

Description
-----------

A sysfs 'read/write' shost attribute.

.. _`_ctl_diag_trigger_event_store`:

\_ctl_diag_trigger_event_store
==============================

.. c:function:: ssize_t _ctl_diag_trigger_event_store(struct device *cdev, struct device_attribute *attr, const char *buf, size_t count)

    store the diag_trigger_event attribute

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: const char \*

    :param count:
        ?
    :type count: size_t

.. _`_ctl_diag_trigger_event_store.description`:

Description
-----------

A sysfs 'read/write' shost attribute.

.. _`_ctl_diag_trigger_scsi_show`:

\_ctl_diag_trigger_scsi_show
============================

.. c:function:: ssize_t _ctl_diag_trigger_scsi_show(struct device *cdev, struct device_attribute *attr, char *buf)

    show the diag_trigger_scsi attribute

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_diag_trigger_scsi_show.description`:

Description
-----------

A sysfs 'read/write' shost attribute.

.. _`_ctl_diag_trigger_scsi_store`:

\_ctl_diag_trigger_scsi_store
=============================

.. c:function:: ssize_t _ctl_diag_trigger_scsi_store(struct device *cdev, struct device_attribute *attr, const char *buf, size_t count)

    store the diag_trigger_scsi attribute

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: const char \*

    :param count:
        ?
    :type count: size_t

.. _`_ctl_diag_trigger_scsi_store.description`:

Description
-----------

A sysfs 'read/write' shost attribute.

.. _`_ctl_diag_trigger_mpi_show`:

\_ctl_diag_trigger_mpi_show
===========================

.. c:function:: ssize_t _ctl_diag_trigger_mpi_show(struct device *cdev, struct device_attribute *attr, char *buf)

    show the diag_trigger_mpi attribute

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_diag_trigger_mpi_show.description`:

Description
-----------

A sysfs 'read/write' shost attribute.

.. _`_ctl_diag_trigger_mpi_store`:

\_ctl_diag_trigger_mpi_store
============================

.. c:function:: ssize_t _ctl_diag_trigger_mpi_store(struct device *cdev, struct device_attribute *attr, const char *buf, size_t count)

    store the diag_trigger_mpi attribute

    :param cdev:
        pointer to embedded class device
    :type cdev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: const char \*

    :param count:
        ?
    :type count: size_t

.. _`_ctl_diag_trigger_mpi_store.description`:

Description
-----------

A sysfs 'read/write' shost attribute.

.. _`_ctl_device_sas_address_show`:

\_ctl_device_sas_address_show
=============================

.. c:function:: ssize_t _ctl_device_sas_address_show(struct device *dev, struct device_attribute *attr, char *buf)

    sas address

    :param dev:
        pointer to embedded class device
    :type dev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_device_sas_address_show.description`:

Description
-----------

This is the sas address for the target

A sysfs 'read-only' shost attribute.

.. _`_ctl_device_handle_show`:

\_ctl_device_handle_show
========================

.. c:function:: ssize_t _ctl_device_handle_show(struct device *dev, struct device_attribute *attr, char *buf)

    device handle

    :param dev:
        pointer to embedded class device
    :type dev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_device_handle_show.description`:

Description
-----------

This is the firmware assigned device handle

A sysfs 'read-only' shost attribute.

.. _`_ctl_device_ncq_prio_enable_show`:

\_ctl_device_ncq_prio_enable_show
=================================

.. c:function:: ssize_t _ctl_device_ncq_prio_enable_show(struct device *dev, struct device_attribute *attr, char *buf)

    send prioritized io commands to device

    :param dev:
        pointer to embedded device
    :type dev: struct device \*

    :param attr:
        ?
    :type attr: struct device_attribute \*

    :param buf:
        the buffer returned
    :type buf: char \*

.. _`_ctl_device_ncq_prio_enable_show.description`:

Description
-----------

A sysfs 'read/write' sdev attribute, only works with SATA

.. _`mpt3sas_ctl_init`:

mpt3sas_ctl_init
================

.. c:function:: void mpt3sas_ctl_init(ushort hbas_to_enumerate)

    main entry point for ctl.

    :param hbas_to_enumerate:
        ?
    :type hbas_to_enumerate: ushort

.. _`mpt3sas_ctl_exit`:

mpt3sas_ctl_exit
================

.. c:function:: void mpt3sas_ctl_exit(ushort hbas_to_enumerate)

    exit point for ctl

    :param hbas_to_enumerate:
        ?
    :type hbas_to_enumerate: ushort

.. This file was automatic generated / don't edit.

