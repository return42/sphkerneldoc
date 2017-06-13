.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/sysdev/axonram.c

.. _`axon_ram_irq_handler`:

axon_ram_irq_handler
====================

.. c:function:: irqreturn_t axon_ram_irq_handler(int irq, void *dev)

    interrupt handler for Axon RAM ECC

    :param int irq:
        interrupt ID

    :param void \*dev:
        pointer to of_device

.. _`axon_ram_make_request`:

axon_ram_make_request
=====================

.. c:function:: blk_qc_t axon_ram_make_request(struct request_queue *queue, struct bio *bio)

    make_request() method for block device

    :param struct request_queue \*queue:
        see \ :c:func:`blk_queue_make_request`\ 

    :param struct bio \*bio:
        *undescribed*

.. _`axon_ram_probe`:

axon_ram_probe
==============

.. c:function:: int axon_ram_probe(struct platform_device *device)

    probe() method for platform driver

    :param struct platform_device \*device:
        see platform_driver method

.. _`axon_ram_remove`:

axon_ram_remove
===============

.. c:function:: int axon_ram_remove(struct platform_device *device)

    remove() method for platform driver

    :param struct platform_device \*device:
        see of_platform_driver method

.. _`axon_ram_init`:

axon_ram_init
=============

.. c:function:: int axon_ram_init( void)

    :param  void:
        no arguments

.. _`axon_ram_exit`:

axon_ram_exit
=============

.. c:function:: void __exit axon_ram_exit( void)

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

