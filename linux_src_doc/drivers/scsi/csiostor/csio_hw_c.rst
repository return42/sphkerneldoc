.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/csiostor/csio_hw.c

.. _`fwcap_to_fwspeed`:

fwcap_to_fwspeed
================

.. c:function:: fw_port_cap32_t fwcap_to_fwspeed(fw_port_cap32_t acaps)

    return highest speed in Port Capabilities

    :param fw_port_cap32_t acaps:
        advertised Port Capabilities

.. _`fwcap_to_fwspeed.description`:

Description
-----------

Get the highest speed for the port from the advertised Port
Capabilities.

.. _`fwcaps16_to_caps32`:

fwcaps16_to_caps32
==================

.. c:function:: fw_port_cap32_t fwcaps16_to_caps32(fw_port_cap16_t caps16)

    convert 16-bit Port Capabilities to 32-bits

    :param fw_port_cap16_t caps16:
        a 16-bit Port Capabilities value

.. _`fwcaps16_to_caps32.description`:

Description
-----------

Returns the equivalent 32-bit Port Capabilities value.

.. _`lstatus_to_fwcap`:

lstatus_to_fwcap
================

.. c:function:: fw_port_cap32_t lstatus_to_fwcap(u32 lstatus)

    translate old lstatus to 32-bit Port Capabilities

    :param u32 lstatus:
        old FW_PORT_ACTION_GET_PORT_INFO lstatus value

.. _`lstatus_to_fwcap.description`:

Description
-----------

Translates old FW_PORT_ACTION_GET_PORT_INFO lstatus field into new
32-bit Port Capabilities value.

.. _`csio_init_link_config`:

csio_init_link_config
=====================

.. c:function:: void csio_init_link_config(struct link_config *lc, fw_port_cap32_t pcaps, fw_port_cap32_t acaps)

    initialize a link's SW state

    :param struct link_config \*lc:
        pointer to structure holding the link state

    :param fw_port_cap32_t pcaps:
        link Port Capabilities

    :param fw_port_cap32_t acaps:
        link current Advertised Port Capabilities

.. _`csio_init_link_config.description`:

Description
-----------

Initializes the SW state maintained for each link, including the link's
capabilities and default speed/flow-control/autonegotiation settings.

.. _`csio_hw_start`:

csio_hw_start
=============

.. c:function:: int csio_hw_start(struct csio_hw *hw)

    Kicks off the HW State machine

    :param struct csio_hw \*hw:
        Pointer to HW module.

.. _`csio_hw_start.description`:

Description
-----------

It is assumed that the initialization is a synchronous operation.
So when we return afer posting the event, the HW SM should be in
the ready state, if there were no errors during init.

.. _`csio_hw_reset`:

csio_hw_reset
=============

.. c:function:: int csio_hw_reset(struct csio_hw *hw)

    Reset the hardware

    :param struct csio_hw \*hw:
        HW module.

.. _`csio_hw_reset.description`:

Description
-----------

Caller should hold lock across this function.

.. _`csio_hw_init`:

csio_hw_init
============

.. c:function:: int csio_hw_init(struct csio_hw *hw)

    Initialize HW module.

    :param struct csio_hw \*hw:
        Pointer to HW module.

.. _`csio_hw_init.description`:

Description
-----------

Initialize the members of the HW module.

.. _`csio_hw_exit`:

csio_hw_exit
============

.. c:function:: void csio_hw_exit(struct csio_hw *hw)

    Un-initialize HW module.

    :param struct csio_hw \*hw:
        Pointer to HW module.

.. This file was automatic generated / don't edit.

