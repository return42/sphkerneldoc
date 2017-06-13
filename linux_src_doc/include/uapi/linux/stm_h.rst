.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/stm.h

.. _`stp_policy_id`:

struct stp_policy_id
====================

.. c:type:: struct stp_policy_id

    identification for the STP policy

.. _`stp_policy_id.definition`:

Definition
----------

.. code-block:: c

    struct stp_policy_id {
        __u32 size;
        __u16 master;
        __u16 channel;
        __u16 width;
        __u16 __reserved_0;
        __u32 __reserved_1;
        char id;
    }

.. _`stp_policy_id.members`:

Members
-------

size
    size of the structure including real id[] length

master
    assigned master

channel
    first assigned channel

width
    number of requested channels

__reserved_0
    *undescribed*

__reserved_1
    *undescribed*

id
    identification string

.. _`stp_policy_id.description`:

Description
-----------

User must calculate the total size of the structure and put it into
\ ``size``\  field, fill out the \ ``id``\  and desired \ ``width``\ . In return, kernel
fills out \ ``master``\ , \ ``channel``\  and \ ``width``\ .

.. This file was automatic generated / don't edit.

