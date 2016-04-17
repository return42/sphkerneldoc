.. -*- coding: utf-8; mode: rst -*-

===========
kmsg_dump.h
===========


.. _`kmsg_dumper`:

struct kmsg_dumper
==================

.. c:type:: kmsg_dumper

    kernel crash message dumper structure


.. _`kmsg_dumper.definition`:

Definition
----------

.. code-block:: c

  struct kmsg_dumper {
    struct list_head list;
    void (* dump) (struct kmsg_dumper *dumper, enum kmsg_dump_reason reason);
    enum kmsg_dump_reason max_reason;
    bool registered;
  };


.. _`kmsg_dumper.members`:

Members
-------

:``list``:
    Entry in the dumper list (private)

:``dump``:
    Call into dumping code which will retrieve the data with
    through the record iterator

:``max_reason``:
    filter for highest reason number that should be dumped

:``registered``:
    Flag that specifies if this is already registered


