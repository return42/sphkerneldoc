
.. _API-struct-w1-slave:

===============
struct w1_slave
===============

*man struct w1_slave(9)*

*4.6.0-rc1*

holds a single slave device on the bus


Synopsis
========

.. code-block:: c

    struct w1_slave {
      struct module * owner;
      unsigned char name[W1_MAXNAMELEN];
      struct list_head w1_slave_entry;
      struct w1_reg_num reg_num;
      atomic_t refcnt;
      int ttl;
      unsigned long flags;
      struct w1_master * master;
      struct w1_family * family;
      void * family_data;
      struct device dev;
    };


Members
=======

owner
    Points to the one wire “wire” kernel module.

name[W1_MAXNAMELEN]
    Device id is ascii.

w1_slave_entry
    data for the linked list

reg_num
    the slave id in binary

refcnt
    reference count, delete when 0

ttl
    decrement per search this slave isn't found, deatch at 0

flags
    bit flags for W1_SLAVE_ACTIVE W1_SLAVE_DETACH

master
    bus which this slave is on

family
    module for device family type

family_data
    pointer for use by the family module

dev
    kernel device identifier
