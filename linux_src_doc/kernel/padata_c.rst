.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/padata.c

.. _`padata_do_parallel`:

padata_do_parallel
==================

.. c:function:: int padata_do_parallel(struct padata_instance *pinst, struct padata_priv *padata, int cb_cpu)

    padata parallelization function

    :param pinst:
        padata instance
    :type pinst: struct padata_instance \*

    :param padata:
        object to be parallelized
    :type padata: struct padata_priv \*

    :param cb_cpu:
        cpu the serialization callback function will run on,
        must be in the serial cpumask of padata(i.e. cpumask.cbcpu).
    :type cb_cpu: int

.. _`padata_do_parallel.description`:

Description
-----------

The parallelization callback function will run with BHs off.

.. _`padata_do_parallel.note`:

Note
----

Every object which is parallelized by padata_do_parallel
must be seen by padata_do_serial.

.. _`padata_do_serial`:

padata_do_serial
================

.. c:function:: void padata_do_serial(struct padata_priv *padata)

    padata serialization function

    :param padata:
        object to be serialized.
    :type padata: struct padata_priv \*

.. _`padata_do_serial.description`:

Description
-----------

padata_do_serial must be called for every parallelized object.
The serialization callback function will run with BHs off.

.. _`padata_register_cpumask_notifier`:

padata_register_cpumask_notifier
================================

.. c:function:: int padata_register_cpumask_notifier(struct padata_instance *pinst, struct notifier_block *nblock)

    Registers a notifier that will be called if either pcpu or cbcpu or both cpumasks change.

    :param pinst:
        A poineter to padata instance
    :type pinst: struct padata_instance \*

    :param nblock:
        A pointer to notifier block.
    :type nblock: struct notifier_block \*

.. _`padata_unregister_cpumask_notifier`:

padata_unregister_cpumask_notifier
==================================

.. c:function:: int padata_unregister_cpumask_notifier(struct padata_instance *pinst, struct notifier_block *nblock)

    Unregisters cpumask notifier registered earlier  using padata_register_cpumask_notifier

    :param pinst:
        A pointer to data instance.
    :type pinst: struct padata_instance \*

    :param nblock:
        *undescribed*
    :type nblock: struct notifier_block \*

.. _`padata_set_cpumask`:

padata_set_cpumask
==================

.. c:function:: int padata_set_cpumask(struct padata_instance *pinst, int cpumask_type, cpumask_var_t cpumask)

    Sets specified by \ ``cpumask_type``\  cpumask to the value equivalent to \ ``cpumask``\ .

    :param pinst:
        padata instance
    :type pinst: struct padata_instance \*

    :param cpumask_type:
        PADATA_CPU_SERIAL or PADATA_CPU_PARALLEL corresponding
        to parallel and serial cpumasks respectively.
    :type cpumask_type: int

    :param cpumask:
        the cpumask to use
    :type cpumask: cpumask_var_t

.. _`padata_start`:

padata_start
============

.. c:function:: int padata_start(struct padata_instance *pinst)

    start the parallel processing

    :param pinst:
        padata instance to start
    :type pinst: struct padata_instance \*

.. _`padata_stop`:

padata_stop
===========

.. c:function:: void padata_stop(struct padata_instance *pinst)

    stop the parallel processing

    :param pinst:
        padata instance to stop
    :type pinst: struct padata_instance \*

.. _`padata_alloc`:

padata_alloc
============

.. c:function:: struct padata_instance *padata_alloc(struct workqueue_struct *wq, const struct cpumask *pcpumask, const struct cpumask *cbcpumask)

    allocate and initialize a padata instance and specify cpumasks for serial and parallel workers.

    :param wq:
        workqueue to use for the allocated padata instance
    :type wq: struct workqueue_struct \*

    :param pcpumask:
        cpumask that will be used for padata parallelization
    :type pcpumask: const struct cpumask \*

    :param cbcpumask:
        cpumask that will be used for padata serialization
    :type cbcpumask: const struct cpumask \*

.. _`padata_alloc.description`:

Description
-----------

Must be called from a \ :c:func:`cpus_read_lock`\  protected region

.. _`padata_alloc_possible`:

padata_alloc_possible
=====================

.. c:function:: struct padata_instance *padata_alloc_possible(struct workqueue_struct *wq)

    Allocate and initialize padata instance. Use the cpu_possible_mask for serial and parallel workers.

    :param wq:
        workqueue to use for the allocated padata instance
    :type wq: struct workqueue_struct \*

.. _`padata_alloc_possible.description`:

Description
-----------

Must be called from a \ :c:func:`cpus_read_lock`\  protected region

.. _`padata_free`:

padata_free
===========

.. c:function:: void padata_free(struct padata_instance *pinst)

    free a padata instance

    :param pinst:
        *undescribed*
    :type pinst: struct padata_instance \*

.. This file was automatic generated / don't edit.

