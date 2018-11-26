.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/core/netevent.c

.. _`register_netevent_notifier`:

register_netevent_notifier
==========================

.. c:function:: int register_netevent_notifier(struct notifier_block *nb)

    register a netevent notifier block

    :param nb:
        notifier
    :type nb: struct notifier_block \*

.. _`register_netevent_notifier.description`:

Description
-----------

Register a notifier to be called when a netevent occurs.
The notifier passed is linked into the kernel structures and must
not be reused until it has been unregistered. A negative errno code
is returned on a failure.

.. _`unregister_netevent_notifier`:

unregister_netevent_notifier
============================

.. c:function:: int unregister_netevent_notifier(struct notifier_block *nb)

    unregister a netevent notifier block

    :param nb:
        notifier
    :type nb: struct notifier_block \*

.. _`unregister_netevent_notifier.description`:

Description
-----------

Unregister a notifier previously registered by
\ :c:func:`register_neigh_notifier`\ . The notifier is unlinked into the
kernel structures and may then be reused. A negative errno code
is returned on a failure.

.. _`call_netevent_notifiers`:

call_netevent_notifiers
=======================

.. c:function:: int call_netevent_notifiers(unsigned long val, void *v)

    call all netevent notifier blocks

    :param val:
        value passed unmodified to notifier function
    :type val: unsigned long

    :param v:
        pointer passed unmodified to notifier function
    :type v: void \*

.. _`call_netevent_notifiers.description`:

Description
-----------

Call all neighbour notifier blocks.  Parameters and return value
are as for \ :c:func:`notifier_call_chain`\ .

.. This file was automatic generated / don't edit.

