.. -*- coding: utf-8; mode: rst -*-

===========
w1_family.h
===========

.. _`w1_family_ops`:

struct w1_family_ops
====================

.. c:type:: struct w1_family_ops

    operations for a family type



Definition
----------

.. code-block:: c

  struct w1_family_ops {
    int (* add_slave) (struct w1_slave *);
    void (* remove_slave) (struct w1_slave *);
    const struct attribute_group ** groups;
  };



Members
-------

:``add_slave``:
    add_slave

:``remove_slave``:
    remove_slave

:``groups``:
    sysfs group



.. _`w1_family`:

struct w1_family
================

.. c:type:: struct w1_family

    reference counted family structure.



Definition
----------

.. code-block:: c

  struct w1_family {
    struct list_head family_entry;
    u8 fid;
    struct w1_family_ops * fops;
    atomic_t refcnt;
  };



Members
-------

:``family_entry``:
    family linked list

:``fid``:
    8 bit family identifier

:``fops``:
    operations for this family

:``refcnt``:
    reference counter


