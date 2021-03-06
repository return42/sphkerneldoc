.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/backing-dev-defs.h

.. _`wb_tryget`:

wb_tryget
=========

.. c:function:: bool wb_tryget(struct bdi_writeback *wb)

    try to increment a wb's refcount

    :param wb:
        bdi_writeback to get
    :type wb: struct bdi_writeback \*

.. _`wb_get`:

wb_get
======

.. c:function:: void wb_get(struct bdi_writeback *wb)

    increment a wb's refcount

    :param wb:
        bdi_writeback to get
    :type wb: struct bdi_writeback \*

.. _`wb_put`:

wb_put
======

.. c:function:: void wb_put(struct bdi_writeback *wb)

    decrement a wb's refcount

    :param wb:
        bdi_writeback to put
    :type wb: struct bdi_writeback \*

.. _`wb_dying`:

wb_dying
========

.. c:function:: bool wb_dying(struct bdi_writeback *wb)

    is a wb dying?

    :param wb:
        bdi_writeback of interest
    :type wb: struct bdi_writeback \*

.. _`wb_dying.description`:

Description
-----------

Returns whether \ ``wb``\  is unlinked and being drained.

.. This file was automatic generated / don't edit.

