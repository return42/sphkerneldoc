.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aic94xx/aic94xx_hwi.h

.. _`asd_ascb_free`:

asd_ascb_free
=============

.. c:function:: void asd_ascb_free(struct asd_ascb *ascb)

    - free a single aSCB after is has completed

    :param ascb:
        pointer to the aSCB of interest
    :type ascb: struct asd_ascb \*

.. _`asd_ascb_free.description`:

Description
-----------

This frees an aSCB after it has been executed/completed by
the sequencer.

.. _`asd_ascb_free_list`:

asd_ascb_free_list
==================

.. c:function:: void asd_ascb_free_list(struct asd_ascb *ascb_list)

    - free a list of ascbs

    :param ascb_list:
        a list of ascbs
    :type ascb_list: struct asd_ascb \*

.. _`asd_ascb_free_list.description`:

Description
-----------

This function will free a list of ascbs allocated by asd_ascb_alloc_list.
It is used when say the scb queueing function returned QUEUE_FULL,
and we do not need the ascbs any more.

.. This file was automatic generated / don't edit.

