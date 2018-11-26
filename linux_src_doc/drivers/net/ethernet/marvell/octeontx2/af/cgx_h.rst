.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/marvell/octeontx2/af/cgx.h

.. _`cgx_event_cb`:

struct cgx_event_cb
===================

.. c:type:: struct cgx_event_cb


.. _`cgx_event_cb.definition`:

Definition
----------

.. code-block:: c

    struct cgx_event_cb {
        int (*notify_link_chg)(struct cgx_link_event *event, void *data);
        void *data;
    }

.. _`cgx_event_cb.members`:

Members
-------

notify_link_chg
    callback for link change notification

data
    data passed to callback function

.. This file was automatic generated / don't edit.

