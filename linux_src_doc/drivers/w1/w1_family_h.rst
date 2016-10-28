.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/w1/w1_family.h

.. _`w1_family_ops`:

struct w1_family_ops
====================

.. c:type:: struct w1_family_ops

    operations for a family type

.. _`w1_family_ops.definition`:

Definition
----------

.. code-block:: c

    struct w1_family_ops {
        int (*add_slave)(struct w1_slave *);
        void (*remove_slave)(struct w1_slave *);
        const struct attribute_group **groups;
    }

.. _`w1_family_ops.members`:

Members
-------

add_slave
    add_slave

remove_slave
    remove_slave

groups
    sysfs group

.. _`w1_family`:

struct w1_family
================

.. c:type:: struct w1_family

    reference counted family structure.

.. _`w1_family.definition`:

Definition
----------

.. code-block:: c

    struct w1_family {
        struct list_head family_entry;
        u8 fid;
        struct w1_family_ops *fops;
        atomic_t refcnt;
    }

.. _`w1_family.members`:

Members
-------

family_entry
    family linked list

fid
    8 bit family identifier

fops
    operations for this family

refcnt
    reference counter

.. This file was automatic generated / don't edit.

