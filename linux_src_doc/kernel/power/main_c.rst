.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/power/main.c

.. _`__pm_pr_dbg`:

\__pm_pr_dbg
============

.. c:function:: void __pm_pr_dbg(bool defer, const char *fmt,  ...)

    Print a suspend debug message to the kernel log.

    :param defer:
        Whether or not to use \ :c:func:`printk_deferred`\  to print the message.
    :type defer: bool

    :param fmt:
        Message format.
    :type fmt: const char \*

    :param ellipsis ellipsis:
        variable arguments

.. _`__pm_pr_dbg.description`:

Description
-----------

The message will be emitted if enabled through the pm_debug_messages
sysfs attribute.

.. _`state_show`:

state_show
==========

.. c:function:: ssize_t state_show(struct kobject *kobj, struct kobj_attribute *attr, char *buf)

    control system sleep states.

    :param kobj:
        *undescribed*
    :type kobj: struct kobject \*

    :param attr:
        *undescribed*
    :type attr: struct kobj_attribute \*

    :param buf:
        *undescribed*
    :type buf: char \*

.. _`state_show.description`:

Description
-----------

\ :c:func:`show`\  returns available sleep state labels, which may be "mem", "standby",
"freeze" and "disk" (hibernation).
See Documentation/admin-guide/pm/sleep-states.rst for a description of
what they mean.

\ :c:func:`store`\  accepts one of those strings, translates it into the proper
enumerated value, and initiates a suspend transition.

.. This file was automatic generated / don't edit.

