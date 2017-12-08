.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/livepatch/shadow.c

.. _`shadow-variable-api-concurrency-notes-`:

Shadow variable API concurrency notes:
======================================

The shadow variable API provides a simple relationship between an
<obj, id> pair and a pointer value.  It is the responsibility of the
caller to provide any mutual exclusion required of the shadow data.

Once a shadow variable is attached to its parent object via the
klp_shadow\_\*alloc() API calls, it is considered live: any subsequent
call to \ :c:func:`klp_shadow_get`\  may then return the shadow variable's data
pointer.  Callers of klp_shadow\_\*alloc() should prepare shadow data
accordingly.

The klp_shadow\_\*alloc() API calls may allocate memory for new shadow
variable structures.  Their implementation does not call kmalloc
inside any spinlocks, but API callers should pass GFP flags according
to their specific needs.

The klp_shadow_hash is an RCU-enabled hashtable and is safe against
concurrent \ :c:func:`klp_shadow_free`\  and \ :c:func:`klp_shadow_get`\  operations.

.. _`klp_shadow`:

struct klp_shadow
=================

.. c:type:: struct klp_shadow

    shadow variable structure

.. _`klp_shadow.definition`:

Definition
----------

.. code-block:: c

    struct klp_shadow {
        struct hlist_node node;
        struct rcu_head rcu_head;
        void *obj;
        unsigned long id;
        char data[];
    }

.. _`klp_shadow.members`:

Members
-------

node
    klp_shadow_hash hash table node

rcu_head
    RCU is used to safely free this structure

obj
    pointer to parent object

id
    data identifier

data
    data area

.. _`klp_shadow_match`:

klp_shadow_match
================

.. c:function:: bool klp_shadow_match(struct klp_shadow *shadow, void *obj, unsigned long id)

    verify a shadow variable matches given <obj, id>

    :param struct klp_shadow \*shadow:
        shadow variable to match

    :param void \*obj:
        pointer to parent object

    :param unsigned long id:
        data identifier

.. _`klp_shadow_match.return`:

Return
------

true if the shadow variable matches.

.. _`klp_shadow_get`:

klp_shadow_get
==============

.. c:function:: void *klp_shadow_get(void *obj, unsigned long id)

    retrieve a shadow variable data pointer

    :param void \*obj:
        pointer to parent object

    :param unsigned long id:
        data identifier

.. _`klp_shadow_get.return`:

Return
------

the shadow variable data element, NULL on failure.

.. _`klp_shadow_alloc`:

klp_shadow_alloc
================

.. c:function:: void *klp_shadow_alloc(void *obj, unsigned long id, void *data, size_t size, gfp_t gfp_flags)

    allocate and add a new shadow variable

    :param void \*obj:
        pointer to parent object

    :param unsigned long id:
        data identifier

    :param void \*data:
        pointer to data to attach to parent

    :param size_t size:
        size of attached data

    :param gfp_t gfp_flags:
        GFP mask for allocation

.. _`klp_shadow_alloc.description`:

Description
-----------

Allocates \ ``size``\  bytes for new shadow variable data using \ ``gfp_flags``\ 
and copies \ ``size``\  bytes from \ ``data``\  into the new shadow variable's own
data space.  If \ ``data``\  is NULL, \ ``size``\  bytes are still allocated, but
no copy is performed.  The new shadow variable is then added to the
global hashtable.

If an existing <obj, id> shadow variable can be found, this routine
will issue a WARN, exit early and return NULL.

.. _`klp_shadow_alloc.return`:

Return
------

the shadow variable data element, NULL on duplicate or
failure.

.. _`klp_shadow_get_or_alloc`:

klp_shadow_get_or_alloc
=======================

.. c:function:: void *klp_shadow_get_or_alloc(void *obj, unsigned long id, void *data, size_t size, gfp_t gfp_flags)

    get existing or allocate a new shadow variable

    :param void \*obj:
        pointer to parent object

    :param unsigned long id:
        data identifier

    :param void \*data:
        pointer to data to attach to parent

    :param size_t size:
        size of attached data

    :param gfp_t gfp_flags:
        GFP mask for allocation

.. _`klp_shadow_get_or_alloc.description`:

Description
-----------

Returns a pointer to existing shadow data if an <obj, id> shadow
variable is already present.  Otherwise, it creates a new shadow
variable like \ :c:func:`klp_shadow_alloc`\ .

This function guarantees that only one shadow variable exists with
the given \ ``id``\  for the given \ ``obj``\ .  It also guarantees that the shadow
variable will be initialized by the given \ ``data``\  only when it did not
exist before.

.. _`klp_shadow_get_or_alloc.return`:

Return
------

the shadow variable data element, NULL on failure.

.. _`klp_shadow_free`:

klp_shadow_free
===============

.. c:function:: void klp_shadow_free(void *obj, unsigned long id)

    detach and free a <obj, id> shadow variable

    :param void \*obj:
        pointer to parent object

    :param unsigned long id:
        data identifier

.. _`klp_shadow_free.description`:

Description
-----------

This function releases the memory for this <obj, id> shadow variable
instance, callers should stop referencing it accordingly.

.. _`klp_shadow_free_all`:

klp_shadow_free_all
===================

.. c:function:: void klp_shadow_free_all(unsigned long id)

    detach and free all <\*, id> shadow variables

    :param unsigned long id:
        data identifier

.. _`klp_shadow_free_all.description`:

Description
-----------

This function releases the memory for all <\*, id> shadow variable
instances, callers should stop referencing them accordingly.

.. This file was automatic generated / don't edit.

