.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/kmsg_dump.h

.. _`kmsg_dumper`:

struct kmsg_dumper
==================

.. c:type:: struct kmsg_dumper

    kernel crash message dumper structure

.. _`kmsg_dumper.definition`:

Definition
----------

.. code-block:: c

    struct kmsg_dumper {
        struct list_head list;
        void (* dump) (struct kmsg_dumper *dumper, enum kmsg_dump_reason reason);
        enum kmsg_dump_reason max_reason;
        bool active;
        bool registered;
        u32 cur_idx;
        u32 next_idx;
        u64 cur_seq;
        u64 next_seq;
    }

.. _`kmsg_dumper.members`:

Members
-------

list
    Entry in the dumper list (private)

dump
    Call into dumping code which will retrieve the data with
    through the record iterator

max_reason
    filter for highest reason number that should be dumped

active
    *undescribed*

registered
    Flag that specifies if this is already registered

cur_idx
    *undescribed*

next_idx
    *undescribed*

cur_seq
    *undescribed*

next_seq
    *undescribed*

.. This file was automatic generated / don't edit.

