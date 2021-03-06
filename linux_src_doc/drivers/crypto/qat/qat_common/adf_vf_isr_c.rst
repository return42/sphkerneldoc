.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/qat/qat_common/adf_vf_isr.c

.. _`adf_vf_isr_resource_free`:

adf_vf_isr_resource_free
========================

.. c:function:: void adf_vf_isr_resource_free(struct adf_accel_dev *accel_dev)

    Free IRQ for acceleration device

    :param accel_dev:
        Pointer to acceleration device.
    :type accel_dev: struct adf_accel_dev \*

.. _`adf_vf_isr_resource_free.description`:

Description
-----------

Function frees interrupts for acceleration device virtual function.

.. _`adf_vf_isr_resource_alloc`:

adf_vf_isr_resource_alloc
=========================

.. c:function:: int adf_vf_isr_resource_alloc(struct adf_accel_dev *accel_dev)

    Allocate IRQ for acceleration device

    :param accel_dev:
        Pointer to acceleration device.
    :type accel_dev: struct adf_accel_dev \*

.. _`adf_vf_isr_resource_alloc.description`:

Description
-----------

Function allocates interrupts for acceleration device virtual function.

.. _`adf_vf_isr_resource_alloc.return`:

Return
------

0 on success, error code otherwise.

.. This file was automatic generated / don't edit.

