.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/call-path.h

.. _`call_path`:

struct call_path
================

.. c:type:: struct call_path

    node in list of calls leading to a function call.

.. _`call_path.definition`:

Definition
----------

.. code-block:: c

    struct call_path {
        struct call_path *parent;
        struct symbol *sym;
        u64 ip;
        u64 db_id;
        bool in_kernel;
        struct rb_node rb_node;
        struct rb_root children;
    }

.. _`call_path.members`:

Members
-------

parent
    call path to the parent function call

sym
    symbol of function called

ip
    only if sym is null, the ip of the function

db_id
    id used for db-export

in_kernel
    whether function is a in the kernel

rb_node
    node in parent's tree of called functions

children
    tree of call paths of functions called

.. _`call_path.description`:

Description
-----------

In combination with the call_return structure, the call_path structure
defines a context-sensitve call-graph.

.. _`call_path_root`:

struct call_path_root
=====================

.. c:type:: struct call_path_root

    root of all call paths.

.. _`call_path_root.definition`:

Definition
----------

.. code-block:: c

    struct call_path_root {
        struct call_path call_path;
        struct list_head blocks;
        size_t next;
        size_t sz;
    }

.. _`call_path_root.members`:

Members
-------

call_path
    root call path

blocks
    list of blocks to store call paths

next
    next free space

sz
    number of spaces

.. This file was automatic generated / don't edit.

