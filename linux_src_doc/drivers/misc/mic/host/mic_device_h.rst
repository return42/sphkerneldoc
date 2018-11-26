.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/host/mic_device.h

.. _`mic_stepping`:

enum mic_stepping
=================

.. c:type:: enum mic_stepping

    MIC stepping ids.

.. _`mic_stepping.definition`:

Definition
----------

.. code-block:: c

    enum mic_stepping {
        MIC_A0_STEP,
        MIC_B0_STEP,
        MIC_B1_STEP,
        MIC_C0_STEP
    };

.. _`mic_stepping.constants`:

Constants
---------

MIC_A0_STEP
    *undescribed*

MIC_B0_STEP
    *undescribed*

MIC_B1_STEP
    *undescribed*

MIC_C0_STEP
    *undescribed*

.. _`mic_device`:

struct mic_device
=================

.. c:type:: struct mic_device

    MIC device information for each card.

.. _`mic_device.definition`:

Definition
----------

.. code-block:: c

    struct mic_device {
        struct mic_mw mmio;
        struct mic_mw aper;
        enum mic_hw_family family;
        struct mic_hw_ops *ops;
        int id;
        enum mic_stepping stepping;
        struct pci_dev *pdev;
        struct mutex mic_mutex;
        struct mic_hw_intr_ops *intr_ops;
        struct mic_smpt_ops *smpt_ops;
        struct mic_smpt_info *smpt;
        struct mic_intr_info *intr_info;
        struct mic_irq_info irq_info;
        struct dentry *dbg_dir;
        u32 bootaddr;
        void *dp;
        dma_addr_t dp_dma_addr;
        struct mbus_device *dma_mbdev;
        struct dma_chan *dma_ch[MIC_MAX_DMA_CHAN];
        int num_dma_ch;
        struct scif_hw_dev *scdev;
        struct vop_device *vpdev;
        struct cosm_device *cosm_dev;
    }

.. _`mic_device.members`:

Members
-------

mmio
    MMIO bar information.

aper
    Aperture bar information.

family
    The MIC family to which this device belongs.

ops
    MIC HW specific operations.

id
    The unique device id for this MIC device.

stepping
    Stepping ID.

pdev
    Underlying PCI device.

mic_mutex
    Mutex for synchronizing access to mic_device.

intr_ops
    HW specific interrupt operations.

smpt_ops
    Hardware specific SMPT operations.

smpt
    MIC SMPT information.

intr_info
    H/W specific interrupt information.

irq_info
    The OS specific irq information

dbg_dir
    debugfs directory of this MIC device.

bootaddr
    MIC boot address.

dp
    virtio device page

dp_dma_addr
    virtio device page DMA address.

dma_mbdev
    MIC BUS DMA device.
    \ ``dma_ch``\  - Array of DMA channels
    \ ``num_dma_ch``\  - Number of DMA channels available

dma_ch
    *undescribed*

num_dma_ch
    *undescribed*

scdev
    SCIF device on the SCIF virtual bus.

vpdev
    Virtio over PCIe device on the VOP virtual bus.

cosm_dev
    COSM device

.. _`mic_hw_ops`:

struct mic_hw_ops
=================

.. c:type:: struct mic_hw_ops

    MIC HW specific operations.

.. _`mic_hw_ops.definition`:

Definition
----------

.. code-block:: c

    struct mic_hw_ops {
        u8 aper_bar;
        u8 mmio_bar;
        u32 (*read_spad)(struct mic_device *mdev, unsigned int idx);
        void (*write_spad)(struct mic_device *mdev, unsigned int idx, u32 val);
        void (*send_intr)(struct mic_device *mdev, int doorbell);
        u32 (*ack_interrupt)(struct mic_device *mdev);
        void (*intr_workarounds)(struct mic_device *mdev);
        void (*reset)(struct mic_device *mdev);
        void (*reset_fw_ready)(struct mic_device *mdev);
        bool (*is_fw_ready)(struct mic_device *mdev);
        void (*send_firmware_intr)(struct mic_device *mdev);
        int (*load_mic_fw)(struct mic_device *mdev, const char *buf);
        u32 (*get_postcode)(struct mic_device *mdev);
        bool (*dma_filter)(struct dma_chan *chan, void *param);
    }

.. _`mic_hw_ops.members`:

Members
-------

aper_bar
    Aperture bar resource number.

mmio_bar
    MMIO bar resource number.

read_spad
    Read from scratch pad register.

write_spad
    Write to scratch pad register.

send_intr
    Send an interrupt for a particular doorbell on the card.

ack_interrupt
    Hardware specific operations to ack the h/w on
    receipt of an interrupt.

intr_workarounds
    Hardware specific workarounds needed after
    handling an interrupt.

reset
    Reset the remote processor.

reset_fw_ready
    Reset firmware ready field.

is_fw_ready
    Check if firmware is ready for OS download.

send_firmware_intr
    Send an interrupt to the card firmware.

load_mic_fw
    Load firmware segments required to boot the card
    into card memory. This includes the kernel, command line, ramdisk etc.

get_postcode
    Get post code status from firmware.

dma_filter
    DMA filter function to be used.

.. _`mic_mmio_read`:

mic_mmio_read
=============

.. c:function:: u32 mic_mmio_read(struct mic_mw *mw, u32 offset)

    read from an MMIO register.

    :param mw:
        MMIO register base virtual address.
    :type mw: struct mic_mw \*

    :param offset:
        register offset.
    :type offset: u32

.. _`mic_mmio_read.return`:

Return
------

register value.

.. _`mic_mmio_write`:

mic_mmio_write
==============

.. c:function:: void mic_mmio_write(struct mic_mw *mw, u32 val, u32 offset)

    write to an MMIO register.

    :param mw:
        MMIO register base virtual address.
    :type mw: struct mic_mw \*

    :param val:
        the data value to put into the register
    :type val: u32

    :param offset:
        register offset.
    :type offset: u32

.. _`mic_mmio_write.return`:

Return
------

none.

.. This file was automatic generated / don't edit.

