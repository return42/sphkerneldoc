.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/avr32/kernel/ocd.c

.. _`ocd_enable`:

ocd_enable
==========

.. c:function:: void ocd_enable(struct task_struct *child)

    enable on-chip debugging

    :param struct task_struct \*child:
        task to be debugged

.. _`ocd_enable.description`:

Description
-----------

If \ ``child``\  is non-NULL, \ :c:func:`ocd_enable`\  first checks if debugging has
already been enabled for \ ``child``\ , and if it has, does nothing.

If \ ``child``\  is NULL (e.g. when debugging the kernel), or debugging
has not already been enabled for it, \ :c:func:`ocd_enable`\  increments the
reference count and enables the debugging hardware.

.. _`ocd_disable`:

ocd_disable
===========

.. c:function:: void ocd_disable(struct task_struct *child)

    disable on-chip debugging

    :param struct task_struct \*child:
        task that was being debugged, but isn't anymore

.. _`ocd_disable.description`:

Description
-----------

If \ ``child``\  is non-NULL, \ :c:func:`ocd_disable`\  checks if debugging is enabled
for \ ``child``\ , and if it isn't, does nothing.

If \ ``child``\  is NULL (e.g. when debugging the kernel), or debugging is
enabled, \ :c:func:`ocd_disable`\  decrements the reference count, and if it
reaches zero, disables the debugging hardware.

.. This file was automatic generated / don't edit.

