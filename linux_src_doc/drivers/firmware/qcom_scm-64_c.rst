.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firmware/qcom_scm-64.c

.. _`qcom_scm_desc`:

struct qcom_scm_desc
====================

.. c:type:: struct qcom_scm_desc


.. _`qcom_scm_desc.definition`:

Definition
----------

.. code-block:: c

    struct qcom_scm_desc {
        u32 arginfo;
        u64 args;
    }

.. _`qcom_scm_desc.members`:

Members
-------

arginfo
    Metadata describing the arguments in args[]

args
    The array of arguments for the secure syscall

.. _`qcom_scm_call`:

qcom_scm_call
=============

.. c:function:: int qcom_scm_call(struct device *dev, u32 svc_id, u32 cmd_id, const struct qcom_scm_desc *desc, struct arm_smccc_res *res)

    Invoke a syscall in the secure world

    :param struct device \*dev:
        device

    :param u32 svc_id:
        service identifier

    :param u32 cmd_id:
        command identifier

    :param const struct qcom_scm_desc \*desc:
        Descriptor structure containing arguments and return values

    :param struct arm_smccc_res \*res:
        *undescribed*

.. _`qcom_scm_call.description`:

Description
-----------

Sends a command to the SCM and waits for the command to finish processing.
This should \*only\* be called in pre-emptible context.

.. _`__qcom_scm_set_cold_boot_addr`:

__qcom_scm_set_cold_boot_addr
=============================

.. c:function:: int __qcom_scm_set_cold_boot_addr(void *entry, const cpumask_t *cpus)

    Set the cold boot address for cpus

    :param void \*entry:
        Entry point function for the cpus

    :param const cpumask_t \*cpus:
        The cpumask of cpus that will use the entry point

.. _`__qcom_scm_set_cold_boot_addr.description`:

Description
-----------

Set the cold boot address of the cpus. Any cpu outside the supported
range would be removed from the cpu present mask.

.. _`__qcom_scm_set_warm_boot_addr`:

__qcom_scm_set_warm_boot_addr
=============================

.. c:function:: int __qcom_scm_set_warm_boot_addr(struct device *dev, void *entry, const cpumask_t *cpus)

    Set the warm boot address for cpus

    :param struct device \*dev:
        Device pointer

    :param void \*entry:
        Entry point function for the cpus

    :param const cpumask_t \*cpus:
        The cpumask of cpus that will use the entry point

.. _`__qcom_scm_set_warm_boot_addr.description`:

Description
-----------

Set the Linux entry point for the SCM to transfer control to when coming
out of a power down. CPU power down may be executed on cpuidle or hotplug.

.. _`__qcom_scm_cpu_power_down`:

__qcom_scm_cpu_power_down
=========================

.. c:function:: void __qcom_scm_cpu_power_down(u32 flags)

    Power down the cpu \ ``flags``\  - Flags to flush cache

    :param u32 flags:
        *undescribed*

.. _`__qcom_scm_cpu_power_down.description`:

Description
-----------

This is an end point to power down cpu. If there was a pending interrupt,
the control would return from this function, otherwise, the cpu jumps to the
warm boot entry point set for this cpu upon reset.

.. This file was automatic generated / don't edit.

