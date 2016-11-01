.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/kernel/cpuidle.c

.. _`arm_cpuidle_simple_enter`:

arm_cpuidle_simple_enter
========================

.. c:function:: int arm_cpuidle_simple_enter(struct cpuidle_device *dev, struct cpuidle_driver *drv, int index)

    a wrapper to \ :c:func:`cpu_do_idle`\ 

    :param struct cpuidle_device \*dev:
        not used

    :param struct cpuidle_driver \*drv:
        not used

    :param int index:
        not used

.. _`arm_cpuidle_simple_enter.description`:

Description
-----------

A trivial wrapper to allow the cpu_do_idle function to be assigned as a
cpuidle callback by matching the function signature.

Returns the index passed as parameter

.. _`arm_cpuidle_suspend`:

arm_cpuidle_suspend
===================

.. c:function:: int arm_cpuidle_suspend(int index)

    function to enter low power idle states

    :param int index:
        an integer used as an identifier for the low level PM callbacks

.. _`arm_cpuidle_suspend.description`:

Description
-----------

This function calls the underlying arch specific low level PM code as
registered at the init time.

Returns the result of the suspend callback.

.. _`arm_cpuidle_get_ops`:

arm_cpuidle_get_ops
===================

.. c:function:: const struct cpuidle_ops *arm_cpuidle_get_ops(const char *method)

    find a registered cpuidle_ops by name

    :param const char \*method:
        the method name

.. _`arm_cpuidle_get_ops.description`:

Description
-----------

Search in the \__cpuidle_method_of_table array the cpuidle ops matching the
method name.

Returns a struct cpuidle_ops pointer, NULL if not found.

.. _`arm_cpuidle_read_ops`:

arm_cpuidle_read_ops
====================

.. c:function:: int arm_cpuidle_read_ops(struct device_node *dn, int cpu)

    Initialize the cpuidle ops with the device tree

    :param struct device_node \*dn:
        a pointer to a struct device node corresponding to a cpu node

    :param int cpu:
        the cpu identifier

.. _`arm_cpuidle_read_ops.description`:

Description
-----------

Get the method name defined in the 'enable-method' property, retrieve the
associated cpuidle_ops and do a struct copy. This copy is needed because all
cpuidle_ops are tagged \__initconst and will be unloaded after the init
process.

Return 0 on sucess, -ENOENT if no 'enable-method' is defined, -EOPNOTSUPP if
no cpuidle_ops is registered for the 'enable-method', or if either init or
suspend callback isn't defined.

.. _`arm_cpuidle_init`:

arm_cpuidle_init
================

.. c:function:: int arm_cpuidle_init(int cpu)

    Initialize cpuidle_ops for a specific cpu

    :param int cpu:
        the cpu to be initialized

.. _`arm_cpuidle_init.description`:

Description
-----------

Initialize the cpuidle ops with the device for the cpu and then call
the cpu's idle initialization callback. This may fail if the underlying HW
is not operational.

.. _`arm_cpuidle_init.return`:

Return
------

0 on success,
-ENODEV if it fails to find the cpu node in the device tree,
-EOPNOTSUPP if it does not find a registered and valid cpuidle_ops for
this cpu,
-ENOENT if it fails to find an 'enable-method' property,
-ENXIO if the HW reports a failure or a misconfiguration,
-ENOMEM if the HW report an memory allocation failure

.. This file was automatic generated / don't edit.

