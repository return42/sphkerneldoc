.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/rc-map.h

.. _`rc_map_table`:

struct rc_map_table
===================

.. c:type:: struct rc_map_table

    represents a scancode/keycode pair

.. _`rc_map_table.definition`:

Definition
----------

.. code-block:: c

    struct rc_map_table {
        u32 scancode;
        u32 keycode;
    }

.. _`rc_map_table.members`:

Members
-------

scancode
    scan code (u32)

keycode
    Linux input keycode

.. _`rc_map`:

struct rc_map
=============

.. c:type:: struct rc_map

    represents a keycode map table

.. _`rc_map.definition`:

Definition
----------

.. code-block:: c

    struct rc_map {
        struct rc_map_table *scan;
        unsigned int size;
        unsigned int len;
        unsigned int alloc;
        enum rc_proto rc_proto;
        const char *name;
        spinlock_t lock;
    }

.. _`rc_map.members`:

Members
-------

scan
    pointer to struct \ :c:type:`struct rc_map_table <rc_map_table>`\ 

size
    Max number of entries

len
    Number of entries that are in use

alloc
    size of \*scan, in bytes

rc_proto
    type of the remote controller protocol, as defined at
    enum \ :c:type:`struct rc_proto <rc_proto>`\ 

name
    name of the key map table

lock
    lock to protect access to this structure

.. _`rc_map_list`:

struct rc_map_list
==================

.. c:type:: struct rc_map_list

    list of the registered \ :c:type:`struct rc_map <rc_map>`\  maps

.. _`rc_map_list.definition`:

Definition
----------

.. code-block:: c

    struct rc_map_list {
        struct list_head list;
        struct rc_map map;
    }

.. _`rc_map_list.members`:

Members
-------

list
    pointer to struct \ :c:type:`struct list_head <list_head>`\ 

map
    pointer to struct \ :c:type:`struct rc_map <rc_map>`\ 

.. _`rc_map_register`:

rc_map_register
===============

.. c:function:: int rc_map_register(struct rc_map_list *map)

    Registers a Remote Controler scancode map

    :param map:
        pointer to struct rc_map_list
    :type map: struct rc_map_list \*

.. _`rc_map_unregister`:

rc_map_unregister
=================

.. c:function:: void rc_map_unregister(struct rc_map_list *map)

    Unregisters a Remote Controler scancode map

    :param map:
        pointer to struct rc_map_list
    :type map: struct rc_map_list \*

.. _`rc_map_get`:

rc_map_get
==========

.. c:function:: struct rc_map *rc_map_get(const char *name)

    gets an RC map from its name

    :param name:
        name of the RC scancode map
    :type name: const char \*

.. This file was automatic generated / don't edit.

