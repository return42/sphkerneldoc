.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/tracepoint.c

.. _`tracepoint_probe_register_prio`:

tracepoint_probe_register_prio
==============================

.. c:function:: int tracepoint_probe_register_prio(struct tracepoint *tp, void *probe, void *data, int prio)

    Connect a probe to a tracepoint with priority

    :param tp:
        tracepoint
    :type tp: struct tracepoint \*

    :param probe:
        probe handler
    :type probe: void \*

    :param data:
        tracepoint data
    :type data: void \*

    :param prio:
        priority of this function over other registered functions
    :type prio: int

.. _`tracepoint_probe_register_prio.description`:

Description
-----------

Returns 0 if ok, error value on error.

.. _`tracepoint_probe_register_prio.note`:

Note
----

if \ ``tp``\  is within a module, the caller is responsible for
unregistering the probe before the module is gone. This can be
performed either with a tracepoint module going notifier, or from
within module exit functions.

.. _`tracepoint_probe_register`:

tracepoint_probe_register
=========================

.. c:function:: int tracepoint_probe_register(struct tracepoint *tp, void *probe, void *data)

    Connect a probe to a tracepoint

    :param tp:
        tracepoint
    :type tp: struct tracepoint \*

    :param probe:
        probe handler
    :type probe: void \*

    :param data:
        tracepoint data
    :type data: void \*

.. _`tracepoint_probe_register.description`:

Description
-----------

Returns 0 if ok, error value on error.

.. _`tracepoint_probe_register.note`:

Note
----

if \ ``tp``\  is within a module, the caller is responsible for
unregistering the probe before the module is gone. This can be
performed either with a tracepoint module going notifier, or from
within module exit functions.

.. _`tracepoint_probe_unregister`:

tracepoint_probe_unregister
===========================

.. c:function:: int tracepoint_probe_unregister(struct tracepoint *tp, void *probe, void *data)

    Disconnect a probe from a tracepoint

    :param tp:
        tracepoint
    :type tp: struct tracepoint \*

    :param probe:
        probe function pointer
    :type probe: void \*

    :param data:
        tracepoint data
    :type data: void \*

.. _`tracepoint_probe_unregister.description`:

Description
-----------

Returns 0 if ok, error value on error.

.. _`register_tracepoint_module_notifier`:

register_tracepoint_module_notifier
===================================

.. c:function:: int register_tracepoint_module_notifier(struct notifier_block *nb)

    register tracepoint coming/going notifier

    :param nb:
        notifier block
    :type nb: struct notifier_block \*

.. _`register_tracepoint_module_notifier.description`:

Description
-----------

Notifiers registered with this function are called on module
coming/going with the tracepoint_module_list_mutex held.
The notifier block callback should expect a "struct tp_module" data
pointer.

.. _`unregister_tracepoint_module_notifier`:

unregister_tracepoint_module_notifier
=====================================

.. c:function:: int unregister_tracepoint_module_notifier(struct notifier_block *nb)

    unregister tracepoint coming/going notifier

    :param nb:
        notifier block
    :type nb: struct notifier_block \*

.. _`unregister_tracepoint_module_notifier.description`:

Description
-----------

The notifier block callback should expect a "struct tp_module" data
pointer.

.. _`for_each_kernel_tracepoint`:

for_each_kernel_tracepoint
==========================

.. c:function:: void for_each_kernel_tracepoint(void (*fct)(struct tracepoint *tp, void *priv), void *priv)

    iteration on all kernel tracepoints

    :param void (\*fct)(struct tracepoint \*tp, void \*priv):
        callback

    :param priv:
        private data
    :type priv: void \*

.. This file was automatic generated / don't edit.

