.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/tipc/name_distr.h

.. _`distr_item`:

struct distr_item
=================

.. c:type:: struct distr_item

    publication info distributed to other nodes

.. _`distr_item.definition`:

Definition
----------

.. code-block:: c

    struct distr_item {
        __be32 type;
        __be32 lower;
        __be32 upper;
        __be32 ref;
        __be32 key;
    }

.. _`distr_item.members`:

Members
-------

type
    name sequence type

lower
    name sequence lower bound

upper
    name sequence upper bound

ref
    publishing port reference

key
    publication key

.. _`distr_item.description`:

Description
-----------

===> All fields are stored in network byte order. <===

First 3 fields identify (name or) name sequence being published.
Reference field uniquely identifies port that published name sequence.
Key field uniquely identifies publication, in the event a port has
multiple publications of the same name sequence.

.. _`distr_item.note`:

Note
----

There is no field that identifies the publishing node because it is
the same for all items contained within a publication message.

.. This file was automatic generated / don't edit.

