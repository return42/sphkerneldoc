.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/bonding/bond_3ad.c

.. _`__get_bond_by_port`:

__get_bond_by_port
==================

.. c:function:: struct bonding *__get_bond_by_port(struct port *port)

    get the port's bonding struct

    :param struct port \*port:
        the port we're looking at

.. _`__get_bond_by_port.description`:

Description
-----------

Return \ ``port``\ 's bonding struct, or \ ``NULL``\  if it can't be found.

.. _`__get_first_agg`:

__get_first_agg
===============

.. c:function:: struct aggregator *__get_first_agg(struct port *port)

    get the first aggregator in the bond

    :param struct port \*port:
        *undescribed*

.. _`__get_first_agg.description`:

Description
-----------

Return the aggregator of the first slave in \ ``bond``\ , or \ ``NULL``\  if it can't be
found.
The caller must hold RCU or RTNL lock.

.. _`__agg_has_partner`:

__agg_has_partner
=================

.. c:function:: int __agg_has_partner(struct aggregator *agg)

    see if we have a partner

    :param struct aggregator \*agg:
        the agregator we're looking at

.. _`__agg_has_partner.description`:

Description
-----------

Return nonzero if aggregator has a partner (denoted by a non-zero ether
address for the partner). Return 0 if not.

.. _`__disable_port`:

__disable_port
==============

.. c:function:: void __disable_port(struct port *port)

    disable the port's slave

    :param struct port \*port:
        the port we're looking at

.. _`__enable_port`:

__enable_port
=============

.. c:function:: void __enable_port(struct port *port)

    enable the port's slave, if it's up

    :param struct port \*port:
        the port we're looking at

.. _`__port_is_enabled`:

__port_is_enabled
=================

.. c:function:: int __port_is_enabled(struct port *port)

    check if the port's slave is in active state

    :param struct port \*port:
        the port we're looking at

.. _`__get_agg_selection_mode`:

__get_agg_selection_mode
========================

.. c:function:: u32 __get_agg_selection_mode(struct port *port)

    get the aggregator selection mode

    :param struct port \*port:
        the port we're looking at

.. _`__get_agg_selection_mode.description`:

Description
-----------

Get the aggregator selection mode. Can be \ ``STABLE``\ , \ ``BANDWIDTH``\  or \ ``COUNT``\ .

.. _`__check_agg_selection_timer`:

__check_agg_selection_timer
===========================

.. c:function:: int __check_agg_selection_timer(struct port *port)

    check if the selection timer has expired

    :param struct port \*port:
        the port we're looking at

.. _`__get_link_speed`:

__get_link_speed
================

.. c:function:: u16 __get_link_speed(struct port *port)

    get a port's speed

    :param struct port \*port:
        the port we're looking at

.. _`__get_link_speed.description`:

Description
-----------

Return \ ``port``\ 's speed in 802.3ad enum format. i.e. one of:
0,
\ ``AD_LINK_SPEED_10MBPS``\ ,
\ ``AD_LINK_SPEED_100MBPS``\ ,
\ ``AD_LINK_SPEED_1000MBPS``\ ,
\ ``AD_LINK_SPEED_2500MBPS``\ ,
\ ``AD_LINK_SPEED_10000MBPS``\ 
\ ``AD_LINK_SPEED_20000MBPS``\ 
\ ``AD_LINK_SPEED_40000MBPS``\ 
\ ``AD_LINK_SPEED_56000MBPS``\ 
\ ``AD_LINK_SPEED_100000MBPS``\ 

.. _`__get_duplex`:

__get_duplex
============

.. c:function:: u8 __get_duplex(struct port *port)

    get a port's duplex

    :param struct port \*port:
        the port we're looking at

.. _`__get_duplex.description`:

Description
-----------

Return \ ``port``\ 's duplex in 802.3ad bitmask format. i.e.:
0x01 if in full duplex
0x00 otherwise

.. _`__ad_timer_to_ticks`:

__ad_timer_to_ticks
===================

.. c:function:: u16 __ad_timer_to_ticks(u16 timer_type, u16 par)

    convert a given timer type to AD module ticks

    :param u16 timer_type:
        which timer to operate

    :param u16 par:
        timer parameter. see below

.. _`__ad_timer_to_ticks.description`:

Description
-----------

If \ ``timer_type``\  is \ ``current_while_timer``\ , \ ``par``\  indicates long/short timer.
If \ ``timer_type``\  is \ ``periodic_timer``\ , \ ``par``\  is one of \ ``FAST_PERIODIC_TIME``\ ,
\ ``SLOW_PERIODIC_TIME``\ .

.. _`__choose_matched`:

__choose_matched
================

.. c:function:: void __choose_matched(struct lacpdu *lacpdu, struct port *port)

    update a port's matched variable from a received lacpdu

    :param struct lacpdu \*lacpdu:
        the lacpdu we've received

    :param struct port \*port:
        the port we're looking at

.. _`__choose_matched.description`:

Description
-----------

Update the value of the matched variable, using parameter values from a
newly received lacpdu. Parameter values for the partner carried in the
received PDU are compared with the corresponding operational parameter
values for the actor. Matched is set to TRUE if all of these parameters
match and the PDU parameter partner_state.aggregation has the same value as
actor_oper_port_state.aggregation and lacp will actively maintain the link
in the aggregation. Matched is also set to TRUE if the value of
actor_state.aggregation in the received PDU is set to FALSE, i.e., indicates
an individual link and lacp will actively maintain the link. Otherwise,
matched is set to FALSE. LACP is considered to be actively maintaining the
link if either the PDU's actor_state.lacp_activity variable is TRUE or both
the actor's actor_oper_port_state.lacp_activity and the PDU's
partner_state.lacp_activity variables are TRUE.

.. _`__choose_matched.note`:

Note
----

the AD_PORT_MATCHED "variable" is not specified by 802.3ad; it is
used here to implement the language from 802.3ad 43.4.9 that requires
recordPDU to "match" the LACPDU parameters to the stored values.

.. _`__record_pdu`:

__record_pdu
============

.. c:function:: void __record_pdu(struct lacpdu *lacpdu, struct port *port)

    record parameters from a received lacpdu

    :param struct lacpdu \*lacpdu:
        the lacpdu we've received

    :param struct port \*port:
        the port we're looking at

.. _`__record_pdu.description`:

Description
-----------

Record the parameter values for the Actor carried in a received lacpdu as
the current partner operational parameter values and sets
actor_oper_port_state.defaulted to FALSE.

.. _`__record_default`:

__record_default
================

.. c:function:: void __record_default(struct port *port)

    record default parameters

    :param struct port \*port:
        the port we're looking at

.. _`__record_default.description`:

Description
-----------

This function records the default parameter values for the partner carried
in the Partner Admin parameters as the current partner operational parameter
values and sets actor_oper_port_state.defaulted to TRUE.

.. _`__update_selected`:

__update_selected
=================

.. c:function:: void __update_selected(struct lacpdu *lacpdu, struct port *port)

    update a port's Selected variable from a received lacpdu

    :param struct lacpdu \*lacpdu:
        the lacpdu we've received

    :param struct port \*port:
        the port we're looking at

.. _`__update_selected.description`:

Description
-----------

Update the value of the selected variable, using parameter values from a
newly received lacpdu. The parameter values for the Actor carried in the
received PDU are compared with the corresponding operational parameter
values for the ports partner. If one or more of the comparisons shows that
the value(s) received in the PDU differ from the current operational values,
then selected is set to FALSE and actor_oper_port_state.synchronization is
set to out_of_sync. Otherwise, selected remains unchanged.

.. _`__update_default_selected`:

__update_default_selected
=========================

.. c:function:: void __update_default_selected(struct port *port)

    update a port's Selected variable from Partner

    :param struct port \*port:
        the port we're looking at

.. _`__update_default_selected.description`:

Description
-----------

This function updates the value of the selected variable, using the partner
administrative parameter values. The administrative values are compared with
the corresponding operational parameter values for the partner. If one or
more of the comparisons shows that the administrative value(s) differ from
the current operational values, then Selected is set to FALSE and
actor_oper_port_state.synchronization is set to OUT_OF_SYNC. Otherwise,
Selected remains unchanged.

.. _`__update_ntt`:

__update_ntt
============

.. c:function:: void __update_ntt(struct lacpdu *lacpdu, struct port *port)

    update a port's ntt variable from a received lacpdu

    :param struct lacpdu \*lacpdu:
        the lacpdu we've received

    :param struct port \*port:
        the port we're looking at

.. _`__update_ntt.description`:

Description
-----------

Updates the value of the ntt variable, using parameter values from a newly
received lacpdu. The parameter values for the partner carried in the
received PDU are compared with the corresponding operational parameter
values for the Actor. If one or more of the comparisons shows that the
value(s) received in the PDU differ from the current operational values,
then ntt is set to TRUE. Otherwise, ntt remains unchanged.

.. _`__agg_ports_are_ready`:

__agg_ports_are_ready
=====================

.. c:function:: int __agg_ports_are_ready(struct aggregator *aggregator)

    check if all ports in an aggregator are ready

    :param struct aggregator \*aggregator:
        the aggregator we're looking at

.. _`__set_agg_ports_ready`:

__set_agg_ports_ready
=====================

.. c:function:: void __set_agg_ports_ready(struct aggregator *aggregator, int val)

    set value of Ready bit in all ports of an aggregator

    :param struct aggregator \*aggregator:
        the aggregator we're looking at

    :param int val:
        Should the ports' ready bit be set on or off

.. _`__get_agg_bandwidth`:

__get_agg_bandwidth
===================

.. c:function:: u32 __get_agg_bandwidth(struct aggregator *aggregator)

    get the total bandwidth of an aggregator

    :param struct aggregator \*aggregator:
        the aggregator we're looking at

.. _`__get_active_agg`:

__get_active_agg
================

.. c:function:: struct aggregator *__get_active_agg(struct aggregator *aggregator)

    get the current active aggregator

    :param struct aggregator \*aggregator:
        the aggregator we're looking at

.. _`__get_active_agg.description`:

Description
-----------

Caller must hold RCU lock.

.. _`__update_lacpdu_from_port`:

__update_lacpdu_from_port
=========================

.. c:function:: void __update_lacpdu_from_port(struct port *port)

    update a port's lacpdu fields

    :param struct port \*port:
        the port we're looking at

.. _`ad_lacpdu_send`:

ad_lacpdu_send
==============

.. c:function:: int ad_lacpdu_send(struct port *port)

    send out a lacpdu packet on a given port

    :param struct port \*port:
        the port we're looking at

.. _`ad_lacpdu_send.return`:

Return
------

0 on success
< 0 on error

.. _`ad_marker_send`:

ad_marker_send
==============

.. c:function:: int ad_marker_send(struct port *port, struct bond_marker *marker)

    send marker information/response on a given port

    :param struct port \*port:
        the port we're looking at

    :param struct bond_marker \*marker:
        marker data to send

.. _`ad_marker_send.return`:

Return
------

0 on success
< 0 on error

.. _`ad_mux_machine`:

ad_mux_machine
==============

.. c:function:: void ad_mux_machine(struct port *port, bool *update_slave_arr)

    handle a port's mux state machine

    :param struct port \*port:
        the port we're looking at

    :param bool \*update_slave_arr:
        Does slave array need update?

.. _`ad_rx_machine`:

ad_rx_machine
=============

.. c:function:: void ad_rx_machine(struct lacpdu *lacpdu, struct port *port)

    handle a port's rx State Machine

    :param struct lacpdu \*lacpdu:
        the lacpdu we've received

    :param struct port \*port:
        the port we're looking at

.. _`ad_rx_machine.description`:

Description
-----------

If lacpdu arrived, stop previous timer (if exists) and set the next state as
CURRENT. If timer expired set the state machine in the proper state.
In other cases, this function checks if we need to switch to other state.

.. _`ad_churn_machine`:

ad_churn_machine
================

.. c:function:: void ad_churn_machine(struct port *port)

    handle port churn's state machine

    :param struct port \*port:
        the port we're looking at

.. _`ad_tx_machine`:

ad_tx_machine
=============

.. c:function:: void ad_tx_machine(struct port *port)

    handle a port's tx state machine

    :param struct port \*port:
        the port we're looking at

.. _`ad_periodic_machine`:

ad_periodic_machine
===================

.. c:function:: void ad_periodic_machine(struct port *port)

    handle a port's periodic state machine

    :param struct port \*port:
        the port we're looking at

.. _`ad_periodic_machine.description`:

Description
-----------

Turn ntt flag on priodically to perform periodic transmission of lacpdu's.

.. _`ad_port_selection_logic`:

ad_port_selection_logic
=======================

.. c:function:: void ad_port_selection_logic(struct port *port, bool *update_slave_arr)

    select aggregation groups

    :param struct port \*port:
        the port we're looking at

    :param bool \*update_slave_arr:
        Does slave array need update?

.. _`ad_port_selection_logic.description`:

Description
-----------

Select aggregation groups, and assign each port for it's aggregetor. The
selection logic is called in the inititalization (after all the handshkes),
and after every lacpdu receive (if selected is off).

.. _`ad_agg_selection_logic`:

ad_agg_selection_logic
======================

.. c:function:: void ad_agg_selection_logic(struct aggregator *agg, bool *update_slave_arr)

    select an aggregation group for a team

    :param struct aggregator \*agg:
        *undescribed*

    :param bool \*update_slave_arr:
        Does slave array need update?

.. _`ad_agg_selection_logic.description`:

Description
-----------

It is assumed that only one aggregator may be selected for a team.

The logic of this function is to select the aggregator according to

.. _`ad_agg_selection_logic.bond_ad_stable`:

BOND_AD_STABLE
--------------

select the aggregator with the most ports attached to
it, and to reselect the active aggregator only if the previous
aggregator has no more ports related to it.

.. _`ad_agg_selection_logic.bond_ad_bandwidth`:

BOND_AD_BANDWIDTH
-----------------

select the aggregator with the highest total
bandwidth, and reselect whenever a link state change takes place or the
set of slaves in the bond changes.

.. _`ad_agg_selection_logic.bond_ad_count`:

BOND_AD_COUNT
-------------

select the aggregator with largest number of ports
(slaves), and reselect whenever a link state change takes place or the
set of slaves in the bond changes.

.. _`ad_agg_selection_logic.fixme`:

FIXME
-----

this function MUST be called with the first agg in the bond, or
\__get_active_agg() won't work correctly. This function should be better
called with the bond itself, and retrieve the first agg from it.

.. _`ad_clear_agg`:

ad_clear_agg
============

.. c:function:: void ad_clear_agg(struct aggregator *aggregator)

    clear a given aggregator's parameters

    :param struct aggregator \*aggregator:
        the aggregator we're looking at

.. _`ad_initialize_agg`:

ad_initialize_agg
=================

.. c:function:: void ad_initialize_agg(struct aggregator *aggregator)

    initialize a given aggregator's parameters

    :param struct aggregator \*aggregator:
        the aggregator we're looking at

.. _`ad_initialize_port`:

ad_initialize_port
==================

.. c:function:: void ad_initialize_port(struct port *port, int lacp_fast)

    initialize a given port's parameters

    :param struct port \*port:
        *undescribed*

    :param int lacp_fast:
        boolean. whether fast periodic should be used

.. _`ad_enable_collecting_distributing`:

ad_enable_collecting_distributing
=================================

.. c:function:: void ad_enable_collecting_distributing(struct port *port, bool *update_slave_arr)

    enable a port's transmit/receive

    :param struct port \*port:
        the port we're looking at

    :param bool \*update_slave_arr:
        Does slave array need update?

.. _`ad_enable_collecting_distributing.description`:

Description
-----------

Enable \ ``port``\  if it's in an active aggregator

.. _`ad_disable_collecting_distributing`:

ad_disable_collecting_distributing
==================================

.. c:function:: void ad_disable_collecting_distributing(struct port *port, bool *update_slave_arr)

    disable a port's transmit/receive

    :param struct port \*port:
        the port we're looking at

    :param bool \*update_slave_arr:
        Does slave array need update?

.. _`ad_marker_info_received`:

ad_marker_info_received
=======================

.. c:function:: void ad_marker_info_received(struct bond_marker *marker_info, struct port *port)

    handle receive of a Marker information frame

    :param struct bond_marker \*marker_info:
        Marker info received

    :param struct port \*port:
        the port we're looking at

.. _`ad_marker_response_received`:

ad_marker_response_received
===========================

.. c:function:: void ad_marker_response_received(struct bond_marker *marker, struct port *port)

    handle receive of a marker response frame

    :param struct bond_marker \*marker:
        marker PDU received

    :param struct port \*port:
        the port we're looking at

.. _`ad_marker_response_received.description`:

Description
-----------

This function does nothing since we decided not to implement send and handle
response for marker PDU's, in this stage, but only to respond to marker
information.

.. _`bond_3ad_initiate_agg_selection`:

bond_3ad_initiate_agg_selection
===============================

.. c:function:: void bond_3ad_initiate_agg_selection(struct bonding *bond, int timeout)

    initate aggregator selection

    :param struct bonding \*bond:
        bonding struct

    :param int timeout:
        *undescribed*

.. _`bond_3ad_initiate_agg_selection.description`:

Description
-----------

Set the aggregation selection timer, to initiate an agg selection in
the very near future.  Called during first initialization, and during
any down to up transitions of the bond.

.. _`bond_3ad_initialize`:

bond_3ad_initialize
===================

.. c:function:: void bond_3ad_initialize(struct bonding *bond, u16 tick_resolution)

    initialize a bond's 802.3ad parameters and structures

    :param struct bonding \*bond:
        bonding struct to work on

    :param u16 tick_resolution:
        tick duration (millisecond resolution)

.. _`bond_3ad_initialize.description`:

Description
-----------

Can be called only after the mac address of the bond is set.

.. _`bond_3ad_bind_slave`:

bond_3ad_bind_slave
===================

.. c:function:: void bond_3ad_bind_slave(struct slave *slave)

    initialize a slave's port

    :param struct slave \*slave:
        slave struct to work on

.. _`bond_3ad_bind_slave.return`:

Return
------

0 on success
< 0 on error

.. _`bond_3ad_unbind_slave`:

bond_3ad_unbind_slave
=====================

.. c:function:: void bond_3ad_unbind_slave(struct slave *slave)

    deinitialize a slave's port

    :param struct slave \*slave:
        slave struct to work on

.. _`bond_3ad_unbind_slave.description`:

Description
-----------

Search for the aggregator that is related to this port, remove the
aggregator and assign another aggregator for other port related to it
(if any), and remove the port.

.. _`bond_3ad_update_ad_actor_settings`:

bond_3ad_update_ad_actor_settings
=================================

.. c:function:: void bond_3ad_update_ad_actor_settings(struct bonding *bond)

    reflect change of actor settings to ports

    :param struct bonding \*bond:
        bonding struct to work on

.. _`bond_3ad_update_ad_actor_settings.description`:

Description
-----------

If an ad_actor setting gets changed we need to update the individual port
settings so the bond device will use the new values when it gets upped.

.. _`bond_3ad_state_machine_handler`:

bond_3ad_state_machine_handler
==============================

.. c:function:: void bond_3ad_state_machine_handler(struct work_struct *work)

    handle state machines timeout

    :param struct work_struct \*work:
        *undescribed*

.. _`bond_3ad_state_machine_handler.description`:

Description
-----------

The state machine handling concept in this module is to check every tick
which state machine should operate any function. The execution order is
round robin, so when we have an interaction between state machines, the
reply of one to each other might be delayed until next tick.

This function also complete the initialization when the agg_select_timer
times out, and it selects an aggregator for the ports that are yet not
related to any aggregator, and selects the active aggregator for a bond.

.. _`bond_3ad_rx_indication`:

bond_3ad_rx_indication
======================

.. c:function:: int bond_3ad_rx_indication(struct lacpdu *lacpdu, struct slave *slave, u16 length)

    handle a received frame

    :param struct lacpdu \*lacpdu:
        received lacpdu

    :param struct slave \*slave:
        slave struct to work on

    :param u16 length:
        length of the data received

.. _`bond_3ad_rx_indication.description`:

Description
-----------

It is assumed that frames that were sent on this NIC don't returned as new
received frames (loopback). Since only the payload is given to this
function, it check for loopback.

.. _`ad_update_actor_keys`:

ad_update_actor_keys
====================

.. c:function:: void ad_update_actor_keys(struct port *port, bool reset)

    Update the oper / admin keys for a port based on its current speed and duplex settings.

    :param struct port \*port:
        the port we'are looking at

    :param bool reset:
        Boolean to just reset the speed and the duplex part of the key

.. _`ad_update_actor_keys.description`:

Description
-----------

The logic to change the oper / admin keys is:
(a) A full duplex port can participate in LACP with partner.
(b) When the speed is changed, LACP need to be reinitiated.

.. _`bond_3ad_adapter_speed_duplex_changed`:

bond_3ad_adapter_speed_duplex_changed
=====================================

.. c:function:: void bond_3ad_adapter_speed_duplex_changed(struct slave *slave)

    handle a slave's speed / duplex change indication

    :param struct slave \*slave:
        slave struct to work on

.. _`bond_3ad_adapter_speed_duplex_changed.description`:

Description
-----------

Handle reselection of aggregator (if needed) for this port.

.. _`bond_3ad_handle_link_change`:

bond_3ad_handle_link_change
===========================

.. c:function:: void bond_3ad_handle_link_change(struct slave *slave, char link)

    handle a slave's link status change indication

    :param struct slave \*slave:
        slave struct to work on

    :param char link:
        *undescribed*

.. _`bond_3ad_handle_link_change.description`:

Description
-----------

Handle reselection of aggregator (if needed) for this port.

.. _`bond_3ad_set_carrier`:

bond_3ad_set_carrier
====================

.. c:function:: int bond_3ad_set_carrier(struct bonding *bond)

    set link state for bonding master \ ``bond``\  - bonding structure

    :param struct bonding \*bond:
        *undescribed*

.. _`bond_3ad_set_carrier.description`:

Description
-----------

if we have an active aggregator, we're up, if not, we're down.
Presumes that we cannot have an active aggregator if there are
no slaves with link up.

This behavior complies with IEEE 802.3 section 43.3.9.

Called by \ :c:func:`bond_set_carrier`\ . Return zero if carrier state does not
change, nonzero if it does.

.. _`__bond_3ad_get_active_agg_info`:

__bond_3ad_get_active_agg_info
==============================

.. c:function:: int __bond_3ad_get_active_agg_info(struct bonding *bond, struct ad_info *ad_info)

    get information of the active aggregator

    :param struct bonding \*bond:
        bonding struct to work on

    :param struct ad_info \*ad_info:
        ad_info struct to fill with the bond's info

.. _`__bond_3ad_get_active_agg_info.return`:

Return
------

0 on success
< 0 on error

.. _`bond_3ad_update_lacp_rate`:

bond_3ad_update_lacp_rate
=========================

.. c:function:: void bond_3ad_update_lacp_rate(struct bonding *bond)

    change the lacp rate \ ``bond``\  - bonding struct

    :param struct bonding \*bond:
        *undescribed*

.. _`bond_3ad_update_lacp_rate.description`:

Description
-----------

When modify lacp_rate parameter via sysfs,
update actor_oper_port_state of each port.

Hold bond->mode_lock,
so we can modify port->actor_oper_port_state,
no matter bond is up or down.

.. This file was automatic generated / don't edit.

