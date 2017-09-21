.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/vsp1.h

.. _`vsp1_du_lif_config`:

struct vsp1_du_lif_config
=========================

.. c:type:: struct vsp1_du_lif_config

    VSP LIF configuration

.. _`vsp1_du_lif_config.definition`:

Definition
----------

.. code-block:: c

    struct vsp1_du_lif_config {
        unsigned int width;
        unsigned int height;
        void (*callback)(void *, bool);
        void *callback_data;
    }

.. _`vsp1_du_lif_config.members`:

Members
-------

width
    output frame width

height
    output frame height

callback
    frame completion callback function (optional). When a callback
    is provided, the VSP driver guarantees that it will be called once
    and only once for each \ :c:func:`vsp1_du_atomic_flush`\  call.

callback_data
    data to be passed to the frame completion callback

.. This file was automatic generated / don't edit.

