.. -*- coding: utf-8; mode: rst -*-

==========
tpm-chip.c
==========


.. _`tpm_dev_release`:

tpm_dev_release
===============

.. c:function:: void tpm_dev_release (struct device *dev)

    free chip memory and the device number

    :param struct device \*dev:
        the character device for the TPM chip



.. _`tpm_dev_release.description`:

Description
-----------

This is used as the release function for the character device.



.. _`tpmm_chip_alloc`:

tpmm_chip_alloc
===============

.. c:function:: struct tpm_chip *tpmm_chip_alloc (struct device *dev, const struct tpm_class_ops *ops)

    allocate a new struct tpm_chip instance

    :param struct device \*dev:
        device to which the chip is associated

    :param const struct tpm_class_ops \*ops:
        struct tpm_class_ops instance



.. _`tpmm_chip_alloc.description`:

Description
-----------

Allocates a new struct tpm_chip instance and assigns a free
device number for it. Caller does not have to worry about
freeing the allocated resources. When the devices is removed
devres calls :c:func:`tpmm_chip_remove` to do the job.

