.. -*- coding: utf-8; mode: rst -*-

========
module.h
========


.. _`module_init`:

module_init
===========

.. c:function:: module_init ( x)

    driver initialization entry point

    :param x:
        function to be run at kernel boot time or module insertion



.. _`module_init.description`:

Description
-----------

:c:func:`module_init` will either be called during :c:func:`do_initcalls` (if
builtin) or at module insertion time (if a module).  There can only
be one per module.



.. _`module_exit`:

module_exit
===========

.. c:function:: module_exit ( x)

    driver exit entry point

    :param x:
        function to be run when driver is removed



.. _`module_exit.description`:

Description
-----------

:c:func:`module_exit` will wrap the driver clean-up code
with :c:func:`cleanup_module` when used with rmmod when
the driver is a module.  If the driver is statically
compiled into the kernel, :c:func:`module_exit` has no effect.
There can only be one per module.

