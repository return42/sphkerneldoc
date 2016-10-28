.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/ide.h

.. _`ide_port_ops`:

struct ide_port_ops
===================

.. c:type:: struct ide_port_ops

    IDE port operations

.. _`ide_port_ops.definition`:

Definition
----------

.. code-block:: c

    struct ide_port_ops {
        void (*init_dev)(ide_drive_t *);
        void (*set_pio_mode)(struct hwif_s *, ide_drive_t *);
        void (*set_dma_mode)(struct hwif_s *, ide_drive_t *);
        int (*reset_poll)(ide_drive_t *);
        void (*pre_reset)(ide_drive_t *);
        void (*resetproc)(ide_drive_t *);
        void (*maskproc)(ide_drive_t *, int);
        void (*quirkproc)(ide_drive_t *);
        void (*clear_irq)(ide_drive_t *);
        int (*test_irq)(struct hwif_s *);
        u8 (*mdma_filter)(ide_drive_t *);
        u8 (*udma_filter)(ide_drive_t *);
        u8 (*cable_detect)(struct hwif_s *);
    }

.. _`ide_port_ops.members`:

Members
-------

init_dev
    host specific initialization of a device

set_pio_mode
    routine to program host for PIO mode

set_dma_mode
    routine to program host for DMA mode

reset_poll
    chipset polling based on hba specifics

pre_reset
    chipset specific changes to default for device-hba resets

resetproc
    routine to reset controller after a disk reset

maskproc
    special host masking for drive selection

quirkproc
    check host's drive quirk list

clear_irq
    clear IRQ

test_irq
    *undescribed*

mdma_filter
    filter MDMA modes

udma_filter
    filter UDMA modes

cable_detect
    detect cable type

.. This file was automatic generated / don't edit.

