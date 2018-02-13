.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/vfio_ccw_cp.h

.. _`channel_program`:

struct channel_program
======================

.. c:type:: struct channel_program

    manage information for channel program

.. _`channel_program.definition`:

Definition
----------

.. code-block:: c

    struct channel_program {
        struct list_head ccwchain_list;
        union orb orb;
        struct device *mdev;
    }

.. _`channel_program.members`:

Members
-------

ccwchain_list
    list head of ccwchains

orb
    orb for the currently processed ssch request

mdev
    the mediated device to perform page pinning/unpinning

.. _`channel_program.description`:

Description
-----------

\ ``ccwchain_list``\  is the head of a ccwchain list, that contents the
translated result of the guest channel program that pointed out by
the iova parameter when calling cp_init.

.. This file was automatic generated / don't edit.

