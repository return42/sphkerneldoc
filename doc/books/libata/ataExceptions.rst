
.. _ataExceptions:

=========================
ATA errors and exceptions
=========================

This chapter tries to identify what error/exception conditions exist for ATA/ATAPI devices and describe how they should be handled in implementation-neutral way.

The term 'error' is used to describe conditions where either an explicit error condition is reported from device or a command has timed out.

The term 'exception' is either used to describe exceptional conditions which are not errors (say, power or hotplug events), or to describe both errors and non-error exceptional
conditions. Where explicit distinction between error and exception is necessary, the term 'non-error exception' is used.


.. _excat:

Exception categories
====================

Exceptions are described primarily with respect to legacy taskfile + bus master IDE interface. If a controller provides other better mechanism for error reporting, mapping those
into categories described below shouldn't be difficult.

In the following sections, two recovery actions - reset and reconfiguring transport - are mentioned. These are described further in :ref:`exrec`.


.. _excatHSMviolation:

HSM violation
-------------

This error is indicated when STATUS value doesn't match HSM requirement during issuing or execution any ATA/ATAPI command.

-  ATA_STATUS doesn't contain !BSY && DRDY && !DRQ while trying to issue a command.

-  !BSY && !DRQ during PIO data transfer.

-  DRQ on command completion.

-  !BSY && ERR after CDB transfer starts but before the last byte of CDB is transferred. ATA/ATAPI standard states that "The device shall not terminate the PACKET command with an
   error before the last byte of the command packet has been written" in the error outputs description of PACKET command and the state diagram doesn't include such transitions.

In these cases, HSM is violated and not much information regarding the error can be acquired from STATUS or ERROR register. IOW, this error can be anything - driver bug, faulty
device, controller and/or cable.

As HSM is violated, reset is necessary to restore known state. Reconfiguring transport for lower speed might be helpful too as transmission errors sometimes cause this kind of
errors.


.. _excatDevErr:

ATA/ATAPI device error (non-NCQ / non-CHECK CONDITION)
------------------------------------------------------

These are errors detected and reported by ATA/ATAPI devices indicating device problems. For this type of errors, STATUS and ERROR register values are valid and describe error
condition. Note that some of ATA bus errors are detected by ATA/ATAPI devices and reported using the same mechanism as device errors. Those cases are described later in this
section.

For ATA commands, this type of errors are indicated by !BSY && ERR during command execution and on completion.

For ATAPI commands,

-  !BSY && ERR && ABRT right after issuing PACKET indicates that PACKET command is not supported and falls in this category.

-  !BSY && ERR(==CHK) && !ABRT after the last byte of CDB is transferred indicates CHECK CONDITION and doesn't fall in this category.

-  !BSY && ERR(==CHK) && ABRT after the last byte of CDB is transferred ⋆probably⋆ indicates CHECK CONDITION and doesn't fall in this category.

Of errors detected as above, the followings are not ATA/ATAPI device errors but ATA bus errors and should be handled according to :ref:`excatATAbusErr`.

CRC error during data transfer
    This is indicated by ICRC bit in the ERROR register and means that corruption occurred during data transfer. Up to ATA/ATAPI-7, the standard specifies that this bit is only
    applicable to UDMA transfers but ATA/ATAPI-8 draft revision 1f says that the bit may be applicable to multiword DMA and PIO.

ABRT error during data transfer or on completion
    Up to ATA/ATAPI-7, the standard specifies that ABRT could be set on ICRC errors and on cases where a device is not able to complete a command. Combined with the fact that MWDMA
    and PIO transfer errors aren't allowed to use ICRC bit up to ATA/ATAPI-7, it seems to imply that ABRT bit alone could indicate transfer errors.

    However, ATA/ATAPI-8 draft revision 1f removes the part that ICRC errors can turn on ABRT. So, this is kind of gray area. Some heuristics are needed here.

ATA/ATAPI device errors can be further categorized as follows.

Media errors
    This is indicated by UNC bit in the ERROR register. ATA devices reports UNC error only after certain number of retries cannot recover the data, so there's nothing much else to
    do other than notifying upper layer.

    READ and WRITE commands report CHS or LBA of the first failed sector but ATA/ATAPI standard specifies that the amount of transferred data on error completion is indeterminate,
    so we cannot assume that sectors preceding the failed sector have been transferred and thus cannot complete those sectors successfully as SCSI does.

Media changed / media change requested error
    <<TODO: fill here>>

Address error
    This is indicated by IDNF bit in the ERROR register. Report to upper layer.

Other errors
    This can be invalid command or parameter indicated by ABRT ERROR bit or some other error condition. Note that ABRT bit can indicate a lot of things including ICRC and Address
    errors. Heuristics needed.

Depending on commands, not all STATUS/ERROR bits are applicable. These non-applicable bits are marked with "na" in the output descriptions but up to ATA/ATAPI-7 no definition of
"na" can be found. However, ATA/ATAPI-8 draft revision 1f describes "N/A" as follows.

    3.2.3.3a N/A
        A keyword the indicates a field has no defined value in this standard and should not be checked by the host or device. N/A fields should be cleared to zero.

So, it seems reasonable to assume that "na" bits are cleared to zero by devices and thus need no explicit masking.


.. _excatATAPIcc:

ATAPI device CHECK CONDITION
----------------------------

ATAPI device CHECK CONDITION error is indicated by set CHK bit (ERR bit) in the STATUS register after the last byte of CDB is transferred for a PACKET command. For this kind of
errors, sense data should be acquired to gather information regarding the errors. REQUEST SENSE packet command should be used to acquire sense data.

Once sense data is acquired, this type of errors can be handled similarly to other SCSI errors. Note that sense data may indicate ATA bus error (e.g. Sense Key 04h HARDWARE ERROR
&& ASC/ASCQ 47h/00h SCSI PARITY ERROR). In such cases, the error should be considered as an ATA bus error and handled according to :ref:`excatATAbusErr`.


.. _excatNCQerr:

ATA device error (NCQ)
----------------------

NCQ command error is indicated by cleared BSY and set ERR bit during NCQ command phase (one or more NCQ commands outstanding). Although STATUS and ERROR registers will contain
valid values describing the error, READ LOG EXT is required to clear the error condition, determine which command has failed and acquire more information.

READ LOG EXT Log Page 10h reports which tag has failed and taskfile register values describing the error. With this information the failed command can be handled as a normal ATA
command error as in :ref:`excatDevErr` and all other in-flight commands must be retried. Note that this retry should not be counted - it's likely that commands retried this way
would have completed normally if it were not for the failed command.

Note that ATA bus errors can be reported as ATA device NCQ errors. This should be handled as described in :ref:`excatATAbusErr`.

If READ LOG EXT Log Page 10h fails or reports NQ, we're thoroughly screwed. This condition should be treated according to :ref:`excatHSMviolation`.


.. _excatATAbusErr:

ATA bus error
-------------

ATA bus error means that data corruption occurred during transmission over ATA bus (SATA or PATA). This type of errors can be indicated by

-  ICRC or ABRT error as described in :ref:`excatDevErr`.

-  Controller-specific error completion with error information indicating transmission error.

-  On some controllers, command timeout. In this case, there may be a mechanism to determine that the timeout is due to transmission error.

-  Unknown/random errors, timeouts and all sorts of weirdities.

As described above, transmission errors can cause wide variety of symptoms ranging from device ICRC error to random device lockup, and, for many cases, there is no way to tell if
an error condition is due to transmission error or not; therefore, it's necessary to employ some kind of heuristic when dealing with errors and timeouts. For example, encountering
repetitive ABRT errors for known supported command is likely to indicate ATA bus error.

Once it's determined that ATA bus errors have possibly occurred, lowering ATA bus transmission speed is one of actions which may alleviate the problem. See :ref:`exrecReconf` for
more information.


.. _excatPCIbusErr:

PCI bus error
-------------

Data corruption or other failures during transmission over PCI (or other system bus). For standard BMDMA, this is indicated by Error bit in the BMDMA Status register. This type of
errors must be logged as it indicates something is very wrong with the system. Resetting host controller is recommended.


.. _excatLateCompletion:

Late completion
---------------

This occurs when timeout occurs and the timeout handler finds out that the timed out command has completed successfully or with error. This is usually caused by lost interrupts.
This type of errors must be logged. Resetting host controller is recommended.


.. _excatUnknown:

Unknown error (timeout)
-----------------------

This is when timeout occurs and the command is still processing or the host and device are in unknown state. When this occurs, HSM could be in any valid or invalid state. To bring
the device to known state and make it forget about the timed out command, resetting is necessary. The timed out command may be retried.

Timeouts can also be caused by transmission errors. Refer to :ref:`excatATAbusErr` for more details.


.. _excatHoplugPM:

Hotplug and power management exceptions
---------------------------------------

<<TODO: fill here>>


.. _exrec:

EH recovery actions
===================

This section discusses several important recovery actions.


.. _exrecClr:

Clearing error condition
------------------------

Many controllers require its error registers to be cleared by error handler. Different controllers may have different requirements.

For SATA, it's strongly recommended to clear at least SError register during error handling.


.. _exrecRst:

Reset
-----

During EH, resetting is necessary in the following cases.

-  HSM is in unknown or invalid state

-  HBA is in unknown or invalid state

-  EH needs to make HBA/device forget about in-flight commands

-  HBA/device behaves weirdly

Resetting during EH might be a good idea regardless of error condition to improve EH robustness. Whether to reset both or either one of HBA and device depends on situation but the
following scheme is recommended.

-  When it's known that HBA is in ready state but ATA/ATAPI device is in unknown state, reset only device.

-  If HBA is in unknown state, reset both HBA and device.

HBA resetting is implementation specific. For a controller complying to taskfile/BMDMA PCI IDE, stopping active DMA transaction may be sufficient iff BMDMA state is the only HBA
context. But even mostly taskfile/BMDMA PCI IDE complying controllers may have implementation specific requirements and mechanism to reset themselves. This must be addressed by
specific drivers.

OTOH, ATA/ATAPI standard describes in detail ways to reset ATA/ATAPI devices.

PATA hardware reset
    This is hardware initiated device reset signalled with asserted PATA RESET- signal. There is no standard way to initiate hardware reset from software although some hardware
    provides registers that allow driver to directly tweak the RESET- signal.

Software reset
    This is achieved by turning CONTROL SRST bit on for at least 5us. Both PATA and SATA support it but, in case of SATA, this may require controller-specific support as the second
    Register FIS to clear SRST should be transmitted while BSY bit is still set. Note that on PATA, this resets both master and slave devices on a channel.

EXECUTE DEVICE DIAGNOSTIC command
    Although ATA/ATAPI standard doesn't describe exactly, EDD implies some level of resetting, possibly similar level with software reset. Host-side EDD protocol can be handled
    with normal command processing and most SATA controllers should be able to handle EDD's just like other commands. As in software reset, EDD affects both devices on a PATA bus.

    Although EDD does reset devices, this doesn't suit error handling as EDD cannot be issued while BSY is set and it's unclear how it will act when device is in unknown/weird
    state.

ATAPI DEVICE RESET command
    This is very similar to software reset except that reset can be restricted to the selected device without affecting the other device sharing the cable.

SATA phy reset
    This is the preferred way of resetting a SATA device. In effect, it's identical to PATA hardware reset. Note that this can be done with the standard SCR Control register. As
    such, it's usually easier to implement than software reset.

One more thing to consider when resetting devices is that resetting clears certain configuration parameters and they need to be set to their previous or newly adjusted values after
reset.

Parameters affected are.

-  CHS set up with INITIALIZE DEVICE PARAMETERS (seldom used)

-  Parameters set with SET FEATURES including transfer mode setting

-  Block count set with SET MULTIPLE MODE

-  Other parameters (SET MAX, MEDIA LOCK...)

ATA/ATAPI standard specifies that some parameters must be maintained across hardware or software reset, but doesn't strictly specify all of them. Always reconfiguring needed
parameters after reset is required for robustness. Note that this also applies when resuming from deep sleep (power-off).

Also, ATA/ATAPI standard requires that IDENTIFY DEVICE / IDENTIFY PACKET DEVICE is issued after any configuration parameter is updated or a hardware reset and the result used for
further operation. OS driver is required to implement revalidation mechanism to support this.


.. _exrecReconf:

Reconfigure transport
---------------------

For both PATA and SATA, a lot of corners are cut for cheap connectors, cables or controllers and it's quite common to see high transmission error rate. This can be mitigated by
lowering transmission speed.

The following is a possible scheme Jeff Garzik suggested.

    If more than $N (3?) transmission errors happen in 15 minutes,

    -  if SATA, decrease SATA PHY speed. if speed cannot be decreased,

    -  decrease UDMA xfer speed. if at UDMA0, switch to PIO4,

    -  decrease PIO xfer speed. if at PIO3, complain, but continue
