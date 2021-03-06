.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/switchdev.h

.. _`switchdev_ops`:

struct switchdev_ops
====================

.. c:type:: struct switchdev_ops

    switchdev operations

.. _`switchdev_ops.definition`:

Definition
----------

.. code-block:: c

    struct switchdev_ops {
        int (*switchdev_port_attr_get)(struct net_device *dev, struct switchdev_attr *attr);
        int (*switchdev_port_attr_set)(struct net_device *dev,const struct switchdev_attr *attr, struct switchdev_trans *trans);
        int (*switchdev_port_obj_add)(struct net_device *dev,const struct switchdev_obj *obj, struct switchdev_trans *trans);
        int (*switchdev_port_obj_del)(struct net_device *dev, const struct switchdev_obj *obj);
    }

.. _`switchdev_ops.members`:

Members
-------

switchdev_port_attr_get
    Get a port attribute (see switchdev_attr).

switchdev_port_attr_set
    Set a port attribute (see switchdev_attr).

switchdev_port_obj_add
    Add an object to port (see switchdev_obj\_\*).

switchdev_port_obj_del
    Delete an object from port (see switchdev_obj\_\*).

.. This file was automatic generated / don't edit.

