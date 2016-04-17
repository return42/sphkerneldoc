
.. _fe-type-t:

=============
Frontend type
=============

For historical reasons, frontend types are named by the type of modulation used in transmission. The fontend types are given by fe_type_t type, defined as:


.. _fe-type:

.. table:: Frontend types

    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | fe_type                                                             | Description            | :ref:`DTV_DELIVERY_SYSTEM    <DTV-DELIVERY-SYSTEM>`  equivalent type                       |
    +=====================================================================+========================+============================================================================================+
    | ``FE_QPSK``                                                         | For DVB-S standard     | ``SYS_DVBS``                                                                               |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``FE_QAM``                                                          | For DVB-C annex A      | ``SYS_DVBC_ANNEX_A``                                                                       |
    |                                                                     | standard               |                                                                                            |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``FE_OFDM``                                                         | For DVB-T standard     | ``SYS_DVBT``                                                                               |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+
    | ``FE_ATSC``                                                         | For ATSC standard      | ``SYS_ATSC`` (terrestrial) or ``SYS_DVBC_ANNEX_B`` (cable)                                 |
    |                                                                     | (terrestrial) or for   |                                                                                            |
    |                                                                     | DVB-C Annex B (cable)  |                                                                                            |
    |                                                                     | used in US.            |                                                                                            |
    +---------------------------------------------------------------------+------------------------+--------------------------------------------------------------------------------------------+


Newer formats like DVB-S2, ISDB-T, ISDB-S and DVB-T2 are not described at the above, as they're supported via the new
:ref:`FE_GET_PROPERTY/FE_GET_SET_PROPERTY <FE_GET_PROPERTY>` ioctl's, using the :ref:`DTV_DELIVERY_SYSTEM <DTV-DELIVERY-SYSTEM>` parameter.

In the old days, struct :ref:`dvb_frontend_info <dvb-frontend-info>` used to contain ``fe_type_t`` field to indicate the delivery systems, filled with either FE_QPSK, FE_QAM,
FE_OFDM or FE_ATSC. While this is still filled to keep backward compatibility, the usage of this field is deprecated, as it can report just one delivery system, but some devices
support multiple delivery systems. Please use :ref:`DTV_ENUM_DELSYS <DTV-ENUM-DELSYS>` instead.

On devices that support multiple delivery systems, struct :ref:`dvb_frontend_info <dvb-frontend-info>`::``fe_type_t`` is filled with the currently standard, as selected by the
last call to :ref:`FE_SET_PROPERTY <FE_GET_PROPERTY>` using the :ref:`DTV_DELIVERY_SYSTEM <DTV-DELIVERY-SYSTEM>` property.
