.. -*- coding: utf-8; mode: rst -*-

===================
scsi_transport_fc.h
===================


.. _`fc_remote_port_chkready`:

fc_remote_port_chkready
=======================

.. c:function:: int fc_remote_port_chkready (struct fc_rport *rport)

    called to validate the remote port state prior to initiating io to the port.

    :param struct fc_rport \*rport:
        remote port to be checked



.. _`fc_remote_port_chkready.description`:

Description
-----------


Returns a scsi result code that can be returned by the LLDD.



.. _`fc_vport_set_state`:

fc_vport_set_state
==================

.. c:function:: void fc_vport_set_state (struct fc_vport *vport, enum fc_vport_state new_state)

    called to set a vport's state. Saves the old state, excepting the transitory states of initializing and sending the ELS traffic to instantiate the vport on the link.

    :param struct fc_vport \*vport:
        virtual port whose state is changing

    :param enum fc_vport_state new_state:
        new state



.. _`fc_vport_set_state.description`:

Description
-----------


Assumes the driver has surrounded this with the proper locking to ensure
a coherent state change.

