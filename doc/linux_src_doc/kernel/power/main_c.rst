.. -*- coding: utf-8; mode: rst -*-

======
main.c
======


.. _`state_show`:

state_show
==========

.. c:function:: ssize_t state_show (struct kobject *kobj, struct kobj_attribute *attr, char *buf)

    control system sleep states.

    :param struct kobject \*kobj:

        *undescribed*

    :param struct kobj_attribute \*attr:

        *undescribed*

    :param char \*buf:

        *undescribed*



.. _`state_show.description`:

Description
-----------


:c:func:`show` returns available sleep state labels, which may be "mem", "standby",
"freeze" and "disk" (hibernation).  See Documentation/power/states.txt for a
description of what they mean.

:c:func:`store` accepts one of those strings, translates it into the proper
enumerated value, and initiates a suspend transition.

