.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/of/dynamic.c

.. _`of_node_get`:

of_node_get
===========

.. c:function:: struct device_node *of_node_get(struct device_node *node)

    Increment refcount of a node

    :param struct device_node \*node:
        Node to inc refcount, NULL is supported to simplify writing of
        callers

.. _`of_node_get.description`:

Description
-----------

Returns node.

.. _`of_node_put`:

of_node_put
===========

.. c:function:: void of_node_put(struct device_node *node)

    Decrement refcount of a node

    :param struct device_node \*node:
        Node to dec refcount, NULL is supported to simplify writing of
        callers

.. _`of_attach_node`:

of_attach_node
==============

.. c:function:: int of_attach_node(struct device_node *np)

    Plug a device node into the tree and global list.

    :param struct device_node \*np:
        *undescribed*

.. _`of_detach_node`:

of_detach_node
==============

.. c:function:: int of_detach_node(struct device_node *np)

    "Unplug" a node from the device tree.

    :param struct device_node \*np:
        *undescribed*

.. _`of_detach_node.description`:

Description
-----------

The caller must hold a reference to the node.  The memory associated with
the node is not freed until its refcount goes to zero.

.. _`of_node_release`:

of_node_release
===============

.. c:function:: void of_node_release(struct kobject *kobj)

    release a dynamically allocated node

    :param struct kobject \*kobj:
        *undescribed*

.. _`of_node_release.description`:

Description
-----------

In \ :c:func:`of_node_put`\  this function is passed to \ :c:func:`kref_put`\  as the destructor.

.. _`__of_prop_dup`:

__of_prop_dup
=============

.. c:function:: struct property *__of_prop_dup(const struct property *prop, gfp_t allocflags)

    Copy a property dynamically.

    :param const struct property \*prop:
        Property to copy

    :param gfp_t allocflags:
        Allocation flags (typically pass GFP_KERNEL)

.. _`__of_prop_dup.description`:

Description
-----------

Copy a property by dynamically allocating the memory of both the
property structure and the property name & contents. The property's
flags have the OF_DYNAMIC bit set so that we can differentiate between
dynamically allocated properties and not.
Returns the newly allocated property or NULL on out of memory error.

.. _`__of_node_dup`:

__of_node_dup
=============

.. c:function:: struct device_node *__of_node_dup(const struct device_node *np, const char *fmt,  ...)

    Duplicate or create an empty device node dynamically.

    :param const struct device_node \*np:
        *undescribed*

    :param const char \*fmt:
        Format string (plus vargs) for new full name of the device node

    :param ellipsis ellipsis:
        variable arguments

.. _`__of_node_dup.description`:

Description
-----------

Create an device tree node, either by duplicating an empty node or by allocating
an empty one suitable for further modification.  The node data are
dynamically allocated and all the node flags have the OF_DYNAMIC &
OF_DETACHED bits set. Returns the newly allocated node or NULL on out of
memory error.

.. _`of_changeset_init`:

of_changeset_init
=================

.. c:function:: void of_changeset_init(struct of_changeset *ocs)

    Initialize a changeset for use

    :param struct of_changeset \*ocs:
        changeset pointer

.. _`of_changeset_init.description`:

Description
-----------

Initialize a changeset structure

.. _`of_changeset_destroy`:

of_changeset_destroy
====================

.. c:function:: void of_changeset_destroy(struct of_changeset *ocs)

    Destroy a changeset

    :param struct of_changeset \*ocs:
        changeset pointer

.. _`of_changeset_destroy.description`:

Description
-----------

Destroys a changeset. Note that if a changeset is applied,
its changes to the tree cannot be reverted.

.. _`of_changeset_apply`:

of_changeset_apply
==================

.. c:function:: int of_changeset_apply(struct of_changeset *ocs)

    Applies a changeset

    :param struct of_changeset \*ocs:
        changeset pointer

.. _`of_changeset_apply.description`:

Description
-----------

Applies a changeset to the live tree.
Any side-effects of live tree state changes are applied here on
success, like creation/destruction of devices and side-effects
like creation of sysfs properties and directories.
Returns 0 on success, a negative error value in case of an error.
On error the partially applied effects are reverted.

.. _`of_changeset_revert`:

of_changeset_revert
===================

.. c:function:: int of_changeset_revert(struct of_changeset *ocs)

    Reverts an applied changeset

    :param struct of_changeset \*ocs:
        changeset pointer

.. _`of_changeset_revert.description`:

Description
-----------

Reverts a changeset returning the state of the tree to what it
was before the application.
Any side-effects like creation/destruction of devices and
removal of sysfs properties and directories are applied.
Returns 0 on success, a negative error value in case of an error.

.. _`of_changeset_action`:

of_changeset_action
===================

.. c:function:: int of_changeset_action(struct of_changeset *ocs, unsigned long action, struct device_node *np, struct property *prop)

    Perform a changeset action

    :param struct of_changeset \*ocs:
        changeset pointer

    :param unsigned long action:
        action to perform

    :param struct device_node \*np:
        Pointer to device node

    :param struct property \*prop:
        Pointer to property

.. _`of_changeset_action.on-action-being-one-of`:

On action being one of
----------------------

+ OF_RECONFIG_ATTACH_NODE
+ OF_RECONFIG_DETACH_NODE,
+ OF_RECONFIG_ADD_PROPERTY
+ OF_RECONFIG_REMOVE_PROPERTY,
+ OF_RECONFIG_UPDATE_PROPERTY
Returns 0 on success, a negative error value in case of an error.

.. This file was automatic generated / don't edit.

