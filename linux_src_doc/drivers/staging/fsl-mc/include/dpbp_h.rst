.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-mc/include/dpbp.h

.. _`dpbp_attr`:

struct dpbp_attr
================

.. c:type:: struct dpbp_attr

    Structure representing DPBP attributes

.. _`dpbp_attr.definition`:

Definition
----------

.. code-block:: c

    struct dpbp_attr {
        int id;
        u16 bpid;
    }

.. _`dpbp_attr.members`:

Members
-------

id
    DPBP object ID

bpid
    Hardware buffer pool ID; should be used as an argument in
    acquire/release operations on buffers

.. This file was automatic generated / don't edit.

