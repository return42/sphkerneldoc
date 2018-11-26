.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/keystone/gate.c

.. _`clk_psc_data`:

struct clk_psc_data
===================

.. c:type:: struct clk_psc_data

    PSC data

.. _`clk_psc_data.definition`:

Definition
----------

.. code-block:: c

    struct clk_psc_data {
        void __iomem *control_base;
        void __iomem *domain_base;
        u32 domain_id;
    }

.. _`clk_psc_data.members`:

Members
-------

control_base
    Base address for a PSC control

domain_base
    Base address for a PSC domain

domain_id
    PSC domain id number

.. _`clk_psc`:

struct clk_psc
==============

.. c:type:: struct clk_psc

    PSC clock structure

.. _`clk_psc.definition`:

Definition
----------

.. code-block:: c

    struct clk_psc {
        struct clk_hw hw;
        struct clk_psc_data *psc_data;
        spinlock_t *lock;
    }

.. _`clk_psc.members`:

Members
-------

hw
    clk_hw for the psc

psc_data
    PSC driver specific data

lock
    Spinlock used by the driver

.. _`clk_register_psc`:

clk_register_psc
================

.. c:function:: struct clk *clk_register_psc(struct device *dev, const char *name, const char *parent_name, struct clk_psc_data *psc_data, spinlock_t *lock)

    register psc clock

    :param dev:
        device that is registering this clock
    :type dev: struct device \*

    :param name:
        name of this clock
    :type name: const char \*

    :param parent_name:
        name of clock's parent
    :type parent_name: const char \*

    :param psc_data:
        platform data to configure this clock
    :type psc_data: struct clk_psc_data \*

    :param lock:
        spinlock used by this clock
    :type lock: spinlock_t \*

.. _`of_psc_clk_init`:

of_psc_clk_init
===============

.. c:function:: void of_psc_clk_init(struct device_node *node, spinlock_t *lock)

    initialize psc clock through DT

    :param node:
        device tree node for this clock
    :type node: struct device_node \*

    :param lock:
        spinlock used by this clock
    :type lock: spinlock_t \*

.. _`of_keystone_psc_clk_init`:

of_keystone_psc_clk_init
========================

.. c:function:: void of_keystone_psc_clk_init(struct device_node *node)

    initialize psc clock through DT

    :param node:
        device tree node for this clock
    :type node: struct device_node \*

.. This file was automatic generated / don't edit.

