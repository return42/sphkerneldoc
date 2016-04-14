.. -*- coding: utf-8; mode: rst -*-

==========
security.c
==========

.. _`security_init`:

security_init
=============

.. c:function:: int security_init ( void)

    initializes the security framework

    :param void:
        no arguments


.. _`security_init.description`:

Description
-----------


This should be called early in the kernel initialization sequence.


.. _`security_module_enable`:

security_module_enable
======================

.. c:function:: int security_module_enable (const char *module)

    Load given security module on boot ?

    :param const char \*module:
        the name of the module


.. _`security_module_enable.description`:

Description
-----------

Each LSM must pass this method before registering its own operations
to avoid security registration races. This method may also be used
to check if your LSM is currently loaded during kernel initialization.

Return true if::

        -The passed LSM is the one chosen by user at boot time,
        -or the passed LSM is configured as the default and the user did not
         choose an alternate LSM at boot time.

Otherwise, return false.

