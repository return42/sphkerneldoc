.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/fsl_hypervisor.h

.. _`fsl_hv_failover_register`:

fsl_hv_failover_register
========================

.. c:function:: int fsl_hv_failover_register(struct notifier_block *nb)

    register a callback for failover events

    :param nb:
        pointer to caller-supplied notifier_block structure
    :type nb: struct notifier_block \*

.. _`fsl_hv_failover_register.description`:

Description
-----------

This function is called by device drivers to register their callback
functions for fail-over events.

The caller should allocate a notifier_block object and initialize the
'priority' and 'notifier_call' fields.

.. _`fsl_hv_failover_unregister`:

fsl_hv_failover_unregister
==========================

.. c:function:: int fsl_hv_failover_unregister(struct notifier_block *nb)

    unregister a callback for failover events

    :param nb:
        the same 'nb' used in previous fsl_hv_failover_register call
    :type nb: struct notifier_block \*

.. This file was automatic generated / don't edit.

