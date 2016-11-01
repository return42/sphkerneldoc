.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb4/sched.c

.. _`cxgb4_sched_class_bind`:

cxgb4_sched_class_bind
======================

.. c:function:: int cxgb4_sched_class_bind(struct net_device *dev, void *arg, enum sched_bind_type type)

    Bind an entity to a scheduling class

    :param struct net_device \*dev:
        net_device pointer

    :param void \*arg:
        Entity opaque data

    :param enum sched_bind_type type:
        Entity type (Queue)

.. _`cxgb4_sched_class_bind.description`:

Description
-----------

Binds an entity (queue) to a scheduling class.  If the entity
is bound to another class, it will be unbound from the other class
and bound to the class specified in \ ``arg``\ .

.. _`cxgb4_sched_class_unbind`:

cxgb4_sched_class_unbind
========================

.. c:function:: int cxgb4_sched_class_unbind(struct net_device *dev, void *arg, enum sched_bind_type type)

    Unbind an entity from a scheduling class

    :param struct net_device \*dev:
        net_device pointer

    :param void \*arg:
        Entity opaque data

    :param enum sched_bind_type type:
        Entity type (Queue)

.. _`cxgb4_sched_class_unbind.description`:

Description
-----------

Unbinds an entity (queue) from a scheduling class.

.. _`cxgb4_sched_class_alloc`:

cxgb4_sched_class_alloc
=======================

.. c:function:: struct sched_class *cxgb4_sched_class_alloc(struct net_device *dev, struct ch_sched_params *p)

    allocate a scheduling class

    :param struct net_device \*dev:
        net_device pointer

    :param struct ch_sched_params \*p:
        new scheduling class to create.

.. _`cxgb4_sched_class_alloc.description`:

Description
-----------

Returns pointer to the scheduling class created.  If \ ``p``\  is NULL, then
it allocates and returns any available unused scheduling class. If a
scheduling class with matching \ ``p``\  is found, then the matching class is
returned.

.. This file was automatic generated / don't edit.

