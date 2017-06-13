.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/rc-map.h

.. _`rc_type`:

enum rc_type
============

.. c:type:: enum rc_type

    type of the Remote Controller protocol

.. _`rc_type.definition`:

Definition
----------

.. code-block:: c

    enum rc_type {
        RC_TYPE_UNKNOWN,
        RC_TYPE_OTHER,
        RC_TYPE_RC5,
        RC_TYPE_RC5X_20,
        RC_TYPE_RC5_SZ,
        RC_TYPE_JVC,
        RC_TYPE_SONY12,
        RC_TYPE_SONY15,
        RC_TYPE_SONY20,
        RC_TYPE_NEC,
        RC_TYPE_NECX,
        RC_TYPE_NEC32,
        RC_TYPE_SANYO,
        RC_TYPE_MCIR2_KBD,
        RC_TYPE_MCIR2_MSE,
        RC_TYPE_RC6_0,
        RC_TYPE_RC6_6A_20,
        RC_TYPE_RC6_6A_24,
        RC_TYPE_RC6_6A_32,
        RC_TYPE_RC6_MCE,
        RC_TYPE_SHARP,
        RC_TYPE_XMP,
        RC_TYPE_CEC
    };

.. _`rc_type.constants`:

Constants
---------

RC_TYPE_UNKNOWN
    Protocol not known

RC_TYPE_OTHER
    Protocol known but proprietary

RC_TYPE_RC5
    Philips RC5 protocol

RC_TYPE_RC5X_20
    Philips RC5x 20 bit protocol

RC_TYPE_RC5_SZ
    StreamZap variant of RC5

RC_TYPE_JVC
    JVC protocol

RC_TYPE_SONY12
    Sony 12 bit protocol

RC_TYPE_SONY15
    Sony 15 bit protocol

RC_TYPE_SONY20
    Sony 20 bit protocol

RC_TYPE_NEC
    NEC protocol

RC_TYPE_NECX
    Extended NEC protocol

RC_TYPE_NEC32
    NEC 32 bit protocol

RC_TYPE_SANYO
    Sanyo protocol

RC_TYPE_MCIR2_KBD
    RC6-ish MCE keyboard

RC_TYPE_MCIR2_MSE
    RC6-ish MCE mouse

RC_TYPE_RC6_0
    Philips RC6-0-16 protocol

RC_TYPE_RC6_6A_20
    Philips RC6-6A-20 protocol

RC_TYPE_RC6_6A_24
    Philips RC6-6A-24 protocol

RC_TYPE_RC6_6A_32
    Philips RC6-6A-32 protocol

RC_TYPE_RC6_MCE
    MCE (Philips RC6-6A-32 subtype) protocol

RC_TYPE_SHARP
    Sharp protocol

RC_TYPE_XMP
    XMP protocol

RC_TYPE_CEC
    CEC protocol

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
        enum rc_type rc_type;
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

rc_type
    type of the remote controller protocol, as defined at
    enum \ :c:type:`struct rc_type <rc_type>`\ 

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

    :param struct rc_map_list \*map:
        pointer to struct rc_map_list

.. _`rc_map_unregister`:

rc_map_unregister
=================

.. c:function:: void rc_map_unregister(struct rc_map_list *map)

    Unregisters a Remote Controler scancode map

    :param struct rc_map_list \*map:
        pointer to struct rc_map_list

.. _`rc_map_get`:

rc_map_get
==========

.. c:function:: struct rc_map *rc_map_get(const char *name)

    gets an RC map from its name

    :param const char \*name:
        name of the RC scancode map

.. This file was automatic generated / don't edit.

