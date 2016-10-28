.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firewire/init_ohci1394_dma.c

.. _`init_ohci1394_wait_for_busresets`:

init_ohci1394_wait_for_busresets
================================

.. c:function:: void init_ohci1394_wait_for_busresets(struct ohci *ohci)

    wait until bus resets are completed

    :param struct ohci \*ohci:
        *undescribed*

.. _`init_ohci1394_wait_for_busresets.description`:

Description
-----------

OHCI1394 initialization itself and any device going on- or offline
and any cable issue cause a IEEE1394 bus reset. The OHCI1394 spec
specifies that physical DMA is disabled on each bus reset and it
has to be enabled after each bus reset when needed. We resort
to polling here because on early boot, we have no interrupts.

.. _`init_ohci1394_enable_physical_dma`:

init_ohci1394_enable_physical_dma
=================================

.. c:function:: void init_ohci1394_enable_physical_dma(struct ohci *ohci)

    Enable physical DMA for remote debugging This enables remote DMA access over IEEE1394 from every host for the low 4GB of address space. DMA accesses above 4GB are not available currently.

    :param struct ohci \*ohci:
        *undescribed*

.. _`init_ohci1394_reset_and_init_dma`:

init_ohci1394_reset_and_init_dma
================================

.. c:function:: void init_ohci1394_reset_and_init_dma(struct ohci *ohci)

    init controller and enable DMA This initializes the given controller and enables physical DMA engine in it.

    :param struct ohci \*ohci:
        *undescribed*

.. _`init_ohci1394_controller`:

init_ohci1394_controller
========================

.. c:function:: void init_ohci1394_controller(int num, int slot, int func)

    Map the registers of the controller and init DMA This maps the registers of the specified controller and initializes it

    :param int num:
        *undescribed*

    :param int slot:
        *undescribed*

    :param int func:
        *undescribed*

.. _`init_ohci1394_dma_on_all_controllers`:

init_ohci1394_dma_on_all_controllers
====================================

.. c:function:: void init_ohci1394_dma_on_all_controllers( void)

    scan for OHCI1394 controllers and init DMA on them Scans the whole PCI space for OHCI1394 controllers and inits DMA on them

    :param  void:
        no arguments

.. _`setup_ohci1394_dma`:

setup_ohci1394_dma
==================

.. c:function:: int setup_ohci1394_dma(char *opt)

    enables early OHCI1394 DMA initialization

    :param char \*opt:
        *undescribed*

.. This file was automatic generated / don't edit.

