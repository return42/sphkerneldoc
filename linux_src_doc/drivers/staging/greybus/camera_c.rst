.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/greybus/camera.c

.. _`gb_camera`:

struct gb_camera
================

.. c:type:: struct gb_camera

    A Greybus Camera Device

.. _`gb_camera.definition`:

Definition
----------

.. code-block:: c

    struct gb_camera {
        struct gb_bundle *bundle;
        struct gb_connection *connection;
        struct gb_connection *data_connection;
        u16 data_cport_id;
        struct mutex mutex;
        enum gb_camera_state state;
        struct {
            struct dentry *root;
            struct gb_camera_debugfs_buffer *buffers;
        } debugfs;
        struct gb_camera_module module;
    }

.. _`gb_camera.members`:

Members
-------

bundle
    *undescribed*

connection
    the greybus connection for camera management

data_connection
    the greybus connection for camera data

data_cport_id
    the data CPort ID on the module side

mutex
    protects the connection and state fields

state
    the current module state

root
    *undescribed*

buffers
    *undescribed*

ebugfs
    *undescribed*

module
    Greybus camera module registered to HOST processor.

.. This file was automatic generated / don't edit.

