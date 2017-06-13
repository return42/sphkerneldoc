.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/of/of_private.h

.. _`alias_prop`:

struct alias_prop
=================

.. c:type:: struct alias_prop

    Alias property in 'aliases' node

.. _`alias_prop.definition`:

Definition
----------

.. code-block:: c

    struct alias_prop {
        struct list_head link;
        const char *alias;
        struct device_node *np;
        int id;
        char stem;
    }

.. _`alias_prop.members`:

Members
-------

link
    List node to link the structure in aliases_lookup list

alias
    Alias property name

np
    Pointer to device_node that the alias stands for

id
    Index value from end of alias name

stem
    Alias string without the index

.. _`alias_prop.description`:

Description
-----------

The structure represents one alias property of 'aliases' node as
an entry in aliases_lookup list.

.. _`__of_prop_dup`:

__of_prop_dup
=============

.. c:function:: struct property *__of_prop_dup(const struct property *prop, gfp_t allocflags)

    :param const struct property \*prop:
        *undescribed*

    :param gfp_t allocflags:
        *undescribed*

.. _`__of_prop_dup.description`:

Description
-----------

All functions with two leading underscores operate
without taking node references, so you either have to
own the devtree lock or work on detached trees only.

.. This file was automatic generated / don't edit.

