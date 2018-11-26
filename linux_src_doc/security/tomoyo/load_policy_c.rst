.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/tomoyo/load_policy.c

.. _`tomoyo_loader_setup`:

tomoyo_loader_setup
===================

.. c:function:: int tomoyo_loader_setup(char *str)

    Set policy loader.

    :param str:
        Program to use as a policy loader (e.g. /sbin/tomoyo-init ).
    :type str: char \*

.. _`tomoyo_loader_setup.description`:

Description
-----------

Returns 0.

.. _`tomoyo_policy_loader_exists`:

tomoyo_policy_loader_exists
===========================

.. c:function:: bool tomoyo_policy_loader_exists( void)

    Check whether /sbin/tomoyo-init exists.

    :param void:
        no arguments
    :type void: 

.. _`tomoyo_policy_loader_exists.description`:

Description
-----------

Returns true if /sbin/tomoyo-init exists, false otherwise.

.. _`tomoyo_trigger_setup`:

tomoyo_trigger_setup
====================

.. c:function:: int tomoyo_trigger_setup(char *str)

    Set trigger for activation.

    :param str:
        Program to use as an activation trigger (e.g. /sbin/init ).
    :type str: char \*

.. _`tomoyo_trigger_setup.description`:

Description
-----------

Returns 0.

.. _`tomoyo_load_policy`:

tomoyo_load_policy
==================

.. c:function:: void tomoyo_load_policy(const char *filename)

    Run external policy loader to load policy.

    :param filename:
        The program about to start.
    :type filename: const char \*

.. _`tomoyo_load_policy.description`:

Description
-----------

This function checks whether \ ``filename``\  is /sbin/init , and if so
invoke /sbin/tomoyo-init and wait for the termination of /sbin/tomoyo-init
and then continues invocation of /sbin/init.
/sbin/tomoyo-init reads policy files in /etc/tomoyo/ directory and
writes to /sys/kernel/security/tomoyo/ interfaces.

Returns nothing.

.. This file was automatic generated / don't edit.

