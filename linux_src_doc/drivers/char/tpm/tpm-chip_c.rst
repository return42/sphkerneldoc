.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/tpm/tpm-chip.c

.. _`tpm_try_get_ops`:

tpm_try_get_ops
===============

.. c:function:: int tpm_try_get_ops(struct tpm_chip *chip)

    Get a ref to the tpm_chip

    :param struct tpm_chip \*chip:
        Chip to ref

.. _`tpm_try_get_ops.description`:

Description
-----------

The caller must already have some kind of locking to ensure that chip is
valid. This function will lock the chip so that the ops member can be
accessed safely. The locking prevents tpm_chip_unregister from
completing, so it should not be held for long periods.

Returns -ERRNO if the chip could not be got.

.. _`tpm_put_ops`:

tpm_put_ops
===========

.. c:function:: void tpm_put_ops(struct tpm_chip *chip)

    Release a ref to the tpm_chip

    :param struct tpm_chip \*chip:
        Chip to put

.. _`tpm_put_ops.description`:

Description
-----------

This is the opposite pair to \ :c:func:`tpm_try_get_ops`\ . After this returns chip may
be kfree'd.

.. _`tpm_chip_find_get`:

tpm_chip_find_get
=================

.. c:function:: struct tpm_chip *tpm_chip_find_get(int chip_num)

    return tpm_chip for a given chip number

    :param int chip_num:
        id to find

.. _`tpm_chip_find_get.description`:

Description
-----------

The return'd chip has been tpm_try_get_ops'd and must be released via
tpm_put_ops

.. _`tpm_dev_release`:

tpm_dev_release
===============

.. c:function:: void tpm_dev_release(struct device *dev)

    free chip memory and the device number

    :param struct device \*dev:
        the character device for the TPM chip

.. _`tpm_dev_release.description`:

Description
-----------

This is used as the release function for the character device.

.. _`tpm_chip_alloc`:

tpm_chip_alloc
==============

.. c:function:: struct tpm_chip *tpm_chip_alloc(struct device *dev, const struct tpm_class_ops *ops)

    allocate a new struct tpm_chip instance

    :param struct device \*dev:
        *undescribed*

    :param const struct tpm_class_ops \*ops:
        struct tpm_class_ops instance

.. _`tpm_chip_alloc.description`:

Description
-----------

Allocates a new struct tpm_chip instance and assigns a free
device number for it. Must be paired with put_device(&chip->dev).

.. _`tpmm_chip_alloc`:

tpmm_chip_alloc
===============

.. c:function:: struct tpm_chip *tpmm_chip_alloc(struct device *pdev, const struct tpm_class_ops *ops)

    allocate a new struct tpm_chip instance

    :param struct device \*pdev:
        parent device to which the chip is associated

    :param const struct tpm_class_ops \*ops:
        struct tpm_class_ops instance

.. _`tpmm_chip_alloc.description`:

Description
-----------

Same as tpm_chip_alloc except devm is used to do the put_device

.. This file was automatic generated / don't edit.

