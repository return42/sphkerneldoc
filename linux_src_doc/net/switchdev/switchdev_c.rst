.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/switchdev/switchdev.c

.. _`switchdev_trans_item_enqueue`:

switchdev_trans_item_enqueue
============================

.. c:function:: void switchdev_trans_item_enqueue(struct switchdev_trans *trans, void *data, void (*destructor)(void const *), struct switchdev_trans_item *tritem)

    Enqueue data item to transaction queue

    :param trans:
        transaction
    :type trans: struct switchdev_trans \*

    :param data:
        pointer to data being queued
    :type data: void \*

    :param void (\*destructor)(void const \*):
        data destructor

    :param tritem:
        transaction item being queued
    :type tritem: struct switchdev_trans_item \*

.. _`switchdev_trans_item_enqueue.description`:

Description
-----------

Enqeueue data item to transaction queue. tritem is typically placed in
cointainter pointed at by data pointer. Destructor is called on
transaction abort and after successful commit phase in case
the caller did not dequeue the item before.

.. _`switchdev_trans_item_dequeue`:

switchdev_trans_item_dequeue
============================

.. c:function:: void *switchdev_trans_item_dequeue(struct switchdev_trans *trans)

    Dequeue data item from transaction queue

    :param trans:
        transaction
    :type trans: struct switchdev_trans \*

.. _`switchdev_deferred_process`:

switchdev_deferred_process
==========================

.. c:function:: void switchdev_deferred_process( void)

    Process ops in deferred queue

    :param void:
        no arguments
    :type void: 

.. _`switchdev_deferred_process.description`:

Description
-----------

Called to flush the ops currently queued in deferred ops queue.
rtnl_lock must be held.

.. _`switchdev_port_attr_get`:

switchdev_port_attr_get
=======================

.. c:function:: int switchdev_port_attr_get(struct net_device *dev, struct switchdev_attr *attr)

    Get port attribute

    :param dev:
        port device
    :type dev: struct net_device \*

    :param attr:
        attribute to get
    :type attr: struct switchdev_attr \*

.. _`switchdev_port_attr_set`:

switchdev_port_attr_set
=======================

.. c:function:: int switchdev_port_attr_set(struct net_device *dev, const struct switchdev_attr *attr)

    Set port attribute

    :param dev:
        port device
    :type dev: struct net_device \*

    :param attr:
        attribute to set
    :type attr: const struct switchdev_attr \*

.. _`switchdev_port_attr_set.description`:

Description
-----------

Use a 2-phase prepare-commit transaction model to ensure
system is not left in a partially updated state due to
failure from driver/device.

rtnl_lock must be held and must not be in atomic section,
in case SWITCHDEV_F_DEFER flag is not set.

.. _`switchdev_port_obj_add`:

switchdev_port_obj_add
======================

.. c:function:: int switchdev_port_obj_add(struct net_device *dev, const struct switchdev_obj *obj)

    Add port object

    :param dev:
        port device
    :type dev: struct net_device \*

    :param obj:
        object to add
    :type obj: const struct switchdev_obj \*

.. _`switchdev_port_obj_add.description`:

Description
-----------

Use a 2-phase prepare-commit transaction model to ensure
system is not left in a partially updated state due to
failure from driver/device.

rtnl_lock must be held and must not be in atomic section,
in case SWITCHDEV_F_DEFER flag is not set.

.. _`switchdev_port_obj_del`:

switchdev_port_obj_del
======================

.. c:function:: int switchdev_port_obj_del(struct net_device *dev, const struct switchdev_obj *obj)

    Delete port object

    :param dev:
        port device
    :type dev: struct net_device \*

    :param obj:
        object to delete
    :type obj: const struct switchdev_obj \*

.. _`switchdev_port_obj_del.description`:

Description
-----------

rtnl_lock must be held and must not be in atomic section,
in case SWITCHDEV_F_DEFER flag is not set.

.. _`register_switchdev_notifier`:

register_switchdev_notifier
===========================

.. c:function:: int register_switchdev_notifier(struct notifier_block *nb)

    Register notifier

    :param nb:
        notifier_block
    :type nb: struct notifier_block \*

.. _`register_switchdev_notifier.description`:

Description
-----------

Register switch device notifier.

.. _`unregister_switchdev_notifier`:

unregister_switchdev_notifier
=============================

.. c:function:: int unregister_switchdev_notifier(struct notifier_block *nb)

    Unregister notifier

    :param nb:
        notifier_block
    :type nb: struct notifier_block \*

.. _`unregister_switchdev_notifier.description`:

Description
-----------

Unregister switch device notifier.

.. _`call_switchdev_notifiers`:

call_switchdev_notifiers
========================

.. c:function:: int call_switchdev_notifiers(unsigned long val, struct net_device *dev, struct switchdev_notifier_info *info)

    Call notifiers

    :param val:
        value passed unmodified to notifier function
    :type val: unsigned long

    :param dev:
        port device
    :type dev: struct net_device \*

    :param info:
        notifier information data
    :type info: struct switchdev_notifier_info \*

.. _`call_switchdev_notifiers.description`:

Description
-----------

Call all network notifier blocks.

.. This file was automatic generated / don't edit.

