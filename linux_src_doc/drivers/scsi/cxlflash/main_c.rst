.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/cxlflash/main.c

.. _`process_cmd_err`:

process_cmd_err
===============

.. c:function:: void process_cmd_err(struct afu_cmd *cmd, struct scsi_cmnd *scp)

    command error handler

    :param struct afu_cmd \*cmd:
        AFU command that experienced the error.

    :param struct scsi_cmnd \*scp:
        SCSI command associated with the AFU command in error.

.. _`process_cmd_err.description`:

Description
-----------

Translates error bits from AFU command to SCSI command results.

.. _`cmd_complete`:

cmd_complete
============

.. c:function:: void cmd_complete(struct afu_cmd *cmd)

    command completion handler

    :param struct afu_cmd \*cmd:
        AFU command that has completed.

.. _`cmd_complete.description`:

Description
-----------

For SCSI commands this routine prepares and submits commands that have
either completed or timed out to the SCSI stack. For internal commands
(TMF or AFU), this routine simply notifies the originator that the
command has completed.

.. _`flush_pending_cmds`:

flush_pending_cmds
==================

.. c:function:: void flush_pending_cmds(struct hwq *hwq)

    flush all pending commands on this hardware queue

    :param struct hwq \*hwq:
        Hardware queue to flush.

.. _`flush_pending_cmds.description`:

Description
-----------

The hardware send queue lock associated with this hardware queue must be
held when calling this routine.

.. _`context_reset`:

context_reset
=============

.. c:function:: int context_reset(struct hwq *hwq, __be64 __iomem *reset_reg)

    reset context via specified register

    :param struct hwq \*hwq:
        Hardware queue owning the context to be reset.

    :param __be64 __iomem \*reset_reg:
        MMIO register to perform reset.

.. _`context_reset.description`:

Description
-----------

When the reset is successful, the SISLite specification guarantees that
the AFU has aborted all currently pending I/O. Accordingly, these commands
must be flushed.

.. _`context_reset.return`:

Return
------

0 on success, -errno on failure

.. _`context_reset_ioarrin`:

context_reset_ioarrin
=====================

.. c:function:: int context_reset_ioarrin(struct hwq *hwq)

    reset context via IOARRIN register

    :param struct hwq \*hwq:
        Hardware queue owning the context to be reset.

.. _`context_reset_ioarrin.return`:

Return
------

0 on success, -errno on failure

.. _`context_reset_sq`:

context_reset_sq
================

.. c:function:: int context_reset_sq(struct hwq *hwq)

    reset context via SQ_CONTEXT_RESET register

    :param struct hwq \*hwq:
        Hardware queue owning the context to be reset.

.. _`context_reset_sq.return`:

Return
------

0 on success, -errno on failure

.. _`send_cmd_ioarrin`:

send_cmd_ioarrin
================

.. c:function:: int send_cmd_ioarrin(struct afu *afu, struct afu_cmd *cmd)

    sends an AFU command via IOARRIN register

    :param struct afu \*afu:
        AFU associated with the host.

    :param struct afu_cmd \*cmd:
        AFU command to send.

.. _`send_cmd_ioarrin.return`:

Return
------

0 on success, SCSI_MLQUEUE_HOST_BUSY on failure

.. _`send_cmd_sq`:

send_cmd_sq
===========

.. c:function:: int send_cmd_sq(struct afu *afu, struct afu_cmd *cmd)

    sends an AFU command via SQ ring

    :param struct afu \*afu:
        AFU associated with the host.

    :param struct afu_cmd \*cmd:
        AFU command to send.

.. _`send_cmd_sq.return`:

Return
------

0 on success, SCSI_MLQUEUE_HOST_BUSY on failure

.. _`wait_resp`:

wait_resp
=========

.. c:function:: int wait_resp(struct afu *afu, struct afu_cmd *cmd)

    polls for a response or timeout to a sent AFU command

    :param struct afu \*afu:
        AFU associated with the host.

    :param struct afu_cmd \*cmd:
        AFU command that was sent.

.. _`wait_resp.return`:

Return
------

0 on success, -errno on failure

.. _`cmd_to_target_hwq`:

cmd_to_target_hwq
=================

.. c:function:: u32 cmd_to_target_hwq(struct Scsi_Host *host, struct scsi_cmnd *scp, struct afu *afu)

    selects a target hardware queue for a SCSI command

    :param struct Scsi_Host \*host:
        SCSI host associated with device.

    :param struct scsi_cmnd \*scp:
        SCSI command to send.

    :param struct afu \*afu:
        SCSI command to send.

.. _`cmd_to_target_hwq.description`:

Description
-----------

Hashes a command based upon the hardware queue mode.

.. _`cmd_to_target_hwq.return`:

Return
------

Trusted index of target hardware queue

.. _`send_tmf`:

send_tmf
========

.. c:function:: int send_tmf(struct cxlflash_cfg *cfg, struct scsi_device *sdev, u64 tmfcmd)

    sends a Task Management Function (TMF)

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

    :param struct scsi_device \*sdev:
        SCSI device destined for TMF.

    :param u64 tmfcmd:
        TMF command to send.

.. _`send_tmf.return`:

Return
------

0 on success, SCSI_MLQUEUE_HOST_BUSY or -errno on failure

.. _`cxlflash_driver_info`:

cxlflash_driver_info
====================

.. c:function:: const char *cxlflash_driver_info(struct Scsi_Host *host)

    information handler for this host driver

    :param struct Scsi_Host \*host:
        SCSI host associated with device.

.. _`cxlflash_driver_info.return`:

Return
------

A string describing the device.

.. _`cxlflash_queuecommand`:

cxlflash_queuecommand
=====================

.. c:function:: int cxlflash_queuecommand(struct Scsi_Host *host, struct scsi_cmnd *scp)

    sends a mid-layer request

    :param struct Scsi_Host \*host:
        SCSI host associated with device.

    :param struct scsi_cmnd \*scp:
        SCSI command to send.

.. _`cxlflash_queuecommand.return`:

Return
------

0 on success, SCSI_MLQUEUE_HOST_BUSY on failure

.. _`cxlflash_wait_for_pci_err_recovery`:

cxlflash_wait_for_pci_err_recovery
==================================

.. c:function:: void cxlflash_wait_for_pci_err_recovery(struct cxlflash_cfg *cfg)

    wait for error recovery during probe

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

.. _`free_mem`:

free_mem
========

.. c:function:: void free_mem(struct cxlflash_cfg *cfg)

    free memory associated with the AFU

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

.. _`cxlflash_reset_sync`:

cxlflash_reset_sync
===================

.. c:function:: void cxlflash_reset_sync(struct cxlflash_cfg *cfg)

    synchronizing point for asynchronous resets

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

.. _`stop_afu`:

stop_afu
========

.. c:function:: void stop_afu(struct cxlflash_cfg *cfg)

    stops the AFU command timers and unmaps the MMIO space

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

.. _`stop_afu.description`:

Description
-----------

Safe to call with AFU in a partially allocated/initialized state.

Cancels scheduled worker threads, waits for any active internal AFU
commands to timeout, disables IRQ polling and then unmaps the MMIO space.

.. _`term_intr`:

term_intr
=========

.. c:function:: void term_intr(struct cxlflash_cfg *cfg, enum undo_level level, u32 index)

    disables all AFU interrupts

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

    :param enum undo_level level:
        Depth of allocation, where to begin waterfall tear down.

    :param u32 index:
        Index of the hardware queue.

.. _`term_intr.description`:

Description
-----------

Safe to call with AFU/MC in partially allocated/initialized state.

.. _`term_mc`:

term_mc
=======

.. c:function:: void term_mc(struct cxlflash_cfg *cfg, u32 index)

    terminates the master context

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

    :param u32 index:
        Index of the hardware queue.

.. _`term_mc.description`:

Description
-----------

Safe to call with AFU/MC in partially allocated/initialized state.

.. _`term_afu`:

term_afu
========

.. c:function:: void term_afu(struct cxlflash_cfg *cfg)

    terminates the AFU

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

.. _`term_afu.description`:

Description
-----------

Safe to call with AFU/MC in partially allocated/initialized state.

.. _`notify_shutdown`:

notify_shutdown
===============

.. c:function:: void notify_shutdown(struct cxlflash_cfg *cfg, bool wait)

    notifies device of pending shutdown

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

    :param bool wait:
        Whether to wait for shutdown processing to complete.

.. _`notify_shutdown.description`:

Description
-----------

This function will notify the AFU that the adapter is being shutdown
and will wait for shutdown processing to complete if wait is true.
This notification should flush pending I/Os to the device and halt
further I/Os until the next AFU reset is issued and device restarted.

.. _`cxlflash_get_minor`:

cxlflash_get_minor
==================

.. c:function:: int cxlflash_get_minor( void)

    gets the first available minor number

    :param  void:
        no arguments

.. _`cxlflash_get_minor.return`:

Return
------

Unique minor number that can be used to create the character device.

.. _`cxlflash_put_minor`:

cxlflash_put_minor
==================

.. c:function:: void cxlflash_put_minor(int minor)

    releases the minor number

    :param int minor:
        Minor number that is no longer needed.

.. _`cxlflash_release_chrdev`:

cxlflash_release_chrdev
=======================

.. c:function:: void cxlflash_release_chrdev(struct cxlflash_cfg *cfg)

    release the character device for the host

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

.. _`cxlflash_remove`:

cxlflash_remove
===============

.. c:function:: void cxlflash_remove(struct pci_dev *pdev)

    PCI entry point to tear down host

    :param struct pci_dev \*pdev:
        PCI device associated with the host.

.. _`cxlflash_remove.description`:

Description
-----------

Safe to use as a cleanup in partially allocated/initialized state. Note that
the reset_waitq is flushed as part of the stop/termination of user contexts.

.. _`alloc_mem`:

alloc_mem
=========

.. c:function:: int alloc_mem(struct cxlflash_cfg *cfg)

    allocates the AFU and its command pool

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

.. _`alloc_mem.description`:

Description
-----------

A partially allocated state remains on failure.

.. _`alloc_mem.return`:

Return
------

0 on success
-ENOMEM on failure to allocate memory

.. _`init_pci`:

init_pci
========

.. c:function:: int init_pci(struct cxlflash_cfg *cfg)

    initializes the host as a PCI device

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

.. _`init_pci.return`:

Return
------

0 on success, -errno on failure

.. _`init_scsi`:

init_scsi
=========

.. c:function:: int init_scsi(struct cxlflash_cfg *cfg)

    adds the host to the SCSI stack and kicks off host scan

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

.. _`init_scsi.return`:

Return
------

0 on success, -errno on failure

.. _`set_port_online`:

set_port_online
===============

.. c:function:: void set_port_online(__be64 __iomem *fc_regs)

    transitions the specified host FC port to online state

    :param __be64 __iomem \*fc_regs:
        Top of MMIO region defined for specified port.

.. _`set_port_online.description`:

Description
-----------

The provided MMIO region must be mapped prior to call. Online state means
that the FC link layer has synced, completed the handshaking process, and
is ready for login to start.

.. _`set_port_offline`:

set_port_offline
================

.. c:function:: void set_port_offline(__be64 __iomem *fc_regs)

    transitions the specified host FC port to offline state

    :param __be64 __iomem \*fc_regs:
        Top of MMIO region defined for specified port.

.. _`set_port_offline.description`:

Description
-----------

The provided MMIO region must be mapped prior to call.

.. _`wait_port_online`:

wait_port_online
================

.. c:function:: bool wait_port_online(__be64 __iomem *fc_regs, u32 delay_us, u32 nretry)

    waits for the specified host FC port come online

    :param __be64 __iomem \*fc_regs:
        Top of MMIO region defined for specified port.

    :param u32 delay_us:
        Number of microseconds to delay between reading port status.

    :param u32 nretry:
        Number of cycles to retry reading port status.

.. _`wait_port_online.description`:

Description
-----------

The provided MMIO region must be mapped prior to call. This will timeout
when the cable is not plugged in.

.. _`wait_port_online.return`:

Return
------

TRUE (1) when the specified port is online
FALSE (0) when the specified port fails to come online after timeout

.. _`wait_port_offline`:

wait_port_offline
=================

.. c:function:: bool wait_port_offline(__be64 __iomem *fc_regs, u32 delay_us, u32 nretry)

    waits for the specified host FC port go offline

    :param __be64 __iomem \*fc_regs:
        Top of MMIO region defined for specified port.

    :param u32 delay_us:
        Number of microseconds to delay between reading port status.

    :param u32 nretry:
        Number of cycles to retry reading port status.

.. _`wait_port_offline.description`:

Description
-----------

The provided MMIO region must be mapped prior to call.

.. _`wait_port_offline.return`:

Return
------

TRUE (1) when the specified port is offline
FALSE (0) when the specified port fails to go offline after timeout

.. _`afu_set_wwpn`:

afu_set_wwpn
============

.. c:function:: void afu_set_wwpn(struct afu *afu, int port, __be64 __iomem *fc_regs, u64 wwpn)

    configures the WWPN for the specified host FC port

    :param struct afu \*afu:
        AFU associated with the host that owns the specified FC port.

    :param int port:
        Port number being configured.

    :param __be64 __iomem \*fc_regs:
        Top of MMIO region defined for specified port.

    :param u64 wwpn:
        The world-wide-port-number previously discovered for port.

.. _`afu_set_wwpn.description`:

Description
-----------

The provided MMIO region must be mapped prior to call. As part of the
sequence to configure the WWPN, the port is toggled offline and then back
online. This toggling action can cause this routine to delay up to a few
seconds. When configured to use the internal LUN feature of the AFU, a
failure to come online is overridden.

.. _`afu_link_reset`:

afu_link_reset
==============

.. c:function:: void afu_link_reset(struct afu *afu, int port, __be64 __iomem *fc_regs)

    resets the specified host FC port

    :param struct afu \*afu:
        AFU associated with the host that owns the specified FC port.

    :param int port:
        Port number being configured.

    :param __be64 __iomem \*fc_regs:
        Top of MMIO region defined for specified port.

.. _`afu_link_reset.description`:

Description
-----------

The provided MMIO region must be mapped prior to call. The sequence to
reset the port involves toggling it offline and then back online. This
action can cause this routine to delay up to a few seconds. An effort
is made to maintain link with the device by switching to host to use
the alternate port exclusively while the reset takes place.
failure to come online is overridden.

.. _`afu_err_intr_init`:

afu_err_intr_init
=================

.. c:function:: void afu_err_intr_init(struct afu *afu)

    clears and initializes the AFU for error interrupts

    :param struct afu \*afu:
        AFU associated with the host.

.. _`cxlflash_sync_err_irq`:

cxlflash_sync_err_irq
=====================

.. c:function:: irqreturn_t cxlflash_sync_err_irq(int irq, void *data)

    interrupt handler for synchronous errors

    :param int irq:
        Interrupt number.

    :param void \*data:
        Private data provided at interrupt registration, the AFU.

.. _`cxlflash_sync_err_irq.return`:

Return
------

Always return IRQ_HANDLED.

.. _`process_hrrq`:

process_hrrq
============

.. c:function:: int process_hrrq(struct hwq *hwq, struct list_head *doneq, int budget)

    process the read-response queue

    :param struct hwq \*hwq:
        *undescribed*

    :param struct list_head \*doneq:
        Queue of commands harvested from the RRQ.

    :param int budget:
        Threshold of RRQ entries to process.

.. _`process_hrrq.description`:

Description
-----------

This routine must be called holding the disabled RRQ spin lock.

.. _`process_hrrq.return`:

Return
------

The number of entries processed.

.. _`process_cmd_doneq`:

process_cmd_doneq
=================

.. c:function:: void process_cmd_doneq(struct list_head *doneq)

    process a queue of harvested RRQ commands

    :param struct list_head \*doneq:
        Queue of completed commands.

.. _`process_cmd_doneq.description`:

Description
-----------

Note that upon return the queue can no longer be trusted.

.. _`cxlflash_irqpoll`:

cxlflash_irqpoll
================

.. c:function:: int cxlflash_irqpoll(struct irq_poll *irqpoll, int budget)

    process a queue of harvested RRQ commands

    :param struct irq_poll \*irqpoll:
        IRQ poll structure associated with queue to poll.

    :param int budget:
        Threshold of RRQ entries to process per poll.

.. _`cxlflash_irqpoll.return`:

Return
------

The number of entries processed.

.. _`cxlflash_rrq_irq`:

cxlflash_rrq_irq
================

.. c:function:: irqreturn_t cxlflash_rrq_irq(int irq, void *data)

    interrupt handler for read-response queue (normal path)

    :param int irq:
        Interrupt number.

    :param void \*data:
        Private data provided at interrupt registration, the AFU.

.. _`cxlflash_rrq_irq.return`:

Return
------

IRQ_HANDLED or IRQ_NONE when no ready entries found.

.. _`cxlflash_async_err_irq`:

cxlflash_async_err_irq
======================

.. c:function:: irqreturn_t cxlflash_async_err_irq(int irq, void *data)

    interrupt handler for asynchronous errors

    :param int irq:
        Interrupt number.

    :param void \*data:
        Private data provided at interrupt registration, the AFU.

.. _`cxlflash_async_err_irq.return`:

Return
------

Always return IRQ_HANDLED.

.. _`read_vpd`:

read_vpd
========

.. c:function:: int read_vpd(struct cxlflash_cfg *cfg, u64 wwpn)

    obtains the WWPNs from VPD

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

    :param u64 wwpn:
        Array of size MAX_FC_PORTS to pass back WWPNs

.. _`read_vpd.return`:

Return
------

0 on success, -errno on failure

.. _`init_pcr`:

init_pcr
========

.. c:function:: void init_pcr(struct cxlflash_cfg *cfg)

    initialize the provisioning and control registers

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

.. _`init_pcr.description`:

Description
-----------

Also sets up fast access to the mapped registers and initializes AFU
command fields that never change.

.. _`init_global`:

init_global
===========

.. c:function:: int init_global(struct cxlflash_cfg *cfg)

    initialize AFU global registers

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

.. _`start_afu`:

start_afu
=========

.. c:function:: int start_afu(struct cxlflash_cfg *cfg)

    initializes and starts the AFU

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

.. _`init_intr`:

init_intr
=========

.. c:function:: enum undo_level init_intr(struct cxlflash_cfg *cfg, struct hwq *hwq)

    setup interrupt handlers for the master context

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

    :param struct hwq \*hwq:
        Hardware queue to initialize.

.. _`init_intr.return`:

Return
------

0 on success, -errno on failure

.. _`init_mc`:

init_mc
=======

.. c:function:: int init_mc(struct cxlflash_cfg *cfg, u32 index)

    create and register as the master context

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

    :param u32 index:
        *undescribed*

.. _`init_mc.index`:

index
-----

HWQ Index of the master context.

.. _`init_mc.return`:

Return
------

0 on success, -errno on failure

.. _`get_num_afu_ports`:

get_num_afu_ports
=================

.. c:function:: void get_num_afu_ports(struct cxlflash_cfg *cfg)

    determines and configures the number of AFU ports

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

.. _`get_num_afu_ports.description`:

Description
-----------

This routine determines the number of AFU ports by converting the global
port selection mask. The converted value is only valid following an AFU
reset (explicit or power-on). This routine must be invoked shortly after
mapping as other routines are dependent on the number of ports during the
initialization sequence.

To support legacy AFUs that might not have reflected an initial global
port mask (value read is 0), default to the number of ports originally
supported by the cxlflash driver (2) before hardware with other port
offerings was introduced.

.. _`init_afu`:

init_afu
========

.. c:function:: int init_afu(struct cxlflash_cfg *cfg)

    setup as master context and start AFU

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

.. _`init_afu.description`:

Description
-----------

This routine is a higher level of control for configuring the
AFU on probe and reset paths.

.. _`init_afu.return`:

Return
------

0 on success, -errno on failure

.. _`afu_reset`:

afu_reset
=========

.. c:function:: int afu_reset(struct cxlflash_cfg *cfg)

    resets the AFU

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

.. _`afu_reset.return`:

Return
------

0 on success, -errno on failure

.. _`drain_ioctls`:

drain_ioctls
============

.. c:function:: void drain_ioctls(struct cxlflash_cfg *cfg)

    wait until all currently executing ioctls have completed

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

.. _`drain_ioctls.description`:

Description
-----------

Obtain write access to read/write semaphore that wraps ioctl
handling to 'drain' ioctls currently executing.

.. _`cxlflash_async_reset_host`:

cxlflash_async_reset_host
=========================

.. c:function:: void cxlflash_async_reset_host(void *data, async_cookie_t cookie)

    asynchronous host reset handler

    :param void \*data:
        Private data provided while scheduling reset.

    :param async_cookie_t cookie:
        Cookie that can be used for checkpointing.

.. _`cxlflash_schedule_async_reset`:

cxlflash_schedule_async_reset
=============================

.. c:function:: void cxlflash_schedule_async_reset(struct cxlflash_cfg *cfg)

    schedule an asynchronous host reset

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

.. _`send_afu_cmd`:

send_afu_cmd
============

.. c:function:: int send_afu_cmd(struct afu *afu, struct sisl_ioarcb *rcb)

    builds and sends an internal AFU command

    :param struct afu \*afu:
        AFU associated with the host.

    :param struct sisl_ioarcb \*rcb:
        Pre-populated IOARCB describing command to send.

.. _`send_afu_cmd.description`:

Description
-----------

The AFU can only take one internal AFU command at a time. This limitation is
enforced by using a mutex to provide exclusive access to the AFU during the
operation. This design point requires calling threads to not be on interrupt
context due to the possibility of sleeping during concurrent AFU operations.

The command status is optionally passed back to the caller when the caller
populates the IOASA field of the IOARCB with a pointer to an IOASA structure.

.. _`send_afu_cmd.return`:

Return
------

0 on success, -errno on failure

.. _`cxlflash_afu_sync`:

cxlflash_afu_sync
=================

.. c:function:: int cxlflash_afu_sync(struct afu *afu, ctx_hndl_t ctx, res_hndl_t res, u8 mode)

    builds and sends an AFU sync command

    :param struct afu \*afu:
        AFU associated with the host.

    :param ctx_hndl_t ctx:
        Identifies context requesting sync.

    :param res_hndl_t res:
        Identifies resource requesting sync.

    :param u8 mode:
        Type of sync to issue (lightweight, heavyweight, global).

.. _`cxlflash_afu_sync.description`:

Description
-----------

AFU sync operations are only necessary and allowed when the device is
operating normally. When not operating normally, sync requests can occur as
part of cleaning up resources associated with an adapter prior to removal.
In this scenario, these requests are simply ignored (safe due to the AFU
going away).

.. _`cxlflash_afu_sync.return`:

Return
------

0 on success, -errno on failure

.. _`cxlflash_eh_abort_handler`:

cxlflash_eh_abort_handler
=========================

.. c:function:: int cxlflash_eh_abort_handler(struct scsi_cmnd *scp)

    abort a SCSI command

    :param struct scsi_cmnd \*scp:
        SCSI command to abort.

.. _`cxlflash_eh_abort_handler.description`:

Description
-----------

CXL Flash devices do not support a single command abort. Reset the context
as per SISLite specification. Flush any pending commands in the hardware
queue before the reset.

.. _`cxlflash_eh_abort_handler.return`:

Return
------

SUCCESS/FAILED as defined in scsi/scsi.h

.. _`cxlflash_eh_device_reset_handler`:

cxlflash_eh_device_reset_handler
================================

.. c:function:: int cxlflash_eh_device_reset_handler(struct scsi_cmnd *scp)

    reset a single LUN

    :param struct scsi_cmnd \*scp:
        SCSI command to send.

.. _`cxlflash_eh_device_reset_handler.return`:

Return
------

SUCCESS as defined in scsi/scsi.h
FAILED as defined in scsi/scsi.h

.. _`cxlflash_eh_host_reset_handler`:

cxlflash_eh_host_reset_handler
==============================

.. c:function:: int cxlflash_eh_host_reset_handler(struct scsi_cmnd *scp)

    reset the host adapter

    :param struct scsi_cmnd \*scp:
        SCSI command from stack identifying host.

.. _`cxlflash_eh_host_reset_handler.description`:

Description
-----------

Following a reset, the state is evaluated again in case an EEH occurred
during the reset. In such a scenario, the host reset will either yield
until the EEH recovery is complete or return success or failure based
upon the current device state.

.. _`cxlflash_eh_host_reset_handler.return`:

Return
------

SUCCESS as defined in scsi/scsi.h
FAILED as defined in scsi/scsi.h

.. _`cxlflash_change_queue_depth`:

cxlflash_change_queue_depth
===========================

.. c:function:: int cxlflash_change_queue_depth(struct scsi_device *sdev, int qdepth)

    change the queue depth for the device

    :param struct scsi_device \*sdev:
        SCSI device destined for queue depth change.

    :param int qdepth:
        Requested queue depth value to set.

.. _`cxlflash_change_queue_depth.description`:

Description
-----------

The requested queue depth is capped to the maximum supported value.

.. _`cxlflash_change_queue_depth.return`:

Return
------

The actual queue depth set.

.. _`cxlflash_show_port_status`:

cxlflash_show_port_status
=========================

.. c:function:: ssize_t cxlflash_show_port_status(u32 port, struct cxlflash_cfg *cfg, char *buf)

    queries and presents the current port status

    :param u32 port:
        Desired port for status reporting.

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

    :param char \*buf:
        Buffer of length PAGE_SIZE to report back port status in ASCII.

.. _`cxlflash_show_port_status.return`:

Return
------

The size of the ASCII string returned in \ ``buf``\  or -EINVAL.

.. _`port0_show`:

port0_show
==========

.. c:function:: ssize_t port0_show(struct device *dev, struct device_attribute *attr, char *buf)

    queries and presents the current status of port 0

    :param struct device \*dev:
        Generic device associated with the host owning the port.

    :param struct device_attribute \*attr:
        Device attribute representing the port.

    :param char \*buf:
        Buffer of length PAGE_SIZE to report back port status in ASCII.

.. _`port0_show.return`:

Return
------

The size of the ASCII string returned in \ ``buf``\ .

.. _`port1_show`:

port1_show
==========

.. c:function:: ssize_t port1_show(struct device *dev, struct device_attribute *attr, char *buf)

    queries and presents the current status of port 1

    :param struct device \*dev:
        Generic device associated with the host owning the port.

    :param struct device_attribute \*attr:
        Device attribute representing the port.

    :param char \*buf:
        Buffer of length PAGE_SIZE to report back port status in ASCII.

.. _`port1_show.return`:

Return
------

The size of the ASCII string returned in \ ``buf``\ .

.. _`port2_show`:

port2_show
==========

.. c:function:: ssize_t port2_show(struct device *dev, struct device_attribute *attr, char *buf)

    queries and presents the current status of port 2

    :param struct device \*dev:
        Generic device associated with the host owning the port.

    :param struct device_attribute \*attr:
        Device attribute representing the port.

    :param char \*buf:
        Buffer of length PAGE_SIZE to report back port status in ASCII.

.. _`port2_show.return`:

Return
------

The size of the ASCII string returned in \ ``buf``\ .

.. _`port3_show`:

port3_show
==========

.. c:function:: ssize_t port3_show(struct device *dev, struct device_attribute *attr, char *buf)

    queries and presents the current status of port 3

    :param struct device \*dev:
        Generic device associated with the host owning the port.

    :param struct device_attribute \*attr:
        Device attribute representing the port.

    :param char \*buf:
        Buffer of length PAGE_SIZE to report back port status in ASCII.

.. _`port3_show.return`:

Return
------

The size of the ASCII string returned in \ ``buf``\ .

.. _`lun_mode_show`:

lun_mode_show
=============

.. c:function:: ssize_t lun_mode_show(struct device *dev, struct device_attribute *attr, char *buf)

    presents the current LUN mode of the host

    :param struct device \*dev:
        Generic device associated with the host.

    :param struct device_attribute \*attr:
        Device attribute representing the LUN mode.

    :param char \*buf:
        Buffer of length PAGE_SIZE to report back the LUN mode in ASCII.

.. _`lun_mode_show.return`:

Return
------

The size of the ASCII string returned in \ ``buf``\ .

.. _`lun_mode_store`:

lun_mode_store
==============

.. c:function:: ssize_t lun_mode_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    sets the LUN mode of the host

    :param struct device \*dev:
        Generic device associated with the host.

    :param struct device_attribute \*attr:
        Device attribute representing the LUN mode.

    :param const char \*buf:
        Buffer of length PAGE_SIZE containing the LUN mode in ASCII.

    :param size_t count:
        Length of data resizing in \ ``buf``\ .

.. _`lun_mode_store.description`:

Description
-----------

The CXL Flash AFU supports a dummy LUN mode where the external
links and storage are not required. Space on the FPGA is used
to create 1 or 2 small LUNs which are presented to the system
as if they were a normal storage device. This feature is useful
during development and also provides manufacturing with a way
to test the AFU without an actual device.

0 = external LUN[s] (default)
1 = internal LUN (1 x 64K, 512B blocks, id 0)
2 = internal LUN (1 x 64K, 4K blocks, id 0)
3 = internal LUN (2 x 32K, 512B blocks, ids 0,1)
4 = internal LUN (2 x 32K, 4K blocks, ids 0,1)

.. _`lun_mode_store.return`:

Return
------

The size of the ASCII string returned in \ ``buf``\ .

.. _`ioctl_version_show`:

ioctl_version_show
==================

.. c:function:: ssize_t ioctl_version_show(struct device *dev, struct device_attribute *attr, char *buf)

    presents the current ioctl version of the host

    :param struct device \*dev:
        Generic device associated with the host.

    :param struct device_attribute \*attr:
        Device attribute representing the ioctl version.

    :param char \*buf:
        Buffer of length PAGE_SIZE to report back the ioctl version.

.. _`ioctl_version_show.return`:

Return
------

The size of the ASCII string returned in \ ``buf``\ .

.. _`cxlflash_show_port_lun_table`:

cxlflash_show_port_lun_table
============================

.. c:function:: ssize_t cxlflash_show_port_lun_table(u32 port, struct cxlflash_cfg *cfg, char *buf)

    queries and presents the port LUN table

    :param u32 port:
        Desired port for status reporting.

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

    :param char \*buf:
        Buffer of length PAGE_SIZE to report back port status in ASCII.

.. _`cxlflash_show_port_lun_table.return`:

Return
------

The size of the ASCII string returned in \ ``buf``\  or -EINVAL.

.. _`port0_lun_table_show`:

port0_lun_table_show
====================

.. c:function:: ssize_t port0_lun_table_show(struct device *dev, struct device_attribute *attr, char *buf)

    presents the current LUN table of port 0

    :param struct device \*dev:
        Generic device associated with the host owning the port.

    :param struct device_attribute \*attr:
        Device attribute representing the port.

    :param char \*buf:
        Buffer of length PAGE_SIZE to report back port status in ASCII.

.. _`port0_lun_table_show.return`:

Return
------

The size of the ASCII string returned in \ ``buf``\ .

.. _`port1_lun_table_show`:

port1_lun_table_show
====================

.. c:function:: ssize_t port1_lun_table_show(struct device *dev, struct device_attribute *attr, char *buf)

    presents the current LUN table of port 1

    :param struct device \*dev:
        Generic device associated with the host owning the port.

    :param struct device_attribute \*attr:
        Device attribute representing the port.

    :param char \*buf:
        Buffer of length PAGE_SIZE to report back port status in ASCII.

.. _`port1_lun_table_show.return`:

Return
------

The size of the ASCII string returned in \ ``buf``\ .

.. _`port2_lun_table_show`:

port2_lun_table_show
====================

.. c:function:: ssize_t port2_lun_table_show(struct device *dev, struct device_attribute *attr, char *buf)

    presents the current LUN table of port 2

    :param struct device \*dev:
        Generic device associated with the host owning the port.

    :param struct device_attribute \*attr:
        Device attribute representing the port.

    :param char \*buf:
        Buffer of length PAGE_SIZE to report back port status in ASCII.

.. _`port2_lun_table_show.return`:

Return
------

The size of the ASCII string returned in \ ``buf``\ .

.. _`port3_lun_table_show`:

port3_lun_table_show
====================

.. c:function:: ssize_t port3_lun_table_show(struct device *dev, struct device_attribute *attr, char *buf)

    presents the current LUN table of port 3

    :param struct device \*dev:
        Generic device associated with the host owning the port.

    :param struct device_attribute \*attr:
        Device attribute representing the port.

    :param char \*buf:
        Buffer of length PAGE_SIZE to report back port status in ASCII.

.. _`port3_lun_table_show.return`:

Return
------

The size of the ASCII string returned in \ ``buf``\ .

.. _`irqpoll_weight_show`:

irqpoll_weight_show
===================

.. c:function:: ssize_t irqpoll_weight_show(struct device *dev, struct device_attribute *attr, char *buf)

    presents the current IRQ poll weight for the host

    :param struct device \*dev:
        Generic device associated with the host.

    :param struct device_attribute \*attr:
        Device attribute representing the IRQ poll weight.

    :param char \*buf:
        Buffer of length PAGE_SIZE to report back the current IRQ poll
        weight in ASCII.

.. _`irqpoll_weight_show.description`:

Description
-----------

An IRQ poll weight of 0 indicates polling is disabled.

.. _`irqpoll_weight_show.return`:

Return
------

The size of the ASCII string returned in \ ``buf``\ .

.. _`irqpoll_weight_store`:

irqpoll_weight_store
====================

.. c:function:: ssize_t irqpoll_weight_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    sets the current IRQ poll weight for the host

    :param struct device \*dev:
        Generic device associated with the host.

    :param struct device_attribute \*attr:
        Device attribute representing the IRQ poll weight.

    :param const char \*buf:
        Buffer of length PAGE_SIZE containing the desired IRQ poll
        weight in ASCII.

    :param size_t count:
        Length of data resizing in \ ``buf``\ .

.. _`irqpoll_weight_store.description`:

Description
-----------

An IRQ poll weight of 0 indicates polling is disabled.

.. _`irqpoll_weight_store.return`:

Return
------

The size of the ASCII string returned in \ ``buf``\ .

.. _`num_hwqs_show`:

num_hwqs_show
=============

.. c:function:: ssize_t num_hwqs_show(struct device *dev, struct device_attribute *attr, char *buf)

    presents the number of hardware queues for the host

    :param struct device \*dev:
        Generic device associated with the host.

    :param struct device_attribute \*attr:
        Device attribute representing the number of hardware queues.

    :param char \*buf:
        Buffer of length PAGE_SIZE to report back the number of hardware
        queues in ASCII.

.. _`num_hwqs_show.return`:

Return
------

The size of the ASCII string returned in \ ``buf``\ .

.. _`num_hwqs_store`:

num_hwqs_store
==============

.. c:function:: ssize_t num_hwqs_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    sets the number of hardware queues for the host

    :param struct device \*dev:
        Generic device associated with the host.

    :param struct device_attribute \*attr:
        Device attribute representing the number of hardware queues.

    :param const char \*buf:
        Buffer of length PAGE_SIZE containing the number of hardware
        queues in ASCII.

    :param size_t count:
        Length of data resizing in \ ``buf``\ .

.. _`num_hwqs_store.description`:

Description
-----------

n > 0: num_hwqs = n
n = 0: num_hwqs = \ :c:func:`num_online_cpus`\ 
n < 0: \ :c:func:`num_online_cpus`\  / abs(n)

.. _`num_hwqs_store.return`:

Return
------

The size of the ASCII string returned in \ ``buf``\ .

.. _`hwq_mode_show`:

hwq_mode_show
=============

.. c:function:: ssize_t hwq_mode_show(struct device *dev, struct device_attribute *attr, char *buf)

    presents the HWQ steering mode for the host

    :param struct device \*dev:
        Generic device associated with the host.

    :param struct device_attribute \*attr:
        Device attribute representing the HWQ steering mode.

    :param char \*buf:
        Buffer of length PAGE_SIZE to report back the HWQ steering mode
        as a character string.

.. _`hwq_mode_show.return`:

Return
------

The size of the ASCII string returned in \ ``buf``\ .

.. _`hwq_mode_store`:

hwq_mode_store
==============

.. c:function:: ssize_t hwq_mode_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    sets the HWQ steering mode for the host

    :param struct device \*dev:
        Generic device associated with the host.

    :param struct device_attribute \*attr:
        Device attribute representing the HWQ steering mode.

    :param const char \*buf:
        Buffer of length PAGE_SIZE containing the HWQ steering mode
        as a character string.

    :param size_t count:
        Length of data resizing in \ ``buf``\ .

.. _`hwq_mode_store.description`:

Description
-----------

rr = Round-Robin
tag = Block MQ Tagging
cpu = CPU Affinity

.. _`hwq_mode_store.return`:

Return
------

The size of the ASCII string returned in \ ``buf``\ .

.. _`mode_show`:

mode_show
=========

.. c:function:: ssize_t mode_show(struct device *dev, struct device_attribute *attr, char *buf)

    presents the current mode of the device

    :param struct device \*dev:
        Generic device associated with the device.

    :param struct device_attribute \*attr:
        Device attribute representing the device mode.

    :param char \*buf:
        Buffer of length PAGE_SIZE to report back the dev mode in ASCII.

.. _`mode_show.return`:

Return
------

The size of the ASCII string returned in \ ``buf``\ .

.. _`cxlflash_worker_thread`:

cxlflash_worker_thread
======================

.. c:function:: void cxlflash_worker_thread(struct work_struct *work)

    work thread handler for the AFU

    :param struct work_struct \*work:
        Work structure contained within cxlflash associated with host.

.. _`cxlflash_worker_thread.handles-the-following-events`:

Handles the following events
----------------------------

- Link reset which cannot be performed on interrupt context due to
blocking up to a few seconds
- Rescan the host

.. _`cxlflash_chr_open`:

cxlflash_chr_open
=================

.. c:function:: int cxlflash_chr_open(struct inode *inode, struct file *file)

    character device open handler

    :param struct inode \*inode:
        Device inode associated with this character device.

    :param struct file \*file:
        File pointer for this device.

.. _`cxlflash_chr_open.description`:

Description
-----------

Only users with admin privileges are allowed to open the character device.

.. _`cxlflash_chr_open.return`:

Return
------

0 on success, -errno on failure

.. _`decode_hioctl`:

decode_hioctl
=============

.. c:function:: char *decode_hioctl(int cmd)

    translates encoded host ioctl to easily identifiable string

    :param int cmd:
        The host ioctl command to decode.

.. _`decode_hioctl.return`:

Return
------

A string identifying the decoded host ioctl.

.. _`cxlflash_lun_provision`:

cxlflash_lun_provision
======================

.. c:function:: int cxlflash_lun_provision(struct cxlflash_cfg *cfg, struct ht_cxlflash_lun_provision *lunprov)

    host LUN provisioning handler

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

    :param struct ht_cxlflash_lun_provision \*lunprov:
        *undescribed*

.. _`cxlflash_lun_provision.return`:

Return
------

0 on success, -errno on failure

.. _`cxlflash_afu_debug`:

cxlflash_afu_debug
==================

.. c:function:: int cxlflash_afu_debug(struct cxlflash_cfg *cfg, struct ht_cxlflash_afu_debug *afu_dbg)

    host AFU debug handler

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

    :param struct ht_cxlflash_afu_debug \*afu_dbg:
        *undescribed*

.. _`cxlflash_afu_debug.description`:

Description
-----------

For debug requests requiring a data buffer, always provide an aligned
(cache line) buffer to the AFU to appease any alignment requirements.

.. _`cxlflash_afu_debug.return`:

Return
------

0 on success, -errno on failure

.. _`cxlflash_chr_ioctl`:

cxlflash_chr_ioctl
==================

.. c:function:: long cxlflash_chr_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    character device IOCTL handler

    :param struct file \*file:
        File pointer for this device.

    :param unsigned int cmd:
        IOCTL command.

    :param unsigned long arg:
        Userspace ioctl data structure.

.. _`cxlflash_chr_ioctl.description`:

Description
-----------

A read/write semaphore is used to implement a 'drain' of currently
running ioctls. The read semaphore is taken at the beginning of each
ioctl thread and released upon concluding execution. Additionally the
semaphore should be released and then reacquired in any ioctl execution
path which will wait for an event to occur that is outside the scope of
the ioctl (i.e. an adapter reset). To drain the ioctls currently running,
a thread simply needs to acquire the write semaphore.

.. _`cxlflash_chr_ioctl.return`:

Return
------

0 on success, -errno on failure

.. _`init_chrdev`:

init_chrdev
===========

.. c:function:: int init_chrdev(struct cxlflash_cfg *cfg)

    initialize the character device for the host

    :param struct cxlflash_cfg \*cfg:
        Internal structure associated with the host.

.. _`init_chrdev.return`:

Return
------

0 on success, -errno on failure

.. _`cxlflash_probe`:

cxlflash_probe
==============

.. c:function:: int cxlflash_probe(struct pci_dev *pdev, const struct pci_device_id *dev_id)

    PCI entry point to add host

    :param struct pci_dev \*pdev:
        PCI device associated with the host.

    :param const struct pci_device_id \*dev_id:
        PCI device id associated with device.

.. _`cxlflash_probe.description`:

Description
-----------

The device will initially start out in a 'probing' state and
transition to the 'normal' state at the end of a successful
probe. Should an EEH event occur during probe, the notification
thread (error_detected()) will wait until the probe handler
is nearly complete. At that time, the device will be moved to
a 'probed' state and the EEH thread woken up to drive the slot
reset and recovery (device moves to 'normal' state). Meanwhile,
the probe will be allowed to exit successfully.

.. _`cxlflash_probe.return`:

Return
------

0 on success, -errno on failure

.. _`cxlflash_pci_error_detected`:

cxlflash_pci_error_detected
===========================

.. c:function:: pci_ers_result_t cxlflash_pci_error_detected(struct pci_dev *pdev, pci_channel_state_t state)

    called when a PCI error is detected

    :param struct pci_dev \*pdev:
        PCI device struct.

    :param pci_channel_state_t state:
        PCI channel state.

.. _`cxlflash_pci_error_detected.description`:

Description
-----------

When an EEH occurs during an active reset, wait until the reset is
complete and then take action based upon the device state.

.. _`cxlflash_pci_error_detected.return`:

Return
------

PCI_ERS_RESULT_NEED_RESET or PCI_ERS_RESULT_DISCONNECT

.. _`cxlflash_pci_slot_reset`:

cxlflash_pci_slot_reset
=======================

.. c:function:: pci_ers_result_t cxlflash_pci_slot_reset(struct pci_dev *pdev)

    called when PCI slot has been reset

    :param struct pci_dev \*pdev:
        PCI device struct.

.. _`cxlflash_pci_slot_reset.description`:

Description
-----------

This routine is called by the pci error recovery code after the PCI
slot has been reset, just before we should resume normal operations.

.. _`cxlflash_pci_slot_reset.return`:

Return
------

PCI_ERS_RESULT_RECOVERED or PCI_ERS_RESULT_DISCONNECT

.. _`cxlflash_pci_resume`:

cxlflash_pci_resume
===================

.. c:function:: void cxlflash_pci_resume(struct pci_dev *pdev)

    called when normal operation can resume

    :param struct pci_dev \*pdev:
        PCI device struct

.. _`cxlflash_devnode`:

cxlflash_devnode
================

.. c:function:: char *cxlflash_devnode(struct device *dev, umode_t *mode)

    provides devtmpfs for devices in the cxlflash class

    :param struct device \*dev:
        Character device.

    :param umode_t \*mode:
        Mode that can be used to verify access.

.. _`cxlflash_devnode.return`:

Return
------

Allocated string describing the devtmpfs structure.

.. _`cxlflash_class_init`:

cxlflash_class_init
===================

.. c:function:: int cxlflash_class_init( void)

    create character device class

    :param  void:
        no arguments

.. _`cxlflash_class_init.return`:

Return
------

0 on success, -errno on failure

.. _`cxlflash_class_exit`:

cxlflash_class_exit
===================

.. c:function:: void cxlflash_class_exit( void)

    destroy character device class

    :param  void:
        no arguments

.. _`init_cxlflash`:

init_cxlflash
=============

.. c:function:: int init_cxlflash( void)

    module entry point

    :param  void:
        no arguments

.. _`init_cxlflash.return`:

Return
------

0 on success, -errno on failure

.. _`exit_cxlflash`:

exit_cxlflash
=============

.. c:function:: void __exit exit_cxlflash( void)

    module exit point

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

