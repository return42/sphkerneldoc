.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/policy_ns.c

.. _`aa_ns_visible`:

aa_ns_visible
=============

.. c:function:: bool aa_ns_visible(struct aa_ns *curr, struct aa_ns *view, bool subns)

    test if \ ``view``\  is visible from \ ``curr``\ 

    :param curr:
        namespace to treat as the parent (NOT NULL)
    :type curr: struct aa_ns \*

    :param view:
        namespace to test if visible from \ ``curr``\  (NOT NULL)
    :type view: struct aa_ns \*

    :param subns:
        whether view of a subns is allowed
    :type subns: bool

.. _`aa_ns_visible.return`:

Return
------

true if \ ``view``\  is visible from \ ``curr``\  else false

.. _`aa_ns_name`:

aa_ns_name
==========

.. c:function:: const char *aa_ns_name(struct aa_ns *curr, struct aa_ns *view, bool subns)

    Find the ns name to display for \ ``view``\  from \ ``curr``\  \ ``curr``\  - current namespace (NOT NULL) \ ``view``\  - namespace attempting to view (NOT NULL) \ ``subns``\  - are subns visible

    :param curr:
        *undescribed*
    :type curr: struct aa_ns \*

    :param view:
        *undescribed*
    :type view: struct aa_ns \*

    :param subns:
        *undescribed*
    :type subns: bool

.. _`aa_ns_name.return`:

Return
------

name of \ ``view``\  visible from \ ``curr``\ 

.. _`alloc_ns`:

alloc_ns
========

.. c:function:: struct aa_ns *alloc_ns(const char *prefix, const char *name)

    allocate, initialize and return a new namespace

    :param prefix:
        parent namespace name (MAYBE NULL)
    :type prefix: const char \*

    :param name:
        a preallocated name  (NOT NULL)
    :type name: const char \*

.. _`alloc_ns.return`:

Return
------

refcounted namespace or NULL on failure.

.. _`aa_free_ns`:

aa_free_ns
==========

.. c:function:: void aa_free_ns(struct aa_ns *ns)

    free a profile namespace

    :param ns:
        the namespace to free  (MAYBE NULL)
    :type ns: struct aa_ns \*

.. _`aa_free_ns.requires`:

Requires
--------

All references to the namespace must have been put, if the
namespace was referenced by a profile confining a task,

.. _`aa_findn_ns`:

aa_findn_ns
===========

.. c:function:: struct aa_ns *aa_findn_ns(struct aa_ns *root, const char *name, size_t n)

    look up a profile namespace on the namespace list

    :param root:
        namespace to search in  (NOT NULL)
    :type root: struct aa_ns \*

    :param name:
        name of namespace to find  (NOT NULL)
    :type name: const char \*

    :param n:
        length of \ ``name``\ 
    :type n: size_t

.. _`aa_findn_ns.return`:

Return
------

a refcounted namespace on the list, or NULL if no namespace
called \ ``name``\  exists.

refcount released by caller

.. _`aa_find_ns`:

aa_find_ns
==========

.. c:function:: struct aa_ns *aa_find_ns(struct aa_ns *root, const char *name)

    look up a profile namespace on the namespace list

    :param root:
        namespace to search in  (NOT NULL)
    :type root: struct aa_ns \*

    :param name:
        name of namespace to find  (NOT NULL)
    :type name: const char \*

.. _`aa_find_ns.return`:

Return
------

a refcounted namespace on the list, or NULL if no namespace
called \ ``name``\  exists.

refcount released by caller

.. _`__aa_lookupn_ns`:

\__aa_lookupn_ns
================

.. c:function:: struct aa_ns *__aa_lookupn_ns(struct aa_ns *view, const char *hname, size_t n)

    lookup the namespace matching \ ``hname``\ 

    :param view:
        *undescribed*
    :type view: struct aa_ns \*

    :param hname:
        hierarchical ns name  (NOT NULL)
    :type hname: const char \*

    :param n:
        length of \ ``hname``\ 
    :type n: size_t

.. _`__aa_lookupn_ns.requires`:

Requires
--------

rcu_read_lock be held

.. _`__aa_lookupn_ns.return`:

Return
------

unrefcounted ns pointer or NULL if not found

Do a relative name lookup, recursing through profile tree.

.. _`aa_lookupn_ns`:

aa_lookupn_ns
=============

.. c:function:: struct aa_ns *aa_lookupn_ns(struct aa_ns *view, const char *name, size_t n)

    look up a policy namespace relative to \ ``view``\ 

    :param view:
        namespace to search in  (NOT NULL)
    :type view: struct aa_ns \*

    :param name:
        name of namespace to find  (NOT NULL)
    :type name: const char \*

    :param n:
        length of \ ``name``\ 
    :type n: size_t

.. _`aa_lookupn_ns.return`:

Return
------

a refcounted namespace on the list, or NULL if no namespace
called \ ``name``\  exists.

refcount released by caller

.. _`__aa_find_or_create_ns`:

\__aa_find_or_create_ns
=======================

.. c:function:: struct aa_ns *__aa_find_or_create_ns(struct aa_ns *parent, const char *name, struct dentry *dir)

    create an ns, fail if it already exists

    :param parent:
        the parent of the namespace being created
    :type parent: struct aa_ns \*

    :param name:
        the name of the namespace
    :type name: const char \*

    :param dir:
        if not null the dir to put the ns entries in
    :type dir: struct dentry \*

.. _`__aa_find_or_create_ns.return`:

Return
------

the a refcounted ns that has been add or an ERR_PTR

.. _`aa_prepare_ns`:

aa_prepare_ns
=============

.. c:function:: struct aa_ns *aa_prepare_ns(struct aa_ns *parent, const char *name)

    find an existing or create a new namespace of \ ``name``\ 

    :param parent:
        ns to treat as parent
    :type parent: struct aa_ns \*

    :param name:
        the namespace to find or add  (NOT NULL)
    :type name: const char \*

.. _`aa_prepare_ns.return`:

Return
------

refcounted namespace or PTR_ERR if failed to create one

.. _`destroy_ns`:

destroy_ns
==========

.. c:function:: void destroy_ns(struct aa_ns *ns)

    remove everything contained by \ ``ns``\ 

    :param ns:
        namespace to have it contents removed  (NOT NULL)
    :type ns: struct aa_ns \*

.. _`__aa_remove_ns`:

\__aa_remove_ns
===============

.. c:function:: void __aa_remove_ns(struct aa_ns *ns)

    remove a namespace and all its children

    :param ns:
        namespace to be removed  (NOT NULL)
    :type ns: struct aa_ns \*

.. _`__aa_remove_ns.requires`:

Requires
--------

ns->parent->lock be held and ns removed from parent.

.. _`__ns_list_release`:

\__ns_list_release
==================

.. c:function:: void __ns_list_release(struct list_head *head)

    remove all profile namespaces on the list put refs

    :param head:
        list of profile namespaces  (NOT NULL)
    :type head: struct list_head \*

.. _`__ns_list_release.requires`:

Requires
--------

namespace lock be held

.. _`aa_alloc_root_ns`:

aa_alloc_root_ns
================

.. c:function:: int aa_alloc_root_ns( void)

    allocate the root profile namespace

    :param void:
        no arguments
    :type void: 

.. _`aa_alloc_root_ns.return`:

Return
------

\ ``0``\  on success else error

.. This file was automatic generated / don't edit.

