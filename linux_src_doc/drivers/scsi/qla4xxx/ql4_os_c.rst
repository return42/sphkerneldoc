.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qla4xxx/ql4_os.c

.. _`qla4xxx_create_chap_list`:

qla4xxx_create_chap_list
========================

.. c:function:: void qla4xxx_create_chap_list(struct scsi_qla_host *ha)

    Create CHAP list from FLASH

    :param ha:
        pointer to adapter structure
    :type ha: struct scsi_qla_host \*

.. _`qla4xxx_create_chap_list.description`:

Description
-----------

Read flash and make a list of CHAP entries, during login when a CHAP entry
is received, it will be checked in this list. If entry exist then the CHAP
entry index is set in the DDB. If CHAP entry does not exist in this list
then a new entry is added in FLASH in CHAP table and the index obtained is
used in the DDB.

.. _`qla4xxx_find_free_chap_index`:

qla4xxx_find_free_chap_index
============================

.. c:function:: int qla4xxx_find_free_chap_index(struct scsi_qla_host *ha, uint16_t *chap_index)

    Find the first free chap index

    :param ha:
        pointer to adapter structure
    :type ha: struct scsi_qla_host \*

    :param chap_index:
        CHAP index to be returned
    :type chap_index: uint16_t \*

.. _`qla4xxx_find_free_chap_index.description`:

Description
-----------

Find the first free chap index available in the chap table

.. _`qla4xxx_find_free_chap_index.note`:

Note
----

Caller should acquire the chap lock before getting here.

.. _`qla4xxx_set_chap_entry`:

qla4xxx_set_chap_entry
======================

.. c:function:: int qla4xxx_set_chap_entry(struct Scsi_Host *shost, void *data, int len)

    Make chap entry with given information

    :param shost:
        pointer to host
    :type shost: struct Scsi_Host \*

    :param data:
        chap info - credentials, index and type to make chap entry
    :type data: void \*

    :param len:
        length of data
    :type len: int

.. _`qla4xxx_set_chap_entry.description`:

Description
-----------

Add or update chap entry with the given information

.. _`qla4xxx_mark_all_devices_missing`:

qla4xxx_mark_all_devices_missing
================================

.. c:function:: void qla4xxx_mark_all_devices_missing(struct scsi_qla_host *ha)

    mark all devices as missing.

    :param ha:
        Pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

.. _`qla4xxx_mark_all_devices_missing.description`:

Description
-----------

This routine marks a device missing and resets the relogin retry count.

.. _`qla4xxx_queuecommand`:

qla4xxx_queuecommand
====================

.. c:function:: int qla4xxx_queuecommand(struct Scsi_Host *host, struct scsi_cmnd *cmd)

    scsi layer issues scsi command to driver.

    :param host:
        scsi host
    :type host: struct Scsi_Host \*

    :param cmd:
        Pointer to Linux's SCSI command structure
    :type cmd: struct scsi_cmnd \*

.. _`qla4xxx_queuecommand.remarks`:

Remarks
-------

This routine is invoked by Linux to send a SCSI command to the driver.
The mid-level driver tries to ensure that queuecommand never gets
invoked concurrently with itself or the interrupt handler (although
the interrupt handler may call this routine as part of request-
completion handling).   Unfortunely, it sometimes calls the scheduler
in interrupt context which is a big NO! NO!.

.. _`qla4xxx_mem_free`:

qla4xxx_mem_free
================

.. c:function:: void qla4xxx_mem_free(struct scsi_qla_host *ha)

    frees memory allocated to adapter

    :param ha:
        Pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

.. _`qla4xxx_mem_free.description`:

Description
-----------

Frees memory previously allocated by qla4xxx_mem_alloc

.. _`qla4xxx_mem_alloc`:

qla4xxx_mem_alloc
=================

.. c:function:: int qla4xxx_mem_alloc(struct scsi_qla_host *ha)

    allocates memory for use by adapter.

    :param ha:
        Pointer to host adapter structure
    :type ha: struct scsi_qla_host \*

.. _`qla4xxx_mem_alloc.description`:

Description
-----------

Allocates DMA memory for request and response queues. Also allocates memory
for srbs.

.. _`qla4_8xxx_check_temp`:

qla4_8xxx_check_temp
====================

.. c:function:: int qla4_8xxx_check_temp(struct scsi_qla_host *ha)

    Check the ISP82XX temperature.

    :param ha:
        adapter block pointer.
    :type ha: struct scsi_qla_host \*

.. _`qla4_8xxx_check_temp.note`:

Note
----

The caller should not hold the idc lock.

.. _`qla4_8xxx_check_fw_alive`:

qla4_8xxx_check_fw_alive
========================

.. c:function:: int qla4_8xxx_check_fw_alive(struct scsi_qla_host *ha)

    Check firmware health

    :param ha:
        Pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

.. _`qla4_8xxx_check_fw_alive.context`:

Context
-------

Interrupt

.. _`qla4_8xxx_watchdog`:

qla4_8xxx_watchdog
==================

.. c:function:: void qla4_8xxx_watchdog(struct scsi_qla_host *ha)

    Poll dev state

    :param ha:
        Pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

.. _`qla4_8xxx_watchdog.context`:

Context
-------

Interrupt

.. _`qla4xxx_timer`:

qla4xxx_timer
=============

.. c:function:: void qla4xxx_timer(struct timer_list *t)

    checks every second for work to do.

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`qla4xxx_cmd_wait`:

qla4xxx_cmd_wait
================

.. c:function:: int qla4xxx_cmd_wait(struct scsi_qla_host *ha)

    waits for all outstanding commands to complete

    :param ha:
        Pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

.. _`qla4xxx_cmd_wait.description`:

Description
-----------

This routine stalls the driver until all outstanding commands are returned.
Caller must release the Hardware Lock prior to calling this routine.

.. _`qla4xxx_soft_reset`:

qla4xxx_soft_reset
==================

.. c:function:: int qla4xxx_soft_reset(struct scsi_qla_host *ha)

    performs soft reset.

    :param ha:
        Pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

.. _`qla4xxx_abort_active_cmds`:

qla4xxx_abort_active_cmds
=========================

.. c:function:: void qla4xxx_abort_active_cmds(struct scsi_qla_host *ha, int res)

    returns all outstanding i/o requests to O.S.

    :param ha:
        Pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

    :param res:
        returned scsi status
    :type res: int

.. _`qla4xxx_abort_active_cmds.description`:

Description
-----------

This routine is called just prior to a HARD RESET to return all
outstanding commands back to the Operating System.
Caller should make sure that the following locks are released

.. _`qla4xxx_abort_active_cmds.before-this-calling-routine`:

before this calling routine
---------------------------

Hardware lock, and io_request_lock.

.. _`qla4xxx_recover_adapter`:

qla4xxx_recover_adapter
=======================

.. c:function:: int qla4xxx_recover_adapter(struct scsi_qla_host *ha)

    recovers adapter after a fatal error

    :param ha:
        Pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

.. _`qla4xxx_do_dpc`:

qla4xxx_do_dpc
==============

.. c:function:: void qla4xxx_do_dpc(struct work_struct *work)

    dpc routine

    :param work:
        *undescribed*
    :type work: struct work_struct \*

.. _`qla4xxx_do_dpc.description`:

Description
-----------

This routine is a task that is schedule by the interrupt handler
to perform the background processing for interrupts.  We put it
on a task queue that is consumed whenever the scheduler runs; that's
so you can do anything (i.e. put the process to sleep etc).  In fact,
the mid-level tries to sleep when it reaches the driver threshold
"host->can_queue". This can cause a panic if we were in our interrupt code.

.. _`qla4xxx_free_adapter`:

qla4xxx_free_adapter
====================

.. c:function:: void qla4xxx_free_adapter(struct scsi_qla_host *ha)

    release the adapter

    :param ha:
        pointer to adapter structure
    :type ha: struct scsi_qla_host \*

.. _`qla4xxx_get_bidi_chap`:

qla4xxx_get_bidi_chap
=====================

.. c:function:: int qla4xxx_get_bidi_chap(struct scsi_qla_host *ha, char *username, char *password)

    Get a BIDI CHAP user and password

    :param ha:
        pointer to adapter structure
    :type ha: struct scsi_qla_host \*

    :param username:
        CHAP username to be returned
    :type username: char \*

    :param password:
        CHAP password to be returned
    :type password: char \*

.. _`qla4xxx_get_bidi_chap.description`:

Description
-----------

If a boot entry has BIDI CHAP enabled then we need to set the BIDI CHAP
user and password in the sysfs entry in /sys/firmware/iscsi_boot#/.
So from the CHAP cache find the first BIDI CHAP entry and set it
to the boot record in sysfs.

.. _`qla4xxx_check_existing_isid`:

qla4xxx_check_existing_isid
===========================

.. c:function:: int qla4xxx_check_existing_isid(struct list_head *list_nt, uint8_t *isid)

    check if target with same isid exist in target list

    :param list_nt:
        list of target
    :type list_nt: struct list_head \*

    :param isid:
        isid to check
    :type isid: uint8_t \*

.. _`qla4xxx_check_existing_isid.description`:

Description
-----------

This routine return QLA_SUCCESS if target with same isid exist

.. _`qla4xxx_update_isid`:

qla4xxx_update_isid
===================

.. c:function:: int qla4xxx_update_isid(struct scsi_qla_host *ha, struct list_head *list_nt, struct dev_db_entry *fw_ddb_entry)

    compare ddbs and updated isid

    :param ha:
        Pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

    :param list_nt:
        list of nt target
    :type list_nt: struct list_head \*

    :param fw_ddb_entry:
        firmware ddb entry
    :type fw_ddb_entry: struct dev_db_entry \*

.. _`qla4xxx_update_isid.description`:

Description
-----------

This routine update isid if ddbs have same iqn, same isid and
different IP addr.
Return QLA_SUCCESS if isid is updated.

.. _`qla4xxx_should_update_isid`:

qla4xxx_should_update_isid
==========================

.. c:function:: int qla4xxx_should_update_isid(struct scsi_qla_host *ha, struct ql4_tuple_ddb *old_tddb, struct ql4_tuple_ddb *new_tddb)

    check if isid need to update

    :param ha:
        Pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

    :param old_tddb:
        ddb tuple
    :type old_tddb: struct ql4_tuple_ddb \*

    :param new_tddb:
        ddb tuple
    :type new_tddb: struct ql4_tuple_ddb \*

.. _`qla4xxx_should_update_isid.description`:

Description
-----------

Return QLA_SUCCESS if different IP, different PORT, same iqn,
same isid

.. _`qla4xxx_is_flash_ddb_exists`:

qla4xxx_is_flash_ddb_exists
===========================

.. c:function:: int qla4xxx_is_flash_ddb_exists(struct scsi_qla_host *ha, struct list_head *list_nt, struct dev_db_entry *fw_ddb_entry)

    check if fw_ddb_entry already exists in list_nt

    :param ha:
        Pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

    :param list_nt:
        list of nt target.
    :type list_nt: struct list_head \*

    :param fw_ddb_entry:
        firmware ddb entry.
    :type fw_ddb_entry: struct dev_db_entry \*

.. _`qla4xxx_is_flash_ddb_exists.description`:

Description
-----------

This routine check if fw_ddb_entry already exists in list_nt to avoid
duplicate ddb in list_nt.
Return QLA_SUCCESS if duplicate ddb exit in list_nl.

.. _`qla4xxx_is_flash_ddb_exists.note`:

Note
----

This function also update isid of DDB if required.

.. _`qla4xxx_remove_failed_ddb`:

qla4xxx_remove_failed_ddb
=========================

.. c:function:: void qla4xxx_remove_failed_ddb(struct scsi_qla_host *ha, struct list_head *list_ddb)

    Remove inactive or failed ddb from list

    :param ha:
        pointer to adapter structure
    :type ha: struct scsi_qla_host \*

    :param list_ddb:
        List from which failed ddb to be removed
    :type list_ddb: struct list_head \*

.. _`qla4xxx_remove_failed_ddb.description`:

Description
-----------

Iterate over the list of DDBs and find and remove DDBs that are either in
no connection active state or failed state

.. _`qla4xxx_sysfs_ddb_is_non_persistent`:

qla4xxx_sysfs_ddb_is_non_persistent
===================================

.. c:function:: int qla4xxx_sysfs_ddb_is_non_persistent(struct device *dev, void *data)

    check for non-persistence of ddb entry

    :param dev:
        dev associated with the sysfs entry
    :type dev: struct device \*

    :param data:
        pointer to flashnode session object
    :type data: void \*

.. _`qla4xxx_sysfs_ddb_is_non_persistent.return`:

Return
------

1: if flashnode entry is non-persistent
0: if flashnode entry is persistent

.. _`qla4xxx_sysfs_ddb_tgt_create`:

qla4xxx_sysfs_ddb_tgt_create
============================

.. c:function:: int qla4xxx_sysfs_ddb_tgt_create(struct scsi_qla_host *ha, struct dev_db_entry *fw_ddb_entry, uint16_t *idx, int user)

    Create sysfs entry for target

    :param ha:
        pointer to host
    :type ha: struct scsi_qla_host \*

    :param fw_ddb_entry:
        flash ddb data
    :type fw_ddb_entry: struct dev_db_entry \*

    :param idx:
        target index
    :type idx: uint16_t \*

    :param user:
        if set then this call is made from userland else from kernel
    :type user: int

.. _`qla4xxx_sysfs_ddb_tgt_create.on-sucess`:

On sucess
---------

QLA_SUCCESS

.. _`qla4xxx_sysfs_ddb_tgt_create.on-failure`:

On failure
----------

QLA_ERROR

This create separate sysfs entries for session and connection attributes of
the given fw ddb entry.
If this is invoked as a result of a userspace call then the entry is marked
as nonpersistent using flash_state field.

.. _`qla4xxx_sysfs_ddb_add`:

qla4xxx_sysfs_ddb_add
=====================

.. c:function:: int qla4xxx_sysfs_ddb_add(struct Scsi_Host *shost, const char *buf, int len)

    Add new ddb entry in flash

    :param shost:
        pointer to host
    :type shost: struct Scsi_Host \*

    :param buf:
        type of ddb entry (ipv4/ipv6)
    :type buf: const char \*

    :param len:
        length of buf
    :type len: int

.. _`qla4xxx_sysfs_ddb_add.description`:

Description
-----------

This creates new ddb entry in the flash by finding first free index and
storing default ddb there. And then create sysfs entry for the new ddb entry.

.. _`qla4xxx_sysfs_ddb_apply`:

qla4xxx_sysfs_ddb_apply
=======================

.. c:function:: int qla4xxx_sysfs_ddb_apply(struct iscsi_bus_flash_session *fnode_sess, struct iscsi_bus_flash_conn *fnode_conn)

    write the target ddb contents to Flash

    :param fnode_sess:
        pointer to session attrs of flash ddb entry
    :type fnode_sess: struct iscsi_bus_flash_session \*

    :param fnode_conn:
        pointer to connection attrs of flash ddb entry
    :type fnode_conn: struct iscsi_bus_flash_conn \*

.. _`qla4xxx_sysfs_ddb_apply.description`:

Description
-----------

This writes the contents of target ddb buffer to Flash with a valid cookie
value in order to make the ddb entry persistent.

.. _`qla4xxx_sysfs_ddb_login`:

qla4xxx_sysfs_ddb_login
=======================

.. c:function:: int qla4xxx_sysfs_ddb_login(struct iscsi_bus_flash_session *fnode_sess, struct iscsi_bus_flash_conn *fnode_conn)

    Login to the specified target

    :param fnode_sess:
        pointer to session attrs of flash ddb entry
    :type fnode_sess: struct iscsi_bus_flash_session \*

    :param fnode_conn:
        pointer to connection attrs of flash ddb entry
    :type fnode_conn: struct iscsi_bus_flash_conn \*

.. _`qla4xxx_sysfs_ddb_login.description`:

Description
-----------

This logs in to the specified target

.. _`qla4xxx_sysfs_ddb_logout_sid`:

qla4xxx_sysfs_ddb_logout_sid
============================

.. c:function:: int qla4xxx_sysfs_ddb_logout_sid(struct iscsi_cls_session *cls_sess)

    Logout session for the specified target

    :param cls_sess:
        pointer to session to be logged out
    :type cls_sess: struct iscsi_cls_session \*

.. _`qla4xxx_sysfs_ddb_logout_sid.description`:

Description
-----------

This performs session log out from the specified target

.. _`qla4xxx_sysfs_ddb_logout`:

qla4xxx_sysfs_ddb_logout
========================

.. c:function:: int qla4xxx_sysfs_ddb_logout(struct iscsi_bus_flash_session *fnode_sess, struct iscsi_bus_flash_conn *fnode_conn)

    Logout from the specified target

    :param fnode_sess:
        pointer to session attrs of flash ddb entry
    :type fnode_sess: struct iscsi_bus_flash_session \*

    :param fnode_conn:
        pointer to connection attrs of flash ddb entry
    :type fnode_conn: struct iscsi_bus_flash_conn \*

.. _`qla4xxx_sysfs_ddb_logout.description`:

Description
-----------

This performs log out from the specified target

.. _`qla4xxx_sysfs_ddb_set_param`:

qla4xxx_sysfs_ddb_set_param
===========================

.. c:function:: int qla4xxx_sysfs_ddb_set_param(struct iscsi_bus_flash_session *fnode_sess, struct iscsi_bus_flash_conn *fnode_conn, void *data, int len)

    Set parameter for firmware DDB entry

    :param fnode_sess:
        pointer to session attrs of flash ddb entry
    :type fnode_sess: struct iscsi_bus_flash_session \*

    :param fnode_conn:
        pointer to connection attrs of flash ddb entry
    :type fnode_conn: struct iscsi_bus_flash_conn \*

    :param data:
        Parameters and their values to update
    :type data: void \*

    :param len:
        len of data
    :type len: int

.. _`qla4xxx_sysfs_ddb_set_param.description`:

Description
-----------

This sets the parameter of flash ddb entry and writes them to flash

.. _`qla4xxx_sysfs_ddb_delete`:

qla4xxx_sysfs_ddb_delete
========================

.. c:function:: int qla4xxx_sysfs_ddb_delete(struct iscsi_bus_flash_session *fnode_sess)

    Delete firmware DDB entry

    :param fnode_sess:
        pointer to session attrs of flash ddb entry
    :type fnode_sess: struct iscsi_bus_flash_session \*

.. _`qla4xxx_sysfs_ddb_delete.description`:

Description
-----------

This invalidates the flash ddb entry at the given index

.. _`qla4xxx_sysfs_ddb_export`:

qla4xxx_sysfs_ddb_export
========================

.. c:function:: int qla4xxx_sysfs_ddb_export(struct scsi_qla_host *ha)

    Create sysfs entries for firmware DDBs

    :param ha:
        pointer to adapter structure
    :type ha: struct scsi_qla_host \*

.. _`qla4xxx_sysfs_ddb_export.description`:

Description
-----------

Export the firmware DDB for all send targets and normal targets to sysfs.

.. _`qla4xxx_build_ddb_list`:

qla4xxx_build_ddb_list
======================

.. c:function:: void qla4xxx_build_ddb_list(struct scsi_qla_host *ha, int is_reset)

    Build ddb list and setup sessions

    :param ha:
        pointer to adapter structure
    :type ha: struct scsi_qla_host \*

    :param is_reset:
        Is this init path or reset path
    :type is_reset: int

.. _`qla4xxx_build_ddb_list.description`:

Description
-----------

Create a list of sendtargets (st) from firmware DDBs, issue send targets
using connection open, then create the list of normal targets (nt)
from firmware DDBs. Based on the list of nt setup session and connection
objects.

.. _`qla4xxx_wait_login_resp_boot_tgt`:

qla4xxx_wait_login_resp_boot_tgt
================================

.. c:function:: void qla4xxx_wait_login_resp_boot_tgt(struct scsi_qla_host *ha)

    Wait for iSCSI boot target login response.

    :param ha:
        pointer to adapter structure
    :type ha: struct scsi_qla_host \*

.. _`qla4xxx_wait_login_resp_boot_tgt.description`:

Description
-----------

When the boot entry is normal iSCSI target then DF_BOOT_TGT flag will be
set in DDB and we will wait for login response of boot targets during
probe.

.. _`qla4xxx_probe_adapter`:

qla4xxx_probe_adapter
=====================

.. c:function:: int qla4xxx_probe_adapter(struct pci_dev *pdev, const struct pci_device_id *ent)

    callback function to probe HBA

    :param pdev:
        pointer to pci_dev structure
    :type pdev: struct pci_dev \*

    :param ent:
        *undescribed*
    :type ent: const struct pci_device_id \*

.. _`qla4xxx_probe_adapter.description`:

Description
-----------

This routine will probe for Qlogic 4xxx iSCSI host adapters.
It returns zero if successful. It also initializes all data necessary for
the driver.

.. _`qla4xxx_prevent_other_port_reinit`:

qla4xxx_prevent_other_port_reinit
=================================

.. c:function:: void qla4xxx_prevent_other_port_reinit(struct scsi_qla_host *ha)

    prevent other port from re-initialize

    :param ha:
        pointer to adapter structure
    :type ha: struct scsi_qla_host \*

.. _`qla4xxx_prevent_other_port_reinit.description`:

Description
-----------

Mark the other ISP-4xxx port to indicate that the driver is being removed,
so that the other port will not re-initialize while in the process of
removing the ha due to driver unload or hba hotplug.

.. _`qla4xxx_remove_adapter`:

qla4xxx_remove_adapter
======================

.. c:function:: void qla4xxx_remove_adapter(struct pci_dev *pdev)

    callback function to remove adapter.

    :param pdev:
        *undescribed*
    :type pdev: struct pci_dev \*

.. _`qla4xxx_config_dma_addressing`:

qla4xxx_config_dma_addressing
=============================

.. c:function:: void qla4xxx_config_dma_addressing(struct scsi_qla_host *ha)

    Configure OS DMA addressing method.

    :param ha:
        HA context
    :type ha: struct scsi_qla_host \*

.. _`qla4xxx_del_from_active_array`:

qla4xxx_del_from_active_array
=============================

.. c:function:: struct srb *qla4xxx_del_from_active_array(struct scsi_qla_host *ha, uint32_t index)

    returns an active srb

    :param ha:
        Pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

    :param index:
        index into the active_array
    :type index: uint32_t

.. _`qla4xxx_del_from_active_array.description`:

Description
-----------

This routine removes and returns the srb at the specified index

.. _`qla4xxx_eh_wait_on_command`:

qla4xxx_eh_wait_on_command
==========================

.. c:function:: int qla4xxx_eh_wait_on_command(struct scsi_qla_host *ha, struct scsi_cmnd *cmd)

    waits for command to be returned by firmware

    :param ha:
        Pointer to host adapter structure.
    :type ha: struct scsi_qla_host \*

    :param cmd:
        Scsi Command to wait on.
    :type cmd: struct scsi_cmnd \*

.. _`qla4xxx_eh_wait_on_command.description`:

Description
-----------

This routine waits for the command to be returned by the Firmware
for some max time.

.. _`qla4xxx_wait_for_hba_online`:

qla4xxx_wait_for_hba_online
===========================

.. c:function:: int qla4xxx_wait_for_hba_online(struct scsi_qla_host *ha)

    waits for HBA to come online

    :param ha:
        Pointer to host adapter structure
    :type ha: struct scsi_qla_host \*

.. _`qla4xxx_eh_wait_for_commands`:

qla4xxx_eh_wait_for_commands
============================

.. c:function:: int qla4xxx_eh_wait_for_commands(struct scsi_qla_host *ha, struct scsi_target *stgt, struct scsi_device *sdev)

    wait for active cmds to finish.

    :param ha:
        pointer to HBA
    :type ha: struct scsi_qla_host \*

    :param stgt:
        *undescribed*
    :type stgt: struct scsi_target \*

    :param sdev:
        *undescribed*
    :type sdev: struct scsi_device \*

.. _`qla4xxx_eh_wait_for_commands.description`:

Description
-----------

This function waits for all outstanding commands to a lun to complete. It
returns 0 if all pending commands are returned and 1 otherwise.

.. _`qla4xxx_eh_abort`:

qla4xxx_eh_abort
================

.. c:function:: int qla4xxx_eh_abort(struct scsi_cmnd *cmd)

    callback for abort task.

    :param cmd:
        Pointer to Linux's SCSI command structure
    :type cmd: struct scsi_cmnd \*

.. _`qla4xxx_eh_abort.description`:

Description
-----------

This routine is called by the Linux OS to abort the specified
command.

.. _`qla4xxx_eh_device_reset`:

qla4xxx_eh_device_reset
=======================

.. c:function:: int qla4xxx_eh_device_reset(struct scsi_cmnd *cmd)

    callback for target reset.

    :param cmd:
        Pointer to Linux's SCSI command structure
    :type cmd: struct scsi_cmnd \*

.. _`qla4xxx_eh_device_reset.description`:

Description
-----------

This routine is called by the Linux OS to reset all luns on the
specified target.

.. _`qla4xxx_eh_target_reset`:

qla4xxx_eh_target_reset
=======================

.. c:function:: int qla4xxx_eh_target_reset(struct scsi_cmnd *cmd)

    callback for target reset.

    :param cmd:
        Pointer to Linux's SCSI command structure
    :type cmd: struct scsi_cmnd \*

.. _`qla4xxx_eh_target_reset.description`:

Description
-----------

This routine is called by the Linux OS to reset the target.

.. _`qla4xxx_is_eh_active`:

qla4xxx_is_eh_active
====================

.. c:function:: int qla4xxx_is_eh_active(struct Scsi_Host *shost)

    check if error handler is running

    :param shost:
        Pointer to SCSI Host struct
    :type shost: struct Scsi_Host \*

.. _`qla4xxx_is_eh_active.description`:

Description
-----------

This routine finds that if reset host is called in EH
scenario or from some application like sg_reset

.. _`qla4xxx_eh_host_reset`:

qla4xxx_eh_host_reset
=====================

.. c:function:: int qla4xxx_eh_host_reset(struct scsi_cmnd *cmd)

    kernel callback

    :param cmd:
        Pointer to Linux's SCSI command structure
    :type cmd: struct scsi_cmnd \*

.. _`qla4xxx_eh_host_reset.description`:

Description
-----------

This routine is invoked by the Linux kernel to perform fatal error
recovery on the specified adapter.

.. _`qla4xxx_pci_mmio_enabled`:

qla4xxx_pci_mmio_enabled
========================

.. c:function:: pci_ers_result_t qla4xxx_pci_mmio_enabled(struct pci_dev *pdev)

    \ :c:func:`qla4xxx_pci_error_detected`\  returns PCI_ERS_RESULT_CAN_RECOVER and read/write to the device still works.

    :param pdev:
        *undescribed*
    :type pdev: struct pci_dev \*

.. This file was automatic generated / don't edit.

