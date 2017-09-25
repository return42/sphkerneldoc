.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/card/mic_device.h

.. _`mic_intr_info`:

struct mic_intr_info
====================

.. c:type:: struct mic_intr_info

    Contains h/w specific interrupt sources info

.. _`mic_intr_info.definition`:

Definition
----------

.. code-block:: c

    struct mic_intr_info {
        u32 num_intr;
    }

.. _`mic_intr_info.members`:

Members
-------

num_intr
    The number of irqs available

.. _`mic_irq_info`:

struct mic_irq_info
===================

.. c:type:: struct mic_irq_info

    OS specific irq information

.. _`mic_irq_info.definition`:

Definition
----------

.. code-block:: c

    struct mic_irq_info {
        int *irq_usage_count;
    }

.. _`mic_irq_info.members`:

Members
-------

irq_usage_count
    usage count array tracking the number of sources
    assigned for each irq.

.. _`mic_device`:

struct mic_device
=================

.. c:type:: struct mic_device

    MIC device information.

.. _`mic_device.definition`:

Definition
----------

.. code-block:: c

    struct mic_device {
        struct mic_mw mmio;
    }

.. _`mic_device.members`:

Members
-------

mmio
    MMIO bar information.

.. _`mic_driver`:

struct mic_driver
=================

.. c:type:: struct mic_driver

    MIC card driver information.

.. _`mic_driver.definition`:

Definition
----------

.. code-block:: c

    struct mic_driver {
        char name[20];
        struct dentry *dbg_dir;
        struct device *dev;
        void __iomem *dp;
        struct mic_device mdev;
        struct work_struct hotplug_work;
        struct mic_irq_info irq_info;
        struct mic_intr_info intr_info;
        struct mbus_device *dma_mbdev;
        struct dma_chan *dma_ch[MIC_MAX_DMA_CHAN];
        int num_dma_ch;
        struct scif_hw_dev *scdev;
        struct vop_device *vpdev;
    }

.. _`mic_driver.members`:

Members
-------

name
    Name for MIC driver.

dbg_dir
    debugfs directory of this MIC device.

dev
    The device backing this MIC.

dp
    The pointer to the virtio device page.

mdev
    MIC device information for the host.

hotplug_work
    Hot plug work for adding/removing virtio devices.

irq_info
    The OS specific irq information

intr_info
    H/W specific interrupt information.

dma_mbdev
    dma device on the MIC virtual bus.
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

.. _`mic_mmio_read`:

mic_mmio_read
=============

.. c:function:: u32 mic_mmio_read(struct mic_mw *mw, u32 offset)

    read from an MMIO register.

    :param struct mic_mw \*mw:
        MMIO register base virtual address.

    :param u32 offset:
        register offset.

.. _`mic_mmio_read.return`:

Return
------

register value.

.. _`mic_mmio_write`:

mic_mmio_write
==============

.. c:function:: void mic_mmio_write(struct mic_mw *mw, u32 val, u32 offset)

    write to an MMIO register.

    :param struct mic_mw \*mw:
        MMIO register base virtual address.

    :param u32 val:
        the data value to put into the register

    :param u32 offset:
        register offset.

.. _`mic_mmio_write.return`:

Return
------

none.

.. This file was automatic generated / don't edit.

