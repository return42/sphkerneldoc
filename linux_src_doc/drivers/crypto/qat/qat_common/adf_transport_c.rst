.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/qat/qat_common/adf_transport.c

.. _`adf_init_etr_data`:

adf_init_etr_data
=================

.. c:function:: int adf_init_etr_data(struct adf_accel_dev *accel_dev)

    Initialize transport rings for acceleration device

    :param accel_dev:
        Pointer to acceleration device.
    :type accel_dev: struct adf_accel_dev \*

.. _`adf_init_etr_data.description`:

Description
-----------

Function is the initializes the communications channels (rings) to the
acceleration device accel_dev.
To be used by QAT device specific drivers.

.. _`adf_init_etr_data.return`:

Return
------

0 on success, error code otherwise.

.. _`adf_cleanup_etr_data`:

adf_cleanup_etr_data
====================

.. c:function:: void adf_cleanup_etr_data(struct adf_accel_dev *accel_dev)

    Clear transport rings for acceleration device

    :param accel_dev:
        Pointer to acceleration device.
    :type accel_dev: struct adf_accel_dev \*

.. _`adf_cleanup_etr_data.description`:

Description
-----------

Function is the clears the communications channels (rings) of the
acceleration device accel_dev.
To be used by QAT device specific drivers.

.. _`adf_cleanup_etr_data.return`:

Return
------

void

.. This file was automatic generated / don't edit.

