.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/tpm/tpm_ibmvtpm.c

.. _`tpm_ibmvtpm_recv`:

tpm_ibmvtpm_recv
================

.. c:function:: int tpm_ibmvtpm_recv(struct tpm_chip *chip, u8 *buf, size_t count)

    Receive data after send

    :param chip:
        tpm chip struct
    :type chip: struct tpm_chip \*

    :param buf:
        buffer to read
    :type buf: u8 \*

    :param count:
        size of buffer
    :type count: size_t

.. _`tpm_ibmvtpm_recv.return`:

Return
------

Number of bytes read

.. _`tpm_ibmvtpm_send`:

tpm_ibmvtpm_send
================

.. c:function:: int tpm_ibmvtpm_send(struct tpm_chip *chip, u8 *buf, size_t count)

    Send tpm request

    :param chip:
        tpm chip struct
    :type chip: struct tpm_chip \*

    :param buf:
        buffer contains data to send
    :type buf: u8 \*

    :param count:
        size of buffer
    :type count: size_t

.. _`tpm_ibmvtpm_send.return`:

Return
------

Number of bytes sent or < 0 on error.

.. _`ibmvtpm_crq_get_rtce_size`:

ibmvtpm_crq_get_rtce_size
=========================

.. c:function:: int ibmvtpm_crq_get_rtce_size(struct ibmvtpm_dev *ibmvtpm)

    Send a CRQ request to get rtce size

    :param ibmvtpm:
        vtpm device struct
    :type ibmvtpm: struct ibmvtpm_dev \*

.. _`ibmvtpm_crq_get_rtce_size.return`:

Return
------

0 on success.
Non-zero on failure.

.. _`ibmvtpm_crq_get_version`:

ibmvtpm_crq_get_version
=======================

.. c:function:: int ibmvtpm_crq_get_version(struct ibmvtpm_dev *ibmvtpm)

    Send a CRQ request to get vtpm version - Note that this is vtpm version and not tpm version

    :param ibmvtpm:
        vtpm device struct
    :type ibmvtpm: struct ibmvtpm_dev \*

.. _`ibmvtpm_crq_get_version.return`:

Return
------

0 on success.
Non-zero on failure.

.. _`ibmvtpm_crq_send_init_complete`:

ibmvtpm_crq_send_init_complete
==============================

.. c:function:: int ibmvtpm_crq_send_init_complete(struct ibmvtpm_dev *ibmvtpm)

    Send a CRQ initialize complete message

    :param ibmvtpm:
        vtpm device struct
    :type ibmvtpm: struct ibmvtpm_dev \*

.. _`ibmvtpm_crq_send_init_complete.return`:

Return
------

0 on success.
Non-zero on failure.

.. _`ibmvtpm_crq_send_init`:

ibmvtpm_crq_send_init
=====================

.. c:function:: int ibmvtpm_crq_send_init(struct ibmvtpm_dev *ibmvtpm)

    Send a CRQ initialize message

    :param ibmvtpm:
        vtpm device struct
    :type ibmvtpm: struct ibmvtpm_dev \*

.. _`ibmvtpm_crq_send_init.return`:

Return
------

0 on success.
Non-zero on failure.

.. _`tpm_ibmvtpm_remove`:

tpm_ibmvtpm_remove
==================

.. c:function:: int tpm_ibmvtpm_remove(struct vio_dev *vdev)

    ibm vtpm remove entry point

    :param vdev:
        vio device struct
    :type vdev: struct vio_dev \*

.. _`tpm_ibmvtpm_remove.return`:

Return
------

Always 0.

.. _`tpm_ibmvtpm_get_desired_dma`:

tpm_ibmvtpm_get_desired_dma
===========================

.. c:function:: unsigned long tpm_ibmvtpm_get_desired_dma(struct vio_dev *vdev)

    Get DMA size needed by this driver

    :param vdev:
        vio device struct
    :type vdev: struct vio_dev \*

.. _`tpm_ibmvtpm_get_desired_dma.return`:

Return
------

Number of bytes the driver needs to DMA map.

.. _`tpm_ibmvtpm_suspend`:

tpm_ibmvtpm_suspend
===================

.. c:function:: int tpm_ibmvtpm_suspend(struct device *dev)

    Suspend

    :param dev:
        device struct
    :type dev: struct device \*

.. _`tpm_ibmvtpm_suspend.return`:

Return
------

Always 0.

.. _`ibmvtpm_reset_crq`:

ibmvtpm_reset_crq
=================

.. c:function:: int ibmvtpm_reset_crq(struct ibmvtpm_dev *ibmvtpm)

    Reset CRQ

    :param ibmvtpm:
        ibm vtpm struct
    :type ibmvtpm: struct ibmvtpm_dev \*

.. _`ibmvtpm_reset_crq.return`:

Return
------

0 on success.
Non-zero on failure.

.. _`tpm_ibmvtpm_resume`:

tpm_ibmvtpm_resume
==================

.. c:function:: int tpm_ibmvtpm_resume(struct device *dev)

    Resume from suspend

    :param dev:
        device struct
    :type dev: struct device \*

.. _`tpm_ibmvtpm_resume.return`:

Return
------

Always 0.

.. _`ibmvtpm_crq_get_next`:

ibmvtpm_crq_get_next
====================

.. c:function:: struct ibmvtpm_crq *ibmvtpm_crq_get_next(struct ibmvtpm_dev *ibmvtpm)

    Get next responded crq

    :param ibmvtpm:
        vtpm device struct
    :type ibmvtpm: struct ibmvtpm_dev \*

.. _`ibmvtpm_crq_get_next.return`:

Return
------

vtpm crq pointer or NULL.

.. _`ibmvtpm_crq_process`:

ibmvtpm_crq_process
===================

.. c:function:: void ibmvtpm_crq_process(struct ibmvtpm_crq *crq, struct ibmvtpm_dev *ibmvtpm)

    Process responded crq

    :param crq:
        crq to be processed
    :type crq: struct ibmvtpm_crq \*

    :param ibmvtpm:
        vtpm device struct
    :type ibmvtpm: struct ibmvtpm_dev \*

.. _`ibmvtpm_interrupt`:

ibmvtpm_interrupt
=================

.. c:function:: irqreturn_t ibmvtpm_interrupt(int irq, void *vtpm_instance)

    Interrupt handler

    :param irq:
        irq number to handle
    :type irq: int

    :param vtpm_instance:
        vtpm that received interrupt
    :type vtpm_instance: void \*

.. _`ibmvtpm_interrupt.return`:

Return
------

IRQ_HANDLED

.. _`tpm_ibmvtpm_probe`:

tpm_ibmvtpm_probe
=================

.. c:function:: int tpm_ibmvtpm_probe(struct vio_dev *vio_dev, const struct vio_device_id *id)

    ibm vtpm initialize entry point

    :param vio_dev:
        vio device struct
    :type vio_dev: struct vio_dev \*

    :param id:
        vio device id struct
    :type id: const struct vio_device_id \*

.. _`tpm_ibmvtpm_probe.return`:

Return
------

0 on success.
Non-zero on failure.

.. _`ibmvtpm_module_init`:

ibmvtpm_module_init
===================

.. c:function:: int ibmvtpm_module_init( void)

    Initialize ibm vtpm module.

    :param void:
        no arguments
    :type void: 

.. _`ibmvtpm_module_init.return`:

Return
------


0 on success.
Non-zero on failure.

.. _`ibmvtpm_module_exit`:

ibmvtpm_module_exit
===================

.. c:function:: void __exit ibmvtpm_module_exit( void)

    Tear down ibm vtpm module.

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

