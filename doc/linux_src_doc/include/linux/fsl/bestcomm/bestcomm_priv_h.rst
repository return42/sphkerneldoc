.. -*- coding: utf-8; mode: rst -*-

===============
bestcomm_priv.h
===============


.. _`bcom_tdt`:

struct bcom_tdt
===============

.. c:type:: bcom_tdt

    Task Descriptor Table Entry


.. _`bcom_tdt.definition`:

Definition
----------

.. code-block:: c

  struct bcom_tdt {
  };


.. _`bcom_tdt.members`:

Members
-------




.. _`bcom_engine`:

struct bcom_engine
==================

.. c:type:: bcom_engine

    


.. _`bcom_engine.definition`:

Definition
----------

.. code-block:: c

  struct bcom_engine {
  };


.. _`bcom_engine.members`:

Members
-------




.. _`bcom_engine.description`:

Description
-----------



This holds all info needed globaly to handle the engine



.. _`bcom_disable_prefetch`:

bcom_disable_prefetch
=====================

.. c:function:: void bcom_disable_prefetch ( void)

    Hook to disable bus prefetching

    :param void:
        no arguments



.. _`bcom_disable_prefetch.description`:

Description
-----------


ATA DMA and the original MPC5200 need this due to silicon bugs.  At the
moment disabling prefetch is a one-way street.  There is no mechanism
in place to turn prefetch back on after it has been disabled.  There is
no reason it couldn't be done, it would just be more complex to implement.

