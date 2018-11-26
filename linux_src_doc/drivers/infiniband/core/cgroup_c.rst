.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/cgroup.c

.. _`ib_device_register_rdmacg`:

ib_device_register_rdmacg
=========================

.. c:function:: int ib_device_register_rdmacg(struct ib_device *device)

    register with rdma cgroup.

    :param device:
        device to register to participate in resource
        accounting by rdma cgroup.
    :type device: struct ib_device \*

.. _`ib_device_register_rdmacg.description`:

Description
-----------

Register with the rdma cgroup. Should be called before
exposing rdma device to user space applications to avoid
resource accounting leak.
Returns 0 on success or otherwise failure code.

.. _`ib_device_unregister_rdmacg`:

ib_device_unregister_rdmacg
===========================

.. c:function:: void ib_device_unregister_rdmacg(struct ib_device *device)

    unregister with rdma cgroup.

    :param device:
        device to unregister.
    :type device: struct ib_device \*

.. _`ib_device_unregister_rdmacg.description`:

Description
-----------

Unregister with the rdma cgroup. Should be called after
all the resources are deallocated, and after a stage when any
other resource allocation by user application cannot be done
for this device to avoid any leak in accounting.

.. This file was automatic generated / don't edit.

