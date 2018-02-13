.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/apparmor/policy_ns.c

.. _`aa_ns_visible`:

aa_ns_visible
=============

.. c:function:: bool aa_ns_visible(struct aa_ns *curr, struct aa_ns *view, bool subns)

    test if \ ``view``\  is visible from \ ``curr``\ 

    :param struct aa_ns \*curr:
        namespace to treat as the parent (NOT NULL)

    :param struct aa_ns \*view:
        namespace to test if visible from \ ``curr``\  (NOT NULL)

    :param bool subns:
        whether view of a subns is allowed

.. _`aa_ns_visible.return`:

Return
------

true if \ ``view``\  is visible from \ ``curr``\  else false

.. _`aa_ns_name`:

aa_ns_name
==========

.. c:function:: const char *aa_ns_name(struct aa_ns *curr, struct aa_ns *view, bool subns)

    Find the ns name to display for \ ``view``\  from \ ``curr``\  \ ``curr``\  - current namespace (NOT NULL) \ ``view``\  - namespace attempting to view (NOT NULL) \ ``subns``\  - are subns visible

    :param struct aa_ns \*curr:
        *undescribed*

    :param struct aa_ns \*view:
        *undescribed*

    :param bool subns:
        *undescribed*

.. _`aa_ns_name.return`:

Return
------

name of \ ``view``\  visible from \ ``curr``\ 

.. _`alloc_ns`:

alloc_ns
========

.. c:function:: struct aa_ns *alloc_ns(const char *prefix, const char *name)

    allocate, initialize and return a new namespace

    :param const char \*prefix:
        parent namespace name (MAYBE NULL)

    :param const char \*name:
        a preallocated name  (NOT NULL)

.. _`alloc_ns.return`:

Return
------

refcounted namespace or NULL on failure.

.. _`aa_free_ns`:

aa_free_ns
==========

.. c:function:: void aa_free_ns(struct aa_ns *ns)

    free a profile namespace

    :param struct aa_ns \*ns:
        the namespace to free  (MAYBE NULL)

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

    :param struct aa_ns \*root:
        namespace to search in  (NOT NULL)

    :param const char \*name:
        name of namespace to find  (NOT NULL)

    :param size_t n:
        length of \ ``name``\ 

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

    :param struct aa_ns \*root:
        namespace to search in  (NOT NULL)

    :param const char \*name:
        name of namespace to find  (NOT NULL)

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

    :param struct aa_ns \*view:
        *undescribed*

    :param const char \*hname:
        hierarchical ns name  (NOT NULL)

    :param size_t n:
        length of \ ``hname``\ 

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

    :param struct aa_ns \*view:
        namespace to search in  (NOT NULL)

    :param const char \*name:
        name of namespace to find  (NOT NULL)

    :param size_t n:
        length of \ ``name``\ 

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

    :param struct aa_ns \*parent:
        the parent of the namespace being created

    :param const char \*name:
        the name of the namespace

    :param struct dentry \*dir:
        if not null the dir to put the ns entries in

.. _`__aa_find_or_create_ns.return`:

Return
------

the a refcounted ns that has been add or an ERR_PTR

.. _`aa_prepare_ns`:

aa_prepare_ns
=============

.. c:function:: struct aa_ns *aa_prepare_ns(struct aa_ns *parent, const char *name)

    find an existing or create a new namespace of \ ``name``\ 

    :param struct aa_ns \*parent:
        ns to treat as parent

    :param const char \*name:
        the namespace to find or add  (NOT NULL)

.. _`aa_prepare_ns.return`:

Return
------

refcounted namespace or PTR_ERR if failed to create one

.. _`destroy_ns`:

destroy_ns
==========

.. c:function:: void destroy_ns(struct aa_ns *ns)

    remove everything contained by \ ``ns``\ 

    :param struct aa_ns \*ns:
        namespace to have it contents removed  (NOT NULL)

.. _`__aa_remove_ns`:

\__aa_remove_ns
===============

.. c:function:: void __aa_remove_ns(struct aa_ns *ns)

    remove a namespace and all its children

    :param struct aa_ns \*ns:
        namespace to be removed  (NOT NULL)

.. _`__aa_remove_ns.requires`:

Requires
--------

ns->parent->lock be held and ns removed from parent.

.. _`__ns_list_release`:

\__ns_list_release
==================

.. c:function:: void __ns_list_release(struct list_head *head)

    remove all profile namespaces on the list put refs

    :param struct list_head \*head:
        list of profile namespaces  (NOT NULL)

.. _`__ns_list_release.requires`:

Requires
--------

namespace lock be held

.. _`aa_alloc_root_ns`:

aa_alloc_root_ns
================

.. c:function:: int aa_alloc_root_ns( void)

    allocate the root profile namespace

    :param  void:
        no arguments

.. _`aa_alloc_root_ns.return`:

Return
------

\ ``0``\  on success else error

.. This file was automatic generated / don't edit.

