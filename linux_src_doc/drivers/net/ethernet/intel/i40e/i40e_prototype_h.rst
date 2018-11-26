.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40e/i40e_prototype.h

.. _`i40e_virtchnl_link_speed`:

i40e_virtchnl_link_speed
========================

.. c:function:: enum virtchnl_link_speed i40e_virtchnl_link_speed(enum i40e_aq_link_speed link_speed)

    Convert AdminQ link_speed to virtchnl definition

    :param link_speed:
        the speed to convert
    :type link_speed: enum i40e_aq_link_speed

.. _`i40e_virtchnl_link_speed.description`:

Description
-----------

Returns the link_speed in terms of the virtchnl interface, for use in
converting link_speed as reported by the AdminQ into the format used for
talking to virtchnl devices. If we can't represent the link speed properly,
report LINK_SPEED_UNKNOWN.

.. This file was automatic generated / don't edit.

