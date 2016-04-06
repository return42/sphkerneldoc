
.. _API-intel-vgt-balloon:

=================
intel_vgt_balloon
=================

*man intel_vgt_balloon(9)*

*4.6.0-rc1*

balloon out reserved graphics address trunks


Synopsis
========

.. c:function:: int intel_vgt_balloon( struct drm_device * dev )

Arguments
=========

``dev``
    drm device


Description
===========

This function is called at the initialization stage, to balloon out the graphic address space allocated to other vGPUs, by marking these spaces as reserved. The ballooning related
knowledge(starting address and size of the mappable/unmappable graphic memory) is described in the vgt_if structure in a reserved mmio range.

To give an example, the drawing below depicts one typical scenario after ballooning. Here the vGPU1 has 2 pieces of graphic address spaces ballooned out each for the mappable and
the non-mappable part. From the vGPU1 point of view, the total size is the same as the physical one, with the start address of its graphic space being zero. Yet there are some
portions ballooned out( the shadow part, which are marked as reserved by drm allocator). From the host point of view, the graphic address space is partitioned by multiple vGPUs in
different VMs.

vGPU1 view Host view 0 ------> +-----------+ +-----------+ ^ |///////////| | vGPU3 | | |///////////| +-----------+ | |///////////| | vGPU2 | | +-----------+
+-----------+ mappable GM | available | ==> | vGPU1 | | +-----------+ +-----------+ | |///////////| | | v |///////////| | Host | +=======+===========+ +===========+ ^
|///////////| | vGPU3 | | |///////////| +-----------+ | |///////////| | vGPU2 | | +-----------+ +-----------+ unmappable GM | available | ==> | vGPU1 | |
+-----------+ +-----------+ | |///////////| | | | |///////////| | Host | v |///////////| | | total GM size ------> +-----------+ +-----------+


Returns
=======

zero on success, non-zero if configuration invalid or ballooning failed
