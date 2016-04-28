.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-w1-master:

================
struct w1_master
================

*man struct w1_master(9)*

*4.6.0-rc5*

one per bus master


Synopsis
========

.. code-block:: c

    struct w1_master {
      struct list_head w1_master_entry;
      struct module * owner;
      unsigned char name[W1_MAXNAMELEN];
      struct mutex list_mutex;
      struct list_head slist;
      struct list_head async_list;
      int max_slave_count;
      int slave_count;
      unsigned long attempts;
      int slave_ttl;
      int initialized;
      u32 id;
      int search_count;
      u64 search_id;
      atomic_t refcnt;
      void * priv;
      int enable_pullup;
      int pullup_duration;
      long flags;
      struct task_struct * thread;
      struct mutex mutex;
      struct mutex bus_mutex;
      struct device_driver * driver;
      struct device dev;
      struct w1_bus_master * bus_master;
      u32 seq;
    };


Members
=======

w1_master_entry
    master linked list

owner
    module owner

name[W1_MAXNAMELEN]
    dynamically allocate bus name

list_mutex
    protect slist and async_list

slist
    linked list of slaves

async_list
    linked list of netlink commands to execute

max_slave_count
    maximum number of slaves to search for at a time

slave_count
    current number of slaves known

attempts
    number of searches ran

slave_ttl
    number of searches before a slave is timed out

initialized
    prevent init/removal race conditions

id
    w1 bus number

search_count
    number of automatic searches to run, -1 unlimited

search_id
    allows continuing a search

refcnt
    reference count

priv
    private data storage

enable_pullup
    allows a strong pullup

pullup_duration
    time for the next strong pullup

flags
    one of w1_master_flags

thread
    thread for bus search and netlink commands

mutex
    protect most of w1_master

bus_mutex
    pretect concurrent bus access

driver
    sysfs driver

dev
    sysfs device

bus_master
    io operations available

seq
    sequence number used for netlink broadcasts


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
