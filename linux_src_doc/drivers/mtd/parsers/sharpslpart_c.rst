.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/parsers/sharpslpart.c

.. _`sharpsl_ftl`:

struct sharpsl_ftl
==================

.. c:type:: struct sharpsl_ftl

    Sharp FTL Logical Table

.. _`sharpsl_ftl.definition`:

Definition
----------

.. code-block:: c

    struct sharpsl_ftl {
        unsigned int logmax;
        unsigned int *log2phy;
    }

.. _`sharpsl_ftl.members`:

Members
-------

logmax
    number of logical blocks

log2phy
    the logical-to-physical table

.. _`sharpsl_ftl.description`:

Description
-----------

Structure containing the logical-to-physical translation table
used by the SHARP SL FTL.

.. This file was automatic generated / don't edit.

