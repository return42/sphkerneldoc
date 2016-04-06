
.. _frontend_legacy_types:

Frontend Legacy Data Types
==========================


.. _fe-type-t:

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


.. _fe-bandwidth-t:

Frontend bandwidth
==================


.. _fe-bandwidth:

.. table:: enum fe_bandwidth

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ID                                                                                         | Description                                                                                |
    +============================================================================================+============================================================================================+
    | ``BANDWIDTH_AUTO``                                                                         | Autodetect bandwidth (if supported)                                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``BANDWIDTH_1_712_MHZ``                                                                    | 1.712 MHz                                                                                  |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``BANDWIDTH_5_MHZ``                                                                        | 5 MHz                                                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``BANDWIDTH_6_MHZ``                                                                        | 6 MHz                                                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``BANDWIDTH_7_MHZ``                                                                        | 7 MHz                                                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``BANDWIDTH_8_MHZ``                                                                        | 8 MHz                                                                                      |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | ``BANDWIDTH_10_MHZ``                                                                       | 10 MHz                                                                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _dvb-frontend-parameters:

frontend parameters
===================

The kind of parameters passed to the frontend device for tuning depend on the kind of hardware you are using.

The struct ``dvb_frontend_parameters`` uses an union with specific per-system parameters. However, as newer delivery systems required more data, the structure size weren't enough
to fit, and just extending its size would break the existing applications. So, those parameters were replaced by the usage of
:ref:`FE_GET_PROPERTY/FE_SET_PROPERTY <FE_GET_PROPERTY>` ioctl's. The new API is flexible enough to add new parameters to existing delivery systems, and to add newer
delivery systems.

So, newer applications should use :ref:`FE_GET_PROPERTY/FE_SET_PROPERTY <FE_GET_PROPERTY>` instead, in order to be able to support the newer System Delivery like DVB-S2,
DVB-T2, DVB-C2, ISDB, etc.

All kinds of parameters are combined as an union in the FrontendParameters structure:


.. code-block:: c

    struct dvb_frontend_parameters {
        uint32_t frequency;     /* (absolute) frequency in Hz for QAM/OFDM */
                    /* intermediate frequency in kHz for QPSK */
        fe_spectral_inversion_t inversion;
        union {
            struct dvb_qpsk_parameters qpsk;
            struct dvb_qam_parameters  qam;
            struct dvb_ofdm_parameters ofdm;
            struct dvb_vsb_parameters  vsb;
        } u;
    };

In the case of QPSK frontends the ``frequency`` field specifies the intermediate frequency, i.e. the offset which is effectively added to the local oscillator frequency (LOF) of
the LNB. The intermediate frequency has to be specified in units of kHz. For QAM and OFDM frontends the ``frequency`` specifies the absolute frequency and is given in Hz.


.. _dvb-qpsk-parameters:

QPSK parameters
===============

For satellite QPSK frontends you have to use the ``dvb_qpsk_parameters`` structure:


.. code-block:: c

     struct dvb_qpsk_parameters {
         uint32_t        symbol_rate;  /* symbol rate in Symbols per second */
         fe_code_rate_t  fec_inner;    /* forward error correction (see above) */
     };


.. _dvb-qam-parameters:

QAM parameters
==============

for cable QAM frontend you use the ``dvb_qam_parameters`` structure:


.. code-block:: c

     struct dvb_qam_parameters {
         uint32_t         symbol_rate; /* symbol rate in Symbols per second */
         fe_code_rate_t   fec_inner;   /* forward error correction (see above) */
         fe_modulation_t  modulation;  /* modulation type (see above) */
     };


.. _dvb-vsb-parameters:

VSB parameters
==============

ATSC frontends are supported by the ``dvb_vsb_parameters`` structure:


.. code-block:: c

    struct dvb_vsb_parameters {
        fe_modulation_t modulation; /* modulation type (see above) */
    };


.. _dvb-ofdm-parameters:

OFDM parameters
===============

DVB-T frontends are supported by the ``dvb_ofdm_parameters`` structure:


.. code-block:: c

     struct dvb_ofdm_parameters {
         fe_bandwidth_t      bandwidth;
         fe_code_rate_t      code_rate_HP;  /* high priority stream code rate */
         fe_code_rate_t      code_rate_LP;  /* low priority stream code rate */
         fe_modulation_t     constellation; /* modulation type (see above) */
         fe_transmit_mode_t  transmission_mode;
         fe_guard_interval_t guard_interval;
         fe_hierarchy_t      hierarchy_information;
     };


.. _dvb-frontend-event:

frontend events
===============


.. code-block:: c

     struct dvb_frontend_event {
         fe_status_t status;
         struct dvb_frontend_parameters parameters;
     };


.. _frontend_legacy_fcalls:

Frontend Legacy Function Calls
==============================

Those functions are defined at DVB version 3. The support is kept in the kernel due to compatibility issues only. Their usage is strongly not recommended


.. _FE_READ_BER:

FE_READ_BER
===========

DESCRIPTION

This ioctl call returns the bit error rate for the signal currently received/demodulated by the front-end. For this command, read-only access to the device is sufficient.

SYNOPSIS

int ioctl(int fd, int request = :ref:`FE_READ_BER <FE_READ_BER>`, uint32_t ⋆ber);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals :ref:`FE_READ_BER    <FE_READ_BER>`    for this command.                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | uint32_t  ⋆ber                                                                             | The bit error rate is stored into ⋆ber.                                                    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _FE_READ_SNR:

FE_READ_SNR
===========

DESCRIPTION

This ioctl call returns the signal-to-noise ratio for the signal currently received by the front-end. For this command, read-only access to the device is sufficient.

SYNOPSIS

int ioctl(int fd, int request = :ref:`FE_READ_SNR <FE_READ_SNR>`, uint16_t ⋆snr);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals :ref:`FE_READ_SNR    <FE_READ_SNR>`    for this command.                            |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | uint16_t  ⋆snr                                                                             | The signal-to-noise ratio is stored into ⋆snr.                                             |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _FE_READ_SIGNAL_STRENGTH:

FE_READ_SIGNAL_STRENGTH
=======================

DESCRIPTION

This ioctl call returns the signal strength value for the signal currently received by the front-end. For this command, read-only access to the device is sufficient.

SYNOPSIS

int ioctl( int fd, int request = :ref:`FE_READ_SIGNAL_STRENGTH <FE_READ_SIGNAL_STRENGTH>`, uint16_t ⋆strength);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals :ref:`FE_READ_SIGNAL_STRENGTH     <FE_READ_SIGNAL_STRENGTH>`     for this command.  |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | uint16_t  ⋆strength                                                                        | The signal strength value is stored into ⋆strength.                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _FE_READ_UNCORRECTED_BLOCKS:

FE_READ_UNCORRECTED_BLOCKS
==========================

DESCRIPTION

This ioctl call returns the number of uncorrected blocks detected by the device driver during its lifetime. For meaningful measurements, the increment in block count during a
specific time interval should be calculated. For this command, read-only access to the device is sufficient.

Note that the counter will wrap to zero after its maximum count has been reached.

SYNOPSIS

int ioctl( int fd, int request = :ref:`FE_READ_UNCORRECTED_BLOCKS <FE_READ_UNCORRECTED_BLOCKS>`, uint32_t ⋆ublocks);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals :ref:`FE_READ_UNCORRECTED_BLOCKS     <FE_READ_UNCORRECTED_BLOCKS>`     for this     |
    |                                                                                            | command.                                                                                   |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | uint32_t  ⋆ublocks                                                                         | The total number of uncorrected blocks seen by the driver so far.                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.


.. _FE_SET_FRONTEND:

FE_SET_FRONTEND
===============

DESCRIPTION

This ioctl call starts a tuning operation using specified parameters. The result of this call will be successful if the parameters were valid and the tuning could be initiated. The
result of the tuning operation in itself, however, will arrive asynchronously as an event (see documentation for :ref:`FE_GET_EVENT <FE_GET_EVENT>` and FrontendEvent.) If a
new :ref:`FE_SET_FRONTEND <FE_SET_FRONTEND>` operation is initiated before the previous one was completed, the previous operation will be aborted in favor of the new one.
This command requires read/write access to the device.

SYNOPSIS

int ioctl(int fd, int request = :ref:`FE_SET_FRONTEND <FE_SET_FRONTEND>`, struct dvb_frontend_parameters ⋆p);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals :ref:`FE_SET_FRONTEND    <FE_SET_FRONTEND>`    for this command.                    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | struct dvb_frontend_parameters   ⋆p                                                        | Points to parameters for tuning operation.                                                 |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EINVAL                                                                                     | Maximum supported symbol rate reached.                                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _FE_GET_FRONTEND:

FE_GET_FRONTEND
===============

DESCRIPTION

This ioctl call queries the currently effective frontend parameters. For this command, read-only access to the device is sufficient.

SYNOPSIS

int ioctl(int fd, int request = :ref:`FE_GET_FRONTEND <FE_GET_FRONTEND>`, struct dvb_frontend_parameters ⋆p);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals :ref:`FE_SET_FRONTEND    <FE_SET_FRONTEND>`    for this command.                    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | struct dvb_frontend_parameters   ⋆p                                                        | Points to parameters for tuning operation.                                                 |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EINVAL                                                                                     | Maximum supported symbol rate reached.                                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _FE_GET_EVENT:

FE_GET_EVENT
============

DESCRIPTION

This ioctl call returns a frontend event if available. If an event is not available, the behavior depends on whether the device is in blocking or non-blocking mode. In the latter
case, the call fails immediately with errno set to EWOULDBLOCK. In the former case, the call blocks until an event becomes available.

The standard Linux poll() and/or select() system calls can be used with the device file descriptor to watch for new events. For select(), the file descriptor should be included in
the exceptfds argument, and for poll(), POLLPRI should be specified as the wake-up condition. Since the event queue allocated is rather small (room for 8 events), the queue must be
serviced regularly to avoid overflow. If an overflow happens, the oldest event is discarded from the queue, and an error (EOVERFLOW) occurs the next time the queue is read. After
reporting the error condition in this fashion, subsequent :ref:`FE_GET_EVENT <FE_GET_EVENT>` calls will return events from the queue as usual.

For the sake of implementation simplicity, this command requires read/write access to the device.

SYNOPSIS

int ioctl(int fd, int request = QPSK_GET_EVENT, struct dvb_frontend_event ⋆ev);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int fd                                                                                     | File descriptor returned by a previous call to open().                                     |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | int request                                                                                | Equals :ref:`FE_GET_EVENT    <FE_GET_EVENT>`    for this command.                          |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | struct dvb_frontend_event   ⋆ev                                                            | Points to the location where the event,                                                    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    |                                                                                            | if any, is to be stored.                                                                   |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EWOULDBLOCK                                                                                | There is no event pending, and the device is in non-blocking mode.                         |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | EOVERFLOW                                                                                  | Overflow in event queue - one or more events were lost.                                    |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+



.. _FE_DISHNETWORK_SEND_LEGACY_CMD:

FE_DISHNETWORK_SEND_LEGACY_CMD
==============================

DESCRIPTION

WARNING: This is a very obscure legacy command, used only at stv0299 driver. Should not be used on newer drivers.

It provides a non-standard method for selecting Diseqc voltage on the frontend, for Dish Network legacy switches.

As support for this ioctl were added in 2004, this means that such dishes were already legacy in 2004.

SYNOPSIS

int ioctl(int fd, int request = :ref:`FE_DISHNETWORK_SEND_LEGACY_CMD <FE_DISHNETWORK_SEND_LEGACY_CMD>`, unsigned long cmd);

PARAMETERS



.. table::

    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
    | unsigned long cmd                                                                          | sends the specified raw cmd to the dish via DISEqC.                                        |
    +--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


RETURN VALUE

On success 0 is returned, on error -1 and the ``errno`` variable is set appropriately. The generic error codes are described at the :ref:`Generic Error Codes <gen-errors>`
chapter.
