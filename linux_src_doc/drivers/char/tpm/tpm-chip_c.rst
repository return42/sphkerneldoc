.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/tpm/tpm-chip.c

.. _`tpm_try_get_ops`:

tpm_try_get_ops
===============

.. c:function:: int tpm_try_get_ops(struct tpm_chip *chip)

    Get a ref to the tpm_chip

    :param chip:
        Chip to ref
    :type chip: struct tpm_chip \*

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

    :param chip:
        Chip to put
    :type chip: struct tpm_chip \*

.. _`tpm_put_ops.description`:

Description
-----------

This is the opposite pair to \ :c:func:`tpm_try_get_ops`\ . After this returns chip may
be kfree'd.

.. _`tpm_default_chip`:

tpm_default_chip
================

.. c:function:: struct tpm_chip *tpm_default_chip( void)

    find a TPM chip and get a reference to it

    :param void:
        no arguments
    :type void: 

.. _`tpm_find_get_ops`:

tpm_find_get_ops
================

.. c:function:: struct tpm_chip *tpm_find_get_ops(struct tpm_chip *chip)

    find and reserve a TPM chip

    :param chip:
        a \ :c:type:`struct tpm_chip <tpm_chip>`\  instance, \ ``NULL``\  for the default chip
    :type chip: struct tpm_chip \*

.. _`tpm_find_get_ops.description`:

Description
-----------

Finds a TPM chip and reserves its class device and operations. The chip must
be released with \ :c:func:`tpm_put_ops`\  after use.
This function is for internal use only. It supports existing TPM callers
by accepting NULL, but those callers should be converted to pass in a chip
directly.

.. _`tpm_find_get_ops.return`:

Return
------

A reserved \ :c:type:`struct tpm_chip <tpm_chip>`\  instance.
\ ``NULL``\  if a chip is not found.
\ ``NULL``\  if the chip is not available.

.. _`tpm_dev_release`:

tpm_dev_release
===============

.. c:function:: void tpm_dev_release(struct device *dev)

    free chip memory and the device number

    :param dev:
        the character device for the TPM chip
    :type dev: struct device \*

.. _`tpm_dev_release.description`:

Description
-----------

This is used as the release function for the character device.

.. _`tpm_class_shutdown`:

tpm_class_shutdown
==================

.. c:function:: int tpm_class_shutdown(struct device *dev)

    prepare the TPM device for loss of power.

    :param dev:
        device to which the chip is associated.
    :type dev: struct device \*

.. _`tpm_class_shutdown.description`:

Description
-----------

Issues a TPM2_Shutdown command prior to loss of power, as required by the
TPM 2.0 spec.
Then, calls bus- and device- specific shutdown code.

.. _`tpm_class_shutdown.xxx`:

XXX
---

This codepath relies on the fact that sysfs is not enabled for

.. _`tpm_class_shutdown.tpm2`:

TPM2
----

sysfs uses an implicit lock on chip->ops, so this could race if TPM2
has sysfs support enabled before TPM sysfs's implicit locking is fixed.

.. _`tpm_chip_alloc`:

tpm_chip_alloc
==============

.. c:function:: struct tpm_chip *tpm_chip_alloc(struct device *pdev, const struct tpm_class_ops *ops)

    allocate a new struct tpm_chip instance

    :param pdev:
        device to which the chip is associated
        At this point pdev mst be initialized, but does not have to
        be registered
    :type pdev: struct device \*

    :param ops:
        struct tpm_class_ops instance
    :type ops: const struct tpm_class_ops \*

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

    :param pdev:
        parent device to which the chip is associated
    :type pdev: struct device \*

    :param ops:
        struct tpm_class_ops instance
    :type ops: const struct tpm_class_ops \*

.. _`tpmm_chip_alloc.description`:

Description
-----------

Same as tpm_chip_alloc except devm is used to do the put_device

.. This file was automatic generated / don't edit.

