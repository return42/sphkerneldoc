.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ps3/sys-manager-core.c

.. _`ps3_sys_manager_register_ops`:

ps3_sys_manager_register_ops
============================

.. c:function:: void ps3_sys_manager_register_ops(const struct ps3_sys_manager_ops *ops)

    Bind ps3_sys_manager_ops to a module.

    :param ops:
        struct ps3_sys_manager_ops.
    :type ops: const struct ps3_sys_manager_ops \*

.. _`ps3_sys_manager_register_ops.description`:

Description
-----------

To be called from \ :c:func:`ps3_sys_manager_probe`\  and \ :c:func:`ps3_sys_manager_remove`\  to
register call back ops for power control.  Copies data to the static
variable ps3_sys_manager_ops.

.. This file was automatic generated / don't edit.

