.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/pseries/suspend.c

.. _`pseries_suspend_begin`:

pseries_suspend_begin
=====================

.. c:function:: int pseries_suspend_begin(suspend_state_t state)

    First phase of hibernation

    :param suspend_state_t state:
        *undescribed*

.. _`pseries_suspend_begin.description`:

Description
-----------

Check to ensure we are in a valid state to hibernate

.. _`pseries_suspend_begin.return-value`:

Return value
------------

0 on success / other on failure

.. _`pseries_suspend_cpu`:

pseries_suspend_cpu
===================

.. c:function:: int pseries_suspend_cpu( void)

    Suspend a single CPU

    :param  void:
        no arguments

.. _`pseries_suspend_cpu.description`:

Description
-----------

Makes the H_JOIN call to suspend the CPU

.. _`pseries_suspend_enable_irqs`:

pseries_suspend_enable_irqs
===========================

.. c:function:: void pseries_suspend_enable_irqs( void)

    :param  void:
        no arguments

.. _`pseries_suspend_enable_irqs.description`:

Description
-----------

Post suspend configuration updates

.. _`pseries_suspend_enter`:

pseries_suspend_enter
=====================

.. c:function:: int pseries_suspend_enter(suspend_state_t state)

    Final phase of hibernation

    :param suspend_state_t state:
        *undescribed*

.. _`pseries_suspend_enter.return-value`:

Return value
------------

0 on success / other on failure

.. _`pseries_prepare_late`:

pseries_prepare_late
====================

.. c:function:: int pseries_prepare_late( void)

    Prepare to suspend all other CPUs

    :param  void:
        no arguments

.. _`pseries_prepare_late.return-value`:

Return value
------------

0 on success / other on failure

.. _`store_hibernate`:

store_hibernate
===============

.. c:function:: ssize_t store_hibernate(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    Initiate partition hibernation

    :param struct device \*dev:
        subsys root device

    :param struct device_attribute \*attr:
        device attribute struct

    :param const char \*buf:
        buffer

    :param size_t count:
        buffer size

.. _`store_hibernate.description`:

Description
-----------

Write the stream ID received from the HMC to this file
to trigger hibernating the partition

.. _`store_hibernate.return-value`:

Return value
------------

number of bytes printed to buffer / other on failure

.. _`show_hibernate`:

show_hibernate
==============

.. c:function:: ssize_t show_hibernate(struct device *dev, struct device_attribute *attr, char *buf)

    Report device tree update responsibilty

    :param struct device \*dev:
        subsys root device

    :param struct device_attribute \*attr:
        device attribute struct

    :param char \*buf:
        buffer

.. _`show_hibernate.description`:

Description
-----------

Report whether a device tree update is performed by the kernel after a
resume, or if drmgr must coordinate the update from user space.

.. _`show_hibernate.return-value`:

Return value
------------

0 if drmgr is to initiate update, and 1 otherwise

.. _`pseries_suspend_sysfs_register`:

pseries_suspend_sysfs_register
==============================

.. c:function:: int pseries_suspend_sysfs_register(struct device *dev)

    Register with sysfs

    :param struct device \*dev:
        *undescribed*

.. _`pseries_suspend_sysfs_register.return-value`:

Return value
------------

0 on success / other on failure

.. _`pseries_suspend_init`:

pseries_suspend_init
====================

.. c:function:: int pseries_suspend_init( void)

    initcall for pSeries suspend

    :param  void:
        no arguments

.. _`pseries_suspend_init.return-value`:

Return value
------------

0 on success / other on failure

.. This file was automatic generated / don't edit.

