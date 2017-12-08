.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/sound/ac97/codec.h

.. _`ac97_id`:

struct ac97_id
==============

.. c:type:: struct ac97_id

    matches a codec device and driver on an ac97 bus

.. _`ac97_id.definition`:

Definition
----------

.. code-block:: c

    struct ac97_id {
        unsigned int id;
        unsigned int mask;
        void *data;
    }

.. _`ac97_id.members`:

Members
-------

id
    The significant bits if the codec vendor ID1 and ID2

mask
    Bitmask specifying which bits of the id field are significant when
    matching. A driver binds to a device when :
    ((vendorID1 << 8 \| vendorID2) & (mask_id1 << 8 \| mask_id2)) == id.

data
    Private data used by the driver.

.. This file was automatic generated / don't edit.

