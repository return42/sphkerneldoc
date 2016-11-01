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

.. _`module_w1_family`:

module_w1_family
================

.. c:function::  module_w1_family( __w1_family)

    Helper macro for registering a 1-Wire families

    :param  __w1_family:
        w1_family struct

.. _`module_w1_family.description`:

Description
-----------

Helper macro for 1-Wire families which do not do anything special in module
init/exit. This eliminates a lot of boilerplate. Each module may only
use this macro once, and calling it replaces \ :c:func:`module_init`\  and \ :c:func:`module_exit`\ 

.. This file was automatic generated / don't edit.

