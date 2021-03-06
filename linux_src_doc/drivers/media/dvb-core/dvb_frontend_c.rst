.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/dvb-core/dvb_frontend.c

.. _`dvb_frontend_swzigzag_autotune`:

dvb_frontend_swzigzag_autotune
==============================

.. c:function:: int dvb_frontend_swzigzag_autotune(struct dvb_frontend *fe, int check_wrapped)

    Performs automatic twiddling of frontend parameters.

    :param fe:
        The frontend concerned.
    :type fe: struct dvb_frontend \*

    :param check_wrapped:
        Checks if an iteration has completed.
        DO NOT SET ON THE FIRST ATTEMPT.
    :type check_wrapped: int

.. _`dvb_frontend_swzigzag_autotune.return`:

Return
------

Number of complete iterations that have been performed.

.. _`dtv_get_frontend`:

dtv_get_frontend
================

.. c:function:: int dtv_get_frontend(struct dvb_frontend *fe, struct dtv_frontend_properties *c, struct dvb_frontend_parameters *p_out)

    calls a callback for retrieving DTV parameters

    :param fe:
        struct dvb_frontend pointer
    :type fe: struct dvb_frontend \*

    :param c:
        struct dtv_frontend_properties pointer (DVBv5 cache)
    :type c: struct dtv_frontend_properties \*

    :param p_out:
        struct dvb_frontend_parameters pointer (DVBv3 FE struct)
    :type p_out: struct dvb_frontend_parameters \*

.. _`dtv_get_frontend.description`:

Description
-----------

This routine calls either the DVBv3 or DVBv5 get_frontend call.
If c is not null, it will update the DVBv5 cache struct pointed by it.
If p_out is not null, it will update the DVBv3 params pointed by it.

.. _`emulate_delivery_system`:

emulate_delivery_system
=======================

.. c:function:: int emulate_delivery_system(struct dvb_frontend *fe, u32 delsys)

    emulate a DVBv5 delivery system with a DVBv3 type

    :param fe:
        struct frontend;
    :type fe: struct dvb_frontend \*

    :param delsys:
        DVBv5 type that will be used for emulation
    :type delsys: u32

.. _`emulate_delivery_system.description`:

Description
-----------

Provides emulation for delivery systems that are compatible with the old
DVBv3 call. Among its usages, it provices support for ISDB-T, and allows
using a DVB-S2 only frontend just like it were a DVB-S, if the frontent
parameters are compatible with DVB-S spec.

.. _`dvbv5_set_delivery_system`:

dvbv5_set_delivery_system
=========================

.. c:function:: int dvbv5_set_delivery_system(struct dvb_frontend *fe, u32 desired_system)

    Sets the delivery system for a DVBv5 API call

    :param fe:
        frontend struct
    :type fe: struct dvb_frontend \*

    :param desired_system:
        delivery system requested by the user
    :type desired_system: u32

.. _`dvbv5_set_delivery_system.description`:

Description
-----------

A DVBv5 call know what's the desired system it wants. So, set it.

There are, however, a few known issues with early DVBv5 applications that

.. _`dvbv5_set_delivery_system.are-also-handled-by-this-logic`:

are also handled by this logic
------------------------------


1) Some early apps use SYS_UNDEFINED as the desired delivery system.
This is an API violation, but, as we don't want to break userspace,
convert it to the first supported delivery system.
2) Some apps might be using a DVBv5 call in a wrong way, passing, for
example, SYS_DVBT instead of SYS_ISDBT. This is because early usage of
ISDB-T provided backward compat with DVB-T.

.. _`dvbv3_set_delivery_system`:

dvbv3_set_delivery_system
=========================

.. c:function:: int dvbv3_set_delivery_system(struct dvb_frontend *fe)

    Sets the delivery system for a DVBv3 API call

    :param fe:
        frontend struct
    :type fe: struct dvb_frontend \*

.. _`dvbv3_set_delivery_system.description`:

Description
-----------

A DVBv3 call doesn't know what's the desired system it wants. It also
doesn't allow to switch between different types. Due to that, userspace
should use DVBv5 instead.
However, in order to avoid breaking userspace API, limited backward
compatibility support is provided.

There are some delivery systems that are incompatible with DVBv3 calls.

This routine should work fine for frontends that support just one delivery
system.

.. _`dvbv3_set_delivery_system.for-frontends-that-support-multiple-frontends`:

For frontends that support multiple frontends
---------------------------------------------

1) It defaults to use the first supported delivery system. There's an
userspace application that allows changing it at runtime;

2) If the current delivery system is not compatible with DVBv3, it gets
the first one that it is compatible.

.. _`dvbv3_set_delivery_system.note`:

NOTE
----

in order for this to work with applications like Kaffeine that
uses a DVBv5 call for DVB-S2 and a DVBv3 call to go back to
DVB-S, drivers that support both DVB-S and DVB-S2 should have the
SYS_DVBS entry before the SYS_DVBS2, otherwise it won't switch back
to DVB-S.

.. _`dtv_property_process_set`:

dtv_property_process_set
========================

.. c:function:: int dtv_property_process_set(struct dvb_frontend *fe, struct file *file, u32 cmd, u32 data)

    Sets a single DTV property

    :param fe:
        Pointer to \ :c:type:`struct dvb_frontend <dvb_frontend>`\ 
    :type fe: struct dvb_frontend \*

    :param file:
        Pointer to \ :c:type:`struct file <file>`\ 
    :type file: struct file \*

    :param cmd:
        Digital TV command
    :type cmd: u32

    :param data:
        An unsigned 32-bits number
    :type data: u32

.. _`dtv_property_process_set.description`:

Description
-----------

This routine assigns the property
value to the corresponding member of
\ :c:type:`struct dtv_frontend_properties <dtv_frontend_properties>`\ 

.. _`dtv_property_process_set.return`:

Return
------

Zero on success, negative errno on failure.

.. This file was automatic generated / don't edit.

