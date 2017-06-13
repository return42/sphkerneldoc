.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/cgroup/rdma.c

.. _`uncharge_cg_locked`:

uncharge_cg_locked
==================

.. c:function:: void uncharge_cg_locked(struct rdma_cgroup *cg, struct rdmacg_device *device, enum rdmacg_resource_type index)

    uncharge resource for rdma cgroup

    :param struct rdma_cgroup \*cg:
        pointer to cg to uncharge and all parents in hierarchy

    :param struct rdmacg_device \*device:
        pointer to rdmacg device

    :param enum rdmacg_resource_type index:
        index of the resource to uncharge in cg (resource pool)

.. _`uncharge_cg_locked.description`:

Description
-----------

It also frees the resource pool which was created as part of
charging operation when there are no resources attached to
resource pool.

.. _`rdmacg_uncharge_hierarchy`:

rdmacg_uncharge_hierarchy
=========================

.. c:function:: void rdmacg_uncharge_hierarchy(struct rdma_cgroup *cg, struct rdmacg_device *device, struct rdma_cgroup *stop_cg, enum rdmacg_resource_type index)

    hierarchically uncharge rdma resource count

    :param struct rdma_cgroup \*cg:
        *undescribed*

    :param struct rdmacg_device \*device:
        pointer to rdmacg device

    :param struct rdma_cgroup \*stop_cg:
        while traversing hirerchy, when meet with stop_cg cgroup
        stop uncharging

    :param enum rdmacg_resource_type index:
        index of the resource to uncharge in cg in given resource pool

.. _`rdmacg_uncharge`:

rdmacg_uncharge
===============

.. c:function:: void rdmacg_uncharge(struct rdma_cgroup *cg, struct rdmacg_device *device, enum rdmacg_resource_type index)

    hierarchically uncharge rdma resource count

    :param struct rdma_cgroup \*cg:
        *undescribed*

    :param struct rdmacg_device \*device:
        pointer to rdmacg device

    :param enum rdmacg_resource_type index:
        index of the resource to uncharge in cgroup in given resource pool

.. _`rdmacg_try_charge`:

rdmacg_try_charge
=================

.. c:function:: int rdmacg_try_charge(struct rdma_cgroup **rdmacg, struct rdmacg_device *device, enum rdmacg_resource_type index)

    hierarchically try to charge the rdma resource

    :param struct rdma_cgroup \*\*rdmacg:
        pointer to rdma cgroup which will own this resource

    :param struct rdmacg_device \*device:
        pointer to rdmacg device

    :param enum rdmacg_resource_type index:
        index of the resource to charge in cgroup (resource pool)

.. _`rdmacg_try_charge.description`:

Description
-----------

This function follows charging resource in hierarchical way.
It will fail if the charge would cause the new value to exceed the
hierarchical limit.
Returns 0 if the charge succeded, otherwise -EAGAIN, -ENOMEM or -EINVAL.
Returns pointer to rdmacg for this resource when charging is successful.

Charger needs to account resources on two criteria.
(a) per cgroup & (b) per device resource usage.
Per cgroup resource usage ensures that tasks of cgroup doesn't cross
the configured limits. Per device provides granular configuration
in multi device usage. It allocates resource pool in the hierarchy
for each parent it come across for first resource. Later on resource
pool will be available. Therefore it will be much faster thereon
to charge/uncharge.

.. _`rdmacg_register_device`:

rdmacg_register_device
======================

.. c:function:: int rdmacg_register_device(struct rdmacg_device *device)

    register rdmacg device to rdma controller.

    :param struct rdmacg_device \*device:
        pointer to rdmacg device whose resources need to be accounted.

.. _`rdmacg_register_device.description`:

Description
-----------

If IB stack wish a device to participate in rdma cgroup resource
tracking, it must invoke this API to register with rdma cgroup before
any user space application can start using the RDMA resources.
Returns 0 on success or EINVAL when table length given is beyond
supported size.

.. _`rdmacg_unregister_device`:

rdmacg_unregister_device
========================

.. c:function:: void rdmacg_unregister_device(struct rdmacg_device *device)

    unregister rdmacg device from rdma controller.

    :param struct rdmacg_device \*device:
        pointer to rdmacg device which was previously registered with rdma
        controller using \ :c:func:`rdmacg_register_device`\ .

.. _`rdmacg_unregister_device.description`:

Description
-----------

IB stack must invoke this after all the resources of the IB device
are destroyed and after ensuring that no more resources will be created
when this API is invoked.

.. _`rdmacg_css_offline`:

rdmacg_css_offline
==================

.. c:function:: void rdmacg_css_offline(struct cgroup_subsys_state *css)

    cgroup css_offline callback

    :param struct cgroup_subsys_state \*css:
        css of interest

.. _`rdmacg_css_offline.description`:

Description
-----------

This function is called when \ ``css``\  is about to go away and responsible
for shooting down all rdmacg associated with \ ``css``\ . As part of that it
marks all the resource pool entries to max value, so that when resources are
uncharged, associated resource pool can be freed as well.

.. This file was automatic generated / don't edit.

