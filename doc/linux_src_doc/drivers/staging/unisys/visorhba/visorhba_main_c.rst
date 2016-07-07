.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/unisys/visorhba/visorhba_main.c

.. _`visor_thread_start`:

visor_thread_start
==================

.. c:function:: struct task_struct *visor_thread_start(int (*) threadfn (void *, void *thrcontext, char *name)

    starts a thread for the device

    :param (int (\*) threadfn (void \*):
        Function the thread starts

    :param void \*thrcontext:
        Context to pass to the thread, i.e. devdata

    :param char \*name:
        string describing name of thread

.. _`visor_thread_start.description`:

Description
-----------

Starts a thread for the device.

Return the task_struct \* denoting the thread on success,
or NULL on failure

.. _`visor_thread_stop`:

visor_thread_stop
=================

.. c:function:: void visor_thread_stop(struct task_struct *task)

    stops the thread if it is running

    :param struct task_struct \*task:
        *undescribed*

.. _`add_scsipending_entry`:

add_scsipending_entry
=====================

.. c:function:: int add_scsipending_entry(struct visorhba_devdata *devdata, char cmdtype, void *new)

    save off io command that is pending in Service Partition

    :param struct visorhba_devdata \*devdata:
        Pointer to devdata

    :param char cmdtype:
        Specifies the type of command pending

    :param void \*new:
        The command to be saved

.. _`add_scsipending_entry.description`:

Description
-----------

Saves off the io command that is being handled by the Service
Partition so that it can be handled when it completes. If new is
NULL it is assumed the entry refers only to the cmdrsp.
Returns insert_location where entry was added,
SCSI_MLQUEUE_DEVICE_BUSY if it can't

.. _`del_scsipending_ent`:

del_scsipending_ent
===================

.. c:function:: void *del_scsipending_ent(struct visorhba_devdata *devdata, int del)

    removes an entry from the pending array

    :param struct visorhba_devdata \*devdata:
        Device holding the pending array

    :param int del:
        Entry to remove

.. _`del_scsipending_ent.description`:

Description
-----------

Removes the entry pointed at by del and returns it.
Returns the scsipending entry pointed at

.. _`get_scsipending_cmdrsp`:

get_scsipending_cmdrsp
======================

.. c:function:: struct uiscmdrsp *get_scsipending_cmdrsp(struct visorhba_devdata *ddata, int ent)

    return the cmdrsp stored in a pending entry #ddata: Device holding the pending array

    :param struct visorhba_devdata \*ddata:
        *undescribed*

    :param int ent:
        Entry that stores the cmdrsp

.. _`get_scsipending_cmdrsp.description`:

Description
-----------

Each scsipending entry has a cmdrsp in it. The cmdrsp is only valid
if the "sent" field is not NULL
Returns a pointer to the cmdrsp.

.. _`forward_taskmgmt_command`:

forward_taskmgmt_command
========================

.. c:function:: int forward_taskmgmt_command(enum task_mgmt_types tasktype, struct scsi_cmnd *scsicmd)

    send taskmegmt command to the Service Partition

    :param enum task_mgmt_types tasktype:
        Type of taskmgmt command

    :param struct scsi_cmnd \*scsicmd:
        *undescribed*

.. _`forward_taskmgmt_command.description`:

Description
-----------

Create a cmdrsp packet and send it to the Serivce Partition
that will service this request.
Returns whether the command was queued successfully or not.

.. _`visorhba_abort_handler`:

visorhba_abort_handler
======================

.. c:function:: int visorhba_abort_handler(struct scsi_cmnd *scsicmd)

    Send TASK_MGMT_ABORT_TASK

    :param struct scsi_cmnd \*scsicmd:
        The scsicmd that needs aborted

.. _`visorhba_abort_handler.description`:

Description
-----------

Returns SUCCESS if inserted, failure otherwise

.. _`visorhba_device_reset_handler`:

visorhba_device_reset_handler
=============================

.. c:function:: int visorhba_device_reset_handler(struct scsi_cmnd *scsicmd)

    Send TASK_MGMT_LUN_RESET

    :param struct scsi_cmnd \*scsicmd:
        The scsicmd that needs aborted

.. _`visorhba_device_reset_handler.description`:

Description
-----------

Returns SUCCESS if inserted, failure otherwise

.. _`visorhba_bus_reset_handler`:

visorhba_bus_reset_handler
==========================

.. c:function:: int visorhba_bus_reset_handler(struct scsi_cmnd *scsicmd)

    Send TASK_MGMT_TARGET_RESET for each target on the bus

    :param struct scsi_cmnd \*scsicmd:
        The scsicmd that needs aborted

.. _`visorhba_bus_reset_handler.description`:

Description
-----------

Returns SUCCESS

.. _`visorhba_host_reset_handler`:

visorhba_host_reset_handler
===========================

.. c:function:: int visorhba_host_reset_handler(struct scsi_cmnd *scsicmd)

    Not supported

    :param struct scsi_cmnd \*scsicmd:
        The scsicmd that needs aborted

.. _`visorhba_host_reset_handler.description`:

Description
-----------

Not supported, return SUCCESS
Returns SUCCESS

.. _`visorhba_get_info`:

visorhba_get_info
=================

.. c:function:: const char *visorhba_get_info(struct Scsi_Host *shp)

    :param struct Scsi_Host \*shp:
        Scsi host that is requesting information

.. _`visorhba_get_info.description`:

Description
-----------

Returns string with info

.. _`visorhba_queue_command_lck`:

visorhba_queue_command_lck
==========================

.. c:function:: int visorhba_queue_command_lck(struct scsi_cmnd *scsicmd, void (*) visorhba_cmnd_done (struct scsi_cmnd *)

    - queues command to the Service Partition

    :param struct scsi_cmnd \*scsicmd:
        Command to be queued

    :param (void (\*) visorhba_cmnd_done (struct scsi_cmnd \*):
        *undescribed*

.. _`visorhba_queue_command_lck.description`:

Description
-----------

Queues to scsicmd to the ServicePartition after converting it to a
uiscmdrsp structure.

Returns success if queued to the Service Partition, otherwise
failure.

.. _`visorhba_slave_alloc`:

visorhba_slave_alloc
====================

.. c:function:: int visorhba_slave_alloc(struct scsi_device *scsidev)

    called when new disk is discovered

    :param struct scsi_device \*scsidev:
        New disk

.. _`visorhba_slave_alloc.description`:

Description
-----------

Create a new visordisk_info structure and add it to our
list of vdisks.

Returns success when created, otherwise error.

.. _`visorhba_slave_destroy`:

visorhba_slave_destroy
======================

.. c:function:: void visorhba_slave_destroy(struct scsi_device *scsidev)

    disk is going away

    :param struct scsi_device \*scsidev:
        scsi device going away

.. _`visorhba_slave_destroy.description`:

Description
-----------

Disk is going away, clean up resources.
Returns void.

.. _`info_debugfs_read`:

info_debugfs_read
=================

.. c:function:: ssize_t info_debugfs_read(struct file *file, char __user *buf, size_t len, loff_t *offset)

    debugfs interface to dump visorhba states

    :param struct file \*file:
        Debug file

    :param char __user \*buf:
        buffer to send back to user

    :param size_t len:
        len that can be written to buf

    :param loff_t \*offset:
        offset into buf

.. _`info_debugfs_read.description`:

Description
-----------

Dumps information about the visorhba driver and devices

.. _`info_debugfs_read.todo`:

TODO
----

Make this per vhba
Returns bytes_read

.. _`visorhba_serverdown_complete`:

visorhba_serverdown_complete
============================

.. c:function:: void visorhba_serverdown_complete(struct visorhba_devdata *devdata)

    Called when we are done cleaning up from serverdown

    :param struct visorhba_devdata \*devdata:
        *undescribed*

.. _`visorhba_serverdown_complete.description`:

Description
-----------

Called when we are done cleanning up from serverdown, stop processing
queue, fail pending IOs.
Returns void when finished cleaning up

.. _`visorhba_serverdown`:

visorhba_serverdown
===================

.. c:function:: int visorhba_serverdown(struct visorhba_devdata *devdata)

    Got notified that the IOVM is down

    :param struct visorhba_devdata \*devdata:
        visorhba that is being serviced by downed IOVM.

.. _`visorhba_serverdown.description`:

Description
-----------

Something happened to the IOVM, return immediately and
schedule work cleanup work.
Return SUCCESS or EINVAL

.. _`do_scsi_linuxstat`:

do_scsi_linuxstat
=================

.. c:function:: void do_scsi_linuxstat(struct uiscmdrsp *cmdrsp, struct scsi_cmnd *scsicmd)

    scsi command returned linuxstat

    :param struct uiscmdrsp \*cmdrsp:
        response from IOVM

    :param struct scsi_cmnd \*scsicmd:
        Command issued.

.. _`do_scsi_linuxstat.description`:

Description
-----------

Don't log errors for disk-not-present inquiries
Returns void

.. _`do_scsi_nolinuxstat`:

do_scsi_nolinuxstat
===================

.. c:function:: void do_scsi_nolinuxstat(struct uiscmdrsp *cmdrsp, struct scsi_cmnd *scsicmd)

    scsi command didn't have linuxstat

    :param struct uiscmdrsp \*cmdrsp:
        response from IOVM

    :param struct scsi_cmnd \*scsicmd:
        Command issued.

.. _`do_scsi_nolinuxstat.description`:

Description
-----------

Handle response when no linuxstat was returned
Returns void

.. _`complete_scsi_command`:

complete_scsi_command
=====================

.. c:function:: void complete_scsi_command(struct uiscmdrsp *cmdrsp, struct scsi_cmnd *scsicmd)

    complete a scsi command

    :param struct uiscmdrsp \*cmdrsp:
        *undescribed*

    :param struct scsi_cmnd \*scsicmd:
        The scsi command

.. _`complete_scsi_command.description`:

Description
-----------

Response returned by the Service Partition, finish it and send
completion to the scsi midlayer.
Returns void.

.. _`complete_taskmgmt_command`:

complete_taskmgmt_command
=========================

.. c:function:: void complete_taskmgmt_command(struct uiscmdrsp *cmdrsp)

    complete task management

    :param struct uiscmdrsp \*cmdrsp:
        Response from the IOVM

.. _`complete_taskmgmt_command.description`:

Description
-----------

Service Partition returned the result of the task management
command. Wake up anyone waiting for it.
Returns void

.. _`queue_disk_add_remove`:

queue_disk_add_remove
=====================

.. c:function:: void queue_disk_add_remove(struct diskaddremove *dar)

    IOSP has sent us a add/remove request

    :param struct diskaddremove \*dar:
        disk add/remove request

.. _`queue_disk_add_remove.description`:

Description
-----------

Queue the work needed to add/remove a disk.
Returns void

.. _`process_disk_notify`:

process_disk_notify
===================

.. c:function:: void process_disk_notify(struct Scsi_Host *shost, struct uiscmdrsp *cmdrsp)

    IOSP has sent a process disk notify event

    :param struct Scsi_Host \*shost:
        Scsi hot

    :param struct uiscmdrsp \*cmdrsp:
        Response from the IOSP

.. _`process_disk_notify.description`:

Description
-----------

Queue it to the work queue.
Return void.

.. _`drain_queue`:

drain_queue
===========

.. c:function:: void drain_queue(struct uiscmdrsp *cmdrsp, struct visorhba_devdata *devdata)

    pull responses out of iochannel

    :param struct uiscmdrsp \*cmdrsp:
        Response from the IOSP

    :param struct visorhba_devdata \*devdata:
        device that owns this iochannel

.. _`drain_queue.description`:

Description
-----------

Pulls responses out of the iochannel and process the responses.
Restuns void

.. _`process_incoming_rsps`:

process_incoming_rsps
=====================

.. c:function:: int process_incoming_rsps(void *v)

    Process responses from IOSP

    :param void \*v:
        void pointer to visorhba_devdata

.. _`process_incoming_rsps.description`:

Description
-----------

Main function for the thread that processes the responses
from the IO Service Partition. When the queue is empty, wait
to check to see if it is full again.

.. _`visorhba_pause`:

visorhba_pause
==============

.. c:function:: int visorhba_pause(struct visor_device *dev, visorbus_state_complete_func complete_func)

    function to handle visorbus pause messages

    :param struct visor_device \*dev:
        device that is pausing.

    :param visorbus_state_complete_func complete_func:
        function to call when finished

.. _`visorhba_pause.description`:

Description
-----------

Something has happened to the IO Service Partition that is
handling this device. Quiet this device and reset commands
so that the Service Partition can be corrected.
Returns SUCCESS

.. _`visorhba_resume`:

visorhba_resume
===============

.. c:function:: int visorhba_resume(struct visor_device *dev, visorbus_state_complete_func complete_func)

    function called when the IO Service Partition is back

    :param struct visor_device \*dev:
        device that is pausing.

    :param visorbus_state_complete_func complete_func:
        function to call when finished

.. _`visorhba_resume.description`:

Description
-----------

Yay! The IO Service Partition is back, the channel has been wiped
so lets re-establish connection and start processing responses.
Returns 0 on success, error on failure.

.. _`visorhba_probe`:

visorhba_probe
==============

.. c:function:: int visorhba_probe(struct visor_device *dev)

    device has been discovered, do acquire

    :param struct visor_device \*dev:
        visor_device that was discovered

.. _`visorhba_probe.description`:

Description
-----------

A new HBA was discovered, do the initial connections of it.
Return 0 on success, otherwise error.

.. _`visorhba_remove`:

visorhba_remove
===============

.. c:function:: void visorhba_remove(struct visor_device *dev)

    remove a visorhba device

    :param struct visor_device \*dev:
        Device to remove

.. _`visorhba_remove.description`:

Description
-----------

Removes the visorhba device.
Returns void.

.. _`visorhba_init`:

visorhba_init
=============

.. c:function:: int visorhba_init( void)

    driver init routine

    :param  void:
        no arguments

.. _`visorhba_init.description`:

Description
-----------

Initialize the visorhba driver and register it with visorbus
to handle s-Par virtual host bus adapter.

.. _`visorhba_exit`:

visorhba_exit
=============

.. c:function:: void visorhba_exit( void)

    driver exit routine

    :param  void:
        no arguments

.. _`visorhba_exit.description`:

Description
-----------

Unregister driver from the bus and free up memory.

.. This file was automatic generated / don't edit.

