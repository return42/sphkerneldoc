.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/plist.h

.. _`plist_head_init`:

PLIST_HEAD_INIT
===============

.. c:function::  PLIST_HEAD_INIT( head)

    static struct plist_head initializer

    :param  head:
        struct plist_head variable name

.. _`plist_head`:

PLIST_HEAD
==========

.. c:function::  PLIST_HEAD( head)

    declare and init plist_head

    :param  head:
        name for struct plist_head variable

.. _`plist_node_init`:

PLIST_NODE_INIT
===============

.. c:function::  PLIST_NODE_INIT( node,  __prio)

    static struct plist_node initializer

    :param  node:
        struct plist_node variable name

    :param  __prio:
        initial node priority

.. _`plist_head_init`:

plist_head_init
===============

.. c:function:: void plist_head_init(struct plist_head *head)

    dynamic struct plist_head initializer

    :param struct plist_head \*head:
        \ :c:type:`struct plist_head <plist_head>`\  pointer

.. _`plist_node_init`:

plist_node_init
===============

.. c:function:: void plist_node_init(struct plist_node *node, int prio)

    Dynamic struct plist_node initializer

    :param struct plist_node \*node:
        \ :c:type:`struct plist_node <plist_node>`\  pointer

    :param int prio:
        initial node priority

.. _`plist_for_each`:

plist_for_each
==============

.. c:function::  plist_for_each( pos,  head)

    iterate over the plist

    :param  pos:
        the type \* to use as a loop counter

    :param  head:
        the head for your list

.. _`plist_for_each_continue`:

plist_for_each_continue
=======================

.. c:function::  plist_for_each_continue( pos,  head)

    continue iteration over the plist

    :param  pos:
        the type \* to use as a loop cursor

    :param  head:
        the head for your list

.. _`plist_for_each_continue.description`:

Description
-----------

Continue to iterate over plist, continuing after the current position.

.. _`plist_for_each_safe`:

plist_for_each_safe
===================

.. c:function::  plist_for_each_safe( pos,  n,  head)

    iterate safely over a plist of given type

    :param  pos:
        the type \* to use as a loop counter

    :param  n:
        another type \* to use as temporary storage

    :param  head:
        the head for your list

.. _`plist_for_each_safe.description`:

Description
-----------

Iterate over a plist of given type, safe against removal of list entry.

.. _`plist_for_each_entry`:

plist_for_each_entry
====================

.. c:function::  plist_for_each_entry( pos,  head,  mem)

    iterate over list of given type

    :param  pos:
        the type \* to use as a loop counter

    :param  head:
        the head for your list

    :param  mem:
        the name of the list_head within the struct

.. _`plist_for_each_entry_continue`:

plist_for_each_entry_continue
=============================

.. c:function::  plist_for_each_entry_continue( pos,  head,  m)

    continue iteration over list of given type

    :param  pos:
        the type \* to use as a loop cursor

    :param  head:
        the head for your list

    :param  m:
        the name of the list_head within the struct

.. _`plist_for_each_entry_continue.description`:

Description
-----------

Continue to iterate over list of given type, continuing after
the current position.

.. _`plist_for_each_entry_safe`:

plist_for_each_entry_safe
=========================

.. c:function::  plist_for_each_entry_safe( pos,  n,  head,  m)

    iterate safely over list of given type

    :param  pos:
        the type \* to use as a loop counter

    :param  n:
        another type \* to use as temporary storage

    :param  head:
        the head for your list

    :param  m:
        the name of the list_head within the struct

.. _`plist_for_each_entry_safe.description`:

Description
-----------

Iterate over list of given type, safe against removal of list entry.

.. _`plist_head_empty`:

plist_head_empty
================

.. c:function:: int plist_head_empty(const struct plist_head *head)

    return !0 if a plist_head is empty

    :param const struct plist_head \*head:
        \ :c:type:`struct plist_head <plist_head>`\  pointer

.. _`plist_node_empty`:

plist_node_empty
================

.. c:function:: int plist_node_empty(const struct plist_node *node)

    return !0 if plist_node is not on a list

    :param const struct plist_node \*node:
        \ :c:type:`struct plist_node <plist_node>`\  pointer

.. _`plist_first_entry`:

plist_first_entry
=================

.. c:function::  plist_first_entry( head,  type,  member)

    get the struct for the first entry

    :param  head:
        the \ :c:type:`struct plist_head <plist_head>`\  pointer

    :param  type:
        the type of the struct this is embedded in

    :param  member:
        the name of the list_head within the struct

.. _`plist_last_entry`:

plist_last_entry
================

.. c:function::  plist_last_entry( head,  type,  member)

    get the struct for the last entry

    :param  head:
        the \ :c:type:`struct plist_head <plist_head>`\  pointer

    :param  type:
        the type of the struct this is embedded in

    :param  member:
        the name of the list_head within the struct

.. _`plist_next`:

plist_next
==========

.. c:function::  plist_next( pos)

    get the next entry in list

    :param  pos:
        the type \* to cursor

.. _`plist_prev`:

plist_prev
==========

.. c:function::  plist_prev( pos)

    get the prev entry in list

    :param  pos:
        the type \* to cursor

.. _`plist_first`:

plist_first
===========

.. c:function:: struct plist_node *plist_first(const struct plist_head *head)

    return the first node (and thus, highest priority)

    :param const struct plist_head \*head:
        the \ :c:type:`struct plist_head <plist_head>`\  pointer

.. _`plist_first.description`:

Description
-----------

Assumes the plist is \_not\_ empty.

.. _`plist_last`:

plist_last
==========

.. c:function:: struct plist_node *plist_last(const struct plist_head *head)

    return the last node (and thus, lowest priority)

    :param const struct plist_head \*head:
        the \ :c:type:`struct plist_head <plist_head>`\  pointer

.. _`plist_last.description`:

Description
-----------

Assumes the plist is \_not\_ empty.

.. This file was automatic generated / don't edit.

