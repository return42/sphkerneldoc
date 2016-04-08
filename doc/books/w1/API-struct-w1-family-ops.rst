
.. _API-struct-w1-family-ops:

====================
struct w1_family_ops
====================

*man struct w1_family_ops(9)*

*4.6.0-rc1*

operations for a family type


Synopsis
========

.. code-block:: c

    struct w1_family_ops {
      int (* add_slave) (struct w1_slave *);
      void (* remove_slave) (struct w1_slave *);
      const struct attribute_group ** groups;
    };


Members
=======

add_slave
    add_slave

remove_slave
    remove_slave

groups
    sysfs group
