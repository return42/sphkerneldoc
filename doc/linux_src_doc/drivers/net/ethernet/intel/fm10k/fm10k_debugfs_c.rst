.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/fm10k/fm10k_debugfs.c

.. _`fm10k_dbg_q_vector_init`:

fm10k_dbg_q_vector_init
=======================

.. c:function:: void fm10k_dbg_q_vector_init(struct fm10k_q_vector *q_vector)

    setup debugfs for the q_vectors

    :param struct fm10k_q_vector \*q_vector:
        q_vector to allocate directories for

.. _`fm10k_dbg_q_vector_init.description`:

Description
-----------

A folder is created for each q_vector found. In each q_vector
folder, a debugfs file is created for each tx and rx ring
allocated to the q_vector.

.. _`fm10k_dbg_q_vector_exit`:

fm10k_dbg_q_vector_exit
=======================

.. c:function:: void fm10k_dbg_q_vector_exit(struct fm10k_q_vector *q_vector)

    setup debugfs for the q_vectors

    :param struct fm10k_q_vector \*q_vector:
        q_vector to allocate directories for

.. _`fm10k_dbg_intfc_init`:

fm10k_dbg_intfc_init
====================

.. c:function:: void fm10k_dbg_intfc_init(struct fm10k_intfc *interface)

    setup the debugfs directory for the intferface

    :param struct fm10k_intfc \*interface:
        the interface that is starting up

.. _`fm10k_dbg_intfc_exit`:

fm10k_dbg_intfc_exit
====================

.. c:function:: void fm10k_dbg_intfc_exit(struct fm10k_intfc *interface)

    clean out the interface's debugfs entries

    :param struct fm10k_intfc \*interface:
        the interface that is stopping

.. _`fm10k_dbg_init`:

fm10k_dbg_init
==============

.. c:function:: void fm10k_dbg_init( void)

    start up debugfs for the driver

    :param  void:
        no arguments

.. _`fm10k_dbg_exit`:

fm10k_dbg_exit
==============

.. c:function:: void fm10k_dbg_exit( void)

    clean out the driver's debugfs entries

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

