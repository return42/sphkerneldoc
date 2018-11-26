.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/security.c

.. _`security_init`:

security_init
=============

.. c:function:: int security_init( void)

    initializes the security framework

    :param void:
        no arguments
    :type void: 

.. _`security_init.description`:

Description
-----------

This should be called early in the kernel initialization sequence.

.. _`security_module_enable`:

security_module_enable
======================

.. c:function:: int security_module_enable(const char *module)

    Load given security module on boot ?

    :param module:
        the name of the module
    :type module: const char \*

.. _`security_module_enable.description`:

Description
-----------

Each LSM must pass this method before registering its own operations
to avoid security registration races. This method may also be used
to check if your LSM is currently loaded during kernel initialization.

.. _`security_module_enable.true-if`:

true if
-------



- The passed LSM is the one chosen by user at boot time,
- or the passed LSM is configured as the default and the user did not
  choose an alternate LSM at boot time.

Otherwise, return false.

.. _`security_add_hooks`:

security_add_hooks
==================

.. c:function:: void security_add_hooks(struct security_hook_list *hooks, int count, char *lsm)

    Add a modules hooks to the hook lists.

    :param hooks:
        the hooks to add
    :type hooks: struct security_hook_list \*

    :param count:
        the number of hooks to add
    :type count: int

    :param lsm:
        the name of the security module
    :type lsm: char \*

.. _`security_add_hooks.description`:

Description
-----------

Each LSM has to register its hooks with the infrastructure.

.. This file was automatic generated / don't edit.

