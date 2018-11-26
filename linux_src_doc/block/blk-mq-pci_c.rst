.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-mq-pci.c

.. _`blk_mq_pci_map_queues`:

blk_mq_pci_map_queues
=====================

.. c:function:: int blk_mq_pci_map_queues(struct blk_mq_tag_set *set, struct pci_dev *pdev, int offset)

    provide a default queue mapping for PCI device

    :param set:
        tagset to provide the mapping for
    :type set: struct blk_mq_tag_set \*

    :param pdev:
        PCI device associated with \ ``set``\ .
    :type pdev: struct pci_dev \*

    :param offset:
        Offset to use for the pci irq vector
    :type offset: int

.. _`blk_mq_pci_map_queues.description`:

Description
-----------

This function assumes the PCI device \ ``pdev``\  has at least as many available
interrupt vectors as \ ``set``\  has queues.  It will then query the vector
corresponding to each queue for it's affinity mask and built queue mapping
that maps a queue to the CPUs that have irq affinity for the corresponding
vector.

.. This file was automatic generated / don't edit.

