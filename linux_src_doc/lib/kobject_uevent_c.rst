.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/kobject_uevent.c

.. _`kobject_synth_uevent`:

kobject_synth_uevent
====================

.. c:function:: int kobject_synth_uevent(struct kobject *kobj, const char *buf, size_t count)

    send synthetic uevent with arguments

    :param kobj:
        struct kobject for which synthetic uevent is to be generated
    :type kobj: struct kobject \*

    :param buf:
        buffer containing action type and action args, newline is ignored
    :type buf: const char \*

    :param count:
        length of buffer
    :type count: size_t

.. _`kobject_synth_uevent.description`:

Description
-----------

Returns 0 if \ :c:func:`kobject_synthetic_uevent`\  is completed with success or the
corresponding error when it fails.

.. _`kobject_uevent_env`:

kobject_uevent_env
==================

.. c:function:: int kobject_uevent_env(struct kobject *kobj, enum kobject_action action, char  *envp_ext)

    send an uevent with environmental data

    :param kobj:
        struct kobject that the action is happening to
    :type kobj: struct kobject \*

    :param action:
        action that is happening
    :type action: enum kobject_action

    :param envp_ext:
        pointer to environmental data
    :type envp_ext: char  \*

.. _`kobject_uevent_env.description`:

Description
-----------

Returns 0 if \ :c:func:`kobject_uevent_env`\  is completed with success or the
corresponding error when it fails.

.. _`kobject_uevent`:

kobject_uevent
==============

.. c:function:: int kobject_uevent(struct kobject *kobj, enum kobject_action action)

    notify userspace by sending an uevent

    :param kobj:
        struct kobject that the action is happening to
    :type kobj: struct kobject \*

    :param action:
        action that is happening
    :type action: enum kobject_action

.. _`kobject_uevent.description`:

Description
-----------

Returns 0 if \ :c:func:`kobject_uevent`\  is completed with success or the
corresponding error when it fails.

.. _`add_uevent_var`:

add_uevent_var
==============

.. c:function:: int add_uevent_var(struct kobj_uevent_env *env, const char *format,  ...)

    add key value string to the environment buffer

    :param env:
        environment buffer structure
    :type env: struct kobj_uevent_env \*

    :param format:
        printf format for the key=value pair
    :type format: const char \*

    :param ellipsis ellipsis:
        variable arguments

.. _`add_uevent_var.description`:

Description
-----------

Returns 0 if environment variable was added successfully or -ENOMEM
if no space was available.

.. This file was automatic generated / don't edit.

