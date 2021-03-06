.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/include/match.h

.. _`yyth_magic`:

YYTH_MAGIC
==========

.. c:function::  YYTH_MAGIC()

    file format (--tables-file option; see Table File Format in the flex info pages and the flex sources for documentation). The magic number used in the header is 0x1B5E783D instead of 0xF13C57B1 though, because new tables have been defined and others YY_ID_CHK (check) and YY_ID_DEF (default) tables are used slightly differently (see the apparmor-parser package).

.. _`yyth_magic.description`:

Description
-----------


The data in the packed dfa is stored in network byte order, and the tables
are arranged for flexibility.  We convert the table data to host native
byte order.

The dfa begins with a table set header, and is followed by the actual
tables.

.. _`aa_get_dfa`:

aa_get_dfa
==========

.. c:function:: struct aa_dfa *aa_get_dfa(struct aa_dfa *dfa)

    increment refcount on dfa \ ``p``\ 

    :param dfa:
        dfa  (MAYBE NULL)
    :type dfa: struct aa_dfa \*

.. _`aa_get_dfa.return`:

Return
------

pointer to \ ``dfa``\  if \ ``dfa``\  is NULL will return NULL

.. _`aa_get_dfa.requires`:

Requires
--------

\ ``dfa``\  must be held with valid refcount when called

.. _`aa_put_dfa`:

aa_put_dfa
==========

.. c:function:: void aa_put_dfa(struct aa_dfa *dfa)

    put a dfa refcount

    :param dfa:
        dfa to put refcount   (MAYBE NULL)
    :type dfa: struct aa_dfa \*

.. _`aa_put_dfa.requires`:

Requires
--------

if \ ``dfa``\  != NULL that a valid refcount be held

.. This file was automatic generated / don't edit.

