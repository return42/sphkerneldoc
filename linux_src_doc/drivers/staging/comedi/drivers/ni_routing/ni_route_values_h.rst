.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/comedi/drivers/ni_routing/ni_route_values.h

.. _`family_route_values`:

struct family_route_values
==========================

.. c:type:: struct family_route_values

    Register values for all routes for a particular family.

.. _`family_route_values.definition`:

Definition
----------

.. code-block:: c

    struct family_route_values {
        const char *family;
        const register_type register_values[NI_NUM_NAMES][NI_NUM_NAMES];
    }

.. _`family_route_values.members`:

Members
-------

family
    lower-case string representation of a specific series or family of
    devices from National Instruments where each member of this family
    shares the same register values for the various signal MUXes.  It
    should be noted that not all devices of any family have access to
    all routes defined.

register_values
    Table of all register values for various signal MUXes on
    National Instruments devices.  The first index of this table is the
    signal destination (i.e. identification of the signal MUX).  The
    second index of this table is the signal source (i.e. input of the
    signal MUX).

.. This file was automatic generated / don't edit.

