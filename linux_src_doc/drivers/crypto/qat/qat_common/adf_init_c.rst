.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/qat/qat_common/adf_init.c

.. _`adf_dev_init`:

adf_dev_init
============

.. c:function:: int adf_dev_init(struct adf_accel_dev *accel_dev)

    Init data structures and services for the given accel device

    :param struct adf_accel_dev \*accel_dev:
        Pointer to acceleration device.

.. _`adf_dev_init.description`:

Description
-----------

Initialize the ring data structures and the admin comms and arbitration
services.

.. _`adf_dev_init.return`:

Return
------

0 on success, error code otherwise.

.. _`adf_dev_start`:

adf_dev_start
=============

.. c:function:: int adf_dev_start(struct adf_accel_dev *accel_dev)

    Start acceleration service for the given accel device

    :param struct adf_accel_dev \*accel_dev:
        Pointer to acceleration device.

.. _`adf_dev_start.description`:

Description
-----------

Function notifies all the registered services that the acceleration device
is ready to be used.
To be used by QAT device specific drivers.

.. _`adf_dev_start.return`:

Return
------

0 on success, error code otherwise.

.. _`adf_dev_stop`:

adf_dev_stop
============

.. c:function:: void adf_dev_stop(struct adf_accel_dev *accel_dev)

    Stop acceleration service for the given accel device

    :param struct adf_accel_dev \*accel_dev:
        Pointer to acceleration device.

.. _`adf_dev_stop.description`:

Description
-----------

Function notifies all the registered services that the acceleration device
is shuting down.
To be used by QAT device specific drivers.

.. _`adf_dev_stop.return`:

Return
------

void

.. _`adf_dev_shutdown`:

adf_dev_shutdown
================

.. c:function:: void adf_dev_shutdown(struct adf_accel_dev *accel_dev)

    shutdown acceleration services and data strucutures

    :param struct adf_accel_dev \*accel_dev:
        Pointer to acceleration device

.. _`adf_dev_shutdown.description`:

Description
-----------

Cleanup the ring data structures and the admin comms and arbitration
services.

.. This file was automatic generated / don't edit.

