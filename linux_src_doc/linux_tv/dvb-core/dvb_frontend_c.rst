.. -*- coding: utf-8; mode: rst -*-

==============
dvb_frontend.c
==============



.. _xref_dvb_frontend_swzigzag_autotune:

dvb_frontend_swzigzag_autotune
==============================

.. c:function:: int dvb_frontend_swzigzag_autotune (struct dvb_frontend * fe, int check_wrapped)

    

    :param struct dvb_frontend * fe:

        _undescribed_

    :param int check_wrapped:

        _undescribed_



Description
-----------



**param** fe The frontend concerned.
**param** check_wrapped Checks if an iteration has completed. DO NOT SET ON THE FIRST ATTEMPT
**returns** Number of complete iterations that have been performed.




.. _xref_dvb_enable_media_tuner:

dvb_enable_media_tuner
======================

.. c:function:: int dvb_enable_media_tuner (struct dvb_frontend * fe)

    tries to enable the DVB tuner

    :param struct dvb_frontend * fe:
        struct dvb_frontend pointer



Description
-----------

This function ensures that just one media tuner is enabled for a given
frontend. It has two different behaviors:
- For trivial devices with just one tuner:
  it just enables the existing tuner->fe link
- For devices with more than one tuner:
  It is up to the driver to implement the logic that will enable one tuner
  and disable the other ones. However, if more than one tuner is enabled for
  the same frontend, it will print an error message and return -EINVAL.


At return, it will return the error code returned by media_entity_setup_link,
or 0 if everything is OK, if no tuner is linked to the frontend or if the
mdev is NULL.




.. _xref_dtv_get_frontend:

dtv_get_frontend
================

.. c:function:: int dtv_get_frontend (struct dvb_frontend * fe, struct dvb_frontend_parameters * p_out)

    calls a callback for retrieving DTV parameters

    :param struct dvb_frontend * fe:
        struct dvb_frontend pointer

    :param struct dvb_frontend_parameters * p_out:

        _undescribed_



Description
-----------

This routine calls either the DVBv3 or DVBv5 get_frontend call.
If c is not null, it will update the DVBv5 cache struct pointed by it.
If p_out is not null, it will update the DVBv3 params pointed by it.




.. _xref_emulate_delivery_system:

emulate_delivery_system
=======================

.. c:function:: int emulate_delivery_system (struct dvb_frontend * fe, u32 delsys)

    emulate a DVBv5 delivery system with a DVBv3 type

    :param struct dvb_frontend * fe:
        struct frontend;

    :param u32 delsys:
        DVBv5 type that will be used for emulation



Description
-----------

Provides emulation for delivery systems that are compatible with the old
DVBv3 call. Among its usages, it provices support for ISDB-T, and allows
using a DVB-S2 only frontend just like it were a DVB-S, if the frontent
parameters are compatible with DVB-S spec.




.. _xref_dvbv5_set_delivery_system:

dvbv5_set_delivery_system
=========================

.. c:function:: int dvbv5_set_delivery_system (struct dvb_frontend * fe, u32 desired_system)

    Sets the delivery system for a DVBv5 API call

    :param struct dvb_frontend * fe:
        frontend struct

    :param u32 desired_system:
        delivery system requested by the user



Description
-----------

A DVBv5 call know what's the desired system it wants. So, set it.


There are, however, a few known issues with early DVBv5 applications that



are also handled by this logic
------------------------------



1) Some early apps use SYS_UNDEFINED as the desired delivery system.
   This is an API violation, but, as we don't want to break userspace,
   convert it to the first supported delivery system.
2) Some apps might be using a DVBv5 call in a wrong way, passing, for
   example, SYS_DVBT instead of SYS_ISDBT. This is because early usage of
   ISDB-T provided backward compat with DVB-T.




.. _xref_dvbv3_set_delivery_system:

dvbv3_set_delivery_system
=========================

.. c:function:: int dvbv3_set_delivery_system (struct dvb_frontend * fe)

    Sets the delivery system for a DVBv3 API call

    :param struct dvb_frontend * fe:
        frontend struct



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



For frontends that support multiple frontends
---------------------------------------------

1) It defaults to use the first supported delivery system. There's an
   userspace application that allows changing it at runtime;


2) If the current delivery system is not compatible with DVBv3, it gets
   the first one that it is compatible.



NOTE
----

in order for this to work with applications like Kaffeine that
	uses a DVBv5 call for DVB-S2 and a DVBv3 call to go back to
	DVB-S, drivers that support both DVB-S and DVB-S2 should have the
	SYS_DVBS entry before the SYS_DVBS2, otherwise it won't switch back
	to DVB-S.


