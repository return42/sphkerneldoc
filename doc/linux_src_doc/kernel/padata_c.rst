.. -*- coding: utf-8; mode: rst -*-

========
padata.c
========


.. _`padata_do_parallel`:

padata_do_parallel
==================

.. c:function:: int padata_do_parallel (struct padata_instance *pinst, struct padata_priv *padata, int cb_cpu)

    padata parallelization function

    :param struct padata_instance \*pinst:
        padata instance

    :param struct padata_priv \*padata:
        object to be parallelized

    :param int cb_cpu:
        cpu the serialization callback function will run on,
        must be in the serial cpumask of padata(i.e. cpumask.cbcpu).



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

.. c:function:: void padata_do_serial (struct padata_priv *padata)

    padata serialization function

    :param struct padata_priv \*padata:
        object to be serialized.



.. _`padata_do_serial.description`:

Description
-----------

padata_do_serial must be called for every parallelized object.
The serialization callback function will run with BHs off.



.. _`padata_register_cpumask_notifier`:

padata_register_cpumask_notifier
================================

.. c:function:: int padata_register_cpumask_notifier (struct padata_instance *pinst, struct notifier_block *nblock)

    Registers a notifier that will be called if either pcpu or cbcpu or both cpumasks change.

    :param struct padata_instance \*pinst:
        A poineter to padata instance

    :param struct notifier_block \*nblock:
        A pointer to notifier block.



.. _`padata_unregister_cpumask_notifier`:

padata_unregister_cpumask_notifier
==================================

.. c:function:: int padata_unregister_cpumask_notifier (struct padata_instance *pinst, struct notifier_block *nblock)

    Unregisters cpumask notifier registered earlier using padata_register_cpumask_notifier

    :param struct padata_instance \*pinst:
        A pointer to data instance.

    :param struct notifier_block \*nblock:

        *undescribed*



.. _`padata_set_cpumasks`:

padata_set_cpumasks
===================

.. c:function:: int padata_set_cpumasks (struct padata_instance *pinst, cpumask_var_t pcpumask, cpumask_var_t cbcpumask)

    Set both parallel and serial cpumasks. The first one is used by parallel workers and the second one by the wokers doing serialization.

    :param struct padata_instance \*pinst:
        padata instance

    :param cpumask_var_t pcpumask:
        the cpumask to use for parallel workers

    :param cpumask_var_t cbcpumask:
        the cpumsak to use for serial workers



.. _`padata_set_cpumask`:

padata_set_cpumask
==================

.. c:function:: int padata_set_cpumask (struct padata_instance *pinst, int cpumask_type, cpumask_var_t cpumask)

    :param struct padata_instance \*pinst:
        padata instance

    :param int cpumask_type:
        PADATA_CPU_SERIAL or PADATA_CPU_PARALLEL corresponding
        to parallel and serial cpumasks respectively.

    :param cpumask_var_t cpumask:
        the cpumask to use



.. _`padata_set_cpumask.description`:

Description
-----------

equivalent to ``cpumask``\ .



.. _`padata_start`:

padata_start
============

.. c:function:: int padata_start (struct padata_instance *pinst)

    start the parallel processing

    :param struct padata_instance \*pinst:
        padata instance to start



.. _`padata_stop`:

padata_stop
===========

.. c:function:: void padata_stop (struct padata_instance *pinst)

    stop the parallel processing

    :param struct padata_instance \*pinst:
        padata instance to stop



.. _`padata_alloc_possible`:

padata_alloc_possible
=====================

.. c:function:: struct padata_instance *padata_alloc_possible (struct workqueue_struct *wq)

    Allocate and initialize padata instance. Use the cpu_possible_mask for serial and parallel workers.

    :param struct workqueue_struct \*wq:
        workqueue to use for the allocated padata instance



.. _`padata_alloc`:

padata_alloc
============

.. c:function:: struct padata_instance *padata_alloc (struct workqueue_struct *wq, const struct cpumask *pcpumask, const struct cpumask *cbcpumask)

    allocate and initialize a padata instance and specify cpumasks for serial and parallel workers.

    :param struct workqueue_struct \*wq:
        workqueue to use for the allocated padata instance

    :param const struct cpumask \*pcpumask:
        cpumask that will be used for padata parallelization

    :param const struct cpumask \*cbcpumask:
        cpumask that will be used for padata serialization



.. _`padata_free`:

padata_free
===========

.. c:function:: void padata_free (struct padata_instance *pinst)

    free a padata instance

    :param struct padata_instance \*pinst:

        *undescribed*

