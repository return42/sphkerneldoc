
.. _libataDriverApi:

=================
libata Driver API
=================

struct ata_port_operations is defined for every low-level libata hardware driver, and it controls how the low-level driver interfaces with the ATA and SCSI layers.

FIS-based drivers will hook into the system with ->qc_prep() and ->qc_issue() high-level hooks. Hardware which behaves in a manner similar to PCI IDE hardware may utilize several
generic helpers, defining at a bare minimum the bus I/O addresses of the ATA shadow register blocks.


struct ata_port_operations
==========================


Disable ATA port
----------------


.. code-block:: c

    void (*port_disable) (struct ata_port *);

Called from ata_bus_probe() error path, as well as when unregistering from the SCSI module (rmmod, hot unplug). This function should do whatever needs to be done to take the port
out of use. In most cases, ata_port_disable() can be used as this hook.

Called from ata_bus_probe() on a failed probe. Called from ata_scsi_release().


Post-IDENTIFY device configuration
----------------------------------


.. code-block:: c

    void (*dev_config) (struct ata_port *, struct ata_device *);

Called after IDENTIFY [PACKET] DEVICE is issued to each device found. Typically used to apply device-specific fixups prior to issue of SET FEATURES - XFER MODE, and prior to
operation.

This entry may be specified as NULL in ata_port_operations.


Set PIO/DMA mode
----------------


.. code-block:: c

    void (*set_piomode) (struct ata_port *, struct ata_device *);
    void (*set_dmamode) (struct ata_port *, struct ata_device *);
    void (*post_set_mode) (struct ata_port *);
    unsigned int (*mode_filter) (struct ata_port *, struct ata_device *, unsigned int);

Hooks called prior to the issue of SET FEATURES - XFER MODE command. The optional ->mode_filter() hook is called when libata has built a mask of the possible modes. This is passed
to the ->mode_filter() function which should return a mask of valid modes after filtering those unsuitable due to hardware limits. It is not valid to use this interface to add
modes.

dev->pio_mode and dev->dma_mode are guaranteed to be valid when ->set_piomode() and when ->set_dmamode() is called. The timings for any other drive sharing the cable will also
be valid at this point. That is the library records the decisions for the modes of each drive on a channel before it attempts to set any of them.

->post_set_mode() is called unconditionally, after the SET FEATURES - XFER MODE command completes successfully.

->set_piomode() is always called (if present), but ->set_dma_mode() is only called if DMA is possible.


Taskfile read/write
-------------------


.. code-block:: c

    void (*sff_tf_load) (struct ata_port *ap, struct ata_taskfile *tf);
    void (*sff_tf_read) (struct ata_port *ap, struct ata_taskfile *tf);

->tf_load() is called to load the given taskfile into hardware registers / DMA buffers. ->tf_read() is called to read the hardware registers / DMA buffers, to obtain the current
set of taskfile register values. Most drivers for taskfile-based hardware (PIO or MMIO) use ata_sff_tf_load() and ata_sff_tf_read() for these hooks.


PIO data read/write
-------------------


.. code-block:: c

    void (*sff_data_xfer) (struct ata_device *, unsigned char *, unsigned int, int);

All bmdma-style drivers must implement this hook. This is the low-level operation that actually copies the data bytes during a PIO data transfer. Typically the driver will choose
one of ata_sff_data_xfer_noirq(), ata_sff_data_xfer(), or ata_sff_data_xfer32().


ATA command execute
-------------------


.. code-block:: c

    void (*sff_exec_command)(struct ata_port *ap, struct ata_taskfile *tf);

causes an ATA command, previously loaded with ->tf_load(), to be initiated in hardware. Most drivers for taskfile-based hardware use ata_sff_exec_command() for this hook.


Per-cmd ATAPI DMA capabilities filter
-------------------------------------


.. code-block:: c

    int (*check_atapi_dma) (struct ata_queued_cmd *qc);

Allow low-level driver to filter ATA PACKET commands, returning a status indicating whether or not it is OK to use DMA for the supplied PACKET command.

This hook may be specified as NULL, in which case libata will assume that atapi dma can be supported.


Read specific ATA shadow registers
----------------------------------


.. code-block:: c

    u8   (*sff_check_status)(struct ata_port *ap);
    u8   (*sff_check_altstatus)(struct ata_port *ap);

Reads the Status/AltStatus ATA shadow register from hardware. On some hardware, reading the Status register has the side effect of clearing the interrupt condition. Most drivers
for taskfile-based hardware use ata_sff_check_status() for this hook.


Write specific ATA shadow register
----------------------------------


.. code-block:: c

    void (*sff_set_devctl)(struct ata_port *ap, u8 ctl);

Write the device control ATA shadow register to the hardware. Most drivers don't need to define this.


Select ATA device on bus
------------------------


.. code-block:: c

    void (*sff_dev_select)(struct ata_port *ap, unsigned int device);

Issues the low-level hardware command(s) that causes one of N hardware devices to be considered 'selected' (active and available for use) on the ATA bus. This generally has no
meaning on FIS-based devices.

Most drivers for taskfile-based hardware use ata_sff_dev_select() for this hook.


Private tuning method
---------------------


.. code-block:: c

    void (*set_mode) (struct ata_port *ap);

By default libata performs drive and controller tuning in accordance with the ATA timing rules and also applies blacklists and cable limits. Some controllers need special handling
and have custom tuning rules, typically raid controllers that use ATA commands but do not actually do drive timing.

    **Warning**

    This hook should not be used to replace the standard controller tuning logic when a controller has quirks. Replacing the default tuning logic in that case would bypass handling
    for drive and bridge quirks that may be important to data reliability. If a controller needs to filter the mode selection it should use the mode_filter hook instead.


Control PCI IDE BMDMA engine
----------------------------


.. code-block:: c

    void (*bmdma_setup) (struct ata_queued_cmd *qc);
    void (*bmdma_start) (struct ata_queued_cmd *qc);
    void (*bmdma_stop) (struct ata_port *ap);
    u8   (*bmdma_status) (struct ata_port *ap);

When setting up an IDE BMDMA transaction, these hooks arm (->bmdma_setup), fire (->bmdma_start), and halt (->bmdma_stop) the hardware's DMA engine. ->bmdma_status is used to
read the standard PCI IDE DMA Status register.

These hooks are typically either no-ops, or simply not implemented, in FIS-based drivers.

Most legacy IDE drivers use ata_bmdma_setup() for the bmdma_setup() hook. ata_bmdma_setup() will write the pointer to the PRD table to the IDE PRD Table Address register,
enable DMA in the DMA Command register, and call exec_command() to begin the transfer.

Most legacy IDE drivers use ata_bmdma_start() for the bmdma_start() hook. ata_bmdma_start() will write the ATA_DMA_START flag to the DMA Command register.

Many legacy IDE drivers use ata_bmdma_stop() for the bmdma_stop() hook. ata_bmdma_stop() clears the ATA_DMA_START flag in the DMA command register.

Many legacy IDE drivers use ata_bmdma_status() as the bmdma_status() hook.


High-level taskfile hooks
-------------------------


.. code-block:: c

    void (*qc_prep) (struct ata_queued_cmd *qc);
    int (*qc_issue) (struct ata_queued_cmd *qc);

Higher-level hooks, these two hooks can potentially supercede several of the above taskfile/DMA engine hooks. ->qc_prep is called after the buffers have been DMA-mapped, and is
typically used to populate the hardware's DMA scatter-gather table. Most drivers use the standard ata_qc_prep() helper function, but more advanced drivers roll their own.

->qc_issue is used to make a command active, once the hardware and S/G tables have been prepared. IDE BMDMA drivers use the helper function ata_qc_issue_prot() for taskfile
protocol-based dispatch. More advanced drivers implement their own ->qc_issue.

ata_qc_issue_prot() calls ->tf_load(), ->bmdma_setup(), and ->bmdma_start() as necessary to initiate a transfer.


Exception and probe handling (EH)
---------------------------------


.. code-block:: c

    void (*eng_timeout) (struct ata_port *ap);
    void (*phy_reset) (struct ata_port *ap);

Deprecated. Use ->error_handler() instead.


.. code-block:: c

    void (*freeze) (struct ata_port *ap);
    void (*thaw) (struct ata_port *ap);

ata_port_freeze() is called when HSM violations or some other condition disrupts normal operation of the port. A frozen port is not allowed to perform any operation until the
port is thawed, which usually follows a successful reset.

The optional ->freeze() callback can be used for freezing the port hardware-wise (e.g. mask interrupt and stop DMA engine). If a port cannot be frozen hardware-wise, the interrupt
handler must ack and clear interrupts unconditionally while the port is frozen.

The optional ->thaw() callback is called to perform the opposite of ->freeze(): prepare the port for normal operation once again. Unmask interrupts, start DMA engine, etc.


.. code-block:: c

    void (*error_handler) (struct ata_port *ap);

->error_handler() is a driver's hook into probe, hotplug, and recovery and other exceptional conditions. The primary responsibility of an implementation is to call ata_do_eh()
or ata_bmdma_drive_eh() with a set of EH hooks as arguments:

'prereset' hook (may be NULL) is called during an EH reset, before any other actions are taken.

'postreset' hook (may be NULL) is called after the EH reset is performed. Based on existing conditions, severity of the problem, and hardware capabilities,

Either 'softreset' (may be NULL) or 'hardreset' (may be NULL) will be called to perform the low-level EH reset.


.. code-block:: c

    void (*post_internal_cmd) (struct ata_queued_cmd *qc);

Perform any hardware-specific actions necessary to finish processing after executing a probe-time or EH-time command via ata_exec_internal().


Hardware interrupt handling
---------------------------


.. code-block:: c

    irqreturn_t (*irq_handler)(int, void *, struct pt_regs *);
    void (*irq_clear) (struct ata_port *);

->irq_handler is the interrupt handling routine registered with the system, by libata. ->irq_clear is called during probe just before the interrupt handler is registered, to be
sure hardware is quiet.

The second argument, dev_instance, should be cast to a pointer to struct ata_host_set.

Most legacy IDE drivers use ata_sff_interrupt() for the irq_handler hook, which scans all ports in the host_set, determines which queued command was active (if any), and calls
ata_sff_host_intr(ap,qc).

Most legacy IDE drivers use ata_sff_irq_clear() for the irq_clear() hook, which simply clears the interrupt and error flags in the DMA status register.


SATA phy read/write
-------------------


.. code-block:: c

    int (*scr_read) (struct ata_port *ap, unsigned int sc_reg,
             u32 *val);
    int (*scr_write) (struct ata_port *ap, unsigned int sc_reg,
                       u32 val);

Read and write standard SATA phy registers. Currently only used if ->phy_reset hook called the sata_phy_reset() helper function. sc_reg is one of SCR_STATUS, SCR_CONTROL,
SCR_ERROR, or SCR_ACTIVE.


Init and shutdown
-----------------


.. code-block:: c

    int (*port_start) (struct ata_port *ap);
    void (*port_stop) (struct ata_port *ap);
    void (*host_stop) (struct ata_host_set *host_set);

->port_start() is called just after the data structures for each port are initialized. Typically this is used to alloc per-port DMA buffers / tables / rings, enable DMA engines,
and similar tasks. Some drivers also use this entry point as a chance to allocate driver-private memory for ap->private_data.

Many drivers use ata_port_start() as this hook or call it from their own port_start() hooks. ata_port_start() allocates space for a legacy IDE PRD table and returns.

->port_stop() is called after ->host_stop(). Its sole function is to release DMA/memory resources, now that they are no longer actively being used. Many drivers also free
driver-private data from port at this time.

->host_stop() is called after all ->port_stop() calls have completed. The hook must finalize hardware shutdown, release DMA and other resources, etc. This hook may be specified
as NULL, in which case it is not called.
