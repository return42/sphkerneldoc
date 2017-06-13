.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwtracing/coresight/coresight-priv.h

.. _`cs_buffers`:

struct cs_buffers
=================

.. c:type:: struct cs_buffers

    keep track of a recording session' specifics

.. _`cs_buffers.definition`:

Definition
----------

.. code-block:: c

    struct cs_buffers {
        unsigned int cur;
        unsigned int nr_pages;
        unsigned long offset;
        local_t data_size;
        bool snapshot;
        void **data_pages;
    }

.. _`cs_buffers.members`:

Members
-------

cur
    index of the current buffer

nr_pages
    max number of pages granted to us

offset
    offset within the current buffer

data_size
    how much we collected in this run

snapshot
    is this run in snapshot mode

data_pages
    a handle the ring buffer

.. This file was automatic generated / don't edit.

