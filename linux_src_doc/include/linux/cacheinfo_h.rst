.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/cacheinfo.h

.. _`cacheinfo`:

struct cacheinfo
================

.. c:type:: struct cacheinfo

    represent a cache leaf node

.. _`cacheinfo.definition`:

Definition
----------

.. code-block:: c

    struct cacheinfo {
        unsigned int id;
        enum cache_type type;
        unsigned int level;
        unsigned int coherency_line_size;
        unsigned int number_of_sets;
        unsigned int ways_of_associativity;
        unsigned int physical_line_partition;
        unsigned int size;
        cpumask_t shared_cpu_map;
        unsigned int attributes;
    #define CACHE_WRITE_THROUGH BIT(0)
    #define CACHE_WRITE_BACK BIT(1)
    #define CACHE_WRITE_POLICY_MASK \
        (CACHE_WRITE_THROUGH | CACHE_WRITE_BACK)#define CACHE_READ_ALLOCATE BIT2;
    #define CACHE_WRITE_ALLOCATE BIT(3)
    #define CACHE_ALLOCATE_POLICY_MASK \
        (CACHE_READ_ALLOCATE | CACHE_WRITE_ALLOCATE)#define CACHE_ID BIT4;
        struct device_node *of_node;
        bool disable_sysfs;
        void *priv;
    }

.. _`cacheinfo.members`:

Members
-------

id
    This cache's id. It is unique among caches with the same (type, level).

type
    type of the cache - data, inst or unified

level
    represents the hierarchy in the multi-level cache

coherency_line_size
    size of each cache line usually representing
    the minimum amount of data that gets transferred from memory

number_of_sets
    total number of sets, a set is a collection of cache
    lines sharing the same index

ways_of_associativity
    number of ways in which a particular memory
    block can be placed in the cache

physical_line_partition
    number of physical cache lines sharing the
    same cachetag

size
    Total size of the cache

shared_cpu_map
    logical cpumask representing all the cpus sharing
    this cache node

attributes
    bitfield representing various cache attributes

BIT2
    *undescribed*

BIT4
    *undescribed*

of_node
    if devicetree is used, this represents either the cpu node in
    case there's no explicit cache node or the cache node itself in the
    device tree

disable_sysfs
    indicates whether this node is visible to the user via
    sysfs or not

priv
    pointer to any private data structure specific to particular
    cache design

.. _`cacheinfo.description`:

Description
-----------

While \ ``of_node``\ , \ ``disable_sysfs``\  and \ ``priv``\  are used for internal book
keeping, the remaining members form the core properties of the cache

.. This file was automatic generated / don't edit.

