.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/tpm/tpm_ibmvtpm.c

.. _`ibmvtpm_send_crq`:

ibmvtpm_send_crq
================

.. c:function:: int ibmvtpm_send_crq(struct vio_dev *vdev, u64 w1, u64 w2)

    Send a CRQ request

    :param struct vio_dev \*vdev:
        vio device struct

    :param u64 w1:
        first word

    :param u64 w2:
        second word

.. _`ibmvtpm_send_crq.return-value`:

Return value
------------

0 -Sucess
Non-zero - Failure

.. _`ibmvtpm_get_data`:

ibmvtpm_get_data
================

.. c:function:: struct ibmvtpm_dev *ibmvtpm_get_data(const struct device *dev)

    Retrieve ibm vtpm data

    :param const struct device \*dev:
        device struct

.. _`ibmvtpm_get_data.return-value`:

Return value
------------

vtpm device struct

.. _`tpm_ibmvtpm_recv`:

tpm_ibmvtpm_recv
================

.. c:function:: int tpm_ibmvtpm_recv(struct tpm_chip *chip, u8 *buf, size_t count)

    Receive data after send

    :param struct tpm_chip \*chip:
        tpm chip struct

    :param u8 \*buf:
        buffer to read

    :param size_t count:
        *undescribed*

.. _`tpm_ibmvtpm_recv.count`:

count
-----

size of buffer

.. _`tpm_ibmvtpm_recv.return-value`:

Return value
------------

Number of bytes read

.. _`tpm_ibmvtpm_send`:

tpm_ibmvtpm_send
================

.. c:function:: int tpm_ibmvtpm_send(struct tpm_chip *chip, u8 *buf, size_t count)

    Send tpm request

    :param struct tpm_chip \*chip:
        tpm chip struct

    :param u8 \*buf:
        buffer contains data to send

    :param size_t count:
        *undescribed*

.. _`tpm_ibmvtpm_send.count`:

count
-----

size of buffer

.. _`tpm_ibmvtpm_send.return-value`:

Return value
------------

Number of bytes sent

.. _`ibmvtpm_crq_get_rtce_size`:

ibmvtpm_crq_get_rtce_size
=========================

.. c:function:: int ibmvtpm_crq_get_rtce_size(struct ibmvtpm_dev *ibmvtpm)

    Send a CRQ request to get rtce size

    :param struct ibmvtpm_dev \*ibmvtpm:
        vtpm device struct

.. _`ibmvtpm_crq_get_rtce_size.return-value`:

Return value
------------

0 - Success
Non-zero - Failure

.. _`ibmvtpm_crq_get_version`:

ibmvtpm_crq_get_version
=======================

.. c:function:: int ibmvtpm_crq_get_version(struct ibmvtpm_dev *ibmvtpm)

    Send a CRQ request to get vtpm version - Note that this is vtpm version and not tpm version

    :param struct ibmvtpm_dev \*ibmvtpm:
        vtpm device struct

.. _`ibmvtpm_crq_get_version.return-value`:

Return value
------------

0 - Success
Non-zero - Failure

.. _`ibmvtpm_crq_send_init_complete`:

ibmvtpm_crq_send_init_complete
==============================

.. c:function:: int ibmvtpm_crq_send_init_complete(struct ibmvtpm_dev *ibmvtpm)

    Send a CRQ initialize complete message

    :param struct ibmvtpm_dev \*ibmvtpm:
        vtpm device struct

.. _`ibmvtpm_crq_send_init_complete.return-value`:

Return value
------------

0 - Success
Non-zero - Failure

.. _`ibmvtpm_crq_send_init`:

ibmvtpm_crq_send_init
=====================

.. c:function:: int ibmvtpm_crq_send_init(struct ibmvtpm_dev *ibmvtpm)

    Send a CRQ initialize message

    :param struct ibmvtpm_dev \*ibmvtpm:
        vtpm device struct

.. _`ibmvtpm_crq_send_init.return-value`:

Return value
------------

0 - Success
Non-zero - Failure

.. _`tpm_ibmvtpm_remove`:

tpm_ibmvtpm_remove
==================

.. c:function:: int tpm_ibmvtpm_remove(struct vio_dev *vdev)

    ibm vtpm remove entry point

    :param struct vio_dev \*vdev:
        vio device struct

.. _`tpm_ibmvtpm_remove.return-value`:

Return value
------------

0

.. _`tpm_ibmvtpm_get_desired_dma`:

tpm_ibmvtpm_get_desired_dma
===========================

.. c:function:: unsigned long tpm_ibmvtpm_get_desired_dma(struct vio_dev *vdev)

    Get DMA size needed by this driver

    :param struct vio_dev \*vdev:
        vio device struct

.. _`tpm_ibmvtpm_get_desired_dma.return-value`:

Return value
------------

Number of bytes the driver needs to DMA map

.. _`tpm_ibmvtpm_suspend`:

tpm_ibmvtpm_suspend
===================

.. c:function:: int tpm_ibmvtpm_suspend(struct device *dev)

    Suspend

    :param struct device \*dev:
        device struct

.. _`tpm_ibmvtpm_suspend.return-value`:

Return value
------------

0

.. _`ibmvtpm_reset_crq`:

ibmvtpm_reset_crq
=================

.. c:function:: int ibmvtpm_reset_crq(struct ibmvtpm_dev *ibmvtpm)

    Reset CRQ

    :param struct ibmvtpm_dev \*ibmvtpm:
        ibm vtpm struct

.. _`ibmvtpm_reset_crq.return-value`:

Return value
------------

0 - Success
Non-zero - Failure

.. _`tpm_ibmvtpm_resume`:

tpm_ibmvtpm_resume
==================

.. c:function:: int tpm_ibmvtpm_resume(struct device *dev)

    Resume from suspend

    :param struct device \*dev:
        device struct

.. _`tpm_ibmvtpm_resume.return-value`:

Return value
------------

0

.. _`ibmvtpm_crq_get_next`:

ibmvtpm_crq_get_next
====================

.. c:function:: struct ibmvtpm_crq *ibmvtpm_crq_get_next(struct ibmvtpm_dev *ibmvtpm)

    Get next responded crq \ ``ibmvtpm``\      vtpm device struct

    :param struct ibmvtpm_dev \*ibmvtpm:
        *undescribed*

.. _`ibmvtpm_crq_get_next.return-value`:

Return value
------------

vtpm crq pointer

.. _`ibmvtpm_crq_process`:

ibmvtpm_crq_process
===================

.. c:function:: void ibmvtpm_crq_process(struct ibmvtpm_crq *crq, struct ibmvtpm_dev *ibmvtpm)

    Process responded crq \ ``crq``\          crq to be processed \ ``ibmvtpm``\      vtpm device struct

    :param struct ibmvtpm_crq \*crq:
        *undescribed*

    :param struct ibmvtpm_dev \*ibmvtpm:
        *undescribed*

.. _`ibmvtpm_crq_process.return-value`:

Return value
------------

Nothing

.. _`ibmvtpm_interrupt`:

ibmvtpm_interrupt
=================

.. c:function:: irqreturn_t ibmvtpm_interrupt(int irq, void *vtpm_instance)

    Interrupt handler

    :param int irq:
        irq number to handle

    :param void \*vtpm_instance:
        vtpm that received interrupt

.. _`ibmvtpm_interrupt.return`:

Return
------

IRQ_HANDLED

.. _`tpm_ibmvtpm_probe`:

tpm_ibmvtpm_probe
=================

.. c:function:: int tpm_ibmvtpm_probe(struct vio_dev *vio_dev, const struct vio_device_id *id)

    ibm vtpm initialize entry point

    :param struct vio_dev \*vio_dev:
        vio device struct

    :param const struct vio_device_id \*id:
        vio device id struct

.. _`tpm_ibmvtpm_probe.return-value`:

Return value
------------

0 - Success
Non-zero - Failure

.. _`ibmvtpm_module_init`:

ibmvtpm_module_init
===================

.. c:function:: int ibmvtpm_module_init( void)

    Initialize ibm vtpm module

    :param  void:
        no arguments

.. _`ibmvtpm_module_init.return-value`:

Return value
------------

0 -Success
Non-zero - Failure

.. _`ibmvtpm_module_exit`:

ibmvtpm_module_exit
===================

.. c:function:: void __exit ibmvtpm_module_exit( void)

    Teardown ibm vtpm module

    :param  void:
        no arguments

.. _`ibmvtpm_module_exit.return-value`:

Return value
------------

Nothing

.. This file was automatic generated / don't edit.

