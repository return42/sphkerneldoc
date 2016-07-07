.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/context_tracking.c

.. _`__context_tracking_enter`:

__context_tracking_enter
========================

.. c:function:: void __context_tracking_enter(enum ctx_state state)

    Inform the context tracking that the CPU is going enter user or guest space mode.

    :param enum ctx_state state:
        *undescribed*

.. _`__context_tracking_enter.description`:

Description
-----------

This function must be called right before we switch from the kernel
to user or guest space, when it's guaranteed the remaining kernel
instructions to execute won't use any RCU read side critical section
because this function sets RCU in extended quiescent state.

.. _`__context_tracking_exit`:

__context_tracking_exit
=======================

.. c:function:: void __context_tracking_exit(enum ctx_state state)

    Inform the context tracking that the CPU is exiting user or guest mode and entering the kernel.

    :param enum ctx_state state:
        *undescribed*

.. _`__context_tracking_exit.description`:

Description
-----------

This function must be called after we entered the kernel from user or
guest space before any use of RCU read side critical section. This
potentially include any high level kernel code like syscalls, exceptions,
signal handling, etc...

This call supports re-entrancy. This way it can be called from any exception
handler without needing to know if we came from userspace or not.

.. This file was automatic generated / don't edit.

