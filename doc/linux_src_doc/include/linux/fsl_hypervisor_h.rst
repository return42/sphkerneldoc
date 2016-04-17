.. -*- coding: utf-8; mode: rst -*-

================
fsl_hypervisor.h
================


.. _`fsl_hv_failover_register`:

fsl_hv_failover_register
========================

.. c:function:: int fsl_hv_failover_register (struct notifier_block *nb)

    register a callback for failover events

    :param struct notifier_block \*nb:
        pointer to caller-supplied notifier_block structure



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

.. c:function:: int fsl_hv_failover_unregister (struct notifier_block *nb)

    unregister a callback for failover events

    :param struct notifier_block \*nb:
        the same 'nb' used in previous fsl_hv_failover_register call

