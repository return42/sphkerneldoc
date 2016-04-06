.. -*- coding: utf-8; mode: rst -*-

=============
libata-scsi.c
=============



.. _xref_ata_std_bios_param:

ata_std_bios_param
==================

.. c:function:: int ata_std_bios_param (struct scsi_device * sdev, struct block_device * bdev, sector_t capacity, int geom[])

    generic bios head/sector/cylinder calculator used by sd.

    :param struct scsi_device * sdev:
        SCSI device for which BIOS geometry is to be determined

    :param struct block_device * bdev:
        block device associated with **sdev**

    :param sector_t capacity:
        capacity of SCSI device

    :param int geom[]:



Description
-----------

	Generic bios head/sector/cylinder calculator
	used by sd. Most BIOSes nowadays expect a XXX/255/16  (CHS)
	mapping. Some situations may arise where the disk is not
	bootable if this is not used.



LOCKING
-------

	Defined by the SCSI layer.  We don't really care.



RETURNS
-------

	Zero.




.. _xref_ata_scsi_unlock_native_capacity:

ata_scsi_unlock_native_capacity
===============================

.. c:function:: void ata_scsi_unlock_native_capacity (struct scsi_device * sdev)

    unlock native capacity

    :param struct scsi_device * sdev:
        SCSI device to adjust device capacity for



Description
-----------

	This function is called if a partition on **sdev** extends beyond
	the end of the device.  It requests EH to unlock HPA.



LOCKING
-------

	Defined by the SCSI layer.  Might sleep.




.. _xref_ata_get_identity:

ata_get_identity
================

.. c:function:: int ata_get_identity (struct ata_port * ap, struct scsi_device * sdev, void __user * arg)

    Handler for HDIO_GET_IDENTITY ioctl

    :param struct ata_port * ap:
        target port

    :param struct scsi_device * sdev:
        SCSI device to get identify data for

    :param void __user * arg:
        User buffer area for identify data



LOCKING
-------

	Defined by the SCSI layer.  We don't really care.



RETURNS
-------

	Zero on success, negative errno on error.




.. _xref_ata_cmd_ioctl:

ata_cmd_ioctl
=============

.. c:function:: int ata_cmd_ioctl (struct scsi_device * scsidev, void __user * arg)

    Handler for HDIO_DRIVE_CMD ioctl

    :param struct scsi_device * scsidev:
        Device to which we are issuing command

    :param void __user * arg:
        User provided data for issuing command



LOCKING
-------

	Defined by the SCSI layer.  We don't really care.



RETURNS
-------

	Zero on success, negative errno on error.




.. _xref_ata_task_ioctl:

ata_task_ioctl
==============

.. c:function:: int ata_task_ioctl (struct scsi_device * scsidev, void __user * arg)

    Handler for HDIO_DRIVE_TASK ioctl

    :param struct scsi_device * scsidev:
        Device to which we are issuing command

    :param void __user * arg:
        User provided data for issuing command



LOCKING
-------

	Defined by the SCSI layer.  We don't really care.



RETURNS
-------

	Zero on success, negative errno on error.




.. _xref_ata_scsi_qc_new:

ata_scsi_qc_new
===============

.. c:function:: struct ata_queued_cmd * ata_scsi_qc_new (struct ata_device * dev, struct scsi_cmnd * cmd)

    acquire new ata_queued_cmd reference

    :param struct ata_device * dev:
        ATA device to which the new command is attached

    :param struct scsi_cmnd * cmd:
        SCSI command that originated this ATA command



Description
-----------

	Obtain a reference to an unused ata_queued_cmd structure,
	which is the basic libata structure representing a single
	ATA command sent to the hardware.


	If a command was available, fill in the SCSI-specific
	portions of the structure with information on the
	current command.



LOCKING
-------

	spin_lock_irqsave(host lock)



RETURNS
-------

	Command allocated, or ``NULL`` if none available.




.. _xref_ata_dump_status:

ata_dump_status
===============

.. c:function:: void ata_dump_status (unsigned id, struct ata_taskfile * tf)

    user friendly display of error info

    :param unsigned id:
        id of the port in question

    :param struct ata_taskfile * tf:
        ptr to filled out taskfile



Description
-----------

	Decode and dump the ATA error/status registers for the user so
	that they have some idea what really happened at the non
	make-believe layer.



LOCKING
-------

	inherited from caller




.. _xref_ata_to_sense_error:

ata_to_sense_error
==================

.. c:function:: void ata_to_sense_error (unsigned id, u8 drv_stat, u8 drv_err, u8 * sk, u8 * asc, u8 * ascq, int verbose)

    convert ATA error to SCSI error

    :param unsigned id:
        ATA device number

    :param u8 drv_stat:
        value contained in ATA status register

    :param u8 drv_err:
        value contained in ATA error register

    :param u8 * sk:
        the sense key we'll fill out

    :param u8 * asc:
        the additional sense code we'll fill out

    :param u8 * ascq:
        the additional sense code qualifier we'll fill out

    :param int verbose:
        be verbose



Description
-----------

	Converts an ATA error into a SCSI error.  Fill out pointers to
	SK, ASC, and ASCQ bytes for later use in fixed or descriptor
	format sense blocks.



LOCKING
-------

	spin_lock_irqsave(host lock)




.. _xref_ata_gen_ata_sense:

ata_gen_ata_sense
=================

.. c:function:: void ata_gen_ata_sense (struct ata_queued_cmd * qc)

    generate a SCSI fixed sense block

    :param struct ata_queued_cmd * qc:
        Command that we are erroring out



Description
-----------

	Generate sense block for a failed ATA command **qc**.  Descriptor
	format is used to accommodate LBA48 block address.



LOCKING
-------

	None.




.. _xref_atapi_drain_needed:

atapi_drain_needed
==================

.. c:function:: int atapi_drain_needed (struct request * rq)

    Check whether data transfer may overflow

    :param struct request * rq:
        request to be checked



Description
-----------

	ATAPI commands which transfer variable length data to host
	might overflow due to application error or hardare bug.  This
	function checks whether overflow should be drained and ignored
	for **request**.



LOCKING
-------

	None.



RETURNS
-------

	1 if ; otherwise, 0.




.. _xref_ata_scsi_slave_config:

ata_scsi_slave_config
=====================

.. c:function:: int ata_scsi_slave_config (struct scsi_device * sdev)

    Set SCSI device attributes

    :param struct scsi_device * sdev:
        SCSI device to examine



Description
-----------

	This is called before we actually start reading
	and writing to the device, to configure certain
	SCSI mid-layer behaviors.



LOCKING
-------

	Defined by SCSI layer.  We don't really care.




.. _xref_ata_scsi_slave_destroy:

ata_scsi_slave_destroy
======================

.. c:function:: void ata_scsi_slave_destroy (struct scsi_device * sdev)

    SCSI device is about to be destroyed

    :param struct scsi_device * sdev:
        SCSI device to be destroyed



Description
-----------

	**sdev** is about to be destroyed for hot/warm unplugging.  If
	this unplugging was initiated by libata as indicated by NULL
	dev->sdev, this function doesn't have to do anything.
	Otherwise, SCSI layer initiated warm-unplug is in progress.
	Clear dev->sdev, schedule the device for ATA detach and invoke
	EH.



LOCKING
-------

	Defined by SCSI layer.  We don't really care.




.. _xref___ata_change_queue_depth:

__ata_change_queue_depth
========================

.. c:function:: int __ata_change_queue_depth (struct ata_port * ap, struct scsi_device * sdev, int queue_depth)

    helper for ata_scsi_change_queue_depth

    :param struct ata_port * ap:
        ATA port to which the device change the queue depth

    :param struct scsi_device * sdev:
        SCSI device to configure queue depth for

    :param int queue_depth:
        new queue depth



Description
-----------

	libsas and libata have different approaches for associating a sdev to
	its ata_port.




.. _xref_ata_scsi_change_queue_depth:

ata_scsi_change_queue_depth
===========================

.. c:function:: int ata_scsi_change_queue_depth (struct scsi_device * sdev, int queue_depth)

    SCSI callback for queue depth config

    :param struct scsi_device * sdev:
        SCSI device to configure queue depth for

    :param int queue_depth:
        new queue depth



Description
-----------

	This is libata standard hostt->change_queue_depth callback.
	SCSI will call into this callback when user tries to set queue
	depth via sysfs.



LOCKING
-------

	SCSI layer (we don't care)



RETURNS
-------

	Newly configured queue depth.




.. _xref_ata_scsi_start_stop_xlat:

ata_scsi_start_stop_xlat
========================

.. c:function:: unsigned int ata_scsi_start_stop_xlat (struct ata_queued_cmd * qc)

    Translate SCSI START STOP UNIT command

    :param struct ata_queued_cmd * qc:
        Storage for translated ATA taskfile



Description
-----------

	Sets up an ATA taskfile to issue STANDBY (to stop) or READ VERIFY
	(to start). Perhaps these commands should be preceded by
	CHECK POWER MODE to see what power mode the device is already in.
	[See SAT revision 5 at www.t10.org]



LOCKING
-------

	spin_lock_irqsave(host lock)



RETURNS
-------

	Zero on success, non-zero on error.




.. _xref_ata_scsi_flush_xlat:

ata_scsi_flush_xlat
===================

.. c:function:: unsigned int ata_scsi_flush_xlat (struct ata_queued_cmd * qc)

    Translate SCSI SYNCHRONIZE CACHE command

    :param struct ata_queued_cmd * qc:
        Storage for translated ATA taskfile



Description
-----------

	Sets up an ATA taskfile to issue FLUSH CACHE or
	FLUSH CACHE EXT.



LOCKING
-------

	spin_lock_irqsave(host lock)



RETURNS
-------

	Zero on success, non-zero on error.




.. _xref_scsi_6_lba_len:

scsi_6_lba_len
==============

.. c:function:: void scsi_6_lba_len (const u8 * cdb, u64 * plba, u32 * plen)

    Get LBA and transfer length

    :param const u8 * cdb:
        SCSI command to translate

    :param u64 * plba:
        the LBA

    :param u32 * plen:
        the transfer length



Description
-----------

	Calculate LBA and transfer length for 6-byte commands.




.. _xref_scsi_10_lba_len:

scsi_10_lba_len
===============

.. c:function:: void scsi_10_lba_len (const u8 * cdb, u64 * plba, u32 * plen)

    Get LBA and transfer length

    :param const u8 * cdb:
        SCSI command to translate

    :param u64 * plba:
        the LBA

    :param u32 * plen:
        the transfer length



Description
-----------

	Calculate LBA and transfer length for 10-byte commands.




.. _xref_scsi_16_lba_len:

scsi_16_lba_len
===============

.. c:function:: void scsi_16_lba_len (const u8 * cdb, u64 * plba, u32 * plen)

    Get LBA and transfer length

    :param const u8 * cdb:
        SCSI command to translate

    :param u64 * plba:
        the LBA

    :param u32 * plen:
        the transfer length



Description
-----------

	Calculate LBA and transfer length for 16-byte commands.




.. _xref_ata_scsi_verify_xlat:

ata_scsi_verify_xlat
====================

.. c:function:: unsigned int ata_scsi_verify_xlat (struct ata_queued_cmd * qc)

    Translate SCSI VERIFY command into an ATA one

    :param struct ata_queued_cmd * qc:
        Storage for translated ATA taskfile



Description
-----------

	Converts SCSI VERIFY command to an ATA READ VERIFY command.



LOCKING
-------

	spin_lock_irqsave(host lock)



RETURNS
-------

	Zero on success, non-zero on error.




.. _xref_ata_scsi_rw_xlat:

ata_scsi_rw_xlat
================

.. c:function:: unsigned int ata_scsi_rw_xlat (struct ata_queued_cmd * qc)

    Translate SCSI r/w command into an ATA one

    :param struct ata_queued_cmd * qc:
        Storage for translated ATA taskfile



Description
-----------

	Converts any of six SCSI read/write commands into the
	ATA counterpart, including starting sector (LBA),
	sector count, and taking into account the device's LBA48
	support.


	Commands ``READ_6``, ``READ_10``, ``READ_16``, ``WRITE_6``, ``WRITE_10``, and
	``WRITE_16`` are currently supported.



LOCKING
-------

	spin_lock_irqsave(host lock)



RETURNS
-------

	Zero on success, non-zero on error.




.. _xref_ata_scsi_translate:

ata_scsi_translate
==================

.. c:function:: int ata_scsi_translate (struct ata_device * dev, struct scsi_cmnd * cmd, ata_xlat_func_t xlat_func)

    Translate then issue SCSI command to ATA device

    :param struct ata_device * dev:
        ATA device to which the command is addressed

    :param struct scsi_cmnd * cmd:
        SCSI command to execute

    :param ata_xlat_func_t xlat_func:
        Actor which translates **cmd** to an ATA taskfile



Description
-----------

	Our ->:c:func:`queuecommand` function has decided that the SCSI
	command issued can be directly translated into an ATA
	command, rather than handled internally.


	This function sets up an ata_queued_cmd structure for the
	SCSI command, and sends that ata_queued_cmd to the hardware.


	The xlat_func argument (actor) returns 0 if ready to execute
	ATA command, else 1 to finish translation. If 1 is returned
	then cmd->result (and possibly cmd->sense_buffer) are assumed
	to be set reflecting an error condition or clean (early)
	termination.



LOCKING
-------

	spin_lock_irqsave(host lock)



RETURNS
-------

	0 on success, SCSI_ML_QUEUE_DEVICE_BUSY if the command
	needs to be deferred.




.. _xref_ata_scsi_rbuf_get:

ata_scsi_rbuf_get
=================

.. c:function:: void * ata_scsi_rbuf_get (struct scsi_cmnd * cmd, bool copy_in, unsigned long * flags)

    Map response buffer.

    :param struct scsi_cmnd * cmd:
        SCSI command containing buffer to be mapped.

    :param bool copy_in:
        copy in from user buffer

    :param unsigned long * flags:
        unsigned long variable to store irq enable status



Description
-----------

	Prepare buffer for simulated SCSI commands.



LOCKING
-------

	spin_lock_irqsave(ata_scsi_rbuf_lock) on success



RETURNS
-------

	Pointer to response buffer.




.. _xref_ata_scsi_rbuf_put:

ata_scsi_rbuf_put
=================

.. c:function:: void ata_scsi_rbuf_put (struct scsi_cmnd * cmd, bool copy_out, unsigned long * flags)

    Unmap response buffer.

    :param struct scsi_cmnd * cmd:
        SCSI command containing buffer to be unmapped.

    :param bool copy_out:
        copy out result

    :param unsigned long * flags:
        **flags** passed to :c:func:`ata_scsi_rbuf_get`



Description
-----------

	Returns rbuf buffer.  The result is copied to **cmd**'s buffer if
	**copy_back** is true.



LOCKING
-------

	Unlocks ata_scsi_rbuf_lock.




.. _xref_ata_scsi_rbuf_fill:

ata_scsi_rbuf_fill
==================

.. c:function:: void ata_scsi_rbuf_fill (struct ata_scsi_args * args, unsigned int (*actor) (struct ata_scsi_args *args, u8 *rbuf)

    wrapper for SCSI command simulators

    :param struct ata_scsi_args * args:
        device IDENTIFY data / SCSI command of interest.

    :param unsigned int (*)(struct ata_scsi_args *args, u8 *rbuf) actor:
        Callback hook for desired SCSI command simulator



Description
-----------

	Takes care of the hard work of simulating a SCSI command...
	Mapping the response buffer, calling the command's handler,
	and handling the handler's return value.  This return value
	indicates whether the handler wishes the SCSI command to be
	completed successfully (0), or not (in which case cmd->result
	and sense buffer are assumed to be set).



LOCKING
-------

	spin_lock_irqsave(host lock)




.. _xref_ata_scsiop_inq_std:

ata_scsiop_inq_std
==================

.. c:function:: unsigned int ata_scsiop_inq_std (struct ata_scsi_args * args, u8 * rbuf)

    Simulate INQUIRY command

    :param struct ata_scsi_args * args:
        device IDENTIFY data / SCSI command of interest.

    :param u8 * rbuf:
        Response buffer, to which simulated SCSI cmd output is sent.



Description
-----------

	Returns standard device identification data associated
	with non-VPD INQUIRY command output.



LOCKING
-------

	spin_lock_irqsave(host lock)




.. _xref_ata_scsiop_inq_00:

ata_scsiop_inq_00
=================

.. c:function:: unsigned int ata_scsiop_inq_00 (struct ata_scsi_args * args, u8 * rbuf)

    Simulate INQUIRY VPD page 0, list of pages

    :param struct ata_scsi_args * args:
        device IDENTIFY data / SCSI command of interest.

    :param u8 * rbuf:
        Response buffer, to which simulated SCSI cmd output is sent.



Description
-----------

	Returns list of inquiry VPD pages available.



LOCKING
-------

	spin_lock_irqsave(host lock)




.. _xref_ata_scsiop_inq_80:

ata_scsiop_inq_80
=================

.. c:function:: unsigned int ata_scsiop_inq_80 (struct ata_scsi_args * args, u8 * rbuf)

    Simulate INQUIRY VPD page 80, device serial number

    :param struct ata_scsi_args * args:
        device IDENTIFY data / SCSI command of interest.

    :param u8 * rbuf:
        Response buffer, to which simulated SCSI cmd output is sent.



Description
-----------

	Returns ATA device serial number.



LOCKING
-------

	spin_lock_irqsave(host lock)




.. _xref_ata_scsiop_inq_83:

ata_scsiop_inq_83
=================

.. c:function:: unsigned int ata_scsiop_inq_83 (struct ata_scsi_args * args, u8 * rbuf)

    Simulate INQUIRY VPD page 83, device identity

    :param struct ata_scsi_args * args:
        device IDENTIFY data / SCSI command of interest.

    :param u8 * rbuf:
        Response buffer, to which simulated SCSI cmd output is sent.



Yields two logical unit device identification designators
---------------------------------------------------------

	 - vendor specific ASCII containing the ATA serial number
	 - SAT defined "t10 vendor id based" containing ASCII vendor
	   name ("ATA     "), model and serial numbers.



LOCKING
-------

	spin_lock_irqsave(host lock)




.. _xref_ata_scsiop_inq_89:

ata_scsiop_inq_89
=================

.. c:function:: unsigned int ata_scsiop_inq_89 (struct ata_scsi_args * args, u8 * rbuf)

    Simulate INQUIRY VPD page 89, ATA info

    :param struct ata_scsi_args * args:
        device IDENTIFY data / SCSI command of interest.

    :param u8 * rbuf:
        Response buffer, to which simulated SCSI cmd output is sent.



Description
-----------

	Yields SAT-specified ATA VPD page.



LOCKING
-------

	spin_lock_irqsave(host lock)




.. _xref_ata_scsiop_noop:

ata_scsiop_noop
===============

.. c:function:: unsigned int ata_scsiop_noop (struct ata_scsi_args * args, u8 * rbuf)

    Command handler that simply returns success.

    :param struct ata_scsi_args * args:
        device IDENTIFY data / SCSI command of interest.

    :param u8 * rbuf:
        Response buffer, to which simulated SCSI cmd output is sent.



Description
-----------

	No operation.  Simply returns success to caller, to indicate
	that the caller should successfully complete this SCSI command.



LOCKING
-------

	spin_lock_irqsave(host lock)




.. _xref_modecpy:

modecpy
=======

.. c:function:: void modecpy (u8 * dest, const u8 * src, int n, bool changeable)

    Prepare response for MODE SENSE

    :param u8 * dest:
        output buffer

    :param const u8 * src:
        data being copied

    :param int n:
        length of mode page

    :param bool changeable:
        whether changeable parameters are requested



Description
-----------

	Generate a generic MODE SENSE page for either current or changeable
	parameters.



LOCKING
-------

	None.




.. _xref_ata_msense_caching:

ata_msense_caching
==================

.. c:function:: unsigned int ata_msense_caching (u16 * id, u8 * buf, bool changeable)

    Simulate MODE SENSE caching info page

    :param u16 * id:
        device IDENTIFY data

    :param u8 * buf:
        output buffer

    :param bool changeable:
        whether changeable parameters are requested



Description
-----------

	Generate a caching info page, which conditionally indicates
	write caching to the SCSI layer, depending on device
	capabilities.



LOCKING
-------

	None.




.. _xref_ata_msense_ctl_mode:

ata_msense_ctl_mode
===================

.. c:function:: unsigned int ata_msense_ctl_mode (u8 * buf, bool changeable)

    Simulate MODE SENSE control mode page

    :param u8 * buf:
        output buffer

    :param bool changeable:
        whether changeable parameters are requested



Description
-----------

	Generate a generic MODE SENSE control mode page.



LOCKING
-------

	None.




.. _xref_ata_msense_rw_recovery:

ata_msense_rw_recovery
======================

.. c:function:: unsigned int ata_msense_rw_recovery (u8 * buf, bool changeable)

    Simulate MODE SENSE r/w error recovery page

    :param u8 * buf:
        output buffer

    :param bool changeable:
        whether changeable parameters are requested



Description
-----------

	Generate a generic MODE SENSE r/w error recovery page.



LOCKING
-------

	None.




.. _xref_ata_scsiop_mode_sense:

ata_scsiop_mode_sense
=====================

.. c:function:: unsigned int ata_scsiop_mode_sense (struct ata_scsi_args * args, u8 * rbuf)

    Simulate MODE SENSE 6, 10 commands

    :param struct ata_scsi_args * args:
        device IDENTIFY data / SCSI command of interest.

    :param u8 * rbuf:
        Response buffer, to which simulated SCSI cmd output is sent.



Description
-----------

	Simulate MODE SENSE commands. Assume this is invoked for direct
	access devices (e.g. disks) only. There should be no block
	descriptor for other device types.



LOCKING
-------

	spin_lock_irqsave(host lock)




.. _xref_ata_scsiop_read_cap:

ata_scsiop_read_cap
===================

.. c:function:: unsigned int ata_scsiop_read_cap (struct ata_scsi_args * args, u8 * rbuf)

    Simulate READ CAPACITY[ 16] commands

    :param struct ata_scsi_args * args:
        device IDENTIFY data / SCSI command of interest.

    :param u8 * rbuf:
        Response buffer, to which simulated SCSI cmd output is sent.



Description
-----------

	Simulate READ CAPACITY commands.



LOCKING
-------

	None.




.. _xref_ata_scsiop_report_luns:

ata_scsiop_report_luns
======================

.. c:function:: unsigned int ata_scsiop_report_luns (struct ata_scsi_args * args, u8 * rbuf)

    Simulate REPORT LUNS command

    :param struct ata_scsi_args * args:
        device IDENTIFY data / SCSI command of interest.

    :param u8 * rbuf:
        Response buffer, to which simulated SCSI cmd output is sent.



Description
-----------

	Simulate REPORT LUNS command.



LOCKING
-------

	spin_lock_irqsave(host lock)




.. _xref_atapi_xlat:

atapi_xlat
==========

.. c:function:: unsigned int atapi_xlat (struct ata_queued_cmd * qc)

    Initialize PACKET taskfile

    :param struct ata_queued_cmd * qc:
        command structure to be initialized



LOCKING
-------

	spin_lock_irqsave(host lock)



RETURNS
-------

	Zero on success, non-zero on failure.




.. _xref_ata_scsi_find_dev:

ata_scsi_find_dev
=================

.. c:function:: struct ata_device * ata_scsi_find_dev (struct ata_port * ap, const struct scsi_device * scsidev)

    lookup ata_device from scsi_cmnd

    :param struct ata_port * ap:
        ATA port to which the device is attached

    :param const struct scsi_device * scsidev:
        SCSI device from which we derive the ATA device



Description
-----------

	Given various information provided in struct scsi_cmnd,
	map that onto an ATA bus, and using that mapping
	determine which ata_device is associated with the
	SCSI command to be sent.



LOCKING
-------

	spin_lock_irqsave(host lock)



RETURNS
-------

	Associated ATA device, or ``NULL`` if not found.




.. _xref_ata_scsi_pass_thru:

ata_scsi_pass_thru
==================

.. c:function:: unsigned int ata_scsi_pass_thru (struct ata_queued_cmd * qc)

    convert ATA pass-thru CDB to taskfile

    :param struct ata_queued_cmd * qc:
        command structure to be initialized



Description
-----------

	Handles either 12 or 16-byte versions of the CDB.



RETURNS
-------

	Zero on success, non-zero on failure.




.. _xref_ata_mselect_caching:

ata_mselect_caching
===================

.. c:function:: int ata_mselect_caching (struct ata_queued_cmd * qc, const u8 * buf, int len)

    Simulate MODE SELECT for caching info page

    :param struct ata_queued_cmd * qc:
        Storage for translated ATA taskfile

    :param const u8 * buf:
        input buffer

    :param int len:
        number of valid bytes in the input buffer



Description
-----------

	Prepare a taskfile to modify caching information for the device.



LOCKING
-------

	None.




.. _xref_ata_scsi_mode_select_xlat:

ata_scsi_mode_select_xlat
=========================

.. c:function:: unsigned int ata_scsi_mode_select_xlat (struct ata_queued_cmd * qc)

    Simulate MODE SELECT 6, 10 commands

    :param struct ata_queued_cmd * qc:
        Storage for translated ATA taskfile



Description
-----------

	Converts a MODE SELECT command to an ATA SET FEATURES taskfile.
	Assume this is invoked for direct access devices (e.g. disks) only.
	There should be no block descriptor for other device types.



LOCKING
-------

	spin_lock_irqsave(host lock)




.. _xref_ata_get_xlat_func:

ata_get_xlat_func
=================

.. c:function:: ata_xlat_func_t ata_get_xlat_func (struct ata_device * dev, u8 cmd)

    check if SCSI to ATA translation is possible

    :param struct ata_device * dev:
        ATA device

    :param u8 cmd:
        SCSI command opcode to consider



Description
-----------

	Look up the SCSI command given, and determine whether the
	SCSI command is to be translated or simulated.



RETURNS
-------

	Pointer to translation function if possible, ``NULL`` if not.




.. _xref_ata_scsi_dump_cdb:

ata_scsi_dump_cdb
=================

.. c:function:: void ata_scsi_dump_cdb (struct ata_port * ap, struct scsi_cmnd * cmd)

    dump SCSI command contents to dmesg

    :param struct ata_port * ap:
        ATA port to which the command was being sent

    :param struct scsi_cmnd * cmd:
        SCSI command to dump



Description
-----------

	Prints the contents of a SCSI command via :c:func:`printk`.




.. _xref_ata_scsi_queuecmd:

ata_scsi_queuecmd
=================

.. c:function:: int ata_scsi_queuecmd (struct Scsi_Host * shost, struct scsi_cmnd * cmd)

    Issue SCSI cdb to libata-managed device

    :param struct Scsi_Host * shost:
        SCSI host of command to be sent

    :param struct scsi_cmnd * cmd:
        SCSI command to be sent



Description
-----------

	In some cases, this function translates SCSI commands into
	ATA taskfiles, and queues the taskfiles to be sent to
	hardware.  In other cases, this function simulates a
	SCSI device by evaluating and responding to certain
	SCSI commands.  This creates the overall effect of
	ATA and ATAPI devices appearing as SCSI devices.



LOCKING
-------

	ATA host lock



RETURNS
-------

	Return value from :c:func:`__ata_scsi_queuecmd` if **cmd** can be queued,
	0 otherwise.




.. _xref_ata_scsi_simulate:

ata_scsi_simulate
=================

.. c:function:: void ata_scsi_simulate (struct ata_device * dev, struct scsi_cmnd * cmd)

    simulate SCSI command on ATA device

    :param struct ata_device * dev:
        the target device

    :param struct scsi_cmnd * cmd:
        SCSI command being sent to device.



Description
-----------

	Interprets and directly executes a select list of SCSI commands
	that can be handled internally.



LOCKING
-------

	spin_lock_irqsave(host lock)




.. _xref_ata_scsi_offline_dev:

ata_scsi_offline_dev
====================

.. c:function:: int ata_scsi_offline_dev (struct ata_device * dev)

    offline attached SCSI device

    :param struct ata_device * dev:
        ATA device to offline attached SCSI device for



Description
-----------

	This function is called from :c:func:`ata_eh_hotplug` and responsible
	for taking the SCSI device attached to **dev** offline.  This
	function is called with host lock which protects dev->sdev
	against clearing.



LOCKING
-------

	spin_lock_irqsave(host lock)



RETURNS
-------

	1 if attached SCSI device exists, 0 otherwise.




.. _xref_ata_scsi_remove_dev:

ata_scsi_remove_dev
===================

.. c:function:: void ata_scsi_remove_dev (struct ata_device * dev)

    remove attached SCSI device

    :param struct ata_device * dev:
        ATA device to remove attached SCSI device for



Description
-----------

	This function is called from :c:func:`ata_eh_scsi_hotplug` and
	responsible for removing the SCSI device attached to **dev**.



LOCKING
-------

	Kernel thread context (may sleep).




.. _xref_ata_scsi_media_change_notify:

ata_scsi_media_change_notify
============================

.. c:function:: void ata_scsi_media_change_notify (struct ata_device * dev)

    send media change event

    :param struct ata_device * dev:
        Pointer to the disk device with media change event



Description
-----------

	Tell the block layer to send a media change notification
	event.



LOCKING
-------

	spin_lock_irqsave(host lock)




.. _xref_ata_scsi_hotplug:

ata_scsi_hotplug
================

.. c:function:: void ata_scsi_hotplug (struct work_struct * work)

    SCSI part of hotplug

    :param struct work_struct * work:
        Pointer to ATA port to perform SCSI hotplug on



Description
-----------

	Perform SCSI part of hotplug.  It's executed from a separate
	workqueue after EH completes.  This is necessary because SCSI
	hot plugging requires working EH and hot unplugging is
	synchronized with hot plugging with a mutex.



LOCKING
-------

	Kernel thread context (may sleep).




.. _xref_ata_scsi_user_scan:

ata_scsi_user_scan
==================

.. c:function:: int ata_scsi_user_scan (struct Scsi_Host * shost, unsigned int channel, unsigned int id, u64 lun)

    indication for user-initiated bus scan

    :param struct Scsi_Host * shost:
        SCSI host to scan

    :param unsigned int channel:
        Channel to scan

    :param unsigned int id:
        ID to scan

    :param u64 lun:
        LUN to scan



Description
-----------

	This function is called when user explicitly requests bus
	scan.  Set probe pending flag and invoke EH.



LOCKING
-------

	SCSI layer (we don't care)



RETURNS
-------

	Zero.




.. _xref_ata_scsi_dev_rescan:

ata_scsi_dev_rescan
===================

.. c:function:: void ata_scsi_dev_rescan (struct work_struct * work)

    initiate scsi_rescan_device()

    :param struct work_struct * work:
        Pointer to ATA port to perform :c:func:`scsi_rescan_device`



Description
-----------

	After ATA pass thru (SAT) commands are executed successfully,
	libata need to propagate the changes to SCSI layer.



LOCKING
-------

	Kernel thread context (may sleep).




.. _xref_ata_sas_port_alloc:

ata_sas_port_alloc
==================

.. c:function:: struct ata_port * ata_sas_port_alloc (struct ata_host * host, struct ata_port_info * port_info, struct Scsi_Host * shost)

    Allocate port for a SAS attached SATA device

    :param struct ata_host * host:
        ATA host container for all SAS ports

    :param struct ata_port_info * port_info:
        Information from low-level host driver

    :param struct Scsi_Host * shost:
        SCSI host that the scsi device is attached to



LOCKING
-------

	PCI/etc. bus probe sem.



RETURNS
-------

	ata_port pointer on success / NULL on failure.




.. _xref_ata_sas_port_start:

ata_sas_port_start
==================

.. c:function:: int ata_sas_port_start (struct ata_port * ap)

    Set port up for dma.

    :param struct ata_port * ap:
        Port to initialize



Description
-----------

	Called just after data structures for each port are
	initialized.


	May be used as the :c:func:`port_start` entry in ata_port_operations.



LOCKING
-------

	Inherited from caller.




.. _xref_ata_sas_port_stop:

ata_sas_port_stop
=================

.. c:function:: void ata_sas_port_stop (struct ata_port * ap)

    Undo ata_sas_port_start()

    :param struct ata_port * ap:
        Port to shut down



Description
-----------

	May be used as the :c:func:`port_stop` entry in ata_port_operations.



LOCKING
-------

	Inherited from caller.




.. _xref_ata_sas_async_probe:

ata_sas_async_probe
===================

.. c:function:: void ata_sas_async_probe (struct ata_port * ap)

    simply schedule probing and return

    :param struct ata_port * ap:
        Port to probe



Description
-----------

For batch scheduling of probe for sas attached ata devices, assumes
the port has already been through :c:func:`ata_sas_port_init`




.. _xref_ata_sas_port_init:

ata_sas_port_init
=================

.. c:function:: int ata_sas_port_init (struct ata_port * ap)

    Initialize a SATA device

    :param struct ata_port * ap:
        SATA port to initialize



LOCKING
-------

	PCI/etc. bus probe sem.



RETURNS
-------

	Zero on success, non-zero on error.




.. _xref_ata_sas_port_destroy:

ata_sas_port_destroy
====================

.. c:function:: void ata_sas_port_destroy (struct ata_port * ap)

    Destroy a SATA port allocated by ata_sas_port_alloc

    :param struct ata_port * ap:
        SATA port to destroy




.. _xref_ata_sas_slave_configure:

ata_sas_slave_configure
=======================

.. c:function:: int ata_sas_slave_configure (struct scsi_device * sdev, struct ata_port * ap)

    Default slave_config routine for libata devices

    :param struct scsi_device * sdev:
        SCSI device to configure

    :param struct ata_port * ap:
        ATA port to which SCSI device is attached



RETURNS
-------

	Zero.




.. _xref_ata_sas_queuecmd:

ata_sas_queuecmd
================

.. c:function:: int ata_sas_queuecmd (struct scsi_cmnd * cmd, struct ata_port * ap)

    Issue SCSI cdb to libata-managed device

    :param struct scsi_cmnd * cmd:
        SCSI command to be sent

    :param struct ata_port * ap:
        ATA port to which the command is being sent



RETURNS
-------

	Return value from :c:func:`__ata_scsi_queuecmd` if **cmd** can be queued,
	0 otherwise.


