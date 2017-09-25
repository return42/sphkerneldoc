.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_debugfs.h

.. _`drm_info_list`:

struct drm_info_list
====================

.. c:type:: struct drm_info_list

    debugfs info list entry

.. _`drm_info_list.definition`:

Definition
----------

.. code-block:: c

    struct drm_info_list {
        const char *name;
        int (*show)(struct seq_file*, void*);
        u32 driver_features;
        void *data;
    }

.. _`drm_info_list.members`:

Members
-------

name
    file name

show

    Show callback. \ :c:type:`seq_file->private <seq_file>`\  will be set to the \ :c:type:`struct drm_info_node <drm_info_node>`\  corresponding to the instance of this info on a given
    \ :c:type:`struct drm_minor <drm_minor>`\ .

driver_features
    Required driver features for this entry

data
    Driver-private data, should not be device-specific.

.. _`drm_info_list.description`:

Description
-----------

This structure represents a debugfs file to be created by the drm
core.

.. _`drm_info_node`:

struct drm_info_node
====================

.. c:type:: struct drm_info_node

    Per-minor debugfs node structure

.. _`drm_info_node.definition`:

Definition
----------

.. code-block:: c

    struct drm_info_node {
        struct drm_minor *minor;
        const struct drm_info_list *info_ent;
        struct list_head list;
        struct dentry *dent;
    }

.. _`drm_info_node.members`:

Members
-------

minor
    &struct drm_minor for this node.

info_ent
    template for this node.

list
    *undescribed*

dent
    *undescribed*

.. _`drm_info_node.description`:

Description
-----------

This structure represents a debugfs file, as an instantiation of a \ :c:type:`struct drm_info_list <drm_info_list>`\  on a \ :c:type:`struct drm_minor <drm_minor>`\ .

.. _`drm_info_node.fixme`:

FIXME
-----


No it doesn't make a hole lot of sense that we duplicate debugfs entries for
both the render and the primary nodes, but that's how this has organically
grown. It should probably be fixed, with a compatibility link, if needed.

.. This file was automatic generated / don't edit.

