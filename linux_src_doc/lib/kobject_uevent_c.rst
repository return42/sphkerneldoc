.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/kobject_uevent.c

.. _`kobject_action_type`:

kobject_action_type
===================

.. c:function:: int kobject_action_type(const char *buf, size_t count, enum kobject_action *type)

    translate action string to numeric type

    :param const char \*buf:
        buffer containing the action string, newline is ignored

    :param size_t count:
        length of buffer

    :param enum kobject_action \*type:
        pointer to the location to store the action type

.. _`kobject_action_type.description`:

Description
-----------

Returns 0 if the action string was recognized.

.. _`kobject_uevent_env`:

kobject_uevent_env
==================

.. c:function:: int kobject_uevent_env(struct kobject *kobj, enum kobject_action action, char  *envp_ext[])

    send an uevent with environmental data

    :param struct kobject \*kobj:
        struct kobject that the action is happening to

    :param enum kobject_action action:
        action that is happening

    :param char  \*envp_ext:
        pointer to environmental data

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

    :param struct kobject \*kobj:
        struct kobject that the action is happening to

    :param enum kobject_action action:
        action that is happening

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

    :param struct kobj_uevent_env \*env:
        environment buffer structure

    :param const char \*format:
        printf format for the key=value pair

    :param ... :
        variable arguments

.. _`add_uevent_var.description`:

Description
-----------

Returns 0 if environment variable was added successfully or -ENOMEM
if no space was available.

.. This file was automatic generated / don't edit.

