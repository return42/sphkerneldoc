.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/libata-scsi.c

.. _`ata_std_bios_param`:

ata_std_bios_param
==================

.. c:function:: int ata_std_bios_param(struct scsi_device *sdev, struct block_device *bdev, sector_t capacity, int geom)

    generic bios head/sector/cylinder calculator used by sd.

    :param sdev:
        SCSI device for which BIOS geometry is to be determined
    :type sdev: struct scsi_device \*

    :param bdev:
        block device associated with \ ``sdev``\ 
    :type bdev: struct block_device \*

    :param capacity:
        capacity of SCSI device
    :type capacity: sector_t

    :param geom:
        location to which geometry will be output
    :type geom: int

.. _`ata_std_bios_param.description`:

Description
-----------

     Generic bios head/sector/cylinder calculator
     used by sd. Most BIOSes nowadays expect a XXX/255/16  (CHS)
     mapping. Some situations may arise where the disk is not
     bootable if this is not used.

.. _`ata_std_bios_param.locking`:

LOCKING
-------

     Defined by the SCSI layer.  We don't really care.

.. _`ata_std_bios_param.return`:

Return
------

     Zero.

.. _`ata_scsi_unlock_native_capacity`:

ata_scsi_unlock_native_capacity
===============================

.. c:function:: void ata_scsi_unlock_native_capacity(struct scsi_device *sdev)

    unlock native capacity

    :param sdev:
        SCSI device to adjust device capacity for
    :type sdev: struct scsi_device \*

.. _`ata_scsi_unlock_native_capacity.description`:

Description
-----------

     This function is called if a partition on \ ``sdev``\  extends beyond
     the end of the device.  It requests EH to unlock HPA.

.. _`ata_scsi_unlock_native_capacity.locking`:

LOCKING
-------

     Defined by the SCSI layer.  Might sleep.

.. _`ata_get_identity`:

ata_get_identity
================

.. c:function:: int ata_get_identity(struct ata_port *ap, struct scsi_device *sdev, void __user *arg)

    Handler for HDIO_GET_IDENTITY ioctl

    :param ap:
        target port
    :type ap: struct ata_port \*

    :param sdev:
        SCSI device to get identify data for
    :type sdev: struct scsi_device \*

    :param arg:
        User buffer area for identify data
    :type arg: void __user \*

.. _`ata_get_identity.locking`:

LOCKING
-------

     Defined by the SCSI layer.  We don't really care.

.. _`ata_get_identity.return`:

Return
------

     Zero on success, negative errno on error.

.. _`ata_cmd_ioctl`:

ata_cmd_ioctl
=============

.. c:function:: int ata_cmd_ioctl(struct scsi_device *scsidev, void __user *arg)

    Handler for HDIO_DRIVE_CMD ioctl

    :param scsidev:
        Device to which we are issuing command
    :type scsidev: struct scsi_device \*

    :param arg:
        User provided data for issuing command
    :type arg: void __user \*

.. _`ata_cmd_ioctl.locking`:

LOCKING
-------

     Defined by the SCSI layer.  We don't really care.

.. _`ata_cmd_ioctl.return`:

Return
------

     Zero on success, negative errno on error.

.. _`ata_task_ioctl`:

ata_task_ioctl
==============

.. c:function:: int ata_task_ioctl(struct scsi_device *scsidev, void __user *arg)

    Handler for HDIO_DRIVE_TASK ioctl

    :param scsidev:
        Device to which we are issuing command
    :type scsidev: struct scsi_device \*

    :param arg:
        User provided data for issuing command
    :type arg: void __user \*

.. _`ata_task_ioctl.locking`:

LOCKING
-------

     Defined by the SCSI layer.  We don't really care.

.. _`ata_task_ioctl.return`:

Return
------

     Zero on success, negative errno on error.

.. _`ata_scsi_qc_new`:

ata_scsi_qc_new
===============

.. c:function:: struct ata_queued_cmd *ata_scsi_qc_new(struct ata_device *dev, struct scsi_cmnd *cmd)

    acquire new ata_queued_cmd reference

    :param dev:
        ATA device to which the new command is attached
    :type dev: struct ata_device \*

    :param cmd:
        SCSI command that originated this ATA command
    :type cmd: struct scsi_cmnd \*

.. _`ata_scsi_qc_new.description`:

Description
-----------

     Obtain a reference to an unused ata_queued_cmd structure,
     which is the basic libata structure representing a single
     ATA command sent to the hardware.

     If a command was available, fill in the SCSI-specific
     portions of the structure with information on the
     current command.

.. _`ata_scsi_qc_new.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_scsi_qc_new.return`:

Return
------

     Command allocated, or \ ``NULL``\  if none available.

.. _`ata_dump_status`:

ata_dump_status
===============

.. c:function:: void ata_dump_status(unsigned id, struct ata_taskfile *tf)

    user friendly display of error info

    :param id:
        id of the port in question
    :type id: unsigned

    :param tf:
        ptr to filled out taskfile
    :type tf: struct ata_taskfile \*

.. _`ata_dump_status.description`:

Description
-----------

     Decode and dump the ATA error/status registers for the user so
     that they have some idea what really happened at the non
     make-believe layer.

.. _`ata_dump_status.locking`:

LOCKING
-------

     inherited from caller

.. _`ata_to_sense_error`:

ata_to_sense_error
==================

.. c:function:: void ata_to_sense_error(unsigned id, u8 drv_stat, u8 drv_err, u8 *sk, u8 *asc, u8 *ascq, int verbose)

    convert ATA error to SCSI error

    :param id:
        ATA device number
    :type id: unsigned

    :param drv_stat:
        value contained in ATA status register
    :type drv_stat: u8

    :param drv_err:
        value contained in ATA error register
    :type drv_err: u8

    :param sk:
        the sense key we'll fill out
    :type sk: u8 \*

    :param asc:
        the additional sense code we'll fill out
    :type asc: u8 \*

    :param ascq:
        the additional sense code qualifier we'll fill out
    :type ascq: u8 \*

    :param verbose:
        be verbose
    :type verbose: int

.. _`ata_to_sense_error.description`:

Description
-----------

     Converts an ATA error into a SCSI error.  Fill out pointers to
     SK, ASC, and ASCQ bytes for later use in fixed or descriptor
     format sense blocks.

.. _`ata_to_sense_error.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_gen_ata_sense`:

ata_gen_ata_sense
=================

.. c:function:: void ata_gen_ata_sense(struct ata_queued_cmd *qc)

    generate a SCSI fixed sense block

    :param qc:
        Command that we are erroring out
    :type qc: struct ata_queued_cmd \*

.. _`ata_gen_ata_sense.description`:

Description
-----------

     Generate sense block for a failed ATA command \ ``qc``\ .  Descriptor
     format is used to accommodate LBA48 block address.

.. _`ata_gen_ata_sense.locking`:

LOCKING
-------

     None.

.. _`atapi_drain_needed`:

atapi_drain_needed
==================

.. c:function:: int atapi_drain_needed(struct request *rq)

    Check whether data transfer may overflow

    :param rq:
        request to be checked
    :type rq: struct request \*

.. _`atapi_drain_needed.description`:

Description
-----------

     ATAPI commands which transfer variable length data to host
     might overflow due to application error or hardware bug.  This
     function checks whether overflow should be drained and ignored
     for \ ``request``\ .

.. _`atapi_drain_needed.locking`:

LOCKING
-------

     None.

.. _`atapi_drain_needed.return`:

Return
------

     1 if ; otherwise, 0.

.. _`ata_scsi_slave_config`:

ata_scsi_slave_config
=====================

.. c:function:: int ata_scsi_slave_config(struct scsi_device *sdev)

    Set SCSI device attributes

    :param sdev:
        SCSI device to examine
    :type sdev: struct scsi_device \*

.. _`ata_scsi_slave_config.description`:

Description
-----------

     This is called before we actually start reading
     and writing to the device, to configure certain
     SCSI mid-layer behaviors.

.. _`ata_scsi_slave_config.locking`:

LOCKING
-------

     Defined by SCSI layer.  We don't really care.

.. _`ata_scsi_slave_destroy`:

ata_scsi_slave_destroy
======================

.. c:function:: void ata_scsi_slave_destroy(struct scsi_device *sdev)

    SCSI device is about to be destroyed

    :param sdev:
        SCSI device to be destroyed
    :type sdev: struct scsi_device \*

.. _`ata_scsi_slave_destroy.description`:

Description
-----------

     \ ``sdev``\  is about to be destroyed for hot/warm unplugging.  If
     this unplugging was initiated by libata as indicated by NULL
     dev->sdev, this function doesn't have to do anything.
     Otherwise, SCSI layer initiated warm-unplug is in progress.
     Clear dev->sdev, schedule the device for ATA detach and invoke
     EH.

.. _`ata_scsi_slave_destroy.locking`:

LOCKING
-------

     Defined by SCSI layer.  We don't really care.

.. _`__ata_change_queue_depth`:

__ata_change_queue_depth
========================

.. c:function:: int __ata_change_queue_depth(struct ata_port *ap, struct scsi_device *sdev, int queue_depth)

    helper for ata_scsi_change_queue_depth

    :param ap:
        ATA port to which the device change the queue depth
    :type ap: struct ata_port \*

    :param sdev:
        SCSI device to configure queue depth for
    :type sdev: struct scsi_device \*

    :param queue_depth:
        new queue depth
    :type queue_depth: int

.. _`__ata_change_queue_depth.description`:

Description
-----------

     libsas and libata have different approaches for associating a sdev to
     its ata_port.

.. _`ata_scsi_change_queue_depth`:

ata_scsi_change_queue_depth
===========================

.. c:function:: int ata_scsi_change_queue_depth(struct scsi_device *sdev, int queue_depth)

    SCSI callback for queue depth config

    :param sdev:
        SCSI device to configure queue depth for
    :type sdev: struct scsi_device \*

    :param queue_depth:
        new queue depth
    :type queue_depth: int

.. _`ata_scsi_change_queue_depth.description`:

Description
-----------

     This is libata standard hostt->change_queue_depth callback.
     SCSI will call into this callback when user tries to set queue
     depth via sysfs.

.. _`ata_scsi_change_queue_depth.locking`:

LOCKING
-------

     SCSI layer (we don't care)

.. _`ata_scsi_change_queue_depth.return`:

Return
------

     Newly configured queue depth.

.. _`ata_scsi_start_stop_xlat`:

ata_scsi_start_stop_xlat
========================

.. c:function:: unsigned int ata_scsi_start_stop_xlat(struct ata_queued_cmd *qc)

    Translate SCSI START STOP UNIT command

    :param qc:
        Storage for translated ATA taskfile
    :type qc: struct ata_queued_cmd \*

.. _`ata_scsi_start_stop_xlat.description`:

Description
-----------

     Sets up an ATA taskfile to issue STANDBY (to stop) or READ VERIFY
     (to start). Perhaps these commands should be preceded by
     CHECK POWER MODE to see what power mode the device is already in.
     [See SAT revision 5 at www.t10.org]

.. _`ata_scsi_start_stop_xlat.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_scsi_start_stop_xlat.return`:

Return
------

     Zero on success, non-zero on error.

.. _`ata_scsi_flush_xlat`:

ata_scsi_flush_xlat
===================

.. c:function:: unsigned int ata_scsi_flush_xlat(struct ata_queued_cmd *qc)

    Translate SCSI SYNCHRONIZE CACHE command

    :param qc:
        Storage for translated ATA taskfile
    :type qc: struct ata_queued_cmd \*

.. _`ata_scsi_flush_xlat.description`:

Description
-----------

     Sets up an ATA taskfile to issue FLUSH CACHE or
     FLUSH CACHE EXT.

.. _`ata_scsi_flush_xlat.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_scsi_flush_xlat.return`:

Return
------

     Zero on success, non-zero on error.

.. _`scsi_6_lba_len`:

scsi_6_lba_len
==============

.. c:function:: void scsi_6_lba_len(const u8 *cdb, u64 *plba, u32 *plen)

    Get LBA and transfer length

    :param cdb:
        SCSI command to translate
    :type cdb: const u8 \*

    :param plba:
        the LBA
    :type plba: u64 \*

    :param plen:
        the transfer length
    :type plen: u32 \*

.. _`scsi_6_lba_len.description`:

Description
-----------

     Calculate LBA and transfer length for 6-byte commands.

.. _`scsi_10_lba_len`:

scsi_10_lba_len
===============

.. c:function:: void scsi_10_lba_len(const u8 *cdb, u64 *plba, u32 *plen)

    Get LBA and transfer length

    :param cdb:
        SCSI command to translate
    :type cdb: const u8 \*

    :param plba:
        the LBA
    :type plba: u64 \*

    :param plen:
        the transfer length
    :type plen: u32 \*

.. _`scsi_10_lba_len.description`:

Description
-----------

     Calculate LBA and transfer length for 10-byte commands.

.. _`scsi_16_lba_len`:

scsi_16_lba_len
===============

.. c:function:: void scsi_16_lba_len(const u8 *cdb, u64 *plba, u32 *plen)

    Get LBA and transfer length

    :param cdb:
        SCSI command to translate
    :type cdb: const u8 \*

    :param plba:
        the LBA
    :type plba: u64 \*

    :param plen:
        the transfer length
    :type plen: u32 \*

.. _`scsi_16_lba_len.description`:

Description
-----------

     Calculate LBA and transfer length for 16-byte commands.

.. _`ata_scsi_verify_xlat`:

ata_scsi_verify_xlat
====================

.. c:function:: unsigned int ata_scsi_verify_xlat(struct ata_queued_cmd *qc)

    Translate SCSI VERIFY command into an ATA one

    :param qc:
        Storage for translated ATA taskfile
    :type qc: struct ata_queued_cmd \*

.. _`ata_scsi_verify_xlat.description`:

Description
-----------

     Converts SCSI VERIFY command to an ATA READ VERIFY command.

.. _`ata_scsi_verify_xlat.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_scsi_verify_xlat.return`:

Return
------

     Zero on success, non-zero on error.

.. _`ata_scsi_rw_xlat`:

ata_scsi_rw_xlat
================

.. c:function:: unsigned int ata_scsi_rw_xlat(struct ata_queued_cmd *qc)

    Translate SCSI r/w command into an ATA one

    :param qc:
        Storage for translated ATA taskfile
    :type qc: struct ata_queued_cmd \*

.. _`ata_scsi_rw_xlat.description`:

Description
-----------

     Converts any of six SCSI read/write commands into the
     ATA counterpart, including starting sector (LBA),
     sector count, and taking into account the device's LBA48
     support.

     Commands \ ``READ_6``\ , \ ``READ_10``\ , \ ``READ_16``\ , \ ``WRITE_6``\ , \ ``WRITE_10``\ , and
     \ ``WRITE_16``\  are currently supported.

.. _`ata_scsi_rw_xlat.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_scsi_rw_xlat.return`:

Return
------

     Zero on success, non-zero on error.

.. _`ata_scsi_translate`:

ata_scsi_translate
==================

.. c:function:: int ata_scsi_translate(struct ata_device *dev, struct scsi_cmnd *cmd, ata_xlat_func_t xlat_func)

    Translate then issue SCSI command to ATA device

    :param dev:
        ATA device to which the command is addressed
    :type dev: struct ata_device \*

    :param cmd:
        SCSI command to execute
    :type cmd: struct scsi_cmnd \*

    :param xlat_func:
        Actor which translates \ ``cmd``\  to an ATA taskfile
    :type xlat_func: ata_xlat_func_t

.. _`ata_scsi_translate.description`:

Description
-----------

     Our ->queuecommand() function has decided that the SCSI
     command issued can be directly translated into an ATA
     command, rather than handled internally.

     This function sets up an ata_queued_cmd structure for the
     SCSI command, and sends that ata_queued_cmd to the hardware.

     The xlat_func argument (actor) returns 0 if ready to execute
     ATA command, else 1 to finish translation. If 1 is returned
     then cmd->result (and possibly cmd->sense_buffer) are assumed
     to be set reflecting an error condition or clean (early)
     termination.

.. _`ata_scsi_translate.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_scsi_translate.return`:

Return
------

     0 on success, SCSI_ML_QUEUE_DEVICE_BUSY if the command
     needs to be deferred.

.. _`ata_scsi_rbuf_get`:

ata_scsi_rbuf_get
=================

.. c:function:: void *ata_scsi_rbuf_get(struct scsi_cmnd *cmd, bool copy_in, unsigned long *flags)

    Map response buffer.

    :param cmd:
        SCSI command containing buffer to be mapped.
    :type cmd: struct scsi_cmnd \*

    :param copy_in:
        copy in from user buffer
    :type copy_in: bool

    :param flags:
        unsigned long variable to store irq enable status
    :type flags: unsigned long \*

.. _`ata_scsi_rbuf_get.description`:

Description
-----------

     Prepare buffer for simulated SCSI commands.

.. _`ata_scsi_rbuf_get.locking`:

LOCKING
-------

     spin_lock_irqsave(ata_scsi_rbuf_lock) on success

.. _`ata_scsi_rbuf_get.return`:

Return
------

     Pointer to response buffer.

.. _`ata_scsi_rbuf_put`:

ata_scsi_rbuf_put
=================

.. c:function:: void ata_scsi_rbuf_put(struct scsi_cmnd *cmd, bool copy_out, unsigned long *flags)

    Unmap response buffer.

    :param cmd:
        SCSI command containing buffer to be unmapped.
    :type cmd: struct scsi_cmnd \*

    :param copy_out:
        copy out result
    :type copy_out: bool

    :param flags:
        \ ``flags``\  passed to \ :c:func:`ata_scsi_rbuf_get`\ 
    :type flags: unsigned long \*

.. _`ata_scsi_rbuf_put.description`:

Description
-----------

     Returns rbuf buffer.  The result is copied to \ ``cmd``\ 's buffer if
     \ ``copy_back``\  is true.

.. _`ata_scsi_rbuf_put.locking`:

LOCKING
-------

     Unlocks ata_scsi_rbuf_lock.

.. _`ata_scsi_rbuf_fill`:

ata_scsi_rbuf_fill
==================

.. c:function:: void ata_scsi_rbuf_fill(struct ata_scsi_args *args, unsigned int (*actor)(struct ata_scsi_args *args, u8 *rbuf))

    wrapper for SCSI command simulators

    :param args:
        device IDENTIFY data / SCSI command of interest.
    :type args: struct ata_scsi_args \*

    :param unsigned int (\*actor)(struct ata_scsi_args \*args, u8 \*rbuf):
        Callback hook for desired SCSI command simulator

.. _`ata_scsi_rbuf_fill.description`:

Description
-----------

     Takes care of the hard work of simulating a SCSI command...
     Mapping the response buffer, calling the command's handler,
     and handling the handler's return value.  This return value
     indicates whether the handler wishes the SCSI command to be
     completed successfully (0), or not (in which case cmd->result
     and sense buffer are assumed to be set).

.. _`ata_scsi_rbuf_fill.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_scsiop_inq_std`:

ata_scsiop_inq_std
==================

.. c:function:: unsigned int ata_scsiop_inq_std(struct ata_scsi_args *args, u8 *rbuf)

    Simulate INQUIRY command

    :param args:
        device IDENTIFY data / SCSI command of interest.
    :type args: struct ata_scsi_args \*

    :param rbuf:
        Response buffer, to which simulated SCSI cmd output is sent.
    :type rbuf: u8 \*

.. _`ata_scsiop_inq_std.description`:

Description
-----------

     Returns standard device identification data associated
     with non-VPD INQUIRY command output.

.. _`ata_scsiop_inq_std.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_scsiop_inq_00`:

ata_scsiop_inq_00
=================

.. c:function:: unsigned int ata_scsiop_inq_00(struct ata_scsi_args *args, u8 *rbuf)

    Simulate INQUIRY VPD page 0, list of pages

    :param args:
        device IDENTIFY data / SCSI command of interest.
    :type args: struct ata_scsi_args \*

    :param rbuf:
        Response buffer, to which simulated SCSI cmd output is sent.
    :type rbuf: u8 \*

.. _`ata_scsiop_inq_00.description`:

Description
-----------

     Returns list of inquiry VPD pages available.

.. _`ata_scsiop_inq_00.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_scsiop_inq_80`:

ata_scsiop_inq_80
=================

.. c:function:: unsigned int ata_scsiop_inq_80(struct ata_scsi_args *args, u8 *rbuf)

    Simulate INQUIRY VPD page 80, device serial number

    :param args:
        device IDENTIFY data / SCSI command of interest.
    :type args: struct ata_scsi_args \*

    :param rbuf:
        Response buffer, to which simulated SCSI cmd output is sent.
    :type rbuf: u8 \*

.. _`ata_scsiop_inq_80.description`:

Description
-----------

     Returns ATA device serial number.

.. _`ata_scsiop_inq_80.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_scsiop_inq_83`:

ata_scsiop_inq_83
=================

.. c:function:: unsigned int ata_scsiop_inq_83(struct ata_scsi_args *args, u8 *rbuf)

    Simulate INQUIRY VPD page 83, device identity

    :param args:
        device IDENTIFY data / SCSI command of interest.
    :type args: struct ata_scsi_args \*

    :param rbuf:
        Response buffer, to which simulated SCSI cmd output is sent.
    :type rbuf: u8 \*

.. _`ata_scsiop_inq_83.yields-two-logical-unit-device-identification-designators`:

Yields two logical unit device identification designators
---------------------------------------------------------

      - vendor specific ASCII containing the ATA serial number
      - SAT defined "t10 vendor id based" containing ASCII vendor
        name ("ATA     "), model and serial numbers.

.. _`ata_scsiop_inq_83.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_scsiop_inq_89`:

ata_scsiop_inq_89
=================

.. c:function:: unsigned int ata_scsiop_inq_89(struct ata_scsi_args *args, u8 *rbuf)

    Simulate INQUIRY VPD page 89, ATA info

    :param args:
        device IDENTIFY data / SCSI command of interest.
    :type args: struct ata_scsi_args \*

    :param rbuf:
        Response buffer, to which simulated SCSI cmd output is sent.
    :type rbuf: u8 \*

.. _`ata_scsiop_inq_89.description`:

Description
-----------

     Yields SAT-specified ATA VPD page.

.. _`ata_scsiop_inq_89.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`modecpy`:

modecpy
=======

.. c:function:: void modecpy(u8 *dest, const u8 *src, int n, bool changeable)

    Prepare response for MODE SENSE

    :param dest:
        output buffer
    :type dest: u8 \*

    :param src:
        data being copied
    :type src: const u8 \*

    :param n:
        length of mode page
    :type n: int

    :param changeable:
        whether changeable parameters are requested
    :type changeable: bool

.. _`modecpy.description`:

Description
-----------

     Generate a generic MODE SENSE page for either current or changeable
     parameters.

.. _`modecpy.locking`:

LOCKING
-------

     None.

.. _`ata_msense_caching`:

ata_msense_caching
==================

.. c:function:: unsigned int ata_msense_caching(u16 *id, u8 *buf, bool changeable)

    Simulate MODE SENSE caching info page

    :param id:
        device IDENTIFY data
    :type id: u16 \*

    :param buf:
        output buffer
    :type buf: u8 \*

    :param changeable:
        whether changeable parameters are requested
    :type changeable: bool

.. _`ata_msense_caching.description`:

Description
-----------

     Generate a caching info page, which conditionally indicates
     write caching to the SCSI layer, depending on device
     capabilities.

.. _`ata_msense_caching.locking`:

LOCKING
-------

     None.

.. _`ata_msense_control`:

ata_msense_control
==================

.. c:function:: unsigned int ata_msense_control(struct ata_device *dev, u8 *buf, bool changeable)

    Simulate MODE SENSE control mode page

    :param dev:
        ATA device of interest
    :type dev: struct ata_device \*

    :param buf:
        output buffer
    :type buf: u8 \*

    :param changeable:
        whether changeable parameters are requested
    :type changeable: bool

.. _`ata_msense_control.description`:

Description
-----------

     Generate a generic MODE SENSE control mode page.

.. _`ata_msense_control.locking`:

LOCKING
-------

     None.

.. _`ata_msense_rw_recovery`:

ata_msense_rw_recovery
======================

.. c:function:: unsigned int ata_msense_rw_recovery(u8 *buf, bool changeable)

    Simulate MODE SENSE r/w error recovery page

    :param buf:
        output buffer
    :type buf: u8 \*

    :param changeable:
        whether changeable parameters are requested
    :type changeable: bool

.. _`ata_msense_rw_recovery.description`:

Description
-----------

     Generate a generic MODE SENSE r/w error recovery page.

.. _`ata_msense_rw_recovery.locking`:

LOCKING
-------

     None.

.. _`ata_scsiop_mode_sense`:

ata_scsiop_mode_sense
=====================

.. c:function:: unsigned int ata_scsiop_mode_sense(struct ata_scsi_args *args, u8 *rbuf)

    Simulate MODE SENSE 6, 10 commands

    :param args:
        device IDENTIFY data / SCSI command of interest.
    :type args: struct ata_scsi_args \*

    :param rbuf:
        Response buffer, to which simulated SCSI cmd output is sent.
    :type rbuf: u8 \*

.. _`ata_scsiop_mode_sense.description`:

Description
-----------

     Simulate MODE SENSE commands. Assume this is invoked for direct
     access devices (e.g. disks) only. There should be no block
     descriptor for other device types.

.. _`ata_scsiop_mode_sense.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_scsiop_read_cap`:

ata_scsiop_read_cap
===================

.. c:function:: unsigned int ata_scsiop_read_cap(struct ata_scsi_args *args, u8 *rbuf)

    Simulate READ CAPACITY[ 16] commands

    :param args:
        device IDENTIFY data / SCSI command of interest.
    :type args: struct ata_scsi_args \*

    :param rbuf:
        Response buffer, to which simulated SCSI cmd output is sent.
    :type rbuf: u8 \*

.. _`ata_scsiop_read_cap.description`:

Description
-----------

     Simulate READ CAPACITY commands.

.. _`ata_scsiop_read_cap.locking`:

LOCKING
-------

     None.

.. _`ata_scsiop_report_luns`:

ata_scsiop_report_luns
======================

.. c:function:: unsigned int ata_scsiop_report_luns(struct ata_scsi_args *args, u8 *rbuf)

    Simulate REPORT LUNS command

    :param args:
        device IDENTIFY data / SCSI command of interest.
    :type args: struct ata_scsi_args \*

    :param rbuf:
        Response buffer, to which simulated SCSI cmd output is sent.
    :type rbuf: u8 \*

.. _`ata_scsiop_report_luns.description`:

Description
-----------

     Simulate REPORT LUNS command.

.. _`ata_scsiop_report_luns.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`atapi_xlat`:

atapi_xlat
==========

.. c:function:: unsigned int atapi_xlat(struct ata_queued_cmd *qc)

    Initialize PACKET taskfile

    :param qc:
        command structure to be initialized
    :type qc: struct ata_queued_cmd \*

.. _`atapi_xlat.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`atapi_xlat.return`:

Return
------

     Zero on success, non-zero on failure.

.. _`ata_scsi_find_dev`:

ata_scsi_find_dev
=================

.. c:function:: struct ata_device *ata_scsi_find_dev(struct ata_port *ap, const struct scsi_device *scsidev)

    lookup ata_device from scsi_cmnd

    :param ap:
        ATA port to which the device is attached
    :type ap: struct ata_port \*

    :param scsidev:
        SCSI device from which we derive the ATA device
    :type scsidev: const struct scsi_device \*

.. _`ata_scsi_find_dev.description`:

Description
-----------

     Given various information provided in struct scsi_cmnd,
     map that onto an ATA bus, and using that mapping
     determine which ata_device is associated with the
     SCSI command to be sent.

.. _`ata_scsi_find_dev.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_scsi_find_dev.return`:

Return
------

     Associated ATA device, or \ ``NULL``\  if not found.

.. _`ata_scsi_pass_thru`:

ata_scsi_pass_thru
==================

.. c:function:: unsigned int ata_scsi_pass_thru(struct ata_queued_cmd *qc)

    convert ATA pass-thru CDB to taskfile

    :param qc:
        command structure to be initialized
    :type qc: struct ata_queued_cmd \*

.. _`ata_scsi_pass_thru.description`:

Description
-----------

     Handles either 12, 16, or 32-byte versions of the CDB.

.. _`ata_scsi_pass_thru.return`:

Return
------

     Zero on success, non-zero on failure.

.. _`ata_format_dsm_trim_descr`:

ata_format_dsm_trim_descr
=========================

.. c:function:: size_t ata_format_dsm_trim_descr(struct scsi_cmnd *cmd, u32 trmax, u64 sector, u32 count)

    SATL Write Same to DSM Trim

    :param cmd:
        SCSI command being translated
    :type cmd: struct scsi_cmnd \*

    :param trmax:
        Maximum number of entries that will fit in sector_size bytes.
    :type trmax: u32

    :param sector:
        Starting sector
    :type sector: u64

    :param count:
        Total Range of request in logical sectors
    :type count: u32

.. _`ata_format_dsm_trim_descr.description`:

Description
-----------

Rewrite the WRITE SAME descriptor to be a DSM TRIM little-endian formatted
descriptor.

.. _`ata_format_dsm_trim_descr.upto-64-entries-of-the-format`:

Upto 64 entries of the format
-----------------------------

  63:48 Range Length
  47:0  LBA

 Range Length of 0 is ignored.
 LBA's should be sorted order and not overlap.

.. _`ata_format_dsm_trim_descr.note`:

NOTE
----

this is the same format as ADD LBA(S) TO NV CACHE PINNED SET

.. _`ata_format_dsm_trim_descr.return`:

Return
------

Number of bytes copied into sglist.

.. _`ata_scsi_write_same_xlat`:

ata_scsi_write_same_xlat
========================

.. c:function:: unsigned int ata_scsi_write_same_xlat(struct ata_queued_cmd *qc)

    SATL Write Same to ATA SCT Write Same

    :param qc:
        Command to be translated
    :type qc: struct ata_queued_cmd \*

.. _`ata_scsi_write_same_xlat.description`:

Description
-----------

Translate a SCSI WRITE SAME command to be either a DSM TRIM command or
an SCT Write Same command.

.. _`ata_scsi_write_same_xlat.based-on-write-same-has-the-unmap-flag`:

Based on WRITE SAME has the UNMAP flag
--------------------------------------


  - When set translate to DSM TRIM
  - When clear translate to SCT Write Same

.. _`ata_scsiop_maint_in`:

ata_scsiop_maint_in
===================

.. c:function:: unsigned int ata_scsiop_maint_in(struct ata_scsi_args *args, u8 *rbuf)

    Simulate a subset of MAINTENANCE_IN

    :param args:
        device MAINTENANCE_IN data / SCSI command of interest.
    :type args: struct ata_scsi_args \*

    :param rbuf:
        Response buffer, to which simulated SCSI cmd output is sent.
    :type rbuf: u8 \*

.. _`ata_scsiop_maint_in.description`:

Description
-----------

     Yields a subset to satisfy \ :c:func:`scsi_report_opcode`\ 

.. _`ata_scsiop_maint_in.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_scsi_report_zones_complete`:

ata_scsi_report_zones_complete
==============================

.. c:function:: void ata_scsi_report_zones_complete(struct ata_queued_cmd *qc)

    convert ATA output

    :param qc:
        command structure returning the data
    :type qc: struct ata_queued_cmd \*

.. _`ata_scsi_report_zones_complete.description`:

Description
-----------

     Convert T-13 little-endian field representation into
     T-10 big-endian field representation.
     What a mess.

.. _`ata_mselect_caching`:

ata_mselect_caching
===================

.. c:function:: int ata_mselect_caching(struct ata_queued_cmd *qc, const u8 *buf, int len, u16 *fp)

    Simulate MODE SELECT for caching info page

    :param qc:
        Storage for translated ATA taskfile
    :type qc: struct ata_queued_cmd \*

    :param buf:
        input buffer
    :type buf: const u8 \*

    :param len:
        number of valid bytes in the input buffer
    :type len: int

    :param fp:
        out parameter for the failed field on error
    :type fp: u16 \*

.. _`ata_mselect_caching.description`:

Description
-----------

     Prepare a taskfile to modify caching information for the device.

.. _`ata_mselect_caching.locking`:

LOCKING
-------

     None.

.. _`ata_mselect_control`:

ata_mselect_control
===================

.. c:function:: int ata_mselect_control(struct ata_queued_cmd *qc, const u8 *buf, int len, u16 *fp)

    Simulate MODE SELECT for control page

    :param qc:
        Storage for translated ATA taskfile
    :type qc: struct ata_queued_cmd \*

    :param buf:
        input buffer
    :type buf: const u8 \*

    :param len:
        number of valid bytes in the input buffer
    :type len: int

    :param fp:
        out parameter for the failed field on error
    :type fp: u16 \*

.. _`ata_mselect_control.description`:

Description
-----------

     Prepare a taskfile to modify caching information for the device.

.. _`ata_mselect_control.locking`:

LOCKING
-------

     None.

.. _`ata_scsi_mode_select_xlat`:

ata_scsi_mode_select_xlat
=========================

.. c:function:: unsigned int ata_scsi_mode_select_xlat(struct ata_queued_cmd *qc)

    Simulate MODE SELECT 6, 10 commands

    :param qc:
        Storage for translated ATA taskfile
    :type qc: struct ata_queued_cmd \*

.. _`ata_scsi_mode_select_xlat.description`:

Description
-----------

     Converts a MODE SELECT command to an ATA SET FEATURES taskfile.
     Assume this is invoked for direct access devices (e.g. disks) only.
     There should be no block descriptor for other device types.

.. _`ata_scsi_mode_select_xlat.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_scsi_var_len_cdb_xlat`:

ata_scsi_var_len_cdb_xlat
=========================

.. c:function:: unsigned int ata_scsi_var_len_cdb_xlat(struct ata_queued_cmd *qc)

    SATL variable length CDB to Handler

    :param qc:
        Command to be translated
    :type qc: struct ata_queued_cmd \*

.. _`ata_scsi_var_len_cdb_xlat.description`:

Description
-----------

     Translate a SCSI variable length CDB to specified commands.
     It checks a service action value in CDB to call corresponding handler.

.. _`ata_scsi_var_len_cdb_xlat.return`:

Return
------

     Zero on success, non-zero on failure

.. _`ata_get_xlat_func`:

ata_get_xlat_func
=================

.. c:function:: ata_xlat_func_t ata_get_xlat_func(struct ata_device *dev, u8 cmd)

    check if SCSI to ATA translation is possible

    :param dev:
        ATA device
    :type dev: struct ata_device \*

    :param cmd:
        SCSI command opcode to consider
    :type cmd: u8

.. _`ata_get_xlat_func.description`:

Description
-----------

     Look up the SCSI command given, and determine whether the
     SCSI command is to be translated or simulated.

.. _`ata_get_xlat_func.return`:

Return
------

     Pointer to translation function if possible, \ ``NULL``\  if not.

.. _`ata_scsi_dump_cdb`:

ata_scsi_dump_cdb
=================

.. c:function:: void ata_scsi_dump_cdb(struct ata_port *ap, struct scsi_cmnd *cmd)

    dump SCSI command contents to dmesg

    :param ap:
        ATA port to which the command was being sent
    :type ap: struct ata_port \*

    :param cmd:
        SCSI command to dump
    :type cmd: struct scsi_cmnd \*

.. _`ata_scsi_dump_cdb.description`:

Description
-----------

     Prints the contents of a SCSI command via \ :c:func:`printk`\ .

.. _`ata_scsi_queuecmd`:

ata_scsi_queuecmd
=================

.. c:function:: int ata_scsi_queuecmd(struct Scsi_Host *shost, struct scsi_cmnd *cmd)

    Issue SCSI cdb to libata-managed device

    :param shost:
        SCSI host of command to be sent
    :type shost: struct Scsi_Host \*

    :param cmd:
        SCSI command to be sent
    :type cmd: struct scsi_cmnd \*

.. _`ata_scsi_queuecmd.description`:

Description
-----------

     In some cases, this function translates SCSI commands into
     ATA taskfiles, and queues the taskfiles to be sent to
     hardware.  In other cases, this function simulates a
     SCSI device by evaluating and responding to certain
     SCSI commands.  This creates the overall effect of
     ATA and ATAPI devices appearing as SCSI devices.

.. _`ata_scsi_queuecmd.locking`:

LOCKING
-------

     ATA host lock

.. _`ata_scsi_queuecmd.return`:

Return
------

     Return value from \ :c:func:`__ata_scsi_queuecmd`\  if \ ``cmd``\  can be queued,
     0 otherwise.

.. _`ata_scsi_simulate`:

ata_scsi_simulate
=================

.. c:function:: void ata_scsi_simulate(struct ata_device *dev, struct scsi_cmnd *cmd)

    simulate SCSI command on ATA device

    :param dev:
        the target device
    :type dev: struct ata_device \*

    :param cmd:
        SCSI command being sent to device.
    :type cmd: struct scsi_cmnd \*

.. _`ata_scsi_simulate.description`:

Description
-----------

     Interprets and directly executes a select list of SCSI commands
     that can be handled internally.

.. _`ata_scsi_simulate.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_scsi_offline_dev`:

ata_scsi_offline_dev
====================

.. c:function:: int ata_scsi_offline_dev(struct ata_device *dev)

    offline attached SCSI device

    :param dev:
        ATA device to offline attached SCSI device for
    :type dev: struct ata_device \*

.. _`ata_scsi_offline_dev.description`:

Description
-----------

     This function is called from \ :c:func:`ata_eh_hotplug`\  and responsible
     for taking the SCSI device attached to \ ``dev``\  offline.  This
     function is called with host lock which protects dev->sdev
     against clearing.

.. _`ata_scsi_offline_dev.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_scsi_offline_dev.return`:

Return
------

     1 if attached SCSI device exists, 0 otherwise.

.. _`ata_scsi_remove_dev`:

ata_scsi_remove_dev
===================

.. c:function:: void ata_scsi_remove_dev(struct ata_device *dev)

    remove attached SCSI device

    :param dev:
        ATA device to remove attached SCSI device for
    :type dev: struct ata_device \*

.. _`ata_scsi_remove_dev.description`:

Description
-----------

     This function is called from \ :c:func:`ata_eh_scsi_hotplug`\  and
     responsible for removing the SCSI device attached to \ ``dev``\ .

.. _`ata_scsi_remove_dev.locking`:

LOCKING
-------

     Kernel thread context (may sleep).

.. _`ata_scsi_media_change_notify`:

ata_scsi_media_change_notify
============================

.. c:function:: void ata_scsi_media_change_notify(struct ata_device *dev)

    send media change event

    :param dev:
        Pointer to the disk device with media change event
    :type dev: struct ata_device \*

.. _`ata_scsi_media_change_notify.description`:

Description
-----------

     Tell the block layer to send a media change notification
     event.

.. _`ata_scsi_media_change_notify.locking`:

LOCKING
-------

     spin_lock_irqsave(host lock)

.. _`ata_scsi_hotplug`:

ata_scsi_hotplug
================

.. c:function:: void ata_scsi_hotplug(struct work_struct *work)

    SCSI part of hotplug

    :param work:
        Pointer to ATA port to perform SCSI hotplug on
    :type work: struct work_struct \*

.. _`ata_scsi_hotplug.description`:

Description
-----------

     Perform SCSI part of hotplug.  It's executed from a separate
     workqueue after EH completes.  This is necessary because SCSI
     hot plugging requires working EH and hot unplugging is
     synchronized with hot plugging with a mutex.

.. _`ata_scsi_hotplug.locking`:

LOCKING
-------

     Kernel thread context (may sleep).

.. _`ata_scsi_user_scan`:

ata_scsi_user_scan
==================

.. c:function:: int ata_scsi_user_scan(struct Scsi_Host *shost, unsigned int channel, unsigned int id, u64 lun)

    indication for user-initiated bus scan

    :param shost:
        SCSI host to scan
    :type shost: struct Scsi_Host \*

    :param channel:
        Channel to scan
    :type channel: unsigned int

    :param id:
        ID to scan
    :type id: unsigned int

    :param lun:
        LUN to scan
    :type lun: u64

.. _`ata_scsi_user_scan.description`:

Description
-----------

     This function is called when user explicitly requests bus
     scan.  Set probe pending flag and invoke EH.

.. _`ata_scsi_user_scan.locking`:

LOCKING
-------

     SCSI layer (we don't care)

.. _`ata_scsi_user_scan.return`:

Return
------

     Zero.

.. _`ata_scsi_dev_rescan`:

ata_scsi_dev_rescan
===================

.. c:function:: void ata_scsi_dev_rescan(struct work_struct *work)

    initiate \ :c:func:`scsi_rescan_device`\ 

    :param work:
        Pointer to ATA port to perform \ :c:func:`scsi_rescan_device`\ 
    :type work: struct work_struct \*

.. _`ata_scsi_dev_rescan.description`:

Description
-----------

     After ATA pass thru (SAT) commands are executed successfully,
     libata need to propagate the changes to SCSI layer.

.. _`ata_scsi_dev_rescan.locking`:

LOCKING
-------

     Kernel thread context (may sleep).

.. _`ata_sas_port_alloc`:

ata_sas_port_alloc
==================

.. c:function:: struct ata_port *ata_sas_port_alloc(struct ata_host *host, struct ata_port_info *port_info, struct Scsi_Host *shost)

    Allocate port for a SAS attached SATA device

    :param host:
        ATA host container for all SAS ports
    :type host: struct ata_host \*

    :param port_info:
        Information from low-level host driver
    :type port_info: struct ata_port_info \*

    :param shost:
        SCSI host that the scsi device is attached to
    :type shost: struct Scsi_Host \*

.. _`ata_sas_port_alloc.locking`:

LOCKING
-------

     PCI/etc. bus probe sem.

.. _`ata_sas_port_alloc.return`:

Return
------

     ata_port pointer on success / NULL on failure.

.. _`ata_sas_port_start`:

ata_sas_port_start
==================

.. c:function:: int ata_sas_port_start(struct ata_port *ap)

    Set port up for dma.

    :param ap:
        Port to initialize
    :type ap: struct ata_port \*

.. _`ata_sas_port_start.description`:

Description
-----------

     Called just after data structures for each port are
     initialized.

     May be used as the \ :c:func:`port_start`\  entry in ata_port_operations.

.. _`ata_sas_port_start.locking`:

LOCKING
-------

     Inherited from caller.

.. _`ata_sas_port_stop`:

ata_sas_port_stop
=================

.. c:function:: void ata_sas_port_stop(struct ata_port *ap)

    Undo \ :c:func:`ata_sas_port_start`\ 

    :param ap:
        Port to shut down
    :type ap: struct ata_port \*

.. _`ata_sas_port_stop.description`:

Description
-----------

     May be used as the \ :c:func:`port_stop`\  entry in ata_port_operations.

.. _`ata_sas_port_stop.locking`:

LOCKING
-------

     Inherited from caller.

.. _`ata_sas_async_probe`:

ata_sas_async_probe
===================

.. c:function:: void ata_sas_async_probe(struct ata_port *ap)

    simply schedule probing and return

    :param ap:
        Port to probe
    :type ap: struct ata_port \*

.. _`ata_sas_async_probe.description`:

Description
-----------

For batch scheduling of probe for sas attached ata devices, assumes
the port has already been through \ :c:func:`ata_sas_port_init`\ 

.. _`ata_sas_port_init`:

ata_sas_port_init
=================

.. c:function:: int ata_sas_port_init(struct ata_port *ap)

    Initialize a SATA device

    :param ap:
        SATA port to initialize
    :type ap: struct ata_port \*

.. _`ata_sas_port_init.locking`:

LOCKING
-------

     PCI/etc. bus probe sem.

.. _`ata_sas_port_init.return`:

Return
------

     Zero on success, non-zero on error.

.. _`ata_sas_port_destroy`:

ata_sas_port_destroy
====================

.. c:function:: void ata_sas_port_destroy(struct ata_port *ap)

    Destroy a SATA port allocated by ata_sas_port_alloc

    :param ap:
        SATA port to destroy
    :type ap: struct ata_port \*

.. _`ata_sas_slave_configure`:

ata_sas_slave_configure
=======================

.. c:function:: int ata_sas_slave_configure(struct scsi_device *sdev, struct ata_port *ap)

    Default slave_config routine for libata devices

    :param sdev:
        SCSI device to configure
    :type sdev: struct scsi_device \*

    :param ap:
        ATA port to which SCSI device is attached
    :type ap: struct ata_port \*

.. _`ata_sas_slave_configure.return`:

Return
------

     Zero.

.. _`ata_sas_queuecmd`:

ata_sas_queuecmd
================

.. c:function:: int ata_sas_queuecmd(struct scsi_cmnd *cmd, struct ata_port *ap)

    Issue SCSI cdb to libata-managed device

    :param cmd:
        SCSI command to be sent
    :type cmd: struct scsi_cmnd \*

    :param ap:
        ATA port to which the command is being sent
    :type ap: struct ata_port \*

.. _`ata_sas_queuecmd.return`:

Return
------

     Return value from \ :c:func:`__ata_scsi_queuecmd`\  if \ ``cmd``\  can be queued,
     0 otherwise.

.. This file was automatic generated / don't edit.

