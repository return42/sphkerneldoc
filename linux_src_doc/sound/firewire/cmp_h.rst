.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/firewire/cmp.h

.. _`cmp_connection`:

struct cmp_connection
=====================

.. c:type:: struct cmp_connection

    manages an isochronous connection to a device

.. _`cmp_connection.definition`:

Definition
----------

.. code-block:: c

    struct cmp_connection {
        int speed;
        bool connected;
        struct mutex mutex;
        struct fw_iso_resources resources;
        __be32 last_pcr_value;
        unsigned int pcr_index;
        unsigned int max_speed;
        enum cmp_direction direction;
    }

.. _`cmp_connection.members`:

Members
-------

speed
    the connection's actual speed

connected
    *undescribed*

mutex
    *undescribed*

resources
    *undescribed*

last_pcr_value
    *undescribed*

pcr_index
    *undescribed*

max_speed
    *undescribed*

direction
    *undescribed*

.. _`cmp_connection.description`:

Description
-----------

This structure manages (using CMP) an isochronous stream between the local
computer and a device's input plug (iPCR) and output plug (oPCR).

There is no corresponding oPCR created on the local computer, so it is not
possible to overlay connections on top of this one.

.. This file was automatic generated / don't edit.

