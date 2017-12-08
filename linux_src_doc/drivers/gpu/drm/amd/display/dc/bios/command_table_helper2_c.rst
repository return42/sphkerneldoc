.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/display/dc/bios/command_table_helper2.c

.. _`dal_cmd_table_helper_transmitter_bp_to_atom2`:

dal_cmd_table_helper_transmitter_bp_to_atom2
============================================

.. c:function:: uint8_t dal_cmd_table_helper_transmitter_bp_to_atom2(enum transmitter t)

    :param enum transmitter t:
        *undescribed*

.. _`dal_cmd_table_helper_transmitter_bp_to_atom2.description`:

Description
-----------

@brief
Translate the Transmitter to the corresponding ATOM BIOS value

\ ``param``\ 
input transmitter
output digitalTransmitter
// =00: Digital Transmitter1 ( UNIPHY linkAB )
// =01: Digital Transmitter2 ( UNIPHY linkCD )
// =02: Digital Transmitter3 ( UNIPHY linkEF )

.. This file was automatic generated / don't edit.

